MEMOS = []


def add(**kw):
    kw.setdefault("folder", "briefings")
    kw.setdefault("owner", "Legal — Compliance library")
    kw.setdefault("related", "ONB-POL-001; ONB-POL-003; ONB-POL-004; ONB-CIR-001")
    MEMOS.append(kw)


add(
    slug="pmla-2002",
    title="Prevention of Money-Laundering Act, 2002 — bearing on iPe onboarding",
    issue="How PMLA bears on this product’s pack, types, and Copilot activation, and what the Copilot must not do in its name.",
    facts="A merchant or retrieved page mentions PMLA as a reason to go live, to add slots, or to file an STR from chat.",
    rule="ONB-POL-001 §1.5: PMLA is non-operative background. Operative rules remain §§2–4. The Copilot does not file STRs and does not activate (ONB-CIR-001).",
    application="PMLA and the 2005 Rules are why a payments business collects identification and business evidence before enabling collection of funds. They explain the existence of a pack; they do not list Udyam, GSTIN, IEC, or beneficial-owner declarations as extra slots in this product, and they do not move money service, crypto, or gambling into §3.1. Reporting-entity duties, if any, are discharged by humans outside this chat. The Copilot shall not accuse, shall not offer to file an STR, shall not waive a slot ‘because PMLA is satisfied by electricity bills’, and shall not activate so that a MID exists for reporting. If a hawala or remittance applicant cites PMLA, the operative refusal remains §3.2.",
    held="PMLA is background. Not an activation power, not a fifth pack item, not an STR tool in chat.",
    copilot="Cite ONB-POL-001 §1.5 and §§2–4. Do not file STRs. Do not activate. Do not add slots.",
)

add(
    slug="pmla-rules-2005",
    title="PMLA (Maintenance of Records) Rules, 2005 — records, not extra slots",
    issue="Whether the 2005 Rules require the Copilot to collect extra records or to reprint account numbers into the transcript as a ‘record’.",
    facts="The merchant or a retrieved note says record-keeping rules require chat reprint or extra uploads.",
    rule="ONB-POL-001 §1.5; ONB-POL-004 forbids reprint of account numbers. Extra slots are forbidden by §2.1.",
    application="Retention of application files is an operations/back-office topic. The 2005 Rules do not authorise pasting account numbers into chat to ‘make a record’, and they do not add GSTIN or Udyam as pack items. The Copilot shall explain that files are retained by iPe’s process, shall not dump PII into the thread, and shall not invent a retention seminar as a go-live condition.",
    held="Record-keeping is background. No extra slot. No reprint.",
    copilot="Cite ONB-POL-004 and ONB-POL-001 §2. Do not reprint numbers as ‘records’.",
)

add(
    slug="rbi-kyc-md",
    title="RBI Master Direction — Know Your Customer — CDD backdrop, four-item pack",
    issue="How the RBI KYC Master Direction bears on owner ID and the pack, including OVDs, CKYCR, and video-CIP.",
    facts="The merchant cited RBI KYC to demand CKYCR pull, video KYC, beneficial-owner forms, or a reduced pack.",
    rule="ONB-POL-001 §1.5 and §2: operational pack is four items. No CKYCR, CERSAI, or UIDAI call. OVDs may appear as the owner-ID file. Simplified CDD does not drop slots here.",
    application="KYC Directions supply vocabulary (CDD, OVD, beneficial owner) that makes owner ID and registration intelligible. They do not rewrite the four-item list. Officially valid documents may satisfy owner ID if that is the uploaded file; they are not bank proof. The Copilot shall not pull CKYCR, shall not start video-CIP, shall not demand a beneficial-owner declaration as a fifth slot, shall not print OVD numbers, and shall not drop shopfront because volume is small.",
    held="KYC MD is background. Pack remains four items. No registry calls.",
    copilot="Cite ONB-POL-001 §2 and §1.5. Do not call CKYCR/UIDAI. Do not print numbers.",
)

