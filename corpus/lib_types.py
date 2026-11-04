"""Type-classification opinions. Aliases also live in ONB-ANX-003; these pages exist for retrieval on the merchant's words."""

MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/types")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §3; ONB-ANX-003")
    MEMOS.append(kw)


add(
    slug="restaurant",
    title="Classification — restaurant",
    issue="Whether a shop that states its business as a restaurant is a permitted type under ONB-POL-001 §3.1, and whether a complete pack lets the Copilot activate it.",
    facts="The merchant described the activity as a restaurant: preparation and sale of food for consumption on or off the premises. No money-transmission, VDA, or wagering activity was stated.",
    rule="ONB-POL-001 §3.1 permits restaurant. Cafe and dhaba are treated as restaurant (ONB-ANX-003). Activation remains ONB-POL-001 §4: only the Merchant Risk Lead, outside chat, and only if the pack is complete. FSSAI licensing under the Food Safety and Standards Act, 2006 is background and is not a fifth pack item.",
    application="A restaurant is the paradigm permitted shop. The Copilot may explain that this type is within §3.1 and that go-live still requires four accepted pack files plus a human activator. It shall not treat FSSAI as a substitute for business registration, shall not waive shopfront because food is prepared inside, and shall not mark the shop live in chat. If the merchant later restates the type as a bar, hotel, or home kitchen, that later statement is a different classification; this opinion applies only where restaurant was the type written.",
    held="Permitted as restaurant. Pack still required. Copilot does not activate.",
    copilot="Cite ONB-POL-001 §3.1 and §4. Do not invent an FSSAI slot. Do not say the shop is live.",
)

add(
    slug="grocery",
    title="Classification — grocery",
    issue="Whether grocery, including a kirana described as grocery, is permitted, and whether a UPI QR at the counter converts it into money service.",
    facts="The merchant stated grocery: retail of food staples and household provisions. A UPI QR is displayed for collecting sale proceeds.",
    rule="ONB-POL-001 §3.1 permits grocery. Kirana described as grocery is grocery (ONB-ANX-003). Money service in §3.2 means transmission or conversion of funds as a business, not acceptance of UPI for one’s own grocery sales. PSS Act / NPCI UPI rules are background and are not a verdict input (ONB-POL-004).",
    application="Collecting consideration for groceries through UPI is ordinary merchant acquiring, not a remittance desk. The Copilot shall not refuse a kirana as money service merely because a QR is printed on the counter. Conversely it shall not treat a hawala or forex business as grocery because biscuits are also sold. Pharmacy, liquor off-licence, and petrol are not grocery even if FMCG is on the shelf. GSTIN is not a pack slot. The pack of four items still applies.",
    held="Permitted as grocery where so described. UPI for own sales is not §3.2. Pack still required.",
    copilot="Cite §3.1. Do not refuse for the QR. Do not stretch grocery over pharmacy or liquor.",
)

add(
    slug="retail",
    title="Classification — retail",
    issue="Whether retail of goods from a shop is permitted, and whether personal-care or workshop services can be read as retail because goods are used in the service.",
    facts="The merchant stated retail: sale of goods to consumers from a shop. Separately, other applicants try to stretch salon, gym, or garage into this word.",
    rule="ONB-POL-001 §3.1 permits retail. ONB-ANX-003 forbids stretching retail to services on the person or workshop services. Completeness of pack does not recast an unlisted type as retail.",
    application="Retail here means a shop selling goods, not every establishment that issues a bill. A salon that uses shampoo, a garage that fits a spare part, or a gym that sells a protein sachet is still the service they stated unless they applied as retail. Treating those as retail would empty §3.3. When the merchant did apply as retail of goods, the type is permitted; shopfront, legal-name bank proof, owner ID, and registration remain. The Copilot shall not recommend go-live for an unlisted type by calling it retail to be helpful.",
    held="Permitted only where the stated type is retail of goods. Services named as salon/gym/garage remain unlisted.",
    copilot="Cite §3.1 and ONB-ANX-003. Do not stretch. Do not activate.",
)

add(
    slug="cafe",
    title="Classification — cafe treated as restaurant",
    issue="Whether a cafe is permitted as restaurant, or must wait in review as an unlisted beverage format, or is a bar because coffee is served with a licence question.",
    facts="The merchant stated cafe: beverages and light food. They did not state a bar, hotel, or on-licence liquor business.",
    rule="ONB-ANX-003 treats cafe and coffee shop as restaurant under §3.1. A licensed bar is unlisted and is not automatically restaurant. State excise is background and does not decide this product’s type list.",
    application="Cafe is an alias of restaurant in this catalogue so that the Copilot does not send every coffee shop to §3.3. That alias does not licence liquor. If the only stated type is cafe, explain that it is treated as restaurant, that the four pack items still apply, and that the Copilot still cannot activate. If they stated bar, this alias does not apply. FSSAI, if uploaded, is not a fifth item and does not waive shopfront.",
    held="Permitted as restaurant via the cafe alias. Pack required. Not a bar by default.",
    copilot="Cite ONB-ANX-003 and §3.1. Do not open an unlisted lecture unless they named an unlisted type.",
)

