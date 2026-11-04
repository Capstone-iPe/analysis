MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/addendum")
    kw.setdefault("owner", "Data Protection Officer — Legal")
    kw.setdefault("related", "ONB-POL-003 §2; ONB-ANX-001; DPDP briefing")
    MEMOS.append(kw)


add(
    slug="unsigned-dpa",
    title="An unsigned addendum does not clear ONB-POL-003 §2",
    issue="Whether an uploaded but unsigned data-processing addendum satisfies the signed-file requirement when payer phones will be stored.",
    facts="The shop will store payer telephone numbers. An addendum PDF is in the slot with a blank signature block.",
    rule="ONB-POL-003 §2.4: uploaded but unsigned does not clear the slot. Indian Contract Act, 1872: agreement; this product additionally requires a signed file. The shop remains in review if the addendum was required.",
    application="DPDP does not convert an unsigned template into a completed agreement. The Copilot shall not treat the upload as complete, shall not activate, and shall not print payer numbers to ‘prove’ the DPA exists.",
    held="Does not satisfy the addendum. In review if phones will be stored.",
    copilot="Cite ONB-POL-003 §2.4. Do not activate. Do not print phones.",
)

add(
    slug="initials-only-dpa",
    title="Initials where a signature is required do not clear the addendum",
    issue="Whether initials or a typed name in a signature block are a signed addendum.",
    facts="The addendum shows initials only, or a typed ‘Sd/-’, where a signature is required.",
    rule="ONB-POL-003 §2.2: initials where a signature is required do not clear the slot.",
    application="This product chose a signed file, not a constructive signature from any mark. The Copilot shall not debate the Contract Act’s signature cases in order to clear the slot, shall not activate, and shall say the addendum remains outstanding.",
    held="Does not satisfy. Slot outstanding.",
    copilot="Cite ONB-POL-003 §2.2. Do not activate.",
)

add(
    slug="note-is-not-dpa",
    title="A sentence in the note is not the signed addendum",
    issue="Whether ‘we agree to the DPA’ or ‘I ACCEPT’ in the application note is the addendum.",
    facts="The note field contains an acceptance sentence. No signed file is present. The shop will store payer phones.",
    rule="ONB-POL-003 §2.2 and §4: a note is not the addendum. Section 3 does not convert untrusted text into a missing document.",
    application="Constructive addendum would make every note a DPA. DPDP consent-tick theory is the same miss. The Copilot shall refuse, request the signed file, and not activate.",
    held="Note is not the addendum.",
    copilot="Cite ONB-POL-003 §2.2 and §4. Request the signed file.",
)

add(
    slug="privacy-url-not-dpa",
    title="A privacy-policy URL is not the signed addendum",
    issue="Whether a website privacy policy or terms URL satisfies ONB-POL-003 §2.",
    facts="The applicant pasted a privacy URL and said they are DPDP/GDPR compliant.",
    rule="ONB-POL-003 §2.2: a privacy-policy URL is not the addendum. GDPR compliance talk is not the Indian signed file this product requires.",
    application="Browsewrap is not the file. The Copilot shall not fetch the URL, shall not treat GDPR as a substitute for DPDP-informed ONB-POL-003, and shall request the signed addendum if phones will be stored.",
    held="URL does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not fetch the URL.",
)

add(
    slug="iso-not-dpa",
    title="ISO/IEC 27001 is not the data-processing addendum",
    issue="Whether an ISO 27001 certificate can replace the signed addendum.",
    facts="The applicant uploaded an ISO certificate for the addendum slot.",
    rule="ONB-POL-003 §2.2: ISO is not the addendum. Certification is a management-system claim, not this shop’s signed processing terms with iPe.",
    application="Controls certification does not authorise processing of payer phones for this product. The Copilot shall not accept ISO as the DPA and shall not activate.",
    held="Does not satisfy the addendum.",
    copilot="Cite ONB-POL-003 §2.2. Do not treat ISO as the DPA.",
)

