# Design Addendum 01 — Mission Reset after Founder Rounds 1-3

| Field | Value |
|---|---|
| Document ID | HFT-ADD-001 |
| Date | 2026-09-24 |
| Status | Frozen record of Advisor decisions |
| Inputs | DEC-01 to DEC-16 in `../QUESTIONS.md` |
| Writing standard | ASD-STE100 writing rules |

## 1. Decisions that drive this addendum

| DEC | Question | Answer | Design effect |
|---|---|---|---|
| DEC-01 | Q01 use | C: whole-firm operating system | DEC-09 and DEC-13 narrow the first build to investment information. The full scope stays in the design. |
| DEC-02 | Q02 people and agents | D: founder plus agents, then copilot after hiring | Agents support one user now. Human-required roles apply when the fund registers. |
| DEC-03 | Q03 founder role | B: CEO and CIO | The user is the only decision maker for investment and firm matters. |
| DEC-04 | Q04 repository | B: new repository with CCGS as upstream | Unchanged. |
| DEC-05 | Q05 archetype | A: single-manager fundamental | Quant agents stay CONDITIONAL on Q25. Research depth is the core function. |
| DEC-06 | Q06 strategy | B: long-biased | Downside defence (bear-market stress, net exposure) is a required risk output. |
| DEC-07 | Q07 jurisdiction | B: Korea first, Cayman later | Jurisdiction config is a list. |
| DEC-08 | Q08 investors | A + D: domestic HNWI, seed/anchor | Relevant when the fund activates (wave W2). |
| DEC-09 | Q09 scale | D + mission reset | See section 2. |
| DEC-10 | Q10 control lines | A: CRO and CCO report to the CEO | The cro agent reports to the user. Its verdicts stay non-overridable by other agents. Revisit before external money arrives. |
| DEC-11 | Q11 front office | A: sector analysts | research-analyst runs as one instance per sector cluster. |
| DEC-12 | Q12 governance | A: founder sole control | Key-person clause and succession plan stay on the document list. |
| DEC-13 | Q37 non-investment scope | A: investment information first | Wave W1 is the information core. Regulatory-limit checks are part of risk information. Operations, IR, regulatory reporting, and setup documents activate in wave W2. |
| DEC-14 | Q38 delivery | A: briefings, reports, Q&A, alerts | Daily briefing, weekly report, on-demand Q&A, and event alerts. |
| DEC-15 | Q39 coverage | A, and prepare for US equities | Korean listed equities at stock level; macro and global indicators for market analysis. Coverage, data sources, and sector taxonomy are config data, so US equities can join later. |
| DEC-16 | Q40 conclusion method | A: bull and bear cases, then CIO synthesis | Every stock call and every house-view change has a bull case, a bear case, and a CIO synthesis with a confidence level. The user decides. |

## 2. Mission

The agent organization gives the founder, one user, all the investment
information that a hedge-fund organization produces. The information
areas are research, investment direction (house view), risk, stock
picking, and market analysis (DEC-09).

Rules:

- The user makes every investment decision. Agents give information,
  analysis, and recommendations with a confidence level. Agents do not
  send orders (Q26 default, design-spec §3).
- Every number carries a source and an as-of date (AAA-04).
- Every stock call and every house-view change goes through the bull,
  bear, and synthesis process (DEC-16).
- The output is for the user's own decisions. It is not advice to third
  parties.

## 3. Activation waves (replace "activation stage" in the roster)

| Wave | Trigger | Content |
|---|---|---|
| W1 information core | Now | The agents and skills that produce investment information for the user. |
| W2 fund operation | The founder starts fund setup (setup stage S1) | Non-investment functions: compliance, operations, NAV check, IR, regulatory reporting, setup documents. Human-required roles apply from registration. |
| W3 institutional | Growth stage 2 or 3 (HF-REF-08 표 6-2) | Dedicated teams and governance roles. |

## 4. Roster changes

New agents (W1):

| Agent | Tier | Supports | Reports to | Function | CCGS donor skeleton |
|---|---|---|---|---|---|
| chief-of-staff | 1 | The user (CEO and CIO) | user | Compiles the daily briefing and the weekly report. Routes on-demand questions and event alerts. Keeps the information register and checks sources and as-of dates. Replaces ceo-office in W1. | producer (coordination, milestone tracking) |
| market-strategist | 2 | Market analysis | cio | Macro, rates, FX, flows, global markets, and the KOSPI/KOSDAQ regime. Writes the base case for the house view. | systems-designer (Formula Output Format for indicators) |
| red-team-analyst | 3 | Bear case and thesis attack | cio | Writes the bear case for every stock call and every house-view change. Cannot be the author of the bull case it attacks. | design-review (adversarial reviewer brief) |
| idea-screener | 3 | Idea generation | head-of-research | Runs valuation, earnings, and event screens on the coverage universe. Feeds the sector analysts. | balance-check (outlier detection) |
| data-steward | 3 | Data sources and freshness | chief-of-staff | Keeps the source registry, data adapters (OpenDART now; US sources later), as-of dates, and the coverage config. | economy-designer (canonical registry) |

Moved to W1: head-of-research (lead of the sector analysts, DEC-11).

Changed in W1:

- cio: runs the bull/bear/synthesis process and writes the synthesis with a confidence level. It never decides for the user.
- cro: gives risk information to the user: exposure, concentration, liquidity, bear-market stress for the long-biased book (DEC-06), and regulatory limits (leverage 400% of NAV, short-selling rules) as information (DEC-13).
- portfolio-manager: turns approved calls into a model portfolio view and sizing proposals.
- research-analyst: one instance per sector cluster; writes the bull case and the full research note.
- trader: gives execution information only: liquidity, market impact, trading cost including the 0.20% securities transaction tax (HF-REF-06 §4.6).

Moved to W2: cco, coo, fund-operations-lead, investor-relations, compliance-analyst, regulatory-reporting-specialist, operations-analyst, fund-accountant, legal-counsel-liaison, technology-lead, security-officer.

Moved to W3: head-of-trading, investor-relations-lead, investor-communications-writer, risk-analyst, risk-analytics-lead, governance-secretary.

Not applicable after DEC-05 and DEC-06: macro-economist (macro archetype), pod-lead and capital-allocation-support (multi-manager), valuation-analyst (Q06 = C only). They stay in the table as "not applicable" rows.

Still CONDITIONAL on Q25 = C or D: quant-research-lead, model-governance-lead, quant-researcher, data-engineer.

Counts:

- W1: 11 agent definitions: chief-of-staff, cio, cro, head-of-research, market-strategist, portfolio-manager, research-analyst, idea-screener, red-team-analyst, data-steward, trader. research-analyst runs as one instance per sector cluster.
- W2: 11 more, 22 in total.
- W3: 6 more, 28 in total.
- Conditional: 0 to 4 more (Q25 = C or D).

## 5. Default sector clusters (config data, change without code)

INFERENCE, for the founder to confirm in a later round:

1. IT, semiconductors, electronics
2. Batteries, autos, industrials
3. Financials
4. Healthcare and biotech
5. Consumer, retail, media, entertainment
6. Materials, energy, utilities

The taxonomy maps to KRX sectors now and to GICS when US equities join (DEC-15).

## 6. Information products (W1 skills)

| Skill | Owner agent | Output | Cadence (DEC-14) |
|---|---|---|---|
| /daily-briefing | chief-of-staff | Market, portfolio, risk, and watch-list events on one page | Each trading day |
| /weekly-report | chief-of-staff | House view, sector reviews, pick-list changes, risk review | Weekly |
| /ask | chief-of-staff | Routed answer from the right agent, with sources | On demand |
| /event-alert | data-steward | Disclosure, price-move, and limit-proximity alerts | On event |
| /house-view | market-strategist + red-team-analyst + cio | Market direction with bull, bear, and synthesis | Weekly, and on regime change |
| /stock-pitch | research-analyst | Bull case and full research note for one stock | On idea |
| /red-team-review | red-team-analyst | Bear case against one pitch or house view | For every pitch and house-view change |
| /cio-synthesis | cio | Synthesis, confidence level, and open questions for the user | After each red-team review |
| /idea-screen | idea-screener | Ranked candidate list with screen evidence | Weekly |
| /risk-report | cro | Exposure, concentration, liquidity, bear-market stress, regulatory limits | Daily summary, weekly full |
| /portfolio-review | portfolio-manager | Model portfolio view and sizing proposals | Weekly |
| /call-review | cio + chief-of-staff | Track record of past calls against outcomes | Monthly |
| /coverage-config | data-steward | Coverage universe, sector clusters, data sources | On change |
| /refresh-facts | data-steward | Re-verification of medium and high volatility values | Quarterly |

The CCGS donors stay as in `../TRANSPLANT-MANIFEST.md`: design-system (section cycle) for /stock-pitch, design-review (adversarial review) for /red-team-review, team-* skeleton for the bull/bear/synthesis sequence, post-mortem and playtest-report for /call-review, consistency-check for the fact registry.

## 7. Questions that change after the mission reset

The following later questions keep their IDs, but their options change to match the mission. Record the change in `../QUESTIONS.md` before asking.

| Question | Change |
|---|---|
| Q17 lifecycle | Add the information-core cadence (daily, weekly, monthly cycles) to the single stage axis. |
| Q19 memo depth | Applies to /stock-pitch. |
| Q20 validation | Becomes "how to judge the quality of calls": tracked recommendations against outcomes. |
| Q22 skill bundles | Options become the W1 information products in section 6. |
| Q23 first milestone | Options become W1 vertical slices, for example one daily briefing plus one stock through bull, bear, and synthesis. |
| Q24 investor-facing tools | Replaced by the delivery surface for the user (repository files, HTML dashboard, chat, notifications). Investor tools move to W2. |

## 8. Risks added

| ID | Risk | Mitigation |
|---|---|---|
| R-13 | Confident but wrong information misleads the single decision maker. | Bull/bear/synthesis for every call; confidence levels; /call-review track record; sources and as-of dates on every number. |
| R-14 | Information for the user is read as investment advice to others. | State in every product that it is for the user's own decisions. Do not distribute products to third parties in W1. |
| R-15 | Data freshness: stale prices or disclosures drive a call. | data-steward checks as-of dates; a product with stale data shows NOT ASSESSED for that part. |

## Erratum 01 (2026-09-24)

Section 4 left ceo-office out of the W2 list. The Advisor keeps ceo-office
in W2, because it supports the fund-setup documents (business plan,
financial model, registration pack). The corrected counts are:

- W1: 11 agent definitions.
- W2: 12 more, 23 in total.
- W3: 6 more, 29 in total.
- Conditional: 0 to 4 more (Q25 = C or D).

The blueprint worker found this gap. The other documents use the
corrected counts.
