# HFT-P2-07 — Notification channel and price data provider

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-07 |
| Title | Notification channel and price data provider |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | `docs/hedge-fund-transition/PLAN.md` §6, §8 (P2 tasks 7-8); `docs/hedge-fund-transition/ORG-BLUEPRINT.md` §11A.6-11A.7; `docs/hedge-fund-transition/TRANSPLANT-MANIFEST.md`; `docs/hedge-fund-transition/evidence/design-addendum-01.md`; decisions.md (DEC-01..DEC-38); `.claude/hooks/notify.sh`; external sources cited inline |
| Writing standard | ASD-STE100 |

## 1. Scope

This document covers P2 tasks 7 and 8:

1. Select the notification channel from the tools the new repository's
   environment can reach (DEC-28).
2. Select the price, volume, and flow data provider from the DEC-31
   source list (OpenDART stays fixed for disclosures and financials).

## 2. Part A — Notification channel

### 2.1 Constraints that apply

- DEC-28: W1 delivers every product through an HTML dashboard and one
  notification channel. P2 selects the channel.
- DEC-32: holdings and personal data stay in a gitignored local
  directory. No classification scheme exists yet in W1.
- R-14: a product states that it is for the user's own decisions. No
  product goes to a third party in wave W1.
- The environment is Claude Code: the CLI, the desktop app, the web
  app, and cloud sessions (brief, §"Context").

### 2.2 Design rule that follows from DEC-32 and R-14

Any channel that runs through an external company's servers (a chat
app, a connector) must carry a pointer, not the data. The message says
a product is ready. The user opens the local dashboard or the
gitignored directory for the values. **INFERENCE**: this rule lets an
external channel comply with DEC-32 and R-14 without giving up on
using that channel.

### 2.3 Options

