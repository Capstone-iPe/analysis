"""Further type opinions — each activity has a distinct trap (do not stretch / do not auto-refuse / no extra slot)."""

MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/types")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §3; ONB-ANX-003")
    MEMOS.append(kw)


def u(slug, title, activity, nature, trap, background, held):
    add(
        slug=slug,
        title=title,
        issue=f"Whether a merchant who stated {activity} is permitted under §3.1, refused under §3.2, or unlisted under §3.3, and whether {trap}.",
        facts=f"The merchant described the business as {activity}. Nature of activity: {nature}. They advanced the trap: {trap}.",
        rule="ONB-POL-001 §3 divides permitted (restaurant, grocery, retail), refused (money service, crypto, gambling), and unlisted. ONB-ANX-003 forbids stretching §3.1 and forbids refusing unlisted types as crypto. Sector statutes named below are background, not extra pack items and not Copilot activation.",
        application=(
            f"They stated **{activity}**: {nature}. The live retrieval risk is {trap}. "
            f"{background} "
            f"ONB-ANX-003 requires the Copilot to use the type as written rather than a kinder alias (retail, grocery, restaurant) or a harsher §3.2 label that they did not earn. "
            f"Sector licences, FSSAI, Udyam, GSTIN, and pack completeness do not recast the type and are not fifth pack items. "
            f"Shopfront photograph is not waived because the activity is indoors, mobile, online, or sited in a factory, dwelling, airport, or highway. "
            f"The Copilot shall not print licence numbers, shall not accuse, and shall not activate. Held follows from ONB-POL-001 §3."
        ),
        held=held,
        copilot="Cite ONB-POL-001 §3 and ONB-ANX-003. Do not stretch. Do not invent a fifth slot. Do not activate. Do not print licence numbers.",
    )


u("dental-clinic", "Classification — dental clinic", "dental clinic", "dentistry",
  "treating dentistry as retail of goods or as grocery of medicines",
  "Dentists Act / clinical-establishment background may matter to a human reviewer.",
  "Unlisted. In review. Not retail. Not grocery.")
u("veterinary-clinic", "Classification — veterinary clinic", "veterinary clinic", "animal treatment",
  "treating a vet practice as grocery because feed is sold",
  "Veterinary and animal-husbandry statutes are background.",
  "Unlisted. In review. Feed does not convert the type to grocery.")
u("diagnostic-lab", "Classification — diagnostic laboratory", "diagnostic lab", "pathology or imaging services",
  "treating lab tests as retail SKUs",
  "Clinical establishment and diagnostics regulation is background.",
  "Unlisted. In review. Tests are not grocery.")
u("hospital", "Classification — hospital", "hospital", "in-patient care",
  "treating a hospital as a restaurant because of a canteen, or adding a clinical-establishment slot",
  "The Clinical Establishments Act, 2010 is background and not a fifth pack item.",
  "Unlisted. In review. Canteen does not rewrite the stated type. No extra slot.")
u("body-shop", "Classification — collision body shop", "body shop", "collision repair of vehicles",
  "treating spare-part invoices as retail of goods under §3.1",
  "Motor-vehicle workshop practice is background.",
  "Unlisted. In review. Spares do not convert repair to retail unless they applied as retail.")
u("hostel", "Classification — hostel", "hostel", "boarding accommodation",
  "treating a hostel as a hotel-restaurant hybrid or as retail of beds",
  "Lodging licences are background.",
  "Unlisted. In review. Not restaurant merely because meals are bundled.")
u("paying-guest", "Classification — paying guest", "paying guest", "residential lodging in a dwelling",
  "waiving shopfront because it is a house, or treating PG as restaurant",
  "Rent-control / lodging colour is background. Shopfront is not waived (ONB-ANX-001).",
  "Unlisted. In review. Shopfront not waived.")
u("coaching-class", "Classification — coaching class", "coaching class", "exam preparation",
  "treating incidental sale of notes as retail of books under §3.1",
  "Education regulation is background, not a pack slot.",
  "Unlisted. In review. Notes do not convert the type to retail.")
u("driving-school", "Classification — driving school", "driving school", "instruction in driving",
  "treating a driving school as retail of forms or as a garage",
  "Motor Vehicles Act instruction is background.",
  "Unlisted. In review. Not garage and not retail.")
