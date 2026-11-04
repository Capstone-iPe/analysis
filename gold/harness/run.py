"""Run an agent against the merchant simulator.

    python harness/run.py --agent harness.agents.reference_agent:ReferenceAgent --split dev --out runs/ref_dev.json
    python harness/run.py --agent my_pkg.my_agent:MyAgent --split test --out runs/mine_test.json

The agent class is instantiated once per conversation (fresh memory each time).
"""
import argparse, importlib, json, os, sys, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from harness.simulator import run_conversation  # noqa: E402


def load(spec):
    mod, cls = spec.split(":")
    return getattr(importlib.import_module(mod), cls)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", required=True, help="module.path:ClassName")
    ap.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    ap.add_argument("--ids", nargs="*", help="run only these scenario ids")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    splits = json.load(open(os.path.join(ROOT, "splits.json")))
    ids = args.ids or (splits["dev"] + splits["test"] if args.split == "all" else splits[args.split])
    Agent = load(args.agent)
    results = {}
    t0 = time.time()
    for sid in ids:
        results[sid] = run_conversation(Agent(), os.path.join(ROOT, "scenarios", sid), os.path.join(ROOT, "policy"))
        print(f"{sid}: {len(results[sid]['turns'])} turns, violations={[v['type'] for v in results[sid]['violations']]}")
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    json.dump(results, open(args.out, "w"), indent=1, ensure_ascii=False)
    print(f"wrote {args.out} ({len(ids)} conversations, {time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
