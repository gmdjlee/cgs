# HFT-QA-001 — AAA Quality Bar

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-QA-001 |
| Title | AAA Quality Bar |
| Version | 0.2 |
| Date | 2026-09-24 |
| Status | Draft for founder review |
| Owner | Advisor (main session) |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules. Checked manually in v0.1; the STE lint helper is a P3 deliverable. |
| Working files | The names design-spec, question-spec, wf1.json, assess-compact.md, orgmap.json, verifier-issues.md, review.txt, and mapping.txt refer to files in [`evidence/`](evidence/README.md). |
| Scope | The AAA-01 to AAA-14 acceptance bar for every hedge-fund agent, skill, gate, hook, template, and document; the new control, investment, reporting, and setup rubric categories; the certification procedure and record; the Skill Testing Framework registry mapping; the ASD-STE100 and Korean language-quality checks. |

This document is not legal advice. It is not tax advice. It is not
investment advice. `PLAN.md` §3 states this rule in full.

**Change history**

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-24 | Initial draft. |
| 0.2 | 2026-09-24 | Applied DEC-17: control check CT3 now needs an approval receipt instead of a protected-path hook. The accepting party for an exception is the user (DEC-10). |

## 2. Purpose

"AAA" is the minimum grade for every member of the hedge-fund
organization. This covers every agent, every skill, every gate, every
hook, every template, and every document that supports one. design-spec
§8 states the rule: only AAA may ship.

A minimum grade is a slogan until it is a test. This document turns "AAA
quality" into 14 numbered criteria (Section 4), each with an exact test
method, a pass condition, and an evidence path. It adds four rubric
categories the hedge-fund organization needs and the Skill Testing
Framework does not yet have (Section 5).

Section 6 sets the certification procedure a component walks, from a
draft to an AAA grade. Section 7 sets the record that proves each step
ran. Section 8 maps the change this whole bar forces onto the Skill
Testing Framework's four registry files. Section 9 closes with the
measurable language checks AAA-12 runs.

Every criterion in this document reuses a CCGS Skill Testing Framework
metric, quoted with its file and line in Section 4.1. Or it states a
new, hedge-fund-specific check. Where a check is new, this document says
so and gives its source: a design-spec fact (F-NN), a blueprint section,
or a report chunk (HF-REF-NN).

## 3. Grades

design-spec §8 sets three grades. This document keeps the same rule.

| Grade | Criteria required |
|---|---|
| **A** | AAA-01 to AAA-03 (structure, category, behavior spec) |
| **AA** | A, plus AAA-04 to AAA-08 (facts, NOT ASSESSED discipline, one verdict vocabulary, control independence, the human boundary) |
| **AAA** | AA, plus AAA-09 to AAA-14 (the failing-gate test, independent review, the P7 dry run, language, the benchmark trace, the audit trail) |

**Only AAA may ship.** A component graded A or AA is a work in progress.
It does not go into the stage-1 roster, a skill bundle, or a published
document (design-spec §8).

A component that fails a criterion inside its target grade does not drop
to the next grade down by default. It stays NOT ASSESSED for that
criterion instead. This holds until the certification record (Section 7)
shows a fix and a re-check. This mirrors `skill-authoring.md`'s first
obligation: a run that could not assess part of its scope has not
established that the scope is good (`.claude/rules/skill-authoring.md`:28-30).

## 4. Criteria table

Read every "Tool or source" cell as a citation, not a summary. Section
4.1 quotes the CCGS rubric metric behind each reused check, with its
file and line.

