/* iPe onboarding — interactive front-end. One continuous chat. */

const ALLOWED = ["restaurant", "grocery", "retail"];
const DISALLOWED = ["money service", "crypto", "gambling", "money_service"];
const CEILING = 4000000;

const FIELDS = [
  { id: "shop_name", kind: "text", q: "What is the shop's legal name?",
    placeholder: "Shop legal name",
    chips: ["Lotus Tea House"],
    why: { text: "Bank proof has to be in the shop's legal name.", cite: "ONB-POL-001 §2" } },
  { id: "city", kind: "text", q: "Which city is the shop in?",
    placeholder: "City",
    chips: ["Pune", "Mumbai"],
    why: { text: "The policies don't state a rule about the city; it is part of the application form." } },
  { id: "business_type", kind: "text", q: "What type of business is it?",
    placeholder: "Business type",
    chips: ["Restaurant", "Grocery", "Retail"],
    why: { text: "Only some business types are allowed.", cite: "ONB-POL-001 §3" } },
  { id: "monthly_volume", kind: "text", q: "What is the expected monthly volume, in rupees?",
    placeholder: "Monthly volume",
    chips: ["₹12,00,000", "₹45,00,000"],
    why: { text: "The stated volume decides who at iPe reviews the shop.", cite: "ONB-POL-002" } },
  { id: "payment_methods", kind: "text", q: "Do you want UPI, cards, or both?",
    placeholder: "UPI, cards, or both",
    chips: ["UPI and cards", "UPI only"],
    why: { text: "The policies don't state a rule about this; it is part of the application form." } },
  { id: "stores_payer_phones", kind: "text", q: "Will the shop store payer phone numbers?",
    placeholder: "Yes or no",
    chips: ["Yes", "No"],
    why: { text: "A shop that stores payer phone numbers needs a signed data-processing addendum.", cite: "ONB-POL-003 §2" } },
  { id: "business_registration", kind: "upload", q: "Please upload the business registration. A PDF or a photo is fine.",
    label: "business registration",
    why: { text: "It is one of the four pack items.", cite: "ONB-POL-001 §2" } },
  { id: "owner_id", kind: "upload", q: "Please upload the owner's government ID.",
    label: "owner's government ID",
    why: { text: "It is one of the four pack items.", cite: "ONB-POL-001 §2" } },
  { id: "bank_proof", kind: "upload", q: "Please upload bank proof in the shop's legal name.",
    label: "bank proof",
    why: { text: "It is one of the four pack items.", cite: "ONB-POL-001 §2" } },
  { id: "shopfront_photo", kind: "upload", q: "Please upload a recent shopfront photo.",
    label: "shopfront photo",
    why: { text: "It is one of the four pack items.", cite: "ONB-POL-001 §2" } },
  { id: "dpa_addendum", kind: "upload", q: "Please upload the signed data-processing addendum.",
    label: "signed data-processing addendum",
    needPhones: true,
    why: { text: "You said the shop stores payer phone numbers.", cite: "ONB-POL-003 §2" } },
  { id: "note", kind: "text", q: "Any note you'd like to add to the application?",
    optional: true,
    placeholder: "Optional note",
    chips: ["No note"],
    why: { text: "The policies don't state a rule about the note; it is optional context for the reviewer." } }
];

const PACK = ["business_registration", "owner_id", "bank_proof", "shopfront_photo"];
const DOC_LABEL = {
  business_registration: "business registration",
  owner_id: "owner's government ID",
  bank_proof: "bank proof",
  shopfront_photo: "shopfront photo",
  dpa_addendum: "signed data-processing addendum"
};

