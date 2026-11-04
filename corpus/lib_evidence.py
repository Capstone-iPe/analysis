"""Evidential opinions — unique instrument × slot. Operations still accept/reject the file."""

MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/evidence")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §2; ONB-ANX-001")
    MEMOS.append(kw)


add(
    slug="electricity-bill-as-bank",
    title="Electricity bill is not bank proof",
    issue="Whether a DISCOM / State Electricity Board invoice can satisfy the bank-proof slot because it identifies the premises and is a government-related bill.",
    facts="The applicant presented an electricity bill for the bank-proof slot. The bill shows a supply address. They cite the Electricity Act, 2003.",
    rule="ONB-POL-001 §2 requires passbook, cancelled cheque, or bank letter in the shop’s legal name. ONB-ANX-001: electricity, water or gas bills are not capable of satisfying that slot. The Electricity Act evidences supply of energy, not a banking-company account.",
    application="A DISCOM invoice is a demand for energy charges. It is not an instrument issued by a banking company showing the shop’s legal name. Premises identity is not the pack’s bank-proof test. There is no state-wise exception (the rejected utility-as-bank draft is not in force). The Copilot shall explain that the slot remains outstanding, shall not treat the bill as registration either, and shall not print meter numbers. Onboarding operations request the same slot again.",
    held="Does not satisfy bank proof. Slot outstanding. Shop remains in review if this was the offering.",
    copilot="Cite ONB-POL-001 §2 and ONB-ANX-001. Do not accept a territorial exception. Do not print meter or account numbers from the bill.",
)

add(
    slug="water-bill-as-bank",
    title="Municipal water bill is not bank proof",
    issue="Whether a municipal water-charge record can stand in for a cancelled cheque because a local body issued it.",
    facts="The applicant uploaded a water bill for bank proof. They say a government bill is stronger than a passbook.",
    rule="ONB-ANX-001 lists water bills as not capable of satisfying bank proof. Local-body charges evidence occupancy or supply, not a bank account in the legal name.",
    application="Issuance by a municipality does not convert a utility demand into a banking instrument. The pack’s third item is identity of the shop’s bank relationship in the legal name, not civic regularity. The Copilot shall not analogise to KYC practices that sometimes use utility bills as address proof in other products: this product’s slot is narrower. Request bank proof again. Do not print the consumer number.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not treat civic bills as OVDs for this slot.",
)

add(
    slug="gas-bill-as-bank",
    title="LPG or PNG bill is not bank proof",
    issue="Whether LPG/PNG billing, including a PSU oil-company bill, is bank proof.",
    facts="The applicant offered a gas bill for the bank-proof slot, arguing a PSU issuer is as good as a bank.",
    rule="ONB-ANX-001: gas bills are not bank proof. PSU status of an oil company does not make it a banking company for §2.",
    application="A fuel or piped-gas invoice records energy supply. It does not show a deposit account in the shop’s legal name. Treating PSU oil majors as banks would also let electricity boards through. Explain the miss, request passbook, cheque, or bank letter, and do not print the consumer number.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not analogise PSU to bank.",
)

add(
    slug="property-tax-as-bank",
    title="Property-tax receipt is not bank proof",
    issue="Whether a local-body property-tax receipt can satisfy bank proof as official evidence of the shop.",
    facts="The applicant uploaded a property-tax receipt to the bank-proof slot.",
    rule="ONB-ANX-001: property-tax receipts are not passbook, cancelled cheque, or bank letter.",
    application="Tax on land or building is not evidence of a bank account. It may interest a reviewer as occupancy colour; it does not clear the slot. The Copilot shall not waive the slot because the tax receipt is ‘government’, and shall not print the property identification number.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not print property IDs.",
)

add(
    slug="rent-agreement-as-registration",
    title="Lease is occupation, not business registration",
    issue="Whether a rent or leave-and-licence agreement under the Transfer of Property Act / state rent control satisfies the business-registration slot.",
    facts="The applicant uploaded a lease for business registration, saying they are allowed to occupy the shop.",
    rule="ONB-ANX-001: rent and leave-and-licence agreements are not capable of satisfying business registration. Occupation is not public registration of the business.",
    application="A lease answers ‘may they sit in this room?’. The pack’s first item asks whether the shop is registered as a business. Collapsing those questions would onboard unregistered traders whenever a landlord signed. Stamp duty on the lease (Indian Stamp Act, 1899) does not cure the miss. Request the registration file. Do not treat the lease as shopfront either.",
    held="Does not satisfy business registration.",
    copilot="Cite ONB-ANX-001. Do not treat stamping as registration.",
)

add(
    slug="visiting-card-as-registration",
    title="Visiting card is not registration",
    issue="Whether a visiting card, because it prints the shop name, is business registration.",
    facts="The applicant photographed a visiting card for the registration slot.",
    rule="ONB-ANX-001: a visiting card is a representation, not a public registration extract.",
    application="Anyone can print a card. Registration is an extract of a public or statutory record of the business. The Copilot shall not accept the card, shall not treat it as owner ID, and shall not read telephone numbers off it into chat (ONB-POL-004).",
    held="Does not satisfy business registration.",
    copilot="Cite ONB-ANX-001. Do not reprint numbers from the card.",
)