u("school", "Classification — school", "school", "formal education",
  "adding RTE recognition as a fifth slot or treating a canteen as the type",
  "RTE and state education law are background, not pack items.",
  "Unlisted. In review. No extra education slot. Use the type they stated.")
u("playschool", "Classification — playschool", "playschool", "early childhood care",
  "treating a playschool as a creche-retail of toys",
  "Childcare regulation is background.",
  "Unlisted. In review. Toys do not convert the type to retail.")
u("warehouse", "Classification — warehouse", "warehouse", "storage of goods not sold at a consumer shop-front",
  "treating warehousing as grocery because food is stored",
  "Warehousing and WDRA colour is background.",
  "Unlisted. In review. Storage is not grocery retail.")
u("cold-storage", "Classification — cold storage", "cold storage", "refrigerated warehousing",
  "treating cold storage as grocery",
  "Food-storage licensing is background, not a shopfront waiver.",
  "Unlisted. In review. Not grocery. Shopfront not waived.")
u("logistics-fleet", "Classification — logistics fleet", "logistics fleet", "transport of goods",
  "treating a fleet as retail of freight or as a dhaba because trucks park nearby",
  "Carriage by Road Act is background.",
  "Unlisted. In review. Not restaurant. Not retail.")
u("courier-franchise", "Classification — courier franchise", "courier franchise", "parcel delivery",
  "treating courier as retail of packaging or as money service because COD cash is handled",
  "COD handling is not hawala without a remittance-desk description. Courier is unlisted.",
  "Unlisted. In review. Do not auto-refuse as money service on COD alone.")
u("packers-and-movers", "Classification — packers and movers", "packers and movers", "household relocation",
  "treating movers as logistics-retail of cartons",
  "Transport licensing is background.",
  "Unlisted. In review. Cartons do not convert the type to retail.")
u("tour-operator", "Classification — tour operator", "tour operator", "organised tours",
  "treating tours as retail of tickets or adding an IATA slot",
  "Tourism credentials are background, not pack items.",
  "Unlisted. In review. No IATA slot.")
u("construction-contractor", "Classification — construction contractor", "construction contractor", "works contracts",
  "treating a contractor as retail of cement or as a shop with a site office photo waiver",
  "Works-contract GST colour is background. Shopfront is not waived.",
  "Unlisted. In review. Shopfront not waived. Cement does not make retail.")
u("textile-mill", "Classification — textile mill", "textile mill", "manufacturing of cloth",
  "treating a mill as retail because there is a factory-gate counter",
  "Factories Act is background, not a fifth slot.",
  "Unlisted where applied as mill. In review. No factory-licence slot.")
u("jewellery-workshop", "Classification — jewellery workshop", "jewellery workshop", "making of ornaments",
  "automatically treating a workshop as retail jeweller, or treating gold-loan as the same thing",
  "Hallmarking / BIS is background. Retail jeweller applies only if they applied as retail.",
  "Unlisted if applied as workshop. Do not confuse with NBFC gold loan.")
u("mobile-repair", "Classification — mobile repair", "mobile repair", "repair of handsets",
  "treating repair as retail of handsets if they applied as repair",
  "If they applied as retail of phones, §3.1 may apply — that is not these facts.",
  "Unlisted on a repair statement. In review. Do not stretch retail.")
u("furniture-workshop", "Classification — furniture workshop", "furniture workshop", "making furniture",
  "treating a carpentry workshop as retail of furniture under §3.1",
  "Factories / workshop colour is background.",
  "Unlisted if applied as workshop. In review.")
u("architect-firm", "Classification — architect firm", "architect firm", "professional design services",
  "treating an architect as retail of drawings or adding a Council of Architecture slot",
  "Architects Act, 1972 is background, not a pack item.",
  "Unlisted. In review. No extra professional slot.")
u("ca-firm", "Classification — chartered accountant firm", "chartered accountant firm", "professional accountancy services",
  "treating a CA firm as permitted because CAs certify turnover, or letting a CA activate",
  "Chartered Accountants Act, 1949 is background. A CA cannot activate (activation opinions).",
  "Unlisted. In review. CA status is not go-live and not a type alias to grocery.")