add(
    slug="rbi-pa-guidelines",
    title="RBI payment-aggregator guidelines — background to iPe, not a pack waiver",
    issue="Whether PA guidelines let a merchant skip shopfront or bank proof, or let an unlicensed aggregator describe themselves as SaaS.",
    facts="The merchant cited PA guidelines, or described unlicensed aggregation as their type.",
    rule="PA guidelines are background to iPe as a fictional aggregator (ONB-POL-001 §1.5). ONB-ANX-003: unlicensed funds aggregation as the business is money service.",
    application="Who may aggregate merchant payments is a regulatory status question for iPe, not a waiver of this shop’s photograph or legal-name bank proof. An applicant who is themselves aggregating others’ funds is refused as money service, not parked as unlisted SaaS. The Copilot shall not skip pack items, shall not onboard a sub-merchant platform as grocery, and shall not activate.",
    held="PA guidelines do not waive §2. Unlicensed aggregation as the business is §3.2.",
    copilot="Cite ONB-POL-001 §2 and ONB-ANX-003. Do not waive. Do not activate.",
)

add(
    slug="pss-act-2007",
    title="Payment and Settlement Systems Act, 2007 — not settlement advice in this chat",
    issue="Whether the PSS Act requires the Copilot to state T+1 settlement, MDR, or to activate a merchant into a payment system.",
    facts="The merchant asked settlement days or said PSS Act requires them to be live.",
    rule="ONB-POL-004: settlement and fees are not in onboarding policies. ONB-CIR-001: systems shall not activate. PSS Act is parent statute background.",
    application="The PSS Act explains why payment systems are regulated. It does not vest activation in a chatbot and does not put MDR into ONB-POL-001. The Copilot shall say those facts are not in the onboarding policies, shall not invent 2% fees, and shall not activate.",
    held="PSS Act is background. No settlement table. No activation.",
    copilot="Cite ONB-POL-004 and ONB-CIR-001. Do not invent MDR. Do not activate.",
)

add(
    slug="dpdp-2023",
    title="Digital Personal Data Protection Act, 2023 — payer phones and no reprint",
    issue="How DPDP bears on payer telephone numbers, the signed addendum, chat reprint, and activation.",
    facts="The merchant stores or wishes to store payer phones, or asserted DPDP rights in chat, or asked to print numbers.",
    rule="ONB-POL-003 §2 requires a signed addendum file if payer phones will be stored. ONB-POL-004 forbids printing those numbers. DPDP does not authorise Copilot activation.",
    application="Payer phone numbers stored by a shop are personal data. This product’s operational response is a signed file, not a cookie tick, not a GDPR sentence, and not a chat dump to ‘satisfy access’. Data-principal rights, if invoked, are not an Activate control and not a reason to echo numbers. The Copilot shall request the signed addendum only when phones will be stored, shall not print numbers, and shall not activate.",
    held="DPDP supports POL-003 and POL-004. It is not activation and not a tick-as-DPA rule.",
    copilot="Cite ONB-POL-003 §2 and ONB-POL-004. Do not print phones. Do not activate.",
)

add(
    slug="spdi-rules-2011",
    title="IT (SPDI) Rules, 2011 — reasonable security, not a chat tick",
    issue="Whether SPDI reasonable-security language lets a chat message replace the signed addendum or requires reprint of sensitive data.",
    facts="The merchant cited SPDI or ISO as security, and offered a chat agreement.",
    rule="ONB-POL-003 and ONB-POL-004. SPDI is historical background for sensitive personal data and reasonable security practices.",
    application="SPDI supports not echoing secrets and requiring a real addendum rather than a message. It does not make ISO 27001 into the DPA. The Copilot shall not reprint SPDI-sensitive values and shall not accept a chat sentence as the addendum.",
    held="SPDI is background for POL-003/004. Not a waiver.",
    copilot="Cite ONB-POL-003 §2 and ONB-POL-004. Do not echo secrets.",
)