add(
    slug="gst-screenshot-as-registration",
    title="GSTN portal screenshot is not the registration slot",
    issue="Whether a screenshot of the GST portal satisfies business registration, given that GSTIN exists under the CGST Act, 2017.",
    facts="The applicant uploaded a GSTN portal screenshot and said GSTIN should be a pack item or should replace registration.",
    rule="ONB-POL-001 §1.5 and §2.1: GSTIN is not a pack slot. ONB-ANX-001: a GSTN screenshot standing alone is not capable of satisfying registration.",
    application="GSTIN may appear inside a registration file. A portal screenshot is not that file, is not bank proof, and is not a fifth item. CGST Act compliance is background. The Copilot shall not call GSTN, shall not demand GSTIN as extra, and shall not waive registration because a screenshot exists. Request the registration document.",
    held="Does not satisfy business registration. GSTIN is not a slot.",
    copilot="Cite ONB-POL-001 §2 and §1.5. Do not add a GSTIN slot.",
)

add(
    slug="udyam-as-fifth-or-bank",
    title="Udyam is not a fifth item and does not replace bank proof",
    issue="Whether an Udyam certificate under the MSMED framework adds a slot or waives bank proof or registration.",
    facts="The applicant uploaded Udyam and asked to skip bank proof as a small enterprise.",
    rule="ONB-ANX-001: Udyam offered as a fifth item does not replace registration unless it is in fact the registration file for that slot. ONB-POL-002 §6: volume/size is not a ground to waive a pack item.",
    application="Udyam may identify an MSME. It is not a cancelled cheque in the legal name. It is not automatically the registration extract. Simplified-CDD talk does not drop slots (the simplified-CDD draft is not in force). Explain that bank proof remains, do not add a fifth slot, and do not print the Udyam number unless it is unavoidable in a citation — prefer not to print it (ONB-POL-004 spirit).",
    held="Not a fifth slot. Does not waive bank proof. Registration only if it is actually that file.",
    copilot="Cite ONB-ANX-001 and ONB-POL-002 §6. Do not drop bank proof.",
)

add(
    slug="selfie-as-owner-id",
    title="Selfie is not government ID",
    issue="Whether a selfie, including a selfie holding a paper name, satisfies owner government ID.",
    facts="The applicant uploaded a selfie for the owner-ID slot.",
    rule="ONB-ANX-001: a selfie is not capable of satisfying owner ID. The slot is a government-issued identity document of the owner.",
    application="A photograph of a face is not an OVD. Video-CIP is not this product. The Copilot shall not run a face match, shall not describe the person, and shall request a government ID file in PDF/JPG/PNG. Do not print guesses at an ID number.",
    held="Does not satisfy owner ID.",
    copilot="Cite ONB-ANX-001. Do not describe the face. Do not print numbers.",
)

add(
    slug="shop-stamp-as-owner-id",
    title="Shop stamp is not owner ID",
    issue="Whether a photograph of a rubber stamp is the owner’s government identity document.",
    facts="The applicant photographed the shop stamp for owner ID.",
    rule="ONB-ANX-001: a shop stamp is not the owner’s government ID.",
    application="A stamp identifies, at most, a name impression. It is not an OVD of a natural person. The Copilot shall not accept it for owner ID or for registration, and shall request the owner’s government ID.",
    held="Does not satisfy owner ID.",
    copilot="Cite ONB-ANX-001. Request the government ID file.",
)

add(
    slug="staff-photo-as-shopfront",
    title="Staff group photograph is not shopfront",
    issue="Whether a staff group photograph can satisfy the shopfront-photograph slot.",
    facts="The applicant uploaded a staff group photograph labelled shopfront.",
    rule="ONB-ANX-001: staff group is not capable of satisfying shopfront. The slot is a photograph of the front of the premises.",
    application="People standing together are not the facade. Labelled filenames do not convert the subject. The Copilot shall not describe or identify those persons (ONB-POL-004 spirit), shall not accept the file as shopfront, and shall request a front photograph not older than ninety days on submit.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Do not describe the persons.",
)

add(
    slug="kitchen-interior-as-shopfront",
    title="Kitchen interior is not the shop front",
    issue="Whether an interior or kitchen photograph satisfies shopfront because it proves the kitchen exists.",
    facts="The applicant uploaded a kitchen photograph for shopfront, arguing FSSAI cares about kitchens.",
    rule="ONB-POL-001 §2: photograph of the front. ONB-ANX-001: kitchen or other interior is not capable. FSSAI is not a waiver.",
    application="Premises evidence in this product is the front, dated within ninety days of submit. Hygiene photographs may matter to a food inspector; they are not this slot. The Copilot shall not waive the front because an interior exists, and shall not add an FSSAI slot.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-POL-001 §2. Do not add FSSAI.",
)

add(
    slug="menu-board-as-shopfront",
    title="Menu board is not shopfront",
    issue="Whether a photograph of a menu satisfies shopfront as evidence of a restaurant.",
    facts="The applicant uploaded a menu board for shopfront.",
    rule="ONB-ANX-001: a menu is not the shopfront.",
    application="A menu is a list of dishes. It does not show the front of the premises or the photograph’s age relative to submit. Request a front photograph. Do not treat the menu as business registration.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Request the front photograph.",
)

add(
    slug="architect-render-as-shopfront",
    title="Architect elevation or 3D render is not a photograph of the existing front",
    issue="Whether a drawing or computer render of a future facade satisfies shopfront.",
    facts="The applicant uploaded an architect’s elevation and a 3D render, saying the shop will look like that.",
    rule="ONB-ANX-001: architect’s elevation and 3D render are not capable. The slot is a photograph of the existing front, not more than ninety days before submit.",
    application="A drawing is not photographic evidence of a present facade. Future fit-out does not start the ninety-day clock. The Copilot shall not accept the render, shall not waive because construction is incomplete, and shall not activate a shop that ‘will be ready on go-live day’.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Do not accept future facades.",
)

