# HFT-PLAN-001 — Hedge Fund Transition Master Plan

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-PLAN-001 |
| Title | Hedge Fund Transition — Master Plan |
| Version | 0.7 |
| Date | 2026-09-24 |
| Status | Draft for founder review |
| Owner | Advisor (main session) |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules. Checked manually in v0.1; the STE lint helper is a P3 deliverable. |
| Working files | The names design-spec, question-spec, wf1.json, assess-compact.md, orgmap.json, verifier-issues.md, review.txt, and mapping.txt refer to files in [`evidence/`](evidence/README.md). |

**Change history**

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-24 | Initial draft. |
| 0.2 | 2026-09-24 | Added the mission reset (DEC-09) and decisions DEC-13 to DEC-16, from [design-addendum-01.md](evidence/design-addendum-01.md). Replaced the stage-based organization counts in Section 6 with the wave counts (W1 11, W2 22, W3 28, plus 0-4 conditional). Rewrote Phases P2, P5, P6, P7, and P8 in Section 8 for the wave roster and the information products. Recorded round R3+ (Q37-Q40) in Section 9; rounds 1-3 and R3+ are done, 16 decisions. Added risks R-13 to R-15. Updated Section 13 and Appendix A to match. |
| 0.3 | 2026-09-24 | Recorded round 4 (DEC-17 to DEC-20). Replaced the protected-path hook design with agent verdicts plus recorded user approval (DEC-17). Updated P-03, P-04, P-07, Phase P4, risks R-03, R-06, R-07, and the glossary. |
| 0.4 | 2026-09-24 | Recorded round 5 (DEC-21 to DEC-24). Applied Erratum 01 to the wave counts (W2 23 total, W3 29 total). |
| 0.5 | 2026-09-24 | Recorded round 6 (DEC-25 to DEC-28). |
| 0.6 | 2026-09-24 | Recorded round 7 (DEC-29 to DEC-32). Q35 and Q36 are not asked (Q25 = B). |
| 0.7 | 2026-09-24 | Recorded round 8 (DEC-33 to DEC-36). Changed risk R-02 for manual fact refresh (DEC-35). Changed risk R-07 to match DEC-32 (no information-grade scheme in W1). Corrected the decision count above Table 6.0-1. |

This document is not legal advice. It is not tax advice. It is not investment
advice. Section 3 states this rule in full.

## 2. Purpose

This plan sets the steps to change Claude Code Game Studios (CCGS) into an
agent organization for a Korean hedge fund management company. The Korean
legal term is 일반 사모집합투자업자 (a general private-fund manager). It uses
transition Strategy C: transplant only the operating foundation (hooks,
config resolution, session state, gate mechanics, skill testing). Strategy C
also writes every fund-domain agent and skill fresh. The plan turns the
founder's answers to 40 questions (QUESTIONS.md) into a phased work plan, a
schedule, and a risk register. It cites every claim to a fact (Section 5), a
report chunk (HF-REF-NN), or a marked INFERENCE or GAP.

## 3. Scope

### 3.1 In scope

- The 10-phase work plan, P0 through P9 (Section 8).
- The founder decision process, 10 rounds and 40 questions (Section 9).
- A summary of the target organization, lifecycle, and control model
  (Section 6). Full detail is in ORG-BLUEPRINT.md.
- The verification strategy for each phase (Section 10).
- The schedule, effort estimate, and risk register (Sections 11 and 12).

### 3.2 Out of scope

- The legal filing and registration process itself. A law firm and the
  Financial Supervisory Service must review every filing.
- Tax filings and tax structuring. An accounting firm must review these.
- Real investment decisions, order execution, and investor solicitation.
- Marketing material and investor communication content.

**This plan does not give legal advice. It does not give tax advice. It does
not give investment advice.** The source report carries the same rule
(HF-REF-00, front matter notice). Before the founder files any document with
a regulator, the founder must get advice from a law firm and an accounting
firm. Section 12, risk R-12, lists the gaps that need outside counsel.

## 4. References

### 4.1 Review files

| File | Content |
|---|---|
| `docs/org-migration-review/README.md` | The T1/T2 reuse-rate review summary. |
| `docs/org-migration-review/index.html` | The full review report, with charts and the component mapping table. |

The working files below built this plan. They are in `evidence/`; see
`evidence/README.md`. Do not edit them. They are a frozen record of the
analysis.

| File | Content |
|---|---|
| [`evidence/design-spec.md`](evidence/design-spec.md) | The Advisor's design decisions (F-01 to F-16, SB-01 to SB-28, the org roster, the lifecycle, the control model, the skill catalog, phases P0 to P9, the AAA bar, the risk list). |
| [`evidence/question-spec.md`](evidence/question-spec.md) | The original specification of 36 founder questions in 9 rounds. `QUESTIONS.md` now holds 40 questions in 10 rounds. |
| [`evidence/wf1.json`](evidence/wf1.json) | The raw assessment result: 6 area assessments plus the org blueprint (`orgmap`), each independently verified. |
| [`evidence/assess-compact.md`](evidence/assess-compact.md) | A readable digest of `wf1.json`. |
| [`evidence/orgmap.json`](evidence/orgmap.json) | The org blueprint raw result. |
| [`evidence/verifier-issues.md`](evidence/verifier-issues.md) | The verifier's corrections, applied in this document set. |
| [`evidence/review.txt`](evidence/review.txt), [`evidence/mapping.txt`](evidence/mapping.txt) | The prior T1/T2 review's working notes and component mapping table. |

### 4.2 Report chunk index

Read `docs/hedge-fund-setup/ref/README.md` first. It lists 21 reference
chunks, HF-REF-00 to HF-REF-20, split from `hedge_fund_setup_report.md`. Cite
a chunk as `HF-REF-NN §x.y` or `HF-REF-NN 표 x-y`. The chunk set passed a
byte-exact reassembly check (source bytes 116,964; reassembled bytes
116,964; sha256 `73dcac968ef8db58db0e2364625ee85bf24ff2ba2547297d5a4ba1f55ec7dc5a`
on both sides; exit code 0).

### 4.3 Companion documents

All companion documents live in `docs/hedge-fund-transition/`, next to this
plan.

| File | Content |
|---|---|
| `README.md` | The entry point for the founder. |
| `PLAN.md` | This document. |
| `ORG-BLUEPRINT.md` | The target organization: roster, tiers, delegation rules, lifecycle, and control model, in full. |
| `TRANSPLANT-MANIFEST.md` | The component-by-component transplant list (TAKE, TAKE-MODIFY, CONDITIONAL, LEAVE). |
| `AAA-QUALITY-BAR.md` | The AAA quality bar and the grading rule. |
| `QUESTIONS.md` | The 40 founder questions (10 rounds) and the decision log (DEC-NN). |