add(
    slug="dhaba",
    title="Classification — dhaba treated as restaurant",
    issue="Whether a dhaba is restaurant or an unlisted transport-side activity because it sits on a highway.",
    facts="The merchant stated dhaba: roadside cooked food. Location is a highway. They did not state a trucking or mandi business.",
    rule="ONB-ANX-003 treats dhaba as restaurant. City and highway location are application fields, not type, and create no waiver (ONB-POL-002 §6; ONB-POL-004).",
    application="Dhaba is cooked-food service under the restaurant alias. Sitting on NH-whatever does not make it logistics, and does not waive shopfront photograph of the front of that dhaba. Electricity bills of the highway DISCOM are still not bank proof. The Copilot shall not invent a rural simplified pack. If they applied as truck operator rather than dhaba, §3.3 would apply; that is not this case.",
    held="Permitted as restaurant. Location is not a waiver. Pack required.",
    copilot="Cite ONB-ANX-003. Do not waive shopfront or bank proof for a highway site.",
)

add(
    slug="kirana",
    title="Classification — kirana treated as grocery",
    issue="Whether a kirana is grocery when so described, or unlisted because the word kirana is absent from §3.1’s three nouns.",
    facts="The merchant stated kirana. Nature of activity is neighbourhood provisions. They did not state money transfer, pharmacy, or liquor.",
    rule="ONB-ANX-003 treats kirana described as grocery / kirana provisions as grocery under §3.1. The Copilot shall not refuse a kirana as unlisted merely because the statute-like list in §3.1 uses the word grocery.",
    application="Kirana is the ordinary Indian neighbourhood grocery. Reading §3.1 as an English-language closed set that excludes kirana would send almost every permitted small shop into §3.3 and defeat the product. The alias applies when they described provisions. It does not apply when they described a money-transfer kiosk that also sells biscuits — that is §3.2 if money service was the business. GSTIN, Udyam, and Shops Act certificates are not extra slots.",
    held="Permitted as grocery when described as kirana/provisions. Pack required.",
    copilot="Cite ONB-ANX-003. Do not send a kirana to unlisted review solely for the word kirana.",
)

add(
    slug="money-service",
    title="Classification — money service refused",
    issue="Whether a money-service business can be onboarded if pack files are complete and PMLA reporting is promised.",
    facts="The merchant stated money service: transmission or conversion of funds as a business. They offer a complete pack and say they will file STRs.",
    rule="ONB-POL-001 §3.2 refuses money service. No activation review is opened. No review identifier is issued. Pack completeness is irrelevant to a §3.2 refusal. PMLA is non-operative background (ONB-POL-001 §1.5).",
    application="Money service is an operative refusal, not a reviewer-discretion type. Promising PMLA compliance does not create a permitted shop. The Copilot is not a reporting entity’s STR desk and shall not offer to file reports, accuse, or keep a review id ‘so compliance can start’. FEMA and the PSS Act explain why this product does not acquire remittance desks; they do not authorise a chatbot to go live. Explain the refusal, cite §3.2, and do not invent an identifier.",
    held="Refused. No review identifier. Copilot does not activate and does not file STRs.",
    copilot="Cite ONB-POL-001 §3.2. Do not issue an id. Do not recommend go-live.",
)

add(
    slug="hawala-desk",
    title="Classification — hawala desk as money service",
    issue="Whether a shop described as a hawala desk is unlisted (person decides) or refused as money service, and whether PMLA reporting lets the Copilot activate once files are in.",
    facts="The merchant described the business as a hawala desk. Nature of activity: informal value transfer. They argue that PMLA already requires reporting, so iPe should go live and report later.",
    rule="ONB-POL-001 §3.2 refuses money service without an activation review and without a review identifier. ONB-ANX-003 maps hawala desk, informal value transfer, and hundi-as-transfer-desk to money service. PMLA is background and does not enlarge §3.1 (ONB-POL-001 §1.5).",
    application="Hawala is informal value transfer: value is accepted here and made available elsewhere outside a licensed payment system as the product. That is money service, not a salon-style unlisted shop and not grocery because a counter exists. Completeness of CDD files does not move §3.2 into §3.1. PMLA is why a pack exists at all; it is not a power of the Copilot to activate a remittance desk so that reporting can begin. FEMA and the PSS Act are background in the same sense. No review identifier is issued. The Copilot shall not offer to file an STR, shall not accuse, and shall not recommend go-live.",
    held="Refused as money service. No review identifier.",
    copilot="Cite ONB-POL-001 §3.2 and ONB-ANX-003. Do not treat hawala as unlisted. Do not activate.",
)

add(
    slug="remittance-agent",
    title="Classification — remittance agent",
    issue="Whether a domestic or cross-border remittance agent is money service or an unlisted financial intermediary for a person to decide.",
    facts="The merchant stated remittance agent: they take cash and arrange payout to a beneficiary on another corridor or in another city.",
    rule="ONB-ANX-003 treats remittance agent and money-transfer kiosk as money service under §3.2. FEMA and the PSS Act are background. Unlisted treatment is for types in neither §3.1 nor §3.2.",
    application="A remittance agent’s product is the transfer, not groceries. Putting it in §3.3 would ask a reviewer to invent a permitted money-service path that §3.2 closed. Principal/agent labels, Money Transfer Service Scheme history, and authorised-dealer categories do not appear in this product’s type list and shall not be used by the Copilot to create a live MID. Refuse, issue no identifier, and do not discuss settlement corridors.",
    held="Refused as money service. No review identifier.",
    copilot="Cite §3.2. Do not open a FEMA licensing seminar. Do not activate.",
)