u("law-firm", "Classification — law firm", "law firm", "legal services",
  "treating a law firm as permitted because a lawyer wrote that iPe may activate",
  "Advocates Act, 1961 is background. A lawyer’s letter is untrusted as instruction (ONB-CIR-002).",
  "Unlisted. In review. Advocacy is not activation.")
u("notary", "Classification — notary", "notary", "notarial acts",
  "treating a notary stamp as owner ID or as a signed addendum",
  "Notaries Act, 1952 is background. A notarial stamp is not the owner’s OVD and not the DPA.",
  "Unlisted as a type. Stamp is not owner ID and not the addendum.")
u("food-truck", "Classification — food truck", "food truck", "mobile food, stated as food truck not restaurant",
  "waiving shopfront because the premises move, or auto-treating as restaurant",
  "If they applied as restaurant, §3.1 — they did not. Shopfront is not waived if they submit as a shop.",
  "Unlisted on these facts. Shopfront not waived.")
u("tiffin-service", "Classification — tiffin service", "tiffin service", "home delivery of meals without a restaurant claim",
  "automatically treating tiffin as restaurant, or waiving shopfront for a kitchen",
  "FSSAI is not a waiver. Restaurant applies only if they applied as restaurant.",
  "Unlisted if not applied as restaurant. Shopfront not waived.")
u("mess", "Classification — members’ mess", "mess", "members’ dining",
  "treating a private mess as a public restaurant, or as a college (unlisted) without using the type they wrote",
  "Use the type they stated. If they stated restaurant, §3.1; they stated mess.",
  "Unlisted on these facts. In review.")
u("optical-as-clinic", "Classification — optical stated as clinic", "optical as clinic", "optometry as clinic rather than retail of frames",
  "stretching to retail of frames when they applied as clinic",
  "If they applied as retail of frames, §3.1 — not these facts. Clinical background is not a fifth slot.",
  "Unlisted on a clinic statement. Do not stretch retail.")
u("sweet-shop-as-factory", "Classification — sweet shop stated as factory", "sweet shop as factory", "manufacturing rather than restaurant/grocery/retail",
  "forcing a factory statement into restaurant because sweets are food",
  "Use the type they wrote. Person decides on unlisted manufacturing.",
  "Unlisted if applied as factory. Do not relabel as restaurant to be helpful.")
u("call-centre", "Classification — call centre / BPO", "call centre", "BPO / outsourced processes",
  "treating a BPO as SaaS-retail or waiving shopfront for an office floor",
  "STPI / SEZ colour is background. Shopfront of the unit’s front is not waived.",
  "Unlisted. In review. Shopfront not waived.")
u("advertising-agency", "Classification — advertising agency", "advertising agency", "creative services",
  "treating an agency as retail of media or as a permitted shop because bills are large",
  "Volume does not change type (ONB-POL-002 §6).",
  "Unlisted. In review. Large volume is routing, not a type alias.")
u("film-production", "Classification — film production", "film production", "audio-visual production",
  "treating production as cinema exhibition or adding a copyright slot",
  "Cinematograph / copyright law is background, not pack items.",
  "Unlisted. In review. No copyright slot.")
u("youtube-studio", "Classification — YouTube studio", "youtube studio", "content production",
  "treating a studio as retail of merch or as gambling because of superchats",
  "Do not auto-refuse as gambling unless they described wagering. Merch incidental does not make retail unless so applied.",
  "Unlisted on these facts. Do not auto-refuse. Do not stretch retail.")
u("amusement-park", "Classification — amusement park", "amusement park", "entertainment premises",
  "treating tickets as retail of goods or a food stall as the whole type",
  "Safety/licensing of rides is background, not a fifth slot.",
  "Unlisted. In review. A stall does not rewrite the stated type.")
u("creche", "Classification — creche", "creche", "childcare",
  "treating a creche as a playschool-retail of toys, or adding a childcare-licence slot",
  "Childcare licensing is background, not a pack item.",
  "Unlisted. In review. No extra licence slot.")
u("old-age-home", "Classification — old age home", "old age home", "residential care",
  "treating residential care as a hotel or as a clinic",
  "Clinical/elder-care regulation is background. Use the type they stated.",
  "Unlisted. In review. Do not relabel as hotel or clinic.")