## 5. Facts baseline

This section verifies every fact below. Table cells give the short fact.
Full wording is in `design-spec.md`.

| ID | Fact | Evidence |
|---|---|---|
| F-01 | The prior review's T2 target (a knowledge-service org, for example an agency or a consulting firm) reuses 41.4% of components by count (96/232) and 32.4% by lines. The review recommends Strategy C. Its estimate is 253-703 hours. | `docs/org-migration-review/README.md`, `index.html` |
| F-02 | A hedge fund is not the review's T2 target. Domain content is close to T2. Governance and process are close to T1. See the verdict table below. | This assessment (`wf1.json`, `assess-compact.md`) |
| F-03 | CCGS gates are advisory only. No hook or skill blocks a failing gate today. | `.claude/docs/workflow-catalog.yaml:16-18`; `.claude/docs/effects-map.md:1230-1245`; `director-gates.md:127-135` |
| F-04 | The default `review_mode` is `lean`. Lean mode skips per-skill gates. | `.claude/docs/director-gates.md:75` |
| F-05 | The default `team.size` is `individual`. It folds non-core agents into the nearest core agent. | `.claude/skills/team-combat/SKILL.md:40-44` (same pattern in every `team-*` skill) |
| F-06 | The `/gate-check` panel shows 1 to 4 directors. The count scales with `modes.workflow`. | `.claude/skills/gate-check/SKILL.md:385-400` |
| F-07 | The 28 director-gate files use 9 different verdict vocabularies. `director-gates.md` claims only 3. AD-CONCEPT-VISUAL has no blocking tier. | `director-gates.md:123-135` |
| F-08 | Three harness-enforced mechanisms exist today: (a) a PreToolUse hook can refuse a tool call; (b) a `tools: Agent(...)` allow-list; (c) a `settings.json` deny rule. Every other rule is prose only. | `.claude/hooks/validate-commit.sh:145`; `godot-specialist.md:4`; `unity-specialist.md:4`; `unreal-specialist.md:4` |
| F-09 | A subagent in the same session is not an independent reviewer. It is a pre-screen. A human with an independent reporting line must sign. | design-spec §1 |
| F-10 | The law needs three real people: three full-time investment professionals, a compliance officer (준법감시인) who cannot also do asset management, and qualified officers (지배구조법 제5조). Agents support these roles. Agents never hold them. | 시행령 제271조의2 (HF-REF-05 표 4-1); HF-REF-06 §4.5 |
| F-11 | `project.stage` is one scalar value. `/help` maps it with a fixed 7-row table. Two concurrent tracks (setup and operation) need a new track dimension, plus a `/help` and `/gate-check` change. | `.claude/skills/help/SKILL.md:70-77` |
| F-12 | A skill's `model:` frontmatter field is declared but not applied. An agent's `model:` field is unverified. | `.claude/docs/model-tiers.md:3-21`; `coordination-rules.md` |
| F-13 | The Skill Testing Framework's `catalog.yaml` registers 74 skills and 49 agents, 123 names in total. `quality-rubric.md`, its `CLAUDE.md`, and its `README.md` must change with it, in lockstep. | `CCGS Skill Testing Framework/catalog.yaml`, `quality-rubric.md`, `CLAUDE.md`, `README.md` |
| F-14 | This environment has an OpenDART MCP connection (Korean corporate disclosures). It is one data source option. | Environment MCP configuration |
| F-15 | `UPGRADING.md` lists four upgrade strategies: A (merge), A2 (selective checkout, no shared history), B (cherry-pick), C (manual copy). Keeping foundation file paths identical keeps A2 and B usable from a new repository. Do not confuse `UPGRADING.md` "Strategy C" with the review's Strategy C. | `UPGRADING.md` |
| F-16 | The report chunk set has 21 chunks, HF-REF-00 to HF-REF-20, in `docs/hedge-fund-setup/ref/`. The reassembly check is byte-exact. | `docs/hedge-fund-setup/ref/README.md` |

### F-02 detail: hedge-fund verdict counts (232 components)

| Area | TAKE | TAKE-MODIFY | CONDITIONAL | LEAVE | Total |
|---|---|---|---|---|---|
| Agents | 0 | 6 | 14 | 29 | 49 |
| Skills | 8 | 19 | 27 | 20 | 74 |
| Templates | 6 | 13 | 16 | 11 | 46 |
| Director gates | 0 | 10 | 9 | 9 | 28 |
| Hooks + yaml-helper | 7 | 6 | 1 | 0 | 14 |
| Scripts | 4 | 2 | 0 | 2 | 8 |
| Rules | 3 | 3 | 2 | 5 | 13 |
| **Total** | **28** | **59** | **69** | **76** | **232** |

Unconditional reuse (TAKE + TAKE-MODIFY) is 87/232, 37.5%. The upper bound
(every CONDITIONAL item resolved to take) is 156/232, 67.2%. Compare: T1
(a software product org) reuses 70.3%. T2 (a knowledge-service org) reuses
41.4%.

A hedge fund is not a knowledge-service organization only. Its research and
portfolio work needs expert judgment, close to T2 work. But it also needs
strict process discipline: decision records, traceability, and change
control, close to T1 work.

This assessment found 87 of 232 components take with no change (37.5%),
below the T2 rate. The Q25 decision (code and model
pipeline) resolves most of the 69 conditional items. If every conditional
item resolves to take, the rate rises to 67.2%, above T2 and close to the T1
rate. The hedge-fund reuse rate sits between T1 and T2 because governance
content transplants well, but domain content does not.

## 6. Target state summary

Full detail is in **ORG-BLUEPRINT.md**. This section gives a summary only.

Section 6.1 states the wave roster. It follows the founder's Q09 decision,
DEC-09 (Round 3, done). Section 6.3 states the control model that round 4
decided: agent verdict plus recorded user approval (DEC-17) and fixed
control seats (DEC-18).

### 6.0 Mission and founder decisions

The agent organization gives the founder, one user, all the investment
information that a hedge-fund organization produces (DEC-09). The
information areas are research, investment direction (the house view),
risk, stock picking, and market analysis.

Rules:

- The user makes every investment decision. Agents give information,
  analysis, and recommendations with a confidence level. Agents do not
  send orders.
