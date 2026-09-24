# Advisor design spec — T2 hedge-fund transition (Strategy C)

Status: authoritative input for the document writers. Do not change decisions here.
Date: 2026-09-24. Baseline: CCGS v1.1.1 (commit 7ed2c3e). Branch: claude/kind-dijkstra-idznze.

## 0. User requirements (trace every requirement in PLAN.md Appendix A)
- UR-01 Build the best hedge-fund organization.
- UR-02 Use the standard hedge-fund org structure; staff it with AAA-or-better members (agents).
- UR-03 Use transition strategy C (transplant operating foundation only).
- UR-04 Decide the agents and skills to build through discussion with the founder (the user).
- UR-05 Ask the founder detailed questions.
- UR-06 Give 4-5 options per question.
- UR-07 Use hedge_fund_setup_report.md as the base frame for the org.
- UR-08 Split the report into optimal chunks before use.
- UR-09 Keep AAA quality or better.
- UR-10 Base every claim on facts and verify it.
- UR-11 Write technical documents in ASD-STE100.

## 1. Facts baseline (all verified; cite these)
F-01 Review T2 = knowledge-service org (agency/consulting). T2 reuse 96/232 = 41.4% (lines 32.4%). Strategy C recommended. Estimate 253-703 h. Source: docs/org-migration-review/README.md, index.html.
F-02 A hedge fund is NOT the review's T2. Domain content is close to T2 (game content mostly LEAVE). Governance and process are close to T1 (decision records, traceability, change control, gates). Hedge-fund verdict counts over the same 232 components (this assessment):
  | area | TAKE | TAKE-MODIFY | CONDITIONAL | LEAVE | total |
  | agents | 0 | 6 | 14 | 29 | 49 |
  | skills | 8 | 19 | 27 | 20 | 74 |
  | templates | 6 | 13 | 16 | 11 | 46 |
  | director gates | 0 | 10 | 9 | 9 | 28 |
  | hooks + yaml-helper | 7 | 6 | 1 | 0 | 14 |
  | scripts | 4 | 2 | 0 | 2 | 8 |
  | rules | 3 | 3 | 2 | 5 | 13 |
  | total | 28 | 59 | 69 | 76 | 232 |
  Unconditional reuse (TAKE + TAKE-MODIFY) = 87/232 = 37.5%. Upper bound (all CONDITIONAL resolved to take) = 156/232 = 67.2%. T1 = 70.3%, T2 = 41.4%.
  The largest single driver of CONDITIONAL items is the founder decision "code/model pipeline yes or no" (Q25).
F-03 CCGS gates are advisory. Evidence: .claude/docs/workflow-catalog.yaml:16-18 ("verdicts are ADVISORY ... never hard-block"); .claude/docs/effects-map.md:1230-1245 (strict_gate_checks "RESERVED - NOT IMPLEMENTED ... No skill or hook reads this setting"); director-gates.md:127-135 blocking is a prose instruction only.
F-04 Default review_mode is lean: per-skill gates are skipped. Evidence: .claude/docs/director-gates.md:75.
F-05 team.size=individual (default) collapses non-core agents into the nearest core agent. Evidence: .claude/skills/team-combat/SKILL.md:40-44 (same pattern in all team-* skills).
F-06 gate-check panel width scales 1-4 directors by modes.workflow. Evidence: .claude/skills/gate-check/SKILL.md:385-400.
F-07 The 28 director-gate files use 9 different verdict vocabularies (director-gates.md:123-135 claims 3). AD-CONCEPT-VISUAL has no blocking tier.
F-08 Harness-enforced mechanisms that exist: (a) PreToolUse hooks can refuse a tool call with exit 2 (.claude/hooks/validate-commit.sh:145); (b) tools: Agent(...) allow-lists (godot-specialist.md:4, unity-specialist.md:4, unreal-specialist.md:4); (c) settings.json permissions deny rules. Everything else is prose.
F-09 A subagent in the same session is not an independent reviewer for segregation of duties. It is a pre-screen. A human with an independent reporting line must sign.
F-10 Law requires real people: 3 full-time investment professionals (시행령 제271조의2; HF-REF-05 표 4-1), a compliance officer (준법감시인) who cannot do asset management (HF-REF-06 §4.5), qualified officers (지배구조법 제5조; HF-REF-05 표 4-1). Agents support these roles. Agents never hold them.
F-11 project.stage is one scalar. /help maps it with a hardcoded 7-row table (.claude/skills/help/SKILL.md:70-77). Two concurrent tracks need a new track dimension plus /help and /gate-check changes.
F-12 Skill model: frontmatter is declared but not applied; agent model: is unverified (.claude/docs/model-tiers.md:3-21; coordination-rules.md).
F-13 The Skill Testing Framework registers 74 skills + 49 agents = 123 names in catalog.yaml, and names also appear in quality-rubric.md, its CLAUDE.md and README.md. All four must change in lockstep.
F-14 This environment has an OpenDART MCP connection (Korean corporate disclosures). It is a data source option.
F-15 UPGRADING.md offers upgrade strategies A (merge), A2 (selective checkout, no shared history), B (cherry-pick), C (manual copy). Keeping foundation file paths identical keeps A2/B usable from a new repo. Do not confuse UPGRADING "Strategy C" with the review's Strategy C.
F-16 Report chunks: 21 chunks, docs/hedge-fund-setup/ref/, byte-exact reassembly verified (sha256 73dcac96...7dc5a).

