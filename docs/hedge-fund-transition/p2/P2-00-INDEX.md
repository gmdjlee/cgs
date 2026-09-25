# HFT-P2-00 — Phase P2 Design Package: Index and Approval

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-00 |
| Title | Phase P2 design package: index and approval |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval. All 25 open items answered (2026-09-25). |
| Owner | Advisor (main session) |
| Inputs | [PLAN.md](../PLAN.md) §8 P2; HFT-P2-01 to HFT-P2-07 |
| Writing standard | ASD-STE100 |

## 1. Purpose

This package is the output of Phase P2 (target design) in
[PLAN.md](../PLAN.md) §8. The exit criterion of P2 is a founder approval
receipt for the package. Section 5 holds the receipt form.

All documents in this package are drafts. DEC-36 lets an agent write a
draft with no approval. A change to final status needs the founder's
approval receipt.

## 2. Package contents

| ID | Document | P2 task | Author | Advisor check |
|---|---|---|---|---|
| HFT-P2-01 | [P2-01-ROSTER.md](P2-01-ROSTER.md): final wave roster, model tiers, tool allow-lists | 1, 9 | Worker | Checked. Added cio delegation to market-strategist and red-team-analyst, and chief-of-staff routing. |
| HFT-P2-02 | [P2-02-LIFECYCLE.md](P2-02-LIFECYCLE.md) and [workflow-catalog.draft.yaml](workflow-catalog.draft.yaml): lifecycle catalog | 2 | Worker | Checked. The YAML parses and keeps the live catalog shape. Resolved P2-L-02. |
| HFT-P2-03 | [P2-03-CONTROL-MODEL.md](P2-03-CONTROL-MODEL.md): verdicts, seats, review depth, receipts, limits, investment committee | 3, 10 | Worker | Checked. Moved the limit files to `config/risk/`. |
| HFT-P2-04 | [P2-04-CONFIG-SCHEMA.md](P2-04-CONFIG-SCHEMA.md) and [project.draft.yaml](project.draft.yaml): config schema | 4 | Worker | Checked. Changed `modes.rigor` from `minimal` to a `standard` proposal and added P2-S-04. |
| HFT-P2-05 | [P2-05-BUILD-PRIORITY.md](P2-05-BUILD-PRIORITY.md): build order and deferred components | 5 | Worker | Checked. Renamed the decision IDs to P2-B. |
| HFT-P2-06 | [P2-06-TERM-MAP.md](P2-06-TERM-MAP.md): Korean-English term map | 6 | Worker | Checked. |
| HFT-P2-07 | [P2-07-CHANNEL-AND-DATA.md](P2-07-CHANNEL-AND-DATA.md): notification channel and price data provider | 7, 8 | Worker | Checked. Deferred P2-D-04 to US activation. |

P2 task 11 (present the package to the founder) is this document.
The P2 outputs in PLAN.md also name `ORG-BLUEPRINT.md` (updated for the
DEC-NN choices, v0.5) and the `TRANSPLANT-MANIFEST.md` draft (v0.3,
Section 10). Both were updated before this package.

## 3. Method

1. The Advisor wrote one shared brief with the context, the output
   rules, and the decisions DEC-01 to DEC-38.
2. Six Workers wrote the seven documents in parallel.
3. The Advisor checked each document against the decision log and
   the cited files, corrected the defects in the "Advisor check"
   column, and committed each document separately.
4. Every agent check in this package is a pre-screen (F-09). The
   founder's approval receipt is the required human sign-off.

## 4. Founder decision register

The documents raise 27 items. The Advisor resolved 1 item (P2-L-02).
One item waits for a later trigger (P2-D-04). The founder decides the
other 25 items. "Rec." is the recommended option. "None" means the
document gives no recommendation (founder judgment).

