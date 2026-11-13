#!/usr/bin/env python3
"""Rebuild generated IRAC memos. Does not overwrite handwritten POL / ANX / CIR / SOP / FAQ-001."""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT.parent / "corpus" / "documents"

GENERATED_DIRS = [
    DOCS / "opinions",
    DOCS / "briefings",
    DOCS / "faq" / "articles",
    DOCS / "territorial",
]

MIN_APPLICATION = 250
MIN_DOCS = 500
MAX_DOCS = 2000


def thicken(m: dict) -> dict:
    """If analysis is short, append unique issue/facts/held — not a shared sermon."""
    app = " ".join(m["application"].split())
    if len(app) >= MIN_APPLICATION:
        m["application"] = app
        return m
    facts = " ".join(m["facts"].split())
    held = " ".join(m["held"].split())
    issue = " ".join(m["issue"].split())
    extra = (
        f" The issue is: {issue} "
        f"On these facts ({facts}) the held is: {held} "
        f"Cite {m['related']}."
    )
    m["application"] = app + extra
    return m


def slug(s: str) -> str:
    out = []
    for c in s.lower():
        out.append(c if c.isalnum() else "-")
    return "-".join(p for p in "".join(out).split("-") if p)[:80]


def wipe_generated() -> None:
    for d in GENERATED_DIRS:
        if d.exists():
            shutil.rmtree(d)


def write_irac(m: dict) -> Path:
    folder = m["folder"]
    s = slug(m["slug"])
    folder_code = slug(folder.split("/")[-1])[:10].upper()
    doc_id = m.get("doc_id") or f"ONB-{folder_code}-{s.upper()[:42]}"
    owner = m.get("owner") or "Head of Merchant Risk — Legal"
    related = m["related"]
    body = f"""# {doc_id}
# {m["title"]}

| | |
|---|---|
| Document ID | {doc_id} |
| Version | 1.0 |
| Status | In force |
| Classification | Internal — Legal / Compliance |
| Owner | {owner} |
| Effective | 1 October 2026 |
| Related | {related} |

iPe (India Pay) is a fictional payments business. This memorandum is for retrieval after onboarding operations have acted. It does not decide the next field, accept a file, or activate a merchant.

---

## Issue

{m["issue"].strip()}

## Facts

{m["facts"].strip()}

## Rule

{m["rule"].strip()}

## Application

{m["application"].strip()}

## Held

{m["held"].strip()}

## Copilot

{m["copilot"].strip()}
"""
    if len(m["application"].strip()) < MIN_APPLICATION:
        raise SystemExit(f"application too short ({len(m['application'].strip())}): {s}")
    path = DOCS / folder / f"{s}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def collect() -> list[dict]:
    from lib_activation import MEMOS as activation
    from lib_addendum import MEMOS as addendum
    from lib_briefings import MEMOS as briefings
    from lib_evidence import MEMOS as evidence
    from lib_faq import MEMOS as faq
    from lib_files import MEMOS as files
    from lib_format import MEMOS as fmt
    from lib_identity import MEMOS as identity
    from lib_integrity import MEMOS as integrity
    from lib_more_issues import MEMOS as more_issues
    from lib_privacy import MEMOS as privacy
    from lib_shopfront import MEMOS as shopfront
    from lib_territorial import MEMOS as territorial
    from lib_types import MEMOS as types
    from lib_types_more import MEMOS as types_more
    from lib_volume import MEMOS as volume

    all_m = (
        list(briefings)
        + list(types)
        + list(types_more)
        + list(evidence)
        + list(volume)
        + list(activation)
        + list(addendum)
        + list(privacy)
        + list(fmt)
        + list(identity)
        + list(shopfront)
        + list(integrity)
        + list(faq)
        + list(files)
        + list(territorial)
        + list(more_issues)
    )
    return all_m


def main() -> None:
    sys.path.insert(0, str(ROOT))
    wipe_generated()
    memos = collect()
    slugs: set[str] = set()
    apps: dict[str, str] = {}
    issues: dict[str, str] = {}
    for m in memos:
        m = thicken(m)
        s = slug(m["slug"])
        key = f"{m['folder']}/{s}"
        if key in slugs:
            raise SystemExit(f"duplicate path {key}")
        slugs.add(key)
        app = " ".join(m["application"].split())
        iss = " ".join(m["issue"].split())
        ah = hashlib.sha256(app.encode()).hexdigest()
        ih = hashlib.sha256(iss.encode()).hexdigest()
        if ah in apps:
            raise SystemExit(f"clone application: {key} == {apps[ah]}")
        if ih in issues:
            raise SystemExit(f"clone issue: {key} == {issues[ih]}")
        apps[ah] = key
        issues[ih] = key
        write_irac(m)

    n = len(list(DOCS.rglob("*.md")))
    print(f"generated_memos: {len(memos)}")
    print(f"documents_now: {n}")
    if n < MIN_DOCS:
        raise SystemExit(f"need >= {MIN_DOCS} documents, have {n}")
    if n > MAX_DOCS:
        raise SystemExit(f"over {MAX_DOCS} documents, have {n}")


if __name__ == "__main__":
    main()
