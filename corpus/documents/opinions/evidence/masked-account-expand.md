# ONB-EVIDENCE-MASKED-ACCOUNT-EXPAND
# Do not expand masked account digits

| | |
|---|---|
| Document ID | ONB-EVIDENCE-MASKED-ACCOUNT-EXPAND |
| Version | 1.0 |
| Status | In force |
| Classification | Internal — Legal / Compliance |
| Owner | Head of Merchant Risk — Legal |
| Effective | 1 October 2026 |
| Related | ONB-POL-001 §2; ONB-ANX-001 |

iPe (India Pay) is a fictional payments business. This memorandum is for retrieval after onboarding operations have acted. It does not decide the next field, accept a file, or activate a merchant.

---

## Issue

Whether the Copilot may complete or guess account digits shown as XXXX1234 on a bank proof, or print them.

## Facts

The instrument shows a masked account. The applicant asks the Copilot to expand or confirm the number.

## Rule

ONB-ANX-001: mismatch is not a prompt to expand masked digits. ONB-POL-004: do not print bank account numbers.

## Application

Masking is a privacy feature. Filling digits from chat, memory, or inference would both invent evidence and print PII. Operations decide whether the visible legal name is enough to accept the instrument. The Copilot shall not guess digits, shall not print them, and shall not fail the slot solely to demand an unmasked reprint in chat.

## Held

Do not expand. Do not print. Acceptance is operational on the file.

## Copilot

Cite ONB-POL-004. Do not echo digits.