| ID | Criterion | Applies to | Test method | Pass condition | Evidence to keep | Tool or source |
|---|---|---|---|---|---|---|
| **AAA-01** Structure | The component passes structural compliance. A skill scores 0 FAIL on the static linter. An agent's frontmatter is complete. | agent, skill | Run `/skill-test static [name]`. For an agent, check `name`, `description`, `tools` (or `allowed-tools`), and `model` are all present. | `/skill-test static` returns COMPLIANT, 0 FAIL (a WARN does not block AAA-01). Every required agent frontmatter field is present. | Certification record (Section 7), row "AAA-01"; `catalog.yaml` `last_static` / `last_static_result`. | `/skill-test static` (`skill-test/SKILL.md`:39, Phase 2A, checks 1-7); reuses rubric **U1**. |
| **AAA-02** Category | The component passes its category rubric — a new hedge-fund category (Section 5) or a kept CCGS category (Section 4.1). | agent, skill, gate | Run `/skill-test category [name]`. | The category check returns COMPLIANT, 0 FAIL. | Certification record, row "AAA-02"; `catalog.yaml` `last_category` / `last_category_result`. | `/skill-test category` (`skill-test/SKILL.md` Phase 2D); `quality-rubric.md`; Section 5 of this document. |
| **AAA-03** Behavior spec | The component's spec has 5 cases — happy path, failure or blocked, mode variant, edge case, gate — and every case passes. | agent, skill | Run `/skill-test spec [name]` against the spec path in `catalog.yaml`. | Overall Verdict PASS. Every case reads PASS. A PARTIAL, FAIL, or NOT ASSESSED case blocks AAA-03. | `CCGS Skill Testing Framework/results/skill-test-spec-[name]-[date].md`. | `/skill-test spec` (`skill-test/SKILL.md` Phase 2B); `templates/skill-test-spec.md`, `templates/agent-test-spec.md`. |
| **AAA-04** Facts | Every regulatory or market value cites `HF-REF-NN §x.y` (or `SRC-NN`) and shows an as-of date. A medium- or high-volatility value carries a re-verify note. | doc, template, skill | List every number tied to law, regulation, or the market in the file. Check each number's citation and as-of date. Check its chunk's volatility grade in `docs/hedge-fund-setup/ref/README.md`'s chunk table. | 100% of the listed numbers carry a citation and an as-of date. Every medium- or high-volatility number carries a re-verify note. | The facts-check list, in the certification record. | `docs/hedge-fund-setup/ref/README.md` chunk table (volatility column); design-spec F-16; PLAN.md P-01. |
| **AAA-05** NOT ASSESSED discipline | The component follows `skill-authoring.md`'s five obligations. An absent input never returns PASS. | skill, gate, hook | Check the component against all five obligations (Section 4.2 lists them). Apply the silent-skip test: "if this step silently did not run, what would the output look like?" | All five obligations hold. The silent-skip test finds no gap. | The five-obligation checklist, in the certification record. | `.claude/rules/skill-authoring.md`:21-79 (the five obligations); `.claude/rules/skill-authoring.md`:107-112 (the silent-skip test). |
| **AAA-06** One verdict vocabulary | The component emits only PASS, CONCERNS, FAIL, or NOT ASSESSED. Precedence: FAIL beats CONCERNS; CONCERNS beats NOT ASSESSED; NOT ASSESSED beats PASS. | gate, skill, agent, hook | Grep the component for every verdict word it emits. Check the set against the four values. Check the precedence rule on a mixed-result example. | The component emits only the four values, or maps a domain-equivalent word to one of them in a stated table. The precedence rule holds. | The grep output, in the certification record. | design-spec §5 (donor `gate-check/SKILL.md`:481-552); PLAN.md P-09; design-spec F-07 (today's 28 gate files use 9 vocabularies). |
| **AAA-07** Control independence | The cro and cco seats stay fixed. The `tools: Agent(...)` allow-lists match the delegation matrix. No agent overrides a cro or cco verdict. | agent, gate, hook | Grep the component for a condition on `modes.workflow`, `modes.review_mode`, or `team.size` that would skip a control review. Diff every agent's `tools: Agent(...)` list against `ORG-BLUEPRINT.md` §8. Grep every agent file for override, edit, or suppress language pointed at a cro or cco verdict. | No conditional skip is found. The allow-list diff is empty. No override language is found; only "the founder" or "the board" appear as the accepting party for a documented exception. | The grep and diff output, in the certification record. | `ORG-BLUEPRINT.md` §8 (delegation matrix, non-override rule); design-spec §5; F-04 (default `review_mode` is `lean`), F-05 (default `team.size` is `individual`), F-06 (the gate-check panel scales 1-4 by `modes.workflow`) — the three ways a seat could silently shrink. |
| **AAA-08** Human boundary | The component lists its prohibited actions. No document assigns a human-required role to an agent. | agent, template, doc | Check the agent file for the general prohibited-action list plus its row-specific entry. Check that no agent is named as the final signer, approver, or holder of a human-required role. | The prohibited-action list is present, verbatim or by reference. No human-required-role assignment is found. | The checklist, in the certification record. | `ORG-BLUEPRINT.md` §3, §4, §6; design-spec F-10. |
| **AAA-09** Failing-gate test | A failing-gate test exists for the component. It breaks the guarded thing, confirms the check fails, then restores it. | hook, gate | Make one mutation — for example, a control decision with no receipt, or a missing config key. Run the check. Confirm it fails or blocks. Restore the file or state. Make one mutation per tool call. | The check fails or reads NOT ASSESSED in the broken state; a hook, where one exists, returns exit code 2. The check passes after the restore. Both runs are logged. | The before-and-after transcript, in `tests/integration/control/` or the certification record. | `.claude/rules/skill-authoring.md`:86-87 ("A gate you have not watched fail is not a gate... Break the thing it guards, confirm it fails, restore."); PLAN.md P-08. |
| **AAA-10** Independent review | A different agent pre-screens the component. The founder reviews it. A receipt records both. | agent, skill, gate, hook, template, doc | Spawn an agent other than the author to pre-screen the component. Hash the reviewed file with `review-receipts.sh hash`. Give the founder the pre-screen result and get a sign-off. | A `Reviewed-Content-Hash:` line exists for the file. The founder's sign-off is logged. The pre-screen alone does not satisfy AAA-10. | The `review-receipts.sh` output line and the founder's sign-off entry, in the certification record (Section 7). | `.claude/scripts/review-receipts.sh` (`hash` mode); design-spec F-09 ("A subagent in the same session is not an independent reviewer... It is a pre-screen."). |
| **AAA-11** Scenario | The component works inside the Phase P7 dry run, with no manual patch. | agent, skill, gate, hook, template | Run the component inside the P7 dry run — one investment idea through the full cycle, or one setup stage through its gate. | The component completes its part of the dry run. No file outside the component's own writes needed a manual edit. | A retained screenshot or log, in `production/qa/evidence/`. | `PLAN.md` Phase P7; `.claude/docs/coding-standards.md` ("A parse check is not a run."). |
| **AAA-12** Language | An English technical document passes the ASD-STE100 checks (Section 9). A Korean regulatory or investor document passes the Korean style checks (Section 9). | doc, skill, agent, template | Run the STE-lint helper on the file. For a Korean document, run the Korean style checklist. | The lint helper reports 0 findings, or every finding carries a dated, documented exception. The Korean checklist has no open item. | The lint helper's output, in the certification record. | `.claude/scripts/ste-lint.sh` — an observation-only script (`CLAUDE.md`:75, "Helpers in `.claude/scripts/` emit observations, never verdicts."); Section 9 of this document. |
| **AAA-13** Benchmark trace | A control-related component names the `ORG-BLUEPRINT.md` §12 principle it encodes. | agent, gate, hook, template | For each control-related component, find the matching row in `ORG-BLUEPRINT.md` §12. Check the citation carries through to the component's own file. | At least one named principle, with its citation, appears in the component file or its certification record. | The trace line, in the certification record. | `ORG-BLUEPRINT.md` §12; HF-REF-17 §9.5 표 9-5 (most rows; some rows in §12 cite HF-REF-14 §8.5 표 8-3 or HF-REF-16 §9.3 instead — read the row's own citation). |
| **AAA-14** Audit trail | The component's actions are logged. The design decision behind it cites a DEC-NN entry. | agent, skill, gate, hook | Confirm `log-agent.sh` / `log-agent-stop.sh` and `session-stop.sh` fire on a representative run. Find the DEC-NN entry in `QUESTIONS.md` behind the component's design. | A log entry exists for the representative run. The DEC-NN citation is present. | The log location and the DEC-NN citation, in the certification record. | `.claude/hooks/log-agent.sh`, `.claude/hooks/log-agent-stop.sh`, `.claude/hooks/session-stop.sh`; `QUESTIONS.md` (the DEC-NN log). |

