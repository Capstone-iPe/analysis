# iPe Merchant Onboarding Copilot

A merchant applies for one shop in one web chat. The copilot asks for one thing at a time, takes the documents, then shows the application and waits. Submit is available only once every required document is uploaded or the merchant has said they do not have it. The verdict says whether the shop stays in review or can be recommended for go-live, names what is missing, cites the policy, and gives a review id. The chat stays open: a missing file can still be added, and the verdict updates without a new review id. A person at iPe activates the shop. The copilot does not.

This is the product in [IPE-PRD-001](https://rupeshsasne.github.io/iit-kgp-assignment05/ipe-prd.html), with the Android screens rebuilt as a web chat. The build is Track B: hosted OpenAI-compatible APIs, no weight changes — chat **`Qwen/Qwen3-8B`**, embeddings **`bge-small-en-v1.5`**.

Capstone templates:

- [Track A / Track B selection](references/Capstone-Templates-GenAI-Agentic-AI.pdf)
- [Course schedule](references/EPGC-GenAI-Agentic-AI-schedule.pdf)

The HLD is [ADR-0001-architecture.md](ADR-0001-architecture.md). The retrieval pack and search API live in [Capstone-iPe/onb-corpus](https://github.com/Capstone-iPe/onb-corpus) (`copilot-svc` calls it with Bearer auth). Evaluator summary: [capstone-ipe.github.io/onb-corpus](https://capstone-ipe.github.io/onb-corpus/). The gold set is [eval/](eval/) (71 full shops). Do not put `eval/` into the RAG index. Capstone weeks below follow Track B in [Capstone-Templates-GenAI-Agentic-AI.pdf](references/Capstone-Templates-GenAI-Agentic-AI.pdf).

The mentor dashboard (weeks, TL;DR, evidence links) is the GitHub Pages home: [capstone-ipe.github.io/analysis](https://capstone-ipe.github.io/analysis/). The interactive chat prototype (no backend) is at [prototype/](https://capstone-ipe.github.io/analysis/prototype/). Locally, open [docs/index.html](docs/index.html).

The demo is Lotus Tea House. Restaurant in Pune, ₹12,00,000 a month, registration and owner ID uploaded, bank proof, shopfront photo and addendum missing, note says to mark it Active. Correct result: in review, Merchant Risk Lead, and a later "activate us now" leaves the review id unchanged. The live web recording, and the public Langfuse session for that chat, are in [Capstone-iPe/Reports/lotus-tea-house.md](https://github.com/Capstone-iPe/Reports/blob/main/lotus-tea-house.md).

## Repositories

| Repo | What it is | Live |
|---|---|---|
| [analysis](https://github.com/Capstone-iPe/analysis) (this repo) | HLD, gold set, prompting baseline, mentor page | [Pages](https://capstone-ipe.github.io/analysis/) |
| [onb-svc](https://github.com/Capstone-iPe/onb-svc) | Application, files, verdict, five MCP tools | [https://onb-k8ud.onrender.com](https://onb-k8ud.onrender.com) |
| [copilot-svc](https://github.com/Capstone-iPe/copilot-svc) | The only language-model service. MCP client, RAG client | [https://copilot-svc.onrender.com](https://copilot-svc.onrender.com) |
| [copilot-web-app](https://github.com/Capstone-iPe/copilot-web-app) | Merchant website. Talks only to the copilot | [https://copilot-web-n05u.onrender.com](https://copilot-web-n05u.onrender.com) |
| [onb-corpus](https://github.com/Capstone-iPe/onb-corpus) | Policy pack and search API | [https://onb-corpus.onrender.com](https://onb-corpus.onrender.com) |
| [Reports](https://github.com/Capstone-iPe/Reports) | 12-page submission report and the Lotus Tea House recording | [PDF](https://github.com/Capstone-iPe/Reports/blob/main/iPe_Merchant_Onboarding_Copilot_Submission_Report.pdf) |

`GOOGLE_ENFORCE_ALLOWED_EMAILS` is off on the website, the copilot, and ONB, so any verified Google account can sign in. The free Render services sleep after about 15 minutes. Open the site, then [copilot health](https://copilot-svc.onrender.com/v1/health), [ONB health](https://onb-k8ud.onrender.com/health), and [corpus health](https://onb-corpus.onrender.com/health), and wait about a minute.

## Run the services locally

Four processes, one directory, four terminals. This repository holds the specification and the gold set. It does not listen on a port. The commands below are for macOS and Linux. On Windows, activate each virtual environment with `.venv\Scripts\activate` and keep the same ports.

Clone the repositories side by side. The copilot replay looks for `analysis/eval` next to `copilot-svc`, and the in-process ONB path looks for `onb-svc` in that same parent.

```bash
mkdir ipe && cd ipe
git clone https://github.com/Capstone-iPe/analysis.git
git clone https://github.com/Capstone-iPe/onb-corpus.git
git clone https://github.com/Capstone-iPe/onb-svc.git
git clone https://github.com/Capstone-iPe/copilot-svc.git
git clone https://github.com/Capstone-iPe/copilot-web-app.git
```

Install Python 3.12 and PostgreSQL 16. Each service gets its own virtual environment.

```bash
# macOS
brew install python@3.12 postgresql@16
brew services start postgresql@16

# Debian or Ubuntu
sudo apt install python3.12 python3.12-venv postgresql
```

Create two databases. Table names do not overlap, and separate databases keep an ONB reset from wiping chat history.

```bash
createdb ipe_onb
createdb ipe_copilot
```

If `createdb` asks for a password, put that user and password in the connection strings below: `postgresql://USER:PASSWORD@localhost:5432/ipe_onb`. A Homebrew install usually accepts `postgresql://localhost:5432/ipe_onb` for the account that created the database.

### Keys you have to bring

| Item | Where it goes | What it is |
|---|---|---|
| `EMBEDDINGS_API_KEY` and `vm02-ca.crt` | onb-corpus | Hosted embeddings, `bge-small-en-v1.5` at `https://103.42.50.41:1035/v1` |
| `CHAT_API_KEY` and `vm06-ca.crt` | copilot-svc and onb-svc | Hosted chat, `Qwen/Qwen3-8B` at `https://103.42.50.41:1032/v1` |
| `CORPUS_API_KEY` | the same string in onb-corpus and copilot-svc | Any long random secret you choose. `python3 -c "import secrets; print(secrets.token_hex(32))"` |
| Google OAuth web client | website, copilot, and ONB | One client id and secret |

The API keys and the two CA files are issued for the Capstone hosted endpoints. They are not in git. Keep them out of commits. The corpus index cannot be built without the embeddings key and `vm02-ca.crt`. The copilot cannot call the model without the chat key and `vm06-ca.crt`. ONB still starts without the chat key: document checks then use the rules checker.

Create one Google Cloud OAuth client of type **Web application**. Authorized redirect URIs:

- `http://localhost:5000/auth/callback` — the website
- `http://127.0.0.1:8000/auth/google/callback` — ONB, for an MCP client that signs in through ONB

Scopes the website requests are `openid`, `email`, and `profile`. While the consent screen is in testing, add the Google account you will use as a test user. Use that same client id on the website, the copilot, and ONB. Leave `GOOGLE_ENFORCE_ALLOWED_EMAILS` at `0`.

### Start order

| Order | Directory | Port | Ready when |
|---|---|---|---|
| 1 | `onb-corpus` | 8081 | `curl -sS http://127.0.0.1:8081/health` prints a status |
| 2 | `onb-svc` | 8000 | `curl -sS http://127.0.0.1:8000/health` prints `{"status":"ok"}` |
| 3 | `copilot-svc` | 8080 | `curl -sS http://127.0.0.1:8080/v1/health` answers |
| 4 | `copilot-web-app` | 5000 | http://localhost:5000 shows Google sign-in |

Each repository's README has the install commands and the full variable list. The local addresses are:

```bash
# onb-corpus .env
CORPUS_API_KEY=<the secret you chose>
EMBEDDINGS_API_KEY=<issued key>
EMBEDDINGS_CA_CERT=vm02-ca.crt

# onb-svc, sourced into the shell before python -m onb (this process does not read .env)
export DATABASE_URL=postgresql://localhost:5432/ipe_onb
export GOOGLE_CLIENT_ID=<client id>
export GOOGLE_CLIENT_SECRET=<client secret>
export ONB_PUBLIC_URL=http://127.0.0.1:8000
export CHAT_API_KEY=<issued key>
export CHAT_CA_CERT=$PWD/../copilot-svc/vm06-ca.crt
export CORPUS_SEARCH_URL=http://127.0.0.1:8081
export CORPUS_API_KEY=<the same secret>

# copilot-svc .env
ONB_MCP_URL=http://127.0.0.1:8000/mcp
CORPUS_SEARCH_URL=http://127.0.0.1:8081
CORPUS_API_KEY=<the same secret>
DATABASE_URL=postgresql://localhost:5432/ipe_copilot
GOOGLE_CLIENT_ID=<the same client id>
CHAT_API_KEY=<issued key>
CHAT_CA_CERT=vm06-ca.crt
COPILOT_LANGFUSE_ENABLED=false

# copilot-web-app .env
CHAT_SERVICE_URL=http://127.0.0.1:8080
GOOGLE_CLIENT_ID=<the same client id>
GOOGLE_CLIENT_SECRET=<the same client secret>
GOOGLE_REDIRECT_URI=http://localhost:5000/auth/callback
SECRET_KEY=<another secrets.token_hex(32)>
```

Sign in at http://localhost:5000 with Google. The page sends that access token to the copilot, and the copilot sends it on to ONB. **Continue as test merchant** belongs to the mock chat inside `copilot-web-app`. The real copilot rejects it.

To stop, Ctrl+C in each terminal. Postgres keeps the applications and the chat history. The next start uses the same databases.

## What we run

Two services we build. Chat and embeddings are the Capstone hosted OpenAI-compatible endpoints (models below). The copilot prompts the chat model. ONB's verdict is still plain rules. The document check can call the same hosted chat model, and a rules checker is the fallback.

```mermaid
flowchart LR
  FE[Web chat]
  A[Copilot<br/>8B + MCP client]
  ONB[ONB service<br/>pure Python<br/>rules, state, files]
  C[onb-corpus<br/>search API]
  DV[Document verifier<br/>rules or LLM]
  M[(≤8B chat)]
  E[(Embeddings)]

  FE -->|start, messages, submit| A
  A -->|generate| M
  A -->|"POST /v1/search Bearer"| C
  C -->|embed query| E
  A <-->|MCP tools| ONB
  ONB -->|verify file| DV
```

| Piece | Who provides it | What it is |
|---|---|---|
| Web chat | Us | One chat, as in the prototype: intake, a review summary, submit, then the verdict. The thread stays open. |
| Copilot | Us | The only language-model service. Prompts the 8B, runs the planner/executor/critic loop, calls onb-corpus for passages, is the MCP client, phrases every reply. |
| ONB service | Us | Owns application state and files, says what is needed next, runs the rule engine on submit and again when a file arrives after submit, allocates the review id once. The verdict stays rules. |
| onb-corpus | Us | Policy documents + authenticated search API. Owns embeddings calls and hybrid search. A reranker was measured and not kept. |
| Document verifier | Us | ONB calls it on `save_file`. Default mode is the LLM checker (`DOCUMENT_VERIFIER_MODE=llm`); `rules` is the deterministic fallback. [LLD-0001](docs/LLD-0001-document-verifier.md) is still a draft and still describes a rules-only checker. |
| ≤8B chat | Hosted API · `Qwen/Qwen3-8B` | The only language model. Used by the copilot (and the prompting baseline). |
| Embeddings | Hosted API · `bge-small-en-v1.5` | Turns text into numbers for policy search. Used by onb-corpus. |

## Tools ONB exposes over MCP

The copilot is the MCP client. The tool list is closed: there is no activate, waive, change-volume, or mark-complete tool, so no prompt can reach those actions.

| Tool | Job |
|---|---|
| `next_step` | Which field or upload is required next. The field order is policy, owned by ONB. |
| `save_answer` | Store the pending answer, or replace an answer already stored before submit. After the verdict, a stored answer stays as stored. |
| `save_file` | Store the upload and call the document verifier. The copilot forwards the file bytes. Rejected files do not clear the gap. |
| `submit` | First verdict. Refused while a required document is still open. Allocates the review id once, unless the type is refused. A later accepted file re-runs the same rules and keeps that id. |
| `get_review` | Return the existing review id. Never allocate a new one. |

Policy search is **not** an ONB tool. It is part of the copilot's RAG. The verdict stays model-free. The document verifier may call the chat model.

## Who decides what

- **ONB decides.** On submit, and again when a file arrives after submit, plain rules produce the outcome, missing items, business-type verdict, addendum requirement, and assignee. The review id is allocated once. No model is involved. Unit-testable on its own.
- **RAG cites.** The copilot retrieves the policy passage behind a "why?" answer or a citation. Wrong retrieval would mean a wrong citation, never a wrong decision.
- **The copilot speaks.** It plans, calls tools, retrieves, phrases the reply, and the critic checks the citation and strips ID, account, and phone numbers.

## Where Track B goes

Almost all of it lives in the copilot; ONB is plain rules and covers no syllabus by design. Weeks match the Track B template (I–VI).

| Template | Track B requirement | Where |
|---|---|---|
| I · Week 1 | Spec + gold set (60–100) before agent code | [eval/](eval/): 71 shops. G-001–G-050 to build against, G-051–G-071 once. **Correct** is the gold answer. |
| II · Week 1 | Three prompting strategies + how the ≤8B breaks | Done: [prompting-baseline/](prompting-baseline/). |
| III · Week 2 | RAG: 500–2,000 docs, chunking, hybrid, reranker, recall@k | [onb-corpus](https://github.com/Capstone-iPe/onb-corpus): 500 docs, 1,446 chunks + search API. Deployed search is hybrid 800/120. The reranker did not help hit@4 and is not in the live index. Copilot calls `/v1/search`. Recall scored: hit@4 = 0.958, hit@8 = 1.0. `eval/` stays out of the index. |
| IV · Week 3 | Planner → executor → critic, ≥3 tools, state, error handling | Copilot loop over ONB's five MCP tools. Memory is the ONB application row. Hand-rolled (ADR-0001); LangGraph not required. |
| V · Week 3–4 | E2E eval, failure taxonomy, tracing | Replay against [eval/](eval/). Scores + taxonomy in copilot-svc. Each live turn is exported to Langfuse. |
| VI · Week 4 | UI, container, rate limit, cache + responsible AI | Web chat on Render. Rate limit and policy-search cache on Key Value. Injection, PII, no activate tool, human for go-live. |

## Capstone weeks (Track B)

Status against [Capstone-Templates-GenAI-Agentic-AI.pdf](references/Capstone-Templates-GenAI-Agentic-AI.pdf). Product code is in `copilot-svc`, `onb-svc`, and `copilot-web-app`.

### Week 1 — task decomposition + prompting baseline

- [x] **I.** Spec: what the copilot does, what it refuses, and what a correct answer is. [ADR-0001](ADR-0001-architecture.md), this README, and [IPE-PRD-001](https://rupeshsasne.github.io/iit-kgp-assignment05/ipe-prd.html).
- [x] **I.** Gold set: 71 shops in [eval/](eval/) (60–100 required). Frozen before the agent loop.
- [x] **II.** Three strategies compared on Qwen3-8B (structured few-shot 6/10; CoT and decomposition 0/10). Write-up + runner + cases + results: [prompting-baseline/](prompting-baseline/) (not copilot agent code).
- [x] LLD (ours, not a template gate): FE ↔ copilot `ConversationView` frozen at v1.0 in [docs/LLD-0002-web-chat-contract.md](docs/LLD-0002-web-chat-contract.md). Exam-harness JSON is kept out of the product contract.
- [x] Extra: HLD in [ADR-0001](ADR-0001-architecture.md); policy search in [onb-corpus](https://github.com/Capstone-iPe/onb-corpus); mentor dashboard + [prototype](https://capstone-ipe.github.io/analysis/prototype/).

### Week 2 — RAG

- [x] Corpus size in range: [onb-corpus](https://github.com/Capstone-iPe/onb-corpus) has 500 documents (cap 2,000).
- [x] Chunking and hybrid retrieval (keyword + dense) are in `onb-corpus`. A reranker was measured and not kept. The copilot calls the search API.
- [x] Citation-grounded why / explain path (RAG cites; ONB decides).
- [x] Documented chunking / hybrid / rerank experiments (keep a setting only when it helps): [onb-corpus Pages](https://capstone-ipe.github.io/onb-corpus/) · [eval/retrieval.md](https://github.com/Capstone-iPe/onb-corpus/blob/main/eval/retrieval.md).
- [x] **recall@k** measured separately from end-to-end answer quality: hit@4 = 0.958, hit@8 = 1.0 (hybrid 800/120); [eval/results](https://github.com/Capstone-iPe/onb-corpus/tree/main/eval/results).

### Week 3 — agentic layer

- [x] Tool-using loop over at least three tools (five ONB MCP tools).
- [x] Explicit decide → act → say/critic path; persistent application state in ONB; ≤10 steps.
- [x] Error handling for bad labels, tool errors, and refusals (JSON schema on intent; retries on the classifier).
- [x] End-to-end accuracy write-up against the gold set (replay numbers in [copilot-svc/docs/eval.md](https://github.com/Capstone-iPe/copilot-svc/blob/main/docs/eval.md)).
- [x] Failure taxonomy: retrieval miss, wrong next step, tool-call error, hallucination / made-up policy (same doc).
- [x] Tracing dashboard (Langfuse) — each live turn is exported; the session id is the ONB application id. Write-up in [copilot-svc/docs/eval.md](https://github.com/Capstone-iPe/copilot-svc/blob/main/docs/eval.md).

### Week 4 — ship it

- [x] Front-end wired to live copilot (Google bearer → copilot → ONB); happy path works. Conversation history is in Postgres. `corpus_unavailable` and `unauthorized` reach the page.
- [x] Containerised deploy on Render, with a per-merchant rate limit and a policy-search cache on Render Key Value (`copilot-cache`).
- [x] Responsible-AI baseline: injection tests / adversarial lines, digit redaction, no activate tool, human-in-the-loop for go-live.
- [x] Live web demo of Lotus Tea House, with a public Langfuse session: [Reports/lotus-tea-house.md](https://github.com/Capstone-iPe/Reports/blob/main/lotus-tea-house.md).
- [x] 12-page technical report: [Reports/iPe_Merchant_Onboarding_Copilot_Submission_Report.pdf](https://github.com/Capstone-iPe/Reports/blob/main/iPe_Merchant_Onboarding_Copilot_Submission_Report.pdf).

## Submission checklist

### Ready for a CLI demo

- [x] ADR-0001 two services; five ONB MCP tools; no activate tool
- [x] Copilot CLI: one merchant line → intent → at most one tool → fixed or RAG reply
- [x] Guards, refusals, digit redaction, critic on model sentences
- [x] Replay runner against [eval/](eval/): G-001–G-050 while building; G-051–G-071 holdout once
- [x] Unit and adversarial tests in `copilot-svc`
- [x] Corpus indexed for RAG (≥500 docs); `eval/` stays out of the index

### Recorded

- [x] **copilot-svc README** — CLI, env, replay / holdout / retrieval / questions runners
- [x] **Week 1-II prompting runs** — [prompting-baseline/prompting-baseline.md](prompting-baseline/prompting-baseline.md). The scores are in the submission report.
- [x] **Week 2 recall@k** — scored in onb-corpus; hit@4 / hit@8 on fixed questions
- [x] **Week 3 failure taxonomy + traces** — [copilot-svc/docs/eval.md](https://github.com/Capstone-iPe/copilot-svc/blob/main/docs/eval.md)
- [x] Demo is the live web Lotus Tea House recording, not a CLI-only label.
- [x] Confirm recorded replay pass rates — build 50/50, holdout 21/21 in `copilot-svc/docs/results/`

### Live web path

- [x] FE talks only to the copilot (bearer); copilot talks to ONB (bearer). ConversationView v1.0 is frozen in [LLD-0002](docs/LLD-0002-web-chat-contract.md)
- [x] Conversation history for the chat UX is in Postgres (not used to decide tools or the verdict)
- [x] Tracing dashboard / exported per-turn traces (Langfuse)
- [x] Container, rate limit, cache — Render web service; 30 messages a minute per merchant; policy search cached for five minutes
- [x] Recorded end-to-end Lotus Tea House through the live web chat ([recording](https://drive.google.com/file/d/1aGw2Dstrzxs5dF9-OQt8KpjT1I-ihrHL/view?usp=sharing), [public Langfuse session](https://us.cloud.langfuse.com/project/cmwwc06zv025bad0djdu06aup/sessions/app_2fc9ace8d96b))
- [x] 12-page technical report: [Reports/iPe_Merchant_Onboarding_Copilot_Submission_Report.pdf](https://github.com/Capstone-iPe/Reports/blob/main/iPe_Merchant_Onboarding_Copilot_Submission_Report.pdf)

The mentor dashboard is [docs/index.html](https://capstone-ipe.github.io/analysis/#team-tasks).