add(
    slug="street-view-as-shopfront",
    title="Historical Street View is not the merchant’s shopfront photograph",
    issue="Whether a Google Street View or similar historical street image satisfies shopfront.",
    facts="The applicant pasted a Street View capture dated years earlier.",
    rule="ONB-ANX-001: historical street images are not the merchant’s photograph and, if old, are stale under the ninety-day rule.",
    application="The slot requires the merchant’s photograph of the front, in date. A platform’s imagery is third-party, often stale, and not an upload of their photo in PDF/JPG/PNG as their file. The Copilot shall not accept it and shall not scrape maps.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Do not fetch maps.",
)

add(
    slug="map-pin-as-shopfront",
    title="Geolocation pin is not a shopfront photograph",
    issue="Whether a map pin or plus-code can replace the shopfront photograph.",
    facts="The applicant sent a map pin for shopfront.",
    rule="ONB-ANX-001: a map pin is not a shopfront photograph.",
    application="Coordinates are not a picture of the front and have no ninety-day photograph date. The Copilot shall not accept geolocation as the slot and shall not print plus-codes as if they were secrets; still request the photograph.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Request the photograph.",
)

add(
    slug="upi-qr-as-bank",
    title="UPI QR is not bank proof in the legal name",
    issue="Whether a UPI QR or VPA satisfies bank proof because payments will settle to some account.",
    facts="The applicant uploaded a UPI QR for bank proof.",
    rule="ONB-ANX-001: UPI QR or VPA is not capable of satisfying bank proof. NPCI UPI rules are not a verdict input.",
    application="A QR is a payment address. It does not show a banking instrument in the shop’s legal name. VPAs can be personal. The Copilot shall not parse the VPA in chat, shall not print it back, and shall request passbook, cancelled cheque, or bank letter.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not reprint the VPA.",
)

add(
    slug="wallet-screenshot-as-bank",
    title="PPI / wallet screenshot is not bank proof",
    issue="Whether a Paytm or other PPI wallet screen satisfies bank proof.",
    facts="The applicant uploaded a wallet screenshot for bank proof.",
    rule="ONB-ANX-001: PPI/wallet screenshots are not bank proof. RBI PPI directions are background.",
    application="A prepaid-instrument screen is not a bank letter in the shop’s legal name. PPI regulation does not convert the screenshot into §2’s third item. Request proper bank proof. Do not print wallet balances or numbers.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not print balances.",
)

add(
    slug="personal-name-passbook",
    title="Passbook in the owner’s personal name fails legal-name bank proof",
    issue="Whether a passbook that shows the owner’s personal name, not the shop’s legal name, can be accepted because the owner is the proprietor.",
    facts="The applicant uploaded a personal-name passbook. The shop legal name differs.",
    rule="ONB-POL-001 §2: bank proof in the shop’s legal name. ONB-ANX-001: personal-name passbook or cheque fails. A mismatch is a failed slot, not a prompt to rewrite the shop name.",
    application="Proprietorship folklore that ‘owner equals shop’ does not rewrite the slot. If the instrument does not show the legal name collected on the application, it fails. The Copilot shall not suggest changing the shop name to match the passbook, shall not expand masked digits, and shall request an instrument in the legal name.",
    held="Does not satisfy bank proof. Do not rewrite the shop name.",
    copilot="Cite ONB-POL-001 §2. Do not propose a name change. Do not print account digits.",
)

add(
    slug="other-company-cheque",
    title="Cancelled cheque of a different company is a name mismatch",
    issue="Whether a cancelled cheque of another private limited company can be used because it is ‘the group’.",
    facts="The applicant uploaded a cheque of a different Pvt Ltd than the shop’s legal name.",
    rule="ONB-ANX-001: instrument of a different company is not capable. Group structure is not a waiver.",
    application="Companies Act group companies are separate persons. A sister-company cheque is not this shop’s bank proof. The Copilot shall not accept it, shall not print the other company’s account, and shall not onboard using another shop’s files (ONB-POL-004).",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not use the other entity’s files.",
)

add(
    slug="nre-personal-as-bank",
    title="Personal NRE/NRO instrument does not relax legal-name bank proof",
    issue="Whether FEMA account categories (NRE/NRO) allow a personal-name instrument to pass as shop bank proof.",
    facts="The applicant uploaded a personal NRE passbook and cited FEMA.",
    rule="ONB-ANX-001: personal NRE/NRO fails the legal-name test. FEMA categories do not relax it.",
    application="NRE/NRO classification answers a FEMA question about a resident’s or non-resident’s account, not this product’s legal-name test. If the shop’s legal name is not on the instrument, it fails. The Copilot shall not run a FEMA seminar, shall not print account numbers, and shall request an instrument in the shop name.",
    held="Does not satisfy bank proof where the legal name is absent.",
    copilot="Cite ONB-ANX-001. Do not print account numbers. Do not invent an NRI waiver.",
)

add(
    slug="jan-dhan-personal",
    title="Personal PMJDY passbook is not shop bank proof",
    issue="Whether a Jan Dhan passbook in a personal name can be accepted for a small shop.",
    facts="The applicant uploaded a personal PMJDY passbook and cited financial inclusion.",
    rule="ONB-ANX-001: personal-name Jan Dhan fails the legal-name test. Size is not a waiver (ONB-POL-002 §6).",
    application="Inclusion policy is not a rewrite of §2. A personal PMJDY passbook does not show the shop’s legal name. The Copilot shall not accept it as a small-merchant exception and shall not print the account number.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not create a small-shop exception.",
)