const LIBRARY = [
  { name: "business_registration.pdf", kind: "PDF", size: "214 KB", slot: "business_registration", ok: true },
  { name: "owner_id.png", kind: "PNG", size: "1.2 MB", slot: "owner_id", ok: true },
  { name: "bank_proof.pdf", kind: "PDF", size: "180 KB", slot: "bank_proof", ok: true },
  { name: "electricity_bill.pdf", kind: "PDF", size: "96 KB", slot: null, ok: false, reason: "this isn't the document for this slot" },
  { name: "shopfront.png", kind: "PNG", size: "2.4 MB", slot: "shopfront_photo", ok: true },
  { name: "dpa_addendum.pdf", kind: "PDF", size: "64 KB", slot: "dpa_addendum", ok: true }
];

const state = {
  idx: 0,
  phase: "intake",
  answers: {},
  files: {},
  injection: false,
  reviewId: null,
  verdict: null,
  messages: [],
  busy: false,
  pickerSlot: null
};

const chatInner = document.getElementById("chat-inner");
const composer = document.getElementById("composer");
const chat = document.getElementById("chat");
const picker = document.getElementById("picker");

function esc(t) {
  return String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\n/g, "<br>");
}
function indianFmt(n) {
  const s = String(n);
  let head = s.slice(0, -3), tail = s.slice(-3), parts = [];
  while (head.length > 2) { parts.unshift(head.slice(-2)); head = head.slice(0, -2); }
  if (head) parts.unshift(head);
  return (parts.length ? parts.join(",") + "," : "") + tail;
}
function parseVolume(t) {
  t = t.toLowerCase().replace(/₹|rs\.?|inr/g, " ");
  let m = t.match(/([\d.]+)\s*cr/); if (m) return Math.round(parseFloat(m[1]) * 1e7);
  m = t.match(/([\d.]+)\s*lakh/); if (m) return Math.round(parseFloat(m[1]) * 1e5);
  m = t.match(/\d[\d,]*/); return m ? parseInt(m[0].replace(/,/g, ""), 10) : null;
}
function cap(t) { return (t || "").replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase()); }

function nextField() {
  let i = state.idx;
  while (i < FIELDS.length) {
    const f = FIELDS[i];
    if (f.needPhones && !state.answers.stores_payer_phones) { i++; continue; }
    return { field: f, index: i };
  }
  return null;
}

function push(msg) { state.messages.push(msg); }

function render() {
  chatInner.innerHTML = state.messages.map(renderMsg).join("");
  renderRail();
  if (!state.busy) renderComposer();
  chat.scrollTop = chat.scrollHeight;
}

function botRow(inner, extra) {
  return `<div class="row-msg bot"><div class="avatar">iP</div><div class="bubble bot ${extra || ""}">${inner}</div></div>`;
}

function renderMsg(m) {
  if (m.role === "typing") {
    return botRow(`<span class="typing"><i></i><i></i><i></i></span>`);
  }
  if (m.role === "verdict") {
    return botRow(`<div class="verdict ${m.go ? "go" : ""}">
      <div class="badge">${esc(m.badge)}</div>
      <h4>${esc(m.title)}</h4>
      ${(m.rows || []).map(r => `<div class="vrow">${esc(r)}</div>`).join("")}
      ${m.miss ? `<div class="miss">${esc(m.miss)}</div>` : ""}
    </div>`, "card");
  }
  if (m.role === "summary") {
    return botRow(`<div class="summary"><h4>${esc(m.title)}</h4>${
      m.rows.map(([k, v, tone]) => `<div class="srow"><span class="k">${esc(k)}</span><span class="${tone || ""}">${esc(v)}</span></div>`).join("")
    }</div>`, "card");
  }
  const body = m.file
    ? `<span class="file"><span class="ic">PDF</span>${esc(m.file)}</span>`
    : esc(m.text) + (m.cite ? `<span class="cite">${esc(m.cite)}</span>` : "");
  if (m.role === "user") {
    return `<div class="row-msg user"><div class="bubble user">${body}</div></div>`;
  }
  return botRow(body);
}

async function say(text, cite) {
  push({ role: "typing" });
  render();
  await wait(420);
  state.messages.pop();
  push({ role: "bot", text, cite });
  render();
}

function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