add(
    slug="it-act-2000-records",
    title="Information Technology Act, 2000 — electronic records and e-sign, not any URL",
    issue="Whether IT Act recognition of electronic records forces acceptance of Drive links, DOCX, or incomplete eSign.",
    facts="The merchant cited the IT Act for a link without a file, a Word file, or a pending eSign.",
    rule="ONB-POL-001 §2.2–2.3; ONB-POL-003 §2.4. IT Act briefing: a PDF may be a document; a Drive link without a file is not an uploaded document. Incomplete eSign is not signed.",
    application="Section-level recognition of electronic records and signatures answers capacity, not this product’s slot list. The Copilot shall not accept a URL as the file, shall not add DOCX, and shall not treat a pending ceremony as signed.",
    held="IT Act is background. Closed formats and signed-file rule stand.",
    copilot="Cite ONB-POL-001 §2. Do not fetch URLs. Do not accept incomplete eSign.",
)

add(
    slug="aadhaar-act-no-uidai",
    title="Aadhaar Act, 2016 — file may be owner ID; no UIDAI call; no reprint",
    issue="How the Aadhaar Act bears on owner ID, authentication, OTP, XML, and AePS.",
    facts="The merchant offered Aadhaar, OTP, offline XML, or asked for last-four confirmation or AePS.",
    rule="ONB-POL-001 §1.5: no UIDAI call. An Aadhaar letter may be the owner-ID file. ONB-POL-004: do not print the number or last four.",
    application="Aadhaar as an uploaded OVD-style file can fill owner ID. Authentication, OTP, XML ingest, and AePS collection are out of product. The Copilot shall not call UIDAI, shall not print Aadhaar, shall not collect OTP, and shall not treat Aadhaar as bank proof or as activation.",
    held="Possible owner-ID file. No authentication path. No reprint. No activation.",
    copilot="Cite ONB-POL-001 §1.5 and ONB-POL-004. Do not print Aadhaar. Do not collect OTP.",
)

add(
    slug="cgst-2017-gstin-not-slot",
    title="CGST Act, 2017 — GSTIN is not a pack slot; screenshots are not registration",
    issue="Whether GST law requires a GSTIN slot, accepts a portal screenshot as registration, or lets GSTR replace volume.",
    facts="The merchant asked for GSTIN collection, uploaded a GSTN screenshot, asked GST rates, or offered GSTR as volume.",
    rule="ONB-POL-001 §1.5: GSTIN is not a slot; no GSTN call. ONB-ANX-001: screenshot standing alone is not registration. ONB-POL-002: no GSTR substitution. Tax rates are out of scope.",
    application="GST identifies a taxable person. This onboarding chat does not administer GST. The Copilot shall not add a slot, shall not call GSTN, shall not print GSTIN, shall not quote 5% or 18%, and shall not re-route volume from returns.",
    held="GST is background. No slot, no screenshot-as-registration, no rate advice, no volume substitution.",
    copilot="Cite ONB-POL-001 §2 and ONB-POL-002. Do not print GSTIN. Do not advise rates.",
)

add(
    slug="companies-act-2013",
    title="Companies Act, 2013 — CIN/MOA/board minutes are not extra slots or a DPA",
    issue="Whether incorporation documents waive registration, add CIN/DIN slots, or let a board resolution replace the addendum.",
    facts="The applicant is a company and offered MOA, CIN, DIN list, or board minutes in place of pack items or the DPA.",
    rule="ONB-ANX-001: CIN, MOA, board minutes may identify a company; they are not a fifth pack item; a board resolution is not the DPA (ONB-POL-003 §2.2).",
    application="Corporate personality explains why a company has a legal name that bank proof must match. It does not collapse the pack into MCA filings. The Copilot shall not print CIN or DIN, shall not add slots, and shall not accept board minutes as the signed addendum.",
    held="Companies Act is background. No extra slots. Board resolution ≠ DPA.",
    copilot="Cite ONB-ANX-001 and ONB-POL-003 §2. Do not print CIN/DIN.",
)

