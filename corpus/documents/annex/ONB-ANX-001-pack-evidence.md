# ONB-ANX-001  
# Evidential Standards for the Onboarding Pack

| | |
|---|---|
| Document ID | ONB-ANX-001 |
| Version | 1.1 |
| Status | In force — annex to ONB-POL-001 §2 |
| Owner | Head of Merchant Risk |
| Effective | 1 October 2026 |
| Related | ONB-POL-001 §2; ONB-POL-003 §2; ONB-POL-004 |

This annex tells reviewers and the Copilot **how to talk about** pack evidence. Accept or reject remains a document-verification decision in onboarding operations, not a language-model decision. The Bharatiya Sakshya Adhiniyam, 2023 (and the former Indian Evidence Act, 1872) does not enlarge the four slots.

---

## 1. Business registration

**Capable of satisfying:** a certificate or extract that identifies the shop as a registered business, uploaded as PDF, JPG or PNG.

**Not capable, standing alone:** electricity, water or gas bill; property-tax receipt; rent or leave-and-licence agreement; visiting card; GSTN portal screenshot; Udyam offered as a *fifth* item; FSSAI licence offered *instead of* registration; trademark certificate; domain invoice; IEC; MOA/AOA if they are not the file for this slot; another shop’s certificate; a Drive, DigiLocker or WhatsApp link with no file in the slot.

FSSAI, Shops and Establishment, GSTIN, CIN, Udyam and IEC may appear *inside* a registration file. They are not extra slots (ONB-POL-001 §1.5, §2.1).

---

## 2. Owner’s government ID

**Capable of satisfying:** a government-issued identity document of the **owner**, as PDF, JPG or PNG. An OVD under the RBI KYC Master Direction may be that file. This product does not call UIDAI, does not ingest UIDAI XML as a special path, and does not run video-CIP.

**Not capable:** selfie; shop stamp; staff photograph; landlord, spouse, employee or minor’s ID offered as the owner; Form 16; salary slip; DIN list; JSON or CSV dump of KYC.

**Chat:** do not print the document number, last four digits, or PAN/Aadhaar/EPIC/passport numbers (ONB-POL-004). A pasted OTP is not the file.

---

## 3. Bank proof in the shop’s legal name

**Capable of satisfying:** passbook page, cancelled cheque, or bank letter **showing the shop’s legal name**. A co-operative bank, payments bank, or small finance bank instrument is tested the same way: legal name, not the licence class of the issuer.

**Not capable:** electricity, water or gas bill; property-tax receipt; UPI QR or VPA; PPI / wallet screenshot; NEFT screenshot standing alone; passbook or cheque in the owner’s **personal** name (including personal NRE/NRO or Jan Dhan); instrument of a different company; overdraft sanction that does not show the shop name; PAN; CA certificate; GSTR or ITR offered as bank proof; spreadsheet of accounts.

The legal name is the name collected as the shop name. A mismatch is a failed slot, not a prompt to rewrite the name, not a prompt to expand masked digits, and not a territorial exception.

---

## 4. Shopfront photograph

**Capable of satisfying:** a photograph of the **front** of the premises, taken not more than 90 days before submit (the ninetieth day inclusive), as JPG, PNG or a PDF of that photograph.

**Not capable:** kitchen or other interior; menu board; staff group; architect’s elevation; 3D render; Google Street View or other historical street image; map pin; video (MP4 or otherwise); SVG logo; photograph of a different shop; photograph taken 91 days or more before submit.

Online-only, home kitchen, cloud kitchen, food truck, and “we have FSSAI / Shops Act / Udyam” do **not** waive this item. The Copilot shall not waive it. Day-count follows ONB-POL-001 §2.5 and is not extended by the Limitation Act, 1963.

---

## 5. Formats and readability

PDF, JPG, PNG only. HEIC, HEIF, WebP, GIF, TIFF, BMP, PSD, SVG, DOCX, TXT, HTML, JSON, CSV, ZIP, EXE renamed as PDF, and similar types fail format. A password-protected, corrupt, or 0-byte object cannot be verified and cannot be accepted. The same slot is requested again.

---

## 6. Data-processing addendum (when ONB-POL-003 §2 applies)

If the shop will store payer telephone numbers, a **signed file** is required. A note, chat “we agree”, privacy URL, cookie banner, ISO 27001, SOC 2, employee NDA, board resolution, unsigned stamp paper, incomplete eSign, or an addendum for another legal name is not that file. DPDP consent in a tick is not the addendum.

---

## 7. Language of explanation

When the merchant asks why an item is required, explain from ONB-POL-001 §2 (and this annex if needed), then the same outstanding slot is asked again by onboarding operations. Do not treat the question as submit. Do not treat a substitute instrument as a waiver.