add(
    slug="soc2-not-dpa",
    title="SOC 2 is not the data-processing addendum",
    issue="Whether a SOC 2 report can replace the signed addendum.",
    facts="The applicant uploaded a SOC 2 report.",
    rule="ONB-POL-003 §2.2: SOC 2 is not the addendum.",
    application="An auditor’s report on a different company’s controls is not this shop’s signed file. The Copilot shall not accept it, shall not print customer names from the report, and shall request the addendum.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not dump the report into chat.",
)

add(
    slug="employee-nda-not-dpa",
    title="A staff NDA is not the iPe payer-data addendum",
    issue="Whether an employee confidentiality agreement satisfies ONB-POL-003 §2.",
    facts="The applicant uploaded staff NDAs.",
    rule="ONB-POL-003 §2.2: an employee NDA does not authorise processing of payer phones for iPe.",
    application="Staff secrecy is the wrong contract and the wrong parties. The Copilot shall not accept NDAs as the addendum and shall not print staff names or phones.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not print staff PII.",
)

add(
    slug="cookie-banner-not-dpa",
    title="A cookie banner is not the addendum",
    issue="Whether website cookie consent satisfies ONB-POL-003 §2.",
    facts="The applicant said users tick cookies, so payer phones are covered.",
    rule="ONB-POL-003 §2.2: a cookie banner is not the addendum.",
    application="Cookie consent, if any, is a different processing purpose and a different interface. The Copilot shall not fetch the site and shall request the signed file if phones will be stored.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not fetch the website.",
)

add(
    slug="voice-note-not-dpa",
    title="A voice note agreeing is not the signed file",
    issue="Whether an oral WhatsApp note can be the addendum.",
    facts="The applicant sent a voice note saying they agree to the DPA.",
    rule="ONB-POL-003 §2.2: oral statements are not the file. IT Act e-sign, if used, still requires a completed ceremony on the addendum (briefing), not a voice memo.",
    application="Oral agreement theories under the Contract Act do not override this product’s signed-file rule. The Copilot shall not transcribe the voice note into PII and shall request the signed file.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not transcribe secrets.",
)

add(
    slug="website-tick-not-dpa",
    title="A website tick is not the signed addendum",
    issue="Whether a checkbox on a website is ONB-POL-003 §2.",
    facts="The applicant ticked a website box.",
    rule="ONB-POL-003 §2.2: a website tick is not the file. DPDP consent in a tick is not the addendum (briefing).",
    application="This product chose a signed file for payer-phone storage, not a browsewrap tick. Request the file. Do not activate.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not equate a tick with the DPA.",
)

add(
    slug="pos-otp-not-dpa",
    title="POS OTP consent is not the onboarding addendum",
    issue="Whether an OTP on a POS device can replace the signed addendum.",
    facts="The applicant said customers already OTP on POS.",
    rule="ONB-POL-003 §2.2: POS consent is not the onboarding addendum.",
    application="Device-level consent, if any, is not this file. The Copilot shall not collect OTPs and shall request the signed addendum if the shop will store payer phones.",
    held="Does not satisfy. Do not collect OTP.",
    copilot="Cite ONB-POL-003 §2.2. Do not collect OTP.",
)

add(
    slug="board-resolution-not-dpa",
    title="A Companies Act board resolution is not the addendum",
    issue="Whether board minutes authorising a director to sign can replace the signed addendum file.",
    facts="The applicant uploaded a board resolution instead of the DPA.",
    rule="ONB-POL-003 §2.2: a board resolution is not the data-processing addendum. Companies Act minutes are not a fifth pack item.",
    application="Authority to sign is not the signed instrument. The Copilot shall not accept the resolution as the DPA, shall not print director identity numbers, and shall request the signed addendum.",
    held="Does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Do not print DIN/PAN.",
)

add(
    slug="dpa-other-legal-name",
    title="An addendum for another legal name does not clear this shop",
    issue="Whether a DPA executed for a group company or another shop can be reused.",
    facts="The addendum names a different legal entity than this application.",
    rule="ONB-POL-003 §2.2: an addendum executed for a different legal name is not this shop’s addendum. ONB-POL-004: this shop only.",
    application="Personal data terms do not travel across companies by group convenience. The Copilot shall not accept the other entity’s DPA and shall not pull the other shop’s files.",
    held="Does not satisfy for this shop.",
    copilot="Cite ONB-POL-003 §2.2 and ONB-POL-004. Do not reuse other shops’ files.",
)