## 2. Silent-break checklist (review 13 + new; all must be tests in Phase 3)
From review (still valid; line numbers re-verified): SB-01 validate-commit.sh:175 design/gdd filter; SB-02 detect-gaps.sh:70-72 concept path; SB-03 detect-gaps.sh:275-282 doc naming; SB-04 pre-compact.sh:144 glob; SB-05 review-scope.sh:34 + gdd-structure-check.sh:37-55; SB-06 yaml-helper.sh:1236-1239 code root; SB-07 yaml-helper.sh:472 engine enum (loud); SB-08 validate-assets.sh:68 assets path; SB-09 statusline.sh:60-136 stage auto-detect; SB-10 workflow-catalog.yaml + artifact-check.sh paths; SB-11 CONTRACT.md vs SKILL.md drift; SB-12 tools: Agent(...) lists (loud); SB-13 Skill Testing Framework registries (loud for audit/spec).
New (this assessment): SB-14 yaml-helper.sh:473 project.stage enum rejects new stage names silently (fall-through at :843-846, :1149-1151). SB-15 detect-gaps.sh:41-116 FRESH_PROJECT never clears (engine.name, concept path, code extensions). SB-16 session-start.sh:272-285 engine-reference check becomes dead code. SB-17 strict_gate_checks looks configured but does nothing. SB-18 gate verdict parser keyed to "REJECT" misses 8 other vocabularies. SB-19 review_mode=lean skips per-skill control gates. SB-20 team.size=individual collapses CRO/CCO. SB-21 gate-check panel scaling drops control seats at workflow=minimal. SB-22 /help hardcoded stage table (help/SKILL.md:70-77). SB-23 coding-standards.md evidence table has no model/compliance row (no default gate level). SB-24 Config/Data evidence ADVISORY default in 3 skills must change together. SB-25 story-type taxonomy shared by 7 skills must change together. SB-26 tech-debt priority formula has no deadline term (tech-debt/SKILL.md:114). SB-27 design-review freshness skip hashes prose only, not referenced data. SB-28 policy gate without "policy file absent" branch passes by default (team-live-ops donor).