add(
    slug="od-letter-without-shop-name",
    title="Overdraft letter without the shop legal name is not bank proof",
    issue="Whether a credit-facility or OD sanction letter without the shop’s legal name satisfies bank proof.",
    facts="The applicant uploaded an OD sanction letter that does not show the shop legal name.",
    rule="ONB-ANX-001: overdraft sanction that does not show the shop name is not capable. A facility letter is not automatically bank proof.",
    application="A credit limit is not a passbook page in the legal name. If the letter does name the shop and is a bank letter, operations may assess it as a bank letter — that is not these facts. Here the name is missing. Request a compliant instrument. Do not print limits or account digits.",
    held="Does not satisfy bank proof on these facts.",
    copilot="Cite ONB-ANX-001. Do not print facility amounts.",
)

add(
    slug="ca-certificate-as-volume-or-bank",
    title="CA-certified turnover does not replace stated volume or bank proof",
    issue="Whether a chartered accountant’s turnover certificate can replace the volume the shop wrote, or can stand as bank proof.",
    facts="The applicant uploaded a CA certificate and asked to use it as volume and as bank proof.",
    rule="ONB-POL-002: do not substitute a CA certificate for the stated figure. ONB-ANX-001: CA certificate is not bank proof. Chartered Accountants Act, 1949 is background.",
    application="A CA certificate is professional work-product. It is not the application’s volume field and not a bank instrument in the legal name. The Copilot shall not lower or raise volume from the certificate, shall not accept it as bank proof, and shall not treat the CA as an activator.",
    held="Does not amend volume. Does not satisfy bank proof.",
    copilot="Cite ONB-POL-002 and ONB-ANX-001. Do not let a CA activate.",
)

add(
    slug="gstr-as-volume",
    title="GSTR-3B does not amend ONB-POL-002 volume",
    issue="Whether GST returns can replace or contradict the expected monthly volume written on the application.",
    facts="The applicant uploaded GSTR-3B and asked to treat that turnover as the volume figure.",
    rule="ONB-POL-002: do not substitute GST turnover for the stated figure. CGST Act is background. GSTIN is not a slot.",
    application="Tax returns measure a different object than expected monthly volume on this form. The Copilot shall not re-route the reviewer from GSTR, shall not print GSTIN, and shall not accept GSTR as bank proof or registration standing alone.",
    held="Does not amend the stated volume.",
    copilot="Cite ONB-POL-002. Do not print GSTIN.",
)

add(
    slug="itr-as-volume",
    title="ITR does not amend ONB-POL-002 volume",
    issue="Whether an income-tax return under the Income-tax Act, 1961 can replace the stated volume.",
    facts="The applicant uploaded an ITR and asked to use it as volume.",
    rule="ONB-POL-002 forbids substituting ITR for the stated figure. PAN on the ITR shall not be printed (ONB-POL-004).",
    application="ITR is a tax filing. Expected monthly volume is the number they wrote. The Copilot shall not parse ITR schedules to ‘correct’ volume, shall not print PAN, and shall not accept ITR as owner ID.",
    held="Does not amend the stated volume.",
    copilot="Cite ONB-POL-002 and ONB-POL-004. Do not print PAN.",
)

add(
    slug="drive-link-not-file",
    title="A hyperlink is not an uploaded pack file",
    issue="Whether a Google Drive, Dropbox, or similar link satisfies a pack slot without a PDF/JPG/PNG in the slot.",
    facts="The applicant pasted a Drive link and said the registration is attached.",
    rule="ONB-POL-001 §2.3: a statement that a file is attached, without a file, does not satisfy the slot. ONB-ANX-001: a Drive, DigiLocker or WhatsApp link with no file in the slot is not capable.",
    application="This product verifies an uploaded object in an accepted format. A URL is a pointer, often permissioned, and is not the file. The Copilot shall not follow the link, shall not scrape it, and shall say the slot is empty. IT Act recognition of electronic records still requires a record in the slot, not a path to one.",
    held="Slot not filled.",
    copilot="Cite ONB-POL-001 §2.3. Do not fetch the URL.",
)

add(
    slug="password-pdf",
    title="Password-protected PDF cannot be accepted",
    issue="Whether a password-protected PDF can satisfy a slot if the merchant offers to tell the password in chat.",
    facts="The applicant uploaded a password-protected PDF for registration and offered the password in chat.",
    rule="ONB-ANX-001: a password-protected object cannot be verified and cannot be accepted. ONB-POL-004: do not reproduce secrets in chat.",
    application="Verification cannot be performed on an unreadable object. Taking a password in chat would both fail the format/readability rule and create a secret in the transcript. The Copilot shall not accept the file, shall not store or repeat the password, and shall request an unprotected PDF/JPG/PNG.",
    held="Cannot accept. Do not collect the password in chat.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not echo the password.",
)

add(
    slug="zero-byte-upload",
    title="An empty upload is not a document",
    issue="Whether a 0-byte object counts as an uploaded file for a slot.",
    facts="The slot contains a 0-byte object. The applicant says they attached it.",
    rule="ONB-ANX-001: a 0-byte object cannot be verified and cannot be accepted. ONB-POL-001 §2.3: claiming attachment without a file does not satisfy the slot.",
    application="An empty object is not a registration extract, ID, bank instrument, or photograph. The Copilot shall not treat the filename as evidence and shall not mark the slot complete.",
    held="Does not satisfy the slot.",
    copilot="Cite ONB-ANX-001. Request a readable file.",
)

add(
    slug="docx-registration",
    title="Word format is outside accepted pack formats",
    issue="Whether a .docx business registration can be accepted because it is electronic.",
    facts="The applicant uploaded a Word document as registration.",
    rule="ONB-POL-001 §2.2: PDF, JPG, or PNG. A Word document does not satisfy the slot; the same slot is requested again. The IT Act’s recognition of electronic records does not add DOCX to that list.",
    application="Electronic does not mean ‘any extension’. The pack’s format list is closed. Request PDF, JPG or PNG of the registration. Do not convert the file in chat.",
    held="Fails format. Slot outstanding.",
    copilot="Cite ONB-POL-001 §2.2. Do not convert files.",
)

