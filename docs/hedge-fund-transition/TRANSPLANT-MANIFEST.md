# HFT-MAN-001 — Component-Level Transplant Manifest for Strategy C

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-MAN-001 |
| Title | Component-Level Transplant Manifest for Strategy C |
| Version | 0.2 |
| Date | 2026-09-24 |
| Status | Draft for founder review |
| Owner | Advisor (main session) |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules. Checked manually in v0.1; the STE lint helper is a P3 deliverable. |
| Working files | The names design-spec, question-spec, wf1.json, assess-compact.md, orgmap.json, verifier-issues.md, review.txt, and mapping.txt refer to files in [`evidence/`](evidence/README.md). |
| Scope | Every CCGS component (agent, skill, template, director gate, hook, script, rule) with a hedge-fund transplant verdict. The minimum transplant set. The 28-item silent-break checklist. The lockstep change sets. |

This document is not legal advice. It is not tax advice. It is not
investment advice. Do not rely on any control point or legal citation
in this document. Get advice first. Ask the Financial Supervisory
Service (FSS), a law firm, and an accounting firm.

This document uses facts from the report chunks in
`docs/hedge-fund-setup/ref/` (HF-REF-00 to HF-REF-20), from the CCGS
component assessment (`wf1.json`), and from the verifier corrections
(`verifier-issues.md`). Every number matches its source. A statement
that extends a cited fact, not a direct quote, is marked INFERENCE.
Missing coverage is marked GAP.

**Change history**

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-24 | Initial draft. |
| 0.2 | 2026-09-24 | Added Section 9, the effect of founder decisions DEC-01 to DEC-16 and the mission reset (DEC-09), from [design-addendum-01.md](evidence/design-addendum-01.md). §3's verdict counts do not change. |

## 2. Verdict definitions

This manifest uses 4 verdicts for every component. It also uses 2
source-verdict labels from the original review.

**TAKE.** Transplant the file with no content change. Rename only
where a path or a cross-reference needs it.

**TAKE-MODIFY.** Transplant the mechanism. Rewrite the domain content.
The “Required changes” column names what to rewrite.

**CONDITIONAL.** The verdict depends on a founder decision. The
“Condition (Q-ID)” column names the question. Read
`QUESTIONS.md` for the question text and options. Where a component
does not map to one question ID, this manifest marks the cell GAP (no
Q-ID assigned) and states the decision it depends on instead.

**LEAVE.** Do not transplant the file. The file may still have a
“donor” value. The “Donor / HF use” column states this value, if
any. An example is a shape or a pattern worth copying, without the
content.

**T2 verdict** is the original review’s verdict for the same file
under Strategy T2, the knowledge-service and marketing-agency target.
T2 uses its own letter codes: K (keep as-is), W (rewrite content,
keep mechanism), R (redesign), D (delete, no counterpart). This
manifest carries the T2 verdict for comparison only. It does not
change the T2 verdict.

**INFERENCE** marks a claim in this manifest that extends a cited
fact rather than quoting it. **GAP** marks a claim this manifest
cannot support from the loaded material.

## 3. Summary counts

Table 3-1 is the Advisor’s verdict count table from design-spec F-02.
This manifest treats it as final. This manifest does not edit it.

**Table 3-1. F-02 verdict counts (authoritative)**

| Area | TAKE | TAKE-MODIFY | CONDITIONAL | LEAVE | Total |
|---|---|---|---|---|---|
| agents | 0 | 6 | 14 | 29 | 49 |
| skills | 8 | 19 | 27 | 20 | 74 |
| templates | 6 | 13 | 16 | 11 | 46 |
| director gates | 0 | 10 | 9 | 9 | 28 |
| hooks + yaml-helper | 7 | 6 | 1 | 0 | 14 |
| scripts | 4 | 2 | 0 | 2 | 8 |
| rules | 3 | 3 | 2 | 5 | 13 |
| **total** | **28** | **59** | **69** | **76** | **232** |

Unconditional reuse (TAKE + TAKE-MODIFY) = 87 / 232 = 37.5%. Upper
bound, all CONDITIONAL resolved to take = 156 / 232 = 67.2%.

**Table 3-2. Row count check**

This manifest built one row per file in §5, applied the Advisor
overrides in §8, and counted the rows per area and per verdict.
Table 3-2 states the result of that count.

| Area | TAKE | TAKE-MODIFY | CONDITIONAL | LEAVE | Total | Matches F-02 |
|---|---|---|---|---|---|---|
| agents | 0 | 6 | 14 | 29 | 49 | YES |
| skills | 8 | 19 | 27 | 20 | 74 | YES |
| templates | 6 | 13 | 16 | 11 | 46 | YES |
| director gates | 0 | 10 | 9 | 9 | 28 | YES |
| hooks + yaml-helper | 7 | 6 | 1 | 0 | 14 | YES |
| scripts | 4 | 2 | 0 | 2 | 8 | YES |
| rules | 3 | 3 | 2 | 5 | 13 | YES |
| **total** | **28** | **59** | **69** | **76** | **232** | **YES** |

**Result: every row in Table 3-2 matches Table 3-1 exactly. No
difference to report.**

## 4. Minimum transplant set

This is the smallest file set that gives the new repository session
state, config resolution, gate-invocation support, audit logs, and
skill-test support. Source: the infra assessment’s MINIMUM
TRANSPLANT SET finding, with file:line dependency evidence.

**Table 4-1. Minimum transplant set, in transplant order**

| # | File / group | Purpose | Depends on | Evidence (file:line) |
|---|---|---|---|---|
| 1 | .claude/hooks/yaml-helper.sh | Core config resolver. Every other kept hook and script sources it. | Python 3 interpreter. | yaml-helper.sh:79-91 (Python dependency) |
| 1 | project.yaml (rewritten schema) | The config file yaml-helper.sh resolves. Must exist on disk. | Nothing; the schema is authored in P2. | yaml-helper.sh (reads project.yaml at every call) |
| 2 | .claude/hooks/session-start.sh | Session banner, review-mode resolution, schema validation, stage-source-agreement warning, session-state recovery preview. | yaml-helper.sh. | session-start.sh:76,93,180,210 |
| 2 | .claude/hooks/pre-compact.sh | Checkpoint-by-reference injection before compaction. | yaml-helper.sh. | pre-compact.sh:37 |
| 2 | .claude/hooks/post-compact.sh | Post-compaction reminder. | yaml-helper.sh. | post-compact.sh:36 |
| 2 | .claude/hooks/session-stop.sh | Content-hash-guarded state archive; subagent spawn-tally and cost report. | yaml-helper.sh. | session-stop.sh:36; spawn-tally block at :110-169 |
| 2 | .claude/scripts/rotate-session-state.sh | Rotates active.md’s narrative into a dated log; keeps the CHECKPOINT block; refuses safely on a malformed file. | Manual script, not a hook. | rotate-session-state.sh:47-53,97-103 |
| 2 | .claude/docs/templates/session-state.md | The CHECKPOINT/STATUS marker contract all 4 session-state hooks share. Transplant verbatim. | Nothing. | Shared contract; 100% generic. |
| 2 | .claude/docs/context-management.md | Documents the session-state and observation-vs-verdict conventions. | Nothing. | Mostly generic; prune 2-3 GDD-specific example lines. |
| 3 | .claude/hooks/validate-commit.sh | The one blocking (exit 2) hook in the repo. Scans for hardcoded values before commit. | yaml-helper.sh. | validate-commit.sh:170-172,283-286 |
| 3 | .claude/hooks/validate-push.sh | Protected-branch warning. | None — fully standalone. | validate-push.sh:37-75 (no yaml-helper.sh dependency) |
| 3 | .claude/scripts/artifact-check.sh | Reads workflow-catalog.yaml; reports PRESENT/ABSENT/SHORT/PATTERN_MISS/NO_CHECK/UNKNOWN. Never returns a verdict. | An external workflow-catalog.yaml, authored fresh in P2/P3 (out of this file’s own scope, but a real dependency). | artifact-check.sh parser loop |
| 3 | .claude/scripts/adr-dep-graph.sh | ADR-dependency graph and cycle detector. Reusable for investment-decision or model-change records. | A docs/architecture/adr-*.md naming convention; no other file dependency. | adr-dep-graph.sh:1-31,108-143 |
| 4 | .claude/hooks/log-agent.sh | Audit-trail hook: records every subagent spawn. | yaml-helper.sh. | log-agent.sh:44 |
| 4 | .claude/hooks/log-agent-stop.sh | Mirror of log-agent.sh for completion events. | yaml-helper.sh. | log-agent-stop.sh:44 |
| 4 | session-stop.sh spawn-tally block | Aggregate audit summary at session end. | Part of session-stop.sh (row above). | session-stop.sh:110-169 |
| 4 | .claude/hooks/log-instructions.sh | Records which rule/instruction file actually reached the model. Confirmed UNWIRED in source CCGS (no InstructionsLoaded entry in settings.json). | yaml-helper.sh. Must be newly wired into settings.json (§5 row 6). | log-instructions.sh:29-53; settings.json (no matching entry upstream) |
| 5 | .claude/hooks/validate-skill-change.sh | Fires on any .claude/skills/ edit; advises /skill-test. | None — no yaml-helper.sh dependency. | validate-skill-change.sh:64-77 |
| 6 | .claude/settings.json | Hook wiring, permissions allow/deny list, statusLine wiring. | Every hook/script kept above must be listed here to run at all. | settings.json:35-158 |
| 7 | .claude/statusline.sh | ctx%/model/rigor/breadcrumb display segments. Drop the game-specific stage-auto-detect block (SB-09). | yaml-helper.sh. | statusline.sh:66,94,154 |
| 7 | .claude/hooks/notify.sh | Desktop notification. Not load-bearing for any of the 4 core capabilities; pure convenience. | None. | notify.sh:59-70 |
| 8 | .claude/docs/code-root-resolution.md + .claude/hooks/validate-assets.sh | Code-root convention and structured-data-path validation. | Only needed if archetype=quant/code-pipeline=yes, or a new assets/-equivalent directory is created. | yaml-helper.sh:1206-1252; validate-assets.sh:68-70 |

**Transplant order.** Do the groups in numeric order. Each group
depends on an earlier one.

1. Core hub. Write project.yaml first. Transplant yaml-helper.sh
   second. Every other kept file sources one or both.
2. Session state. Transplant the 4 session-state hooks, the rotation
   script, and the 2 shared-contract docs together. All 4 hooks gate
   on the same session_state_enabled() check.
3. Gate-invocation support. Transplant validate-commit.sh,
   validate-push.sh, artifact-check.sh, and adr-dep-graph.sh.
   artifact-check.sh needs a workflow-catalog.yaml to read; author
   that file before or alongside this step.
4. Audit logs. Transplant log-agent.sh, log-agent-stop.sh, and
   log-instructions.sh together. Wire log-instructions.sh into
   settings.json in this same step; it does nothing until wired.
5. Skill-test support. Transplant validate-skill-change.sh.
6. Wiring. Rewrite settings.json last, after every file above is in
   place, so its hook-command list matches exactly what was kept.
7. Optional UI. Transplant statusline.sh and notify.sh. Neither
   blocks any of the 4 core capabilities.
8. Conditional. Transplant code-root-resolution.md and
   validate-assets.sh only if Q25 resolves to C or D, or a new
   structured-data directory is created.

**Explicitly not in the minimum set.**
- detect-gaps.sh. Onboarding-gap UX only, not core. See SB-15.
- migrate-v1-config.sh. No v1.0 CCGS predecessor exists under
  Strategy C.
- project-coherence.sh. Godot/Unity/Unreal-specific. No clean
  transplant target.
- gdd-structure-check.sh and review-scope.sh. These belong to the
  domain skills the fund writes fresh in P6. Their mechanism is
  still worth reuse once those skills exist.

## 5. Component tables

Each table below covers one area. The columns are:
- Component. The file path.
- T2 verdict. The original review’s verdict for the same file.
  Letter codes K/W/R/D.
- HF verdict. This manifest’s verdict.
- Condition (Q-ID). The founder question ID a CONDITIONAL verdict
  depends on.
- Required changes. A short, imperative summary. Read the cited
  evidence for the full analysis.
- Evidence. File:line citations.
- Donor / HF use. The hedge-fund use of the file.

A grouped finding in the source assessment (for example “15 engine
agents” or “4 PHASE-GATE files”) is expanded here to one row
per file. Each expanded row inherits the group’s verdict and
evidence unless a row-specific note says otherwise. §8 lists every
place this manifest applied an Advisor override or a verifier
correction.