### 4.1 CCGS rubric metrics this bar reuses

AAA-02 also covers a component that keeps a CCGS category. A transplanted
`sprint-plan`-shaped skill keeps the `sprint` category, for example. The
table below quotes one or two metrics from every CCGS skill category and
every CCGS agent category a hedge fund can reuse. It skips the `engine`
agent category — a hedge fund has no engine specialist. Each quote is
verbatim from `CCGS Skill Testing Framework/quality-rubric.md`, cited by
line.

| Metric | Category | Quote | File:line | Reused by |
|---|---|---|---|---|
| **G1** | gate (skill) | "Skill reads `production/session-state/review-mode.txt` (or equivalent) before deciding which directors to spawn" | quality-rubric.md:23 | AAA-07 — a hedge-fund control gate reads the mode, then must NOT let the mode remove the cro or cco seat. |
| **G5** | gate (skill) | "Skill never writes `production/stage.txt` without explicit user confirmation via \"May I write\"" | quality-rubric.md:27 | AAA-08 — the same no-silent-advance rule, applied to a human-required final call. |
| **R3** | review (skill) | "Verdict is exactly one of: APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED (design) or PASS / CONCERNS / FAIL (architecture)" | quality-rubric.md:42 | AAA-06 — the source pattern for one fixed vocabulary, generalized to PASS / CONCERNS / FAIL / NOT ASSESSED. |
| **A5** | authoring (skill) | "Full authoring skills create a file skeleton with all section headers before filling content, to preserve progress on session interruption." | quality-rubric.md:66 | AAA-02 — a hedge-fund authoring skill (for example `/business-plan`, `/policy-author`) keeps this metric. |
| **P3** | pipeline (skill) | "Skill asks \"May I write [artifact]?\" before creating each output file, not batch-approving all files at once" | quality-rubric.md:102 | AAA-05 and AAA-02 — an investment-cycle pipeline skill (for example `/investment-memo`) keeps this metric. |
| **AN1** | analysis (skill) | "Analysis phase uses only Read/Glob/Grep tools; no Write or Edit during the scan itself" | quality-rubric.md:118 | AAA-05 — a compliance or risk analysis skill (for example `/risk-report`) keeps this metric as a floor; Section 5's `control` category raises it to a hard block. |
| **AN3** | analysis (skill) | "Any suggested file writes (e.g., tech-debt register, fix patches) are gated behind \"May I write\"" | quality-rubric.md:120 | AAA-05 — `/control-gap-register` (the `tech-debt` donor) keeps this metric. |
| **T3** | team (skill) | "If any spawned agent returns BLOCKED or fails, skill surfaces it immediately and halts dependent work — never silently skips" | quality-rubric.md:137 | AAA-05 — an orchestration skill that spawns more than one agent keeps this metric. |
| **SP4** | sprint (skill) | "Skill never writes sprint files or milestone records without \"May I write\"" | quality-rubric.md:155 | AAA-02 — the transplanted `sprint-plan`, `sprint-status`, `retrospective`, and `milestone-review` skills keep the `sprint` category and this metric. |
| **U1** | utility (skill) | "`/skill-test static [name]` returns COMPLIANT with 0 FAILs" | quality-rubric.md:172 | AAA-01 — the mechanism AAA-01 generalizes to every skill, not only the `utility` category. |
| **D1** | director (agent) | "Returns APPROVE / CONCERNS / REJECT (or domain equivalent: REALISTIC/CONCERNS/UNREALISTIC for producer)" | quality-rubric.md:187 | AAA-06 — a Tier-1 leadership agent (for example cio, coo) that keeps this verdict shape maps it to PASS / CONCERNS / FAIL / NOT ASSESSED. |
| **D4** | director (agent) | "Agent is assigned Opus model per coordination-rules.md" | quality-rubric.md:190 | AAA-02 — a Tier-1 leadership agent keeps this metric as a target, not a verified fact. design-spec F-12 marks an agent's `model:` field unverified; PLAN.md R-10 schedules the check in Phase P3. |
| **L2** | lead (agent) | "Out-of-domain conflicts escalate to creative-director (design) or technical-director (tech)" | quality-rubric.md:200 | AAA-02 and AAA-07 — a Tier-2 lead escalates to its Tier-1 parent; a Tier-2 lead under cro or cco escalates inside that line only (`ORG-BLUEPRINT.md` §8). |
| **S3** | specialist (agent) | "Out-of-domain requests are redirected to the correct agent, not refused silently" | quality-rubric.md:214 | AAA-02 — a Tier-3 specialist (for example research-analyst) keeps this metric. |
| **Q3** | qa (agent) | "Does not propose new features; flags gaps for humans to decide" | quality-rubric.md:238 | AAA-08 — a compliance-analyst or risk-analyst agent flags a gap for the founder or the cco; it does not decide the exception itself. |
| **O2** | operations (agent) | "Does not write game logic or engine code; delegates to appropriate specialist" | quality-rubric.md:248 | AAA-02 — the coo and fund-operations-lead agents keep this "delegate, do not implement" shape. |