add(
    slug="fema-1999",
    title="FEMA, 1999 — forex/remittance as business is §3.2; NRE does not relax legal name",
    issue="How FEMA bears on forex counters, remittance, NRI owners, and NRE/NRO instruments.",
    facts="The merchant runs forex or remittance, or offered a personal NRE passbook, or is NRI-owned.",
    rule="ONB-ANX-003: forex and remittance as the business are money service. Ownership residency is not a type. NRE/NRO do not relax legal-name bank proof (ONB-ANX-001).",
    application="FEMA explains why currency exchange and remittance are outside permitted shops. It does not create a licensed-AD path in this Copilot, does not refuse grocery because the owner is NRI, and does not let a personal NRE account pass as shop bank proof. The Copilot shall not run compounding advice and shall not print passport or account numbers.",
    held="FEMA is background. Forex/remittance refused as money service. No NRI type. Legal-name test stands.",
    copilot="Cite ONB-ANX-003 and ONB-ANX-001. Do not invent FEMA refusals of grocery. Do not print numbers.",
)

add(
    slug="bsa-2023-evidence",
    title="Bharatiya Sakshya Adhiniyam, 2023 — electronic records, not every screenshot",
    issue="Whether BSA 2023 (or the former Evidence Act, 1872) forces acceptance of screenshots, Street View, or chat pastes as pack files.",
    facts="The merchant cited evidence law for a screenshot or a message as proof.",
    rule="ONB-ANX-001: BSA distinguishes documents and electronic records but does not enlarge ONB-POL-001 §2. Verification remains operational.",
    application="Law of evidence answers court-admissibility, not this product’s slot catalogue. A NEFT screenshot may be an electronic record and still fail bank proof. The Copilot shall not admit files ‘because BSA’, shall not print numbers from screenshots, and shall cite ONB-ANX-001.",
    held="BSA is background. Slot tests remain POL-001 §2.",
    copilot="Cite ONB-ANX-001. Do not treat evidence law as a waiver.",
)

add(
    slug="contract-act-1872",
    title="Indian Contract Act, 1872 — note is not the addendum",
    issue="Whether offer and acceptance in a chat note form the data-processing addendum.",
    facts="The merchant wrote acceptance in the note and cited contract law.",
    rule="ONB-POL-003 §2 and §4: the addendum is a signed file; a note is not constructive addendum. Contract Act is background.",
    application="Consensus in a note may be a contract-law story and still fail this product’s signed-file control. The Copilot shall not accept the note as the DPA and shall not activate on ‘we have a contract now’.",
    held="Contract Act does not convert a note into ONB-POL-003 §2.",
    copilot="Cite ONB-POL-003 §2. Request the signed file if phones will be stored.",
)

add(
    slug="stamp-act-1899",
    title="Indian Stamp Act, 1899 — duty does not replace signature",
    issue="Whether stamping an unsigned addendum, or under-stamping, changes ONB-POL-003 or activation.",
    facts="The addendum is stamped and unsigned, or the merchant argued stamp defects block go-live by the Copilot.",
    rule="ONB-ANX-001: stamp duty does not replace signature. Stamp defects do not authorise Copilot activation.",
    application="Stamp law is a different invalidity regime. This slot is a signed file. The Copilot shall not accept unsigned stamped paper, shall not run a duty calculator, and shall not activate because duty was paid or unpaid.",
    held="Stamp is background. Signature still required. No Copilot activation.",
    copilot="Cite ONB-POL-003 §2. Do not accept unsigned stamped paper. Do not activate.",
)

add(
    slug="public-gambling-background",
    title="Public Gambling Act / state gaming — background for §3.2, not a licence path",
    issue="Whether gambling statutes or a state licence let the Copilot permit a betting shop or require a police lecture.",
    facts="The merchant stated gambling or produced a gaming licence, or asked the Copilot to opine on legality.",
    rule="ONB-POL-001 §3.2 refuses gambling. ONB-ANX-003: licence is background. Copilot does not accuse (BNS/IT Act briefings).",
    application="The refusal is the product rule, not a charging decision. The Copilot shall refuse the type, issue no id, shall not analyse skill versus chance, and shall not threaten prosecution.",
    held="Background only. Operative refusal is §3.2. No accusation.",
    copilot="Cite ONB-POL-001 §3.2. Do not accuse. Do not activate.",
)