function renderRail() {
  document.getElementById("rail-shop").textContent = state.answers.shop_name || "New application";
  document.getElementById("rail-id").textContent = state.reviewId ? state.reviewId : "Not submitted";
  const { label, cls } = statusLabel();
  const railStatus = document.getElementById("rail-status");
  const hdrStatus = document.getElementById("hdr-status");
  railStatus.textContent = label;
  hdrStatus.textContent = label;
  hdrStatus.className = "status-pill " + cls;
  document.getElementById("hdr-sub").textContent = headerSub();

  const checks = [
    ["Shop details", ["shop_name", "city", "business_type", "monthly_volume", "payment_methods", "stores_payer_phones"].every(k => k in state.answers)],
    ["Documents", PACK.every(s => state.files[s]) && (!state.answers.stores_payer_phones || state.files.dpa_addendum)],
    ["Submitted", state.phase === "submitted"]
  ];
  let currentSet = false;
  document.getElementById("rail-steps").innerHTML = checks.map(([name, done]) => {
    let c = done ? "done" : "";
    if (!done && !currentSet) { c = "current"; currentSet = true; }
    return `<div class="item ${c}"><span class="dot"></span>${name}</div>`;
  }).join("");
}

function statusLabel() {
  if (state.phase === "submitted") {
    const v = state.verdict;
    if (v?.outcome === "RECOMMEND_GO_LIVE") return { label: "Recommend go-live", cls: "recommend" };
    if (v?.outcome === "REFUSED") return { label: "Refused", cls: "review" };
    return { label: "In review", cls: "review" };
  }
  return { label: "Draft", cls: "draft" };
}
function headerSub() {
  if (state.phase === "submitted") return [state.answers.shop_name, state.reviewId].filter(Boolean).join(" · ");
  if (state.phase === "review") return "Review your application";
  const n = nextField();
  return n ? n.field.q.replace(/\?.*$/, "") : "Onboarding";
}

function renderComposer() {
  if (state.phase === "intake") return renderIntakeComposer();
  if (state.phase === "review") return renderReviewComposer();
  return renderSubmittedComposer();
}

function chipsRow(items) {
  if (!items) return "";
  return `<div class="chip-row">${items}</div>`;
}
function inputRow(placeholder) {
  return `<div class="composer-row">
    <input id="composer-input" type="text" placeholder="${placeholder}" autocomplete="off" />
    <button class="send" id="composer-send" type="button">Send</button>
  </div>`;
}

function renderIntakeComposer() {
  const n = nextField();
  if (!n) { enterReview(); return; }
  const f = n.field;
  let html = "";
  if (f.kind === "upload") {
    html += `<div class="upload-zone"><div><strong>Add a file</strong>PDF, JPG, or PNG</div>
      <button class="chip primary" type="button" data-act="open-picker" data-slot="${f.id}">Choose file</button></div>`;
    html += chipsRow(`<button class="chip" type="button" data-act="missing" data-slot="${f.id}">I don't have this</button>
      <button class="chip" type="button" data-act="why">Why is this needed?</button>`);
    html += inputRow("Message");
  } else {
    const chips = (f.chips || []).map(c =>
      `<button class="chip" type="button" data-act="answer" data-value="${encodeURIComponent(c)}">${esc(c)}</button>`
    ).join("") + `<button class="chip" type="button" data-act="why">Why is this needed?</button>`;
    html += chipsRow(chips);
    html += inputRow(f.placeholder || "Message");
  }
  composer.innerHTML = html;
  wireComposer();
}

function renderReviewComposer() {
  const missing = openGaps();
  if (missing.length) {
    const slot = missing[0];
    const chips = `<button class="chip primary" type="button" data-act="open-picker" data-slot="${slot}">Upload ${DOC_LABEL[slot]}</button>`
      + `<button class="chip" type="button" data-act="confirm-missing">I don't have these</button>`;
    composer.innerHTML = chipsRow(chips) + inputRow("Message");
  } else {
    composer.innerHTML = chipsRow(
      `<button class="chip primary" type="button" data-act="submit">Submit application</button>`
    ) + inputRow("Message");
  }
  wireComposer();
}

