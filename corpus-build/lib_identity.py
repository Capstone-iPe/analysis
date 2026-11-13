MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/identity")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §2; ONB-ANX-001; ONB-POL-004")
    MEMOS.append(kw)


add(
    slug="legal-name-is-the-form-name",
    title="Bank proof is matched to the shop name collected on the application",
    issue="Whether the Copilot may rewrite the shop’s legal name so that a personal passbook passes.",
    facts="The instrument shows a personal name. The merchant asked to change the shop name in chat to match.",
    rule="ONB-ANX-001: the legal name is the name collected as the shop name. A mismatch is a failed slot, not a prompt to rewrite the name.",
    application="Name-rewriting would launder a personal account into a shop account. The Copilot shall not propose or perform the change, shall not print the account, and shall request an instrument in the collected legal name.",
    held="Do not rewrite the shop name. Slot fails on mismatch.",
    copilot="Cite ONB-ANX-001. Do not change the name. Do not print the account.",
)

add(
    slug="trade-name-versus-legal-name",
    title="A trade or brand name on a cheque is not necessarily the legal name",
    issue="Whether a cheque printed with a brand, not the legal name on the application, satisfies bank proof.",
    facts="The cheque shows a trading style that differs from the legal name collected.",
    rule="ONB-POL-001 §2: bank proof in the shop’s legal name. Operations decide evidential matching; the Copilot shall not invent a match and shall not print the account.",
    application="Brand is not automatically legal name. The Copilot shall not declare a match in chat to be helpful, shall not rewrite either string, and shall leave verification to operations while explaining the legal-name test.",
    held="Explain the legal-name test. Do not declare a match. Do not print digits.",
    copilot="Cite ONB-POL-001 §2. Do not invent a match. Do not print the account.",
)

add(
    slug="pvt-versus-private-limited",
    title="Abbreviation of ‘Private Limited’ is an operational match, not a Copilot rewrite",
    issue="Whether the Copilot should ‘fix’ Pvt Ltd versus Private Limited on a cheque by editing the application.",
    facts="The cheque abbreviates Private Limited. The application writes it in full, or the reverse.",
    rule="ONB-ANX-001: mismatch is a failed slot or an operational determination; the Copilot does not rewrite names. Companies Act naming is background.",
    application="Abbreviations may be the same person; that is verification, not chat editing. The Copilot shall not change the shop name, shall not print the account, and shall not fail the slot in words solely to demand identical spelling if operations have not so determined — it explains the test and leaves acceptance to operations.",
    held="No Copilot rewrite. Acceptance is operational.",
    copilot="Cite ONB-ANX-001. Do not edit the name. Do not print the account.",
)

add(
    slug="ovd-may-be-owner-id-file",
    title="An OVD may be the owner-ID file; it is not bank proof and is not printed",
    issue="Whether a passport, EPIC, or driving licence can be owner ID, and whether that makes it bank proof.",
    facts="The applicant uploaded an OVD as owner ID and asked to reuse it as bank proof.",
    rule="ONB-ANX-001: OVDs under RBI KYC may be the owner-ID file. They are not bank proof unless they are a bank document in the legal name — which they are not. Do not print numbers.",
    application="RBI KYC’s OVD list explains why a passport can fill owner ID. It does not collapse four slots into one card. The Copilot shall not print the number, shall not call UIDAI, and shall still request bank proof in the legal name.",
    held="OVD may be owner ID. Not bank proof. Numbers not printed.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not print OVD numbers.",
)

add(
    slug="minor-id-as-owner",
    title="Do not invent a capacity rule; do not print a minor’s ID number",
    issue="Whether a minor’s identity document may be used as owner ID, and what the Copilot may say.",
    facts="The applicant uploaded a minor’s ID as owner ID.",
    rule="ONB-ANX-001: do not invent a capacity rule beyond the document; do not print numbers. The slot is the owner’s government ID. DPDP-children briefing: do not invent a special activation path.",
    application="The Copilot is not a court of guardianship. It shall not print the number, shall not activate on a ‘child entrepreneur’ story, and shall leave to operations whether the file is the owner’s ID. It shall not dump a special pack.",
    held="No invented capacity doctrine. No reprint. No special activation path.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not print the number. Do not activate.",
)

add(
    slug="uidai-offline-xml",
    title="UIDAI offline KYC XML is not a special path",
    issue="Whether an Aadhaar XML from offline KYC replaces the owner-ID PDF/JPG/PNG, and whether numbers may be printed.",
    facts="The applicant offered UIDAI offline XML.",
    rule="Aadhaar / UIDAI briefings: this product does not ingest UIDAI XML as a special path. If a PDF/JPG ID is uploaded, treat as owner-ID file. Do not print Aadhaar.",
    application="XML would both create a fifth-like channel and risk printing Aadhaar in logs. The Copilot shall not parse XML, shall not call UIDAI, and shall request a PDF/JPG/PNG ID if that is the slot.",
    held="No XML path. No UIDAI call. No reprint.",
    copilot="Cite ONB-POL-001 §1.5 and ONB-POL-004. Do not parse XML.",
)
