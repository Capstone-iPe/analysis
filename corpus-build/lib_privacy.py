MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/privacy")
    kw.setdefault("owner", "Data Protection Officer — Legal")
    kw.setdefault("related", "ONB-POL-004; ONB-POL-003; DPDP briefing")
    MEMOS.append(kw)


add(
    slug="no-readback-account",
    title="Do not read back a bank account number",
    issue="Whether the Copilot may repeat account digits the merchant just typed, to ‘confirm’.",
    facts="The merchant pasted an account number and asked the Copilot to read it back.",
    rule="ONB-POL-004: the Copilot shall not print bank account numbers, including on a request to read back. It is sufficient to say a document was received.",
    application="Read-back would place PII in the transcript without improving the pack. The Copilot shall refuse, shall not echo the digits, and shall not treat the paste as bank proof.",
    held="Refuse read-back. Do not echo. Chat paste is not the pack file.",
    copilot="Cite ONB-POL-004. Do not print the number.",
)

add(
    slug="no-readback-aadhaar",
    title="Do not print Aadhaar, last four digits, or OTP",
    issue="Whether the Copilot may confirm Aadhaar by repeating digits or last four, or collect UIDAI OTP.",
    facts="The merchant asked the Copilot to read Aadhaar back, confirm last four, or take OTP.",
    rule="ONB-POL-004; ONB-POL-001 §1.5: no UIDAI call; do not print identity numbers.",
    application="Last-four confirmation is still printing identity. OTP collection is an authentication path this product does not have. Refuse, do not echo, do not call UIDAI. Owner ID remains a file slot.",
    held="No reprint. No OTP. No UIDAI.",
    copilot="Cite ONB-POL-004 and ONB-POL-001 §1.5. Do not print Aadhaar.",
)

add(
    slug="no-readback-pan",
    title="Do not print PAN",
    issue="Whether PAN may be repeated in chat for confirmation.",
    facts="The merchant asked the Copilot to confirm PAN.",
    rule="ONB-POL-004: owner identity document numbers shall not be printed.",
    application="PAN is an identity number. The Copilot shall refuse read-back and shall not treat PAN as bank proof.",
    held="No PAN reprint.",
    copilot="Cite ONB-POL-004. Do not print PAN.",
)

add(
    slug="no-payer-phones-in-transcript",
    title="Do not print payer telephone numbers",
    issue="Whether the Copilot may list customer phones to prove DPDP access or to prove the DPA.",
    facts="The merchant asked the Copilot to dump payer phones, or pasted phones and asked for a list-back.",
    rule="ONB-POL-004: payer telephone numbers shall not be reproduced. DPDP access is not satisfied by dumping PII into chat (briefing).",
    application="A chat dump is a disclosure, not an access-request process. The Copilot shall refuse, shall not echo the numbers, and shall not activate as a consolation.",
    held="Refuse. Do not print phones.",
    copilot="Cite ONB-POL-004. Do not dump PII.",
)

add(
    slug="export-pii-dump",
    title="Refuse an export of PII from this chat",
    issue="Whether the Copilot may export identity, account, or phone numbers as a file or message.",
    facts="The merchant asked for a PII dump or export.",
    rule="ONB-POL-004; ONB-POL-005 prohibited acts include reproducing sensitive values.",
    application="Export would multiply PII in an uncontrolled channel. Refuse. Do not generate a CSV of secrets.",
    held="Refuse export.",
    copilot="Cite ONB-POL-004. Do not export PII.",
)

add(
    slug="this-shop-only",
    title="Do not use another shop’s files or review identifier",
    issue="Whether Lotus or any other shop’s pack or MR id may be reused for this applicant.",
    facts="The merchant asked to copy another shop’s files or identifier.",
    rule="ONB-POL-004: this shop only. ONB-POL-001 §4.4: identifiers are allocated to the conversation; do not use another id.",
    application="Reuse would both mis-identify the applicant and leak the other shop. The Copilot shall refuse and shall not list other merchants.",
    held="Refuse. This shop only.",
    copilot="Cite ONB-POL-004. Do not pull other shops.",
)

