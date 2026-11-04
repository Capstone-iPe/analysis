# ONB-EVIDENCE-JSON-KYC-DUMP
# A JSON KYC dump is not the government ID file

| | |
|---|---|
| Document ID | ONB-EVIDENCE-JSON-KYC-DUMP |
| Version | 1.0 |
| Status | In force |
| Classification | Internal — Legal / Compliance |
| Owner | Head of Merchant Risk — Legal |
| Effective | 1 October 2026 |
| Related | ONB-POL-001 §2; ONB-ANX-001 |

iPe (India Pay) is a fictional payments business. This memorandum is for retrieval after onboarding operations have acted. It does not decide the next field, accept a file, or activate a merchant.

---

## Issue

Whether a CKYCR-style JSON dump can replace the owner-ID upload.

## Facts

The applicant uploaded a JSON object of KYC fields.

## Rule

ONB-ANX-001: JSON dump of KYC is not the government ID file. This product does not download CKYCR.

## Application

Structured data is not the OVD. The Copilot shall not parse the JSON into PII in chat, shall not call CKYCR, and shall request the ID file in PDF/JPG/PNG. The issue is: Whether a CKYCR-style JSON dump can replace the owner-ID upload. On these facts (The applicant uploaded a JSON object of KYC fields.) the held is: Does not satisfy owner ID. No CKYCR pull. Cite ONB-POL-001 §2; ONB-ANX-001.

## Held

Does not satisfy owner ID. No CKYCR pull.

## Copilot

Cite ONB-ANX-001. Do not print fields from the JSON.
