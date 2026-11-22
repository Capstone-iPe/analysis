"""Thin client for the hosted <=8B chat endpoint (OpenAI-compatible).

Used ONLY offline, to write narrative text (shop names, activity wording, notes)
for synthetic fixtures. It never decides a label. Labels come from oracle.py.

Configuration is by environment so no provider or key is written into the repo:

    IPE_CHAT_BASE    base URL that already ends in /v1
    IPE_CHAT_KEY     group API key (keep private)
    IPE_CHAT_MODEL   model id served at that URL
    IPE_CHAT_CACERT  path to the CA certificate for that URL
"""

from __future__ import annotations

import json
import os
import re
import time

import requests


def configured() -> bool:
    return all(os.getenv(k) for k in ("IPE_CHAT_BASE", "IPE_CHAT_KEY", "IPE_CHAT_MODEL"))


def _verify():
    path = os.getenv("IPE_CHAT_CACERT")
    return os.path.expanduser(path) if path else True


def _headers():
    return {"Authorization": f"Bearer {os.environ['IPE_CHAT_KEY']}"}


def _clean(raw: str) -> str:
    raw = re.sub(r"<think>.*?</think>", "", raw or "", flags=re.S).strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.S).strip()
    return raw


def models() -> dict:
    r = requests.get(f"{os.environ['IPE_CHAT_BASE']}/models", headers=_headers(),
                     verify=_verify(), timeout=30)
    r.raise_for_status()
    return r.json()


def chat(messages: list[dict], max_tokens: int = 400, temperature: float = 0.7,
         retries: int = 4) -> str:
    body = {
        "model": os.environ["IPE_CHAT_MODEL"],
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        # Hybrid-thinking models otherwise spend the token budget on reasoning.
        # Servers that do not know this key ignore it; set IPE_CHAT_NO_TEMPLATE_KWARGS=1 if yours rejects it.
        "chat_template_kwargs": {"enable_thinking": False},
    }
    if os.getenv("IPE_CHAT_NO_TEMPLATE_KWARGS"):
        body.pop("chat_template_kwargs")
    last = None
    for attempt in range(retries):
        try:
            r = requests.post(f"{os.environ['IPE_CHAT_BASE']}/chat/completions",
                              headers=_headers(), json=body, verify=_verify(), timeout=120)
            r.raise_for_status()
            return _clean(r.json()["choices"][0]["message"]["content"])
        except Exception as e:  # network, 5xx, rate limit
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"chat endpoint failed after {retries} tries: {last}")


def chat_json(system: str, user: str, keys: list[str], temperature: float = 0.7) -> dict:
    """Ask for one JSON object; raise ValueError if it is missing any key."""
    raw = chat([{"role": "system", "content": system},
                {"role": "user", "content": user}], temperature=temperature)
    start, end = raw.find("{"), raw.rfind("}")
    if start < 0 or end <= start:
        raise ValueError(f"no JSON object in reply: {raw[:120]!r}")
    obj = json.loads(raw[start:end + 1])
    missing = [k for k in keys if not isinstance(obj.get(k), str)]
    if missing:
        raise ValueError(f"reply lacks keys {missing}")
    return obj


if __name__ == "__main__":
    if not configured():
        raise SystemExit("Set IPE_CHAT_BASE, IPE_CHAT_KEY, IPE_CHAT_MODEL (and IPE_CHAT_CACERT).")
    print(json.dumps(models(), indent=2)[:600])
    print(chat([{"role": "user", "content": "Reply with the single word: ready"}], max_tokens=10))

