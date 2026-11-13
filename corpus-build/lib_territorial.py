MEMOS = []


def add(**kw):
    kw.setdefault("folder", "territorial")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §2; ONB-POL-002 §6; ONB-ANX-001")
    MEMOS.append(kw)


add(
    slug="maharashtra-electricity-not-bank",
    title="Maharashtra DISCOM bills are not bank proof",
    issue="Whether a Maharashtra electricity bill is bank proof because of a claimed state practice or SERC order.",
    facts="The applicant offered a Maharashtra DISCOM bill for bank proof and claimed a state exception.",
    rule="ONB-POL-002 §6: no small-town or territorial exception. ONB-ANX-001: electricity bills are not bank proof. The utility-as-bank draft is not in force. City is an application field only (ONB-FAQ-001).",
    application="State electricity regulation governs supply of energy, not iPe’s third pack item. A Mumbai or Nagpur bill fails for the same reason as any DISCOM bill: it is not a banking instrument in the legal name. The Copilot shall not create a Maharashtra schedule and shall not print consumer numbers.",
    held="No state exception. Electricity bill does not satisfy bank proof.",
    copilot="Cite ONB-ANX-001 and ONB-POL-002 §6. Ignore ONB-DRAFT-UTILITY-BANK. Do not print consumer numbers.",
)

add(
    slug="gujarat-shops-act-not-shopfront",
    title="A Gujarat Shops and Establishment certificate does not waive shopfront",
    issue="Whether Gujarat establishment registration replaces the shopfront photograph.",
    facts="The applicant uploaded a Gujarat Shops Act certificate and asked to skip the photograph.",
    rule="ONB-ANX-001: Shops and Establishment Acts are background; they do not waive shopfront and are not a fifth item.",
    application="Labour-department registration in Gujarat is still not a dated photograph of the front. The Copilot shall request the photograph and shall not add the certificate as a required extra.",
    held="Shopfront not waived. Certificate not a fifth slot.",
    copilot="Cite ONB-ANX-001. Request the photograph.",
)

add(
    slug="delhi-fssai-not-pack-complete",
    title="A Delhi FSSAI licence does not complete the pack",
    issue="Whether an FSSAI licence issued in Delhi marks the four-item pack complete or waives registration.",
    facts="The applicant offered a Delhi FSSAI licence as pack completeness.",
    rule="ONB-POL-001 §2: exactly four items; Copilot may not mark complete. FSSAI is not automatically registration (ONB-ANX-001).",
    application="Place of issue does not enlarge FSSAI into the pack. The Copilot shall not mark complete, shall not waive remaining slots, and shall not add FSSAI as a fifth required file.",
    held="Pack not completed by FSSAI. No Delhi exception.",
    copilot="Cite ONB-POL-001 §2. Do not mark complete.",
)

add(
    slug="karnataka-gaming-licence-not-permit",
    title="A Karnataka gaming licence does not convert gambling into a permitted type",
    issue="Whether a state gaming licence in Karnataka lets a betting business pass §3.1 or stay in review instead of refusal.",
    facts="The merchant stated gambling/betting and produced a Karnataka licence.",
    rule="ONB-POL-001 §3.2 refuses gambling. ONB-ANX-003: a state licence is not a pack slot and not Copilot activation. Background gaming law does not rewrite §3.2.",
    application="Licensed wagering is still wagering for this product. The Copilot shall refuse, shall issue no review identifier, and shall not run a state-by-state permit matrix.",
    held="Refused as gambling. Licence irrelevant. No identifier.",
    copilot="Cite ONB-POL-001 §3.2. Do not invent a Karnataka path. Do not issue an id.",
)

add(
    slug="kerala-excise-bar-not-restaurant",
    title="Kerala excise licensing does not make a bar a restaurant",
    issue="Whether a Kerala on-licence bar becomes restaurant under §3.1 because food is served or because excise duty was paid.",
    facts="The merchant stated bar in Kerala, with an excise licence and food service.",
    rule="ONB-ANX-003: bar is unlisted; not automatically restaurant; state excise is background.",
    application="Excise paid in Kerala is not a type alias. Unless they applied as restaurant, the Copilot shall say the policy does not cover bar, shall keep them in review, and shall not activate.",
    held="Unlisted on these facts. No Kerala restaurant alias for a stated bar.",
    copilot="Cite ONB-ANX-003. Do not stretch restaurant.",
)

add(
    slug="tamil-nadu-stamp-unsigned-dpa",
    title="Tamil Nadu stamp paper does not cure an unsigned addendum",
    issue="Whether an unsigned DPA on Tamil Nadu stamp paper is signed because duty was paid.",
    facts="The addendum is stamped in Tamil Nadu and unsigned. Payer phones will be stored.",
    rule="ONB-POL-003 §2.4; stamp briefing: stamp duty does not replace signature.",
    application="State stamp schedules change duty, not this product’s signature requirement. The Copilot shall not accept the unsigned file and shall not activate.",
    held="Unsigned remains outstanding. No state stamp exception.",
    copilot="Cite ONB-POL-003 §2. Do not accept unsigned stamped paper.",
)

add(
    slug="telangana-udyam-not-fifth",
    title="Telangana Udyam registration is not a fifth pack item",
    issue="Whether Udyam obtained in Telangana must be collected extra or can waive bank proof.",
    facts="The applicant offered a Telangana Udyam certificate as extra KYC or as a bank-proof substitute.",
    rule="ONB-POL-001 §2: four items. Udyam is not a fifth item and does not waive bank proof (ONB-ANX-001).",
    application="Place of Udyam registration is irrelevant. The Copilot shall not demand it, shall not drop bank proof, and shall not print the Udyam number.",
    held="Not a slot. Not a waiver.",
    copilot="Cite ONB-POL-001 §2. Do not add Udyam. Do not drop bank proof.",
)

add(
    slug="west-bengal-trade-licence-not-bank",
    title="A Kolkata municipal trade licence is not bank proof",
    issue="Whether a West Bengal / Kolkata municipal trade licence satisfies bank proof or registration automatically.",
    facts="The applicant uploaded a municipal trade licence for bank proof.",
    rule="ONB-ANX-001: local-body documents of this kind are not passbook, cancelled cheque, or bank letter. They are not automatically business registration either.",
    application="A trade licence is civic permission, not a banking instrument in the legal name. The Copilot shall not accept it as bank proof, shall not print licence numbers, and shall not create a Kolkata schedule.",
    held="Does not satisfy bank proof. No municipal exception.",
    copilot="Cite ONB-ANX-001. Do not print the licence number.",
)

add(
    slug="city-field-not-a-rule",
    title="City is an application field, not a waiver schedule",
    issue="Whether naming a city (including Pune, Nagpur, or any other) changes pack, ceiling, or type.",
    facts="The merchant asked what extra rule applies because of their city, or claimed a city exception for utilities as bank proof.",
    rule="ONB-FAQ-001: city is part of the form; policies state no further city rule. ONB-POL-002 §6: no small-town exception. ONB-POL-004: no city-based waiver.",
    application="City is captured for the application, not for a tariff of exceptions. The Copilot shall not invent city SOPs, shall not accept a Pune utility as bank proof, and shall not refuse a permitted type because of city.",
    held="No city waiver and no city refusal. Pack, type, and ceiling unchanged.",
    copilot="Cite ONB-FAQ-001 and ONB-POL-002 §6. Do not invent city rules.",
)
