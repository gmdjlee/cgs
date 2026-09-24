# HFT-PLAN-001 — Hedge Fund Transition Master Plan

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-PLAN-001 |
| Title | Hedge Fund Transition — Master Plan |
| Version | 0.1 |
| Date | 2026-09-24 |
| Status | Draft for founder review |
| Owner | Advisor (main session) |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules |

This document is not legal advice. It is not tax advice. It is not investment
advice. Section 3 states this rule in full.

## 2. Purpose

This plan sets the steps to change Claude Code Game Studios (CCGS) into an
agent organization for a Korean hedge fund management company. The Korean
legal term is 일반 사모집합투자업자 (a general private-fund manager). It uses
transition Strategy C: transplant only the operating foundation (hooks,
config resolution, session state, gate mechanics, skill testing). Strategy C
also writes every fund-domain agent and skill fresh. The plan turns the
founder's answers to 36 questions (QUESTIONS.md) into a phased work plan, a
schedule, and a risk register. It cites every claim to a fact (Section 5), a
report chunk (HF-REF-NN), or a marked INFERENCE or GAP.

## 3. Scope

### 3.1 In scope

- The 10-phase work plan, P0 through P9 (Section 8).
- The founder decision process, 9 rounds and 36 questions (Section 9).
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

The working files below built this plan. They are session-scratch files.
They are not part of the repository.

| File | Content |
|---|---|
| `design-spec.md` | The Advisor's design decisions (F-01 to F-16, SB-01 to SB-28, the org roster, the lifecycle, the control model, the skill catalog, phases P0 to P9, the AAA bar, the risk list). |
| `question-spec.md` | The 36 founder questions in 9 rounds. |
| `wf1.json` | The raw assessment result: 6 area assessments plus the org blueprint (`orgmap`), each independently verified. |
| `assess-compact.md` | A readable digest of `wf1.json`. |
| `orgmap.json` | The org blueprint raw result. |
| `verifier-issues.md` | The verifier's corrections, applied in this document set. |
| `review.txt`, `mapping.txt` | The prior T1/T2 review's working notes and component mapping table. |

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
| `QUESTIONS.md` | The 36 founder questions and the decision log (DEC-NN). |

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

Some items below are the Advisor's recommended answer to an open founder
question, not yet a decision. Section 6.1's build order matches the
recommended option for Q09. Section 6.3's control-blocking mechanism and
fixed-seat scope match the recommended options for Q13 and Q14. Round 3
(Q09) and Round 4 (Q13, Q14) confirm or change them.

### 6.1 Organization

| Stage | Name | Agent count (design estimate) |
|---|---|---|
| Stage 1 | 설립기 (founding stage) | 10-13 |
| Stage 2 | 성장기 (growth stage) | 22-27 |
| Stage 3 | 기관화 (institutionalization stage) | 24-31 |

The roster follows HF-REF-08 표 6-1 (functions) and 표 6-2 (stage
activation). The cro (risk officer support) and the cco (준법감시인, compliance
officer, support) report outside the cio's line (HF-REF-08 §6.2). Counts
are design estimates. They are not a fixed headcount. See Section 7, P-07,
"Design stage 3, build stage 1 first," for the build order.

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
- **Fixed control seats**: the cro and the cco stay active in every gate.
  `modes.workflow`, `modes.review_mode`, and `team.size` do not remove them.
- **Hook enforcement**: a PreToolUse hook blocks a write to a protected path
  (for example `config/risk/**`, `policies/**`, `investor/outgoing/**`)
  unless a matching approval receipt exists.
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
| P-04 | Enforce controls with the harness, not with prose |
| P-05 | Data-driven limits |
| P-06 | Keep foundation file paths for upstream updates |
| P-07 | Design stage 3, build stage 1 first |
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

**P-03 Control independence.** The cro and the cco report outside the cio's
line (Section 6.1). No agent may override, edit, or suppress a cro or a cco
verdict. Only the founder or the board may accept a documented exception.

**P-04 Enforce controls with the harness, not with prose.** Today's gates
are advisory. A prose instruction does not block a tool call (F-03, F-08).
Use a PreToolUse hook, a `tools: Agent(...)` allow-list, or a `settings.json`
deny rule instead. Keep prose for guidance that carries no compliance
weight.