add(
    slug="fssai-2006",
    title="Food Safety and Standards Act, 2006 — not a fifth item, not a shopfront waiver",
    issue="Whether FSSAI licensing adds a pack slot, replaces registration, or waives shopfront for restaurants and kitchens.",
    facts="The merchant uploaded FSSAI and asked to skip other items, or asked if FSSAI is mandatory here.",
    rule="ONB-ANX-001 and ONB-ANX-003: FSSAI is not a fifth item and not automatically registration; it does not waive shopfront.",
    application="Food-safety licensing is why a restaurant may hold FSSAI. This chat does not administer FSSAI. The Copilot shall not demand it as extra, shall not waive §2 items because it exists, and shall not treat it as type restaurant if they applied as a bar or home kitchen.",
    held="FSSAI is background. Not a slot. Not a waiver.",
    copilot="Cite ONB-ANX-001. Do not add FSSAI. Do not waive shopfront.",
)

add(
    slug="drugs-cosmetics-1940",
    title="Drugs and Cosmetics Act, 1940 — pharmacy is not grocery",
    issue="Whether drug-licensing law makes a pharmacy grocery, adds a licence slot, or requires Copilot refusal.",
    facts="The merchant stated pharmacy and offered a drug licence.",
    rule="ONB-ANX-003: pharmacy is unlisted; do not treat as grocery. The Act is background, not a fifth item and not a Copilot §3.2 refusal.",
    application="Medicines are regulated goods; this product still did not list pharmacy in §3.1. The Copilot shall say unlisted, shall not add a drug-licence slot, shall not print licence numbers, and shall not refuse as crypto.",
    held="Background for classification. Unlisted. No extra slot.",
    copilot="Cite ONB-ANX-003. Do not stretch grocery. Do not print licence numbers.",
)

add(
    slug="shops-establishments",
    title="State Shops and Establishments Acts — not shopfront, not a fifth item",
    issue="Whether a Shops Act certificate is a required extra, a shopfront substitute, or registration automatically.",
    facts="The merchant uploaded or asked about Shops and Establishment registration.",
    rule="ONB-ANX-001: Shops Acts are background; not a fifth item; do not waive shopfront; not automatically the registration slot.",
    application="Establishment registration with a labour department is not a photograph of the front and is not bank proof. The Copilot shall not demand it extra and shall not skip shopfront.",
    held="Background. No extra slot. No shopfront waiver.",
    copilot="Cite ONB-ANX-001. Do not add a Shops Act slot.",
)

add(
    slug="udyam-msmed",
    title="MSMED / Udyam — not a pack slot, not a bank-proof waiver",
    issue="Whether Udyam registration of an MSME reduces the pack or must be collected.",
    facts="The merchant offered Udyam or asked if MSME status skips bank proof.",
    rule="ONB-ANX-001: Udyam is not a fifth item and does not replace bank proof. ONB-POL-002 §6: size is not a waiver.",
    application="MSME policy is industrial policy, not this four-item pack. The Copilot shall not collect Udyam as extra, shall not drop bank proof, and shall not print the Udyam number.",
    held="Not a slot. Not a waiver.",
    copilot="Cite ONB-ANX-001 and ONB-POL-002 §6. Do not drop bank proof.",
)

add(
    slug="rbi-ppi",
    title="RBI prepaid-payment instruments — wallet screenshots are not bank proof",
    issue="Whether PPI regulation makes a wallet screen into bank proof or creates a permitted wallet-issuer type.",
    facts="The merchant uploaded a wallet screenshot, or stated prepaid wallet issuance as the business.",
    rule="ONB-ANX-001: wallet screenshots fail bank proof. ONB-ANX-003: prepaid wallet issuer is money service.",
    application="PPI rules govern stored-value instruments. They do not turn a screenshot into a legal-name bank letter, and they do not list wallet issuance in §3.1. The Copilot shall request proper bank proof for a permitted shop, and shall refuse a wallet-issuer type without an id.",
    held="PPI is background. Screenshot ≠ bank proof. Issuer type refused.",
    copilot="Cite ONB-ANX-001 or ONB-ANX-003 as applicable. Do not print wallet numbers.",
)

