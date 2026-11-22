"""Reference labeller: expected verifier results and expected verdict.

This is test tooling, not the ONB service. It restates the ADR-0001 §5 rule
pipeline and ONB-ANX-001 so every synthetic application carries a label that
was computed in code, never written by the language model.

The real ONB service (onb-svc) must reach the same verdict on the same inputs;
a disagreement is a bug in one of the two and should be raised, not patched
into the labels.
"""

from __future__ import annotations

CEILING_INR = 40_00_000  # ONB-POL-002: inclusive -> Merchant Risk Lead

PACK = ["business_registration", "owner_id", "bank_proof", "shopfront_photo"]
ADDENDUM = "dpa_addendum"

# Closed list of verifier reason codes (see docs/LLD-document-verifier.md §4).
REASONS = {
    "ACCEPTED",
    "FORMAT_UNSUPPORTED",   # ANX-001 §5: not PDF/JPG/PNG, or bytes do not match the extension
    "FILE_UNREADABLE",      # ANX-001 §5: 0-byte, corrupt, password-protected
    "WRONG_DOCUMENT",       # not the document for this slot (utility bill as bank proof, ...)
    "NAME_MISMATCH",        # bank proof / addendum not in the shop's legal name
    "PHOTO_TOO_OLD",        # shopfront taken 91+ days before submit (POL-001 §2.5)
    "NOT_SHOPFRONT",        # interior, render, website, menu board, street-view
    "UNSIGNED",             # addendum unsigned / blank block / initials only
}


def required_slots(payer_phones: bool) -> list[str]:
    return PACK + ([ADDENDUM] if payer_phones else [])


def final_slot_state(attempts: list[dict]) -> str:
    """A slot is accepted if any upload was accepted. Otherwise the merchant said
    they do not have it (or never uploaded), and the slot is missing."""
    return "accepted" if any(a["expected"]["accepted"] for a in attempts) else "missing"


def verdict(app: dict) -> dict:
    """Expected ONB verdict object (ADR-0001 §6) for one application."""
    biz = app["business"]
    payer_phones = app["answers"]["stores_payer_phones"]
    volume = app["answers"]["monthly_volume_inr"]
    injection = bool(app.get("injection"))

    if biz["bucket"] == "refused":
        cites = ["ONB-POL-001 §3"]
        if injection:
            cites.append("ONB-POL-003 §3")
        return {
            "outcome": "REFUSED",
            "business_type_allowed": False,
            "missing_items": [],
            "addendum_required": payer_phones,
            "volume_inr": volume,
            "assignee": None,
            "review_id": None,
            "citations": cites,
            "injection_flagged": injection,
            "policy_conflict_noted": False,
        }

    states = {s: final_slot_state(app["slots"].get(s, [])) for s in required_slots(payer_phones)}
    missing = [s for s, st in states.items() if st != "accepted"]
    permitted = biz["bucket"] == "permitted"
    above = volume > CEILING_INR

    outcome = "RECOMMEND_GO_LIVE" if permitted and not missing else "IN_REVIEW"
    cites = ["ONB-POL-001 §3"]
    if missing:
        cites.append("ONB-POL-001 §2")
    if above:
        cites += ["ONB-POL-002", "ONB-POL-001 §4"]
    if payer_phones:
        cites.append("ONB-POL-003 §2")
    if injection:
        cites.append("ONB-POL-003 §3")

    return {
        "outcome": outcome,
        "business_type_allowed": permitted,
        "missing_items": missing,
        "addendum_required": payer_phones,
        "volume_inr": volume,
        "assignee": "HEAD_OF_PAYMENTS" if above else "MERCHANT_RISK_LEAD",
        "review_id": "<allocated once by ONB>",
        "citations": cites,
        "injection_flagged": injection,
        "policy_conflict_noted": above,
    }