**P-05 Data-driven limits.** Store every loss limit, exposure limit, and
leverage limit in a config file, never in code or in a skill's prose
(`coding-standards.md`). This lets the founder and the cro change a limit
without a text edit to a skill file.

**P-06 Keep foundation file paths for upstream updates.** Keep the same
file paths as CCGS for hooks, scripts, and config resolution (F-15). This
keeps `UPGRADING.md` strategy A2 and strategy B usable for upstream security
and bug fixes.

**P-07 Design stage 3, build stage 1 first.** Design the full three-stage
organization now. Build only the stage-1 roster first. This meets the
"best organization" goal through the design. It also caps the organization
at the size the founder needs, and no more (risk R-06).

**P-08 Test first.** Write a test for every silent break, SB-01 to SB-28,
before Phase P6 starts (Section 10). Write a failing-gate test for every
new hook: break the guarded thing, confirm the check fails, then restore it
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
| P0 done; `QUESTIONS.md` holds 36 questions in 9 rounds | Every question Q01-Q34 (and Q35-Q36 if triggered) has one DEC-NN entry | 4-8 h (plus 2-4 h founder time) | Advisor + Founder |

Tasks:

1. Read `design-spec.md` and `question-spec.md` rules before round 1.
2. Ask the founder round 1 (Q01-Q04).
3. Record each answer as DEC-01 to DEC-04 in `QUESTIONS.md`.
4. Repeat steps 2-3 for rounds 2 through 9, in order.
5. Add Q35 and Q36 to round 7 only if the Q25 answer is C or D.
6. Close each round once every question in it has a DEC-NN entry.

Outputs: `QUESTIONS.md` (answered register with DEC-NN entries); a term map
of new `project.yaml` keys named by the founder's answers.

Gating questions: none. This phase produces the answers other phases need.

### P2 — Target design

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P1 complete, all DEC-NN recorded | The founder approves the design package in writing (an approval receipt) | 12-30 h | Advisor |

Tasks:

1. Finalize the agent roster from the Q05 and Q09 answers.
2. Draft the lifecycle catalog (S1-S8, G1-G3) to replace
   `workflow-catalog.yaml`.
3. Finalize the control model: verdict vocabulary, fixed seats, hook
   rules.
4. Draft the new `project.yaml` config schema: `archetype`, `jurisdiction`,
   `risk.*`, `regulatory_calendar`, `controls.four_eyes`,
   `controls.protected_paths`.
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
3. Build the protected-path PreToolUse hook and the approval-receipt
   format.
4. Build the regulatory value registry (`as_of` and effective dates).
5. Rewrite `coordination-rules.md` to add the non-override rule.
6. Set the `tools: Agent(...)` allow-lists so a front-office agent cannot
   spawn or edit the cro, the cco, or their reports.
7. Write a failing-gate test for every new hook.

Outputs: `.claude/docs/coordination-rules.md` (revised); the protected-path
hook script; the regulatory value registry file; the adapted
`review-receipts.sh`; agent frontmatter allow-lists;
`tests/integration/control/*`.

Gating questions: Q10, Q13, Q14, Q15, Q25, Q26, Q28, Q35, Q36.

### P5 — Pilot and re-measure

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P4 done | All three pilot components reach grade AAA; the re-estimate note exists | 10-25 h | Worker |

Tasks:

1. Build the cro agent to the AAA bar.
2. Build the `/risk-report` skill to the AAA bar.
3. Build the `/regulatory-calendar` skill to the AAA bar.
4. Run each through the AAA-QUALITY-BAR.md checks.
5. Log the actual hours spent on tasks 1-4.
6. Re-estimate phases P6 through P9 from the measured hours.

Outputs: `agents/cro.md`; `skills/risk-report/SKILL.md`;
`skills/regulatory-calendar/SKILL.md`; a pilot log; a re-estimate note
added to Section 11 of this document.

Gating questions: Q22, Q23, Q33, Q34.

### P6 — Stage-1 roster and priority skills

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P5 re-estimate done | `/skill-test static` returns 0 FAIL for every new skill; `/skill-test category` returns COMPLIANT | 100-300 h | Worker |

Tasks:

1. Build the 10 stage-1 core agents (see `ORG-BLUEPRINT.md`).
2. Build 0-3 archetype agents per the Q05 answer.
3. Build the priority skill bundles from the Q22 answer.
4. Build the matching templates.
5. Run `/skill-test static` and `/skill-test category` on each new skill.

