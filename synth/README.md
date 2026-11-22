# Synthetic applications for the Document Verifier

Builds merchant applications with rendered pack files (PDF, JPG, PNG, and deliberately broken files) and labels computed in code. Design: [docs/LLD-0001-document-verifier.md](../docs/LLD-0001-document-verifier.md).

| File | Job |
|---|---|
| `catalog.py` | Business types from `corpus/lib_types.py` + `lib_types_more.py`. Bucket comes from each memo's `held`. |
| `render.py` | Renderers and the variant catalogue: one row per (slot, variant), with its expected `accepted` and `reason_code`. |
| `oracle.py` | Reference labeller: expected verdict (ADR-0001 §5–6). Test tooling, not ONB. |
| `narrative.py` | Shop names and wording. The only use of the chat model. Rule-checked, template fallback. |
| `build.py` | Case matrix → files + `application.json` + `label.json` + `fixtures.csv`. |
| `check.py` | Re-derives Tier-1 facts from bytes and checks verdict invariants. |
| `llm.py` | OpenAI-compatible client, configured only by environment. |

## Run

```sh
cd analysis/synth
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

.venv/bin/python build.py          # offline templates, ~7 s
.venv/bin/python check.py          # must print "all checks passed"
```

With the team's hosted chat model (keep the key out of git):

```sh
export IPE_CHAT_BASE="https://<host>:<port>/v1"
export IPE_CHAT_KEY="<group key>"
export IPE_CHAT_MODEL="<model id>"
export IPE_CHAT_CACERT="$HOME/Downloads/<ca>.crt"

.venv/bin/python llm.py                        # connectivity check
.venv/bin/python build.py --llm --workers 4    # ~440 chat calls
.venv/bin/python check.py
```

`summary.json` reports how many narratives fell back to templates. A fallback changes wording only, never a label.

## Rules this data keeps

- Labels never come from the model.
- Four pack slots, plus `dpa_addendum` only when payer phones are stored. GSTIN, Udyam and FSSAI are never slots.
- Every file is marked `SPECIMEN - SYNTHETIC TEST DOCUMENT`. No real ID layout is imitated.
- `out/` is git-ignored. Do not put it in the RAG index, and do not copy `eval/` shops into it.

