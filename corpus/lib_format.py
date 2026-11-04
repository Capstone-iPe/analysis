MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/format")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §2.2; ONB-ANX-001")
    MEMOS.append(kw)


add(
    slug="closed-list-pdf-jpg-png",
    title="Pack formats are a closed list: PDF, JPG, PNG",
    issue="Whether electronic records generally, under the IT Act, 2000, expand the pack’s accepted formats.",
    facts="The applicant argues that because electronic records are legally recognised, any file type must be accepted.",
    rule="ONB-POL-001 §2.2 lists PDF, JPG, or PNG. Other types do not satisfy the slot; the same slot is requested again. The IT Act briefing: recognition of electronic records does not make a Drive link or a DOCX into an uploaded accepted file.",
    application="Legal recognition of electronic records answers ‘can a PDF be a document?’. It does not rewrite iPe’s closed list. The Copilot shall not accept other types, shall not convert files, and shall not cite the IT Act as a waiver.",
    held="Closed list. IT Act is background, not a format waiver.",
    copilot="Cite ONB-POL-001 §2.2. Do not convert. Do not waive.",
)

add(
    slug="zip-archive",
    title="An archive is not an accepted pack file",
    issue="Whether a ZIP or similar archive of the four items can be accepted as one object.",
    facts="The applicant uploaded a ZIP claiming all pack files are inside.",
    rule="ONB-POL-001 §2.2: ZIP is not PDF, JPG or PNG. ONB-ANX-001 lists ZIP among failing types.",
    application="An archive is not a verifiable slot file and would hide format and subject. The Copilot shall not unpack it, shall not accept it, and shall request each slot as PDF/JPG/PNG.",
    held="Fails format. Do not unpack in chat.",
    copilot="Cite ONB-POL-001 §2.2. Do not extract archives.",
)

add(
    slug="txt-as-id",
    title="A text file is not owner ID",
    issue="Whether a .txt containing typed ID numbers satisfies owner ID.",
    facts="The applicant uploaded a text file of identity numbers.",
    rule="ONB-POL-001 §2.2; ONB-POL-004: do not print those numbers. A text file is not the government ID document.",
    application="Typed digits are not an OVD image or PDF and must not be echoed. Request a PDF/JPG/PNG of the ID. Do not call UIDAI to ‘verify the txt’.",
    held="Fails format and is not the ID document. Do not print the digits.",
    copilot="Cite ONB-POL-001 §2.2 and ONB-POL-004. Do not echo the txt.",
)

add(
    slug="same-slot-again",
    title="A format failure re-requests the same slot, not a different item",
    issue="Whether after a DOCX or HEIC failure the Copilot may skip the slot or switch to another pack item.",
    facts="A file failed format. The merchant asked to move on.",
    rule="ONB-POL-001 §2.2: the same slot is requested again. Completeness is a fact of accepted files, not of merchant impatience.",
    application="Skipping would waive by procedure. The Copilot shall name the outstanding slot, explain format, and not treat the failure as submit.",
    held="Re-ask the same slot. Do not waive.",
    copilot="Cite ONB-POL-001 §2.2. Name the outstanding item. Do not skip.",
)