Outputs: `agents/*.md` (stage-1 set); `skills/*/SKILL.md` (priority
bundles); `templates/*`.

Gating questions: Q09, Q11, Q19, Q22.

### P7 — End-to-end dry run

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P6 done for the stage-1 set one idea and one setup stage need | The idea cycle completes with no manual patching; the setup-stage gate returns a verdict; evidence is retained | 10-25 h | Worker + Founder (review) |

Tasks:

1. Run one investment idea through the full cycle: idea, analysis,
   portfolio review, pre-check, execution record, monitoring, and
   post-review.
2. Run one setup stage (S1-S8) through its own gate.
3. Take a screenshot or a log of every step as evidence.
4. Store the evidence in `production/qa/evidence/`.
5. Record the dry run result and any patch it needs.

Outputs: `production/qa/evidence/*` (retained evidence); a dry-run report.

Gating questions: Q17, Q18, Q20, Q23.

### P8 — Stage-2/3 activation and conditional pipeline

| Entry criteria | Exit criteria | Estimate | Owner |
|---|---|---|---|
| P7 passed; the founder approves stage-2/3 activation | Each new component reaches grade AAA; the model-governance failing-gate test passes if the quant pipeline is built | 60-200 h (conditional on scope) | Worker |

Tasks:

1. Build the remaining stage-2 agents and skills.
2. Build the remaining stage-3 agents and skills.
3. If Q25 is C or D, build the quant research pipeline: `/model-change`,
   `/model-review`, `/backtest-evidence`, and the model governance
   controls.
4. Activate conditional agents per the founder's archetype answer and the
   Q24 answer.