u("political-office", "Classification — political office", "political office", "party office, not a merchant shop of goods",
  "refusing as money service because donations are collected, or permitting as retail of merchandise",
  "Donation collection is not automatically hawala. Merchandise incidental does not make §3.1 unless they applied as retail.",
  "Unlisted. Do not auto-refuse as money service on the word donation alone.")
u("interior-designer", "Classification — interior designer", "interior designer", "design services",
  "treating design as retail of furniture unless they applied as retail",
  "Professional-service colour is background.",
  "Unlisted if applied as designer. In review.")
u("mlm-direct-selling", "Classification — MLM / direct selling", "MLM / direct selling", "network selling",
  "auto-refusing as prize-chit/gambling, or treating as grocery",
  "Consumer Protection (Direct Selling) Rules are background. Do not auto-refuse unless they described wagering or money service.",
  "Unlisted on these facts. Do not auto-refuse. Do not stretch grocery.")
u("donation-desk", "Classification — donation desk", "donation desk", "collection of donations rather than sale of goods in §3.1",
  "auto-refusing as hawala/money service, or permitting as grocery of receipt books",
  "FCRA/trust law is background. Do not auto-refuse without a remittance description.",
  "Unlisted. Do not auto-refuse as money service. Not grocery.")
u("truck-operator", "Classification — truck operator", "truck operator", "goods carriage",
  "treating a trucker as a dhaba because of a highway location",
  "Motor Vehicles / carriage law is background. Location is not a type (ONB-POL-004).",
  "Unlisted. In review. Highway is not a restaurant alias.")
u("taxi-fleet", "Classification — taxi fleet", "taxi fleet", "passenger transport",
  "treating a fleet as retail of rides or waiving shopfront because cars move",
  "MV Act is background. Shopfront is not waived.",
  "Unlisted. In review. Shopfront not waived.")
u("customs-broker", "Classification — customs broker", "customs broker", "customs clearance",
  "adding a CBLR licence as a fifth slot, or treating IEC trade as the same type",
  "Customs Brokers Licensing Regulations are background, not a pack item.",
  "Unlisted. In review. No extra customs-licence slot.")
u("import-export-trader", "Classification — import-export trader without a retail-shop claim", "import export trader", "IEC trade without a retail shop claim",
  "adding IEC as a pack item or treating the trader as retail of imported goods when they did not apply as retail",
  "FTDR Act is background. IEC is not a fifth item (ONB-ANX-001).",
  "Unlisted on these facts. IEC is not a slot. Do not stretch retail.")
u("agri-input-dealer", "Classification — agricultural input dealer", "agricultural input dealer", "seeds, fertiliser, or pesticide as specialised trade if not applied as retail",
  "automatically treating specialised agri-inputs as grocery or adding Insecticides Act licences as slots",
  "Insecticides Act / Seeds Act are background, not pack items. If they applied as retail, that is a different file.",
  "Unlisted if that is the type named. No extra pesticide slot.")
u("tractor-dealer-workshop", "Classification — tractor dealer applied as workshop", "tractor dealer as workshop", "workshop, not retail of tractors",
  "stretching a workshop application into retail of vehicles",
  "Use the type they stated. PESO/MV background is not a slot.",
  "Unlisted on a workshop statement. Do not stretch retail.")
u("blood-bank", "Classification — blood bank", "blood bank", "blood and components",
  "treating a blood bank as a clinic-retail or adding a NACO/D&C licence slot",
  "Drugs and Cosmetics / NACO is background, not a fifth item.",
  "Unlisted. In review. No extra blood-bank slot.")
u("ayurvedic-clinic", "Classification — ayurvedic clinic", "ayurvedic clinic", "AYUSH clinical practice",
  "treating AYUSH practice as pharmacy-grocery of medicines",
  "AYUSH regulation is background. Pharmacy itself is already unlisted, not grocery.",
  "Unlisted. In review. Not grocery.")
u("homeopathy-clinic", "Classification — homeopathy clinic", "homeopathy clinic", "homeopathic practice",
  "treating homeopathy as grocery of pellets",
  "Professional healthcare is not §3.1.",
  "Unlisted. In review. Not grocery.")