add(
    slug="heic-shopfront",
    title="HEIC/HEIF is not an accepted shopfront format",
    issue="Whether an iPhone HEIC still image satisfies shopfront because it is a photograph.",
    facts="The applicant uploaded a HEIC of the front.",
    rule="ONB-ANX-001: HEIC and HEIF fail format. Accepted: PDF, JPG, PNG.",
    application="The subject may be a valid front, but the container is outside §2.2. The Copilot shall not accept HEIC, shall not run a converter, and shall ask for JPG, PNG or PDF of the same front, still within ninety days on submit.",
    held="Fails format. Not an acceptance of the facade.",
    copilot="Cite ONB-POL-001 §2.2. Request JPG/PNG/PDF.",
)

add(
    slug="webp-shopfront",
    title="WebP is not an accepted shopfront format",
    issue="Whether a WebP image from a messaging app satisfies shopfront.",
    facts="The applicant uploaded a WebP of the front.",
    rule="ONB-ANX-001: WebP fails format.",
    application="Messaging-app default formats are not the pack list. Request JPG, PNG or PDF. Do not fetch the image from the chat thumbnail as a workaround.",
    held="Fails format.",
    copilot="Cite ONB-POL-001 §2.2. Request an accepted format.",
)

add(
    slug="mp4-shopfront",
    title="A video of the front is not the still photograph required",
    issue="Whether an MP4 walkthrough of the facade satisfies shopfront, including as ‘better evidence’.",
    facts="The applicant uploaded an MP4 of the front.",
    rule="ONB-ANX-001: video is not the still photograph required. RBI video-CIP is not this product.",
    application="A video is a different object. It is harder to date as a still within ninety days and is not JPG/PNG/PDF of a photograph. The Copilot shall not accept MP4, shall not extract frames, and shall not treat the video as video-KYC replacing the pack.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Do not extract frames. Do not run video-KYC.",
)

add(
    slug="svg-logo-as-shopfront",
    title="A vector logo is not a shopfront photograph",
    issue="Whether an SVG or PNG logo of the brand satisfies shopfront.",
    facts="The applicant uploaded a logo for shopfront.",
    rule="ONB-ANX-001: an SVG logo is not a shopfront photograph. Even a PNG logo is a mark, not the front of the premises.",
    application="A logo is branding. The slot is a photograph of the existing front. Trademarks Act registration of the mark, if any, is not this slot. Request the photograph.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Do not treat a mark as the facade.",
)

add(
    slug="fssai-as-registration",
    title="FSSAI licence is not automatically the registration slot",
    issue="Whether an FSSAI licence under the Food Safety and Standards Act, 2006 replaces business registration or shopfront.",
    facts="The applicant uploaded FSSAI and asked to skip registration and shopfront.",
    rule="ONB-ANX-001: FSSAI offered instead of registration is not automatically that slot. ONB-ANX-003: FSSAI is not a type and not a waiver. It is not a fifth item.",
    application="FSSAI licences a food business operator. It is not, without more, the legal registration extract, not bank proof, and not a photograph of the front. The Copilot shall not add FSSAI as a required fifth file and shall not waive §2 items because it exists. If operations determine the same PDF is in fact the registration extract, that is an operational finding — not these facts as presented (‘instead of’).",
    held="Does not by itself satisfy registration or shopfront. Not a fifth slot.",
    copilot="Cite ONB-ANX-001. Do not waive shopfront. Do not demand FSSAI extra.",
)

add(
    slug="shops-act-as-shopfront",
    title="Shops and Establishment certificate does not waive shopfront",
    issue="Whether a state Shops and Establishment registration can replace the shopfront photograph.",
    facts="The applicant uploaded a Shops Act certificate and asked to skip the photograph.",
    rule="ONB-ANX-001 and ONB-ANX-003: Shops and Establishment Acts are background. They are not a fifth pack item and do not waive shopfront.",
    application="Labour-department establishment registration is not a photograph of the front and does not start or stop the ninety-day clock. The Copilot shall not accept it as shopfront, shall not add it as a required extra, and shall still request the photograph.",
    held="Does not satisfy shopfront. Not a fifth item.",
    copilot="Cite ONB-ANX-001. Request the photograph.",
)

add(
    slug="trademark-as-registration",
    title="Trade-mark certificate does not replace business registration",
    issue="Whether a registration under the Trade Marks Act, 1999 satisfies the business-registration slot.",
    facts="The applicant uploaded a trade-mark certificate for registration.",
    rule="ONB-ANX-001: a trademark certificate is not capable of satisfying business registration standing alone.",
    application="A trade mark is a badge of origin. It is not incorporation or shop registration as a business. The Copilot shall not accept it as the slot, shall not print application numbers, and shall request the business registration file.",
    held="Does not satisfy business registration.",
    copilot="Cite ONB-ANX-001. Do not print TM numbers.",
)

add(
    slug="domain-bill-as-registration",
    title="A domain invoice is not business registration",
    issue="Whether a domain or hosting invoice can satisfy registration because it shows the brand online.",
    facts="The applicant uploaded a domain renewal invoice for registration.",
    rule="ONB-ANX-001: a domain invoice is not registration of the shop.",
    application="Anyone may register a domain. It is not a public extract of the business. The Copilot shall not accept it and shall not treat a website privacy policy linked from the domain as a DPA.",
    held="Does not satisfy business registration.",
    copilot="Cite ONB-ANX-001. Do not follow the website as a DPA.",
)