### 4.2 The five `skill-authoring.md` obligations (AAA-05's checklist)

AAA-05 checks all five. State each result as PASS or FAIL, never a
free-form note.

1. **A "could not assess" value exists.** The component's verdict
   vocabulary has a NOT ASSESSED value (or the local equivalent), ranked
   above PASS and below every failure value (`.claude/rules/skill-authoring.md`:21-36).
2. **No permissive default.** An absent config key does not take the
   permissive branch, especially when nothing in the framework writes that
   key (`.claude/rules/skill-authoring.md`:38-45).
3. **A skipped step announces itself.** The output names a skipped phase,
   category, or agent by name, not only in the source
   (`.claude/rules/skill-authoring.md`:47-55).
4. **No unsourced assertion.** A fact the component cannot source reads
   "GAP" or "NOT SOURCEABLE — [what] is not covered by [path]." This
   forces obligation 1's value rather than a note beside it
   (`.claude/rules/skill-authoring.md`:57-69).
5. **The component derives its covered set; it does not enumerate it.**
   The component may use a hand-written list only when it states why
   derivation failed and the duty to extend the list
   (`.claude/rules/skill-authoring.md`:70-79).

## 5. New hedge-fund rubric categories

The Skill Testing Framework has nine skill categories and six usable
agent categories (Section 4.1). None of them cover a compliance check, a
trade record, an investor report, or a firm-setup step. This section
adds four categories: `control`, `investment`, `reporting`, `setup`.
Write these into `quality-rubric.md` in the same style as the existing
categories. Use an ID, a check, and a pass rule, one row per metric, with
5 metrics per category.