u("physiotherapy", "Classification — physiotherapy", "physiotherapy", "therapy services",
  "treating physio as a gym membership or as retail of belts",
  "Not gym-as-retail; gym is unlisted too. Not §3.1.",
  "Unlisted. In review. Do not stretch gym or retail.")
u("yoga-studio", "Classification — yoga studio", "yoga studio", "instruction",
  "treating yoga as gym-as-retail of memberships",
  "Instruction is unlisted. Membership is not retail of goods under §3.1 as drafted.",
  "Unlisted. In review.")
u("dance-school", "Classification — dance school", "dance school", "instruction",
  "treating a dance school as retail of costumes",
  "Costumes incidental do not make §3.1 unless they applied as retail.",
  "Unlisted. In review.")
u("music-school", "Classification — music school", "music school", "instruction",
  "treating a music school as retail of instruments, or adding a copyright music-licence slot",
  "Copyright / music-licence questions are out of onboarding chat (ONB-POL-004).",
  "Unlisted. In review. No music-licence slot.")
u("art-gallery", "Classification — art gallery", "art gallery", "exhibition / sale of art if applied as gallery not retail",
  "forcing gallery into retail, or refusing as NFT/crypto without a token description",
  "If they applied as retail, §3.1 — they applied as gallery. Do not refuse as crypto unless they described tokens.",
  "Unlisted on these facts. Do not auto-refuse as NFT.")
u("library", "Classification — library", "library", "lending of books",
  "treating a library as grocery or as retail of books",
  "Lending is not a shop selling groceries or a bookstore unless they applied as retail.",
  "Unlisted. In review. Not grocery.")
u("temple-as-temple", "Classification — temple prasad stall applied as temple", "temple prasad stall as temple", "religious institution as the stated type",
  "forcing a temple statement into restaurant because prasad is food",
  "If they applied as restaurant, restaurant — they applied as temple. Person decides.",
  "Unlisted if applied as a religious institution. Do not relabel as restaurant.")
u("huf-as-huf", "Classification — HUF named as the type", "HUF shop as HUF", "they named the type as HUF rather than grocery/retail/restaurant",
  "inventing a type from Hindu Undivided Family status, or refusing under FEMA",
  "HUF is a person, not a shop activity. Do not invent a type. Classify the activity if they stated one; here they named HUF.",
  "Unlisted as stated. Do not invent a refusal from family form. Person decides.")
u("sez-unit", "Classification — SEZ unit", "SEZ unit", "applied as SEZ unit not as retail/restaurant/grocery",
  "waiving ONB-POL-001 because of SEZ Act, 2005 status",
  "SEZ status does not waive the pack or activation ban. Type remains unlisted if so applied.",
  "Unlisted on these facts. SEZ is not a waiver. Pack stands.")
u("duty-free", "Classification — duty-free shop", "duty free", "airport duty-free if so applied",
  "treating duty-free as retail automatically, or adding a Customs bond slot",
  "Customs is background. If they applied as retail, that differs — they applied as duty-free.",
  "Unlisted on these facts. No extra customs slot.")
u("embassy-shop", "Classification — embassy shop", "embassy shop", "diplomatic premises shop if so applied",
  "inventing a diplomatic waiver of pack or type",
  "Diplomatic premises do not waive ONB-POL-001. Not §3.1 automatically.",
  "Unlisted. No diplomatic pack waiver. Copilot does not activate.")
u("government-canteen", "Classification — government canteen as government", "government canteen as government", "type stated is government canteen not restaurant",
  "forcing government-canteen into restaurant, or adding a government-ID slot for the department",
  "If restaurant, §3.1 — they did not so apply. Departmental status is not a pack waiver.",
  "Unlisted on these facts. Do not relabel. No extra departmental slot.")
u("defence-canteen", "Classification — defence / CSD canteen", "defence canteen", "CSD / unit canteen if so applied",
  "treating CSD as grocery automatically, or waiving pack for a unit",
  "Service canteen rules are background. Pack and activation rules stand.",
  "Unlisted if so applied. No pack waiver.")
u("nidhi-company", "Classification — nidhi company", "nidhi company", "Nidhi Rules under the Companies Act",
  "auto-refusing as money service, or treating as a permitted shop",
  "Nidhi is not money service unless they described remittance; still not §3.1. Person decides.",
  "Unlisted. Do not auto-refuse unless remittance was described.")