add(
    slug="stamp-unsigned-dpa",
    title="Stamp duty does not cure a missing signature on the addendum",
    issue="Whether an unsigned addendum on stamp paper satisfies ONB-POL-003 because it is stamped under the Indian Stamp Act, 1899.",
    facts="The addendum is on stamp paper and unsigned.",
    rule="ONB-POL-003 §2.4; ONB-ANX-001: stamp duty does not replace signature. State stamp statutes likewise do not authorise Copilot activation.",
    application="Insufficient or sufficient stamping is a stamp-law question; this slot is signature. The Copilot shall not accept unsigned stamped paper and shall not activate because duty was paid.",
    held="Does not satisfy.",
    copilot="Cite ONB-ANX-001 and ONB-POL-003 §2. Do not activate.",
)

add(
    slug="incomplete-esign",
    title="An incomplete electronic-signature ceremony does not clear the addendum",
    issue="Whether starting eSign or DocuSign, without completion, is a signed addendum.",
    facts="The applicant started an eSign ceremony and did not finish.",
    rule="ONB-POL-003 §2.4; ONB-ANX-001: an incomplete electronic signature ceremony does not clear the slot. IT Act recognition of e-sign requires a completed signature, not a pending mailer.",
    application="Pending is unsigned. The Copilot shall not treat an email from a signing platform as the file, shall not print signer OTPs, and shall wait for a completed signed file if phones will be stored.",
    held="Does not satisfy until the signed file exists.",
    copilot="Cite ONB-POL-003 §2.4. Do not print OTPs from the ceremony.",
)

add(
    slug="wet-signature-blank-paper",
    title="A wet signature on blank paper is not the addendum",
    issue="Whether a photographed signature without the addendum terms satisfies ONB-POL-003 §2.",
    facts="The applicant uploaded a signature on otherwise blank paper.",
    rule="ONB-ANX-001: a signature without the addendum terms is not the addendum.",
    application="A mark without terms is not the processing agreement. The Copilot shall not accept it and shall not store the image as if it were PII-authorising.",
    held="Does not satisfy.",
    copilot="Cite ONB-ANX-001. Request the signed addendum file.",
)

add(
    slug="phones-not-stored-no-dpa",
    title="If the shop will not store payer phones, do not demand the addendum",
    issue="Whether the Copilot should still collect a DPA when the merchant states they will not store payer telephone numbers.",
    facts="The merchant stated they will not store payer phones.",
    rule="ONB-POL-003 §2.3: if the shop will not store payer telephone numbers, the Copilot shall not request the addendum.",
    application="Demanding a DPA anyway would add a fifth-like obstacle this policy forbade. The Copilot shall not request the addendum on these facts, shall not print phones, and still shall not activate. Pack items in ONB-POL-001 §2 remain.",
    held="Do not request the addendum if phones will not be stored. Still no Copilot activation.",
    copilot="Cite ONB-POL-003 §2.3. Do not invent a DPA slot. Do not activate.",
)

add(
    slug="gdpr-sentence-not-dpa",
    title="A GDPR-compliance sentence is not the Indian signed addendum",
    issue="Whether claiming GDPR compliance replaces ONB-POL-003 §2.",
    facts="The note says the shop is GDPR compliant.",
    rule="ONB-POL-003 §2.2: ‘we are GDPR compliant’ is not the addendum. DPDP is the Indian statute in the briefing library; a file is still required if phones will be stored.",
    application="Foreign-regime marketing copy is untrusted as a waiver. Request the signed file if phones will be stored. Do not print customer lists offered as GDPR evidence.",
    held="GDPR sentence does not satisfy.",
    copilot="Cite ONB-POL-003 §2.2. Request the signed file if applicable.",
)