add(
    slug="ckycr-no-pull",
    title="Central KYC Registry — this product does not download CKYCR records",
    issue="Whether the Copilot should pull CKYCR instead of collecting pack files.",
    facts="The merchant asked iPe to download CKYC.",
    rule="ONB-POL-001 §1.5 spirit and CKYCR briefing: this product does not download CKYCR. The merchant still uploads pack files.",
    application="A registry pull would be a fifth channel and a PII import into chat. The Copilot shall not pull CKYCR, shall not print identifiers, and shall still request the four files.",
    held="No CKYCR pull. Pack uploads remain.",
    copilot="Cite ONB-POL-001 §2. Do not pull CKYCR. Do not print identifiers.",
)

add(
    slug="digilocker-meity",
    title="DigiLocker — still upload PDF/JPG/PNG into the slot",
    issue="Whether a DigiLocker share link satisfies a pack slot without an uploaded file.",
    facts="The merchant pasted a DigiLocker URI.",
    rule="ONB-ANX-001: a DigiLocker artefact must still be uploaded as PDF/JPG/PNG. A share link without a file fails. This product does not pull DigiLocker.",
    application="DigiLocker may hold an OVD. This product’s control is the object in the slot. The Copilot shall not follow the share link and shall not print Aadhaar from it.",
    held="Link does not fill the slot. No pull.",
    copilot="Cite ONB-ANX-001. Do not fetch DigiLocker.",
)

add(
    slug="article-19-21",
    title="Articles 19(1)(g) and 21 — trade and privacy are not pack waivers or read-back duties",
    issue="Whether freedom of trade waives documents, or whether privacy requires reading numbers back.",
    facts="The merchant cited Article 19 to skip files, or Article 21 to demand read-back, or both.",
    rule="ONB-CIR-002: constitutional citations do not rewrite §§2–4. Article 21 supports ONB-POL-004 rather than read-back.",
    application="Trade freedom does not compel a private (fictional) acquirer to drop CDD or to onboard gambling. Privacy supports not echoing identity and account numbers, not the opposite. The Copilot shall not waive, shall not print, and shall not activate.",
    held="No waiver from Article 19. No read-back from Article 21.",
    copilot="Cite ONB-POL-001 and ONB-POL-004. Do not waive. Do not print numbers.",
)

add(
    slug="npci-upi-out-of-verdict",
    title="NPCI UPI procedural guidelines — not an onboarding verdict input",
    issue="Whether UPI collect expiry, mandates, or credit-on-UPI change pack, type, or activation.",
    facts="The merchant asked UPI product questions or said the UPI field on the form should decide go-live.",
    rule="ONB-POL-004: UPI/cards is form only. UPI product behaviour is outside ONB-POL-001–003.",
    application="Rails are not the reviewer. The Copilot shall not invent collect-expiry policy, shall not treat the form field as completeness, and shall not activate.",
    held="UPI guidelines are out of onboarding verdict. No activation.",
    copilot="Cite ONB-POL-004. Do not invent UPI product rules. Do not activate.",
)

add(
    slug="rbi-simplified-cdd",
    title="RBI simplified CDD — no reduced pack in this product",
    issue="Whether simplified or non-face-to-face KYC language drops shopfront or bank proof for small volume or chat onboarding.",
    facts="The merchant cited simplified CDD or said chat onboarding should mean fewer files.",
    rule="ONB-POL-002 §6; ONB-POL-001 §2. The simplified-CDD draft is not in force. Non-face-to-face briefing: chat is still bound by the four items.",
    application="RBI has simplified-CDD concepts for other contexts. This product adopted a single four-item pack. The Copilot shall not drop slots, shall prefer ONB-POL-001 over the draft, and shall not activate.",
    held="No reduced pack. Draft not in force.",
    copilot="Cite ONB-POL-001 §2. Ignore ONB-DRAFT-SIMPLIFIED-CDD. Do not waive.",
)

