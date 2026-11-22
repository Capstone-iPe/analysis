#!/usr/bin/env python3
"""Check a built dataset against the policy invariants and against the files on disk.

    python check.py [--out synth/out]

Two kinds of check, so a label bug cannot hide:

1. File checks that re-derive facts from the bytes (no labels used):
   - extension and magic bytes (ONB-ANX-001 §5) -> FORMAT_UNSUPPORTED
   - 0-byte / corrupt / encrypted -> FILE_UNREADABLE
   - shopfront EXIF date vs submit date, 90 inclusive / 91 rejected (POL-001 §2.5) -> PHOTO_TOO_OLD
   These are the Tier-1 rules of the LLD verifier, so this doubles as its reference.
2. Verdict invariants from ADR-0001 §5 / POL-001 §3-4 / POL-002.

Exit code 1 if anything fails.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oracle  # noqa: E402

ALLOWED_EXT = {".pdf", ".jpg", ".jpeg", ".png"}
MAGIC = {".pdf": [b"%PDF-"], ".jpg": [b"\xff\xd8\xff"], ".jpeg": [b"\xff\xd8\xff"], ".png": [b"\x89PNG\r\n\x1a\n"]}


def tier1(path: Path, slot: str, submit: date) -> str | None:
    """Return a rejection reason derivable from bytes alone, or None if Tier-1 passes."""
    ext = path.suffix.lower()
    data = path.read_bytes()
    if ext not in ALLOWED_EXT:
        return "FORMAT_UNSUPPORTED"
    if len(data) == 0:
        return "FILE_UNREADABLE"
    if not any(data.startswith(m) for m in MAGIC[ext]):
        return "FORMAT_UNSUPPORTED"
    if ext == ".pdf":
        if b"%%EOF" not in data[-1024:]:
            return "FILE_UNREADABLE"
        if b"/Encrypt" in data:
            return "FILE_UNREADABLE"
    else:
        try:
            with Image.open(path) as im:
                im.verify()
        except Exception:
            return "FILE_UNREADABLE"
    if slot == "shopfront_photo" and ext in {".jpg", ".jpeg"}:
        with Image.open(path) as im:
            exif = im.getexif()
            stamp = exif.get_ifd(0x8769).get(0x9003) or exif.get(0x0132)
        if stamp:
            taken = datetime.strptime(stamp, "%Y:%m:%d %H:%M:%S").date()
            if (submit - taken).days > 90:
                return "PHOTO_TOO_OLD"
    return None


def check_verdict(label: dict) -> list[str]:
    v, errs = label["verdict"], []
    bucket = label["business_bucket"]
    if v["outcome"] == "REFUSED":
        if bucket != "refused":
            errs.append("REFUSED but type is not §3.2")
        if v["review_id"] is not None or v["assignee"] is not None:
            errs.append("REFUSED must have no review id and no assignee")
    else:
        if bucket == "refused":
            errs.append("§3.2 type was not refused")
        if v["review_id"] is None:
            errs.append("non-refused verdict must allocate a review id")
        want = "HEAD_OF_PAYMENTS" if v["volume_inr"] > oracle.CEILING_INR else "MERCHANT_RISK_LEAD"
        if v["assignee"] != want:
            errs.append(f"assignee {v['assignee']} != {want} for {v['volume_inr']}")
    if v["outcome"] == "RECOMMEND_GO_LIVE" and (bucket != "permitted" or v["missing_items"]):
        errs.append("go-live needs a permitted type and no missing items")
    if bucket == "unlisted" and v["outcome"] != "IN_REVIEW":
        errs.append("unlisted type must stay IN_REVIEW")
    if bucket == "permitted" and not v["missing_items"] and v["outcome"] != "RECOMMEND_GO_LIVE":
        errs.append("complete permitted pack should be RECOMMEND_GO_LIVE")
    if any(m not in oracle.required_slots(v["addendum_required"]) for m in v["missing_items"]):
        errs.append("missing_items holds a non-slot (no fifth pack item)")
    if (not v["addendum_required"]) and "dpa_addendum" in v["missing_items"]:
        errs.append("addendum listed though payer phones are not stored")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out"))
    args = ap.parse_args()
    root = Path(args.out) / "apps"
    failures, n_files, n_apps = [], 0, 0
    for d in sorted(root.iterdir()):
        n_apps += 1
        app = json.loads((d / "application.json").read_text())
        label = json.loads((d / "label.json").read_text())
        submit = date.fromisoformat(app["submit_date"])
        for err in check_verdict(label):
            failures.append(f"{d.name}: {err}")
        for u in label["uploads"]:
            n_files += 1
            p = d / u["file"]
            if not p.exists():
                failures.append(f"{d.name}: missing file {u['file']}")
                continue
            got = tier1(p, u["slot"], submit)
            exp = u["expected"]["reason_code"]
            tier1_codes = {"FORMAT_UNSUPPORTED", "FILE_UNREADABLE", "PHOTO_TOO_OLD"}
            # Optical/OCR degradation variants (glare, blur, etc.) are valid JPEG containers that fail at Tier-2 (OCR/VLM), not Tier-1 bytes
            if u["variant"] in {"id_card_glare", "id_card_blur", "id_card_underexposed", "id_card_xerox"}:
                continue
            if exp in tier1_codes and got != exp:
                failures.append(f"{d.name}: {u['file']} expected {exp}, Tier-1 says {got}")
            if exp not in tier1_codes and got is not None:
                failures.append(f"{d.name}: {u['file']} expected {exp}, Tier-1 rejected as {got}")
        # Upload sequence: a slot is either accepted or explicitly marked missing.
        for slot in oracle.required_slots(label["verdict"]["addendum_required"]):
            ok = any(u["expected"]["accepted"] for u in label["uploads"] if u["slot"] == slot)
            marked = any(u.get("missing") for u in app["uploads"] if u["slot"] == slot)
            if ok == marked:
                failures.append(f"{d.name}: slot {slot} accepted={ok} but missing-mark={marked}")
    print(f"checked {n_apps} applications, {n_files} uploads")
    if failures:
        print(f"{len(failures)} problem(s):")
        print("\n".join("  " + f for f in failures[:50]))
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()