### 5.1 hooks + yaml-helper (14)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/hooks/session-start.sh | W | TAKE-MODIFY | — | Delete the BUG-*.md scan directories. Gate the code-health block behind archetype=quant. Redesign the engine-reference-mismatch block as a regulatory-ruleset check. | Branch/commit banner, review-mode resolution, schema validation, and the stage-agreement warning are generic and directly reusable. | .claude/hooks/session-start.sh:118-143; .claude/hooks/session-start.sh:182-194; .claude/hooks/session-start.sh:267-285 |
| .claude/hooks/detect-gaps.sh | R | TAKE-MODIFY | — | Rewrite the artifact names (game-concept.md, design/gdd/ paths, src/Assets/Source scan) for the new document set. Keep the stage-vs-artifact drift check. | The onboarding nudge and stage-vs-artifact drift check are reusable; content checks 1, 3, and 4 need full rewrite. | .claude/hooks/detect-gaps.sh:70; .claude/hooks/detect-gaps.sh:84-91; .claude/hooks/detect-gaps.sh:297-327 |
| .claude/hooks/validate-commit.sh | W | TAKE-MODIFY | — | Repoint the DATA_FILES and DESIGN_FILES globs to the new risk-config directory. Replace the hardcoded-value regex with leverage, limit, and threshold terms. | The JSON-validity block and the hardcoded-value scan (damage, health, speed) match a model-governance control for hardcoded risk parameters. | .claude/hooks/validate-commit.sh:114-150; .claude/hooks/validate-commit.sh:175-241; .claude/hooks/validate-commit.sh:243-310 |
| .claude/hooks/validate-push.sh | K | TAKE | — | Keep the file unchanged. | This is a fully generic protected-branch warning with no build or test enforcement; the block path stays commented out. | .claude/hooks/validate-push.sh:54-73 |
| .claude/hooks/validate-assets.sh | W | CONDITIONAL | Q15 (limits kept as config data) | Repoint the assets/ path filter to the new structured data directory, if the fund keeps limits as config data. Otherwise, leave the hook unused. | The naming-convention and JSON-validity checks are generic but need a structured data directory like assets/ to have any effect. | .claude/hooks/validate-assets.sh:68-70; .claude/hooks/validate-assets.sh:79-81; .claude/hooks/validate-assets.sh:85-109 |
| .claude/hooks/validate-skill-change.sh | K | TAKE | — | Keep the file unchanged. | The hook is fully generic. It fires on any skill edit and advises running /skill-test. | .claude/hooks/validate-skill-change.sh:64-77 |
| .claude/hooks/notify.sh | K | TAKE | — | Keep the file unchanged. | This is a fully generic Windows toast notification with no domain coupling. | .claude/hooks/notify.sh:59-70 |
| .claude/hooks/pre-compact.sh | W | TAKE-MODIFY | — | Repoint the design/gdd/*.md glob at line 144 to the new document directory. | Checkpoint-by-reference injection, bounded git-status lists, and compaction logging are fully generic and high value. | .claude/hooks/pre-compact.sh:61-87; .claude/hooks/pre-compact.sh:105-126; .claude/hooks/pre-compact.sh:144-156 |
| .claude/hooks/post-compact.sh | K | TAKE | — | Keep the file unchanged. | This is a fully generic reminder hook, gated on features.session_state, with no domain coupling. | .claude/hooks/post-compact.sh:44-51 |
| .claude/hooks/session-stop.sh | K | TAKE | — | Keep the file unchanged. | The content-hash-guarded state archive and the subagent spawn-cost report support the audit-trail requirement. | .claude/hooks/session-stop.sh:71-84; .claude/hooks/session-stop.sh:110-169 |
| .claude/hooks/log-agent.sh | K | TAKE | — | Keep the file unchanged. | This is a fully generic audit-trail hook for the investment-decision-record requirement. | .claude/hooks/log-agent.sh:76-79 |
| .claude/hooks/log-agent-stop.sh | K | TAKE | — | Keep the file unchanged. | This is the completion-event mirror of log-agent.sh, fully generic. | .claude/hooks/log-agent-stop.sh:76 |
| .claude/hooks/log-instructions.sh | K | TAKE-MODIFY | — | Add an InstructionsLoaded hook entry to the new settings.json that points at this script. | This generic diagnostic traces which rule or instruction file reached the model; wire it, do not leave it inert. | .claude/hooks/log-instructions.sh:29-53; .claude/settings.json:35-158 |
| .claude/hooks/yaml-helper.sh | W | TAKE-MODIFY | — | Rewrite the enum table to drop game-specific rows and add jurisdiction and archetype values. Rewrite resolve_code_root and the engine emission block. | The YAML parser, enum validator, override chain, decision-log writer, and resolve_config dispatcher are about 90 percent generic. | .claude/hooks/yaml-helper.sh:460-483; .claude/hooks/yaml-helper.sh:1135-1177; .claude/hooks/yaml-helper.sh:1206-1252 |

### 5.2 scripts (8)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/scripts/adr-dep-graph.sh | D | TAKE | — | Keep the file unchanged. | This generic ADR-dependency-graph and cycle detector supports investment-decision or model-change records. | .claude/scripts/adr-dep-graph.sh:1-31; .claude/scripts/adr-dep-graph.sh:108-143 |
| .claude/scripts/artifact-check.sh | K | TAKE | — | Keep the file unchanged. | The script body is fully generic and data-driven; only the external workflow-catalog.yaml carries domain content. | .claude/scripts/artifact-check.sh:1-16; .claude/scripts/artifact-check.sh:225-262 |
| .claude/scripts/gdd-structure-check.sh | R | TAKE-MODIFY | — | Replace the MATCH and LABEL section vocabulary and the exclusion list with the IC-memo or policy-doc section schema. | The grep-based section-presence-checker mechanism is clean and reusable; the section vocabulary is game-design content. | .claude/scripts/gdd-structure-check.sh:30-46; .claude/scripts/gdd-structure-check.sh:49-55 |
| .claude/scripts/migrate-v1-config.sh | K | LEAVE | — | Do not transplant this script. | The script migrates only CCGS's own v1.0-to-v1.1 file format; the new fund repo has no such predecessor. | .claude/scripts/migrate-v1-config.sh:3-27; .claude/scripts/migrate-v1-config.sh:490-493 |
| .claude/scripts/project-coherence.sh | D | LEAVE | — | Do not transplant this script. | All six checks compare project.yaml against Godot, Unity, or Unreal files; none has a hedge-fund target. | .claude/scripts/project-coherence.sh:79-119; .claude/scripts/project-coherence.sh:121-131; .claude/scripts/project-coherence.sh:148-191 |
| .claude/scripts/review-receipts.sh | K | TAKE | — | Keep the file unchanged. | This generic content-hash tracker of document changes maps to segregation-of-duties and independent-review requirements. | .claude/scripts/review-receipts.sh:1-30; .claude/scripts/review-receipts.sh:130-146 |
| .claude/scripts/review-scope.sh | W | TAKE-MODIFY | — | Repoint the GDD_GLOB and the not_a_system_gdd exclusion list to the new document directory and naming convention. | The mechanism finds the latest cross-review report and follows declared dependency links; it fits periodic policy-document review. | .claude/scripts/review-scope.sh:34; .claude/scripts/review-scope.sh:38-44; .claude/scripts/review-scope.sh:63-64 |
| .claude/scripts/rotate-session-state.sh | K | TAKE | — | Keep the file unchanged. | This generic script rotates active.md's narrative into a dated log and writes atomically. | .claude/scripts/rotate-session-state.sh:47-53; .claude/scripts/rotate-session-state.sh:97-103 |

### 5.3 other infrastructure files (not counted in the 232)

settings.json, statusline.sh, project.yaml, .gitignore, coordination-rules.md, director-gates.md, model-tiers.md, automation-modes.md, workflow-modes.md, context-management.md, workflow-catalog.yaml, effects-map.md, code-root-resolution.md, and the CCGS Skill Testing Framework files. These support the 232 counted components. They are not counted themselves.

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/statusline.sh | — | TAKE-MODIFY | — | Delete or rewrite the auto-detect fallback (lines 60-136) to match the new project.stage vocabulary and artifact set. | The context percentage, model, rigor posture, and stage breadcrumb are generic and high value. | .claude/statusline.sh:60-136; .claude/statusline.sh:138-175; .claude/statusline.sh:177-206 |
| .claude/settings.json | — | TAKE-MODIFY | — | List in the hooks block only the hooks kept from the per-file review. Add an InstructionsLoaded entry. Strengthen the deny list. | The permission philosophy and per-event hook wiring are generic; hook command paths carry over for every kept hook. | .claude/settings.json:7-34; .claude/settings.json:35-158 |
| project.yaml | — | TAKE | — | Add content for archetype, jurisdiction, and a risk-limit block; keep the file's single-source-of-truth shape. | The single-YAML-source-of-truth pattern and its guardrail comments are generic and worth keeping verbatim. | project.yaml:1-8; project.yaml:10-22 |
| .gitignore | — | TAKE-MODIFY | — | Remove the three engine-specific blocks (lines 49-107) and the docs/consistency-failures.md line. Keep everything else. | The Claude-Code-local section and the secrets section are the highest-value lines for a regulated entity. | .gitignore:12-23; .gitignore:49-107; .gitignore:130-137 |
| .claude/docs/coordination-rules.md | — | TAKE-MODIFY | — | Add a non-override clause for CRO and CCO output. Make them co-equal Tier-1 escalation targets alongside CIO and COO. | This is the nearest skeleton in the repo for independent control-function escalation, delegation, and change propagation. | .claude/docs/coordination-rules.md:7-9; .claude/docs/coordination-rules.md:12-13 |
| .claude/docs/director-gates.md | — | TAKE-MODIFY | — | Standardize on one verdict vocabulary. Make CRO and CCO gates independent of modes.review_mode. Do not rely on strict_gate_checks. | This is the skeleton for CIO, CRO, and CCO review gates and the phase-gate launch panel. | .claude/docs/director-gates.md:123-135; .claude/docs/director-gates.md:75 |
| .claude/docs/model-tiers.md | — | TAKE-MODIFY | — | Do not rely on the model tier for compliance guarantees until the agent-level enforcement is verified. | This is a usable model-tier assignment framework for cost and capability tiering, once verified. | .claude/docs/model-tiers.md:3-10; .claude/docs/model-tiers.md:18-21 |
| .claude/docs/automation-modes.md + docs/COLLABORATIVE-DESIGN-PRINCIPLE.md + .claude/docs/workflow-modes.md | — | TAKE-MODIFY | — | Add hedge-fund always-ask categories, such as limit changes, model deployment, and investor communication, to the current defaults. | The Question-Options-Decision-Draft-Approval sign-off discipline is the closest thing to a four-eyes control at the workflow layer. | .claude/docs/automation-modes.md:130; docs/COLLABORATIVE-DESIGN-PRINCIPLE.md:455-463 |
| .claude/docs/context-management.md | — | TAKE-MODIFY | — | Prune the GDD-specific example lines; keep the CHECKPOINT and STATUS marker contract unchanged. | The session-state checkpoint contract and the observations-not-verdicts rule are generic and load-bearing. | .claude/docs/context-management.md:12; .claude/docs/context-management.md:28-29; .claude/docs/context-management.md:131 |
| .claude/docs/effects-map.md | — | TAKE-MODIFY | — | Rewrite one section per surviving or new config key once the schema is final; drop sections for removed keys. | The document gives one section per setting, about 900 tokens each; each section names its readers. | .claude/docs/effects-map.md:5-22; .claude/docs/effects-map.md:1230-1253 |
| .claude/docs/code-root-resolution.md | — | CONDITIONAL | Q25 = C or D | Apply this procedure only if the fund creates a code or model pipeline; otherwise leave it unused. | This is the code-root resolution convention; it applies only when a code pipeline exists. | .claude/hooks/yaml-helper.sh:1206-1252 |
| .claude/docs/workflow-catalog.yaml | — | TAKE-MODIFY | — | Reuse the phases, steps, glob, pattern, and min_count schema as-is for the firm-setup track. | The phase and step schema is reusable; /help and /gate-check need edits to support two concurrent tracks. | .claude/docs/workflow-catalog.yaml:1-19; .claude/skills/help/SKILL.md:70-77; .claude/scripts/artifact-check.sh:138 |
| CCGS Skill Testing Framework/catalog.yaml | — | TAKE-MODIFY | — | Rewrite every name and spec path for the new hedge-fund skill and agent set. | The registry mechanism (spec path, priority, category, coverage fields) transplants directly for 74 skills and 49 agents. | CCGS Skill Testing Framework/catalog.yaml:1-14; CCGS Skill Testing Framework/catalog.yaml:822 |
| CCGS Skill Testing Framework/quality-rubric.md | — | TAKE-MODIFY | — | Rewrite the category name lists for hedge-fund roles; keep the RD3 and D1/D4 metrics unchanged. | RD3 and D1/D4 map directly onto compliance-hold verdicts and CRO/CCO-equivalent control-function agents. | CCGS Skill Testing Framework/quality-rubric.md:81-89; CCGS Skill Testing Framework/quality-rubric.md:186-191 |
| CCGS Skill Testing Framework/ (static/spec/category/audit modes) | — | TAKE-MODIFY | — | Transplant all four modes' mechanism. Rewrite the registry for spec, category, and audit modes; static needs no rewrite. | The README's own degrade and break table shows what happens to each mode when skill and agent names change. | CCGS Skill Testing Framework/README.md:17-21 |
| CCGS Skill Testing Framework/templates/skill-test-spec.md | — | TAKE | — | Add this component to the catalog; the behavior-spec template needs no rewrite to transplant. | This is a fully generic behavior-spec template for a new hedge-fund skill's five AAA-03 test cases. | CCGS Skill Testing Framework/templates/skill-test-spec.md:1-19 |
| CCGS Skill Testing Framework/templates/agent-test-spec.md | — | TAKE | — | Add this component to the catalog; the agent behavior-spec template needs no rewrite. | This is a fully generic agent behavior-spec template for a new hedge-fund agent's test cases. | CCGS Skill Testing Framework/templates/agent-test-spec.md:1-13 |

### 5.4 config keys (not counted in the 232)

| Config key | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| schema_version | K | TAKE | — | Keep this key unchanged. | Marks the project.yaml schema version so old files can be detected and migrated. | project.yaml:4; effects-map.md:2157-2171 |
| framework.version / last_upgraded | K | TAKE | — | Keep this key unchanged. | Records which CCGS version created or last touched the project. | project.yaml:6-8; effects-map.md:2182-2208 |
| modes.rigor | K | TAKE | — | Keep this key unchanged. | Gives one question that sets compliance and review rigor by fund stage. | .claude/hooks/yaml-helper.sh:999; effects-map.md:457-465 |
| workflow_overrides | K | TAKE | — | Keep this key unchanged. | Lets one system override the standard document-requirement rules. | .claude/hooks/yaml-helper.sh:1504-1519; effects-map.md:704-712 |
| modes.story_granularity | K | TAKE | — | Keep this key unchanged. | Sets how big each story or memo unit is, and how many make up a cycle. | effects-map.md:982-990 |
| docs.density | K | TAKE | — | Keep this key unchanged. | Sets how deep each authored document section goes. | effects-map.md:1017-1025 |
| performance.enforce | K | TAKE | — | Keep this key unchanged. | Sets whether a breached numeric threshold warns, blocks, or is off; reusable for a future risk-limit breach. | .claude/hooks/yaml-helper.sh:469; .claude/hooks/yaml-helper.sh:1451-1457 |
| features.session_state | K | TAKE | — | Keep this key unchanged. | Turns the session-checkpoint and audit-trail pipeline on or off; on by default. | .claude/hooks/yaml-helper.sh:665-676; effects-map.md:1914-1930 |
| cadence.sprint_length / milestone_length | K | TAKE | — | Keep this key unchanged. | Sets recurring cycle lengths; reusable for board or IC meeting cadence once implemented. | effects-map.md:1496-1509 |
| features.token_budget_warn_at | W | TAKE | — | Keep this key, and wire it into pre-compact.sh, session-start.sh, and statusline.sh where it is documented but not read. | Sets the context-usage percentage at which a session warns; default 0.7. | effects-map.md:2123-2139; .claude/hooks/yaml-helper.sh:528 |
| modes.review_mode (full/lean/solo) | K | TAKE-MODIFY | — | Rename the full, lean, and solo values for a control panel; keep the chain. Flag solo for restriction on control gates. | Sets how many specialist and director agents a skill spawns for review depth. | .claude/hooks/yaml-helper.sh:461,970-976; effects-map.md:326-334 |
| modes.automation (collaborative/guided/autonomous) | K | TAKE-MODIFY | — | Keep the three values. Flag autonomous for restriction on regulated actions. | Sets whether a skill asks for approval before acting, or proceeds and reports. | .claude/hooks/yaml-helper.sh:464,998; effects-map.md:772-778 |
| modes.automation_always_ask | K | TAKE-MODIFY | — | Keep the default list. Add hedge-fund categories: risk_limit_changes, trade_related_actions, client_data_access. | Names decision categories that always trigger a question, regardless of automation mode. | .claude/hooks/yaml-helper.sh:890-892; effects-map.md:940-946 |
| modes.workflow (full/standard/minimal) | K | TAKE-MODIFY | — | Keep the doc-section-count dial. Reuse the three tiers for IC-memo completeness. | Sets how much design documentation a system needs before work begins. | effects-map.md:527-534 |
| qa.level (minimal/standard/full) | K | TAKE-MODIFY | — | Rename the key to review or validation level. Keep the three tiers. | Sets what test or review evidence a story needs before it closes. | effects-map.md:1160-1169 |
| team.size (individual/small/studio) | K | TAKE-MODIFY | — | Rename the values only; the wording is cosmetic. Do not let cro or cco seats scale with this key. | Sets which agents are active by default, based on team size. | .claude/hooks/yaml-helper.sh:468,1016-1017; effects-map.md:1270-1276 |
| project.stage | W | TAKE-MODIFY | — | Keep the single authoritative-value, gate-check-only-write, and dual legacy-mirror mechanism. Replace all seven stage names with the fund's own lifecycle stages. | Tracks the current development phase; only gate-check may advance it, and only on a PASS verdict. | .claude/hooks/yaml-helper.sh:473,1057-1060,1149-1177; effects-map.md:1589-1598 |
| testing.strict.{logic,integration,visual,ui,config} | W | TAKE-MODIFY | — | Keep the per-type block-or-advisory mechanism. Redesign the five type names into a hedge-fund evidence taxonomy. | Sets whether missing or failing evidence blocks a story, per evidence type. | effects-map.md:1107-1115 |
| strict_gate_checks | K | TAKE-MODIFY | — | Keep the key. Implement it, or replace it with the protected-path hook design, before it can block a compliance failure. | Controls whether a failed gate blocks stage advancement or only warns; not yet wired to any hook. | effects-map.md:1230-1253 |
| commands.{build,test,run,smoke} | K | CONDITIONAL | Q25 = C or D | Keep the OS-aware map and fallback logic. Replace the values with the strategy code's own build, test, and run commands. | Names the shell commands a code or model pipeline runs for build, test, run, and smoke checks. | effects-map.md:1732-1740 |
| testing.framework | W | CONDITIONAL | Q25 = C or D | Replace the engine test-runner table with the strategy code's own test framework and coverage tool. | Names the test runner and coverage tool a code or model pipeline uses. | effects-map.md:1070-1078 |
| qa.coverage_minimum | W | CONDITIONAL | Q25 = C or D | Keep the enforcement mechanism. Swap the engine-specific coverage-report parsing for the strategy code's own tool. | Sets the minimum code-coverage percentage enforced when qa.level is full. | effects-map.md:1207-1213 |
| naming.{classes,variables,constants,signals,files} | D | CONDITIONAL | Q25 = C or D | Keep the naming-convention block. Drop the scenes and prefabs row, which is engine-only. | Names the code-naming conventions passed into a brief, manifest, or spec. | effects-map.md:1847-1856 |
| code-root-resolution.md + resolve_code_root() | — | CONDITIONAL | Q25 = C or D | Add a case arm for the strategy code's own root directory; the function returns empty until one is added. | Finds the directory that holds the strategy code, chosen by the archetype. | .claude/hooks/yaml-helper.sh:1206-1215,1235-1241 |
| engine.name + specialists | D | LEAVE | — | Do not port this key. Build a new archetype key with its own specialist-routing table. | Routes code work to a language, shader, or UI specialist, by engine choice. | .claude/hooks/yaml-helper.sh:472,1235-1241; effects-map.md:1709-1716 |
| project.kind | W | LEAVE | — | Do not port as-is. Implement it as the domain-branch point it was reserved for; no skill or hook reads it today. | A reserved key meant to select the domain a project runs in. | effects-map.md:1646-1650 |
| platform.multiplayer | D | LEAVE | — | Remove this key; it has no hedge-fund analogue. | Routes real-time multiplayer network code; a hedge fund has no such feature. | effects-map.md:1328-1332 |
| platform.online | W | LEAVE | — | Rename and reuse only if a founder confirms external market-data or broker API calls; otherwise remove this key. | Marks whether the project calls cloud-save, leaderboard, or in-app-purchase services. | effects-map.md:1371-1375 |
| platform.cert_tier | D | LEAVE | — | Remove this key; it has no hedge-fund analogue. | Sets the store certification tier for an Itch, Steam, or console release. | effects-map.md:1408-1412 |
| accessibility.target | W | LEAVE | — | Keep this key only if a founder decides to wire it in; no skill or hook reads it today. | A reserved key meant to set an accessibility compliance target. | effects-map.md:1447-1451 |
| performance.target_framerate / frame_budget_ms / draw_call_limit / memory_ceiling_mb | D | LEAVE | — | Remove these keys. Design a new latency key set fresh if execution-latency limits matter; do not treat this as a rename. | Sets rendering-performance budgets for framerate, draw calls, and memory; a fund has no such need. | effects-map.md:1532-1536 |
| archetype | — | NEW (INFERENCE) | — | Add this key with values quant, discretionary, macro, or multi-strategy. Use it to route specialist agents the way engine.name does today. | Drives which specialist agents spawn for the fund's chosen strategy type; replaces engine.name's routing role. | effects-map.md:1709-1716 |
| jurisdiction | — | NEW (INFERENCE) | — | Add this key, for example KR-FSC, KY-CIMA, or US-SEC. Author the checklist content fresh; no key holds it today. | Drives which regulatory checklist and calendar apply to the fund, by country or regulator. | docs/hedge-fund-setup/ref/07-offshore-setup.md:20; effects-map.md:1408-1412 |
| risk.leverage_cap_pct_nav / risk.var_limit / risk.concentration_limit / risk.loss_limit_daily | — | NEW (INFERENCE) | — | Add this block; no key covers it today. Treat it as the top-priority new key set, given the legal leverage cap. | Holds the fund's leverage, value-at-risk, concentration, and daily-loss limits; the law caps leverage at 400% of NAV. | docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:23-31 |
| regulatory_calendar | — | NEW (INFERENCE) | — | Add this key for filing deadlines, IC or board meeting cadence, and audit windows. Use cadence.sprint_length as the structural shape only. | Tracks fund filing deadlines and report dates, such as the 2-week setup report and quarterly derivative report. | docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:30,33; effects-map.md:1496-1502 |
| code_pipeline.model_change_approval / code_pipeline.version_control_required | — | NEW (INFERENCE) | Q25 = C or D | Add these keys per the model-governance rule. Use commands.* and testing.strict.* as the closest structural donors for the mechanism shape. | Records who approved a model change and that its code is under version control, per the SEC Two Sigma finding. | docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| controls.four_eyes_required_for | — | NEW (INFERENCE) | — | Add this key with trade_execution, valuation, and nav_calculation. Build the second-human check fresh; automation_always_ask only supplies the category-list shape. | Names the actions that need a second, independent human sign-off: trade execution, valuation, and NAV calculation. | .claude/hooks/yaml-helper.sh:890-892; docs/hedge-fund-setup/ref/10-operations-and-providers.md:32 |
| independent valuation / custody flags | — | NEW (INFERENCE) | — | Add these flags to record that custody and NAV sign-off sit outside the manager. No key in this schema covers it today. | Records that an independent custodian holds fund assets and an independent administrator sets the NAV. | docs/hedge-fund-setup/ref/10-operations-and-providers.md:29,32 |

### 5.5 rules (13)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/rules/agent-memory.md | K | TAKE-MODIFY | — | Swap the day-one worked example (src/, GDDs, engine) for a hedge-fund equivalent, such as NAV, positions, or limits. | Agent memory is the one place an agent may write without asking; the staleness-guard discipline transplants directly. | .claude/rules/agent-memory.md:8-11; .claude/rules/agent-memory.md:33-38; .claude/rules/agent-memory.md:23-29 |
| .claude/rules/ai-code.md | D | LEAVE | — | Do not transplant this rule; write a fresh rule if a signal-generation component exists. | The vocabulary (behavior trees, perception ranges, formation, flanking) is too game-specific to salvage. | .claude/rules/ai-code.md:9-13 |
| .claude/rules/data-files.md | D | TAKE-MODIFY | — | Change the path from assets/data/** to config/data/**. Replace the worked example with a risk_limits.json equivalent. | This transplants directly for the fund's own parameter files, such as risk limits and fee schedules. | .claude/rules/data-files.md:8-12; .claude/rules/data-files.md:29-48 |
| .claude/rules/design-docs.md | R | TAKE-MODIFY | — | Change the path to design/strategies/**; keep the section-count and Formulas-required-when-numeric-rules test unchanged. | The Formulas-required-when-numeric-rules test reads almost verbatim as a hedge-fund requirement. | .claude/rules/design-docs.md:9-10; .claude/rules/design-docs.md:19-21 |
| .claude/rules/engine-code.md | D | LEAVE | — | Do not transplant this rule. | This rule is too specific to real-time rendering and physics to salvage. | .claude/rules/engine-code.md:8; .claude/rules/engine-code.md:11 |
| .claude/rules/gameplay-code.md | D | CONDITIONAL | Q05 = B or E | Rename the rule to quant-code.md and reword it lightly, if the fund adopts the quant archetype. | The never-hardcoded rule and the unit-tests-for-all-logic rule serve the model-governance requirement directly. | .claude/rules/gameplay-code.md:8; .claude/rules/gameplay-code.md:12-15 |
| .claude/rules/narrative.md | W | LEAVE | — | Do not transplant this rule at the core org-setup level; write a fresh investor-comms rule instead. | Story and dialogue content has no fund analogue; investor-communication style is narrower and needs its own rule. | .claude/rules/narrative.md:8-12 |
| .claude/rules/network-code.md | D | LEAVE | — | Do not transplant this rule; write a fresh API-integration rule for rate limits and failover, if needed. | This rule is multiplayer-netcode specific; the fund's networking need is external API integration instead. | .claude/rules/network-code.md:8; .claude/rules/network-code.md:10 |
| .claude/rules/prototype-code.md | K | TAKE | — | Keep the file unchanged. | The rule that research code must not deploy without rewrite fits the quant desk's research and backtesting code directly. | .claude/rules/prototype-code.md:32-36 |
| .claude/rules/shader-code.md | D | LEAVE | — | Do not transplant this rule. | This rule is entirely graphics-shader specific, with no hedge-fund use. | .claude/rules/shader-code.md:1-9 |
| .claude/rules/skill-authoring.md | K | TAKE | — | Swap only the evidence table's CCGS examples for hedge-fund ones; keep the five obligations unchanged. | This meta-rule governs how every new hedge-fund skill, agent, and gate must be written. | .claude/rules/skill-authoring.md:9; .claude/rules/skill-authoring.md:21-36; .claude/rules/skill-authoring.md:70-79 |
| .claude/rules/test-standards.md | K | TAKE | — | Replace the GDScript code examples with the fund's own code language. | This fully domain-neutral rule serves the model-governance test-discipline requirement for any quant or trading code. | .claude/rules/test-standards.md:15-18 |
| .claude/rules/ui-code.md | W | CONDITIONAL | Q24 = B | Keep the no-hardcoded-strings and mandatory-accessibility rules, if the fund builds a proprietary investor portal. | Gamepad and HUD content is not relevant; only the localization and accessibility principles survive. | .claude/rules/ui-code.md:9; .claude/rules/ui-code.md:14 |

### 5.6 templates (46)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/docs/templates/SKILL-CONTRACT-TEMPLATE.md | K | TAKE | — | Copy the simpler six-field contract shape; skip the aspirational Testing Evidence and Drift Monitoring sections, which no shipped contract uses. | Gives new HF skill handoffs (for example /investment-decision to /trade-execution) a domain-neutral contract structure. | .claude/docs/templates/SKILL-CONTRACT-TEMPLATE.md:3-21 |
| .claude/docs/templates/accessibility-requirements.md | W | CONDITIONAL | Q24 = B | Delete all game, console, and mobile feature rows; write a plain web-accessibility checklist for the investor portal UI. | Gives the investor portal UI a web-accessibility checklist, only if the firm builds the portal. | .claude/docs/templates/accessibility-requirements.md:57-156 |
| .claude/docs/templates/architecture-decision-record.md | D | TAKE-MODIFY | changes depend on Q25 | Replace the Engine Compatibility section with a Regulatory or Model-Risk Impact section; keep change approval and version history. | Records model-governance decisions for trading and model code, including change approval and version history. | .claude/docs/templates/architecture-decision-record.md:41,71; scratchpad/mapping.txt:79 |
| .claude/docs/templates/architecture-doc-from-code.md | D | CONDITIONAL | Q25 = C or D | Keep the headers as written; use this template only after a code pipeline exists. | Writes an ADR after the fact for a trading-system component that has no original decision record. | .claude/docs/templates/architecture-doc-from-code.md:1-250 |
| .claude/docs/templates/architecture-traceability.md | D | CONDITIONAL | Q25 = C or D | Swap GDD for Regulatory Requirement or IC Policy in every heading; keep the matrix shape unchanged. | Traces regulatory and IC-policy requirements to system controls and ADRs as ODD evidence. | .claude/docs/templates/architecture-traceability.md:1-88 |
| .claude/docs/templates/art-bible.md | R | LEAVE | — | Leave this file behind; it has no reusable structure beyond the generic brand-guide concept T2 already extracted. | Serves at most as a cosmetic style-guide donor for a pitch deck; not a standard org-setup document. | .claude/docs/templates/art-bible.md:48-73 |
| .claude/docs/templates/changelog-template.md | W | TAKE-MODIFY | — | Rename the Balance Changes table to log risk and strategy-parameter changes with before and after values and rationale. | Keeps a model-governance version history of strategy and model changes, not customer messaging. | .claude/docs/templates/changelog-template.md:23-28 |
| .claude/docs/templates/concept-doc-from-prototype.md | W | TAKE-MODIFY | — | Rename the Production Readiness Assessment section to Live Capital Readiness; route sign-off to the CRO and CIO. | Assesses readiness to move a strategy pilot from paper trading to live capital. | .claude/docs/templates/concept-doc-from-prototype.md:146-168 |
| .claude/docs/templates/design-doc-from-implementation.md | D | CONDITIONAL | Q25 = C or D | Keep the structure unchanged; use it to reconstruct a strategy design document after implementation. | Reverse-documents a trading system implementation; its Balance and Tuning section records parameter settings. | .claude/docs/templates/design-doc-from-implementation.md:53-147 |
| .claude/docs/templates/difficulty-curve.md | D | LEAVE | — | Leave this file behind; it paces player experience and has no hedge-fund equivalent. | Has no hedge-fund use. | .claude/docs/templates/difficulty-curve.md:11-305 |
| .claude/docs/templates/economy-model.md | D | CONDITIONAL | Q22 includes A | Use this template only if the founder wants a fee and waterfall economics document apart from the legal PPM. | Lends its Sources, Sinks, and Balance Targets structure to model fee flows, hurdle rates, and high-water marks. | .claude/docs/templates/economy-model.md:31-53 |
| .claude/docs/templates/faction-design.md | R | LEAVE | — | Leave this file behind; it is narrative and worldbuilding content with no role in HF org setup. | Has no use for firm org setup. | .claude/docs/templates/faction-design.md:1-98 |
| .claude/docs/templates/game-brief.md | W | TAKE-MODIFY | — | Rename core loop to core investment process loop and MVP to minimum viable fund launch scope. | Gives the minimal workflow tier a one-page fund or strategy summary. | .claude/docs/templates/game-brief.md:17-35 |
| .claude/docs/templates/game-concept.md | W | TAKE-MODIFY | — | Delete the MDA Aesthetics and Bartle Taxonomy sections outright; keep Core Identity, Core Loop, Target LP Profile, Technical Considerations, Risks, and MVP Definition. | Gives the fund or strategy concept document its core identity, loop, target LP profile, risks, and MVP scope. | .claude/docs/templates/game-concept.md:68-102,119-126; .claude/docs/templates/game-concept.md:219-231,279-304 |
| .claude/docs/templates/game-design-document.md | R | TAKE-MODIFY | — | Delete the Visual/Audio Requirements and Game Feel sections; keep Formulas, Edge Cases, Dependencies, and Tuning Knobs as written. | Becomes the priority Strategy Design Document; records exposure limits, loss rules, leverage caps, and the investment-decision audit trail. | .claude/docs/templates/game-design-document.md:50-69; .claude/docs/templates/game-design-document.md:69-96; .claude/docs/templates/game-design-document.md:96-156 |
| .claude/docs/templates/game-pillars.md | W | TAKE-MODIFY | — | Swap the escalation path to the CIO or IC chair; replace the examples table with investment-committee examples. | Records the firm's investment philosophy and pillars for the investment committee to reference. | .claude/docs/templates/game-pillars.md:207-227 |
| .claude/docs/templates/hud-design.md | D | CONDITIONAL | Q25 = D | Use this template only if the firm builds its own trading terminal instead of a vendor OMS or EMS. | Specifies the trading dashboard or terminal UI, needed only without a vendor OMS or EMS. | .claude/docs/templates/hud-design.md:1-251 |
| .claude/docs/templates/incident-response.md | W | TAKE-MODIFY | — | Keep the Timeline, Root Cause, Mitigation, Communication, Prevention, and Sign-off shape; route ownership and retention to the CCO. | Logs operational incidents and limit breaches as a formal, CCO-owned regulatory record with mandatory retention. | .claude/docs/templates/incident-response.md:67-86; .claude/docs/templates/incident-response.md:125-130 |
| .claude/docs/templates/interaction-pattern-library.md | R | CONDITIONAL | Q24 = B | Use this component library only if the firm builds its own investor portal. | Supplies UI components for a proprietary investor portal only. | .claude/docs/templates/interaction-pattern-library.md:109-413 |
| .claude/docs/templates/level-design-document.md | D | LEAVE | — | Leave this file behind; it has no hedge-fund analog. | Has no hedge-fund use. | .claude/docs/templates/level-design-document.md:1-106 |
| .claude/docs/templates/milestone-definition.md | K | TAKE | — | Swap the Type enum values for firm-setup milestone names; keep the rest of the structure unchanged. | Tracks firm-setup milestones, such as FSC registration, compliance go-live, and first close. | .claude/docs/templates/milestone-definition.md:1-79; .claude/docs/templates/milestone-definition.md:6 |
| .claude/docs/templates/narrative-character-sheet.md | R | LEAVE | — | Leave this file behind; it is character and dialogue content with no marketing use case here. | Has no org-setup use; LP persona work is only a marketing or IR nicety. | .claude/docs/templates/narrative-character-sheet.md:26-93 |
| .claude/docs/templates/pitch-document.md | W | TAKE-MODIFY | — | Map the Business Model table to fee structure, share classes, and conflicts-of-interest policy; drop the Audio Identity section. | Builds the investor pitch and fund deck. | .claude/docs/templates/pitch-document.md:99-109; .claude/docs/templates/pitch-document.md:40-46 |
| .claude/docs/templates/player-journey.md | R | CONDITIONAL | Q24 = B or C | Use this template only if the founder wants a formal investor onboarding journey as a CRM artifact. | Maps the investor onboarding journey; low priority and not a standard org-setup document. | .claude/docs/templates/player-journey.md:58-198 |
| .claude/docs/templates/post-mortem.md | K | TAKE | — | Keep this template unchanged; it already fits the investment post-trade review. | Records the investment post-trade review. | .claude/docs/templates/post-mortem.md:1-70 |
| .claude/docs/templates/project-stage-report.md | W | TAKE-MODIFY | — | Rename the category subsections to Regulatory Filings, Compliance Policies, Risk Framework, Trading Systems, and Governance. | Audits where the firm-setup track stands. | .claude/docs/templates/project-stage-report.md:21-78 |
| .claude/docs/templates/prototype-report.md | R | CONDITIONAL | Q05 = B or E, or Q20 | Keep the PROCEED, PIVOT, KILL pattern unchanged; use it for the quant research go or no-go decision. | Writes the strategy backtest or paper-trade go/no-go memo before the firm commits capital. | .claude/docs/templates/prototype-report.md:1-100 |
| .claude/docs/templates/release-checklist-template.md | D | LEAVE | — | Leave this file behind; milestone-definition.md already covers go-live checklists. | Has no use; milestone-definition.md already covers go-live checklists. | .claude/docs/templates/release-checklist-template.md:58-95 |
| .claude/docs/templates/release-notes.md | W | TAKE-MODIFY | — | Rename the Balance Adjustments table to a Strategy Parameter Changes disclosure table for investors. | Gives the investor update and monthly letter its cadence-report skeleton. | .claude/docs/templates/release-notes.md:27-32 |
| .claude/docs/templates/risk-register-entry.md | K | TAKE | — | Keep this template unchanged; it directly serves the firm's risk register need. | Records firm-setup and investment risk register entries. | .claude/docs/templates/risk-register-entry.md:10-14; .claude/docs/templates/risk-register-entry.md:41-51 |
| .claude/docs/templates/session-state.md | K | TAKE | — | Keep this template unchanged; it is a pure engineering session-checkpoint mechanism. | Serves as an unmodified part of the operating-foundation transplant list. | .claude/docs/templates/session-state.md:6-29 |
| .claude/docs/templates/sound-bible.md | D | LEAVE | — | Leave this file behind; it is pure audio design with no hedge-fund use. | Has no hedge-fund use. | .claude/docs/templates/sound-bible.md:1-100 |
| .claude/docs/templates/sprint-plan.md | K | TAKE | — | Swap the Definition-of-Done checklist items for compliance sign-off items; keep the rest unchanged. | Runs the firm-setup track's own sprint cadence. | .claude/docs/templates/sprint-plan.md:55-65 |
| .claude/docs/templates/systems-index.md | R | TAKE-MODIFY | — | Rewrite the Categories enum for firm-setup layers: Foundation, Core, Feature, and Presentation. | Drives the firm-setup track as the master Firm Systems Index across all four layers. | .claude/docs/templates/systems-index.md:31,66-82 |
| .claude/docs/templates/technical-design-document.md | D | CONDITIONAL | Q25 = C or D | Use this template only if the firm builds proprietary OMS, EMS, or market-data infrastructure. | Documents the OMS, EMS, and market-data architecture as the technical counterpart to the Strategy Design Document. | .claude/docs/templates/technical-design-document.md:11-25 |
| .claude/docs/templates/test-evidence.md | W | TAKE-MODIFY | — | Swap the sign-off role list for Portfolio Manager, Risk Officer, and Independent Valuator. | Records trade or model validation evidence and independent valuation sign-off for segregation of duties. | .claude/docs/templates/test-evidence.md:80-88 |
| .claude/docs/templates/test-plan.md | D | CONDITIONAL | Q25 = C or D | Use this template only once the code or model pipeline needs formal test planning. | Plans model and system tests for the quant pipeline. | .claude/docs/templates/test-plan.md:25-56 |
| .claude/docs/templates/ux-spec.md | R | CONDITIONAL | Q24 = B | Use this template only if the firm builds its own investor portal. | Specifies screens and flows for the investor portal only. | .claude/docs/templates/ux-spec.md:245-285 |
| .claude/docs/templates/vertical-slice-report.md | D | LEAVE | — | Leave this file behind; prototype-report.md already covers the same go/no-go shape for less effort. | Has no use; prototype-report.md covers the same PROCEED, PIVOT, KILL pattern better. | .claude/docs/templates/vertical-slice-report.md:10-19,93 |
| .claude/docs/templates/guidance/accessibility-requirements-guide.md | W | LEAVE | — | Leave this file behind; it is bundled with its parent template's conditional. | Shares the same investor-portal-build conditional as its parent template. | .claude/docs/templates/guidance/accessibility-requirements-guide.md:1-9 |
| .claude/docs/templates/guidance/hud-design-guide.md | D | LEAVE | — | Leave this file behind; it only guides a template the firm is not taking. | Has no hedge-fund use. | .claude/docs/templates/guidance/hud-design-guide.md:10-371 |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-game-specific.md | D | LEAVE | — | Leave this file behind; it documents pure game UI patterns with no hedge-fund use. | Has no hedge-fund use. | .claude/docs/templates/guidance/interaction-pattern-library-guide-game-specific.md:9-148 |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md | R | CONDITIONAL | Q24 = B | Use this guide only if the firm builds its own investor portal. | Documents generic navigation, loading, and error-state patterns. | .claude/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md:9-121 |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md | R | CONDITIONAL | Q24 = B | Use this guide only if the firm builds its own investor portal. | Documents generic button, modal, toast, and tooltip specifications. | .claude/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md:9-554 |
| .claude/docs/templates/guidance/interaction-pattern-library-guide.md | R | CONDITIONAL | Q24 = B | Use this index only if the firm builds its own investor portal. | Indexes the pattern-library guidance set. | .claude/docs/templates/guidance/interaction-pattern-library-guide.md:3 |
| .claude/docs/templates/guidance/ux-spec-guide.md | R | CONDITIONAL | Q24 = B | Use this guide only if the firm builds its own investor portal. | Gives authoring guidance for ux-spec.md under the same conditional. | .claude/docs/templates/guidance/ux-spec-guide.md:3-434 |

### 5.7 director gates (28)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/docs/director-gates/cd-phase-gate.md | K | TAKE-MODIFY | — | Replace creative or visual readiness content with fund-launch readiness (filings, custody, risk limits, compliance sign-off). Keep the parallel-spawn and strictest-verdict rule. | Runs a launch-readiness or quarterly control-review panel; spawns CIO, CRO, CCO, and COO in parallel. | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 |
| .claude/docs/director-gates/td-phase-gate.md | W | TAKE-MODIFY | — | Replace creative or visual readiness content with fund-launch readiness (filings, custody, risk limits, compliance sign-off). Keep the parallel-spawn and strictest-verdict rule. | Runs a launch-readiness or quarterly control-review panel; spawns CIO, CRO, CCO, and COO in parallel. | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 |
| .claude/docs/director-gates/pr-phase-gate.md | K | TAKE-MODIFY | — | Replace creative or visual readiness content with fund-launch readiness (filings, custody, risk limits, compliance sign-off). Keep the parallel-spawn and strictest-verdict rule. | Runs a launch-readiness or quarterly control-review panel; spawns CIO, CRO, CCO, and COO in parallel. | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 |
| .claude/docs/director-gates/ad-phase-gate.md | K | TAKE-MODIFY | — | Replace creative or visual readiness content with fund-launch readiness (filings, custody, risk limits, compliance sign-off). Keep the parallel-spawn and strictest-verdict rule. | Runs a launch-readiness or quarterly control-review panel; spawns CIO, CRO, CCO, and COO in parallel. | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 |
| .claude/docs/director-gates/td-system-boundary.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/td-architecture.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/td-adr.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/td-manifest.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/lp-feasibility.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/lp-code-review.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/ql-test-coverage.md | R | CONDITIONAL | Q05 = B or E and Q25 = C or D | Rename ADR to model-change record and GDD requirement to strategy-spec requirement. Replace engine-version and post-cutoff API checks with data-library version and known model-risk checks. | Gives a model-governance review chain: strategy sign-off, per-change code review, and backtest coverage review, for a quant code pipeline. | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21; docs/hedge-fund-setup/ref/12-technology-infrastructure.md:34 |
| .claude/docs/director-gates/cd-pillars.md | K | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/cd-gdd-align.md | R | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/cd-systems.md | R | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/cd-narrative.md | W | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/cd-playtest.md | R | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/ad-concept-visual.md | K | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/ad-art-bible.md | W | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/ad-visual.md | K | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/nd-consistency.md | W | LEAVE | — | Do not port this gate; it has no place in the fund's core control loop. | Checks creative or brand identity, which a fund's control framework does not need; at most a thin IR check. | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 |
| .claude/docs/director-gates/pr-scope.md | K | TAKE-MODIFY | — | Change wording only: sprint becomes cycle, milestone becomes regulatory or launch milestone. Collapse the three separate verdict vocabularies into one before reuse. | Gives a generic operations or PMO planning-feasibility panel; sprint, milestone, and scope language map to fund-ops planning cycles. | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 |
| .claude/docs/director-gates/pr-sprint.md | K | TAKE-MODIFY | — | Change wording only: sprint becomes cycle, milestone becomes regulatory or launch milestone. Collapse the three separate verdict vocabularies into one before reuse. | Gives a generic operations or PMO planning-feasibility panel; sprint, milestone, and scope language map to fund-ops planning cycles. | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 |
| .claude/docs/director-gates/pr-milestone.md | K | TAKE-MODIFY | — | Change wording only: sprint becomes cycle, milestone becomes regulatory or launch milestone. Collapse the three separate verdict vocabularies into one before reuse. | Gives a generic operations or PMO planning-feasibility panel; sprint, milestone, and scope language map to fund-ops planning cycles. | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 |
| .claude/docs/director-gates/pr-epic.md | K | TAKE-MODIFY | — | Change wording only: sprint becomes cycle, milestone becomes regulatory or launch milestone. Collapse the three separate verdict vocabularies into one before reuse. | Gives a generic operations or PMO planning-feasibility panel; sprint, milestone, and scope language map to fund-ops planning cycles. | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 |
| .claude/docs/director-gates/td-change-impact.md | W | TAKE-MODIFY | — | Keep the APPROVE, CONCERNS, or REJECT verdicts. Retarget the review from a design-scope change to a strategy, limit, or policy-scope change. | Reviews the impact of a strategy, limit, or policy change that touches more than one department; owner is coo. | .claude/docs/director-gates/td-change-impact.md:5; .claude/docs/director-gates/td-change-impact.md:25 |
| .claude/docs/director-gates/td-feasibility.md | R | TAKE-MODIFY | — | Keep the VIABLE, CONCERNS, or HIGH RISK verdicts. Retarget the review to a strategy's data, borrow, and execution infrastructure. | Checks a proposed strategy's data, borrow, and execution infrastructure before build-out starts; owner is technology-lead or coo. | .claude/docs/director-gates/td-feasibility.md:5; .claude/docs/director-gates/td-feasibility.md:24 |
| .claude/docs/director-gates/td-engine-risk.md | D | CONDITIONAL | Q05 = B or E and Q25 = C or D | Retarget the review from post-cutoff engine-API risk to data-library and vendor-API version risk. Keep the APPROVE, CONCERNS, or REJECT verdicts. | Reviews library and vendor market-data or broker API version risk before a quant strategy build starts. | .claude/docs/director-gates/td-engine-risk.md:5; .claude/docs/director-gates/td-engine-risk.md:22 |
| .claude/docs/director-gates/ql-story-ready.md | R | CONDITIONAL | Q05 = B or E and Q25 = C or D | Apply this gate only where a code or model pipeline exists. Keep the ADEQUATE, GAPS, or INADEQUATE verdicts unchanged. | Checks a model-change story's acceptance criteria for testability before the story enters a sprint. | .claude/docs/director-gates/ql-story-ready.md:5; .claude/docs/director-gates/ql-story-ready.md:27 |

### 5.8 agents (49)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/agents/creative-director.md | — | LEAVE | — | Keep only the decision-workflow shell. Drop the pillar, MDA aesthetics, and player-psychology content; none apply to a fund. | No direct role. The Strategic Decision Workflow protocol gives a generic pattern for CIO investment-thesis decisions. | .claude/agents/creative-director.md:18-20; .claude/agents/creative-director.md:199-247 |
| .claude/agents/technical-director.md | — | CONDITIONAL | Q25 = C or D | Replace engine architecture with trading and model platform architecture. Keep the ADR format: Status, Context, Decision, Consequences, Alternatives. | Gives the skeleton for a Head of Quant Technology role: ADR ownership, technology evaluation, performance budgets, technical-debt management. | .claude/agents/technical-director.md:80-94; .claude/agents/technical-director.md:138 |
| .claude/agents/producer.md | — | TAKE-MODIFY | — | Rename the sprint cycle to the ops cycle. Reuse the risk register as-is for operational risk, not market risk. | Gives the COO or Head of Operations role: sprint planning, milestone tracking, risk register, cross-department coordination, retrospectives. | .claude/agents/producer.md:89-90; .claude/agents/producer.md:107-113 |
| .claude/agents/qa-lead.md | — | CONDITIONAL | Q25 = C or D | Replace the Logic, Integration, Visual, UI, and Config rows with backtest, live-shadow, data-quality, and reporting categories. | Gives the Model Validation function: the evidence-type table and shift-left discipline map onto backtest evidence requirements. | .claude/agents/qa-lead.md:69-79; .claude/agents/qa-lead.md:13-16 |
| .claude/agents/lead-programmer.md | — | CONDITIONAL | Q25 = C or D | Keep the Coding Standards Enforcement list almost as written. Change 'gameplay values' to 'strategy parameters'. | Gives a Head of Quant Development role: code review, API design, and coding-standard rules that map onto model-change control. | .claude/agents/lead-programmer.md:84-91; .claude/agents/lead-programmer.md:72-75 |
| .claude/agents/security-engineer.md | — | TAKE-MODIFY | — | Rename anti-cheat to fraud and market-abuse detection, and save data to investor and position data. Keep the checklist. | Gives a CISO role: network security, data-at-rest encryption, privacy compliance, and a per-feature Security Review Checklist. | .claude/agents/security-engineer.md:82-87; .claude/agents/security-engineer.md:111-119 |
| .claude/agents/analytics-engineer.md | — | CONDITIONAL | Q09 = B, C, or D (stage 2+) | Replace the game.level.started naming convention with a risk-metric taxonomy such as risk.exposure.updated and risk.limit.breached. | Gives a Risk Analytics or Investor Reporting function: event taxonomy and dashboard-specification pattern transfer to risk-metric dashboards. | .claude/agents/analytics-engineer.md:82-91; .claude/agents/analytics-engineer.md:74-76 |
| .claude/agents/release-manager.md | — | TAKE-MODIFY | — | Replace platform certification requirements with regulatory filing requirements such as FSC registration. Reuse semantic versioning for document amendments. | Gives a Fund Launch Manager role: the staged, no-skip release pipeline and version-numbering discipline map onto fund launch order. | .claude/agents/release-manager.md:66-78; .claude/agents/release-manager.md:93-105 |
| .claude/agents/community-manager.md | — | TAKE-MODIFY | — | Rename players to investors and patch notes to investor updates. Ask the founder to confirm the model tier; it is currently the cheapest one. | Gives Investor Relations use: patch-notes structure becomes investor updates; the no-unverified-claim rule fits investor-facing copy well. | .claude/agents/community-manager.md:128-134; .claude/agents/community-manager.md:5 |
| .claude/agents/writer.md | — | TAKE-MODIFY | — | Replace dialogue, lore, and item-description work with investor-letter, fact-sheet, and pitch-deck copy work. | Gives an investor-letters copywriter role: the section-by-section drafting workflow suits long-form investor letters well. | .claude/agents/writer.md:34-42; .claude/agents/writer.md:104-105 |
| .claude/agents/systems-designer.md | — | TAKE-MODIFY | — | Retarget the formulas from combat and progression to risk and exposure. Keep the mandatory-format enforcement rule as written. | Gives a quant risk-formula documentation owner role: the mandatory format template fits VaR, exposure, and leverage formulas. | .claude/agents/systems-designer.md:97-115; .claude/agents/systems-designer.md:141-158 |
| .claude/agents/economy-designer.md | — | CONDITIONAL | Q05 = B or E | Replace the item and loot registry with an instrument and position registry. | Gives an instrument and position master-data steward role: check the canonical registry first and flag any value that conflicts. | .claude/agents/economy-designer.md:79-93 |
| .claude/agents/devops-engineer.md | — | CONDITIONAL | Q25 = C or D | Rename the build and CI targets to model-deployment targets. Keep the branching strategy as written. | Gives an infra and model-deployment engineer role: the branching strategy supports code-access-control and version-history requirements. | .claude/agents/devops-engineer.md:79-85 |
| .claude/agents/godot-specialist.md | — | LEAVE | — | Drop all Godot-specific content. Keep only the lead-plus-sub-specialist delegation shape for a possible future quant-platform team. | No domain content transfers. The lead-plus-four-subspecialist delegation shape is a template for a future quant-platform team. | .claude/agents/godot-specialist.md:3; .claude/agents/godot-specialist.md:4 |
| .claude/agents/godot-gdscript-specialist.md | — | LEAVE | — | Drop all Godot-specific content. Keep only the lead-plus-sub-specialist delegation shape for a possible future quant-platform team. | No domain content transfers. The lead-plus-four-subspecialist delegation shape is a template for a future quant-platform team. | .claude/agents/godot-gdscript-specialist.md:3 |
| .claude/agents/godot-csharp-specialist.md | — | LEAVE | — | Drop all Godot-specific content. Keep only the lead-plus-sub-specialist delegation shape for a possible future quant-platform team. | No domain content transfers. The lead-plus-four-subspecialist delegation shape is a template for a future quant-platform team. | .claude/agents/godot-csharp-specialist.md:3 |
| .claude/agents/godot-shader-specialist.md | — | LEAVE | — | Drop all Godot-specific content. Keep only the lead-plus-sub-specialist delegation shape for a possible future quant-platform team. | No domain content transfers. The lead-plus-four-subspecialist delegation shape is a template for a future quant-platform team. | .claude/agents/godot-shader-specialist.md:3 |
| .claude/agents/godot-gdextension-specialist.md | — | LEAVE | — | Drop all Godot-specific content. Keep only the lead-plus-sub-specialist delegation shape for a possible future quant-platform team. | No domain content transfers. The lead-plus-four-subspecialist delegation shape is a template for a future quant-platform team. | .claude/agents/godot-gdextension-specialist.md:3 |
| .claude/agents/unity-specialist.md | — | LEAVE | — | Drop all Unity-specific content such as ECS and Shader Graph. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot family: only the delegation shape, via the Agent allow-list. | .claude/agents/unity-specialist.md:3; .claude/agents/unity-specialist.md:4 |
| .claude/agents/unity-dots-specialist.md | — | LEAVE | — | Drop all Unity-specific content such as ECS and Shader Graph. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot family: only the delegation shape, via the Agent allow-list. | .claude/agents/unity-dots-specialist.md:3 |
| .claude/agents/unity-shader-specialist.md | — | LEAVE | — | Drop all Unity-specific content such as ECS and Shader Graph. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot family: only the delegation shape, via the Agent allow-list. | .claude/agents/unity-shader-specialist.md:3 |
| .claude/agents/unity-addressables-specialist.md | — | LEAVE | — | Drop all Unity-specific content such as ECS and Shader Graph. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot family: only the delegation shape, via the Agent allow-list. | .claude/agents/unity-addressables-specialist.md:3 |
| .claude/agents/unity-ui-specialist.md | — | LEAVE | — | Drop all Unity-specific content such as ECS and Shader Graph. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot family: only the delegation shape, via the Agent allow-list. | .claude/agents/unity-ui-specialist.md:3 |
| .claude/agents/unreal-specialist.md | — | LEAVE | — | Drop all Unreal-specific content such as GAS and Blueprint. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot and Unity families: only the delegation shape, via the Agent allow-list. | .claude/agents/unreal-specialist.md:3; .claude/agents/unreal-specialist.md:4 |
| .claude/agents/ue-gas-specialist.md | — | LEAVE | — | Drop all Unreal-specific content such as GAS and Blueprint. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot and Unity families: only the delegation shape, via the Agent allow-list. | .claude/agents/ue-gas-specialist.md:3 |
| .claude/agents/ue-blueprint-specialist.md | — | LEAVE | — | Drop all Unreal-specific content such as GAS and Blueprint. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot and Unity families: only the delegation shape, via the Agent allow-list. | .claude/agents/ue-blueprint-specialist.md:3 |
| .claude/agents/ue-replication-specialist.md | — | LEAVE | — | Drop all Unreal-specific content such as GAS and Blueprint. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot and Unity families: only the delegation shape, via the Agent allow-list. | .claude/agents/ue-replication-specialist.md:3 |
| .claude/agents/ue-umg-specialist.md | — | LEAVE | — | Drop all Unreal-specific content such as GAS and Blueprint. Keep only the delegation shape from the Agent allow-list. | Gives the same reuse as the Godot and Unity families: only the delegation shape, via the Agent allow-list. | .claude/agents/ue-umg-specialist.md:3 |
| .claude/agents/prototyper.md | — | CONDITIONAL | Q05 = B or E | Replace the HTML, Engine, and Paper prototype paths with backtest, simulation, and paper-trading paths. Keep PROCEED, PIVOT, KILL, and the isolation rule as written. | Gives a Quant Researcher role: the falsifiable-hypothesis discipline and hard isolation rule keep research code out of production. | .claude/agents/prototyper.md:161-162; .claude/agents/prototyper.md:7 |
| .claude/agents/qa-tester.md | — | CONDITIONAL | Q25 = C or D | Keep the test-writing process as is; only the terms are game-specific. Use it only when code or model logic needs validation. | Writes test cases and backtest scenarios for the Model Validation function. | .claude/agents/qa-tester.md:3 |
| .claude/agents/engine-programmer.md | — | CONDITIONAL | Q25 = C or D | Drop the rendering and physics content. Keep 'performance-critical framework code'; it generalizes to a low-latency execution engine built in-house. | Gives a core trading-platform engineer role: execution engine, data pipeline, and performance-critical framework code, if built in-house. | .claude/agents/engine-programmer.md:3 |
| .claude/agents/gameplay-programmer.md | — | CONDITIONAL | Q25 = C or D | Keep the role shape as written; it implements a designed system as code, if strategies are coded in-house. | Gives a strategy-implementation engineer role: turns a researched strategy into production code. | .claude/agents/gameplay-programmer.md:3 |
| .claude/agents/ai-programmer.md | — | CONDITIONAL | Q25 = C or D | Drop the pathfinding and NPC-behavior content; it does not generalize. Keep only the decision-making capability for signal logic. | Gives an ML or quant-signal engineer role, if the fund uses machine-learning models; the fit is weak. | .claude/agents/ai-programmer.md:3 |
| .claude/agents/network-programmer.md | — | LEAVE | — | Do not transplant this agent. Its multiplayer content overlaps little with market-data feeds, and better donors exist. | A weak donor for a market-data or execution-connectivity role, only if the fund builds custom connectivity in-house. | .claude/agents/network-programmer.md:3 |
| .claude/agents/tools-programmer.md | — | CONDITIONAL | Q25 = C or D | Keep the role as written; only the word 'editor' is game-specific. | Gives an internal-tooling engineer role: dashboards, debug utilities, pipeline automation, useful for any archetype with internal engineering. | .claude/agents/tools-programmer.md:3 |
| .claude/agents/ui-programmer.md | — | LEAVE | — | Do not transplant this agent. Its HUD and inventory-screen content has little hedge-fund analog. | A weak donor for an internal dashboard or PM-tool front-end role, only if the fund builds internal UI. | .claude/agents/ui-programmer.md:3 |
| .claude/agents/technical-artist.md | — | LEAVE | — | Do not transplant this agent; its domain is entirely visual and rendering work. | No hedge-fund role matches this agent's visual and rendering work. | .claude/agents/technical-artist.md:3 |
| .claude/agents/performance-analyst.md | — | CONDITIONAL | Q25 = C or D | Keep the profiling process as written; frame-time profiling maps cleanly to execution-latency profiling for a trading system. | Gives a latency and throughput profiling role for an in-house execution engine: frame time becomes order-to-execution latency. | .claude/agents/performance-analyst.md:3 |
| .claude/agents/ux-designer.md | — | LEAVE | — | Do not transplant this agent; its player-onboarding-flow process has weak relevance to a fund. | A weak, low-priority donor for an internal reporting-dashboard UX role. | .claude/agents/ux-designer.md:3 |
| .claude/agents/accessibility-specialist.md | — | LEAVE | — | Do not transplant this agent; its WCAG and colorblind-mode domain has no relevance to a control framework. | No hedge-fund role matches this agent's WCAG and colorblind-mode domain. | .claude/agents/accessibility-specialist.md:3 |
| .claude/agents/localization-lead.md | — | CONDITIONAL | Q07 = B, C, D, or E | Replace language locales with regulatory-jurisdiction locales, such as Korea, Cayman, and the United States. | Gives a multi-jurisdiction documentation lead role: locale-testing expertise seeds work across Korean, Cayman, and US filings. | .claude/agents/localization-lead.md:3 |
| .claude/agents/live-ops-designer.md | — | LEAVE | — | Do not transplant this agent; a hedge fund's control framework has no live-ops equivalent. | No hedge-fund role matches seasonal content or battle passes. | .claude/agents/live-ops-designer.md:3 |
| .claude/agents/art-director.md | — | LEAVE | — | Do not transplant this agent. It owns the AD gates, which are all left for the same reason. | A weak donor, only if the fund wants a pitch-deck or investor-collateral visual-identity role; not a control role. | .claude/agents/art-director.md:3 |
| .claude/agents/audio-director.md | — | LEAVE | — | Do not transplant this agent; a fund's operations have no sonic-identity need. | No hedge-fund role matches this agent's sonic-identity work. | .claude/agents/audio-director.md:3 |
| .claude/agents/sound-designer.md | — | LEAVE | — | Do not transplant this agent; a fund has no audio need. | No hedge-fund role matches this agent's audio-specification work. | .claude/agents/sound-designer.md:3 |
| .claude/agents/narrative-director.md | — | LEAVE | — | Do not transplant this agent; a fund has no story or world-building need. | No direct hedge-fund role. It owns the ND-CONSISTENCY gate, left for the same reasons as the other creative gates. | .claude/agents/narrative-director.md:3 |
| .claude/agents/world-builder.md | — | LEAVE | — | Do not transplant this agent; a fund has no world or lore need. | No hedge-fund role matches this agent's world and lore work. | .claude/agents/world-builder.md:3 |
| .claude/agents/level-designer.md | — | LEAVE | — | Do not transplant this agent; a fund has no spatial or level-design need. | No hedge-fund role matches this agent's spatial level-design work. | .claude/agents/level-designer.md:3 |
| .claude/agents/game-designer.md | — | LEAVE | — | Do not transplant this agent's mechanics-design content; keep only the Question-First Workflow protocol shape. | No direct role. The Question-First Workflow protocol shape gives a reusable template for a Head of Strategy Research role. | .claude/agents/game-designer.md:3 |

### 5.9 skills — management (25)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/skills/sprint-plan/SKILL.md | K | TAKE | — | No change is required to run. Optionally repoint the two design/gdd references to the chosen policy document root. | Sprint engine for firm-setup and fund-launch work; its Definition-of-Done checklist maps to a regulated-release controls checklist. | .claude/skills/sprint-plan/SKILL.md:97; .claude/skills/sprint-plan/SKILL.md:99 |
| .claude/skills/sprint-status/SKILL.md | K | TAKE | — | No change is required. | Read-only status snapshot for any workstream, with stale-item detection useful for the compliance calendar. | .claude/skills/sprint-status/SKILL.md:2 |
| .claude/skills/retrospective/SKILL.md | K | TAKE | — | No change is required. Optionally chain it as the mandatory post-incident review after /hotfix. | Sprint and milestone retrospectives; chained from a hotfix, doubles as the post-incident review a regulator expects. | .claude/skills/retrospective/SKILL.md:2 |
| .claude/skills/scope-check/SKILL.md | K | TAKE | — | Change 'core player experience' at line 157 to 'core mandate or investor experience'. | Detects scope creep against the firm-setup or fund-launch plan, with a quantified Bloat Score. | .claude/skills/scope-check/SKILL.md:25; .claude/skills/scope-check/SKILL.md:157 |
| .claude/skills/settings/SKILL.md | K | TAKE | — | No change to the skill. Define hedge-fund keys such as firm.jurisdiction and fund.structure in the project.yaml schema. | Single view and change surface for firm-level config once the project.yaml schema carries hedge-fund keys. | .claude/skills/settings/SKILL.md:456 |
| .claude/skills/skill-test/SKILL.md | K | TAKE | — | No change to the skill. Add new category rubrics to quality-rubric.md and catalog.yaml for hedge-fund skill categories. | Regression safety net: run static checks on every new compliance, risk, or quant skill before it ships. | .claude/skills/skill-test/SKILL.md:2 |
| .claude/skills/skill-improve/SKILL.md | K | TAKE | — | No change is required. | Iterative test-fix-retest loop that hardens newly authored hedge-fund skills during build-out. | .claude/skills/skill-improve/SKILL.md:2 |
| .claude/skills/estimate/SKILL.md | W | TAKE-MODIFY | — | Swap 'design/gdd/' for the chosen policy document root. Replace the example 'gameplay, UI' row with 'risk engine, OMS, reports'. | Estimates effort for build-out tasks and, where a quant archetype applies, model or strategy work. | .claude/skills/estimate/SKILL.md:16; .claude/skills/estimate/SKILL.md:67 |
| .claude/skills/milestone-review/SKILL.md | W | TAKE | — | No change is required. Optionally rename the 'Feature Completeness' header to 'Deliverable/Control Completeness'. | Go/no-go review for firm-setup checkpoints; flags a regulatory timeline slip before a filing deadline hits. | .claude/skills/milestone-review/SKILL.md:2 |
| .claude/skills/help/SKILL.md | W | TAKE-MODIFY | — | Rewrite the stage-detection and phase-mapping table together with the new workflow-catalog.yaml, in the same commit. | Fast orientation across firm-setup and fund-launch tracks, once the catalog and phase table are rewritten together. | .claude/skills/help/SKILL.md:70; .claude/skills/help/SKILL.md:71; .claude/skills/help/SKILL.md:77 |
| .claude/skills/onboard/SKILL.md | W | TAKE-MODIFY | — | Replace the five role branches with hedge-fund functions: portfolio manager, risk officer, compliance officer, operations, and IR. | Role-specific onboarding document for new hires or new agent instances across the org chart. | .claude/skills/onboard/SKILL.md:58; .claude/skills/onboard/SKILL.md:60 |
| .claude/skills/bug-triage/SKILL.md | W | TAKE-MODIFY | — | Reword the S1-S4 severity table for trading and ops impact. Keep the P1-P4 urgency ladder unchanged. | Flags repeated incidents in one system, such as the risk engine, as a named systemic issue. | .claude/skills/bug-triage/SKILL.md:97; .claude/skills/bug-triage/SKILL.md:98 |
| .claude/skills/bug-report/SKILL.md | R | TAKE-MODIFY | — | Replace the Category enum with Trading, Risk, Compliance, Data, Reporting, Model, and Infra. Replace Scene/Level and Game State with Module/System fields. | Structured incident record with root cause and closure, the base evidence unit for model-governance audit trails. | .claude/skills/bug-report/SKILL.md:59; .claude/skills/bug-report/SKILL.md:67; .claude/skills/bug-report/SKILL.md:48 |
| .claude/skills/hotfix/SKILL.md | R | TAKE-MODIFY | — | Add a fourth mandatory approver, risk or compliance, for any fix to a trading, risk-limit, or valuation code path. | Emergency change-control workflow for a live trading or risk-engine defect, with mandatory triple sign-off. | .claude/skills/hotfix/SKILL.md:109; .claude/skills/hotfix/SKILL.md:111; .claude/skills/hotfix/SKILL.md:161 |
| .claude/skills/tech-debt/SKILL.md | R | TAKE-MODIFY | — | Rename the register to 'Control Gap Register'. Extend the scan to also find placeholder markers in compliance and risk documents. | Single register for code debt and control gaps, each entry recording why it was accepted. | .claude/skills/tech-debt/SKILL.md:45; .claude/skills/tech-debt/SKILL.md:114 |
| .claude/skills/start/SKILL.md | R | TAKE-MODIFY | changes depend on Q17 | Once decided, replace the four initial options and the path tables with firm-stage equivalents. | First-session onboarding that sets project.stage, modes.rigor, and modes.automation before regulatory-track work starts. | .claude/skills/start/SKILL.md:63; .claude/skills/start/SKILL.md:309; .claude/skills/start/SKILL.md:313 |
| .claude/skills/project-stage-detect/SKILL.md | R | TAKE-MODIFY | — | Replace the 7-row stage table with regulatory milestones. Keep the compare-observed-against-claimed mechanism unchanged. | Checks the claimed stage against observed filings and documents, to catch an unsupported 'registration granted' claim. | .claude/skills/project-stage-detect/SKILL.md:125; .claude/skills/project-stage-detect/SKILL.md:107; .claude/skills/project-stage-detect/SKILL.md:118 |
| .claude/skills/adopt/SKILL.md | R | TAKE-MODIFY | — | Redefine the 8-section GDD schema and the ADR's 5 critical sections as the chosen regulatory-document schema. | Brownfield compliance-readiness audit that distinguishes existence from whether a document meets its required structure. | .claude/skills/adopt/SKILL.md:135; .claude/skills/adopt/SKILL.md:159; .claude/skills/adopt/SKILL.md:272 |
| .claude/skills/gate-check/ | R | TAKE-MODIFY | changes depend on Q14 | If CRO and CCO seats are mandatory, give them a fixed seat outside the tier-scaled panel. | PASS/CONCERNS/NOT ASSESSED/FAIL verdicts to advance firm-setup and fund-launch milestones, with a documented, not automatic, decision. | .claude/skills/gate-check/SKILL.md:392; .claude/skills/gate-check/SKILL.md:394; .claude/skills/gate-check/CONTRACT.md:4 |
| .claude/skills/consistency-check/SKILL.md | W | TAKE-MODIFY | — | Replace the entity/item/formula registry schema with a regulatory-value registry. Add an as-of or effective-date field per entry. | Catches a limit stated differently across documents, such as a leverage cap of 350% versus 400%. | .claude/skills/consistency-check/SKILL.md:18; .claude/skills/consistency-check/SKILL.md:64; .claude/skills/consistency-check/SKILL.md:104 |
| .claude/skills/quick-design/SKILL.md | W | TAKE-MODIFY | — | Replace the two MDA-aesthetic mentions with a policy-materiality test. Repoint the GDD reference at the chosen policy doc root. | Lightweight, auditable record for small parameter or procedure tuning, with an escape valve to the full process. | .claude/skills/quick-design/SKILL.md:144; .claude/skills/quick-design/SKILL.md:291; .claude/skills/quick-design/SKILL.md:18 |
| .claude/skills/changelog/SKILL.md | R | TAKE-MODIFY | — | Rename the Game/Framework classification to Trading-Platform/Model versus Internal-Tooling. Keep the hard-stop-on-zero-match rule unchanged. | Auto-generated, provenance-checked changelog from git history: audit-trail evidence for model-governance review. | .claude/skills/changelog/SKILL.md:30; .claude/skills/changelog/SKILL.md:117; .claude/skills/changelog/SKILL.md:64 |
| .claude/skills/patch-notes/SKILL.md | R | CONDITIONAL | Q22 includes E | If in scope, replace the jargon-translation table with an operations-to-investor-value table. Drop the game-specific tone check. | Drafts investor updates in plain language, gated by human IR or compliance review before distribution. | .claude/skills/patch-notes/SKILL.md:131; .claude/skills/patch-notes/SKILL.md:3 |
| .claude/skills/day-one-patch/SKILL.md | R | TAKE-MODIFY | — | Replace 'gold master' and 'cert feedback' with 'production release build' and 'regulator feedback'. Replace the platform rollback plan with a trading rollback plan. | Rollback-first emergency-fix process for issues that surface right after go-live or a filing approval. | .claude/skills/day-one-patch/SKILL.md:19; .claude/skills/day-one-patch/SKILL.md:46; .claude/skills/day-one-patch/SKILL.md:151 |
| .claude/skills/localize/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for the coverage-matrix table format only, to seed a bilingual investor-document tracker if offshore expansion proceeds. | .claude/skills/localize/SKILL.md:16; .claude/skills/localize/SKILL.md:292; .claude/skills/localize/SKILL.md:239 |

### 5.10 skills — pipeline (26)

This table carries 2 HF-verdict columns because Q25 (code/model
pipeline) is the largest single driver of CONDITIONAL items in this
area (design-spec F-02). “Q25=A/B” is the no-pipeline / analysis-only
branch. “Q25=C/D” is the research-repository / production-system
branch.

The top-level verdict counted in §3 is CONDITIONAL for every row in
this table, with 4 exceptions. The 4 exceptions apply the same
mechanism under both branches: create-control-manifest,
propagate-design-change, team-release, and launch-checklist. Their
top-level verdict is TAKE-MODIFY.

5 rows show TAKE-MODIFY in both branch columns but still count as
CONDITIONAL at the top level: create-epics, create-stories,
story-readiness, test-evidence-review, and security-audit. For these
5, the verdict word matches across branches. The required changes
differ by scope, so the source assessment keeps the row CONDITIONAL
on Q25.

| Component | T2 | HF (Q25 = A or B) | HF (Q25 = C or D) | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/skills/architecture-decision/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the engine-context and engine-specialist steps with a compute/data-stack load and a model specialist. Reassign acceptance authority to the CRO or Model-Risk Committee. | A model or architecture change-approval record with one narrow approver. | .claude/skills/architecture-decision/SKILL.md:169-209; .claude/skills/architecture-decision/SKILL.md:490-498; .claude/skills/architecture-decision/CONTRACT.md:56-57 |
| .claude/skills/architecture-review/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the Engine Compatibility Cross-Check with a Data/Compute Stack Compatibility Cross-Check. Rename GDD requirement sources to Strategy or Model Spec. Keep the Requirement-Decision-Story-Test chain. | A requirement-to-evidence traceability matrix for model validation lineage. | .claude/skills/architecture-review/SKILL.md:432-482; .claude/skills/architecture-review/SKILL.md:286-349; .claude/skills/architecture-review/SKILL.md:185-202 |
| .claude/skills/create-architecture/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the engine-context phase with a compute/data-stack context. Rename the layer map to Reporting, Portfolio Construction, Signal/Model, Data Ingestion, and Execution. Keep the sign-off gate. | A master architecture blueprint, with a CRO or CTO sign-off gate, for a data or model pipeline. | .claude/skills/create-architecture/SKILL.md:59-92; .claude/skills/create-architecture/SKILL.md:212-230; .claude/skills/create-architecture/SKILL.md:425-460 |
| .claude/skills/create-control-manifest/SKILL.md | D | TAKE-MODIFY | TAKE-MODIFY | Rename layer labels to functional roles. Change Forbidden APIs to forbidden trading or code patterns. Change Performance Guardrails to numeric risk limits. | A trading and compliance control manifest with exposure limits, loss rules, and the leverage cap as guardrails. | .claude/skills/create-control-manifest/SKILL.md:110-117; .claude/skills/create-control-manifest/SKILL.md:129-139; .claude/skills/create-control-manifest/SKILL.md:219-222 |
| .claude/skills/create-epics/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Rename the layer order to Data/Infra, Signal/Model, Portfolio/Risk, Execution/Reporting. Drop the full decision-record trace table without a code pipeline; keep it with one. | An epic document per functional module, with governance and requirement traceability tables for each system. | .claude/skills/create-epics/SKILL.md:164-176; .claude/skills/create-epics/CONTRACT.md:36-44; .claude/skills/create-epics/SKILL.md:28-40 |
| .claude/skills/create-stories/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Reclassify Config/Data test evidence as BLOCKING. Drop the Visual/Feel type; retype Logic, Integration, and Config/Data for a code pipeline. Keep the spec-first pattern. | Story decomposition with embedded requirement or decision-record traceability and pre-written validation specs. | .claude/skills/create-stories/SKILL.md:169-180; .claude/skills/create-stories/SKILL.md:211-246; .claude/skills/create-stories/SKILL.md:389-399 |
| .claude/skills/story-readiness/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Change the asset-reference check to a data or config file reference check. Keep the AC-count minimums once Visual/Feel drops out. | A pre-implementation or pre-publication readiness gate with explicit could-not-evaluate handling. | .claude/skills/story-readiness/SKILL.md:36-44; .claude/skills/story-readiness/SKILL.md:259-271; .claude/skills/story-readiness/SKILL.md:275-279 |
| .claude/skills/story-done/SKILL.md | R | CONDITIONAL | TAKE-MODIFY | Rename GDD to Strategy or Model Spec, ADR to Decision Record, and control-manifest to Compliance/Trading Rules Manifest. Drop the Visual/Feel gate. Reclassify Config/Data as BLOCKING. | A model-change closure record: acceptance-criteria check, deviation log, independent coverage review, named approver sign-off. | .claude/skills/story-done/SKILL.md:228-234; .claude/skills/story-done/SKILL.md:360-368; .claude/skills/story-done/SKILL.md:371-397 |
| .claude/skills/dev-story/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the routing table with quant roles (data-engineer, quant-researcher, execution-engineer, risk-engineer). Replace the launch-and-screenshot step with a backtest run and retained tearsheet. | A risk-classification trigger for a mandatory second reviewer, a same-session pre-screen only, not an independent validator. | .claude/skills/dev-story/SKILL.md:241-251; .claude/skills/dev-story/SKILL.md:303-316; .claude/skills/dev-story/SKILL.md:471-486 |
| .claude/skills/code-review/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace Engine Specialists with data or quant-infra specialists. Replace Game-Specific Concerns with look-ahead bias, deterministic seeds, and point-in-time data checks. | A decision-record-compliance code review with mandatory finding verification before any defect report. | .claude/skills/code-review/SKILL.md:75-98; .claude/skills/code-review/SKILL.md:132-138; .claude/skills/code-review/SKILL.md:146-163 |
| .claude/skills/test-setup/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the engine runner and CI YAML files with a pytest and GitHub Actions equivalent. Keep the unit, integration, and smoke directory layout. | A directory and CI scaffold that enforces no merge on failed tests, a code-access-control-adjacent policy. | .claude/skills/test-setup/SKILL.md:163-233; .claude/skills/test-setup/SKILL.md:238-372; .claude/skills/test-setup/SKILL.md:375-407 |
| .claude/skills/test-helpers/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the engine assertion and factory snippets with pytest fixtures for synthetic market data. Keep the base, factory, and system-specific structure. | An assertion and factory helper generator grounded in a strategy spec's Formulas section, never a guessed API. | .claude/skills/test-helpers/SKILL.md:34-61; .claude/skills/test-helpers/SKILL.md:145-157; .claude/skills/test-helpers/SKILL.md:365-404 |
| .claude/skills/smoke-check/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the engine test-run commands with the quant pipeline's runner. Replace manual smoke batches with data feed, reconciliation, and leverage checks. Reclassify Config/Data as BLOCKING. | A daily pre-trading-day pipeline health gate for data, risk, and reconciliation checks. | .claude/skills/smoke-check/SKILL.md:140-160; .claude/skills/smoke-check/SKILL.md:419-463; .claude/skills/smoke-check/SKILL.md:480-500 |
| .claude/skills/regression-suite/SKILL.md | D | LEAVE | TAKE-MODIFY | Rename GDD to strategy spec and bug to model incident. Move bug records from production/qa/bugs to production/model-incidents. | A curated regression-coverage register tied to closed model incidents, so a defect cannot silently recur. | .claude/skills/regression-suite/SKILL.md:156-172; .claude/skills/regression-suite/SKILL.md:307-321 |
| .claude/skills/test-evidence-review/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Rename sign-off roles to Analyst, Portfolio-Manager, Compliance, or Author, Independent-Validator, Model-Risk. Apply the automated-test-quality section only with a code pipeline. | A quality, not just existence, review of model validation evidence and sign-off completeness. | .claude/skills/test-evidence-review/SKILL.md:123-127; .claude/skills/test-evidence-review/SKILL.md:149-154; .claude/skills/test-evidence-review/SKILL.md:208-224 |
| .claude/skills/test-flakiness/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace JUnit-XML and engine log parsing with pytest and CI output parsing. Replace the scene-load-race cause with a data-snapshot timing race. | Backtest or pipeline flakiness triage with a quarantine-not-delete rule, an audit trail of known gaps. | .claude/skills/test-flakiness/SKILL.md:109-127; .claude/skills/test-flakiness/SKILL.md:211-219 |
| .claude/skills/security-audit/SKILL.md | D | TAKE-MODIFY | TAKE-MODIFY | Change Category 1 to trade or order record tamper-evidence. Change Category 2 to a server-side leverage check. Drop Category 5; add a code-access-control category. | A category-by-category audit with a never-guess-the-pattern-set rule; a new category covers code access control. | .claude/skills/security-audit/SKILL.md:104-126; .claude/skills/security-audit/SKILL.md:185-191; .claude/skills/security-audit/SKILL.md:240-254 |
| .claude/skills/propagate-design-change/SKILL.md | D | TAKE-MODIFY | TAKE-MODIFY | Rename design/gdd to design/strategy or docs/policy. Rename docs/architecture/adr files to docs/decisions files. Read ADR as any decision record that governs, without a code pipeline. | Design or policy-change impact propagation onto the decision records that govern it, whether or not code exists. | .claude/skills/propagate-design-change/SKILL.md:51-66; .claude/skills/propagate-design-change/SKILL.md:130-151; .claude/skills/propagate-design-change/SKILL.md:185-210 |
| .claude/skills/reverse-document/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace the design template target with a strategy-spec-from-implementation target. Replace the architecture template with a decision-record-from-code target. Keep the provenance-stamping banner unchanged. | Backfill of a model or strategy spec from undocumented legacy code, with inferred intent marked unconfirmed. | .claude/skills/reverse-document/SKILL.md:117-144; .claude/skills/reverse-document/SKILL.md:185-192; .claude/skills/reverse-document/SKILL.md:221-246 |
| .claude/skills/qa-plan/SKILL.md | R | CONDITIONAL | TAKE-MODIFY | Drop the Visual/Feel rows and the Playtest Requirements section. Reclassify Config/Data evidence to match story-done, create-stories, and dev-story. | A pre-cycle test or review plan that classifies stories by type, with clear entry and exit rules. | .claude/skills/qa-plan/SKILL.md:153-159; .claude/skills/qa-plan/SKILL.md:225-241; .claude/skills/qa-plan/SKILL.md:71-93 |
| .claude/skills/team-qa/SKILL.md | R | CONDITIONAL | TAKE-MODIFY | Rename qa-lead and qa-tester to model-validator and quant-reviewer. Rename bugs to model incidents. Link smoke-check to the daily pipeline health check. | A QA-cycle orchestration that ends in an Approved, Conditions, Not-Approved, or Not-Assessed verdict, never vacuous. | .claude/skills/team-qa/SKILL.md:274-297; .claude/skills/team-qa/SKILL.md:43-66 |
| .claude/skills/team-release/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Rename qa-lead to model-validation-lead and community-manager to investor relations. Rename network-programmer to execution or connectivity engineer. Keep the no-go override rule. | A go or no-go release orchestration with a mandatory approval step before any irreversible action. | .claude/skills/team-release/SKILL.md:161-176; .claude/skills/team-release/SKILL.md:179-186; .claude/skills/team-release/SKILL.md:91 |
| .claude/skills/release-checklist/SKILL.md | R | LEAVE | CONDITIONAL | Change Build Verification to a model or strategy deployment package check. Drop the Steamworks, itch, and console certification blocks; they have no analogue. | A narrow deployment-package build and quality check, mostly redundant with team-release. | .claude/skills/release-checklist/SKILL.md:122-148; .claude/skills/release-checklist/SKILL.md:19-55; .claude/skills/release-checklist/SKILL.md:218-227 |
| .claude/skills/launch-checklist/SKILL.md | R | TAKE-MODIFY | TAKE-MODIFY | Keep Code Readiness only with a code pipeline. Rename Content and Store sections to Strategy and Investor/Distribution Readiness. Rename sign-offs to CCO, CRO, COO, CEO. | A cross-departmental fund or strategy launch-readiness gate with one go or no-go and named executive sign-offs. | .claude/skills/launch-checklist/SKILL.md:19-55; .claude/skills/launch-checklist/SKILL.md:117-328; .claude/skills/launch-checklist/SKILL.md:323-328 |
| .claude/skills/perf-profile/SKILL.md | D | LEAVE | TAKE-MODIFY | Replace hot-path scanning with vectorized-versus-loop data-processing scanning, data-pull latency, and order-routing round-trip latency. Drop the draw-call and overdraw content. | A latency or capacity check against committed budgets, with a clear accept, fix, or escalate rule. | .claude/skills/perf-profile/SKILL.md:19-46; .claude/skills/perf-profile/SKILL.md:78-114; .claude/skills/perf-profile/SKILL.md:201-213 |
| .claude/skills/soak-test/SKILL.md | D | LEAVE | CONDITIONAL | Drop the balance or fatigue items. Change durations to one trading day or one trading week. Keep the unit-as-displayed, delta-from-baseline rule. | Extended-run leak or drift detection for any live trading or risk-monitoring system that runs continuously. | .claude/skills/soak-test/SKILL.md:102-114; .claude/skills/soak-test/SKILL.md:276-286 |

### 5.11 skills — design-domain donors (23)

| Component | T2 | HF verdict | Condition | Required change | Hedge-fund use | Evidence |
|---|---|---|---|---|---|---|
| .claude/skills/brainstorm/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for a fund-thesis brainstorm skill: pillar, anti-pillar, and per-pillar design-test pattern. | .claude/skills/brainstorm/SKILL.md:262-268; .claude/skills/brainstorm/SKILL.md:269-272 |
| .claude/skills/map-systems/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for a workstream-decomposition skill: dependency layers, circular-dependency detection, and priority tiers. | .claude/skills/map-systems/SKILL.md:172-193; .claude/skills/map-systems/SKILL.md:211-222 |
| .claude/skills/design-system/SKILL.md | R | LEAVE | — | Do not transplant. | Richest donor in the batch: seeds an investment-memo skill from its section-cycle and specialist-routing table. | .claude/skills/design-system/SKILL.md:495-546; .claude/skills/design-system/SKILL.md:1162-1202; .claude/skills/design-system/SKILL.md:699-726 |
| .claude/skills/design-review/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for an Investment Committee memo review: adversarial parallel specialist review with a NOT ASSESSED rank. | .claude/skills/design-review/SKILL.md:183-219; .claude/skills/design-review/SKILL.md:296-307; .claude/skills/design-review/SKILL.md:47-86 |
| .claude/skills/review-all-gdds/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for a cross-policy consistency review: dependency, contradiction, and formula-range checks, plus a scenario walkthrough. | .claude/skills/review-all-gdds/SKILL.md:159-181; .claude/skills/review-all-gdds/SKILL.md:383-408; .claude/skills/review-all-gdds/SKILL.md:500-541 |
| .claude/skills/prototype/SKILL.md | R | LEAVE | — | Do not transplant. | Strongest donor for a paper-trading pilot skill: falsifiable hypothesis, structured debrief, and a KILL checklist. | .claude/skills/prototype/SKILL.md:76-84; .claude/skills/prototype/SKILL.md:375-399; .claude/skills/prototype/SKILL.md:478-487 |
| .claude/skills/vertical-slice/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for an end-to-end investment-cycle dry run: validation question, velocity log, and a distinct KILL checklist. | .claude/skills/vertical-slice/SKILL.md:62-66; .claude/skills/vertical-slice/SKILL.md:220-228; .claude/skills/vertical-slice/SKILL.md:322-330 |
| .claude/skills/art-bible/SKILL.md | W | LEAVE | — | Do not transplant. | Donor for the collaborative-draft discipline only: batch interdependent sections into one specialist call, not several. | .claude/skills/art-bible/SKILL.md:329-334; .claude/skills/art-bible/SKILL.md:127-134 |
| .claude/skills/asset-audit/SKILL.md | W | LEAVE | — | Do not transplant. | Donor for the NOT ASSESSED, never-fabricated-estimate pattern, useful for any hedge-fund data-quality report. | .claude/skills/asset-audit/SKILL.md:18-22; .claude/skills/asset-audit/SKILL.md:42-52 |
| .claude/skills/asset-spec/SKILL.md | W | CONDITIONAL | Q24 = B or C | If in-house collateral is chosen, reuse the sequential asset-ID scheme and the shared-asset dedup protocol. | Donor for an investor-collateral spec skill, if collateral production stays in-house rather than outsourced. | .claude/skills/asset-spec/SKILL.md:325-335; .claude/skills/asset-spec/SKILL.md:339-349 |
| .claude/skills/balance-check/SKILL.md | D | LEAVE | — | Do not transplant. | Strongest numeric-rule donor: dominant-strategy detection seeds leverage-cap, loss-rule, and exposure-limit outlier checks. | .claude/skills/balance-check/SKILL.md:94-99; .claude/skills/balance-check/SKILL.md:18-32 |
| .claude/skills/content-audit/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for a mandate-vs-executed-portfolio reconciliation audit, with a gap-status table and a HIGH PRIORITY flag rule. | .claude/skills/content-audit/SKILL.md:196-217; .claude/skills/content-audit/SKILL.md:43-57 |
| .claude/skills/playtest-report/SKILL.md | R | LEAVE | — | Do not transplant. | Donor for a post-trade post-mortem skill: four-bucket result routing with a director sign-off gate. | .claude/skills/playtest-report/SKILL.md:107-119; .claude/skills/playtest-report/SKILL.md:123-140 |
| .claude/skills/ux-design/SKILL.md | D | CONDITIONAL | Q24 = B | If an investor portal is built in-house, reuse the section-cycle draft flow and the coverage-check machinery. | Donor for a specification skill, if the fund builds an investor-facing portal or dashboard in-house. | .claude/skills/ux-design/SKILL.md:568-589; .claude/skills/ux-design/SKILL.md:622-648 |
| .claude/skills/ux-review/SKILL.md | D | CONDITIONAL | Q24 = B | If an investor portal exists, reuse the gate that reports NOT ASSESSED, never COMPLIANT, against an uncommitted standard. | Donor for a compliance-gate pattern: it checks a proposal against a risk-limits document that may not exist yet. | .claude/skills/ux-review/SKILL.md:242-254 |
| .claude/skills/setup-engine/SKILL.md | D | CONDITIONAL | Q22 includes A | If a guided vendor or jurisdiction-selection skill is wanted, reuse the tradeoffs-table interaction pattern only. | Weak, low-priority donor for a custodian, administrator, or jurisdiction-selection skill built as a guided decision tree. | .claude/skills/setup-engine/SKILL.md:60-64; .claude/skills/setup-engine/SKILL.md:88-106; .claude/skills/setup-engine/SKILL.md:162-174 |
| .claude/skills/team-audio/SKILL.md | D | LEAVE | — | Do not transplant. | Orchestration-skeleton donor: config resolve, active-set announcement, bounded write exception, and error-recovery protocol. | .claude/skills/team-audio/SKILL.md:46-53; .claude/skills/team-audio/SKILL.md:93 |
| .claude/skills/team-combat/SKILL.md | D | LEAVE | — | Do not transplant. | Fullest orchestration template for an Investment Committee skill: gated review, parallel execution, and sign-off. | .claude/skills/team-combat/SKILL.md:142-153; .claude/skills/team-combat/SKILL.md:155-160; .claude/skills/team-combat/SKILL.md:181-191 |
| .claude/skills/team-level/SKILL.md | D | LEAVE | — | Do not transplant. | Donor for cross-workstream dependency checks and a BLOCKING-severity gate the user must acknowledge. | .claude/skills/team-level/SKILL.md:111-120; .claude/skills/team-level/SKILL.md:136-144; .claude/skills/team-level/SKILL.md:176-181 |
| .claude/skills/team-live-ops/SKILL.md | R | LEAVE | — | Do not transplant. | Best orchestration donor for an IC compliance gate: block sign-off on a policy violation, force a decision. | .claude/skills/team-live-ops/SKILL.md:159-161; .claude/skills/team-live-ops/SKILL.md:161-164 |
| .claude/skills/team-narrative/SKILL.md | W | LEAVE | — | Do not transplant. | Donor for a fixed destination-path table and an i18n compliance check, useful for bilingual investor communications. | .claude/skills/team-narrative/SKILL.md:92-105; .claude/skills/team-narrative/SKILL.md:155 |
| .claude/skills/team-polish/SKILL.md | D | LEAVE | — | Do not transplant. | Donor for a pre-launch operational-readiness skill: assessment, Hardening phase, and a binary READY verdict. | .claude/skills/team-polish/SKILL.md:160-172; .claude/skills/team-polish/SKILL.md:110-116 |
| .claude/skills/team-ui/SKILL.md | D | LEAVE | — | Do not transplant. | Donor for two input-integrity habits: report every input's presence, and never let an unwritten standard pass. | .claude/skills/team-ui/SKILL.md:115-118; .claude/skills/team-ui/SKILL.md:120-129 |

## 6. Silent-break checklist (SB-01 .. SB-28)

design-spec section 2 lists 28 silent-break points: 13 carried over
from the original review, re-verified in this assessment, and 15 new
points found in this assessment. Every point must become a test.

Detection has 3 values. Silent means the break gives no error and no
warning. Loud means the harness or a hook refuses the action outright.
Misleading means the break gives a result that looks valid but is
wrong.

P3 items are foundation-transplant checks: run them as the hooks,
scripts, and config schema in §4 and §5.1-5.4 are transplanted. P4
items are control-spine checks: run them as the control model in
design-spec §5 is built. Retest every item at the P7 end-to-end dry
run.

| ID | Location | Trigger | Symptom | Detection | Test method (P3/P4) | Phase |
|---|---|---|---|---|---|---|
| SB-01 | validate-commit.sh:175 | design/gdd/ is renamed or replaced without updating the grep filter at line 175. | The GDD section-completeness check stops running on every commit. No error appears. | Silent | Rename the document directory. Commit a file with a missing required section. Confirm the hook still flags it. | P3 |
| SB-02 | detect-gaps.sh:70-72 | game-concept.md / game-brief.md paths are replaced without updating this check. | A finished project shows the NEW PROJECT notice on every session. | Misleading | Create the new concept-equivalent doc. Run the hook. Confirm the NEW PROJECT notice does not fire. | P3 |
| SB-03 | detect-gaps.sh:275-282 | The system-document naming rule changes without updating this check. | The missing-document check gives false positives or stops finding real gaps. | Silent | Add and remove a correctly named system doc. Confirm the check reports each case correctly. | P3 |
| SB-04 | pre-compact.sh:144 | design/gdd/ path changes without updating the glob at line 144. | The work-in-progress check returns an empty result. An empty result looks the same as “no WIP”. | Silent | Create a WIP document under the new path. Trigger compaction. Confirm the WIP check finds it. | P3 |
| SB-05 | review-scope.sh:34 + gdd-structure-check.sh:37-55 | The design-document path and exclusion list change without updating both scripts together. | Review scope is empty, or the wrong documents are checked as if they were GDDs. | Silent | Run both scripts against a fixture repo with the new path layout. Confirm the same document set. | P3 |
| SB-06 | yaml-helper.sh:1236-1239 (resolve_code_root) | engine.name is replaced by a new archetype key without adding a matching case arm. | code root resolves to an empty value. The project looks like it has no code, even when it does. | Silent | Set archetype=quant with code-pipeline=yes. Call resolve_code_root. Confirm it returns a real path or a documented GAP, not a silent empty value. | P3 |
| SB-07 | yaml-helper.sh:472 (engine.name enum, loud) | project.stage or another enum value is set to a new name not yet added to this table. | Every session start rejects the new value. | Loud | Set the new enum value. Start a session. Confirm the rejection message names the value and the allowed list. | P3 |
| SB-08 | validate-assets.sh:68 | assets/ is replaced by a new structured-data directory without repointing the path filter. | The whole hook no-ops on every write. It never blocks a bad file. | Silent | Write a file with a naming violation under the new directory. Confirm the hook blocks it. | P3 |
| SB-09 | statusline.sh:60-136 (stage auto-detect) | .gd/.tscn extensions and the stage-detect heuristic are not replaced for the new file types. | The status line keeps showing the first lifecycle stage forever, regardless of real progress. | Silent | Advance project.stage by hand. Confirm the status line reflects the change, or is replaced by a direct read of project.stage. | P3 |
| SB-10 | workflow-catalog.yaml + artifact-check.sh | Artifact paths in the catalog are renamed without checking artifact-check.sh’s parser against them. | Every phase reports ABSENT even when the equivalent artifact exists. | Misleading | Create the renamed artifact. Run artifact-check.sh --phase. Confirm it reports PRESENT. | P3 |
| SB-11 | CONTRACT.md vs SKILL.md (story-done, story-readiness) | SKILL.md is edited without the matching CONTRACT.md edit. | gate-check reads the stale CONTRACT.md and returns a verdict that does not match the current SKILL.md behavior. | Silent | Edit one skill’s SKILL.md only. Run gate-check. Confirm it flags the CONTRACT.md/SKILL.md mismatch, or fails visibly rather than returning a false PASS. | P3 |
| SB-12 | tools: Agent(...) allow-lists (engine-lead agents, loud) | A sub-specialist agent is renamed without updating the lead agent’s allow-list. | The harness refuses the call to the renamed agent. | Loud | Rename one sub-specialist. Call it from the lead agent. Confirm the harness refusal names the missing allow-list entry. | P3 |
| SB-13 | CCGS Skill Testing Framework/catalog.yaml + quality-rubric.md + CLAUDE.md + README.md (loud for audit/spec) | A skill or agent file is renamed without updating all 4 registry files (123 name: entries). | audit mode reports an item with no matching file; spec mode fails against the old behavior. | Loud (for audit/spec) | Rename one skill. Run /skill-test audit and /skill-test spec. Confirm both surface the mismatch by name. | P3 |
| SB-14 | yaml-helper.sh:473 (project.stage enum) + :843-846 + :1149-1151 (resolve_setting fall-through) | project.yaml sets project.stage to a new lifecycle name without updating the enum at line 473 in the same commit. | The new stage name is silently rejected. statusline.sh and gate-adjacent logic keep reporting the old or default stage forever. The rejection is visible only on a notes: line almost nobody reads. | Silent | Set project.stage to the new lifecycle name. Read it back through resolve_setting. Confirm it returns the new value, not a silent fallback. | P3 |
| SB-15 | detect-gaps.sh:41-116 (FRESH_PROJECT gate) | None of the 3 conditions that clear FRESH_PROJECT (engine.name set, concept doc present, code-root scan) can become true without a rewrite, because engine.name is replaced by archetype and the code-scan extensions are game-language-specific. | The onboarding hook is stuck in “fresh project” forever, on any project of any age. Checks 1-6 never run. | Silent | Set up a complete, mature fixture project under the new schema. Run detect-gaps.sh. Confirm FRESH_PROJECT clears and Checks 1-6 run. | P3 |
| SB-16 | session-start.sh:272-285 (engine-reference-mismatch check) | CLAUDE.md in the new repo has no @docs/engine-reference/[a-z]+/VERSION.md import line, which is the expected, correct state for a hedge fund. | The block no-ops every session, forever. This is dead code, not a dangerous failure, but it should not be mistaken for a working control. | Silent (fails safe) | Start a session in the new repo. Confirm the block does not fire and is documented as intentionally inert, not a working check. | P3 |
| SB-17 | effects-map.md:1230-1253 (strict_gate_checks) | A founder sets strict_gate_checks: true (or a hedge-fund equivalent key) believing it makes a CRO/CCO REJECT verdict a hard stop. | The value round-trips cleanly through /settings, looks configured, and produces no observable difference in behavior. No skill or hook reads it. | Silent | Set the key to true. Force a REJECT verdict from a gate. Confirm the run actually stops, not just that the key was accepted. | P4 |
| SB-18 | gate-check/SKILL.md:604-623; director-gates.md:127-135 (verdict parser keyed to “REJECT”) | A new CRO/CCO gate is modeled on the existing director-gate verdict pattern (a spawned agent returning a text verdict) instead of a hook. | Nothing in the codebase prevents the orchestrating skill from proceeding anyway. The stop is an instruction the model is told to follow, not a permission-system check. | Silent (visible only via after-the-fact audit) | Return a blocking verdict word the parser does not recognize (one of the 8 other vocabularies). Confirm the calling skill still halts. | P4 |
| SB-19 | director-gates.md:75 (modes.review_mode default = lean) | A CRO/CCO per-decision gate is invoked the same way TD-ADR or LP-CODE-REVIEW are invoked today, without hard-wiring it outside review_mode. | The gate is OFF by default from day one. The calling skill prints “[GATE-ID] skipped -- Lean mode” and proceeds. No error. | Silent (unless someone reads the transcript) | Run the gate at review_mode: lean. Confirm the CRO/CCO seat still runs and the verdict is not silently skipped. | P4 |
| SB-20 | team-*/SKILL.md team.size default (7 files, e.g. team-combat/SKILL.md:40-44) | team.size stays at its default, individual. | A CRO/CCO-equivalent agent silently routes through the nearest core agent “with an informational note” instead of being spawned. This is indistinguishable from a real independent review unless the reader checks the Active-set line. | Silent | Run the Investment Committee skill at team.size: individual. Confirm CRO and CCO appear by name in the Active-set line, not folded into another role. | P4 |
| SB-21 | gate-check/SKILL.md:385-400 (director-panel width scales with modes.workflow) | A CCO/CRO seat is folded into the existing tier-scaled director panel (1 seat at minimal, 2 at standard, 4 at full) instead of made a fixed seat. | Running gate-check at workflow: minimal or review_mode: solo during early build-out silently drops compliance/risk review from the phase-gate verdict. The gate still returns PASS. | Silent | Run gate-check at workflow: minimal and review_mode: solo on a fixture with a known risk/compliance defect. Confirm the verdict names the missing review, not PASS. | P4 |
| SB-22 | help/SKILL.md:70-77 (hardcoded phase-name-to-key table) | workflow-catalog.yaml is swapped for hedge-fund phases in one commit, but this separate inline table is not updated in the same commit. | /help does not error. It falls through its own artifact-inference heuristics or the “Nothing -> concept” default, quietly reporting a plausible but wrong phase. | Silent | Set project.stage to a new-catalog phase name not yet in this table. Run /help. Confirm it does not silently default to the first phase. | P3 |
| SB-23 | coding-standards.md 5-row test-evidence-by-story-type table | A Trade/Model Validation Evidence record does not fit any of the 5 existing rows (Logic/Integration/Visual/UI/Config). | This evidence type has no defined default gate level. A skill checking it could default to treating it as satisfied when no explicit override is set. | Silent | Submit a model-validation story with no explicit gate-level override. Confirm the story is NOT ASSESSED, not silently PASS. | P4 |
| SB-24 | create-stories Test Evidence template:389-399; dev-story Phase 4/5:355,403-446; story-done Default Gate Level table:228-246 (3 skills) | testing.strict.config is reclassified from ADVISORY to BLOCKING for the quant archetype in story-done only, while create-stories’ template and dev-story’s briefing are left at the old ADVISORY assumption. | Every Config/Data story closes BLOCKED with no evidence found, and no story was ever asked to produce the evidence at implementation time. A dead end, not a fixable finding. | Silent | Flip testing.strict.config to BLOCKING. Run a Config/Data story end to end. Confirm create-stories asks for the evidence artifact before dev-story implements it. | P4 |
| SB-25 | create-stories Story Type table:169-180; dev-story routing table:241-251; story-done evidence table:228-234; qa-plan:153-159; code-review Phase 7; test-evidence-review §4-5; smoke-check coverage table (7 skills) | Each of the 7 skills is authored fresh in its own session (Strategy C), and independently decides how to relabel or drop Visual/Feel and UI. | The same story is typed inconsistently across the 7 skills that share this taxonomy, silently breaking type-based routing and evidence gating. | Silent | Author all 7 skills from one shared taxonomy table (§7 lockstep set 2). Type one story. Confirm all 7 skills agree on its type. | P4 |
| SB-26 | tech-debt/SKILL.md:114 (priority score formula) | (impact_if_unfixed × frequency_of_encounter) / fix_effort has no time/deadline term. | A compliance gap tied to a hard regulatory filing deadline scores identically to an unrelated item of equal impact/effort. It can sit at moderate priority indefinitely as the deadline approaches. | Silent | Add a control-gap item with a near-term regulatory deadline and low impact/effort scores. Confirm the register does not bury it below unrelated higher-scored items. | P4 |
| SB-27 | design-review.md:47-86 (freshness/receipt skip) | The byte-identical-skip optimisation is reused for an IC-memo re-review skill, hashing only the memo text, not the market/risk data it references. | A memo whose referenced numbers are stale (price moved, a limit changed) reports “unchanged since last review, prior APPROVED verdict stands” on a live-capital decision. | Silent | Change a referenced risk figure without changing the memo prose. Re-run the review. Confirm it does NOT report “unchanged”. | P4 |
| SB-28 | team-live-ops.md:159-161 (policy gate, “policy file absent” branch) | The ethics-policy gate pattern is adapted for an IC compliance gate, keeping only the “violation found -> block” half and dropping the “policy file does not exist yet -> flag, do not silently pass” half. | A fund with no risk-limits document yet passes every IC review by default, on every trade, until someone authors the policy file. | Silent | Run the gate with no policy file present. Confirm it flags the absence and does not return an APPROVE. | P4 |

