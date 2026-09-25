# HFT-P2-00 — Phase P2 Design Package: Index and Approval

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-00 |
| Title | Phase P2 design package: index and approval |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval |
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

The documents raise 28 items. The Advisor resolved 1 item (P2-L-02).
One item waits for a later trigger (P2-D-04). The founder decides the
other 26 items. "Rec." is the recommended option. "None" means the
document gives no recommendation (founder judgment).

| ID | Topic | Rec. | Status |
|---|---|---|---|
| P2-R-01 | Model tier for risk-analyst (W3) | A (Haiku) | Open |
| P2-R-02 | Model tier for governance-secretary (W3) | A (Haiku) | Open |
| P2-R-03 | research-analyst instances: all clusters or on demand | None | Open |
| P2-L-01 | `pre-setup` as a gated stage before S1 | A | Open |
| P2-L-02 | Correct the addendum's "Quarterly" cadence text | A | Resolved by the Advisor (the addendum is a frozen record; DEC-35 governs) |
| P2-L-03 | Replace `/gate-check` reference files with the `gate:` block | B | Open |
| P2-C-01 | Owner of the investment committee minutes | A (chief-of-staff) | Open |
| P2-C-02 | Review depth for the 12 products DEC-20 does not name | A (accept the table) | Open |
| P2-C-03 | Receipt path `production/control/receipts.log`; limits in `config/risk/` | A | Open |
| P2-C-04 | When to fix the missing fail tier in one CCGS vocabulary | A (P4 task 1) | Open |
| P2-S-01 | How `modes.automation` expresses DEC-36 | B (new value `draft_free`) | Open |
| P2-S-02 | Rename the `qa.level` and `modes.review_mode` values | None | Open |
| P2-S-03 | More `strategy` values now | A (`long_biased` only) | Open |
| P2-S-04 | Start value of `modes.rigor` | B (`standard`) | Open |
| P2-B-01 | Build place for four unordered W1 skills | A | Open |
| P2-B-02 | W1 dashboard reuses the 10 UI/UX deferred components | A | Open |
| P2-B-03 | Four investor-facing deferred components wait for W2 | A | Open |
| P2-B-04 | `/call-review` reuses the PROCEED/PIVOT/KILL memo shape | A | Open |
| P2-B-05 | `setup-engine` waits for W2 | A | Open |
| P2-T-01 | Korean names for the five new agent roles | None | Open |
| P2-T-02 | Korean form of the CRO title in products | C | Open |
| P2-T-03 | Korean term for "pre-screen" | None | Open |
| P2-T-04 | Use 일반 사모펀드 as the only current fund-type term | A | Open |
| P2-D-01 | Notification channel | C (scheduled Routine push or email, pointer only) | Open |
| P2-D-02 | Dashboard: local file only, or also a hosted status page | None | Open |
| P2-D-03 | Price, volume, and flow data provider | A (KRX OPEN API), fallback E (pykrx) | Open |
| P2-D-04 | US-equities data adapter | Deferred | Decide when US coverage activates (DEC-15) |

The Advisor records each founder answer as a P2 decision in this
table, then updates the affected document.

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
