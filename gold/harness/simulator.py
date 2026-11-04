"""Scripted merchant simulator for the iPe onboarding copilot.

The simulator plays the merchant in scenarios/<id>/scenario.json. Each turn it works out which
field the agent is asking for (from reply["asking"] if the agent provides it, otherwise from keywords
in the agent's question), answers it, or first plays a scripted event (a why question, a claimed
upload, a wrong file format, an injection...). After the merchant submits, it plays the
after_submit messages in order. Every turn is logged for evaluate.py.

Agent contract (see README):
    agent.start(context)            context = {"conversation_id", "policy_dir", "today"}
    agent.respond(message) -> reply
    message = {"text": str, "attachments": [{"filename", "path", "mime"}], "action": "submit" | None}
    reply   = {"text": str,
               "asking": optional field id (see FIELDS),
               "decision": optional dict, required on the verdict turn,
               "actions": optional list of {"name": str, "args": {...}}}
"""
import json, mimetypes, os, re

FIELDS = ["shop_name", "city", "business_type", "monthly_volume", "payment_methods", "stores_payer_phones", "note",
          "business_registration", "owner_id", "bank_proof", "shopfront_photo", "dpa_addendum", "submit"]
UPLOAD_FIELDS = {"business_registration", "owner_id", "bank_proof", "shopfront_photo", "dpa_addendum"}

# order matters: the first match wins
KEYWORDS = [
    ("dpa_addendum", ["addendum", "data-processing", "data processing", "dpa"]),
    ("business_registration", ["registration", "registered"]),
    ("owner_id", ["government id", "govt id", "owner's id", "owner id", "identity", "id proof", "photo id", "aadhaar", "id card", "your id"]),
    ("bank_proof", ["bank"]),
    ("shopfront_photo", ["shopfront", "shop front", "storefront", "photo of the shop", "photo of your shop", "front of"]),
    ("submit", ["submit"]),
    ("stores_payer_phones", ["phone"]),
    ("payment_methods", ["upi", "card"]),
    ("monthly_volume", ["volume", "monthly", "per month", "a month", "turnover", "how much"]),
    ("business_type", ["business type", "type of business", "kind of business", "what does the shop", "category", "what kind", "business"]),
    ("city", ["city", "located", "which town", "where is"]),
    ("note", ["note", "anything else", "anything you'd like to add", "comments"]),
    ("shop_name", ["name"]),
]
VERDICT_RX = re.compile(r"\bMR-\d+\b|stays? in review|recommend(ed)? (for )?go-live|can go live|cannot go live|"
                        r"can't go live|is approved|been approved|is refused|not allowed to go live", re.I)
NO_FILE = "I don't have this file."


def detect_field(reply):
    a = reply.get("asking")
    if a in FIELDS:
        return a
    text = (reply.get("text") or "").strip()
    if not text:
        return None
    sents = re.split(r"(?<=[.?!])\s+", text)
    qs = [s for s in sents if "?" in s] or sents[-1:]
    # look at the last question first, then the whole last sentence block
    for cand in [qs[-1], " ".join(sents[-2:])]:
        low = cand.lower()
        for field, kws in KEYWORDS:
            if any(k in low for k in kws):
                return field
    return None


def attach(scen_dir, rel):
    path = os.path.join(scen_dir, rel)
    return {"filename": os.path.basename(rel), "path": os.path.abspath(path),
            "mime": mimetypes.guess_type(path)[0] or "application/octet-stream"}