add(
    slug="forex-counter",
    title="Classification — forex counter",
    issue="Whether a currency-exchange counter is money service, or may pass as retail of foreign notes, or as a permitted shop with incidental FX.",
    facts="The merchant stated forex counter as the business: buying and selling foreign currency. They did not describe a restaurant that occasionally changes a tourist’s notes.",
    rule="ONB-ANX-003 treats forex counter and currency exchange as the business as money service. The catalogue does not assume incidental FX at a permitted shop. FEMA is background.",
    application="Exchange of currency as the business is conversion of funds, which this product refuses. Calling banknotes ‘goods’ in order to reach §3.1 retail would rewrite money service as retail. Authorised-dealer licensing, if the applicant boasts of it, is not a pack slot and is not Copilot activation. If they had applied only as a permitted restaurant, incidental tourist change would not have been assumed to be a forex desk — but they applied as the desk.",
    held="Refused as money service. No review identifier.",
    copilot="Cite ONB-ANX-003 and §3.2. Do not treat notes as retail goods.",
)

add(
    slug="crypto",
    title="Classification — crypto / VDA desk",
    issue="Whether a crypto or virtual-digital-asset desk can be onboarded if volume is small or if the shop also sells tea.",
    facts="The merchant stated crypto: tokens, bitcoin, or similar VDA activity as the business. They say volume is below one lakh and they also sell tea.",
    rule="ONB-POL-001 §3.2 refuses crypto including bitcoin and similar tokens. No review identifier. Volume is not a waiver of type (ONB-POL-002 §6). ONB-ANX-003: if the stated type is crypto, tea does not save it.",
    application="VDA activity is an operative refusal. Simplified-CDD talk, small volume, and a tea kettle do not create a restaurant path when they stated crypto. RBI and Ministry of Finance VDA communications are background; this product does not run a VDA licence analysis and does not need one in order to refuse. The Copilot shall not recommend go-live, shall not issue an id ‘for the tea side’, and shall not cite a draft that drops the pack for small volume (that draft is not in force).",
    held="Refused as crypto. No review identifier. Volume irrelevant.",
    copilot="Cite §3.2. Do not split the shop into tea plus crypto. Do not activate.",
)

add(
    slug="bitcoin-atm",
    title="Classification — bitcoin ATM",
    issue="Whether an unattended VDA cash-in/out machine is crypto under §3.2 or an unlisted kiosk because no human teller is present.",
    facts="The merchant stated bitcoin ATM: unattended cash-to-token or token-to-cash. They argue it is only hardware rental.",
    rule="ONB-ANX-003 maps bitcoin ATM and VDA cash-in to crypto under §3.2. Hardware rental and POS rental are not onboarding verdict inputs (ONB-POL-004).",
    application="The product being onboarded is VDA cash conversion, not a restaurant POS. Unattended delivery does not make it unlisted; §3.2 is about the activity, not staffing. Calling it a kiosk or ‘ATM as a service’ does not reach §3.1 retail. Refuse without an identifier. Do not quote scheme MDR or hardware rent.",
    held="Refused as crypto. No review identifier.",
    copilot="Cite ONB-ANX-003. Do not treat hardware rental as the type.",
)

add(
    slug="nft-shop",
    title="Classification — NFT shop",
    issue="Whether trade in tokenised assets is crypto under §3.2 or retail of digital art under §3.1.",
    facts="The merchant stated NFT shop: sale of tokenised assets. They say it is retail of art.",
    rule="ONB-ANX-003 maps NFT shop to crypto. §3.1 retail means a shop selling goods in the ordinary sense of this product, not token rails.",
    application="An NFT shop’s inventory is a token. Reading it as retail of art would move VDA activity into §3.1 by metaphor. Copyright in an image, if any, is background (Copyright Act, 1957) and does not convert a token desk into a permitted shop. Refuse as crypto, issue no id, and do not open a how-to-mint discussion.",
    held="Refused as crypto. No review identifier.",
    copilot="Cite ONB-ANX-003. Do not stretch retail to tokens.",
)

add(
    slug="gambling",
    title="Classification — gambling refused",
    issue="Whether a gambling or betting business is refused, and whether a state gaming licence or a tea counter changes that.",
    facts="The merchant stated gambling: wagering as the business. They mention a state licence and tea sales.",
    rule="ONB-POL-001 §3.2 refuses gambling including betting. ONB-ANX-003: if type is gambling, tea does not save it. Public Gambling Act / state gaming laws and the Lotteries (Regulation) Act, 1998 are background.",
    application="This product does not onboard wagering, licensed or not. A state licence is not a pack slot and is not Copilot activation. The Copilot shall not conduct a skill-versus-chance enquiry to be helpful. If they had stated cafe only, a television showing a match would not have been gambling; they stated gambling. Refuse, no identifier.",
    held="Refused as gambling. No review identifier. Licence and tea irrelevant.",
    copilot="Cite §3.2. Do not analyse the licence. Do not activate.",
)