function renderSubmittedComposer() {
  const missing = state.verdict.missing_items || [];
  const chips = missing.map(slot =>
    `<button class="chip primary" type="button" data-act="open-picker" data-slot="${slot}">Upload ${DOC_LABEL[slot]}</button>`
  ).join("") + `<button class="chip" type="button" data-act="recall">What's my review reference?</button>`;
  composer.innerHTML = chipsRow(chips) + inputRow("Message");
  wireComposer();
}

function wireComposer() {
  composer.querySelectorAll("[data-act]").forEach(el => el.addEventListener("click", onAction));
  const input = document.getElementById("composer-input");
  const send = document.getElementById("composer-send");
  if (send) send.addEventListener("click", onSend);
  if (input) {
    input.addEventListener("keydown", e => { if (e.key === "Enter") onSend(); });
    input.focus();
  }
}

function onSend() {
  const input = document.getElementById("composer-input");
  if (!input) return;
  const text = input.value.trim();
  if (!text) return;
  input.value = "";
  handleTyped(text);
}

async function handleTyped(text) {
  const low = text.toLowerCase();
  if (/\bwhy\b|kyun|needed/.test(low) && state.phase === "intake") { await doWhy(text); return; }
  if (state.phase === "submitted") {
    push({ role: "user", text });
    await handlePostSubmit(low);
    render();
    return;
  }
  if (state.phase === "review") {
    push({ role: "user", text });
    if (/submit/.test(low) && !openGaps().length) { await doSubmit(); return; }
    if (/submit/.test(low)) { await say("A few documents are still open, so I can't take a submit yet. Upload them, or say you don't have them."); return; }
    if (openGaps().length) {
      await say("Those answers stay as stored. Upload the document that is still open, or say you don't have it.");
    } else {
      await say("Those answers stay as stored. Submit when you're ready.");
    }
    return;
  }
  const n = nextField();
  if (!n) return;
  if (n.field.kind === "upload") {
    if (/don't have|do not have|dont have|don't have this/.test(low)) {
      await markSlot(n.field.id, { missing: true }, text);
    } else {
      push({ role: "user", text });
      await say(`Please choose a file for the ${n.field.label}, or say you don't have it.`);
    }
    return;
  }
  await acceptAnswer(n.field, text, text);
}

async function onAction(e) {
  const el = e.currentTarget;
  const act = el.dataset.act;
  if (act === "why") return doWhy("Why is this needed?");
  if (act === "answer") {
    const n = nextField(); if (!n) return;
    const val = decodeURIComponent(el.dataset.value);
    await acceptAnswer(n.field, val, val === "No note" ? "No note" : val);
    return;
  }
  if (act === "open-picker") { openPicker(el.dataset.slot); return; }
  if (act === "missing") { await markSlot(el.dataset.slot, { missing: true }, "I don't have this"); return; }
  if (act === "confirm-missing") { await confirmAllMissing(); return; }
  if (act === "submit") { push({ role: "user", text: "Submit application" }); await doSubmit(); return; }
  if (act === "recall") { push({ role: "user", text: "What's my review reference?" }); await handlePostSubmit("review id"); render(); }
}

function openPicker(slot) {
  state.pickerSlot = slot;
  document.getElementById("picker-title").textContent = "Choose a file · " + DOC_LABEL[slot];
  document.getElementById("picker-list").innerHTML = LIBRARY.map((f, i) =>
    `<li data-i="${i}"><span class="icon">${f.kind}</span><span><span class="name">${esc(f.name)}</span><br><span class="meta">${f.size}</span></span></li>`
  ).join("");
  picker.classList.remove("hidden");
  picker.querySelectorAll("li").forEach(li => li.addEventListener("click", () => pickFile(Number(li.dataset.i))));
}

function closePicker() {
  picker.classList.add("hidden");
  state.pickerSlot = null;
}