| ID | Topic | Rec. | Status |
|---|---|---|---|
| P2-R-01 | Model tier for risk-analyst (W3) | A (Haiku) | Decided 2026-09-25: A: Haiku |
| P2-R-02 | Model tier for governance-secretary (W3) | A (Haiku) | Decided 2026-09-25: A: Haiku |
| P2-R-03 | research-analyst instances: all clusters or on demand | None | Decided 2026-09-25: C: hybrid. All 6 clusters run once a week for the weekly report; at other times only a cluster with a signal runs |
| P2-L-01 | `pre-setup` as a gated stage before S1 | A | Decided 2026-09-25: A: `pre-setup` is a gated stage before S1 |
| P2-L-02 | Correct the addendum's "Quarterly" cadence text | A | Resolved by the Advisor (the addendum is a frozen record; DEC-35 governs) |
| P2-L-03 | Replace `/gate-check` reference files with the `gate:` block | B | Decided 2026-09-25: B: the `gate:` block replaces the reference files |
| P2-C-01 | Owner of the investment committee minutes | A (chief-of-staff) | Decided 2026-09-25: A: chief-of-staff keeps the minutes |
| P2-C-02 | Review depth for the 12 products DEC-20 does not name | A (accept the table) | Decided 2026-09-25: A: accept the table |
| P2-C-03 | Receipt path `production/control/receipts.log`; limits in `config/risk/` | A | Decided 2026-09-25: A: `production/control/receipts.log`; limits in `config/risk/` |
| P2-C-04 | When to fix the missing fail tier in one CCGS vocabulary | A (P4 task 1) | Decided 2026-09-25: A: fix in P4 task 1 |
| P2-S-01 | How `modes.automation` expresses DEC-36 | B (new value `draft_free`) | Decided 2026-09-25: B: add the value `draft_free` |
| P2-S-02 | Rename the `qa.level` and `modes.review_mode` values | None | Decided 2026-09-25: B: rename the values in P3, before P3 builds the readers |
| P2-S-03 | More `strategy` values now | A (`long_biased` only) | Decided 2026-09-25: A: `long_biased` only |
| P2-S-04 | Start value of `modes.rigor` | B (`standard`) | Decided 2026-09-25: B: `standard` |
| P2-B-01 | Build place for four unordered W1 skills | A | Decided 2026-09-25: A: the proposed order |
| P2-B-02 | W1 dashboard reuses the 10 UI/UX deferred components | A | Decided 2026-09-25: A: reuse all 10 for the W1 dashboard |
| P2-B-03 | Four investor-facing deferred components wait for W2 | A | Decided 2026-09-25: A: wait for W2 |
| P2-B-04 | `/call-review` reuses the PROCEED/PIVOT/KILL memo shape | A | Decided 2026-09-25: A: reuse the memo shape |
| P2-B-05 | `setup-engine` waits for W2 | A | Decided 2026-09-25: A: wait for W2 |
| P2-T-01 | Korean names for the five new agent roles | None | Decided 2026-09-25: A: 수석보좌역, 시장전략가, 레드팀 애널리스트, 종목 스크리너, 데이터 스튜어드 |
| P2-T-02 | Korean form of the CRO title in products | C | Decided 2026-09-25: C: by context, as recommended |
| P2-T-03 | Korean term for "pre-screen" | None | Decided 2026-09-25: A: 사전 검토 |
| P2-T-04 | Use 일반 사모펀드 as the only current fund-type term | A | Decided 2026-09-25: A: 일반 사모펀드 only |
| P2-D-01 | Notification channel | C (scheduled Routine push or email, pointer only) | Decided 2026-09-25: B: Telegram channel (differs from the recommendation) |
| P2-D-02 | Dashboard: local file only, or also a hosted status page | None | Decided 2026-09-25: C: local generated file, plus a market summary with no holdings in the Telegram message |
| P2-D-03 | Price, volume, and flow data provider | A (KRX OPEN API), fallback E (pykrx) | Decided 2026-09-25: C: KIS Developers Open API (Korea Investment & Securities) (differs from the recommendation) |
| P2-D-04 | US-equities data adapter | Deferred | Decide when US coverage activates (DEC-15) |