add(
    slug="satta-matka",
    title="Classification — satta / matka",
    issue="Whether satta or matka is unlisted local colour or gambling under §3.2.",
    facts="The merchant stated satta / matka as the business.",
    rule="ONB-ANX-003 maps satta and matka to gambling. §3.2 refuses gambling. No review identifier.",
    application="Satta and matka are wagering. Treating them as unlisted because the English word gambling was not used would let the merchant’s vocabulary defeat §3.2. The Copilot shall refuse, shall not issue an id, and shall not moralise or threaten police. Public-law gambling statutes are background for the explanation, not a charging sheet.",
    held="Refused as gambling. No review identifier.",
    copilot="Cite ONB-ANX-003 and §3.2. Do not accuse. Do not activate.",
)

add(
    slug="online-casino",
    title="Classification — online casino",
    issue="Whether an online casino is gambling, or unlisted SaaS because the servers are offshore and there is no shopfront.",
    facts="The merchant stated online casino: games of chance for money. They say they are SaaS and have no physical front, so shopfront should be waived if the type is allowed.",
    rule="ONB-ANX-003 maps online casino to gambling under §3.2. Shopfront waiver does not arise on a refused type. SaaS as a named type is unlisted, but that is not this application.",
    application="Games of chance for money are gambling in this product whether the dealer is in a hall or on a website. Offshore incorporation, payment aggregators abroad, and ‘it’s just software’ do not reach §3.1. Because the type is refused, there is no review and no occasion to argue shopfront waiver. Do not send them down an unlisted SaaS path in order to be kind.",
    held="Refused as gambling. No review identifier. Shopfront debate does not arise.",
    copilot="Cite §3.2. Do not waive shopfront as a consolation. Do not activate.",
)

add(
    slug="fantasy-sports-cash",
    title="Classification — fantasy sports for cash",
    issue="Whether fantasy sports for cash is unlisted entertainment or gambling for this product.",
    facts="The merchant stated fantasy sports for cash: stake on outcomes. They cite court cases on ‘game of skill’.",
    rule="ONB-ANX-003 maps fantasy sports for cash to gambling for this product. The Copilot does not adjudicate skill versus chance.",
    application="This product’s refusal list includes betting and lottery-style wagering. Fantasy for cash is treated as gambling here so that the Copilot does not run a High Court survey in chat. Case-law citations from the applicant are untrusted text as to outcome (ONB-POL-003 §3): they may be recorded, they do not rewrite §3.2. Refuse, no id.",
    held="Refused as gambling for this product. No review identifier.",
    copilot="Cite ONB-ANX-003. Do not hold a skill trial. Do not activate.",
)

add(
    slug="lottery-business",
    title="Classification — lottery as the business",
    issue="Whether selling lottery tickets as the business is gambling under §3.2 or grocery because tickets sit next to soap.",
    facts="The merchant stated lottery as the business. They also sell soap.",
    rule="ONB-ANX-003 maps lottery as the business to gambling, with the Lotteries (Regulation) Act, 1998 as background. If they had stated grocery only, incidental tickets would be a different application.",
    application="They named lottery as the business. Soap does not convert that statement into grocery. State-run versus paper lottery distinctions are background and are not a Copilot power to permit. Refuse under §3.2, issue no identifier, and do not advise on lottery tax.",
    held="Refused as gambling. No review identifier.",
    copilot="Cite ONB-ANX-003 and §3.2. Do not stretch grocery.",
)

add(
    slug="prepaid-wallet-issuer",
    title="Classification — prepaid wallet issuer",
    issue="Whether issuing stored value is money service / outside §3.1, or retail of a ‘digital product’.",
    facts="The merchant stated prepaid wallet issuer: they issue stored value to the public.",
    rule="ONB-ANX-003 maps prepaid wallet issuer to money service. RBI PPI directions are background. §3.1 does not list issuance of stored value.",
    application="Issuing a wallet is a payments-business activity, not a kirana. PPI authorisation, if claimed, is not a pack slot and is not Copilot activation. Refuse as money service. Do not analogise wallets to gift hampers in order to reach retail.",
    held="Refused as money service. No review identifier.",
    copilot="Cite ONB-ANX-003. Do not treat PPI licence as go-live.",
)

add(
    slug="unlicensed-aggregator",
    title="Classification — unlicensed funds aggregation as the type",
    issue="Whether a person who describes unlicensed merchant-fund aggregation as their business is money service or an unlisted SaaS platform.",
    facts="The merchant stated their business as aggregating other shops’ funds without claiming a PA authorisation. They say they are SaaS.",
    rule="ONB-ANX-003 maps unlicensed funds aggregation described as the business to money service; RBI PA guidelines are background. SaaS named as type is unlisted — but only if that is the type they stated, not a relabel of aggregation.",
    application="If the stated business is taking other merchants’ money, that is money service for this product, not a coworking-style unlisted SaaS. PA guidelines explain why iPe itself is fictional-aggregator shaped; they do not let an applicant skip §3.2 by saying platform. Refuse, no id. Do not onboard them as a sub-merchant of themselves.",
    held="Refused as money service. No review identifier.",
    copilot="Cite ONB-ANX-003. Do not relabel as SaaS to keep them in review.",
)