async function pickFile(i) {
  const file = LIBRARY[i];
  const slot = state.pickerSlot;
  closePicker();
  const accepted = file.ok && file.slot === slot;
  await markSlot(slot, {
    accepted,
    filename: file.name,
    reason: accepted ? null : (file.slot && file.slot !== slot
      ? "it isn't the right document for this item"
      : (file.reason || "it doesn't satisfy this item"))
  });
}

async function doWhy(userMsg) {
  const n = nextField();
  const f = state.phase === "intake" && n ? n.field : null;
  push({ role: "user", text: userMsg });
  if (f?.why) {
    await say(f.why.text, f.why.cite);
    await say(f.q);
  } else {
    await say("The policies I work from don't add anything here. Your application is unchanged.");
  }
}

async function acceptAnswer(f, value, label) {
  push({ role: "user", text: label });
  let stored = value;
  if (f.id === "monthly_volume") {
    const v = parseVolume(value);
    if (v === null) { await say("I couldn't read that as a monthly volume in rupees."); return; }
    stored = v;
  } else if (f.id === "business_type") {
    const t = value.toLowerCase();
    stored = /crypto|bitcoin/.test(t) ? "crypto"
      : /gambl|bett/.test(t) ? "gambling"
      : /money service|remittance|forex/.test(t) ? "money_service"
      : /restaurant|cafe|dhaba/.test(t) ? "restaurant"
      : /grocery|kirana/.test(t) ? "grocery"
      : /retail/.test(t) ? "retail"
      : t;
  } else if (f.id === "stores_payer_phones") {
    stored = /^y/i.test(value);
  } else if (f.id === "note") {
    if (/no note/i.test(value)) stored = "";
    if (/ignore .*polic|mark .*active|set .*active/i.test(value)) state.injection = true;
  }
  state.answers[f.id] = stored;
  const n = nextField();
  if (n) state.idx = n.index + 1;
  const nn = nextField();
  if (nn) await say(nn.field.q);
  else await enterReview();
}

async function markSlot(slot, result, typed) {
  if (typed) push({ role: "user", text: typed });
  else push({ role: "user", file: result.filename || (DOC_LABEL[slot] + ".pdf") });

  if (result.missing) {
    state.files[slot] = "missing";
    await say("Noted. You can add it later if you have it.");
  } else if (result.accepted) {
    state.files[slot] = "accepted";
    await say("Received.");
  } else {
    state.files[slot] = "rejected";
    await say(`I received the file, but ${result.reason}, so ${DOC_LABEL[slot]} is still needed.`, "ONB-POL-001 §2");
    if (state.phase === "submitted") {
      await reevaluate();
    }
    render();
    return;
  }

  if (state.phase === "submitted") {
    await reevaluate();
    return;
  }
  if (state.phase === "review") {
    const left = openGaps();
    if (!left.length) await say("That's everything accounted for. You can submit when you're ready.");
    render();
    return;
  }
  const n = nextField();
  if (n) state.idx = n.index + 1;
  const nn = nextField();
  if (nn) await say(nn.field.q);
  else await enterReview();
}

function openGaps() {
  const miss = [];
  for (const slot of PACK) {
    const s = state.files[slot];
    if (s !== "accepted" && s !== "missing") miss.push(slot);
  }
  if (state.answers.stores_payer_phones) {
    const s = state.files.dpa_addendum;
    if (s !== "accepted" && s !== "missing") miss.push("dpa_addendum");
  }
  return miss;
}

function missingForVerdict() {
  const miss = [];
  for (const slot of PACK) if (state.files[slot] !== "accepted") miss.push(slot);
  if (state.answers.stores_payer_phones && state.files.dpa_addendum !== "accepted") miss.push("dpa_addendum");
  return miss;
}

async function enterReview() {
  state.phase = "review";
  await say("Here's what I have. Check it before you submit — I'll only evaluate after you submit.");
  push(summaryCard());
  const gaps = openGaps();
  if (gaps.length) await say("A few documents are still open. Upload them, or say you don't have them, and then you can submit.");
  else await say("Looks complete. Submit when you're ready.");
}