- Every number carries a source and an as-of date (AAA-04).
- Every stock call and every house-view change goes through the bull
  case, the bear case, and the CIO synthesis (DEC-16).
- The output serves the user's own decisions. It is not advice to a
  third party.

Table 6.0-1 lists the 36 founder decisions that set this plan. Read
[QUESTIONS.md](QUESTIONS.md) for the full question text and every option.
Read [design-addendum-01.md](evidence/design-addendum-01.md) for the
mission reset in full.

**Table 6.0-1. Founder decisions DEC-01 to DEC-36**

| DEC | Question | Answer | Effect |
|---|---|---|---|
| DEC-01 | Q01 purpose | C: a whole-firm operating system | DEC-09 and DEC-13 narrow the first build to investment information. |
| DEC-02 | Q02 people and agents | D: the founder plus agents, then a copilot after hiring | Agents support one user now. Human-required roles apply when the fund registers. |
| DEC-03 | Q03 founder role | B: CEO and CIO | The user is the only decision maker for investment and firm matters. |
| DEC-04 | Q04 repository | B: a new repository with CCGS as the upstream | No change from the original design. |
| DEC-05 | Q05 archetype | A: single-manager fundamental | Quant agents stay conditional on Q25. Research depth is the core function. |
| DEC-06 | Q06 strategy | B: long-biased | The design needs a downside-defense risk output: bear-market stress and net exposure. |
| DEC-07 | Q07 jurisdiction | B: Korea first, Cayman later | The jurisdiction config holds a list. |
| DEC-08 | Q08 investors | A and D: domestic HNWI, then a seed or anchor investor | This decision applies when the fund activates, in wave W2. |
| DEC-09 | Q09 scale, plus the mission reset | D, plus the mission reset | See the mission above. |
| DEC-10 | Q10 control lines | A: the CRO and the CCO report to the CEO | The cro agent reports to the user. Its verdicts stay non-overridable by other agents. Revisit this line before outside money arrives. |
| DEC-11 | Q11 front office | A: sector analysts | The research-analyst agent runs as one instance per sector cluster. |
| DEC-12 | Q12 governance | A: the founder holds sole control | The key-person clause and the succession plan stay on the document list. |
| DEC-13 | Q37 non-investment scope | A: investment information first | Wave W1 is the information core. Operations, IR, regulatory reporting, and setup documents activate in wave W2. |
| DEC-14 | Q38 delivery | A: briefings, reports, on-demand answers, and alerts | The daily briefing, the weekly report, on-demand answers, and event alerts make up the W1 products. |
| DEC-15 | Q39 coverage | A, plus preparation for US equities | Korean listed equities at stock level; macro and global indicators for market analysis. US equities can join later. |
| DEC-16 | Q40 conclusion method | A: the bull case, the bear case, then the CIO synthesis | Every stock call and every house-view change carries a bull case, a bear case, and a synthesis with a confidence level. |
| DEC-17 | Q13 blocking method | B: agent verdict plus user approval | No protected-path hook. A control decision needs the cro verdict and a recorded user approval. A decision without a receipt reads NOT ASSESSED. Revisit before real capital. |
| DEC-18 | Q14 control seats | A: never skipped | The cro (W1) and the cco (W2) join every gate and every cio synthesis, whatever the mode settings. |
| DEC-19 | Q15 initial limits | B: cro drafts, founder approves | The cro drafts loss and exposure limits for the long-biased book. The founder approves. Limits live in config files. |
| DEC-20 | Q16 review depth | D: by output type | Judgment outputs (stock calls, house view, limits) use full review. Routine outputs (daily briefing) use lean review. |
| DEC-21 | Q17 lifecycle | A: stage axis plus information cycles | S1-S8 and G1-G3 serve the fund. W1 runs on daily, weekly, and monthly cycles. `project.stage` stays one scalar. |
| DEC-22 | Q18 decision body | B: virtual investment committee plus minutes | cio, cro, portfolio-manager, and red-team-analyst present. The user decides. Minutes are kept. |
| DEC-23 | Q19 stock-pitch depth | A: full format, 8 sections | /stock-pitch has 8 sections plus the bull, bear, and synthesis parts. P5 measures the time per stock. |
| DEC-24 | Q20 call quality | C: call record plus model portfolio | /call-review tracks every call against its outcome. A model portfolio runs against a benchmark. |
| DEC-25 | Q21 principles | B + C + D: documented principles, research-centred collective management, capacity control | Decision records and open dissent come first. Research quality is the centre of the organization. W1 products carry capacity estimates. Numeric limits stay as config values (DEC-19). |
| DEC-26 | Q22 first products | A + B: market information and stock information | Build /daily-briefing, /house-view, /event-alert, /idea-screen, /stock-pitch, /red-team-review, and /cio-synthesis first. Then risk, portfolio, and quality products. |
| DEC-27 | Q23 first milestone | C: briefing plus one-stock vertical slice | One daily briefing, and one stock through screen, pitch, red team, synthesis, and the virtual investment committee. |
| DEC-28 | Q24 delivery surface | D: dashboard plus notification channel | An HTML dashboard and a notification channel. P2 selects the channel from the tools that the new repository's environment can reach. |
| DEC-29 | Q25 code pipeline | B: analysis code | Data collection, screens, valuation and stress calculations, and model-portfolio tracking run as versioned, tested scripts. No model-governance skills. The four quant conditional agents stay off. Q35 and Q36 are not asked. |
| DEC-30 | Q26 agent authority | B: analysis plus model-portfolio records | Agents read, analyze, write, and record hypothetical model-portfolio positions. Agents do not draft or send orders. |
| DEC-31 | Q27 data sources | A + C + D: OpenDART, exchange/broker data, web search | OpenDART for disclosures and financials; exchange or broker data for prices, volume, and flows; web search for regulation, news, and macro. P2 selects the price provider. Data adapters stay per source for the US extension. |
| DEC-32 | Q28 confidential data | B: gitignored local directory | Holdings and personal data stay in a gitignored local directory. No classification scheme in W1. Revisit with legal review before W2 (MNPI GAP). |
| DEC-33 | Q29 document language | A: STE English for technical documents; Korean for information products and external documents | Agents, skills, rules, and procedures use ASD-STE100 English. Briefings, reports, answers, alerts, the dashboard, and regulatory and investor documents use Korean. Responses to the user use Korean. AAA-12 applies the STE checks or the Korean style checks by document language. |
| DEC-34 | Q30 AAA scope | A: all criteria, only AAA ships | AAA-01 to AAA-14 apply to every agent, skill, gate, template, and document. A component with a grade below AAA does not ship. |
| DEC-35 | Q31 fact freshness | D: manual | No fixed re-verification schedule. `/refresh-facts` runs only on the founder's request. Every value still shows its source and `as_of` date (AAA-04). Risk R-02 goes up. |
| DEC-36 | Q32 approval scope | B: free drafts, approval before final status or a commit | Agents write drafts with no approval prompt. A change to final status and every commit need a founder approval. No CCGS `modes.automation` value matches exactly (`.claude/docs/automation-modes.md`:66-94); P2 extends `guided` or adds a value. Control decisions still follow DEC-17. |