Outputs: `agents/*.md` (stage-2/3 set); `skills/*/SKILL.md` (quant
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

The founder answers 36 questions in 9 rounds, in `QUESTIONS.md`. Round 1
starts right after the founder reads this plan.

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

| Round | Questions | Phases it unblocks |
|---|---|---|
| R1 | Q01-Q04 | P2, P3 |
| R2 | Q05-Q08 | P2, P6 |
| R3 | Q09-Q12 | P2, P4, P6, P8 |
| R4 | Q13-Q16 | P3, P4 |
| R5 | Q17-Q20 | P2, P6, P7 |
| R6 | Q21-Q24 | P2, P5, P6, P7, P8 |
| R7 | Q25-Q28 | P3, P4, P8 |
| R8 | Q29-Q32 | P2, P3, P4, P9 |
| R9 | Q33-Q36 | P3, P4, P5, P8 |

## 10. Verification strategy

**AAA-QUALITY-BAR.md** holds the full grading rule. This section maps each
phase to its check.

| Phase | What is verified | How |
|---|---|---|
| P0 | Chunk lossless reassembly; 6 area assessments plus the org blueprint | `split_report.py --check` (exit 0); one verifier pass per area, plus one for the org blueprint |
| P1 | Every question answered | A completeness check of DEC-NN entries against the 36 (plus 0-2 conditional) question IDs |
| P2 | The design package | A founder approval receipt; the term map checked against Appendix B |
| P3 | Transplant integrity | SB-01 to SB-28 tests, one test per silent break |
| P4 | The control spine | Failing-gate tests: break the guard, confirm the check fails, restore it |
| P5 | The 3 pilot components | `/skill-test` static, spec, and category modes; one independent review receipt per component |
| P6 | The stage-1 build | `/skill-test static` (0 FAIL) and `/skill-test category` (COMPLIANT) on every new skill; the ASD-STE100 lint helper run on every new document (observation only) |
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
| R-02 | Regulatory values go stale | M | M | Run `/refresh-facts` on a quarterly schedule (Q31); every value carries an `as_of` date in the registry | cco / compliance-analyst | P4, P9 |
| R-03 | An advisory gate gets skipped silently | H | H | Replace prose gates with hooks and allow-lists (P-04); build the protected-path hook | Worker | P4 |
| R-04 | A silent break appears during the transplant | H | M | Run the SB-01 to SB-28 test set before Phase P6 starts | Worker | P3 |
| R-05 | A same-session review gets mistaken for an independent one | M | H | Label every agent review "pre-screen" (F-09); require a human sign-off receipt | Founder | P4, P5 |
| R-06 | Scope grows toward the full 24-31 agent organization before it is needed | H | M | Design stage 3, build stage 1 first (P-07); a founder approval gate before each stage activation | Advisor | P2, P6, P8 |
| R-07 | Confidential data or MNPI (undisclosed material information) reaches the repository | M | H | Apply the Q28 information-grade policy; start with a gitignored local directory; use the protected-path hook | cco | P4 |
| R-08 | Upstream CCGS changes drift away from the transplant | M | M | Keep foundation file paths identical (P-06); use `UPGRADING.md` strategy A2 or B | Worker | P3 |
| R-09 | An agent states a legal or regulatory fact with no source | M | H | Enforce the AAA-04 citation rule; every fact in this plan cites HF-REF-NN or F-NN | Advisor | All phases; checked at P9 |
| R-10 | The agent `model:` tier pin turns out not to work | M | L | Measure whether the `model:` field changes behavior during Phase P3, before the Q34 tier plan is relied on | Worker | P3 |
| R-11 | Two concurrent tracks (setup and operation) do not fit one `project.stage` value | M | M | Keep `project.stage` a single scalar (Q17); change only the `/help` and `/gate-check` tables (F-11) | Worker | P2, P3 |
| R-12 | The source report is not legal, tax, or investment advice; some topics are gaps | H | H | State the disclaimer in Section 3; route each gap to outside counsel before the matching phase closes | Founder | P1 (decision to get counsel); ongoing |

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

1. The founder reads `README.md` and this plan (`PLAN.md`).
2. The founder and the Advisor run round 1 (Q01-Q04) right after that
   reading.
3. The Advisor records each round-1 answer as a DEC-NN entry in
   `QUESTIONS.md`.
4. The Advisor and the founder run rounds 2 through 9, in order, one round
   at a time.
5. The Advisor adds Q35 and Q36 to round 7 only if the Q25 answer is C or
   D.
6. The Advisor drafts the Phase P2 design package from the completed
   decision log.
7. The founder approves the Phase P2 design package with an approval
   receipt.
8. The Worker starts Phase P3 once the founder approves Phase P2 and
   answers Q04.
9. The Advisor schedules the Phase P5 re-estimate check before Phase P6
   starts.

## Appendix A: Requirements traceability

| ID | Requirement | Satisfied in | Evidence |
|---|---|---|---|
| UR-01 | Build the best hedge-fund organization | Section 6; `ORG-BLUEPRINT.md` | The full roster, tier structure, and stage counts |
| UR-02 | Use the standard hedge-fund org structure; staff it with AAA-or-better agents | Section 6; Section 10; `AAA-QUALITY-BAR.md` | The AAA-01 to AAA-14 grading rule; "only AAA may ship" |
| UR-03 | Use transition strategy C (transplant the operating foundation only) | Section 2; Section 3; Section 6; `TRANSPLANT-MANIFEST.md` | F-01, the review's Strategy C recommendation |
| UR-04 | Decide the agents and skills through discussion with the founder | Section 9 | 9 rounds, 36 questions, DEC-NN decision log |
| UR-05 | Ask the founder detailed questions | Section 9; `QUESTIONS.md` | 36 questions with 질문/왜 묻는가/근거 fields |
| UR-06 | Give 4-5 options per question | Section 9 rules | The `question-spec.md` option format |
| UR-07 | Use `hedge_fund_setup_report.md` as the base frame | Section 4.2 | HF-REF-00 to HF-REF-20 chunk index |
| UR-08 | Split the report into optimal chunks | Section 4.2; Section 8, Phase P0 | 21 chunks, byte-exact reassembly check |
| UR-09 | Keep AAA quality or better | Section 10; `AAA-QUALITY-BAR.md` | Per-phase verification table |
| UR-10 | Base every claim on facts and verify it | Section 5; Section 7, P-01 | F-01 to F-16, each with a citation |
| UR-11 | Write technical documents in ASD-STE100 | Document header; Section 7, P-10 | The writing-standard field; the sentence-length and voice rules |

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
  `policies/**`) that a PreToolUse hook blocks, unless a matching approval
  receipt exists.
- **approval receipt** — a recorded, hashed approval for a change to a
  protected path, or for a stage advance. It names the approver's role and
  the content hash.
- **stage activation** — the count of agents and skills built and turned
  on at a given organization stage (stage 1, 2, or 3). See Section 6.1.