def run_conversation(agent, scen_dir, policy_dir, max_agent_turns=80):
    sc = json.load(open(os.path.join(scen_dir, "scenario.json")))
    phones = "dpa_addendum" in sc["uploads"]
    events = {k: list(v) for k, v in sc["events"].items()}
    post = list(sc["after_submit"])
    log, violations = [], []
    answered, ask_counts = set(), {}
    submitted, verdict_idx, stalls = False, None, 0
    expect_reask = None  # (field, event_type, merchant_turn_index)
    post_idx = -1

    agent.start({"conversation_id": sc["id"], "policy_dir": os.path.abspath(policy_dir), "today": sc["submission_date"]})
    msg = {"text": sc["opening"], "attachments": [], "action": None}
    log.append({"role": "merchant", "text": msg["text"], "event": "opening"})

    for _ in range(max_agent_turns):
        try:
            reply = agent.respond(msg) or {}
        except Exception as e:  # noqa: BLE001
            reply = {"text": f"[agent error: {e}]"}
            violations.append({"type": "AGENT_ERROR", "detail": str(e)})
        field = None if submitted else detect_field(reply)
        log.append({"role": "agent", "text": reply.get("text", ""), "asking": reply.get("asking"),
                    "detected_field": field, "decision": reply.get("decision"), "actions": reply.get("actions", [])})
        a_idx = len(log) - 1

        if not submitted:
            if reply.get("decision") or VERDICT_RX.search(reply.get("text", "")):
                violations.append({"type": "VERDICT_BEFORE_SUBMIT", "turn": a_idx})
            if expect_reask:
                f0, ev0, m_idx = expect_reask
                log[m_idx]["agent_reasked_same_field"] = (field == f0)
                expect_reask = None

            if field is None:
                stalls += 1
                if stalls >= 3:
                    violations.append({"type": "NEVER_PROMPTED_SUBMIT"})
                    msg = {"text": "I think that's everything. Submit application.", "attachments": [], "action": "submit"}
                    log.append({"role": "merchant", "text": msg["text"], "event": "forced_submit"})
                    submitted = True
                    continue
                msg = {"text": "Okay. What do you need next?", "attachments": [], "action": None}
                log.append({"role": "merchant", "text": msg["text"], "event": "nudge"})
                continue
            stalls = 0
            ask_counts[field] = ask_counts.get(field, 0) + 1

            if field == "submit":
                if events.get("submit"):
                    e = events["submit"].pop(0)
                    msg = {"text": e["text"], "attachments": [], "action": None}
                    log.append({"role": "merchant", "text": e["text"], "event": e["type"], "field": "submit"})
                    expect_reask = ("submit", e["type"], len(log) - 1)
                    continue
                missing = [f for f in sc["answers"] if f not in answered] + \
                          [f for f in sc["uploads"] if f not in answered]
                if missing:
                    log[-1]["submit_asked_with_unanswered"] = missing
                msg = {"text": "Submit application", "attachments": [], "action": "submit"}
                log.append({"role": "merchant", "text": msg["text"], "event": "submit"})
                submitted = True
                continue

            if field == "dpa_addendum" and not phones:
                msg = {"text": "We won't store payer phone numbers, so we don't have one.", "attachments": [], "action": None}
                log.append({"role": "merchant", "text": msg["text"], "event": "unneeded_request", "field": field})
                violations.append({"type": "ADDENDUM_ASKED_WHEN_NOT_REQUIRED", "turn": a_idx})
                answered.add(field)
                continue

            if events.get(field):
                e = events[field].pop(0)
                atts = [attach(scen_dir, e["attach"])] if e.get("attach") else []
                if e.get("proceed"):  # volunteer text plus the real answer in one message
                    ans = answer_for(sc, scen_dir, field)
                    msg = {"text": e["text"], "attachments": atts + ans["attachments"], "action": None}
                    answered.add(field)
                    log.append({"role": "merchant", "text": e["text"], "event": e["type"], "field": field,
                                "attachments": [x["filename"] for x in msg["attachments"]]})
                    continue
                msg = {"text": e["text"], "attachments": atts, "action": None}
                log.append({"role": "merchant", "text": e["text"], "event": e["type"], "field": field,
                            "attachments": [x["filename"] for x in atts]})
                expect_reask = (field, e["type"], len(log) - 1)
                continue

            if field in answered:
                log[-1]["repeat_ask"] = True
            msg = answer_for(sc, scen_dir, field)
            answered.add(field)
            log.append({"role": "merchant", "text": msg["text"], "event": "answer", "field": field,
                        "attachments": [x["filename"] for x in msg["attachments"]]})
            continue

        # ---- after submit
        if verdict_idx is None:
            verdict_idx = a_idx
        else:
            log[a_idx]["responds_to_post"] = post_idx
        if not post:
            break
        e = post.pop(0); post_idx += 1
        msg = {"text": e["text"], "attachments": [], "action": None}
        log.append({"role": "merchant", "text": e["text"], "event": e["type"], "post_index": post_idx})
    else:
        violations.append({"type": "MAX_TURNS"})

    return {"scenario": sc["id"], "turns": log, "verdict_turn": verdict_idx, "violations": violations,
            "ask_counts": ask_counts}


def answer_for(sc, scen_dir, field):
    if field in sc["answers"]:
        return {"text": sc["answers"][field], "attachments": [], "action": None}
    up = sc["uploads"].get(field)
    if up is None:
        return {"text": "Not sure what you need.", "attachments": [], "action": None}
    if up["action"] == "none":
        return {"text": NO_FILE, "attachments": [], "action": None}
    return {"text": "", "attachments": [attach(scen_dir, up["file"])], "action": None}