### `control`

**Applies to**: cro, cco, and any gate, hook, or skill that enforces a
limit, a policy, or a protected path (for example `/pre-trade-check`,
`/risk-report`, `/limit-registry`).

| ID | Check | Pass rule |
|---|---|---|
| **CT1 — Fixed seat** | The cro or cco seat runs in every mode. | `modes.workflow`, `modes.review_mode`, and `team.size` never remove or fold the seat into another agent. A grep for a conditional skip finds none. |
| **CT2 — NOT ASSESSED on an absent policy or limit file** | The component's verdict is NOT ASSESSED, not PASS, when its policy or limit file is missing. | The verdict names the missing path. It never defaults to PASS. |
| **CT3 — Approval receipt on a control decision (DEC-17)** | A change to a protected path (for example `config/risk/**`, `policies/**`) or another control decision carries the cro verdict and a recorded user approval. | Every control decision has a `review-receipts.sh` receipt that names the approver and the content hash. A decision without a receipt reads NOT ASSESSED, never PASS. No hook blocks the write (DEC-17); the receipt check is the control. |
| **CT4 — No agent sends an order or signs** | No tool, skill instruction, or template lets an agent submit a live order, sign a filing or a contract, give the final NAV, give the final compliance or limit approval, make an investor promise, or give legal advice. | A grep for these actions, scoped to an agent's own authority (not a human's), finds none granted. |
| **CT5 — No override** | No agent instruction lets any agent edit, suppress, or overwrite a cro or cco verdict. | Only the user (the founder) appears as the accepting party for a documented exception (`ORG-BLUEPRINT.md` §8; DEC-10, DEC-17). |

### `investment`

**Applies to**: the investment-cycle skills (`/idea-screen`,
`/investment-memo`, `/ic-review`, `/pre-trade-check`, `/post-trade-review`,
`/strategy-pilot`, `/cycle-dry-run`).

| ID | Check | Pass rule |
|---|---|---|
| **IV1 — Decision record before the pre-trade gate** | The investment thesis and the stop-loss or re-check condition are written before the idea reaches the pre-trade-check step. | The skill's output order places the decision record ahead of the gate call. |
| **IV2 — Pre-trade gate blocks** | The idea does not reach order execution without a PASS, or a cleared CONCERNS, on the pre-trade check. | The check covers the fund rule limit, the statutory limit, and the stock-loan balance (HF-REF-09 §7.1, §7.3). A violation returns the idea to portfolio construction. |
| **IV3 — No order authority** | The skill's output is a record or a report for a human trader. | The skill never submits, sends, or confirms an order itself. |
| **IV4 — Post-review closes the loop** | The post-trade review compares the result against the original decision record. | The comparison is not limited to P&L; it checks the stated thesis and stop-loss condition. |
| **IV5 — As-of dated inputs** | Every market or regulatory value the skill cites carries an as-of date and a citation. | Reuses AAA-04, applied to the investment cycle specifically. |

### `reporting`

**Applies to**: the reporting skills (`/monthly-report`,
`/investor-letter`, `/ddq-response`, `/regulatory-calendar`, `/nav-check`,
`/fee-calc`).

| ID | Check | Pass rule |
|---|---|---|
| **RP1 — Cadence sourced** | The report's cadence or trigger cites a chunk, or reads GAP. | It is never invented. Compare against `ORG-BLUEPRINT.md` §10's cadence column. |
| **RP2 — No unverified investor claim** | The skill does not let an investor-facing document state a return, a guarantee, or a promise with no data source. | A grep for a return figure, a guarantee word, or a promise word finds a citation next to each one, or none appear. |
| **RP3 — Independent check before publish** | A NAV-affecting number gets an independent check before the report goes out. | The fund-accountant's shadow NAV (or an equivalent named check) runs before publication (HF-REF-10 §7.4). |
| **RP4 — Correct addressee** | The skill states who reads the report — internal or external. | An internal report (for example the regulatory calendar) and an external one (for example the investor letter, the DDQ response) are not mixed in the same output. |
| **RP5 — Filing deadline tracked** | A regulatory report names its statutory deadline, or reads GAP. | The skill warns before the deadline passes, when a deadline is named. |

### `setup`

**Applies to**: the firm-setup skills (`/hf-start`, `/business-plan`,
`/policy-author`, `/accountability-map`, `/registration-readiness`,
`/vendor-selection`, `/fund-launch-checklist`).