## 7. Lockstep change sets

Each set below is a group of files. Every file in a set must change
in the same commit. A commit that changes only some files in a set
leaves the other files with stale data. This gives no error. §6
lists the matching silent-break IDs for sets 1-3.

**Set 1. project.stage enum + statusline + help table + detect-gaps +
gate-check.** Change these files together:
- yaml-helper.sh:473, the enum.
- statusline.sh:60-136, the stage-auto-detect block.
- help/SKILL.md:70-77, the phase-name table.
- detect-gaps.sh:41-116, the FRESH_PROJECT gate.
- gate-check’s stage-write logic.

Matches SB-07, SB-09, SB-14, SB-15, SB-22.

**Set 2. Story-type taxonomy in 7 skills.** Change these files
together:
- create-stories Story Type table, lines 169-180.
- dev-story routing table, lines 241-251.
- story-done evidence table, lines 228-234.
- qa-plan classification table, lines 153-159.
- code-review Phase 7.
- test-evidence-review Sections 4-5.
- smoke-check coverage table.

Matches SB-25.

**Set 3. Config/Data evidence default in 3 skills.** Change these
files together:
- create-stories Test Evidence template, lines 389-399.
- dev-story Phase 4 item 7 and Phase 5, lines 355 and 403-446.
- story-done Default Gate Level table, lines 228-246.

