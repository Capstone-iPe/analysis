"""Business-type catalogue built from the corpus type memos.

The bucket of each type comes from the memo's own `held` line, which mirrors
ONB-POL-001 §3 and ONB-ANX-003:

    "Permitted ..." -> permitted (§3.1)
    "Refused ..."   -> refused   (§3.2)
    anything else   -> unlisted  (§3.3, stays in review)

Two memos are not a business type and are skipped as type cases:
nri-owned-shop (ownership is not a type) and sub-merchant-platform (outcome
depends on whether funds aggregation was described).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

CORPUS = Path(__file__).resolve().parent.parent / "corpus"

SKIP = {"nri-owned-shop", "sub-merchant-platform"}

# Canonical §3.1 type for the permitted aliases (ONB-POL-001 §3.1, ONB-ANX-003 §1).
CANONICAL = {"restaurant": "restaurant", "cafe": "restaurant", "dhaba": "restaurant",
             "grocery": "grocery", "kirana": "grocery", "retail": "retail"}

# What the merchant types in the business_type field. lib_types.py memos have no
# `activity` key, and some lib_types_more activities read "X as Y" (the type is Y).
STATED = {
    "kirana": "kirana (general provisions, grocery)",
    "money-service": "money service",
    "hawala-desk": "hawala desk",
    "remittance-agent": "remittance agent",
    "forex-counter": "forex counter",
    "bitcoin-atm": "bitcoin ATM",
    "nft-shop": "NFT shop",
    "satta-matka": "satta matka",
    "online-casino": "online casino",
    "fantasy-sports-cash": "fantasy sports for cash",
    "lottery-business": "lottery business",
    "prepaid-wallet-issuer": "prepaid wallet issuer",
    "unlicensed-aggregator": "payment aggregator collecting other merchants' funds",
    "nbfc-gold-loan": "NBFC gold loan",
    "saas-company": "SaaS company",
    "ngo": "NGO",
    "esports-prizes": "esports tournaments with prizes",
    "spa-massage": "spa and massage",
    "mutual-fund-distributor": "mutual fund distributor",
    "tyre-shop-workshop": "tyre fitting workshop",
    "optical-as-clinic": "optometry clinic",
    "sweet-shop-as-factory": "sweet manufacturing factory",
    "tractor-dealer-workshop": "tractor repair workshop",
    "temple-as-temple": "temple",
    "huf-as-huf": "HUF",
    "railway-stall-as-railway": "railway stall",
    "airport-kiosk-as-kiosk": "airport kiosk",
    "pesticide-shop-as-pesticide": "pesticide shop",
    "government-canteen": "government canteen",
    "college-canteen-as-college": "college",
    "seed-shop-not-retail": "seed shop",
    "dairy-as-dairy": "dairy",
    "two-wheeler-service": "two-wheeler service centre",
}


@dataclass(frozen=True)
class BizType:
    slug: str
    stated: str          # words typed into business_type
    bucket: str          # permitted | refused | unlisted
    canonical: str | None  # restaurant/grocery/retail for permitted, else None
    nature: str          # one-line description for the narrative prompt
    trap: str            # the retrieval / classification trap the memo guards
    held: str
    source: str          # lib_types | lib_types_more


def _bucket(held: str) -> str:
    h = held.strip().lower()
    if h.startswith("permitted"):
        return "permitted"
    if h.startswith("refused"):
        return "refused"
    return "unlisted"


def _nature(m: dict) -> str:
    """lib_types_more has `nature`. lib_types only has `facts`, phrased as
    'The merchant stated X: <activity>. ...'; keep just <activity>."""
    if m.get("nature"):
        return m["nature"]
    first = m["facts"].split(". ")[0]
    return first.split(":", 1)[1].strip() if ":" in first else first


def load() -> list[BizType]:
    sys.path.insert(0, str(CORPUS))
    try:
        import lib_types
        import lib_types_more
    finally:
        sys.path.pop(0)
    out: list[BizType] = []
    for source, memos in (("lib_types", lib_types.MEMOS), ("lib_types_more", lib_types_more.MEMOS)):
        for m in memos:
            if m["slug"] in SKIP:
                continue
            bucket = _bucket(m["held"])
            stated = STATED.get(m["slug"]) or m.get("activity") or m["slug"].replace("-", " ")
            out.append(BizType(
                slug=m["slug"], stated=stated, bucket=bucket,
                canonical=CANONICAL.get(m["slug"]) if bucket == "permitted" else None,
                nature=_nature(m),
                trap=m.get("trap") or m["issue"],
                held=m["held"], source=source,
            ))
    return out


if __name__ == "__main__":
    from collections import Counter
    types = load()
    print(len(types), Counter(t.bucket for t in types))
    for t in types:
        if t.bucket != "unlisted":
            print(f"  {t.bucket:9s} {t.slug:24s} -> {t.stated}")