| ID | Check | Pass rule |
|---|---|---|
| **SU1 — Stage exit criteria checked** | The skill checks the current setup stage's (S1-S8) exit criteria before it recommends an advance. | The check reads `ORG-BLUEPRINT.md` §11.1's exit-criteria column for the current stage. |
| **SU2 — No auto-advance of `project.stage`** | The skill asks "May I write" before it writes `project.stage`. | Same rule as G5 (Section 4.1), applied to a setup-stage skill specifically. |
| **SU3 — Counsel flag present** | A setup skill that touches a registration or a filing requirement states the "not legal advice, get counsel" rule. | The stated rule matches `PLAN.md` §3.2's wording or its substance. |
| **SU4 — Human-required role check** | A setup skill checks that the three investment-staff seats and the compliance-officer seat name real people. | The check fails, or reads NOT ASSESSED, when a seat lists an agent instead of a person (design-spec F-10; AAA-08). |
| **SU5 — GAP surfaced, not invented** | When a setup step's chunk gives no procedure detail, the skill states GAP and routes to counsel. | Compare against `ORG-BLUEPRINT.md` §13's gap list; the skill does not invent a procedure for a listed gap. |

## 6. Certification procedure

Run these steps in order, from a draft to an AAA grade. Steps 2 to 4
check AAA-01 to AAA-03 and reach grade A. Step 5 checks AAA-04 and, in
the same pass, AAA-05 to AAA-08, to reach grade AA. Steps 6 to 10 check
AAA-09 to AAA-14 and reach grade AAA.

1. **Draft the component.** Write the skill, agent, gate, hook, or
   template file.
2. **Run the static check.** Run `/skill-test static [name]`. Fix every
   FAIL before you continue. (AAA-01)
3. **Run the category check.** Run `/skill-test category [name]` against
   the matching category. Use a hedge-fund category from Section 5, or a
   kept CCGS category from Section 4.1. Fix every FAIL. (AAA-02)
4. **Write and run the behavior spec.** Write the 5-case spec file. Run
   `/skill-test spec [name]`. Fix every FAIL, PARTIAL, and NOT ASSESSED
   case. (AAA-03)
5. **Run the facts check.** List every regulatory or market value. Check
   each citation, as-of date, and volatility grade. Add a re-verify note
   to a medium- or high-volatility value. In the same pass, run the
   AAA-05 checklist (Section 4.2). Confirm the single verdict vocabulary
   (AAA-06). Confirm control independence (AAA-07). Confirm the human
   boundary (AAA-08).
6. **Run the failing-gate test.** Break the thing the component guards.
   Confirm the check fails or blocks. Restore the broken state. Make one
   mutation per tool call. (AAA-09)
7. **Get an independent review.** Spawn a different agent to pre-screen
   the component. Hash the file with `review-receipts.sh hash`. Record
   the hash. (AAA-10, first half)
8. **Get the founder's sign-off.** Give the founder the pre-screen
   result. Record the founder's decision as a DEC-NN entry or an approval
   receipt. Do not treat the pre-screen alone as sign-off (design-spec
   F-09). (AAA-10, second half)
9. **Run the component in the P7 dry run.** Confirm the component
   completes its part with no manual patch. Take a screenshot or a log.
   Store it in `production/qa/evidence/`. (AAA-11)
10. **Record the certification.** Copy the Section 7 template. Fill
    every AAA-01 to AAA-14 row. Update `catalog.yaml`'s `last_static`,
    `last_category`, and `last_spec` fields. State the grade awarded.
    (This step also checks AAA-12, AAA-13, and AAA-14. Run the language
    check on the file itself. Name the benchmark principle for a
    control-related component. Do this before you record the grade.)

A component that stops before step 10 has no certification, whatever
grade its last completed step reached. Record a partial result as NOT
ASSESSED for every step it has not yet run. Never record a pass by
omission.

## 7. Certification record template

Copy this block into `docs/hedge-fund-transition/certification/[type]/[name].md`.
This path is a new convention this document sets. It is separate from
`docs/hedge-fund-transition/evidence/`. That folder is a frozen snapshot
of the planning analysis (`evidence/README.md`), not a place for ongoing
certification records.

```markdown
# Certification Record — [component name]

| Field | Value |
|---|---|
| Component | [name] |
| Type | agent / skill / gate / hook / template / doc |
| Category | [CCGS category kept, or control / investment / reporting / setup] |
| Grade sought | A / AA / AAA |
| Author | [name or agent id] |
| Date started | [date] |
| Date certified | [date, or blank] |

## Step log

| Step | Result | Evidence path | Date |
|---|---|---|---|
| 1. Draft | | | |
| 2. Static (AAA-01) | | | |
| 3. Category (AAA-02) | | | |
| 4. Spec (AAA-03) | | | |
| 5. Facts check (AAA-04) | | | |
| 5. NOT ASSESSED discipline (AAA-05) | | | |
| 5. Verdict vocabulary (AAA-06) | | | |
| 5. Control independence (AAA-07) | | | |
| 5. Human boundary (AAA-08) | | | |
| 6. Failing-gate test (AAA-09) | | | |
| 7. Independent review (AAA-10a) | | | |
| 8. Founder sign-off (AAA-10b) | | | |
| 9. Dry-run participation (AAA-11) | | | |
| 10. Language check (AAA-12) | | | |
| 10. Benchmark trace (AAA-13) | | | |
| 10. Audit trail (AAA-14) | | | |

## Sign-off

| Role | Name | Date | Receipt |
|---|---|---|---|
| Author | | | |
| Independent reviewer (pre-screen only — design-spec F-09) | | | |
| Founder | | | |

## Grade awarded

[A / AA / AAA / NOT ASSESSED, with the reason for any grade below AAA]
```