Matches SB-24 and SB-23.

**Set 4. Skill Testing Framework, 4 registries.** Change these files
together:
- CCGS Skill Testing Framework/catalog.yaml.
- CCGS Skill Testing Framework/quality-rubric.md.
- CCGS Skill Testing Framework/CLAUDE.md.
- CCGS Skill Testing Framework/README.md.

All 4 files carry the same 123 name: entries (74 skills + 49 agents).
Matches SB-13.

**Set 5. design-docs rule + gdd-structure-check + review-scope.**
Change these files together:
- .claude/rules/design-docs.md, the frontmatter path convention.
- gdd-structure-check.sh, the section list and exclusion glob.
- review-scope.sh:34, the design-document path, and its exclusion
  list at lines 38-44.

Matches SB-05.

**Set 6. control-manifest header date readers.** Change these files
together:
- story-readiness CONTRACT.md’s manifest-version note.
- create-stories.
- dev-story.
- story-done.

Each of the 4 files above independently compares a story’s embedded
Manifest Version string against the header date of
docs/architecture/control-manifest.md. The comparison is a plain
string match, not a semantic version comparison. A rename of
control-manifest.md to a Trading-and-Compliance Control Manifest
breaks this check, unless all 4 readers change in the same commit.
Staleness detection then stops on every open story at once. This
gives no error.