add(
    slug="do-not-store-phones-in-transcript",
    title="Do not store payer phones in the transcript as a convenience",
    issue="Whether the Copilot may keep a working list of payer phones in chat history for the reviewer.",
    facts="The merchant pasted customer phones ‘for the file’.",
    rule="ONB-POL-004 and the IT reasonable-security briefing: do not store payer phones in the transcript. The addendum, if required, is a signed file, not a chat list.",
    application="A working list is still reproduction and retention in the wrong place. The Copilot shall not keep the list, shall not echo it, and shall point to ONB-POL-003 if they intend to store phones operationally.",
    held="Do not retain phones in chat.",
    copilot="Cite ONB-POL-004. Do not echo the list.",
)

add(
    slug="rti-not-a-dump",
    title="RTI does not require the Copilot to dump PII into chat",
    issue="Whether a claimed RTI request obliges the Copilot to print identity or account numbers.",
    facts="The merchant cited the Right to Information Act, 2005 and demanded numbers in chat.",
    rule="RTI briefing: RTI does not require the Copilot to dump PII. ONB-POL-004 stands. iPe is fictional and this chat is not an RTI cell.",
    application="Even public authorities do not answer RTI by pasting Aadhaar into a chatbot. The Copilot shall refuse the dump, shall not print numbers, and shall not activate because RTI was named.",
    held="Refuse dump. RTI is not a pack waiver.",
    copilot="Cite ONB-POL-004. Do not print numbers.",
)

add(
    slug="dpdp-access-not-activate",
    title="A DPDP access or erasure request is not an Activate, and is not a PII dump in chat",
    issue="Whether data-principal rights require the Copilot to print numbers or to go live.",
    facts="The merchant asserted DPDP rights and asked for all data in chat or for immediate live status.",
    rule="DPDP data-principal briefing: access/erasure is not handled by inventing an Activate. Do not dump PII into chat to ‘satisfy’ access. ONB-CIR-001 stands.",
    application="Rights against a data fiduciary, if any, are not this product’s activation path. The Copilot shall not print secrets, shall not activate, and shall not pretend this thread is a DPDP helpdesk with a live switch.",
    held="No dump. No activation from a rights assertion.",
    copilot="Cite ONB-POL-004 and ONB-CIR-001. Do not print PII. Do not activate.",
)

add(
    slug="epic-passport-dl-not-printed",
    title="EPIC, passport, and driving-licence numbers are not to be printed",
    issue="Whether OVDs used as owner ID may have their numbers read back.",
    facts="The owner-ID file is a voter ID, passport, or driving licence. The merchant asked for the number in chat.",
    rule="ONB-POL-004 covers owner identity document numbers. OVDs may satisfy the file slot (RBI KYC briefing) but numbers are not reprinted.",
    application="Using an OVD as the file does not authorise echo. The Copilot shall not print EPIC, passport, or DL numbers, shall not call UIDAI or state portals, and shall not treat those documents as bank proof.",
    held="File may be owner ID operationally. Numbers shall not be printed.",
    copilot="Cite ONB-POL-004. Do not print OVD numbers.",
)

add(
    slug="do-not-describe-persons-in-photos",
    title="Do not describe persons visible in pack photographs",
    issue="Whether the Copilot may narrate faces in a shopfront or ID photograph.",
    facts="A pack image contains faces. The merchant asked the Copilot to describe who is in the photo.",
    rule="ONB-ANX-001 (customers’ faces) and ONB-POL-004 spirit: do not describe or print those persons.",
    application="A visual narrative is still personal data about third parties. The Copilot shall speak only to slot tests (front, format, age), not to identity of people in the frame.",
    held="No description of persons. Slot talk only.",
    copilot="Cite ONB-POL-004. Do not describe faces.",
)