### 6.1 Organization

The roster now activates in waves, not stages (DEC-09; addendum §3). A
wave activates on a trigger, not on a calendar date.

| Wave | Trigger | Content | Agent count |
|---|---|---|---|
| W1 information core | Now | The agents and skills that produce investment information for the user. | 11 |
| W2 fund operation | The founder starts fund setup (setup stage S1) | Non-investment functions: compliance, operations, NAV check, IR, regulatory reporting, setup documents. | 23 total |
| W3 institutional | Growth stage 2 or 3 (HF-REF-08 표 6-2) | Dedicated teams and governance roles. | 29 total |
| Conditional | Q25 = C or D | Quant-research and model-governance agents. | 0-4 more |

Wave W1 runs on daily, weekly, and monthly information cycles: a daily
briefing, a weekly report, and a monthly call-review, among other
products (Section 6.0; Section 8, Phase P6).

The roster follows HF-REF-08 표 6-1 (functions) and 표 6-2 (growth-stage
activation) for the W2 and W3 content. The cro (risk officer support)
reports to the user, who is the CEO and the CIO (DEC-03, DEC-10). The cco
(준법감시인, compliance officer, support) joins in W2. Revisit these
reporting lines before external money arrives (HF-REF-08 §6.2). Counts are
design estimates. They are not a fixed headcount. See Section 7, P-07,
"Design the full organization, build wave W1 first," for the build order.

### 6.2 Lifecycle design

One stage axis carries the whole lifecycle. It has two parts.

**Setup, S1 to S8** (HF-REF-05 표 4-2):

| ID | Korean | English gloss |
|---|---|---|
| S1 | 사업 설계 | Business design |
| S2 | 법인 설립 | Company incorporation |
| S3 | 인력·규정 | Staffing and rules |
| S4 | 전산·설비 | Systems and facilities |
| S5 | 사전 협의 | Pre-consultation |
| S6 | 등록 신청·심사 | Registration application and review |
| S7 | 협회 가입·인력 등록 | Association membership and staff registration |
| S8 | 첫 펀드 설정 | First fund launch |

**Growth, G1 to G3** (HF-REF-08 표 6-2). G1 to G3 match the three
organization stages in Section 6.1.

The investment cycle (HF-REF-09 §7.1: idea, analysis, portfolio, pre-check,
execution, monitoring, post-review) is a repeatable per-idea process. It is
not a stage. It runs like a story inside a stage. This keeps `project.stage`
a single scalar value (F-11). `/help` and `/gate-check` need a table change
only, not a new track dimension.

### 6.3 Control model

- **Verdict vocabulary**: PASS, CONCERNS, FAIL, NOT ASSESSED. Precedence:
  FAIL beats CONCERNS. CONCERNS beats NOT ASSESSED. NOT ASSESSED beats PASS.
- **Fixed control seats (DEC-18)**: the cro (from W1) and the cco (from
  W2) stay active in every gate and in every cio synthesis.
  `modes.workflow`, `modes.review_mode`, and `team.size` do not remove them.
- **Approval enforcement (DEC-17)**: a control decision needs the cro
  verdict and a recorded approval by the user (an approval receipt). The
  design does not build a protected-path hook. A prose gate cannot block a
  tool call (F-03), so the receipt is the control. A control decision
  without a receipt reads NOT ASSESSED. Revisit hook enforcement before
  real capital (R-03).
- **Registry**: a regulatory value registry stores each limit with an
  `as_of` date and an effective date.
- **Pre-screen rule**: label every agent review a pre-screen (F-09). A human
  with an independent reporting line must sign before a control record is
  final.

## 7. Transition principles (P-01 to P-10)

| ID | Principle |
|---|---|
| P-01 | Facts first |
| P-02 | Humans hold legal roles |
| P-03 | Control independence |
| P-04 | Allow-lists and recorded approvals (DEC-17) |
| P-05 | Data-driven limits |
| P-06 | Keep foundation file paths for upstream updates |
| P-07 | Design the full organization, build wave W1 first |
| P-08 | Test first |
| P-09 | One verdict vocabulary |
| P-10 | Language policy |

**P-01 Facts first.** State every claim as a fact with a citation. Mark an
unverified claim INFERENCE. Mark a missing input GAP. Do not state a
regulatory or a market value without a source and an `as_of` date (AAA-04).
This document follows the same rule; see Section 5.

**P-02 Humans hold legal roles.** The law needs three full-time investment
professionals, a compliance officer, and qualified officers (F-10). Agents
support these roles. Agents never hold them. No document in this transition
may assign a legal role to an agent.

**P-03 Control independence.** No agent may override, edit, or suppress a
cro or a cco verdict. Only the user may accept a documented exception. The
cro reports to the user (DEC-10). Revisit the reporting line before external
money arrives (HF-REF-08 §6.2).

**P-04 Allow-lists and recorded approvals (DEC-17).** Today's gates are
advisory. A prose instruction does not block a tool call (F-03, F-08). The
founder chose agent verdicts plus a recorded user approval for control
decisions. Use `tools: Agent(...)` allow-lists so a front-office agent
cannot spawn or edit a control agent. Record every control approval as a
receipt. Revisit hook enforcement before real capital (R-03).

**P-05 Data-driven limits.** Store every loss limit, exposure limit, and
leverage limit in a config file, never in code or in a skill's prose
(`coding-standards.md`). This lets the founder and the cro change a limit
without a text edit to a skill file.

**P-06 Keep foundation file paths for upstream updates.** Keep the same
file paths as CCGS for hooks, scripts, and config resolution (F-15). This
keeps `UPGRADING.md` strategy A2 and strategy B usable for upstream security
and bug fixes.

**P-07 Design the full organization, build wave W1 first.** Design the
full organization (W1, W2, W3) now. Build only the W1 information core
first. This meets the
"best organization" goal through the design. It also caps the organization
at the size the founder needs, and no more (risk R-06).