## 8. Corrections applied

This section lists every verifier correction and every Advisor
override this manifest applied, and where.

### 8.1 Verifier corrections (verifier-issues.md)

1. **yaml-helper.sh project.stage citation.** The infra CONFIG KEYS
   finding cited yaml-helper.sh:473,1589-1614 for the
   single-authoritative-value mechanism. The file is 1590 lines long;
   lines 1591-1614 do not exist, and 1589-1590 are the unrelated CLI
   dispatcher tail. Corrected to yaml-helper.sh:473, 1057-1060,
   1149-1177. Applied in §5.4 (config keys, project.stage row).
2. **create-epics minimal-tier citation.** The quote “minimal tier --
   synthesize the epic from the brief” was cited at
   create-epics/SKILL.md:91-104. It does not exist there; it belongs
   to create-stories/SKILL.md:91-99. create-epics’s own minimal tier
   (lines 28-40) is “optional, skipped”, not a synthesis step.
   Corrected in §5.10 (skills-pipeline, create-epics row): evidence
   now cites create-epics/SKILL.md:28-40, and the condition field no
   longer attributes the synthesis mechanism to create-epics itself.
3. **help/SKILL.md stage-table citation.** Cited at lines 96-105 in
   2 places (the workflow-catalog.yaml component and the content-qa
   silent_breaks entry). The real content is at line 70 (the mapping
   instruction) and lines 71-77 (the 7-row table). Lines 96-105 cover
   an unrelated step. Corrected in §5.3 (workflow-catalog.yaml row)
   and in SB-22 (§6), both of which now cite help/SKILL.md:70-77.