add(
    slug="salon",
    title="Classification — salon unlisted",
    issue="Whether a salon is retail because products are sold at the desk, or unlisted personal service under §3.3.",
    facts="The merchant stated salon: grooming services on the person. They sell shampoo at the desk and have a complete pack.",
    rule="ONB-POL-001 §3.3 sends types in neither §3.1 nor §3.2 to human review. ONB-ANX-003: do not stretch retail to services on the person. Pack completeness does not alter type.",
    application="A salon’s primary activity is service on the person. Incidental retail of bottles does not rewrite the stated type into §3.1. Completeness of files would matter for activation if the type were permitted; it is not a curing provision for §3.3. The Copilot shall say the policy does not cover salon, shall not recommend go-live, shall not refuse as crypto, and shall not activate. A person decides. Volume routing, if a review exists, follows ONB-POL-002.",
    held="Unlisted. In review. Do not stretch to retail. Do not refuse as crypto.",
    copilot="Cite ONB-POL-001 §3.3 and ONB-ANX-003. Do not activate.",
)

add(
    slug="gym",
    title="Classification — gym unlisted",
    issue="Whether a gym is retail of memberships or equipment, or unlisted fitness service.",
    facts="The merchant stated gym: fitness services and access to equipment. They argue a membership is a good.",
    rule="ONB-ANX-003: gym is not grocery, not restaurant, and membership is not retail of goods under §3.1 as drafted. §3.3 applies.",
    application="Access to a floor and a trainer is a service. Calling a membership a ‘good’ to reach retail would also sweep hotels and SaaS into §3.1. The Copilot shall not recommend go-live, shall not refuse as gambling unless they stated wagering, and shall not waive shopfront because the floor is indoors. In review; a person decides.",
    held="Unlisted. In review. Membership is not retail for this product.",
    copilot="Cite ONB-ANX-003 and §3.3. Do not activate.",
)

add(
    slug="pharmacy",
    title="Classification — pharmacy not grocery",
    issue="Whether a pharmacy is grocery because medicines are sold like SKUs, or unlisted, and whether the Drugs and Cosmetics Act adds a slot or a refusal.",
    facts="The merchant stated pharmacy: dispensing medicines. They also sell soap. They offer a drug licence as pack proof.",
    rule="ONB-ANX-003: pharmacy is unlisted; do not treat as grocery. Drugs and Cosmetics Act, 1940 is background. It is not a fifth pack item and not a Copilot refusal list.",
    application="Dispensing medicines is not kirana grocery as this product uses the word. Soap does not convert the stated type. A drug licence may be interesting to a human reviewer; it is not registration of the business unless that is the file in the registration slot, and it is not bank proof. Do not refuse as crypto. Do not recommend go-live. Say the policy does not cover pharmacy.",
    held="Unlisted. In review. Not grocery. Licence is not a fifth slot.",
    copilot="Cite ONB-ANX-003. Do not invent a drug-licence slot. Do not activate.",
)

add(
    slug="clinic",
    title="Classification — clinic unlisted",
    issue="Whether an outpatient clinic is unlisted healthcare or retail of consultations.",
    facts="The merchant stated clinic. Clinical Establishments law is mentioned by the applicant as if it onboarded them.",
    rule="ONB-ANX-003: clinic is unlisted. Clinical Establishments (Registration and Regulation) Act, 2010 is background. §3.3 requires the Copilot to say the policy does not cover the type.",
    application="A clinic is not restaurant, grocery, or retail of goods. Statutory registration of a clinical establishment does not add a pack item and does not authorise Copilot activation. The Copilot shall not demand a clinical-establishment certificate as a fifth file, shall not waive owner ID because a doctor is the owner, and shall not print registration numbers. In review; a person decides.",
    held="Unlisted. In review. Sector licence is background only.",
    copilot="Cite §3.3. Do not add a fifth slot. Do not print numbers.",
)

add(
    slug="bar",
    title="Classification — bar not automatically restaurant",
    issue="Whether a bar is restaurant because food may be served, or unlisted on-licence liquor service.",
    facts="The merchant stated bar: on-licence liquor. They have FSSAI and say food is served.",
    rule="ONB-ANX-003: bar is unlisted; state excise is background; not automatically restaurant. Restaurant applies if they applied as restaurant.",
    application="They applied as bar. Excise licensing and FSSAI do not rewrite the stated type into §3.1. Stretching restaurant to every on-licence room would hide liquor service from reviewers. If they had applied as restaurant, this opinion would not recast them as a bar. Here, say the policy does not cover bar, keep them in review, do not refuse as gambling unless they stated wagering, and do not activate.",
    held="Unlisted unless they applied as restaurant. This applicant: in review.",
    copilot="Cite ONB-ANX-003. Do not stretch restaurant. Do not activate.",
)

add(
    slug="liquor-shop",
    title="Classification — liquor shop not grocery",
    issue="Whether an off-licence liquor shop is grocery of bottled goods or unlisted.",
    facts="The merchant stated liquor shop. They compare bottles to grocery SKUs.",
    rule="ONB-ANX-003: liquor shop is unlisted; excise is background; not grocery.",
    application="Off-licence liquor is a specialised trade this product did not put in §3.1. Grocery means provisions as used in the catalogue, not every bottled liquid. The Copilot shall not recommend go-live, shall not add an excise-licence slot, and shall not refuse as money service. In review; a person decides.",
    held="Unlisted. In review. Not grocery.",
    copilot="Cite ONB-ANX-003. Do not invent an excise slot.",
)

