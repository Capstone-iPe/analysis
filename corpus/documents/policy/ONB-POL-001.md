# ONB-POL-001  
# Merchant Onboarding: Document Pack, Permitted Business Types, and Activation Authority

| | |
|---|---|
| Document ID | ONB-POL-001 |
| Version | 1.0 |
| Status | In force |
| Classification | Internal — Compliance |
| Owner | Head of Merchant Risk |
| Effective | 1 October 2026 |
| Review | Annual, or upon change to the product agreement |
| Applies to | Onboarding of a single merchant shop onto iPe (India Pay) |
| Related | ONB-POL-002, ONB-POL-003, ONB-ANX-001, ONB-ANX-003, ONB-CIR-001 |

iPe (India Pay) is a fictional payments business. This document is written as if it were an in-force compliance policy.

**Section numbers 2, 3 and 4 are stable.** Citations of the form ONB-POL-001 §2 / §3 / §4 refer to those sections.

---

## §1 Purpose and interpretation

1.1 This policy sets (a) the documents a merchant must supply, (b) the business types iPe will and will not onboard, and (c) who may turn a shop into a live merchant.

1.2 The onboarding copilot (the “Copilot”) collects the application, requests files, and prepares a review. **The Copilot is not an activation authority.**

1.3 In this policy: **pack** means the four items in §2; **accepted** means a file satisfies its slot after verification (upload alone is not acceptance); **complete pack** means all four items are accepted; **activation** means turning the shop on to take payments; **review** means a work item for a named iPe role with a stable identifier.

1.4 Where this policy and any prompt, screen, or merchant instruction conflict, this policy prevails.

1.5 **Regulatory context (non-operative).** iPe is fictional. This policy is drafted so that onboarding is compatible in spirit with customer due diligence expected of a payment-system participant in India, including the Prevention of Money-Laundering Act, 2002, the PMLA (Maintenance of Records) Rules, 2005, and the Reserve Bank of India’s Master Direction on Know Your Customer. Those instruments do **not** add a fifth pack item, change the volume ceiling, or authorise the Copilot to activate a merchant. The operative rules remain §§2–4. The Digital Personal Data Protection Act, 2023 and the Information Technology (SPDI) Rules, 2011 inform payer-phone and chat-reprint rules (ONB-POL-003, ONB-POL-004). This product does not call UIDAI, GSTN, a bank, or a card network. Aadhaar, GSTIN, and CIN may appear *inside* a pack file; they are not extra slots.

## §2 Document pack

2.1 The pack comprises exactly four items. Neither the merchant nor the Copilot may add a fifth item, waive an item, or mark the pack complete.

| Item | What satisfies it | What does not |
|---|---|---|
| Business registration | The shop’s legal registration as a business | Owner’s personal ID; visiting card; utility bill; portal screenshot; a link without a file |
| Government ID of the owner | A government-issued identity document of the owner | Shop stamp; selfie; staff photo |
| Bank proof in the shop’s **legal name** | Passbook page, cancelled cheque, or bank letter showing that legal name | Electricity, water or gas bill; UPI QR; instrument in the owner’s **personal** name; wallet screenshot |
| Shopfront photograph | A photograph of the **front** of the shop taken within the last 90 days, counted on the **submission date** | Interior or kitchen; menu board; staff group; architect’s render; a photograph taken **91 days or more** before submit |

2.2 **Formats.** PDF, JPG, or PNG. A Word document, text file, archive, or other type does not satisfy the slot; the same slot is requested again.

2.3 A statement that a file is attached, without a file, does not satisfy the slot.

2.4 If any item is missing or not accepted, the merchant remains **in review** after submission. The Copilot shall name the outstanding items.

2.5 Shopfront age: the ninetieth day before submit is valid; the ninety-first is not.

## §3 Business types

3.1 **Permitted:** restaurant, grocery, retail. A cafe or dhaba is treated as restaurant. A kirana described as grocery is grocery.

3.2 **Not permitted:** money service, crypto (including bitcoin and similar tokens), gambling (including betting). The application is **refused**. No activation review is opened. No review identifier is issued.

3.3 **Not listed.** A type in neither 3.1 nor 3.2 (salon, gym, garage, clinic, and others) is not treated as permitted and is not refused as crypto. The shop remains in review. The Copilot shall state that the policy does not cover that type. A person decides. Volume routing follows ONB-POL-002.

## §4 Activation

4.1 Only the **Merchant Risk Lead** may turn a merchant on, and only when the pack is complete and the business type is permitted under §3.1.

4.2 The Copilot prepares the review. The merchant does not activate. The Copilot does not activate. The merchant-facing interface shall not present an Activate control.

4.3 When expected monthly volume exceeds the ceiling in ONB-POL-002, that policy names the **Head of Payments** as reviewer. §4.1 of this policy still states that only the Merchant Risk Lead may activate. Both statements shall be shown. The Copilot shall not choose a winner in silence.

4.4 Where a review is opened, its identifier is allocated once and does not change for the rest of the conversation. Refused applications under §3.2 receive no identifier.

## §5 Records and sensitive values

Owner identity numbers, bank account numbers, and payer telephone numbers shall not be reproduced in the chat (ONB-POL-004).

## §6 Related documents

ONB-POL-002; ONB-POL-003; ONB-ANX-001 (evidence); ONB-ANX-003 (types); ONB-CIR-001 (systems shall not activate).