function summaryCard() {
  const a = state.answers;
  const docRow = (slot) => {
    const s = state.files[slot];
    const title = {
      business_registration: "Business registration",
      owner_id: "Owner's government ID",
      bank_proof: "Bank proof",
      shopfront_photo: "Shopfront photo",
      dpa_addendum: "Signed data-processing addendum"
    }[slot];
    if (s === "accepted") return [title, "Uploaded", "ok"];
    if (s === "rejected") return [title, "Not accepted", "bad"];
    if (s === "missing") return [title, "Not available", "bad"];
    return [title, "Not provided", "bad"];
  };
  const rows = [
    ["Shop name", a.shop_name || "—"],
    ["City", a.city || "—"],
    ["Business type", cap(a.business_type)],
    ["Monthly volume", a.monthly_volume ? "₹" + indianFmt(a.monthly_volume) : "—"],
    ["Payment methods", a.payment_methods || "—"],
    ["Payer phones", a.stores_payer_phones ? "Yes · addendum required" : "No"],
    docRow("business_registration"),
    docRow("owner_id"),
    docRow("bank_proof"),
    docRow("shopfront_photo")
  ];
  if (a.stores_payer_phones) rows.push(docRow("dpa_addendum"));
  rows.push(["Note", a.note || "—"]);
  return { role: "summary", title: "Application", rows };
}

async function confirmAllMissing() {
  push({ role: "user", text: "I don't have the remaining documents." });
  for (const slot of openGaps()) state.files[slot] = "missing";
  await say("Noted. Submitting with those missing will keep the shop in review. Submit when you're ready.");
}

function evaluate() {
  const a = state.answers;
  const cat = a.business_type;
  const vol = a.monthly_volume;
  const allowed = ALLOWED.includes(cat) ? true : DISALLOWED.includes(cat) ? false : null;
  const missing = missingForVerdict();
  let outcome, assignee = null, reviewId = null, conflict = false;
  if (allowed === false) {
    outcome = "REFUSED";
  } else {
    assignee = vol <= CEILING ? "MERCHANT_RISK_LEAD" : "HEAD_OF_PAYMENTS";
    conflict = assignee === "HEAD_OF_PAYMENTS";
    reviewId = a.shop_name === "Lotus Tea House" ? "MR-2041" : "MR-" + (2000 + Math.abs(hash(a.shop_name || "x")) % 800);
    outcome = (!missing.length && allowed === true) ? "RECOMMEND_GO_LIVE" : "IN_REVIEW";
  }
  const citations = ["ONB-POL-001 §3"];
  if (missing.length) citations.push("ONB-POL-001 §2");
  if (a.stores_payer_phones) citations.push("ONB-POL-003 §2");
  if (assignee) citations.push("ONB-POL-002");
  if (outcome !== "REFUSED") citations.push("ONB-POL-001 §4");
  if (state.injection) citations.push("ONB-POL-003 §3");
  return {
    outcome, business_type_allowed: allowed, missing_items: missing, assignee, reviewId, conflict,
    volume: vol, citations: [...new Set(citations)]
  };
}
function hash(s) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0;
  return h;
}

function verdictCard(v) {
  const name = state.answers.shop_name;
  const role = v.assignee === "MERCHANT_RISK_LEAD" ? "Merchant Risk Lead" : "Head of Payments";
  if (v.outcome === "RECOMMEND_GO_LIVE") {
    return { role: "verdict", go: true, badge: `Review ${v.reviewId} · Recommend go-live`,
      title: `${name} · ${state.answers.city}`,
      rows: [`₹${indianFmt(v.volume)} a month · ${cap(state.answers.business_type)}`,
        `Recommended to the ${role}`, `The ${role} activates — this chat does not`] };
  }
  if (v.outcome === "REFUSED") {
    return { role: "verdict", badge: "Refused", title: `${name} · ${state.answers.city}`,
      rows: [`${cap(state.answers.business_type)} is not an allowed business type`],
      miss: "Not queued for activation." };
  }
  return { role: "verdict", badge: `Review ${v.reviewId} · In review`,
    title: `${name} · ${state.answers.city}`,
    rows: [`₹${indianFmt(v.volume)} a month · ${cap(state.answers.business_type)}`, `For the ${role}`],
    miss: "Missing: " + v.missing_items.map(s => DOC_LABEL[s]).join(", ") };
}