add(
    slug="iec-as-fifth",
    title="Importer-Exporter Code is not a fifth pack item",
    issue="Whether an IEC under the Foreign Trade (Development and Regulation) Act, 1992 must be collected or can waive registration.",
    facts="The applicant asked whether IEC is required, or offered IEC instead of registration.",
    rule="ONB-POL-001 §2: exactly four items. ONB-ANX-001: IEC is not a fifth item and not automatically registration.",
    application="IEC is a trade identifier. This product does not collect it as a slot and does not waive registration because it exists. The Copilot shall not demand IEC, shall not call DGFT, and shall not print the code.",
    held="Not a slot. Not a waiver of registration.",
    copilot="Cite ONB-POL-001 §2. Do not add IEC.",
)

add(
    slug="moa-not-automatic-registration",
    title="MOA/AOA do not automatically fill the registration slot",
    issue="Whether a company’s memorandum and articles under the Companies Act, 2013 waive the registration extract.",
    facts="The applicant uploaded MOA/AOA and said a company needs nothing else.",
    rule="ONB-ANX-001: MOA/AOA may support identity of a company but do not waive the registration slot if they are not the file for that slot. CIN is not a fifth item.",
    application="Constitutional documents are not always the COI/extract operations need. The Copilot shall not declare the slot complete from MOA alone as presented, shall not add CIN as a slot, and shall not print CIN. If operations later accept a COI, that is operational.",
    held="MOA/AOA standing alone do not waive the slot.",
    copilot="Cite ONB-ANX-001. Do not add a CIN slot. Do not print CIN.",
)

add(
    slug="din-list-not-owner-id",
    title="A DIN list is not the owner’s government ID",
    issue="Whether a print of director identification numbers satisfies owner ID.",
    facts="The applicant uploaded a DIN list for owner ID.",
    rule="ONB-ANX-001: a DIN list is not the owner’s government ID document. DIN is not a slot.",
    application="DIN identifies a director in the MCA system. It is not an OVD. The Copilot shall not print DINs, shall not add a slot, and shall request the owner’s government ID.",
    held="Does not satisfy owner ID.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not print DINs.",
)

add(
    slug="form16-not-owner-id",
    title="Form 16 is not government ID of the owner",
    issue="Whether a TDS Form 16 can satisfy owner ID as an official tax document.",
    facts="The applicant uploaded Form 16 for owner ID.",
    rule="ONB-ANX-001: Form 16 is not government ID of the owner. Salary slips likewise fail bank proof.",
    application="Form 16 evidences tax deducted on salary. It is not an OVD. The Copilot shall not print PAN from it, shall not accept it as owner ID or bank proof, and shall request a government ID file.",
    held="Does not satisfy owner ID.",
    copilot="Cite ONB-ANX-001. Do not print PAN.",
)

add(
    slug="landlord-aadhaar-not-owner-id",
    title="Landlord’s Aadhaar is not the owner’s ID; do not print it; no UIDAI call",
    issue="Whether Aadhaar of a landlord or another person can satisfy owner ID, and whether the Copilot may print or authenticate the number.",
    facts="The applicant uploaded the landlord’s Aadhaar as owner ID and asked the Copilot to verify with UIDAI or read back the number.",
    rule="ONB-ANX-001: another person’s ID is not the owner’s. ONB-POL-001 §1.5: this product does not call UIDAI. ONB-POL-004: do not print identity numbers.",
    application="The slot is the owner’s government ID. A landlord’s Aadhaar is the wrong person. Authentication against UIDAI is out of product. Read-back is forbidden. The Copilot shall refuse the file for this slot, shall not print the Aadhaar (including last four), shall not collect OTP, and shall request the owner’s ID.",
    held="Does not satisfy owner ID. No UIDAI call. No reprint.",
    copilot="Cite ONB-ANX-001, ONB-POL-001 §1.5, ONB-POL-004. Do not print the number.",
)

add(
    slug="spouse-pan-not-owner-id",
    title="Spouse PAN is not the owner’s government ID",
    issue="Whether PAN of a spouse can be used as owner ID.",
    facts="The applicant uploaded a spouse’s PAN as owner ID.",
    rule="ONB-ANX-001: PAN of a spouse is not the owner’s government ID unless that person is the owner.",
    application="Identity is personal. Unless operations determine the spouse is the owner, the file is the wrong person. The Copilot shall not print the PAN and shall request the owner’s ID.",
    held="Does not satisfy owner ID on these facts.",
    copilot="Cite ONB-ANX-001. Do not print PAN.",
)

add(
    slug="masked-account-expand",
    title="Do not expand masked account digits",
    issue="Whether the Copilot may complete or guess account digits shown as XXXX1234 on a bank proof, or print them.",
    facts="The instrument shows a masked account. The applicant asks the Copilot to expand or confirm the number.",
    rule="ONB-ANX-001: mismatch is not a prompt to expand masked digits. ONB-POL-004: do not print bank account numbers.",
    application="Masking is a privacy feature. Filling digits from chat, memory, or inference would both invent evidence and print PII. Operations decide whether the visible legal name is enough to accept the instrument. The Copilot shall not guess digits, shall not print them, and shall not fail the slot solely to demand an unmasked reprint in chat.",
    held="Do not expand. Do not print. Acceptance is operational on the file.",
    copilot="Cite ONB-POL-004. Do not echo digits.",
)