4. **workflow-catalog.yaml step counts.** Stated as
   concept(5)->systems-design(4)->technical-setup(5)->pre-production(11)
   ->production(9)->polish(5)->release(4). A direct count of `- id:`
   entries gives concept=6, systems-design=4, technical-setup=5,
   pre-production=10, production=11, polish=5, release=4 (45 steps
   total, not the ~43 the wrong counts implied). Corrected in §5.3
   (workflow-catalog.yaml row).
5. **propagate-design-change T1 rating.** Stated as T1=K and as the
   “ONLY” skill in its batch with that rating. mapping.txt line 37
   shows T1=W. The assessment’s own text names create-epics and
   regression-suite as also T1=K elsewhere; the corrected T1=K set is
   create-epics, regression-suite, and test-evidence-review. Corrected
   in §5.10 (skills-pipeline, propagate-design-change row).
6. **“Two Sigma” fact citations.** The source stated this fact 2 of 3
   times with no citation. Every occurrence of this fact in this
   manifest now cites HF-REF-12 §7.8 and HF-REF-14 §8.5 (SRC-50).
   These are the 2 chunks that carry the Two Sigma model-governance
   lesson. This applies to: the code-governance gates row (§5.7); the
   technical-director, lead-programmer, devops-engineer, and
   prototyper agent rows (§5.8); and the propagate-design-change,
   code-review, and launch-checklist skill rows (§5.10).
