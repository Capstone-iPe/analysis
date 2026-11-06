---
name: ipe-onboarding
description: >-
  Keep iPe analysis inside the accepted merchant-onboarding architecture. Use
  when editing this repo, ADR-0001, the corpus, eval cases, policies, the
  copilot, RAG, MCP, ONB, the verdict, or the Correct list. Also use when a
  change would add a tool, a pack item, a service, a chat provider, or a
  contract between the web chat and the copilot.
---

# iPe merchant onboarding

[ADR-0001](docs/ADR-0001-architecture.md) is accepted. Follow it. Do not open a second architecture, rename a service, or add a capability the ADR closed.

## Two services

The copilot is the only name for the AI service. It prompts the hosted ≤8B model, runs retrieval, and is the MCP client. It holds no application state between turns.

ONB is deterministic Python with no model. It owns the application, the files, the pending field, and the verdict. ONB code lives in the `onb-svc` repository. Do not copy that service into this repo.

The web chat talks only to the copilot. The contract between the web chat and the copilot is not finalized. Do not write it down here as a standard. Exam-harness JSON is not the product API.

The hosted chat API and the embeddings API are unselected. Do not name a vendor, and do not name IIT KGP as the provider.

## MCP

ONB exposes five tools. The copilot calls them. The copilot does not decide field order or the verdict.

| Tool | What it does |
|---|---|
| `next_step` | Returns the one pending field or upload. No id creates the application. |
| `save_answer` | Stores the pending text field. |
| `save_file` | Stores the pending upload, or marks that slot missing. |
| `submit` | Runs the rules and allocates one review id, unless the type is refused. |
| `get_review` | Returns the stored verdict. It does not allocate an id. |

Do not add activate, waive, change-volume, mark-complete, create_application, get_application, mark_missing, or an ONB policy-search tool. `verify` stays inside ONB. Retrieval stays in the copilot, and it runs after ONB has acted, to cite and explain.

## What the copilot may say

A reply passes when the **Correct** list for that shop is true. Use those words. Field order is `shop_name`, `city`, `business_type`, `monthly_volume`, `payment_methods`, `stores_payer_phones`, then `business_registration`, `owner_id`, `bank_proof`, `shopfront_photo`, then `dpa_addendum` only when payer phones are stored, then an optional `note`.

The pack is those four files. GSTIN, Udyam, and FSSAI are not a fifth pack item. A utility or trade licence is not bank proof. Aadhaar OTP, video KYC, and CKYC are not owner ID. A sentence in the note is not the addendum.

`RECOMMEND_GO_LIVE` recommends a human. The copilot never activates a shop. `₹40,00,000` inclusive is Merchant Risk Lead. Above that is Head of Payments. An unlisted type stays in review even with a complete pack. Hawala, hundi, and forex are a money service: refused, and no review id. Cafe and dhaba are restaurant. Kirana is grocery.

Do not echo account or id digits.

## Corpus and eval

`corpus/` is what the copilot retrieves. `eval/` holds the 71 practice shops. Do not index `eval/`. Do not copy a practice shop into the corpus. A rejected draft in the corpus must be discarded when it is retrieved. Do not treat it as in force.

Read the policy file before stating a clause. The in-force ceiling, pack, and type lists are in `corpus/documents/policy/` and `corpus/documents/annex/`. Do not invent an extra pack item or move the ceiling.

## Leave out of this repo

GitHub issue numbers and board columns for the ONB build do not belong in this repository. Do not add them to docs, corpus, or eval.