**P-08 Test first.** Write a test for every silent break, SB-01 to SB-28,
before Phase P6 starts (Section 10). Write a failing-gate test for every
new control gate and allow-list: break the guarded thing, confirm the check fails, then restore it
(AAA-09).

**P-09 One verdict vocabulary.** Use PASS, CONCERNS, FAIL, NOT ASSESSED
everywhere. Today's 28 gate files use 9 different vocabularies (F-07). A
missing input must never read as PASS. It must read as NOT ASSESSED.

**P-10 Language policy.** Write technical documents (agents, skills, rules,
procedures) in ASD-STE100 English. Write regulatory filings and investor
documents in Korean. Give a short English gloss after a Korean term the
first time it appears.

## 8. Work breakdown

This section lists tasks and gating questions per phase. Gating-question
lists are the Advisor's synthesis from each question's stated impact field
in `question-spec.md` and from each phase's entry criteria in
`design-spec.md` §7. They are not a verbatim source table; treat them as
INFERENCE.

### P0 — Baseline and reference prep

**Status: DONE in this change.**

Delivered:

1. 21 reference chunks, HF-REF-00 to HF-REF-20, in
   `docs/hedge-fund-setup/ref/`, with a byte-exact lossless reassembly
   check (sha256 match on both sides, exit code 0).
2. The chunk-to-source-line map, `docs/hedge-fund-setup/ref/manifest.json`
   and the chunk table in `docs/hedge-fund-setup/ref/README.md`.
3. Assessments across 6 areas (infra, skills-mgmt, skills-pipeline,
   skills-design, agents-gates, content-qa), each independently verified,
   plus the org blueprint, independently verified.
4. This document set: `README.md`, `PLAN.md`, `ORG-BLUEPRINT.md`,
   `TRANSPLANT-MANIFEST.md`, `AAA-QUALITY-BAR.md`, `QUESTIONS.md`, in
   `docs/hedge-fund-transition/`.

Exit criteria (met): every output above exists; the reassembly check
returns exit code 0; every area assessment carries a verifier pass.

### P1 — Founder decisions

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P0 done; `QUESTIONS.md` holds 40 questions in 10 rounds | Every question Q01-Q34 and Q37-Q40 (and Q35-Q36 if triggered) has one DEC-NN entry | 4-8 h (plus 2-4 h founder time) | Advisor + Founder |

Tasks:

1. Read `design-spec.md` and `question-spec.md` rules before round 1.
2. Ask the founder round 1 (Q01-Q04).
3. Record each answer as DEC-01 to DEC-04 in `QUESTIONS.md`.
4. Repeat steps 2-3 for rounds 2 through 9, in order.
5. Add Q35 and Q36 to round 9 only if the Q25 answer is C or D.
6. Close each round once every question in it has a DEC-NN entry.

Outputs: `QUESTIONS.md` (answered register with DEC-NN entries); a term map
of new `project.yaml` keys named by the founder's answers.

Gating questions: none. This phase produces the answers other phases need.

### P2 — Target design

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P1 complete, all DEC-NN recorded | The founder approves the design package in writing (an approval receipt) | 12-30 h | Advisor |

The design package uses [design-addendum-01.md](evidence/design-addendum-01.md)
for the mission (DEC-09) and the wave roster (W1, W2, W3).

Tasks:

1. Finalize the wave roster from the addendum and its Erratum 01: W1 (11
   agents), W2 (23 total), W3 (29 total), and the Q25 conditional set
   (0-4 more).
2. Draft the lifecycle catalog (S1-S8, G1-G3) to replace
   `workflow-catalog.yaml`.
3. Finalize the control model: verdict vocabulary, fixed seats, and
   approval-receipt rules (DEC-17).
4. Draft the new `project.yaml` config schema: `archetype`, `jurisdiction`,
   `risk.*`, `regulatory_calendar`, `coverage.*`, `controls.four_eyes`,
   `controls.approval_required_for`.
5. Set the skill build priority from the Q22 and Q23 answers.
6. Build the Korean-English term map for shared documents.
7. Present the design package to the founder for approval.

Outputs: `ORG-BLUEPRINT.md` (updated for the DEC-NN choices);
`TRANSPLANT-MANIFEST.md` draft; a config schema draft; the term map.

Gating questions: Q01, Q02, Q03, Q05-Q12, Q17-Q24, Q29-Q31.

### P3 — Repository bootstrap and foundation transplant

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P2 approved; Q04 answered | The new repository's own transplant set passes a reassembly-style check; SB-01 to SB-28 tests pass for every applicable break | 20-50 h | Worker |

Tasks:

1. Create the new repository per the Q04 answer.
2. Copy the minimum transplant set from `TRANSPLANT-MANIFEST.md`.
3. Fix every silent break, SB-01 to SB-28, that applies to the transplant
   set.
4. Write the new `project.stage` enum and schema in `yaml-helper.sh`.
5. Update `settings.json` (permissions, hooks).
6. Wire `log-instructions.sh` and `statusline.sh` to the new schema.
7. Rewrite `detect-gaps.sh` for the new project shape.
8. Build the ASD-STE100 lint helper as an observation-only script.

Outputs: the new repository; `.claude/hooks/*`; `.claude/scripts/*`;
`project.yaml`; `settings.json`; `.claude/scripts/ste-lint.sh`
(observation only, per `.claude/docs/context-management.md`'s rule that a
helper gives observations, never a verdict).

Gating questions: Q04, Q16, Q25, Q27, Q29, Q32, Q34.

### P4 — Control spine

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P3 done | Every failing-gate test fails when its guard is off and passes when its guard is on | 25-60 h | Worker |

Tasks:

1. Write the single verdict vocabulary into every gate file.
2. Fix the cro and the cco seats. Remove their dependence on
   `modes.workflow`, `modes.review_mode`, and `team.size`.
3. Build the approval-receipt format. A control decision without a
   receipt reads NOT ASSESSED (DEC-17). Do not build a protected-path hook.
4. Build the regulatory value registry (`as_of` and effective dates).
5. Rewrite `coordination-rules.md` to add the non-override rule.
6. Set the `tools: Agent(...)` allow-lists so a front-office agent cannot
   spawn or edit the cro, the cco, or their reports.
7. Write a failing-gate test for every control gate and allow-list.

Outputs: `.claude/docs/coordination-rules.md` (revised); the
approval-receipt format; the regulatory value registry file; the adapted
`review-receipts.sh`; agent frontmatter allow-lists;
`tests/integration/control/*`.

Gating questions: Q10, Q13, Q14, Q15, Q25, Q26, Q28, Q35, Q36.