u("e-waste", "Classification — e-waste handler", "e-waste", "handling of e-waste",
  "adding E-Waste Rules authorisation as a fifth slot, or treating as scrap-retail",
  "E-Waste (Management) Rules, 2022 are background, not pack slots.",
  "Unlisted. In review. No extra e-waste slot.")
u("two-wheeler-service", "Classification — two-wheeler service only", "two wheeler service only", "service centre, not retail of vehicles",
  "stretching a service-only statement into retail of vehicles",
  "If they applied as retail of vehicles, §3.1 — they applied as service.",
  "Unlisted. In review. Do not stretch retail.")
u("guest-house", "Classification — guest house", "guest house", "short stay",
  "running a hotel-licence analysis in Copilot or stretching to restaurant because of breakfast",
  "Not a hotel-licence enquiry in this chat; unlisted. Breakfast does not make restaurant unless so applied.",
  "Unlisted. In review. Do not analyse hotel licences.")
u("service-apartment", "Classification — service apartment", "service apartment", "serviced lodging",
  "treating serviced apartments as hotels-as-restaurant",
  "Lodging is unlisted. Do not stretch restaurant.",
  "Unlisted. In review.")
u("water-park", "Classification — water park", "water park", "amusement",
  "treating a water park as retail of tickets or adding a municipal NOC slot",
  "Municipal NOCs are not pack items (fire NOC is not shopfront either).",
  "Unlisted. In review. No extra NOC slot.")
u("packaging-unit", "Classification — packaging unit", "packaging unit", "packaging as manufacturing",
  "treating packaging as retail of packaged goods",
  "Legal Metrology packaged-commodities rules are background, not a pack item.",
  "Unlisted. In review. Not retail of goods at a shop merely because packaging occurs.")
u("railway-stall-as-railway", "Classification — railway stall as railway", "railway stall as railway", "type is railway stall not restaurant/retail",
  "forcing a railway-stall statement into restaurant",
  "If they applied as restaurant, §3.1. They applied as railway stall. Person decides.",
  "Unlisted on these facts. Do not relabel as restaurant.")
u("airport-kiosk-as-kiosk", "Classification — airport kiosk as kiosk type", "airport kiosk as kiosk type", "not stated as retail/restaurant/grocery",
  "forcing a kiosk label into retail, or waiving shopfront because of airport security",
  "Airport siting does not waive shopfront or rewrite type.",
  "Unlisted if not stated as retail/restaurant/grocery. Shopfront not waived.")
u("mandi-agent", "Classification — mandi agent", "mandi agent", "agricultural market intermediary",
  "treating a mandi agent as grocery, or adding an APMC licence slot",
  "APMC / state mandi law is background, not a pack item.",
  "Unlisted. In review. No extra mandi slot.")
u("pesticide-shop-as-pesticide", "Classification — pesticide shop named as pesticide", "pesticide shop as pesticide", "Insecticides Act trade if that is the type named",
  "automatically treating pesticide trade as grocery",
  "Insecticides Act, 1968 is background. Not grocery automatically. In review if that is the type named.",
  "Unlisted if that is the type named. Not grocery. No extra licence slot demanded by Copilot.")
u("imaging-centre", "Classification — imaging centre", "imaging centre", "radiology",
  "adding an AERB licence as a fifth slot, or treating imaging as a diagnostic-retail",
  "AERB is background for X-ray, not a pack item.",
  "Unlisted. In review. No AERB slot.")
u("online-only-store", "Classification — online-only store", "online-only store", "they denied a physical front and applied as online-only not retail",
  "waiving shopfront because there is no street facade, or stretching to retail",
  "Shopfront photo remains a pack item under §2; Copilot shall not waive. Retail if they said retail — they said online-only.",
  "Unlisted if type unlisted. Shopfront not waived. Website is not the photograph.")
u("kirana-aggregator", "Classification — aggregator of kiranas", "aggregator of kiranas", "platform of other shops",
  "pulling other shops’ files, or treating the platform as grocery",
  "This chat is one shop; type is what they stated for themselves. Do not pull other shops’ files (ONB-POL-004).",
  "Unlisted on a platform statement. This shop only. Do not pull other files.")