7. **dev-story / code-review “independent validation” claim (F-09).**
   dev-story, architecture-decision, architecture-review,
   create-architecture, and code-review each spawn an
   engine-specialist sub-agent. The source described this sub-agent
   as independent validation. Per F-09, a same-session sub-agent is a
   pre-screen, not an organizationally independent reviewer. A human
   with a separate reporting line must still sign. Corrected in §5.10:
   the code-review row renames its Phase 7 to “Independent Validation
   Pre-Screen”. The dev-story row’s donor/use cell carries the same
   caveat. The same caveat also applies to architecture-decision,
   architecture-review, and create-architecture. Their table rows in
   §5.10 do not repeat the wording. None of their source cells used
   the words “independent validation”.
8. **Config keys, 2 missing entries.** strict_gate_checks
   (effects-map.md:1230-1253) and features.token_budget_warn_at
   (effects-map.md:2123-2139; yaml-helper.sh:528) were absent from the
   CONFIG KEYS findings entirely. Added in §5.4. strict_gate_checks is
   TAKE-MODIFY: implement it, or replace it with the protected-path
   hook design in design-spec §5; today it does nothing.
   features.token_budget_warn_at is TAKE: documented in 3 places, but
   wired in exactly 1.
9. **Skill Testing Framework templates, 2 missing files.**
   skill-test-spec.md and agent-test-spec.md sit under `CCGS Skill
   Testing Framework/templates/`. The task named both files in scope.
   Neither file was ever opened, quoted, or given a verdict. Added in
   §5.3 as TAKE.