add(
    slug="petrol-pump",
    title="Classification — petrol pump not retail/grocery",
    issue="Whether fuel retail is §3.1 retail or unlisted, and whether PESO or Petroleum Rules add a pack item.",
    facts="The merchant stated petrol pump. They argue fuel is goods sold at retail.",
    rule="ONB-ANX-003: petrol pump is unlisted; Petroleum Rules / PESO are background; fuel is not grocery or general retail in §3.1 as drafted.",
    application="§3.1’s retail is the ordinary shop, not every sale of a commodity. Fuel retailing sits with specialised safety and licensing regimes; those regimes are not slots and not Copilot activation. Do not stretch grocery because engine oil is on a rack. Say unlisted, in review, no fifth PESO file demanded by the Copilot.",
    held="Unlisted. In review. PESO is not a pack item.",
    copilot="Cite ONB-ANX-003. Do not demand PESO as a fifth item. Do not activate.",
)

add(
    slug="garage",
    title="Classification — garage / workshop",
    issue="Whether a garage is retail of spare parts or unlisted repair.",
    facts="The merchant stated garage: repair of vehicles. Spares are billed.",
    rule="ONB-ANX-003: garage and body shop are workshop services, not retail under §3.1 unless they applied as retail.",
    application="Repair is the stated activity. Invoicing a filter does not make the business a parts showroom. Motor Vehicles Act provisions on workshops are background. In review; do not refuse as crypto; do not waive shopfront because work happens in a pit.",
    held="Unlisted. In review. Spares do not convert the type to retail.",
    copilot="Cite ONB-ANX-003. Do not stretch retail.",
)

add(
    slug="hotel",
    title="Classification — hotel not restaurant by breakfast",
    issue="Whether a hotel is restaurant because breakfast is served, or unlisted lodging.",
    facts="The merchant stated hotel. Breakfast is included. They did not apply as restaurant.",
    rule="ONB-ANX-003: hotel is unlisted; not restaurant merely because breakfast is served, unless they applied as restaurant. Lodging licences are background.",
    application="Lodging is the stated type. Bundled breakfast is incidental. Treating every hotel as restaurant would hide occupancy from reviewers. If they had applied as restaurant, the alias would run the other way and this memo would not recast them as a hotel. Shopfront of the hotel front is still a pack item if they proceed as a shop; the Copilot shall not waive it. In review.",
    held="Unlisted where applied as hotel. In review.",
    copilot="Cite ONB-ANX-003. Do not stretch restaurant. Do not waive shopfront.",
)

add(
    slug="cloud-kitchen",
    title="Classification — cloud kitchen",
    issue="Whether a cloud kitchen is restaurant, and whether absence of a classic dining room waives shopfront.",
    facts="The merchant stated cloud kitchen, not restaurant. There is no dine-in room. They ask to skip the shopfront photograph.",
    rule="ONB-ANX-003: if they applied as restaurant, §3.1; if they applied as cloud kitchen, not listed. Shopfront is not waived (ONB-POL-001 §2; ONB-ANX-001).",
    application="They named cloud kitchen. That is unlisted. Even if operations later treated a similarly situated applicant who wrote ‘restaurant’ as restaurant, this applicant wrote cloud kitchen. Independently, §2’s shopfront item is not waived for dark production sites. The Copilot shall not skip the photograph, shall not recommend go-live, and shall say the policy does not cover this type.",
    held="Unlisted on these facts. Shopfront not waived.",
    copilot="Cite ONB-ANX-003 and ONB-ANX-001. Do not waive shopfront.",
)

add(
    slug="home-kitchen",
    title="Classification — home kitchen",
    issue="Whether a home kitchen is restaurant, and whether a dwelling waives shopfront.",
    facts="The merchant stated home kitchen, not restaurant. Cooking is in a dwelling.",
    rule="ONB-ANX-003: home kitchen is unlisted if not applied as restaurant. Shopfront is not waived. FSSAI does not waive pack items.",
    application="Home kitchen as a stated type is not §3.1. A dwelling front is still a front if they submit as a shop; the Copilot shall not waive the photograph because neighbours might object, and shall not invent a cottage-industry pack. In review; a person decides. Do not refuse as money service.",
    held="Unlisted. In review. Shopfront not waived.",
    copilot="Cite ONB-ANX-003. Do not waive shopfront. Do not activate.",
)

add(
    slug="pawn-broker",
    title="Classification — pawn broker",
    issue="Whether pawn is retail of unredeemed goods, money service, or unlisted lending against pledge.",
    facts="The merchant stated pawn broker. State pawnbroker statutes are cited by them as a licence to go live.",
    rule="ONB-ANX-003: pawn is unlisted; state pawnbroker statutes are background; not retail. It is not money service unless they described remittance.",
    application="Lending against pledged goods is not kirana retail and not, without more, hawala. The Copilot shall not refuse as §3.2 on these facts, shall not stretch retail, shall not treat the pawn licence as a pack slot or as activation, and shall say unlisted. A person decides.",
    held="Unlisted. In review. Not retail; not automatically money service.",
    copilot="Cite ONB-ANX-003. Do not refuse as hawala without a remittance description.",
)

add(
    slug="nbfc-gold-loan",
    title="Classification — NBFC gold loan",
    issue="Whether gold-loan origination is retail of jewellery, money service, or unlisted lending.",
    facts="The merchant stated NBFC gold loan: non-bank lending against bullion.",
    rule="ONB-ANX-003: NBFC gold loan is unlisted; RBI NBFC directions are background; neither grocery nor retail of goods in the shop sense of §3.1.",
    application="The product is a loan, not a jewellery showroom, unless they applied as retail jeweller. NBFC registration is not a fifth pack item and not Copilot activation. Do not refuse as crypto. In review.",
    held="Unlisted. In review. Sector directions are background.",
    copilot="Cite ONB-ANX-003. Do not add an NBFC-certificate slot.",
)

