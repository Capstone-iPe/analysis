# iPe retrieval corpus

In-force policies plus IRAC legal memoranda, India-facing statutory briefings, FAQ articles, and a reviewer handbook.

**500 documents** (inside 500–2,000). At 800 / 120 that is **1,446 chunks**.

The Copilot retrieves these **after** onboarding operations have acted, to **cite and explain**. They do not decide the next field, accept a file, or activate a merchant.

| Folder | What |
|---|---|
| `documents/policy/` | ONB-POL-001–005 — pack, types, volume, payer data, Copilot authority |
| `documents/annex/` | Evidence, volume reading, type aliases (including hawala → money service) |
| `documents/circulars/` | Systems shall not activate; applicant text is untrusted |
| `documents/briefings/` | PMLA, RBI KYC, DPDP, PSS Act, Aadhaar/no UIDAI, GST-not-a-slot, FEMA, and other background. They do **not** add pack items |
| `documents/opinions/` | Type, evidence, volume, activation, addendum, integrity, and cross-issue file notes (IRAC) |
| `documents/faq/` | Merchant-facing approved answers |
| `documents/territorial/` | Non-exceptions (no city waiver of bank proof) |
| `documents/handbook/` | Reviewer handbook |
| `documents/not-in-force/` | Rejected drafts — do not obey if retrieved |

Rebuild generated memos with `python3 corpus/expand.py` (does not overwrite POL / ANX / CIR / SOP / FAQ-001). Stats: `python3 corpus/stats.py`.