### 8.2 Advisor overrides (design-spec F-02 and this task)

10. **skills gate-check and start.** Worker verdict: CONDITIONAL.
    Advisor override: TAKE-MODIFY. The transplant itself is certain;
    only the required changes depend on Q14 (control-seat scaling) and
    Q17 (lifecycle design). Applied in §5.9 (skills-management,
    gate-check and start rows). patch-notes keeps its worker verdict,
    CONDITIONAL, pending the IR-track decision (Q22=E).
11. **director gates, 4 missing files.** td-change-impact.md and
    td-feasibility.md were absent from the assessment. Advisor
    verdict: TAKE-MODIFY. td-engine-risk.md and ql-story-ready.md were
    also absent. Advisor verdict: CONDITIONAL on Q25=C/D. Added in
    §5.7 (director gates). This brings the area total from 24
    assessed files to the full 28.
12. **rules, agent-memory.md.** The agents-gates area’s own component
    row rated this TAKE. The content-qa area’s row (the authoritative,
    complete 13-rule pass) already rated it TAKE-MODIFY. Advisor
    override: TAKE-MODIFY, swap the worked example. This manifest uses
    the content-qa row. It already matches the override; no further
    change was needed there.

### 8.3 Net effect on the F-02 count

This manifest applied every override above. §3 Table 3-2 shows the
row-by-row count from this manifest matches F-02 exactly, area by
area and verdict by verdict. F-02 stays unedited. §3 Table 3-2
states the independently-computed check next to Table 3-1 (F-02
verbatim) and reports the match.

## 9. Effect of founder decisions DEC-01 to DEC-16

[design-addendum-01.md](evidence/design-addendum-01.md) records the
founder's decisions DEC-01 to DEC-16 and the mission reset (DEC-09).
This section states the effect on this manifest.

### 9.1 The verdict counts stay the same

Table 3-1 and Table 3-2 do not change. Both tables describe transplant
fitness: whether a component transplants with no change, transplants
with a rewrite, depends on a founder decision, or stays behind. The
mission reset changes the build order. It does not change any
component's transplant fitness. §3 stays the authoritative count.

### 9.2 DEC-05 and the Q25 conditional set

DEC-05 picks the single-manager fundamental archetype. This keeps
every Q25-conditional item off, unless the founder answers Q25 as C or
D (round 7, not yet run). §5.10's code-pipeline branch, and every
CONDITIONAL row keyed to Q25 in §5.4, §5.6, §5.7, §5.8, and §5.9, wait
on that answer.

### 9.3 The transplant order for wave W1

Wave W1 (addendum §3, §4) is the information core: 11 agents and 14
information-product skills. Before this wave builds, the new
repository needs these transplants first:

- The minimum transplant set, §4, in the transplant order §4 states.
- `.claude/skills/gate-check/`, for the PASS, CONCERNS, NOT ASSESSED,
  or FAIL verdict every W1 product needs.
- `.claude/skills/consistency-check/SKILL.md`, rewritten as the fact
  registry every stock call and house-view cites (addendum §6;
  DEC-16).
- `.claude/skills/skill-test/SKILL.md`, to run the static and category
  checks on every new W1 skill.
- `.claude/skills/sprint-plan/SKILL.md` and
  `.claude/skills/sprint-status/SKILL.md`, to run the W1 build cycle.
- `.claude/skills/scope-check/SKILL.md`, to catch scope creep past the
  W1 roster.
- `.claude/skills/retrospective/SKILL.md`, to close each cycle.
- `.claude/skills/help/SKILL.md` and `.claude/skills/onboard/SKILL.md`,
  for orientation once the W1 agents exist.

### 9.4 The donors for the W1 skills

Addendum §6 names the CCGS donor skeleton for each W1 information
product.

**Table 9-1. W1 skill donors**

| W1 skill | Donor skeleton |
|---|---|
| `/stock-pitch` | design-system, the section-cycle draft flow |
| `/red-team-review` | design-review, the adversarial reviewer brief |
| The bull, bear, and synthesis sequence | The team-* skeleton, §5.11 |
| `/call-review` | post-mortem and playtest-report |
| The fact registry every product cites | consistency-check |
| `/idea-screen` | balance-check, the outlier-detection mechanism |

§5.9 and §5.11 carry the full transplant detail for each donor.

### 9.5 W2 transplants wait for wave W2

Wave W2, fund operation, activates when the founder starts fund
setup. The transplants that serve W2 functions wait for that trigger.
This set includes `.claude/skills/launch-checklist/SKILL.md`,
`.claude/skills/team-release/SKILL.md`,
`.claude/docs/templates/incident-response.md`,
`.claude/docs/templates/test-evidence.md`, and the other W2-only
components §5 lists. §8 does not change any of their verdicts; this
section states only when to build them.