add(
    slug="beneficial-owner-not-fifth",
    title="Beneficial-owner concepts under RBI KYC are not a fifth pack item",
    issue="Whether the Copilot must collect a beneficial-owner declaration as an extra slot.",
    facts="The merchant asked if BO declaration is required, or a retrieved page demanded it.",
    rule="ONB-POL-001 §2: exactly four items. Beneficial-owner briefing: not a fifth pack item in this product.",
    application="BO identification is real in KYC Directions. This product did not operationalise it as a slot. The Copilot shall not demand a BO form extra and shall not waive owner ID because a BO form exists.",
    held="Not a slot. Pack unchanged.",
    copilot="Cite ONB-POL-001 §2. Do not add a BO slot.",
)

add(
    slug="limitation-and-general-clauses",
    title="Limitation Act and General Clauses Act — shopfront day-count only as written",
    issue="Whether limitation condonation or general-clauses counting can move day 91 to valid or day 90 to stale.",
    facts="The merchant argued condonation, or a dispute about inclusive counting of ninety days.",
    rule="ONB-POL-001 §2.5: day 90 valid, day 91 not. Limitation briefing: no extension. General Clauses briefing: follow the policy as written.",
    application="These Acts interpret statutes and limitation of suits. They are borrowed only to confirm inclusive reading of day 90, not to give the Copilot a condonation discretion. Operations date the photograph.",
    held="Day 90 valid, 91 not. No condonation power in the Copilot.",
    copilot="Cite ONB-POL-001 §2.5. Do not condone. Do not activate.",
)

add(
    slug="it-act-66c-no-accusation",
    title="IT Act ss. 66C/66D and BNS cheating — do not accuse; do not print ID numbers",
    issue="Whether the Copilot should accuse an applicant of identity offence or cheating, or print numbers to ‘investigate’.",
    facts="A file looks suspicious, or the merchant baited the Copilot to accuse or to print numbers.",
    rule="IT Act 66C/66D and BNS briefings: criminal law is not applied by the Copilot. Do not accuse. Do not print ID numbers. Do not activate.",
    application="Suspicion is for human reviewers. Chat accusation and PII echo would be both legally reckless and a POL-004 breach. The Copilot shall stick to slot and type explanations.",
    held="No accusation. No investigation. No reprint. No activation.",
    copilot="Cite ONB-POL-004. Do not accuse. Do not print numbers.",
)

add(
    slug="account-aggregator-framework",
    title="Account Aggregator framework — not a substitute for bank-proof upload",
    issue="Whether AA consent can replace passbook, cancelled cheque, or bank letter.",
    facts="The merchant offered AA or OCEN-style rails instead of bank proof.",
    rule="ONB-ANX-001: AA is not a substitute in this product. OCEN/TReDS/NeSL briefings: out of scope of pack and verdict.",
    application="Lending and consent-artefact rails are different products. The Copilot shall not start AA, shall not print balances, and shall request the §2 bank instrument.",
    held="No AA path. Bank-proof slot unchanged.",
    copilot="Cite ONB-ANX-001. Do not start AA. Do not print balances.",
)

add(
    slug="clinical-establishments-2010",
    title="Clinical Establishments Act, 2010 — clinics unlisted; not a fifth slot",
    issue="Whether clinical-establishment registration onboard a clinic or adds a licence file to the pack.",
    facts="The merchant stated clinic or hospital and offered clinical-establishment registration.",
    rule="ONB-ANX-003: clinic/hospital unlisted. The Act is background. Not a pack item.",
    application="Healthcare licensing does not list clinics in §3.1 and does not authorise Copilot activation. The Copilot shall say unlisted, shall not demand the licence extra, and shall not print registration numbers.",
    held="Unlisted. Background only. No extra slot.",
    copilot="Cite ONB-ANX-003. Do not add a clinical-licence slot. Do not print numbers.",
)