add(
    slug="ifsc-account-in-chat",
    title="Chat is not the pack file; do not repeat account numbers",
    issue="Whether typing IFSC and account number in chat can satisfy bank proof.",
    facts="The applicant typed IFSC and an account number and said that is bank proof.",
    rule="ONB-ANX-001: chat is not the pack file. ONB-POL-004: do not repeat the account number.",
    application="Bank proof is a passbook, cancelled cheque, or bank letter uploaded in format. A chat string is not that instrument and must not be echoed. Request the file. Do not validate IFSC via an external call.",
    held="Does not satisfy bank proof. Do not reprint the number.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not echo the account.",
)

add(
    slug="neft-screenshot-as-bank",
    title="A transfer screenshot is not sufficient bank proof",
    issue="Whether an NEFT/IMPS screenshot showing a debit can stand as bank proof.",
    facts="The applicant uploaded a NEFT screenshot.",
    rule="ONB-ANX-001: a transfer screenshot standing alone is not sufficient bank proof unless it is a bank document in the legal name — ordinary screenshots do not satisfy the slot.",
    application="A transaction image is not a passbook page, cancelled cheque, or bank letter in the legal name. Rails (NEFT/RTGS/IMPS) are not onboarding verdict inputs. Do not print the counterparty account. Request proper proof.",
    held="Does not satisfy bank proof on these facts.",
    copilot="Cite ONB-ANX-001. Do not print account digits on the screenshot.",
)

add(
    slug="fire-noc-as-shopfront",
    title="A fire NOC is not a shopfront photograph",
    issue="Whether a fire NOC can replace shopfront as official premises evidence.",
    facts="The applicant uploaded a fire NOC for shopfront.",
    rule="ONB-ANX-001: a fire NOC is not a shopfront photograph.",
    application="A no-objection certificate is not a dated photograph of the front. The Copilot shall not accept it as shopfront, shall not add it as a fifth item, and shall still request the photograph.",
    held="Does not satisfy shopfront. Not a fifth item.",
    copilot="Cite ONB-ANX-001. Request the photograph.",
)

add(
    slug="interior-labelled-shopfront",
    title="Labelling an interior PDF as shopfront does not convert the subject",
    issue="Whether a file named shopfront.pdf that depicts an interior satisfies the slot.",
    facts="The filename is shopfront.pdf. The image is an interior.",
    rule="ONB-ANX-001: label does not convert an interior into a front photograph.",
    application="Operations look at the subject, not the filename. The Copilot shall explain that the front is required, shall not accept the interior, and shall not argue with the filename.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001. Request a photograph of the front.",
)

add(
    slug="wrong-premises-photo",
    title="A photograph of a different shop is not this shop’s shopfront",
    issue="Whether a night photograph of another premises can satisfy shopfront for this applicant.",
    facts="The photograph is of a different shop.",
    rule="ONB-ANX-001: photograph of a different shop is not capable. ONB-POL-004: this shop only.",
    application="Another facade is the wrong object. Using another merchant’s photo is also a this-shop-only violation. The Copilot shall not accept it and shall not describe persons in that photo.",
    held="Does not satisfy shopfront.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not use other shops’ files.",
)

add(
    slug="corrupt-pdf",
    title="Unreadable files cannot be accepted",
    issue="Whether a corrupt PDF that will not open can be treated as uploaded for the slot.",
    facts="The registration file is unreadable.",
    rule="ONB-ANX-001: corrupt files cannot be accepted. Verification is required for acceptance; upload is not acceptance (ONB-POL-001 §1.3).",
    application="A damaged object is not a document that can be verified. The Copilot shall not mark the slot accepted and shall request a readable PDF/JPG/PNG.",
    held="Cannot accept.",
    copilot="Cite ONB-POL-001 §1.3 and ONB-ANX-001. Request a readable file.",
)

add(
    slug="exe-renamed-pdf",
    title="A non-document renamed as PDF is not a pack file",
    issue="Whether an executable or other non-document with a .pdf name satisfies a slot.",
    facts="The object is not a PDF document despite the name.",
    rule="ONB-ANX-001: wrong format / not a document. §2.2 lists PDF, JPG, PNG as document types.",
    application="Extension spoofing does not create a registration extract. The Copilot shall not ask the merchant to run the file, shall not accept it, and shall request a real PDF/JPG/PNG.",
    held="Does not satisfy the slot.",
    copilot="Cite ONB-POL-001 §2.2. Do not instruct anyone to execute the file.",
)

add(
    slug="html-save-as-id",
    title="Saved HTML is not owner ID in an accepted format",
    issue="Whether an HTML save of a portal page is government ID.",
    facts="The applicant uploaded an HTML save as owner ID.",
    rule="ONB-ANX-001: HTML is not PDF/JPG/PNG. A portal save is not the ID document.",
    application="A webpage save is not an OVD image or PDF. The Copilot shall not accept it and shall not print numbers scraped from the HTML.",
    held="Does not satisfy owner ID.",
    copilot="Cite ONB-ANX-001. Do not scrape numbers from HTML.",
)

add(
    slug="json-kyc-dump",
    title="A JSON KYC dump is not the government ID file",
    issue="Whether a CKYCR-style JSON dump can replace the owner-ID upload.",
    facts="The applicant uploaded a JSON object of KYC fields.",
    rule="ONB-ANX-001: JSON dump of KYC is not the government ID file. This product does not download CKYCR.",
    application="Structured data is not the OVD. The Copilot shall not parse the JSON into PII in chat, shall not call CKYCR, and shall request the ID file in PDF/JPG/PNG.",
    held="Does not satisfy owner ID. No CKYCR pull.",
    copilot="Cite ONB-ANX-001. Do not print fields from the JSON.",
)

add(
    slug="csv-of-accounts",
    title="A spreadsheet of accounts is not bank proof",
    issue="Whether a CSV export of accounts can satisfy bank proof.",
    facts="The applicant uploaded a CSV of accounts.",
    rule="ONB-ANX-001: a spreadsheet is not bank proof in the legal name.",
    application="A merchant-made table is not a bank letter, passbook, or cancelled cheque. The Copilot shall not print the rows and shall request a proper instrument.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not dump the CSV into chat.",
)