## 8. Mapping to the Skill Testing Framework

Four files register the same set of names: `catalog.yaml`,
`quality-rubric.md`, `CCGS Skill Testing Framework/CLAUDE.md`, and
`CCGS Skill Testing Framework/README.md` (design-spec F-13). A direct
read of `catalog.yaml` confirms the count: 123 `name:` entries — 74
skill entries before the `agents:` line at `catalog.yaml`:822, then 49
agent entries. Two skill entries already carry an empty `spec:` field:
`catalog.yaml`:150 and `catalog.yaml`:812 — `vertical-slice` and
`settings`. Do not repeat this gap for a new hedge-fund entry.

### 8.1 What changes in each file

| File | What changes | Current location of the two name lists |
|---|---|---|
| `catalog.yaml` | Rewrite the 74 skill `name:` / `spec:` pairs and the 49 agent `name:` / `spec:` pairs to the hedge-fund names. Add the `control`, `investment`, `reporting`, and `setup` category values (Section 5) to the `category:` field of the matching entries. | 74 skill entries, `catalog.yaml`:3-821; 49 agent entries, `catalog.yaml`:822-1123. |
| `quality-rubric.md` | Add four new `###` sections — `control`, `investment`, `reporting`, `setup` — in the style of Section 5. Rewrite the `**Skills**:` and `**Agents**:` name lists for every kept category to the hedge-fund names. | `**Skills**:` / `**Agents**:` lines under each of the 9 skill and 6 usable agent `###` headers (Section 4.1 lists the exact lines quoted from this file). |
| `CCGS Skill Testing Framework/CLAUDE.md` | Rewrite the "Skill categories" ASCII table and the "Agent tiers" ASCII table to the hedge-fund names. | `CLAUDE.md`:28-46 (skill categories); `CLAUDE.md`:48-68 (agent tiers). |
| `CCGS Skill Testing Framework/README.md` | Rewrite the "Skill categories" markdown table and the "Agent tiers" markdown table to the hedge-fund names. | `README.md`:111-121 (skill categories); `README.md`:125-136 (agent tiers). |

### 8.2 The lockstep rule

Rewrite all four files in the same change, in this order:

1. `catalog.yaml` first. It is the only file `/skill-test spec` and
   `/skill-test category` read to resolve a name to a path
   (`skill-test/SKILL.md`:179-181, 268-269). A category or a spec lookup
   with no `catalog.yaml` entry fails before it reaches
   `quality-rubric.md` or a spec file at all.
2. `quality-rubric.md` second. Reuse the same names `catalog.yaml` just
   added.
3. `CLAUDE.md` and `README.md` third, to mirror the tables. A person or
   an agent reads these two files to orient to the framework, not
   `/skill-test` itself. They can safely follow the first two files.

A rewrite might skip a file, or leave a stale name in one of the four.
Each failure mode is different. `/skill-test audit` then reports that
every new hedge-fund skill has no spec. `/skill-test spec` then has no
catalog entry to resolve a path from. `/skill-test category` then has no
matching `quality-rubric.md` section for a category the founder
introduced (assess-compact.md, DELIVERABLE 4, silent_breaks). This is
the SB-13 break from design-spec, restated here with the exact file and
line ranges.

### 8.3 A drift already found between two of the four files

A direct read of both files during this task found a live version of the
exact failure Section 8.2 warns against. This failure sits inside the
current CCGS Skill Testing Framework itself:

- `README.md`:28-34 states: "Earlier revisions of this file called the
  folder 'optional' and said 'nothing in `.claude/` depends on it.' That
  was wrong — `/skill-test` references this directory 16 times and
  `/skill-improve` once."
- `CLAUDE.md`:90-94 still states the corrected-away claim: "This folder
  is deletable... Nothing in `.claude/` imports from here."

`README.md` names its own earlier claim wrong and keeps the correction.
`CLAUDE.md` carries the same wrong claim today, uncorrected. This is a
live instance of design-spec SB-13 (the four-registry drift), found by
direct comparison, not inferred from the design spec.