add(
    slug="chit-fund",
    title="Classification — chit fund",
    issue="Whether a chit fund is gambling, money service, or unlisted, given the Prize Chits Act as background.",
    facts="The merchant stated chit fund. They did not describe a lottery or a remittance desk.",
    rule="ONB-ANX-003 and the briefing on the Prize Chits and Money Circulation Schemes (Banning) Act, 1978: chit as a stated type is unlisted, not a Copilot refusal unless described as gambling or money service.",
    application="The Copilot shall not run a chit-versus-prize-chit prosecution in chat. It shall not refuse under §3.2 unless they described wagering or funds transfer as the business. It shall not permit as retail of ‘subscriptions’. Unlisted; person decides; no activation.",
    held="Unlisted on these facts. In review. Do not auto-refuse.",
    copilot="Cite ONB-ANX-003. Do not accuse. Do not activate.",
)

add(
    slug="insurance-agency",
    title="Classification — insurance agency",
    issue="Whether soliciting insurance is grocery of policies or unlisted, and whether IRDAI enrolment activates the shop.",
    facts="The merchant stated insurance agency.",
    rule="ONB-ANX-003: insurance agency is unlisted; IRDAI is background; type not in §3.1 or §3.2.",
    application="Policies are not groceries. IRDAI credentials are not pack slots and not Copilot activation. Do not refuse as gambling. Say unlisted, in review.",
    held="Unlisted. In review. IRDAI is not go-live.",
    copilot="Cite ONB-ANX-003. Do not demand an IRDAI file as a fifth item.",
)

add(
    slug="saas-company",
    title="Classification — SaaS",
    issue="Whether a SaaS company is unlisted, and whether absence of a shopfront of a ‘shop’ waives the photograph.",
    facts="The merchant stated SaaS company. They say there is no physical shop.",
    rule="ONB-ANX-003: SaaS is unlisted. ONB-POL-001 §2 still lists shopfront photograph; the Copilot shall not waive it (ONB-ANX-001).",
    application="SaaS is not restaurant, grocery, or retail of goods. Unlisted, in review. Independently, this product did not create an online-only pack. The Copilot shall not skip shopfront, shall not recommend go-live, and shall not analogise to ISO 27001 as a substitute for pack files.",
    held="Unlisted. In review. Shopfront not waived.",
    copilot="Cite ONB-ANX-003 and §2. Do not waive shopfront.",
)

add(
    slug="tuition-centre",
    title="Classification — tuition / coaching",
    issue="Whether a tuition centre is retail of books or unlisted education service.",
    facts="The merchant stated tuition centre. Books are sold at the desk.",
    rule="ONB-ANX-003: tuition and coaching are education services, not §3.1, and not retail of books merely because books are sold incidentally.",
    application="Instruction is the activity. Incidental books do not create a bookstore path unless they applied as retail. RTE / state education law is background, not a slot. Unlisted; in review; shopfront of the centre’s front still not waived.",
    held="Unlisted. In review. Books do not convert the type to retail.",
    copilot="Cite ONB-ANX-003. Do not stretch retail.",
)

add(
    slug="travel-agency",
    title="Classification — travel agency",
    issue="Whether booking travel is retail of tickets or unlisted, and whether IATA or GST on tickets is a pack item.",
    facts="The merchant stated travel agency.",
    rule="ONB-ANX-003: travel agency is not restaurant or retail of goods. Sector credentials are background.",
    application="Ticketing is a service. The Copilot shall not treat IATA, GST on fares, or airline stock as bank proof or as a fifth slot. Unlisted; in review; do not refuse as money service without a remittance description.",
    held="Unlisted. In review. Credentials are not pack items.",
    copilot="Cite ONB-ANX-003. Do not add an IATA slot.",
)

add(
    slug="ngo",
    title="Classification — NGO / trust counter / section 8",
    issue="Whether an NGO or section 8 company is a permitted shop, a refused money service because it collects donations, or unlisted.",
    facts="The merchant stated NGO / section 8 / trust shop as the type, not grocery.",
    rule="ONB-ANX-003: NGO, trust counter, and section 8 company are not automatically a permitted shop. FCRA is background. Ownership form is not itself a §3.2 refusal.",
    application="Constitution under the Companies Act or a trust deed is not a type of restaurant. Donation collection is not automatically hawala. The Copilot shall not refuse as money service on the word NGO alone, shall not permit as grocery, shall say unlisted, and shall not demand FCRA as a fifth slot.",
    held="Unlisted. In review. Do not invent a refusal from legal form.",
    copilot="Cite ONB-ANX-003. Do not add FCRA as a slot.",
)

add(
    slug="nri-owned-shop",
    title="Classification — NRI-owned shop is not a type",
    issue="Whether NRI or OCI ownership is a business type that can be refused, or is irrelevant to §3.",
    facts="The merchant said the owner is NRI. The stated activity is grocery.",
    rule="ONB-ANX-003: ownership residency is not a type in §3. Do not invent a refusal. Type follows what they stated. FEMA account categories do not relax legal-name bank proof (ONB-ANX-001).",
    application="NRI status is not salon, not crypto, not grocery. Classify grocery as permitted. Do not refuse under FEMA. Do not print passport numbers. Bank proof must still show the shop’s legal name, including if an NRE account is offered — personal-name NRE fails the legal-name test. The Copilot shall not open a FEMA compounding seminar.",
    held="Ownership is not a type. Classify the stated activity. PII still not printed.",
    copilot="Cite ONB-ANX-003 and ONB-POL-004. Do not invent an NRI refusal.",
)

