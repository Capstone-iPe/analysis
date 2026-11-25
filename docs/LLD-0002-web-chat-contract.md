# LLD-0002: Web chat ↔ copilot contract (ConversationView v1.0)

- Status: Frozen at **v1.0** (2026-11-23).
- Date: 2026-11-23
- Implements: [ADR-0001](../ADR-0001-architecture.md) D1 (the web chat talks only to the copilot) and D3 (ONB owns the verdict; the copilot does not alter a field)
- Machine-checkable form: [`copilot-web-app/contracts/chat_service.schema.json`](https://github.com/Capstone-iPe/copilot-web-app/blob/main/contracts/chat_service.schema.json) (`x-contract-version: 1.0`)
- Produced by: `copilot-svc` (`src/copilot/app.py`, `adapters/web.py`). Read by: `copilot-web-app` (`website/static/app.js`). The in-repo mock chat service in `copilot-web-app` produces the same shape.

## 1. Scope and rules

This is the only interface between the web chat and the copilot. It closes the Week 1 open item "FE ↔ copilot fields".

| Rule                                                 | Consequence                                                                                                                             |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| The web chat renders; it never decides (ADR-0001 D3) | Every status, verdict field, pill and step comes from the copilot. The page computes nothing about the application.                     |
| One shop, one conversation                           | A conversation id is the ONB application id. A second shop is a new conversation.                                                       |
| The product contract is closed                       | Objects have exactly the fields in §4. A field not listed is not part of the product, even if it is harmless.                           |
| Exam-harness JSON is not the product API             | Scoring fields, verifier evidence and ONB internals stay in the replay harness, traces or ONB (§5). They are never sent to the browser. |
| Merchant text is data                                | Nothing in this contract lets a message change the verdict, the review id, or a stored answer after the verdict.                        |

## 2. Transport and identity

Base URL: `CHAT_SERVICE_URL` (live: `https://copilot-svc.onrender.com`). JSON bodies, except file uploads (multipart).

| Header          | Value                                                                                                                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | `Bearer <Google access token>` for a merchant signed in with Google. The copilot checks it with Google (audience = the web client id) and forwards it to ONB. Development sign-in uses `Bearer <CHAT_SERVICE_TOKEN>` and works only with the in-repo mock. |
| `X-Merchant-Id` | `google:<sub>` from the same Google sign-in. A mismatch with the bearer is `401 unauthorized`.                                                                                                                                                             |

A merchant sees only their own conversations. Another merchant's id is `404 not_found`, never `403`, so ids cannot be probed.

## 3. Endpoints

| Call                  | Request                                                                                                              | Success                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Create a conversation | `POST /v1/conversations`, body empty, or `{"application_id": "<id>"}` to reopen one of this merchant's conversations | `201 {conversation}` (`200` when reopening)                  |
| List conversations    | `GET /v1/conversations`                                                                                              | `200 {conversations: [ListItem]}`, newest `updated_at` first |
| Load a conversation   | `GET /v1/conversations/{id}`                                                                                         | `200 {conversation}`                                         |
| Send a message        | `POST /v1/conversations/{id}/messages` `{"text", "action", "client_message_id"}`                                     | `200 {conversation, reply}`                                  |
| Upload a file         | `POST /v1/conversations/{id}/files`, multipart `document`, `file`, `client_message_id`                               | `200 {conversation, reply}`                                  |
| Health                | `GET /v1/health`, no headers                                                                                         | `200`, body not part of the contract                         |

Message body:

- `text`: what the merchant typed or the pill's `value`, at most 2,000 characters.
- `action`: `"submit"` when the merchant presses Submit, otherwise `null`. Submit ignores `text`.
- `client_message_id`: 1–128 characters, made by the page, one per merchant turn. A repeat with the same id returns the stored reply and does not run the turn again. The same id with different input is `409 message_id_reused`.

Upload: `document` is one of the five slot ids in §4.2. `file` is PDF, JPG or PNG, at most 10 MB. `client_message_id` behaves as for messages. Before the verdict, the page uploads only for the slot being asked for. After the verdict, a file for a missing slot re-runs ONB's rules: the outcome may change, and the review id does not.

## 4. Objects (frozen)

### 4.1 ConversationView

| Field                      | Type                                                       | Meaning                                                                    | The page uses it for           |
| -------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------ |
| `id`                       | string                                                     | ONB application id, `app_` + 12 hex (mock: `c_` + 12)                      | URL `/c/<id>`, every call      |
| `shop_name`                | string \| null                                             | Stored legal name, once given                                              | Side panel, header, shops list |
| `status`                   | `DRAFT` \| `IN_REVIEW` \| `RECOMMEND_GO_LIVE` \| `REFUSED` | `DRAFT` until the first verdict, then the verdict's outcome                | Status badge                   |
| `review_id`                | string \| null                                             | `MR-<digits>` once a review exists; `null` before submit and for `REFUSED` | Side panel                     |
| `steps`                    | Steps                                                      | Progress of the three steps                                                | Step list                      |
| `messages`                 | Message[]                                                  | Whole transcript, oldest first                                             | Thread                         |
| `prompt`                   | Prompt                                                     | What to offer under the last message                                       | Pills, text box, file picker   |
| `result`                   | Result \| null                                             | The current verdict; `null` before submit                                  | Side panel state               |
| `created_at`, `updated_at` | string                                                     | ISO 8601, UTC                                                              | List order                     |

**Steps:** `shop_details`, `documents`, `submitted`, each `todo` \| `current` \| `done`.

**ListItem** (from `GET /v1/conversations`): `id`, `shop_name`, `status`, `review_id`, `updated_at`.

### 4.2 Message, attachments and cards

| Field         | Type                              | Meaning                                                                                           |
| ------------- | --------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`          | string                            | Opaque, `m_` + up to 32 characters                                                                |
| `role`        | `merchant` \| `assistant`         | Who said it                                                                                       |
| `text`        | string                            | Already redacted by the copilot's critic (no ID, account or phone digits)                         |
| `attachments` | `[{document, filename}]`          | `document` ∈ `business_registration`, `owner_id`, `bank_proof`, `shopfront_photo`, `dpa_addendum` |
| `card`        | null \| SummaryCard \| ResultCard | Drawn under the text                                                                              |
| `created_at`  | string                            | ISO 8601, UTC                                                                                     |

- **ResultCard:** `{"type": "result"}` plus exactly the six Result fields below.
- **SummaryCard** (optional; the copilot sends the read-back as text today): `{"type": "summary", "rows": [{"label", "value"}]}`.

**Result** (exactly these six, from ONB's verdict; ADR-0001 §6 minus the exam fields):

| Field           | Type                                               |
| --------------- | -------------------------------------------------- |
| `outcome`       | `IN_REVIEW` \| `RECOMMEND_GO_LIVE` \| `REFUSED`    |
| `missing_items` | slot id[]                                          |
| `assignee`      | `MERCHANT_RISK_LEAD` \| `HEAD_OF_PAYMENTS` \| null |
| `review_id`     | `MR-<digits>` \| null                              |
| `citations`     | string[], e.g. `ONB-POL-001 §2`                    |
| `volume_inr`    | integer ≥ 0                                        |

### 4.3 Prompt and pills

| Field    | Type                                                    | Meaning                                                                                                                |
| -------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `field`  | string \| null                                          | Pending field or slot, `summary` before submit, `change` while choosing an answer to replace, `null` after the verdict |
| `kind`   | `text` \| `choice` \| `upload` \| `summary` \| `closed` | `closed` = after the verdict                                                                                           |
| `input`  | boolean                                                 | Show the text box                                                                                                      |
| `pills`  | Pill[]                                                  | Buttons under the question                                                                                             |
| `accept` | subset of `.pdf .jpg .jpeg .png`                        | File types for the picker                                                                                              |

A **Pill** is `{label, action}` plus:

- `value` (the text to send), required when `action` is `send`
- `document` (which slot), required when `action` is `upload`

The `submit` action needs neither. After the verdict, the copilot sends one `upload` pill per missing slot. There is no pill, field or action that activates a shop.

## 5. Not in the product contract

These exist, and stay where they are used. They never reach the browser.

| Field                                                                                                       | Lives in                                        | Why it stays out                                                                                           |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `injection_flagged`, `policy_conflict_noted`, `business_type_allowed`, `addendum_required`, `invalid_items` | ONB verdict → copilot → replay harness / scorer | Exam-harness scoring fields. The merchant reads the effect in the reply text and citations.                |
| `files` (per-slot state, verifier `evidence`, reason codes)                                                 | ONB snapshot                                    | Internal. Evidence can carry extracted document detail; the merchant sees the accept/reject as reply text. |
| Top-level `evidence` on upload replies                                                                      | Verifier                                        | As above.                                                                                                  |
| `trace`, `asking`, `assistant_texts`, dialogue state                                                        | Copilot / traces                                | Implementation detail; traces go to the trace export.                                                      |

The replay harness talks to the copilot directly, not through this API, so it keeps every field it scores.

## 6. Errors

Every error is `{"error": {"code", "message"}}`. **The page chooses its own wording by `code`.** `message` is for logs and developers, and may contain detail merchants must not see. The page shows the server's `message` only for the input errors marked †.

| Code                  | Status  | From    | Meaning                                                                      | Page behaviour                                                                                                                                       |
| --------------------- | ------- | ------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `unauthorized`        | 401     | copilot | Bearer missing, invalid, or rejected by ONB; or merchant id mismatch         | Website refreshes the Google token once and retries. If still rejected: sign out, show the sign-in page with a plain message.                        |
| `forbidden`           | 403     | copilot | Token issued for another Google client                                       | Sign out, "this account is not allowed".                                                                                                             |
| `sign_in_required`    | 401     | website | Website session ended                                                        | Go to the sign-in page.                                                                                                                              |
| `not_found`           | 404     | copilot | No such conversation for this merchant                                       | Open the merchant's latest conversation instead; say the link isn't available.                                                                       |
| `corpus_unavailable`  | 502     | copilot | Policy search failed mid-turn. ONB may already have saved the answer.        | Not retried automatically. Reload the conversation to show its true state; keep the merchant's typed text; say policy search is briefly unavailable. |
| `onb_unavailable`     | 502/503 | copilot | ONB asleep or failing                                                        | Website retries reads and id-carrying writes; then "waking up" with **Try again** (same `client_message_id`).                                        |
| `history_unavailable` | 503     | copilot | Conversation store unavailable                                               | As `onb_unavailable`.                                                                                                                                |
| `chat_unavailable`    | 503     | website | Copilot asleep or unreachable                                                | "Waking up" with **Try again**.                                                                                                                      |
| `conversation_busy`   | 409     | copilot | Another request holds this conversation                                      | Retry with the same `client_message_id`.                                                                                                             |
| `rate_limited`        | 429     | copilot | This merchant sent more messages or files than the minute allows             | Not retried. Keep the typed text. Say to wait a minute.                                                                                              |
| `turn_interrupted`    | 409     | copilot | An earlier turn was interrupted; the copilot reconciled it without replaying | Reload the conversation; the copilot has appended an explanation.                                                                                    |
| `message_id_reused`   | 409     | copilot | Same id, different input                                                     | Generic error; the next send gets a new id.                                                                                                          |
| `conversation_exists` | 409     | copilot | Create raced with an existing id                                             | Generic error.                                                                                                                                       |
| `empty_message`†      | 400     | copilot | No text and no submit                                                        | Show message.                                                                                                                                        |
| `no_file`†            | 400     | both    | No file in the upload                                                        | Show message.                                                                                                                                        |
| `bad_document`†       | 400     | mock    | `document` is not a slot id (the copilot should do the same, §9)             | Show message.                                                                                                                                        |
| `unsupported_type`†   | 415     | both    | Not PDF/JPG/PNG                                                              | Show message.                                                                                                                                        |
| `file_too_large`†     | 413     | website | Over 10 MB                                                                   | Show message.                                                                                                                                        |
| `bad_request`         | 400/500 | both    | Anything else                                                                | Generic error.                                                                                                                                       |

## 7. Behaviour the contract guarantees

1. **Reload shows the same conversation.** `GET /v1/conversations/{id}` returns the stored view, including `prompt`. The list is ordered by `updated_at`, newest first.
2. **A retry never runs a turn twice.** A turn is keyed by `client_message_id`. An interrupted turn is reconciled on the next load, not replayed.
3. **The review id is allocated once.** It never changes after the first verdict, including after a late upload or an "activate us now" message.
4. **Answers lock at the verdict.** Before submit, a stored answer can be replaced through the `change` prompt. After it, no field changes except a missing slot's file.

## 8. Changing the contract

- **Adding an optional field** is a minor change (1.1). Update this LLD and the schema in the same pull request. The page must still work if the field is absent.
- **Renaming, removing, or changing a type or enum** is a breaking change. Serve it under `/v2/…` and keep `/v1/…` until the web chat has moved.
- **Conformance is checked, not assumed:**
  - `copilot-web-app` tests validate every mock response against the schema.
  - `tools/check_contract.py --url <service>` checks a running copilot (mock or live) the same way.

## 9. Conformance on freeze (copilot-svc `main`, 2026-11-23)

Checked by building views with `copilot-svc`'s own web adapter and validating them against the v1.0 schema:

| Item                                                                         | Status          | Change needed in copilot-svc                                                                                                                                                       |
| ---------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ConversationView, Message, Prompt, Pill, Steps, Result, ResultCard, ListItem | Match           | —                                                                                                                                                                                  |
| `conversation.files`                                                         | Not in contract | Remove `"files"` from `_update_view`'s key list and from `WebAdapter.open`/`render` output (`app.py`, `adapters/web.py`). Update `tests/test_http.py`, which currently asserts it. |
| Top-level `evidence` on file replies                                         | Not in contract | Stop adding `resp["evidence"]` in `_run_turn` (`app.py`). Keep it in the trace.                                                                                                    |
| Timestamps to the second                                                     | Allowed, weak   | Two conversations touched in the same second list in id order. Prefer milliseconds in `new_message`/`_now`.                                                                        |
| Edge: upload when nothing is pending sends `document: ""`                    | Not in contract | Reject a `document` that is not a slot id with `400 bad_document` before the turn, as the mock does.                                                                               |
| Edge: verdict without an outcome renders `outcome: ""`                       | Not in contract | Treat as an ONB error (`502 onb_unavailable`), not a result.                                                                                                                       |