u("sub-merchant-platform", "Classification — sub-merchant platform", "sub-merchant platform", "aggregation of merchants",
  "relabelling aggregation as SaaS to avoid §3.2 when they described taking others’ funds",
  "If they described unlicensed funds aggregation as the business, refuse as money service (ONB-ANX-003). If they only named a platform without that description, unlisted — use the type they wrote.",
  "Use the type they wrote. Do not relabel to be kind. Do not activate.")
u("payroll-company", "Classification — payroll company", "payroll company", "HR processing",
  "treating payroll as money service because salaries move, or as grocery of payslips",
  "Salary processing is not hawala without a remittance-desk description, and is not §3.1. Do not auto-refuse on salary movement alone.",
  "Unlisted. Do not auto-refuse as money service solely because payroll moves funds.")
u("laundry", "Classification — laundry", "laundry", "washing as a service",
  "treating laundry as retail of detergent",
  "Detergent incidental does not make §3.1.",
  "Unlisted. In review. Not retail of goods.")
u("tailor", "Classification — tailor", "tailor", "stitching services",
  "treating a tailor as retail merely because cloth is used",
  "ONB-ANX-003: not retail merely because cloth is used.",
  "Unlisted. In review. Cloth does not convert the type to retail.")
u("photo-studio", "Classification — photo studio", "photo studio", "photography services",
  "treating a studio as retail of prints, or using studio portraits as owner ID",
  "Prints incidental do not make retail unless so applied. A studio portrait is not government ID (ONB-ANX-001).",
  "Unlisted as a type. Portraits are not owner ID.")
u("ev-charging", "Classification — EV charging", "EV charging", "sale of charging service",
  "treating charging as petrol-retail of energy or as grocery",
  "Not §3.1 as drafted. Electricity supply to a vehicle is not a DISCOM bill as bank proof either.",
  "Unlisted. In review. Not grocery. Not a utility-bill bank-proof story.")
u("scrap-dealer", "Classification — scrap dealer", "scrap dealer", "trade in scrap",
  "treating scrap as retail of goods under §3.1 automatically, or adding pollution consents as slots",
  "Pollution consents are background, not pack items. Type is unlisted as drafted.",
  "Unlisted. In review. No extra consent slot.")
u("security-agency", "Classification — security agency", "security agency", "private security",
  "adding a PSARA licence as a fifth slot",
  "PSARA, 2005 is background, not a pack item.",
  "Unlisted. In review. No PSARA slot.")
u("manpower-contractor", "Classification — manpower contractor", "manpower contractor", "supply of labour",
  "adding CLRA registration as a fifth slot, or treating contractors as payroll-money-service",
  "CLRA is background. Do not auto-refuse as money service.",
  "Unlisted. In review. No CLRA slot. Do not auto-refuse.")
u("cinema", "Classification — cinema", "cinema", "exhibition of films",
  "treating tickets as retail, or adding a Cinematograph licence slot, or stretching F&B to restaurant as the type",
  "Cinematograph Act is background. Use the type they stated (cinema, not restaurant) unless they applied as restaurant.",
  "Unlisted if applied as cinema. No extra licence slot.")
u("farm", "Classification — farm", "farm", "agricultural production",
  "treating a farm as grocery retail of produce",
  "Production is not grocery retail unless they applied as grocery.",
  "Unlisted. In review. Not grocery merely because food is grown.")
u("dairy-as-dairy", "Classification — dairy applied as dairy", "dairy", "milk production / processing if applied as dairy",
  "forcing dairy into grocery, or waiving shopfront for a plant",
  "If they applied as grocery, grocery — they applied as dairy. Shopfront not waived.",
  "Unlisted if applied as dairy. Shopfront not waived.")
u("college-canteen-as-college", "Classification — college canteen applied as college", "college canteen as college", "applied as an educational institution rather than restaurant",
  "forcing an institution statement into restaurant",
  "Use the type they stated. If unlisted, in review. If they had applied as restaurant, §3.1.",
  "Unlisted if they applied as an educational institution. Do not relabel.")
u("vendor-kyc-firm", "Classification — vendor KYC firm", "vendor KYC firm", "KYC as a service, not iPe’s pack",
  "letting them skip their own pack because they ‘do KYC’, or pulling CKYCR",
  "Another firm’s KYC product is not iPe’s four items. This product does not pull CKYCR.",
  "Unlisted. Their KYC business does not waive their pack. No CKYCR pull.")