### P5 — Pilot and re-measure

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P4 done | All pilot components reach grade AAA; the re-estimate note exists | 10-25 h | Worker |

Tasks:

1. Build the chief-of-staff agent to the AAA bar.
2. Build the `/daily-briefing` skill to the AAA bar.
3. Run one stock through `/stock-pitch`, `/red-team-review`, and
   `/cio-synthesis`, each to the AAA bar.
4. Run each pilot component through the AAA-QUALITY-BAR.md checks.
5. Log the actual hours spent on tasks 1-4.
6. Re-estimate phases P6 through P9 from the measured hours. This
   plan's P6-P9 hour estimates stay as stated until this re-estimate
   runs.

Outputs: `agents/chief-of-staff.md`; `skills/daily-briefing/SKILL.md`;
`skills/stock-pitch/SKILL.md`; `skills/red-team-review/SKILL.md`;
`skills/cio-synthesis/SKILL.md`; a pilot log; a re-estimate note added
to Section 11 of this document.

Gating questions: Q22, Q23, Q33, Q34.

### P6 — W1 roster and the W1 information products

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P5 re-estimate done | `/skill-test static` returns 0 FAIL for every new skill; `/skill-test category` returns COMPLIANT | 100-300 h | Worker |

Tasks:

1. Build the 11 W1 agents (addendum §4): chief-of-staff, cio, cro,
   head-of-research, market-strategist, portfolio-manager,
   research-analyst, idea-screener, red-team-analyst, data-steward,
   and trader.
2. Build the 14 W1 information-product skills (addendum §6):
   `/daily-briefing`, `/weekly-report`, `/ask`, `/event-alert`,
   `/house-view`, `/stock-pitch`, `/red-team-review`,
   `/cio-synthesis`, `/idea-screen`, `/risk-report`,
   `/portfolio-review`, `/call-review`, `/coverage-config`, and
   `/refresh-facts`.
3. Build the matching templates.
4. Run `/skill-test static` and `/skill-test category` on each new
   skill.

Outputs: `agents/*.md` (the 11-agent W1 roster); `skills/*/SKILL.md`
(the 14 W1 information products); `templates/*`.

Gating questions: Q09, Q11, Q19, Q22.

### P7 — End-to-end dry run

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P6 done for the W1 set | One full week of the information cycle completes with no manual patching; evidence is retained | 10-25 h | Worker + Founder (review) |

Tasks:

1. Run one full week of the information cycle: 5 daily briefings
   through `/daily-briefing` and 1 weekly report through
   `/weekly-report`.
2. Run 1 house view through `/house-view`.
3. Run 2 stock calls through `/stock-pitch`, `/red-team-review`, and
   `/cio-synthesis`.
4. Trigger at least 1 alert through `/event-alert`.
5. Take a screenshot or a log of every step as evidence.
6. Store the evidence in `production/qa/evidence/`.
7. Record the dry run result and any patch it needs.

Outputs: `production/qa/evidence/*` (retained evidence); a dry-run report.

Gating questions: Q17, Q18, Q20, Q23.

### P8 — W2 and W3 activation, plus the conditional pipeline

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P7 passed; the founder starts fund setup (the wave-W2 trigger, addendum §3) | Each new component reaches grade AAA; the model-governance failing-gate test passes if the quant pipeline is built | 60-200 h (conditional on scope) | Worker |

Tasks:

1. Build the remaining wave-W2 agents and skills, once the founder
   starts fund setup (setup stage S1): cco, coo,
   fund-operations-lead, investor-relations, compliance-analyst,
   regulatory-reporting-specialist, operations-analyst,
   fund-accountant, legal-counsel-liaison, technology-lead, and
   security-officer.
2. Build the remaining wave-W3 agents and skills, once the firm
   reaches growth stage 2 or 3: head-of-trading,
   investor-relations-lead, investor-communications-writer,
   risk-analyst, risk-analytics-lead, and governance-secretary.
3. If Q25 is C or D, build the quant research pipeline: `/model-change`,
   `/model-review`, `/backtest-evidence`, and the model governance
   controls.
4. Activate the Q25 conditional agents: quant-research-lead,
   model-governance-lead, quant-researcher, and data-engineer.

Outputs: `agents/*.md` (the W2 and W3 set); `skills/*/SKILL.md` (quant
pipeline, if triggered); `templates/*` (investor-portal set, if Q24 is B).

Gating questions: Q09, Q12, Q24, Q25, Q35, Q36.

### P9 — Documentation, test catalog, handoff

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P6 done (and P8, if built) | `/skill-test audit` finds no orphaned or unregistered component | 20-50 h | Worker |

Tasks:

1. Write the onboarding document for the new organization.
2. Update the Skill Testing Framework registries (`catalog.yaml`,
   `quality-rubric.md`, `CLAUDE.md`, `README.md`) in lockstep.
3. Write a spec for every new skill and agent.
4. Run `/skill-test audit` across the full set.
5. Write the handoff `README.md`.

Outputs: `CCGS Skill Testing Framework/catalog.yaml`; `quality-rubric.md`;
an onboarding document; a handoff `README.md`.

Gating questions: Q29, Q30, Q31.

## 9. Founder decision process

The founder answers 40 questions in 10 rounds, in `QUESTIONS.md`. Round
R3+ is a follow-up round the mission reset added (DEC-09). It holds
Q37-Q40, the questions that confirm the mission reset's scope
([design-addendum-01.md](evidence/design-addendum-01.md) §7). Rounds 1
through 8 and round R3+ are done, with 36 decisions recorded, DEC-01
through DEC-36. Q35 and Q36 are not asked, because Q25 = B (DEC-29).

Rules:

- Give the founder 4 or 5 options per question.
- Give a recommendation with a source, or state
  "권장안 없음(창업자 판단)" (no recommendation, founder's judgment) with the
  reason.
- Record each answer as a DEC-NN entry in `QUESTIONS.md`.
- Ask Q35 and Q36 only if the Q25 answer is C or D.
- The `AskUserQuestion` tool allows 4 options plus an automatic "Other".
  When a question has 5 options, mark which 4 go into the tool, and state
  that the 5th option is available as "Other".

### Round dependency table

This table maps each round to the phases it unblocks. It is the Advisor's
synthesis from the tasks in Section 8; mark it INFERENCE.

| Round | Questions | Phases it unblocks | Status |
|---|---|---|---|
| R1 | Q01-Q04 | P2, P3 | Done |
| R2 | Q05-Q08 | P2, P6 | Done |
| R3 | Q09-Q12 | P2, P4, P6, P8 | Done |
| R3+ | Q37-Q40 | P2, P6, P7 | Done |
| R4 | Q13-Q16 | P3, P4 | Done |
| R5 | Q17-Q20 | P2, P6, P7 | Done |
| R6 | Q21-Q24 | P2, P5, P6, P7, P8 | Done |
| R7 | Q25-Q28 | P3, P4, P8 | Done |
| R8 | Q29-Q32 | P2, P3, P4, P9 | Done |
| R9 | Q33-Q36 | P3, P4, P5, P8 | Next |

## 10. Verification strategy

**AAA-QUALITY-BAR.md** holds the full grading rule. This section maps each
phase to its check.

| Phase | What is verified | How |
|---|---|---|
| P0 | Chunk lossless reassembly; 6 area assessments plus the org blueprint | `split_report.py --check` (exit 0); one verifier pass per area, plus one for the org blueprint |
| P1 | Every question answered | A completeness check of DEC-NN entries against the 38 unconditional (plus 0-2 conditional) question IDs |
| P2 | The design package | A founder approval receipt; the term map checked against Appendix B |
| P3 | Transplant integrity | SB-01 to SB-28 tests, one test per silent break |
| P4 | The control spine | Failing-gate tests: break the guard, confirm the check fails, restore it |
| P5 | The 3 pilot components | `/skill-test` static, spec, and category modes; one independent review receipt per component |
| P6 | The W1 build | `/skill-test static` (0 FAIL) and `/skill-test category` (COMPLIANT) on every new skill; the ASD-STE100 lint helper run on every new document (observation only) |
| P7 | The dry run | The dry run itself: one idea through the full cycle, one setup stage through its gate, evidence retained |
| P8 | Stage-2/3 build and the conditional pipeline | `/skill-test static` and `/skill-test category` on every new component; a model-governance failing-gate test if the quant pipeline is built |
| P9 | Documentation and handoff | `/skill-test audit` across the full catalog; independent review receipts recorded for the document set |

## 11. Schedule and effort

### 11.1 Phase estimates

| Phase | Low (h) | High (h) |
|---|---|---|
| P1 | 4 | 8 |
| P2 | 12 | 30 |
| P3 | 20 | 50 |
| P4 | 25 | 60 |
| P5 | 10 | 25 |
| P6 | 100 | 300 |
| P7 | 10 | 25 |
| P9 | 20 | 50 |
| **Core total (P1-P7, P9)** | **201** | **548** |
| P8 (conditional) | 60 | 200 |
| **Total with P8** | **261** | **748** |
| Review T2 estimate (comparison, F-01) | 253 | 703 |

### 11.2 Conversion method

The hour ranges use the review's own conversion method. Each task in a
phase gets a size label: S, M, or L. An S task needs 0.25 to 0.5 hour. An
M task needs 1 to 3 hours. An L task needs 3 to 8 hours. The phase range
sums the low end and the high end of every task's size label.

### 11.3 Weekly scenarios

Weeks equal hours divided by the weekly rate, rounded to the nearest whole
week.

| Rate | Core (201-548 h) | Core + P8 (261-748 h) |
|---|---|---|
| 10 h/week | 20-55 weeks | 26-75 weeks |
| 20 h/week | 10-27 weeks | 13-37 weeks |
| 30 h/week | 7-18 weeks | 9-25 weeks |
| 40 h/week | 5-14 weeks | 7-19 weeks |

### 11.4 Re-estimate rule

Phase P5 measures the actual hours for the 3 pilot components. Use the
measured rate to re-estimate phases P6 through P9 before Phase P6 starts.
Do not carry the original P6-P9 estimate forward without this check.

## 12. Risk register

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Phase |
|---|---|---|---|---|---|---|
| R-01 | Agents get treated as legal personnel | M | H | Enforce the F-10 role list; check the human-boundary list on every agent (AAA-08) | Founder / cco | P2, P4 |
| R-02 | Regulatory values go stale | H | M | No fixed schedule (DEC-35). The founder runs `/refresh-facts` on request. Every value carries an `as_of` date in the registry, and every product shows it next to the value (AAA-04). Revisit a fixed schedule before wave W2 | Founder; data-steward (W1); cco / compliance-analyst (W2) | P4, P9 |
| R-03 | An advisory gate gets skipped silently | M | H | Fixed control seats (DEC-18); agent verdict plus a recorded user approval (DEC-17); allow-lists (P-04); a control decision without a receipt reads NOT ASSESSED; revisit hook enforcement before real capital | Worker | P4 |
| R-04 | A silent break appears during the transplant | H | M | Run the SB-01 to SB-28 test set before Phase P6 starts | Worker | P3 |
| R-05 | A same-session review gets mistaken for an independent one | M | H | Label every agent review "pre-screen" (F-09); require a human sign-off receipt | Founder | P4, P5 |
| R-06 | Scope grows toward the full 29-agent (W3) organization before it is needed | H | M | Design the full organization, build wave W1 first (P-07); a founder approval gate before each wave activation | Advisor | P2, P6, P8 |
| R-07 | Confidential data or MNPI (undisclosed material information) reaches the repository | M | H | Keep holdings and personal data in a gitignored local directory (DEC-32); add a `settings.json` deny rule for that directory; revisit an information-grade scheme with legal review before wave W2 | cro (W1), cco (W2) | P4 |
| R-08 | Upstream CCGS changes drift away from the transplant | M | M | Keep foundation file paths identical (P-06); use `UPGRADING.md` strategy A2 or B | Worker | P3 |
| R-09 | An agent states a legal or regulatory fact with no source | M | H | Enforce the AAA-04 citation rule; every fact in this plan cites HF-REF-NN or F-NN | Advisor | All phases; checked at P9 |
| R-10 | The agent `model:` tier pin turns out not to work | M | L | Measure whether the `model:` field changes behavior during Phase P3, before the Q34 tier plan is relied on | Worker | P3 |
| R-11 | Two concurrent tracks (setup and operation) do not fit one `project.stage` value | M | M | Keep `project.stage` a single scalar (Q17); change only the `/help` and `/gate-check` tables (F-11) | Worker | P2, P3 |
| R-12 | The source report is not legal, tax, or investment advice; some topics are gaps | H | H | State the disclaimer in Section 3; route each gap to outside counsel before the matching phase closes | Founder | P1 (decision to get counsel); ongoing |
| R-13 | Confident but wrong information misleads the single decision maker | M | H | Run the bull, bear, and synthesis process for every call; state a confidence level; run `/call-review` to track the record; give a source and an as-of date on every number | cio / red-team-analyst | P6, P7 |
| R-14 | Information for the user is read as investment advice to a third party | L | H | State in every product that it is for the user's own decisions; do not distribute products to a third party in wave W1 | chief-of-staff | P6, P9 |
| R-15 | Stale prices or disclosures drive a call | M | M | The data-steward agent checks every as-of date; a product built on stale data shows NOT ASSESSED for that part | data-steward | P6, P7 |

Section 12, risk R-12, lists the gaps that need outside counsel:

- MNPI information-barrier procedure
- personal-trading pre-clearance detail
- cybersecurity roles
- AML/KYC
- BCP (business continuity plan) detail
- vendor due diligence
- valuation committee quorum
- key-person succession
- ESG/stewardship
- investor privacy
- the fee crystallization period
- the model governance procedure

## 13. Next steps

1. Done. The founder read `README.md` and this plan (`PLAN.md`).
2. Done. The founder and the Advisor ran round 1 (Q01-Q04), round 2
   (Q05-Q08), round 3 (Q09-Q12), the follow-up round R3+ (Q37-Q40),
   round 4 (Q13-Q16), round 5 (Q17-Q20), round 6 (Q21-Q24), round 7
   (Q25-Q28), and round 8 (Q29-Q32).
3. Done. The Advisor recorded 36 decisions, DEC-01 through DEC-36, in
   `QUESTIONS.md`.
4. **Next action.** The founder and the Advisor run round 9 (Q33-Q34,
   resources).
5. Q35 and Q36 are not asked, because Q25 = B (DEC-29).
6. The Advisor adds Q35 and Q36 to round 9 only if the Q25 answer is C
   or D.
7. The Advisor drafts the Phase P2 design package from the completed
   decision log.
8. The founder approves the Phase P2 design package with an approval
   receipt.
9. The Worker starts Phase P3 once the founder approves Phase P2.
10. The Advisor schedules the Phase P5 re-estimate check before Phase
    P6 starts.

## Appendix A: Requirements traceability

| ID | Requirement | Satisfied in | Evidence |
|---|---|---|---|
| UR-01 | Build the best hedge-fund organization | Section 6; `ORG-BLUEPRINT.md` | The mission (DEC-09); the wave roster (W1 11, W2 23 total, W3 29 total, plus 0-4 conditional) |
| UR-02 | Use the standard hedge-fund org structure; staff it with AAA-or-better agents | Section 6; Section 10; `AAA-QUALITY-BAR.md` | The mission (DEC-09); the wave roster; the AAA-01 to AAA-14 grading rule; "only AAA may ship" |
| UR-03 | Use transition strategy C (transplant the operating foundation only) | Section 2; Section 3; Section 6; `TRANSPLANT-MANIFEST.md` | F-01, the review's Strategy C recommendation |
| UR-04 | Decide the agents and skills through discussion with the founder | Section 9; `QUESTIONS.md` | 10 rounds, 40 questions, DEC-NN decision log. Status: rounds 1-8 and round R3+ are done (36 decisions). Round 9 is next. |
| UR-05 | Ask the founder detailed questions | Section 9; `QUESTIONS.md` | 40 questions with 질문/왜 묻는가/근거 fields. Status: rounds 1-8 and round R3+ are done (36 decisions); round 9 remains. |
| UR-06 | Give 4-5 options per question | Section 9 rules; `QUESTIONS.md` | Every question has 4 or 5 options ([`evidence/question-spec.md`](evidence/question-spec.md)). |
| UR-07 | Use `hedge_fund_setup_report.md` as the base frame | Section 4.2 | HF-REF-00 to HF-REF-20 chunk index |
| UR-08 | Split the report into optimal chunks | Section 4.2; Section 8, Phase P0 | 21 chunks, byte-exact reassembly check |
| UR-09 | Keep AAA quality or better | Section 10; `AAA-QUALITY-BAR.md` | The bar is defined and testable. The first certification records come from the P5 pilot, because no agent or skill exists yet. |
| UR-10 | Base every claim on facts and verify it | Section 5; Section 7, P-01 | F-01 to F-16, each with a citation |
| UR-11 | Write technical documents in ASD-STE100 | Document header; Section 7, P-10; DEC-33 | Verifiers checked sentence length, voice, and tense by hand in v0.1. The STE lint helper (P3) makes the check repeatable. DEC-33 keeps technical documents in STE English and puts information products and external documents in Korean. |

## Appendix B: Glossary

- **TAKE** — a transplant verdict. Keep the component with no change.
- **TAKE-MODIFY** — a transplant verdict. Keep the component. Change the
  parts the manifest lists.
- **CONDITIONAL** — a transplant verdict. Keep the component only if a
  named founder decision picks the branch that needs it.
- **LEAVE** — a transplant verdict. Do not transplant the component. It is
  game-specific, or a fresh domain version replaces it.
- **HF-REF** — a reference chunk ID from `docs/hedge-fund-setup/ref/`
  (HF-REF-00 to HF-REF-20). Cite as `HF-REF-NN §x.y`.
- **SRC** — a source ID from HF-REF-20 (SRC-01 to SRC-63). It is the
  original public source behind a report fact.
- **SB** — a silent-break ID (SB-01 to SB-28). It names a path or a name
  that breaks a mechanism with no error message.
- **DEC** — a decision-record ID (DEC-01 and up) in `QUESTIONS.md`. It
  records the founder's answer to one question.
- **P-NN** — a transition-principle ID (P-01 to P-10), Section 7.
- **F-NN** — a fact ID (F-01 to F-16), Section 5.
- **pre-screen** — an agent's review of another agent's work, in the same
  session. It is not an independent review. A human with an independent
  reporting line must still sign (F-09).
- **fixed control seat** — the cro or the cco role. It stays active in
  every gate. It does not scale down with `modes.workflow`,
  `modes.review_mode`, or `team.size` (F-04, F-05, F-06).
- **protected path** — a file path (for example `config/risk/**`,
  `policies/**`) whose change needs an approval receipt (DEC-17). No hook
  blocks the write. The receipt is the control, and a change without a
  receipt reads NOT ASSESSED.
- **approval receipt** — a recorded, hashed approval for a change to a
  protected path, or for a stage advance. It names the approver's role and
  the content hash.
- **activation wave** — the set of agents and skills turned on together:
  W1 information core, W2 fund operation, W3 institutional. See Section
  6.1 and `evidence/design-addendum-01.md` §3.