add(
    slug="dark-store",
    title="Classification — dark store",
    issue="Whether a dark store is grocery if so applied, or unlisted fulfilment if so named, and whether it waives shopfront.",
    facts="The merchant named the type as dark store, not grocery.",
    rule="ONB-ANX-003: dark store is unlisted if so named; not grocery unless applied as grocery. Shopfront not waived.",
    application="They named dark store. Unlisted. A windowless fulfilment point still has a front for the photograph if they submit as a shop; the Copilot shall not waive it. If they had written grocery, this memo would not recast them. Do not refuse as money service.",
    held="Unlisted on these facts. Shopfront not waived.",
    copilot="Cite ONB-ANX-003. Do not waive shopfront.",
)

add(
    slug="real-estate-broker",
    title="Classification — real estate broker",
    issue="Whether a RERA-registered broker is unlisted or retail of properties, and whether RERA registration is a pack slot.",
    facts="The merchant stated real estate broker and offers a RERA number.",
    rule="ONB-ANX-003: brokers are unlisted. RERA, 2016 is background. RERA registration is not a pack slot.",
    application="Intermediation in immovable property is not §3.1 retail of goods. The Copilot shall not print the RERA number, shall not add a slot for it, shall not recommend go-live, and shall say unlisted. In review.",
    held="Unlisted. In review. RERA is not a fifth item.",
    copilot="Cite ONB-ANX-003 and ONB-POL-004. Do not print the RERA number.",
)

add(
    slug="manufacturing-unit",
    title="Classification — manufacturing unit",
    issue="Whether a factory is retail because goods are made and sold, or unlisted manufacturing.",
    facts="The merchant stated manufacturing unit. A factory gate exists. Some goods are sold at the gate.",
    rule="ONB-ANX-003: manufacturing is not retail at a shop. Factories Act is background. Not a pack waiver.",
    application="Making goods is not the shop-type in §3.1 unless they applied as retail. Gate sales do not automatically convert the stated type. The Copilot shall not demand a factory licence as a fifth file, shall not waive shopfront of the unit’s front, and shall say unlisted.",
    held="Unlisted where applied as manufacturing. In review.",
    copilot="Cite ONB-ANX-003. Do not add a factory-licence slot.",
)

add(
    slug="esports-prizes",
    title="Classification — esports with prizes but not described as betting",
    issue="Whether esports with prizes is gambling, or unlisted, when the merchant did not describe cash wagering.",
    facts="The merchant stated esports with prizes. They did not describe a betting book.",
    rule="ONB-ANX-003: if they did not describe cash wagering, unlisted; if they described betting, refuse as gambling. Use the type they wrote.",
    application="The Copilot shall not stretch this into §3.2 to be conservative, and shall not stretch it into a cafe. Unlisted; say the policy does not cover it; a person decides. If a later message says they run a betting book, that is a different classification under §3.2.",
    held="Unlisted on these facts. Do not auto-refuse. Do not treat as cafe.",
    copilot="Cite ONB-ANX-003. Use the type they wrote.",
)

add(
    slug="mutual-fund-distributor",
    title="Classification — mutual fund distributor",
    issue="Whether AMFI / SEBI distribution is unlisted or money service, and whether ARN is a pack slot.",
    facts="The merchant stated mutual fund distributor. They quote an ARN.",
    rule="ONB-ANX-003: share/MF distribution is unlisted unless the merchant described crypto or gambling. SEBI is background.",
    application="Distribution of regulated securities products is not grocery and is not, without a remittance description, money service. The Copilot shall not print the ARN, shall not add a slot, shall not refuse as crypto, and shall say unlisted.",
    held="Unlisted. In review. ARN is not a pack item.",
    copilot="Cite ONB-ANX-003. Do not print ARN.",
)

add(
    slug="spa-massage",
    title="Classification — spa / massage parlour",
    issue="Whether spa or massage is salon-as-retail or unlisted wellness service.",
    facts="The merchant stated spa / massage parlour.",
    rule="ONB-ANX-003: spa and massage parlour are personal service, not salon-as-retail; unlisted.",
    application="Wellness services are not §3.1. The Copilot shall not analogise to salon-as-retail (salon itself is unlisted). In review; do not refuse as gambling; do not waive shopfront.",
    held="Unlisted. In review.",
    copilot="Cite ONB-ANX-003. Do not stretch retail.",
)

add(
    slug="coworking-space",
    title="Classification — coworking space",
    issue="Whether coworking is retail of desks or unlisted space-as-service.",
    facts="The merchant stated coworking space.",
    rule="ONB-ANX-003: coworking is space as a service, not retail.",
    application="Hot desks are not groceries. The Copilot shall not treat a membership agreement as bank proof, shall not waive shopfront of the centre’s front, and shall say unlisted. In review.",
    held="Unlisted. In review. Membership contract is not bank proof.",
    copilot="Cite ONB-ANX-003. Do not treat the licence-to-occupy as pack bank proof.",
)