## 3. Target organization (standard roster; design decision)
Principles: follow HF-REF-08 표 6-1 functions; CRO and CCO lines independent of CIO (HF-REF-08 §6.2 핵심); stage activation per 표 6-2; archetype variants per 표 6-3.
Governance (human only): board and auditor; founder; investment committee members (humans vote).
Tier 1 leadership (stage 1): ceo-office (supports CEO; donor producer), cio (supports CIO; donor creative-director protocol shape only), cro (supports CRO; reports to CEO or board), cco (supports 준법감시인; reports to CEO or board), coo (supports COO/CFO; donor producer).
Tier 2 leads: portfolio-manager (stage 1), fund-operations-lead (stage 1), head-of-research (stage 2), head-of-trading (stage 2), investor-relations-lead (stage 2), technology-lead (stage 2; donor technical-director), legal-counsel-liaison (stage 2; external law firm interface), risk-analytics-lead (stage 3, under cro), quant-research-lead (CONDITIONAL quant; stage 1 if quant), model-governance-lead (CONDITIONAL quant; reports to cro, never to research; stage 1 if quant).
Tier 3 specialists: research-analyst (stage 1; instances per Q11), trader (stage 1; execution support only, never sends orders), investor-relations (stage 1; donor community-manager discipline), risk-analyst (stage 2, under cro), compliance-analyst (stage 2, under cco), regulatory-reporting-specialist (stage 2, under cco), operations-analyst (stage 2), fund-accountant (stage 2; shadow NAV, fee calc), investor-communications-writer (stage 2; donor writer), security-officer (stage 2; donor security-engineer), governance-secretary (stage 3; board/IC minutes, succession), quant-researcher (CONDITIONAL quant), data-engineer (CONDITIONAL code pipeline, stage 2), valuation-analyst (CONDITIONAL non-marketable assets, stage 2), macro-economist (CONDITIONAL macro), pod roles + capital-allocation support (CONDITIONAL multi-manager, stage 3).
Counts: stage-1 core = 10 agents (ceo-office, cio, cro, cco, coo, portfolio-manager, fund-operations-lead, research-analyst, trader, investor-relations) + 0-3 archetype agents = 10-13. Stage 2 adds 12 core (5 Tier 2: head-of-research, head-of-trading, investor-relations-lead, technology-lead, legal-counsel-liaison; 7 Tier 3: risk-analyst, compliance-analyst, regulatory-reporting-specialist, operations-analyst, fund-accountant, investor-communications-writer, security-officer) + 0-2 conditional (data-engineer, valuation-analyst) = 22-27. Stage 3 adds 2 core (risk-analytics-lead, governance-secretary) + 0-2 multi-manager conditional = 24-31.
Delegation rules: front-office agents cannot spawn or edit control agents (tools: Agent allow-lists exclude cro, cco, and their reports). Control reviews are invoked by skills, not by the agent under review. New coordination rule: no agent may override, edit, or suppress a cro or cco verdict; only the founder or board can accept a documented exception.
Prohibited for all agents: send orders; sign filings or contracts; final NAV; final compliance approval; final limit approval; investor promises; legal advice.

## 4. Lifecycle design (recommended option of Q17)
One stage axis: setup stages S1-S8 (HF-REF-05 표 4-2: 사업 설계, 법인 설립, 인력·규정, 전산·설비, 사전 협의, 등록 신청·심사, 협회 가입·인력 등록, 첫 펀드 설정) then growth stages G1-G3 (HF-REF-08 표 6-2). The investment cycle (HF-REF-09 §7.1: idea -> analysis -> portfolio -> pre-check -> execution -> monitoring -> post-review) is a repeatable per-idea process, like a story, not a stage. This keeps project.stage a single scalar, so /help and /gate-check need a table change only, not a track dimension. Exit criteria per stage come from HF-REF-18 표 10-1.