The P9 rewrite (`PLAN.md` Phase P9, task 2) rewrites these four files for
the hedge-fund names. Fix this drift in the same change. `CLAUDE.md`'s
"This folder is deletable" section must match `README.md`'s corrected
claim. Or it must state, for a regulated organization, that removal of
the Skill Testing Framework is a real trade against `/skill-test
category`. That command checks CT1 to CT5, IV1 to IV5, RP1 to RP5, and
SU1 to SU5. Removal is not a free cleanup.

## 9. Language quality

### 9.1 STE checks for AAA-12 (English documents)

`.claude/scripts/ste-lint.sh` (design-spec §7, Phase P3 output) runs
these checks. It is observation-only — it prints a finding per line; it
never prints PASS or FAIL itself (`CLAUDE.md`:75). AAA-12's own pass
condition (Section 4) is what turns 0 findings, or a documented
exception, into a PASS.

1. **Procedural sentence length.** Flag a numbered-step or imperative
   sentence over 20 words.
2. **Descriptive sentence length.** Flag a non-step sentence over 25
   words.
3. **Passive voice.** Flag an "is/are/was/were + past participle"
   pattern outside a fixed technical name.
4. **-ing form as a main verb.** Flag a gerund or a participle opening a
   clause (for example "Using…", "Running…"), outside a technical name.
5. **More than one instruction per sentence.** Flag two or more
   imperative verbs joined by "and" or "then" in one procedural sentence.
6. **Banned-verb list.** Flag `ensure`, `provide`, `utilize`, `perform`,
   `prior to`, `in order to`, `obtain`, `determine`, `indicate`, and
   `require`. Report the substitution from this table.

   | Banned word | Use instead |
   |---|---|
   | `ensure` | `make sure` |
   | `provide` | `give` |
   | `utilize` | `use` |
   | `perform` | `do` |
   | `prior to` | `before` |
   | `in order to` | `to` |
   | `obtain` | `get` |
   | `determine` | `find` |
   | `indicate` | `show` |
   | `require` | "it is necessary to" or "must" |
7. **Paragraph length.** Flag a paragraph over 6 sentences.
8. **Warning form.** Flag a warning or a caution sentence that does not
   open with the instruction. Example: the sentence does not start with
   "Do not" or an imperative verb.
9. **Article omission.** Flag a run of noun phrases with no article.
   Flag it when the same noun took an article earlier in the sentence or
   the paragraph. Report this check as WARN-level; it is a heuristic, not
   an exact match.
10. **Non-simple tense.** Flag a future-perfect, past-perfect, or
    conditional-chain verb form outside a quoted source.

### 9.2 Korean style checks (regulatory and investor documents)

The founder has not yet answered Q29 (document language policy;
`question-spec.md` R8). This checklist is **INFERENCE** — a provisional
design placeholder built from general plain-Korean legal-writing
practice, not from a chunk or a repository file. Mark every check below
INFERENCE until the founder answers Q29. Build a companion
Korean-language script in Phase P3, alongside `ste-lint.sh`.

1. **문장 길이 (Sentence length).** Flag a sentence over about 60
   syllables, the rough Korean equivalent of the STE 20/25-word caps.
2. **한 문장 한 지시 (One instruction per sentence).** Flag two or more
   imperative clauses (Korean imperative or "-하십시오/-합니다" form)
   joined in one sentence.
3. **존댓말 일관성 (Consistent formal register).** Flag a document that
   mixes the formal register (합니다체) with a casual ending.
4. **이중 부정 금지 (No double negatives).** Flag a "-하지 않을 수 없다"
   construction or its equivalent.
5. **법률 용어 최초 등장 시 국문 병기 (First-use Korean gloss for a
   foreign legal term).** Flag a foreign-language legal term with no
   Korean gloss on its first use. This check mirrors this document's own
   rule for a Korean term in an English document.
6. **수치·날짜 표기 통일 (Consistent numeral and date format).** Flag a
   document that mixes 한글 numerals and Arabic numerals for the same
   value type. Also flag a cited figure with no 기준일 (as-of date). This
   reuses AAA-04 for a Korean document.
7. **번역투 금지 (No translationese).** Flag a literal English-syntax
   calque. Examples: "-에 있어서," or a passive "-되어지다" form.
   Plain-Korean drafting guides flag these forms.

## Appendix: ID index

- **AAA-NN** — a criterion in Section 4 (AAA-01 to AAA-14).
- **CT/IV/RP/SU-N** — a metric in a new hedge-fund rubric category
  (Section 5): control, investment, reporting, setup.
- **G/R/A/RD/P/AN/T/SP/U-N** (skill) and **D/L/S/E/Q/O-N** (agent) — a
  metric quoted from the existing CCGS `quality-rubric.md` (Section 4.1).
