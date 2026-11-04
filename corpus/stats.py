#!/usr/bin/env python3
"""Chunk count for the curated corpus (800 / 120)."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "documents"
CHUNK, OVERLAP = 800, 120


def n_chunks(text: str) -> int:
    n = len(text)
    if n <= CHUNK:
        return 1
    return 1 + math.ceil((n - CHUNK) / (CHUNK - OVERLAP))


def main() -> None:
    files = sorted(p for p in DOCS.rglob("*.md") if p.is_file())
    rows = []
    for p in files:
        text = p.read_text(encoding="utf-8")
        rows.append({
            "path": str(p.relative_to(DOCS)),
            "chars": len(text),
            "chunks_800_120": n_chunks(text),
        })
    stats = {
        "documents": len(rows),
        "chars": sum(r["chars"] for r in rows),
        "chunks_800_120": sum(r["chunks_800_120"] for r in rows),
        "chunk_size": CHUNK,
        "overlap": OVERLAP,
    }
    (ROOT / "stats.json").write_text(json.dumps({"stats": stats, "files": rows}, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=2))
    for r in rows:
        print(f"  {r['chunks_800_120']:3d} chunks  {r['path']}")


if __name__ == "__main__":
    main()