The Advisor records each founder answer as a P2 decision in this
table, then updates the affected document.

## 4A. Consequences of the founder's answers

The founder answered all 25 open items on 2026-09-25. Three answers
differ from the recommendation or extend it. Their consequences are:

1. **P2-D-01, Telegram channel.** A Telegram channel delivers events
   only while a Claude Code session with the channel is running
   (HFT-P2-07 §2.3, option B). P3 sets up one long-running session for
   the channel. The local desktop hook stays as a supplement. The
   message text passes through Telegram's servers, so rule 2 applies.
2. **P2-D-02, local dashboard plus a Telegram summary.** The dashboard
   stays a locally generated file in a gitignored path (DEC-32). The
   Telegram message can carry a market summary. It never carries
   holdings, positions, sizing, or personal data (DEC-32, R-14). This
   replaces the "pointer only" rule in HFT-P2-07 §2.2 with a
   "no holdings" rule.
3. **P2-D-03, KIS Developers Open API.** This source needs a
   brokerage account, and that account also has order endpoints. The
   design keeps DEC-30 by construction:
   - The price adapter calls only an allow-list of quote and history
     endpoints. P3 writes the allow-list and a test that fails if the
     adapter code names an order or account-transfer endpoint.
   - The app key and secret stay in the gitignored private directory
     (DEC-32). No agent reads them. Only the adapter script uses them.
   - HFT-P2-07 §3.2 marks some KIS facts GAP. P3 checks whether KIS
     gives investor-type flows and short-selling data. If a data type
     is missing, P3 adds pykrx as a supplementary adapter for that data
     type only (DEC-31 allows one adapter per source).
   - The KIS overseas-equity endpoints become the first candidate for
     the US adapter (P2-D-04, still deferred; DEC-15).
4. **P2-S-02, rename in P3.** P3 names the hedge-fund values for
   `qa.level` and `modes.review_mode` before it builds their readers.
   The rename adds upstream-merge work (R-08). P3 records the old-to-new
   value map in the config schema.

## 5. Approval receipt

The founder approves the package after every Open item in Section 4
has an answer. The Advisor fills this form from the founder's recorded
approval. It follows the receipt fields in HFT-P2-03 §4.3.

| Field | Value |
|---|---|
| ID | AR-P2-0001 |
| Decision type | Change to final status (DEC-36) |
| Target | `docs/hedge-fund-transition/p2/` (HFT-P2-00 to HFT-P2-07) |
| Content hash | The commit hash of the approved package (to be filled) |
| CRO verdict reference | Not applicable: the package holds no control decision that takes effect now. The limit values stay for the cro to draft after P6 (DEC-19). |
| Approver | The founder (to be filled) |
| Date and time | To be filled |
| Scope | Approval of the P2 design package. It lets Phase P3 start (PLAN.md §8). |
| Notes | To be filled |

## 6. Traceability

| P2 task (PLAN.md §8) | Covered in |
|---|---|
| 1. Finalize the wave roster | HFT-P2-01 §3 |
| 2. Draft the lifecycle catalog | HFT-P2-02; `workflow-catalog.draft.yaml` |
| 3. Finalize the control model | HFT-P2-03 §1 to §5 |
| 4. Draft the config schema, including DEC-36 | HFT-P2-04; `project.draft.yaml` |
| 5. Set the skill build priority | HFT-P2-05 |
| 6. Build the term map | HFT-P2-06 |
| 7. Select the notification channel | HFT-P2-07 §2 (P2-D-01) |
| 8. Select the price data provider | HFT-P2-07 §3 (P2-D-03) |
| 9. Map W2 and W3 model tiers | HFT-P2-01 §4 |
| 10. Design the investment committee | HFT-P2-03 §6 |
| 11. Present the package | This document |