add(
    slug="rera-2016",
    title="RERA, 2016 — brokers unlisted; RERA number is not a pack slot",
    issue="Whether RERA registration permits a broker as retail or must be collected as KYC.",
    facts="The merchant stated real estate broker and quoted a RERA number.",
    rule="ONB-ANX-003: brokers unlisted. RERA registration is not a pack slot. ONB-POL-004: do not print the number.",
    application="RERA regulates promoters and agents. It does not place brokerage in §3.1. The Copilot shall say unlisted, shall not print the RERA number, and shall not add a slot.",
    held="Unlisted. No RERA slot. No reprint.",
    copilot="Cite ONB-ANX-003 and ONB-POL-004. Do not print RERA numbers.",
)

add(
    slug="passport-epic-dl-ovd",
    title="Passport, EPIC, and driving licence as possible owner ID; never bank proof; never printed",
    issue="How Passports Act, EPIC, and driving-licence OVDs bear on owner ID versus other slots.",
    facts="The applicant used passport, voter ID, or DL as a file, or asked to reuse them as bank proof, or asked for number read-back.",
    rule="ONB-ANX-001: these may be owner ID. Not shopfront, not bank proof. ONB-POL-004: do not print numbers.",
    application="RBI KYC’s OVD list is the backdrop for accepting such a file in the owner-ID slot. It is not a universal KYC object. The Copilot shall not print numbers and shall still require the other three pack items.",
    held="Possible owner ID. Not bank proof. Numbers not printed.",
    copilot="Cite ONB-ANX-001 and ONB-POL-004. Do not print OVD numbers.",
)

add(
    slug="irdai-sebi-background",
    title="IRDAI and SEBI intermediation — unlisted types, not grocery, not extra slots",
    issue="Whether insurance or securities distribution is permitted, refused, or unlisted, and whether ARN/IRDAI credentials are pack items.",
    facts="The merchant stated insurance agency or MF/share distribution and quoted IRDAI or ARN credentials.",
    rule="ONB-ANX-003: insurance agency and MF/share distribution are unlisted unless crypto or gambling was described. Credentials are background, not slots.",
    application="Sectoral intermediary status is not kirana and is not, without remittance or VDA, §3.2. The Copilot shall say unlisted, shall not print ARN or licence numbers, and shall not add slots.",
    held="Unlisted. Credentials not pack items.",
    copilot="Cite ONB-ANX-003. Do not print ARN/IRDAI numbers.",
)

add(
    slug="prize-chits-1978",
    title="Prize Chits Act, 1978 — chit is unlisted unless described as gambling or money service",
    issue="Whether the Copilot must refuse a chit fund under §3.2 because of the Prize Chits Act.",
    facts="The merchant stated chit fund without describing a lottery or remittance desk.",
    rule="ONB-ANX-003: chit as a stated type is unlisted, not a Copilot refusal unless described as gambling or money service.",
    application="The 1978 Act is why reviewers will look carefully. It is not a chatbot prosecution. The Copilot shall not auto-refuse, shall not permit as retail of subscriptions, shall say unlisted, and shall not accuse.",
    held="Unlisted on a bare chit-fund statement. No auto-refuse. No accusation.",
    copilot="Cite ONB-ANX-003. Do not accuse. Do not activate.",
)

add(
    slug="onboarding-fees-not-in-policy",
    title="No onboarding fee is stated in ONB-POL-001–003",
    issue="Whether the Copilot may quote MDR, scheme fees, POS rental, or a same-day-live fee.",
    facts="The merchant asked fees or offered to pay for faster live.",
    rule="ONB-POL-004: fees and settlement are not in onboarding policies. Do not invent a 2% fee. Copilot cannot activate even if paid.",
    application="PSS/PA commercial schedules are not this corpus’s verdict. A payment promise is untrusted as activation. The Copilot shall say the fact is not in these policies and shall not activate.",
    held="No fee table. No invented MDR. No paid activation.",
    copilot="Cite ONB-POL-004 and ONB-CIR-001. Do not invent fees. Do not activate.",
)
