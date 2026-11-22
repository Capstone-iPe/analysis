"""Validation script using local qwen2.5vl:7b over Ollama.

Evaluates synthetic document images against real OCR and optical stress.
Usage:
    .venv/bin/python eval_ollama.py --image /tmp/stress_test/standard_glare.jpg
    .venv/bin/python eval_ollama.py --suite
"""

from __future__ import annotations

import argparse
import base64
import json
import time
import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"


def inspect_document(image_path: str) -> dict:
    """Send an image to local qwen2.5vl to extract fields and flag quality issues."""
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")

    prompt = (
        "You are an automated KYC Document Verification inspector.\n"
        "Analyze the provided image and return ONLY a JSON object with these exact keys:\n"
        "{\n"
        '  "doc_type": "national_id | other_membership | unknown",\n'
        '  "extracted_name": "<full name or null if unreadable>",\n'
        '  "extracted_id": "<id number or null if unreadable>",\n'
        '  "optical_defect": "none | severe_glare | severe_blur | severe_underexposure | xerox_noise",\n'
        '  "is_legible": true | false\n'
        "}"
    )

    t0 = time.time()
    res = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "images": [b64],
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": 180},
        },
        timeout=90,
    )
    elapsed = time.time() - t0
    txt = res.json().get("response", "").strip()

    # Extract JSON block
    s, e = txt.find("{"), txt.rfind("}")
    parsed = {}
    if s >= 0 and e > s:
        try:
            parsed = json.loads(txt[s : e + 1])
        except Exception:
            parsed = {"raw": txt}
    else:
        parsed = {"raw": txt}

    parsed["latency_seconds"] = round(elapsed, 2)
    return parsed


def run_suite():
    tests = [
        ("Clean Standard", "/tmp/id_test/standard_id.jpg"),
        ("Flash Glare", "/tmp/stress_test/standard_glare.jpg"),
        ("Motion Blur", "/tmp/stress_test/standard_blur.jpg"),
        ("Underexposed / Dark", "/tmp/stress_test/standard_underexposed.jpg"),
        ("Warm Tungsten Light", "/tmp/stress_test/standard_tungsten.jpg"),
        ("Photocopy / Xerox", "/tmp/stress_test/standard_xerox.jpg"),
        ("Gym Pass (Deviated)", "/tmp/id_test/deviated_gym_pass.jpg"),
    ]
    print(f"Running automated OCR/defect evaluation using {MODEL_NAME}...\n")
    for name, path in tests:
        if not Path(path).exists():
            continue
        res = inspect_document(path)
        print(f"[{name}] -> Legible: {res.get('is_legible')}, Defect: {res.get('optical_defect')}, Name: {res.get('extracted_name')}, ID: {res.get('extracted_id')} ({res.get('latency_seconds')}s)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="Path to single image")
    parser.add_argument("--suite", action="store_true", help="Run benchmark suite")
    args = parser.parse_args()

    if args.image:
        print(json.dumps(inspect_document(args.image), indent=2))
    else:
        run_suite()