## 5. Control model (design)
- One verdict vocabulary for all gates: PASS / CONCERNS / FAIL / NOT ASSESSED, precedence FAIL > CONCERNS > NOT ASSESSED > PASS (donor gate-check/SKILL.md:481-552).
- Control seats (cro, cco) are fixed seats. They do not scale with modes.workflow, modes.review_mode, or team.size (answer depends on Q14; recommended A).
- Hard enforcement uses hooks, not prose: a PreToolUse hook refuses Write/Edit on protected paths (for example config/risk/**, policies/**, investor/outgoing/**) unless a matching approval receipt exists (review-receipts.sh content hash + approver role). Stage advancement also needs the receipt. (Recommended option of Q13.) Agents do not trade (Q26), so there is no order tool to guard in this repo.
- Regulatory value registry with as_of and effective dates (donor consistency-check).
- NOT ASSESSED discipline everywhere (.claude/rules/skill-authoring.md obligations 1-5).
- Every agent review is labeled "pre-screen"; the human sign-off is the control record (F-09).

## 6. New skill catalog (candidates; priority set by Q22 and Q23)
Setup: /hf-start (donor start), /business-plan (donor design-system + economy-model; HF-REF-13), /policy-author (donor design-system; policy set of HF-REF-18 표 10-1), /accountability-map (책무구조도; HF-REF-06 §4.5), /registration-readiness (donor gate-check + adopt; HF-REF-05 표 4-1, HF-REF-18), /vendor-selection (donor setup-engine guided selection; HF-REF-10 표 7-3), /fund-launch-checklist (donor launch-checklist; HF-REF-06 표 4-3).
Investment cycle: /idea-screen, /investment-memo (donor design-system section cycle), /ic-review (donor design-review + team-live-ops policy gate), /pre-trade-check (record for humans; donor balance-check), /risk-report (limits, stress, liquidity, crowding; HF-REF-09 표 7-1, HF-REF-14 §8.4), /post-trade-review (donor post-mortem + playtest-report routing), /strategy-pilot (donor prototype; PROCEED/PIVOT/KILL), /cycle-dry-run (donor vertical-slice).
Control and reporting: /regulatory-calendar (HF-REF-06 표 4-3, HF-REF-05 §4.1), /limit-registry (donor consistency-check), /personal-trading-log, /incident-log (donor incident-response + bug-report), /control-gap-register (donor tech-debt; add deadline term), /nav-check (shadow NAV; HF-REF-10 §7.4), /fee-calc (HWM, hurdle; HF-REF-11 표 7-4), /refresh-facts (re-verify medium/high volatility chunks).
IR: /ddq-response (HF-REF-11 §7.7), /monthly-report, /investor-letter (donor writer + community-manager no-unverified-claims rule).
Quant (CONDITIONAL Q25=C/D): /model-change (donor architecture-decision), /model-review (donor code-review), /backtest-evidence (donor story-done + test-evidence), plus the pipeline skills in TRANSPLANT-MANIFEST.
Transplanted management skills keep their names: sprint-plan, sprint-status, retrospective, scope-check, settings, skill-test, skill-improve, milestone-review, estimate, help, onboard, gate-check, adopt, project-stage-detect, consistency-check, quick-design, bug-triage, bug-report, hotfix, tech-debt (renamed register), changelog, day-one-patch.

## 7. Work breakdown (phases; estimates are ranges, method: review conversion S 0.25-0.5 h, M 1-3 h, L 3-8 h)
P0 Baseline and reference prep — DONE in this change. Chunks, source map, assessments, plan set.
P1 Founder decisions — 9 rounds, 36 questions (QUESTIONS.md). Output: answered register, decision log DEC-NN, term map. 4-8 h (founder 2-4 h).
P2 Target design — finalize roster, lifecycle catalog draft, control model, config schema (new keys: archetype, jurisdiction, risk.*, regulatory_calendar, controls.four_eyes, controls.protected_paths), skill priority, term map. Founder approval gate. 12-30 h.
P3 Repository bootstrap and foundation transplant — create repo (Q04), minimum transplant set, fix SB-01..SB-28 that apply, config enum and schema, settings.json, wire log-instructions.sh, statusline, detect-gaps rewrite, STE lint helper (observations only). 20-50 h.
P4 Control spine — verdict vocabulary, fixed control seats, protected-path hook + approval receipts, regulatory value registry, coordination rules rewrite (independence + non-override), Agent allow-lists, failing-gate tests. 25-60 h.
P5 Pilot and re-measure — build cro agent + /risk-report + /regulatory-calendar to the AAA bar. Measure hours. Re-estimate P6-P9. 10-25 h.
P6 Stage-1 roster and priority skills — 10-13 agents, first skill bundles, templates. 100-300 h.
P7 End-to-end dry run — one idea through the full cycle; one setup stage through its gate; evidence retained. 10-25 h.
P8 Stage-2/3 activation and conditional pipeline — remaining roster, quant pipeline if Q25=C/D. 60-200 h (conditional).
P9 Documentation, test catalog, handoff — README, onboarding, Skill Testing Framework registries and specs. 20-50 h.
Totals: core (P1-P7, P9) 201-548 h; with P8 261-748 h. Review T2 estimate was 253-703 h. At 30 h/week: core 7-18 weeks.
Each phase: entry criteria, tasks, outputs, exit criteria, owner (Advisor = main session; Worker = Sonnet/Haiku subagents; Founder).

## 8. AAA quality bar (acceptance for every agent, skill, gate, hook, template)
AAA-01 Structure: /skill-test static -> 0 FAIL (skills); agent frontmatter complete.
AAA-02 Category: /skill-test category -> COMPLIANT against new hedge-fund categories (control, investment, reporting, setup).
AAA-03 Behavior spec: 5 cases (happy path, failure/blocked, mode variant, edge case, gate) -> PASS.
AAA-04 Facts: every regulatory or market value cites HF-REF-NN §x.y (or SRC-NN) and shows as_of; medium/high volatility values carry a re-verify note.
AAA-05 NOT ASSESSED discipline: skill-authoring.md obligations 1-5; absent input never gives PASS.
AAA-06 One verdict vocabulary.
AAA-07 Control independence: fixed cro/cco seats; allow-lists; non-override rule.
AAA-08 Human boundary: prohibited actions listed; human-required roles never assigned to an agent.
AAA-09 Failing-gate test: break the guarded thing, confirm the check fails, restore (skill-authoring.md closing rule).
AAA-10 Independent review: a different agent plus the founder review each artifact; receipt recorded (review-receipts.sh).
AAA-11 Scenario: the component works in the P7 dry run without manual patching.
AAA-12 Language: technical docs pass ASD-STE100 checks (sentence length 20 procedural / 25 descriptive, active voice, simple tenses, no -ing forms except technical names, one instruction per sentence); regulatory and investor documents in Korean follow the Korean style rules.
AAA-13 Benchmark trace: control-related components trace to HF-REF-17 표 9-5 principles.
AAA-14 Audit trail: actions logged (log-agent.sh, session-stop.sh); decisions recorded as DEC-NN.
Grades: A = AAA-01..03; AA = A + AAA-04..08; AAA = AA + AAA-09..14. Only AAA may ship.

## 9. Risks (register)
R-01 Agents treated as legal personnel. R-02 Stale regulatory values. R-03 Advisory gates skipped silently. R-04 Silent breaks during transplant. R-05 Same-session review mistaken for independent validation. R-06 Scope growth from "best org" goal (up to about 31 agents). R-07 Confidential data or MNPI in the repository. R-08 Upstream drift. R-09 Model states legal facts without source. R-10 Agent model pin unverified. R-11 Two concurrent tracks not supported. R-12 Report is not legal advice; gaps (MNPI barriers, personal-trading pre-clearance detail, cybersecurity roles, AML/KYC, BCP detail, vendor due diligence, valuation committee quorum, key-person succession, ESG/stewardship, investor privacy, fee crystallization period, model governance procedure) need counsel.
Each: likelihood, impact, mitigation, owner, phase.

## 10. Blueprint corrections from the verifier (apply)
- Personal trading GAP cites HF-REF-08 표 6-1 and HF-REF-18 표 10-1, not HF-REF-06 §4.5.
- ir-lead "IR 전담 인력" cites HF-REF-08 표 6-2 (stage 2).
- "전담 리스크팀" is stage 2 (표 6-2); stage 3 phrase is "중앙 리스크·데이터 플랫폼".
- 핵심상품설명서: 운용사 writes; 판매사 (external) verifies (HF-REF-06 표 4-3). Internal CCO review is INFERENCE.
- Model change control approval: CCO/CRO (HF-REF-12 §7.8 says include in compliance rules). Quant lead gives technical input only, no approval (INFERENCE).
- Macro CIO doubling as economist is INFERENCE.
- Add controls: investor count 100 / 49 (HF-REF-06 표 4-3), 15-year disposal of 경영참여 investments, transfer restriction to non-qualified investors, investment advertising restriction, external audit duty, securities-lending tenor 90 days / 12 months max (HF-REF-06 표 4-4), deferred performance pay applicability check (HF-REF-08 §6.5).
- Add recurring artifact: external audit report (cadence GAP).