| # | Option | What the user receives | Setup effort | Works with no session open | Third-party data exposure | Cost | Source |
|---|---|---|---|---|---|---|---|
| A | Claude mobile app push (Remote Control) | A push alert on the phone; Claude picks the text, or the user asks for one in a prompt | Low: install the Claude app, sign in with the same account, run `/config` and turn on push | No. The local `claude` process must keep running (a terminal, `tmux`, or `screen`) | None beyond the phone OS's own push relay (Apple or Google); content is set by Claude, so it stays pointer-only under the rule in §2.2 | Free with a claude.ai subscription | [Remote Control docs](https://code.claude.com/docs/en/remote-control), accessed 2026-09-25 |
| B | Telegram channel (official plugin) | A two-way chat message in Telegram; Claude replies in the same chat | Medium: create a bot with BotFather, install the plugin, restart with `--channels`, pair the account | No. Events arrive only while a session is open (a background process still counts as open) | The message text passes through Telegram's servers, a third party. Keep it pointer-only per §2.2 | Free (Telegram itself charges nothing) | [Channels docs](https://code.claude.com/docs/en/channels), accessed 2026-09-25 |
| C | Scheduled cloud Routine, built-in push or email | A push to the phone, an email, or both, when a run finishes | Low: turn on notifications when the Routine is created; no extra account beyond claude.ai | Yes. Routines run on Anthropic-managed cloud infrastructure on a schedule | None beyond the phone OS's push relay and the user's own inbox; no separate chat-app company is in the path | Counts against the normal subscription usage; no added fee documented | [Routines docs](https://code.claude.com/docs/en/routines), accessed 2026-09-25; Routine-notification behavior also confirmed against this session's own scheduling tool, 2026-09-25 |
| D | Local desktop notification hook (`.claude/hooks/notify.sh`, already in the transplant set) | A Windows toast popup | None. The file is already marked TAKE in the transplant manifest | No. It fires only while a local interactive session is open and is waiting on the user | None. Fully local; no network call | Free | `docs/hedge-fund-transition/TRANSPLANT-MANIFEST.md:143,211`; `.claude/hooks/notify.sh:59-70` |
| E | Slack message via a Routine connector | A message posted to a Slack channel | Medium: connect a Slack workspace as a connector, add it to the Routine | Yes. Runs on cloud infrastructure on a schedule | The message passes through Slack's servers, a third party. Keep it pointer-only per §2.2 | Free at small scale, but needs a Slack workspace the user must set up and maintain | [Routines docs](https://code.claude.com/docs/en/routines) (backlog-maintenance example: "posts a summary to Slack"), accessed 2026-09-25 |

A GitHub issue was considered and dropped from the table. GitHub
triggers are documented only as an *inbound* path (a GitHub event
starts a Routine), not as an outbound notification path. Using an
issue as a notification would also place data on GitHub's servers,
which the pointer-only rule in §2.2 would still have to guard.
**INFERENCE**.

### 2.4 Recommendation

Recommend **Option C: the scheduled cloud Routine's built-in push and
email notification**, sent pointer-only ("the daily briefing is
ready; open the dashboard").

Reason: it is the only option that both reaches the user with no
local machine or terminal left open (DEC-28's environment already
includes cloud sessions) and adds no third-party chat-app company to
the data path (DEC-32, R-14). Setup is a single toggle on the Routine
that produces the daily briefing. Option D (the existing desktop
hook) stays in place as a free, zero-risk supplement for interactive
sessions, since it costs nothing to keep. Option A is a good second
choice if the founder prefers to keep a local session open through
the day.

### 2.5 The HTML dashboard half of DEC-28

DEC-28 also asks for an HTML dashboard. Two options exist:

- **A static HTML file generated into the repository.** The file
  reads from the gitignored local directory at generation time and is
  itself written to a location `.gitignore` also excludes, so it never
  reaches a remote. Lowest risk under DEC-32.
- **A hosted page** (for example, a published Artifact). This is
  visible outside the local machine and must **never** carry holdings
  data, per DEC-32 and R-14. A hosted page may only carry a schedule,
  a status line, or a pointer to the local file.

**Recommend the static, locally generated file** for any content that
touches holdings. A hosted page, if the founder wants one, is limited
to non-holdings content. **GAP**: whether the founder wants a hosted
page at all is not settled by any DEC-NN; see decision P2-D-01.

## 3. Part B — Price, volume, and flow data provider

### 3.1 Constraints that apply

- DEC-31: OpenDART covers disclosures and financials (fixed, out of
  scope here). Exchange or broker data covers prices, volume, and
  flows. Web search covers regulation, news, and macro (out of scope
  here). P2 selects the price provider.
- DEC-15: Korean listed equities now; US equities can join later via
  config. Data adapters stay per source (DEC-31), so the US extension
  is a separate adapter, not a rewrite of the Korean one.
- DEC-30: agents read, analyze, and record. Agents never draft or
  send orders. A data source that needs a brokerage account is
  acceptable for data only.
- DEC-32 / R-14: any data pulled in stays local; a provider's terms on
  storing data for internal, non-redistributed use are what matters
  here, not terms on public redistribution (this system does not
  redistribute).

### 3.2 Options

| # | Option | Data offered | Delay | Cost | Account / approval | Storage or redistribution limit | Rate limit | US extension path | Source |
|---|---|---|---|---|---|---|---|---|---|
| A | KRX Data Marketplace / KRX OPEN API (Korea Exchange, official) | Listed-stock OHLCV, short-selling data, investor-type (foreign / institutional / individual) flow data, index data, per the service list | GAP: exact latency per dataset not confirmed; official exchange source, end-of-day for most listed items (INFERENCE) | Free authentication key; some data products are paid, with a 50% discount for academic/public-interest use | Register as a Data Marketplace member; apply for and get approval on each API individually | GAP: full terms not read in this pass; a paid-product page states per-product terms | GAP: not confirmed | No US coverage; a separate adapter is needed for US equities | [KRX Data Marketplace OPEN API](https://openapi.krx.co.kr/contents/OPP/INFO/OPPINFO001.jsp), accessed 2026-09-25 (WebSearch summary; direct fetch blocked by this session's network egress proxy) |
| B | 공공데이터포털 (data.go.kr), 금융위원회_주식시세정보 (FSC stock price API) | Listed-stock and related-security OHLC and volume, by ticker and date | Next business day, after 13:00 (T+1); not real-time | Free | A data.go.kr account and an API key request | GAP: not read in this pass | GAP: not confirmed | No US coverage; separate adapter needed | [금융위원회_주식시세정보](https://www.data.go.kr/data/15094808/openapi.do), accessed 2026-09-25 (WebSearch summary; direct fetch blocked by this session's network egress proxy) |
| C | Korea Investment & Securities, KIS Developers Open API (broker) | Domestic and overseas equities: quotes, daily and intraday data; account/order endpoints exist but are not used (DEC-30) | Near real-time for quotes (REST) and streaming (WebSocket); GAP on exact latency figure | Currently free; one source notes a future paid tier is possible (**INFERENCE**, not confirmed) | Needs a KIS brokerage account (real or paper) plus an Open API service application (certificate login, phone verification) | GAP: not read in this pass | Approximately 20 requests/second on a real-trading account (sliding window); a paper-trading account has a lower limit | Same platform's overseas-stock endpoints cover US equities: the natural US-extension path | [KIS Developers portal](https://apiportal.koreainvestment.com/apiservice); [koreainvestment/open-trading-api](https://github.com/koreainvestment/open-trading-api), accessed 2026-09-25 (WebSearch summary and GitHub fetch; the portal domain itself was blocked by this session's network egress proxy) |
| D | Kiwoom Securities REST API / Open API+ (broker) | Domestic equities: quotes, conditional search, real-time via WebSocket; a separate overseas-derivatives Open API also exists | GAP: not confirmed | GAP: not confirmed | Needs a Kiwoom brokerage account and separate Open API+ usage registration | GAP: not read in this pass | GAP: not confirmed | An overseas-derivatives Open API exists; whether it covers US cash equities is GAP | [Kiwoom Open API+](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView); [KIWOOM REST API](https://openapi.kiwoom.com/guide/index?dummyVal=0), accessed 2026-09-25 |
| E | pykrx (open-source Python library, scrapes KRX and Naver) | OHLCV, fundamentals (PER/PBR/EPS/BPS/DIV/DPS), investor-type flow, short-selling volume/value/balance, index data, market cap, foreign-ownership rate | Matches the source site's own update timing; no separate SLA (unofficial) | Free | None; `pip install` only | The project asks users to "refrain from indiscriminate calls" and notes data copyright belongs to KRX/Naver; commercial redistribution needs the providers' own terms. This system does not redistribute (R-14), which lowers this risk | No stated hard limit; the project's own guidance against indiscriminate calls is the only control | No US coverage; a separate adapter is needed. **Fallback pairing**: `FinanceDataReader` (same open-source family) gives a unified KR+US OHLCV interface and is a candidate for that later adapter | [sharebook-kr/pykrx](https://github.com/sharebook-kr/pykrx), accessed 2026-09-25 |

`FinanceDataReader` was researched as a sixth candidate and is folded
into the table as E's paired option rather than given its own row: it
covers KRX and US OHLCV under one interface (MIT license) but, unlike
pykrx, does not carry investor-type flow or short-selling data, so it
does not stand alone against DEC-31's "prices, volume, and flows."
[FinanceData/FinanceDataReader](https://github.com/FinanceData/FinanceDataReader), accessed 2026-09-25.

### 3.3 Recommendation

Recommend **Option A (KRX Data Marketplace OPEN API) as the primary
source, with Option E (pykrx) as the fallback**.

Reasons:

- Option A is the exchange-direct, official source. It carries the
  least legal and terms-of-use risk of the five, and it covers every
  data type DEC-31 asks for (prices, volume, flows) in one place,
  including the short-selling and investor-type flow data that a
  long-biased, downside-aware book needs (DEC-06).
- Option A does not need a brokerage account, so it keeps the data
  path separate from any account that could later carry order
  authority. This keeps the data-only boundary in DEC-30 clean by
  construction, not by policy alone.
- Option A's per-API approval step (§3.2) can take time the founder
  may not want to wait on before the first milestone (DEC-27: one
  daily briefing, one stock through the full pipeline). **Option E
  (pykrx) covers the same data shapes with no approval wait**, so it
  is the fallback: usable from day one, and a safety net if a KRX
  API approval is delayed or a specific dataset needs a paid tier
  the founder has not yet approved.
- Option C (KIS) is not the primary because a brokerage-account data
  path is unnecessary when a non-broker official source (Option A)
  already covers the same ground; the task brief allows a broker
  source for data only, but does not require one when it is not
  needed. Option C stays the natural candidate for the **US
  extension adapter** later (DEC-15), because its overseas-equity
  endpoints sit on the same platform as its Korean ones.
- Option D (Kiwoom) is not recommended: several of its facts are GAP
  in this pass (cost, exact rate limit, overseas cash-equity
  coverage), and Option C already gives a broker-based path if one is
  ever needed.
- Option B (data.go.kr) is not recommended as primary because its
  T+1, post-13:00 delay is too slow for a daily briefing that should
  reflect the prior trading day promptly; it remains a plausible
  second fallback if both A and E are unavailable. **GAP**: not
  scored against A/E head-to-head in this pass.

This selection is data-only. No agent gains order-sending capability
through any of these sources (DEC-30).

## 4. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-D-01 | Which notification channel carries W1 product-ready alerts? | A. Claude mobile push (Remote Control); B. Telegram channel; C. Scheduled Routine push/email; D. Local desktop hook only; E. Slack via Routine connector | Recommend C (pointer-only), with D kept as a free supplement. Reason and sources: §2.4. |
| P2-D-02 | Does the HTML dashboard stay a local generated file, or does the founder also want a hosted page for non-holdings status only? | A. Local generated file only; B. Local file plus a hosted status-only page | No recommendation (founder judgment): both meet DEC-32 if the hosted page never carries holdings data; the choice is about convenience, not risk. See §2.5. |
| P2-D-03 | Which price/volume/flow provider does data-steward implement first? | A. KRX Data Marketplace OPEN API; B. data.go.kr FSC stock price API; C. KIS Developers Open API; D. Kiwoom REST API; E. pykrx | Recommend A as primary, E as fallback. Reason and sources: §3.3. |
| P2-D-04 | Which source becomes the US-equities adapter when US coverage activates (DEC-15)? | Not yet scoped in this pass; candidates noted in §3.2/§3.3 are KIS Developers (Option C, broker overseas endpoints) and FinanceDataReader (paired with Option E) | Deferred: decide when US coverage activates (DEC-15 asks only for preparation in W1). GAP: a head-to-head US-source comparison was not run. |

## Founder decisions recorded (2026-09-25)

The founder answered the items above. HFT-P2-00 §4 is the register; §4A states the consequences.

| ID | Answer |
|---|---|
| P2-D-01 | B: Telegram channel |
| P2-D-02 | C: local generated file, plus a market summary with no holdings in the Telegram message |
| P2-D-03 | C: KIS Developers Open API (Korea Investment & Securities) |
| P2-D-04 | Deferred to US activation (DEC-15). KIS overseas endpoints are the first candidate. |

## 5. Traceability

| P2 task / DEC-NN | Covered in |
|---|---|
| P2 task 7 (select notification channel) | §2 |
| P2 task 8 (select price/data provider) | §3 |
| DEC-28 (dashboard + one channel; P2 selects) | §2.1, §2.3, §2.4, §2.5 |
| DEC-31 (OpenDART fixed; exchange/broker data for prices/volume/flows; P2 selects) | §3.1, §3.2, §3.3 |
| DEC-32 (gitignored local directory for holdings) | §2.1, §2.2, §2.5, §3.1 |
| DEC-30 (agents never send orders) | §3.1, §3.3, §3.3 closing line |
| DEC-15 (Korean equities now; US later via config) | §3.1, §3.2 (US-extension column), §3.3, P2-D-04 |
| R-14 (products are for the user only) | §2.1, §2.2, §2.4 |
| DEC-36 (drafts need no approval; final status needs a receipt) | Document control (Status field) |
