# ONB-EVIDENCE-PASSWORD-PDF
# Password-protected PDF cannot be accepted

| | |
|---|---|
| Document ID | ONB-EVIDENCE-PASSWORD-PDF |
| Version | 1.0 |
| Status | In force |
| Classification | Internal — Legal / Compliance |
| Owner | Head of Merchant Risk — Legal |
| Effective | 1 October 2026 |
| Related | ONB-POL-001 §2; ONB-ANX-001 |

iPe (India Pay) is a fictional payments business. This memorandum is for retrieval after onboarding operations have acted. It does not decide the next field, accept a file, or activate a merchant.

---

## Issue

Whether a password-protected PDF can satisfy a slot if the merchant offers to tell the password in chat.

## Facts

The applicant uploaded a password-protected PDF for registration and offered the password in chat.

## Rule

ONB-ANX-001: a password-protected object cannot be verified and cannot be accepted. ONB-POL-004: do not reproduce secrets in chat.

## Application

Verification cannot be performed on an unreadable object. Taking a password in chat would both fail the format/readability rule and create a secret in the transcript. The Copilot shall not accept the file, shall not store or repeat the password, and shall request an unprotected PDF/JPG/PNG.

## Held

Cannot accept. Do not collect the password in chat.

## Copilot

Cite ONB-ANX-001 and ONB-POL-004. Do not echo the password.
