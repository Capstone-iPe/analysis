MEMOS = []


def add(**kw):
    kw.setdefault("folder", "opinions/shopfront")
    kw.setdefault("owner", "Head of Merchant Risk — Legal")
    kw.setdefault("related", "ONB-POL-001 §2.5; ONB-ANX-001")
    MEMOS.append(kw)


add(
    slug="day-ninety-inclusive",
    title="The ninetieth day before submit is valid",
    issue="Whether a shopfront photograph taken on the ninetieth day before submit is stale.",
    facts="The photograph’s date is exactly ninety days before the submission date.",
    rule="ONB-POL-001 §2.5: the ninetieth day before submit is valid; the ninety-first is not. ONB-ANX-001: day 90 inclusive. General Clauses briefing: day-count follows the policy as written.",
    application="Inclusive counting is the rule, not a courtesy. The Copilot shall not treat day 90 as stale to be conservative, shall not extend to day 91, and shall not activate. Operations date the file.",
    held="Day 90 valid. Day 91 not. Copilot does not activate.",
    copilot="Cite ONB-POL-001 §2.5. Do not extend. Do not activate.",
)

add(
    slug="day-ninety-one-stale",
    title="The ninety-first day before submit is stale",
    issue="Whether a photograph taken ninety-one days before submit can be accepted because it is ‘about ninety’.",
    facts="The photograph is dated 91 days before submit. The merchant asks for rounding.",
    rule="ONB-POL-001 §2.5: day 91 is not valid. The Limitation Act briefing: limitation law does not extend the ninety-day shopfront window.",
    application="Rounding would rewrite §2.5. The Copilot shall say the photo is stale, shall not accept it in words, shall not activate, and shall not waive because FSSAI or a Shops Act certificate exists.",
    held="Stale. Slot outstanding.",
    copilot="Cite ONB-POL-001 §2.5. Do not round. Do not waive.",
)

add(
    slug="limitation-act-no-extension",
    title="The Limitation Act does not extend shopfront age",
    issue="Whether limitation or condonation language can add days to the shopfront window.",
    facts="The merchant cited the Limitation Act, 1963, or asked for condonation of delay on a stale photo.",
    rule="Limitation briefing: the Act does not extend the 90-day shopfront window. ONB-POL-001 §2.5 is the count.",
    application="Onboarding is not a suit. Condonation is not a Copilot power. Request a photograph within date. Do not activate.",
    held="No extension. Stale remains stale.",
    copilot="Cite ONB-POL-001 §2.5. Do not condone. Do not activate.",
)

add(
    slug="online-only-no-waiver",
    title="Online-only does not waive shopfront",
    issue="Whether denying a physical front waives the shopfront photograph.",
    facts="The merchant said they are online-only and have no facade.",
    rule="ONB-ANX-001: online-only does not waive shopfront. ONB-POL-001 §2 lists the item; the Copilot shall not waive it.",
    application="This product did not create a no-premises pack. The Copilot shall not skip the photograph, shall not substitute a website screenshot, and shall not activate. If the type named is online-only store, it is unlisted as well (ONB-ANX-003).",
    held="Shopfront not waived. Website is not the photograph.",
    copilot="Cite ONB-ANX-001 and §2. Do not waive. Do not activate.",
)

add(
    slug="submit-date-not-photo-exif-debate",
    title="Age is counted on the submission date; the Copilot does not run forensics",
    issue="Whether the Copilot should parse EXIF, argue about clocks, or recompute submit date to save a stale photo.",
    facts="The merchant asked the Copilot to read EXIF or to treat today as a different submit date.",
    rule="ONB-POL-001 §2.5: counted on the submission date. Verification is operational. The Copilot does not decide acceptance.",
    application="EXIF debate in chat is not verification and may leak location. The Copilot shall explain day 90/91, shall not claim to have parsed EXIF, shall not change submit date, and shall not activate.",
    held="Explain the count. Do not forensically accept. Do not alter submit date.",
    copilot="Cite ONB-POL-001 §2.5. Do not pretend to parse EXIF. Do not activate.",
)