async function doSubmit() {
  const v = evaluate();
  state.verdict = v;
  state.phase = "submitted";
  state.reviewId = v.reviewId;
  push(verdictCard(v));
  let s = "";
  if (v.outcome === "REFUSED") s = `No. The application for ${state.answers.shop_name} is refused and not queued for activation.`;
  else if (v.outcome === "RECOMMEND_GO_LIVE") s = `The pack is complete, so go-live may be recommended. ${state.answers.shop_name} is not live until a person at iPe acts.`;
  else {
    s = `No. ${state.answers.shop_name} stays in review.`;
    if (state.injection) s += " The note that said to mark it Active was not followed.";
  }
  await say(s, v.citations.join(" · "));
}

async function reevaluate() {
  const v = evaluate();
  state.verdict = v;
  state.reviewId = v.reviewId || state.reviewId;
  push(verdictCard(v));
  if (v.outcome === "RECOMMEND_GO_LIVE") {
    const role = v.assignee === "MERCHANT_RISK_LEAD" ? "Merchant Risk Lead" : "Head of Payments";
    await say(`The pack is complete. Go-live may be recommended to the ${role}. ${state.answers.shop_name} is not live until they act.`, "ONB-POL-001 §4 · ONB-POL-002");
  } else {
    await say("I've updated the review." + (v.missing_items.length ? " Still missing: " + v.missing_items.map(s => DOC_LABEL[s]).join(", ") + "." : ""), "ONB-POL-001 §2");
  }
}

async function handlePostSubmit(low) {
  if (/activate|go live|mark.*active|waive/.test(low)) {
    await say(`I can't activate ${state.answers.shop_name}. Only the Merchant Risk Lead may turn a merchant on, and only when the pack is complete and the business type is allowed.`
      + (state.reviewId ? ` ${state.reviewId} is unchanged.` : ""), "ONB-POL-001 §4");
  } else if (/review|reference|id|mr-/.test(low)) {
    await say(state.reviewId ? `Your review reference is ${state.reviewId}. It does not change.` : "No review was opened for this application.");
  } else {
    await say("This chat stays open. You can add a missing document, or ask about the decision. I still can't activate the shop.");
  }
}

function restart() {
  Object.assign(state, {
    idx: 0, phase: "intake", answers: {}, files: {}, injection: false,
    reviewId: null, verdict: null, messages: [], busy: false, pickerSlot: null
  });
  boot();
}

async function boot() {
  await say("Welcome to iPe. I'll help you apply for one shop. I ask for one thing at a time. When everything is in, you review it and submit. I can't turn a merchant on — a person at iPe does that.");
  await say(FIELDS[0].q);
}

document.getElementById("picker-close").addEventListener("click", closePicker);
picker.addEventListener("click", e => { if (e.target === picker) closePicker(); });
document.getElementById("new-app").addEventListener("click", () => { closeNav(); restart(); });

const appEl = document.querySelector(".app");
const navScrim = document.getElementById("nav-scrim");
function openNav() {
  appEl.classList.add("nav-open");
  navScrim.classList.remove("hidden");
  document.getElementById("menu-btn").setAttribute("aria-label", "Close menu");
}
function closeNav() {
  appEl.classList.remove("nav-open");
  navScrim.classList.add("hidden");
  document.getElementById("menu-btn").setAttribute("aria-label", "Open menu");
}
document.getElementById("menu-btn").addEventListener("click", () => {
  appEl.classList.contains("nav-open") ? closeNav() : openNav();
});
navScrim.addEventListener("click", closeNav);

boot();