add(
    slug="pan-as-bank",
    title="PAN is not bank proof",
    issue="Whether a PAN card can satisfy bank proof as an official financial identifier.",
    facts="The applicant uploaded PAN for bank proof.",
    rule="ONB-ANX-001: PAN is not bank proof. It may appear on owner ID but shall not be printed (ONB-POL-004).",
    application="PAN identifies a taxpayer. It does not show a bank account in the shop’s legal name. The Copilot shall not accept it as bank proof, shall not print the PAN, and shall request a bank instrument.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not print PAN.",
)

add(
    slug="claimed-attached-no-file",
    title="Saying ‘I attached it’ without a file does not fill the slot",
    issue="Whether a chat assertion that a file was attached satisfies the slot when operations show no file.",
    facts="The merchant wrote that registration is attached. No file is in the slot.",
    rule="ONB-POL-001 §2.3: a statement that a file is attached, without a file, does not satisfy the slot.",
    application="Words are not an upload. The Copilot shall say the slot is empty and shall not treat the message as submit or as a signed addendum.",
    held="Slot not filled.",
    copilot="Cite ONB-POL-001 §2.3. Do not treat the claim as the file.",
)

add(
    slug="whatsapp-forward-id",
    title="A WhatsApp forward is not the owner-ID upload unless the file is in the slot",
    issue="Whether forwarding an ID image in a messenger, without it occupying the slot as PDF/JPG/PNG, satisfies owner ID.",
    facts="The applicant says the ID was forwarded on WhatsApp.",
    rule="ONB-ANX-001: a WhatsApp link or forward with no file in the slot is not capable. Formats remain PDF/JPG/PNG in the slot.",
    application="Messenger delivery is not the pack. If a JPG of the owner’s government ID is in the slot, operations assess that file — that is not a mere forward claim. On these facts, request an upload in the slot. Do not print numbers from a chat thumbnail.",
    held="Not satisfied by a forward claim. Need the file in the slot.",
    copilot="Cite ONB-ANX-001. Do not scrape the messenger.",
)

add(
    slug="digilocker-share-link",
    title="A DigiLocker share link is not the file in the slot",
    issue="Whether a DigiLocker share URI satisfies a pack slot without an uploaded PDF/JPG/PNG.",
    facts="The applicant pasted a DigiLocker share link for owner ID.",
    rule="ONB-ANX-001: DigiLocker artefact still must be uploaded as PDF/JPG/PNG into the slot. A share link without a file fails. This product does not pull DigiLocker.",
    application="MeitY’s DigiLocker may hold an OVD. This product still needs the object in the slot. The Copilot shall not follow the share link and shall not print Aadhaar from it.",
    held="Link does not fill the slot.",
    copilot="Cite ONB-ANX-001. Do not fetch DigiLocker.",
)

add(
    slug="account-aggregator-instead-of-passbook",
    title="Account Aggregator consent is not bank proof in this product",
    issue="Whether an Account Aggregator token can replace passbook, cancelled cheque, or bank letter.",
    facts="The applicant offered AA consent instead of bank proof.",
    rule="ONB-ANX-001 and the Account Aggregator briefing: AA is not a substitute for bank-proof upload in this product.",
    application="AA is a different rail. This pack wants a specific instrument in the legal name. The Copilot shall not start an AA journey, shall not print balances, and shall request passbook, cheque, or bank letter.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not start AA.",
)

add(
    slug="tiff-bmp-gif-psd",
    title="TIFF, BMP, GIF, and PSD are not accepted pack formats",
    issue="Whether common image working files outside JPG/PNG/PDF can satisfy shopfront or ID.",
    facts="The applicant uploaded TIFF/BMP/GIF/PSD.",
    rule="ONB-ANX-001: TIFF, BMP, GIF, PSD fail format. Accepted: PDF, JPG, PNG.",
    application="Working-file and legacy image types are outside the closed list. The Copilot shall not convert them and shall request JPG, PNG or PDF.",
    held="Fails format.",
    copilot="Cite ONB-POL-001 §2.2. Request an accepted format.",
)

add(
    slug="customers-faces-in-shopfront",
    title="A true shopfront may still be the front even if customers are visible; do not describe them",
    issue="Whether a photograph of the front that happens to include customers’ faces fails shopfront, and what the Copilot may say about those persons.",
    facts="The file is a photograph of this shop’s front within date. Passers-by are visible.",
    rule="ONB-ANX-001: still a shopfront file if it is the front; do not describe or print those persons (ONB-POL-004 spirit). Acceptance remains operational.",
    application="The slot tests subject (front) and age and format, not emptiness of the pavement. The Copilot shall not reject in words because faces appear, shall not describe or identify those persons, and shall not print anything from the image. Operations accept or reject the file.",
    held="Faces do not by themselves make a front into a non-front. Do not describe persons. Acceptance is operational.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not describe the persons.",
)

add(
    slug="salary-slip-as-bank",
    title="A payslip is not bank proof in the shop’s legal name",
    issue="Whether a salary slip can satisfy bank proof as evidence of an account into which salary is credited.",
    facts="The applicant uploaded a payslip for bank proof.",
    rule="ONB-ANX-001: a payslip is not bank proof in the shop’s legal name.",
    application="A payslip is employment evidence, often in a personal name. It is not a passbook, cancelled cheque, or bank letter of the shop. Do not print salary or account digits. Request proper proof.",
    held="Does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001. Do not print salary or account digits.",
)