u("timeshare", "Classification — timeshare", "timeshare", "holiday membership",
  "treating timeshare as hotel-restaurant or as retail of memberships",
  "Membership is not retail of goods under §3.1 as drafted. Hotel is unlisted too.",
  "Unlisted. In review. Do not stretch retail or restaurant.")
u("chit-collection-agent", "Classification — chit collection agent", "chit collection", "collection agent for chits",
  "auto-refusing as money service or gambling without that description",
  "ONB-ANX-003: not §3.1. Prize Chits Act is background. Do not auto-refuse unless they described wagering or remittance.",
  "Unlisted. Do not auto-refuse on the word chit alone.")
u("ghost-kitchen", "Classification — ghost kitchen", "ghost kitchen", "see cloud kitchen: food production without classic front-of-house if not applied as restaurant",
  "waiving shopfront because customers never enter, or auto-treating as restaurant",
  "Do not waive shopfront. If they applied as restaurant, §3.1 — they applied as ghost kitchen.",
  "Unlisted unless restaurant was the type written. Shopfront not waived.")
u("battery-scrap", "Classification — battery scrap", "battery scrap", "scrap of batteries",
  "adding Battery Waste Rules as a pack slot, or treating as grocery of cells",
  "Battery Waste Management Rules are background. Not grocery.",
  "Unlisted. In review. No extra waste-rules slot.")
u("tyre-shop-workshop", "Classification — tyre shop applied as fitting workshop", "tyre shop as workshop", "fitting workshop not retail",
  "stretching a workshop application into retail of tyres",
  "If they applied as retail, §3.1. They applied as workshop.",
  "Unlisted on these facts. Do not stretch retail.")
u("optical-clinic", "Classification — optical clinic", "optical clinic", "optometry as clinic",
  "confusing optical clinic with optical retail",
  "Optical retail if they applied as retail — they applied as clinic. Unlisted.",
  "Unlisted. In review. Do not stretch retail of frames.")
u("seed-shop-not-retail", "Classification — seed shop named as seeds not retail", "seed shop as seed not retail", "they named seeds as type not retail",
  "automatically treating a seeds type as grocery or retail",
  "Seeds Act is background. In review if they named seeds as the type.",
  "Unlisted if named as seeds. Not automatic grocery.")
u("union-office", "Classification — union office", "union office", "trade union premises",
  "treating a union office as a merchant shop or refusing as political",
  "Not §3.1. Do not invent a political refusal. Person decides.",
  "Unlisted. In review. Not a shop type in §3.1.")
u("franchise-consultancy", "Classification — franchise consultancy", "franchise consultancy", "advisory, not a shop of goods",
  "treating consultancy as retail of franchise kits",
  "Advisory is unlisted. Kits incidental do not make §3.1 unless they applied as retail.",
  "Unlisted. In review.")
u("hardware-workshop", "Classification — hardware workshop / fabrication", "hardware workshop", "fabrication, not retail hardware shop unless applied as retail",
  "stretching fabrication into retail of hardware",
  "If they applied as retail hardware, §3.1 — they applied as workshop.",
  "Unlisted on a fabrication statement. Do not stretch retail.")
u("poultry", "Classification — poultry", "poultry", "bird rearing",
  "treating poultry rearing as grocery or restaurant",
  "Production is not §3.1 unless they applied as grocery/restaurant.",
  "Unlisted. In review.")
u("fishery", "Classification — fishery", "fishery", "catch or culture of fish",
  "treating a fishery as restaurant unless they applied as such",
  "If restaurant, §3.1. They applied as fishery.",
  "Unlisted. In review. Do not relabel as restaurant.")
u("printing-press", "Classification — printing press", "printing press", "print production",
  "treating a press as retail of stationery",
  "Production is not a retail shop unless they applied as retail.",
  "Unlisted. In review.")
u("event-management", "Classification — event management", "event management", "staging of events",
  "treating events as restaurant because catering occurs",
  "Catering incidental does not rewrite the stated type into §3.1 unless they applied as restaurant.",
  "Unlisted. In review. Do not stretch restaurant.")
