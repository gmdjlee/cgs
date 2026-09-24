# HFT-MAN-001 — Component-Level Transplant Manifest for Strategy C

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-MAN-001 |
| Title | Component-Level Transplant Manifest for Strategy C |
| Version | 0.1 |
| Date | 2026-09-24 |
| Status | Draft for founder review |
| Owner | Advisor (main session) |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules |
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

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/hooks/session-start.sh | W (mapping.txt: 'L273-281 엔진 레퍼런스 경로 검사') — agrees with TAKE-MODIFY. | TAKE-MODIFY |  | Delete/repoint BUG-*.md scan dirs; drop or gate the code-health block behind archetype=quant; delete the engine-reference-mismatch block (lines 267-285) or redesign it... | .claude/hooks/session-start.sh:118-143; .claude/hooks/session-start.sh:159-168; .claude/hooks/session-start.sh:182-194 | Branch/commit banner, review-mode resolution, schema validation, stage-source-agreement warning, and the session-state recovery preview (lines 30-116, 196-265) are fully... |
| .claude/hooks/detect-gaps.sh | R (mapping.txt: '게임 W R M L'). Hedge-fund verdict is less severe than T2's full redesign... | TAKE-MODIFY |  | The gap-detection PATTERN (fresh-project onboarding nudge, doc-vs-code drift check, stage-vs-artifact drift check at lines 297-327) is reusable, but every artifact name... | .claude/hooks/detect-gaps.sh:70; .claude/hooks/detect-gaps.sh:84-91; .claude/hooks/detect-gaps.sh:245-258 | The gap-detection PATTERN (fresh-project onboarding nudge, doc-vs-code drift check, stage-vs-artifact drift check at lines 297-327) is reusable, but every artifact name... |
| .claude/hooks/validate-commit.sh | W (mapping.txt: 'L175 ^design/gdd/ 필터, L304 damage·health 등 수치 정규식') — agrees, though... | TAKE-MODIFY |  | Repoint DATA_FILES glob from assets/data/ to the new risk-config/reference-data dir; repoint DESIGN_FILES glob and REQUIRED section vocabulary; replace hardcoded-value... | .claude/hooks/validate-commit.sh:114-150; .claude/hooks/validate-commit.sh:175-241; .claude/hooks/validate-commit.sh:243-310 | High hedge-fund value: this is the ONE blocking (exit 2) hook in the repo, and its hardcoded-gameplay-value scan (damage/health/speed/rate/chance/cost/duration) is... |
| .claude/hooks/validate-push.sh | K (mapping.txt) — agrees. | TAKE |  | Fully generic protected-branch warning with no build/test enforcement (the block path is commented out at line 71-72). | .claude/hooks/validate-push.sh:54-73 | Fully generic protected-branch warning with no build/test enforcement (the block path is commented out at line 71-72) |
| .claude/hooks/validate-assets.sh | W (mapping.txt: 'L68 assets/ 경로가 아니면 즉시 종료') — I mark CONDITIONAL rather than W because... | CONDITIONAL | GAP (no Q-ID assigned) | The naming-convention + JSON-validity-blocking mechanism is generic and cheap to repoint, but has no meaning without an assets/-equivalent directory in a hedge-fund repo. | .claude/hooks/validate-assets.sh:68-70; .claude/hooks/validate-assets.sh:79-81; .claude/hooks/validate-assets.sh:85-109 | The naming-convention + JSON-validity-blocking mechanism is generic and cheap to repoint, but has no meaning without an assets/-equivalent directory in a hedge-fund repo. |
| .claude/hooks/validate-skill-change.sh | K — agrees. | TAKE |  | Fully generic; fires on any .claude/skills/ edit and advises /skill-test. | .claude/hooks/validate-skill-change.sh:64-77 | Fully generic; fires on any .claude/skills/ edit and advises /skill-test |
| .claude/hooks/notify.sh | K — agrees. | TAKE |  | Fully generic Windows toast notification; zero domain coupling. | .claude/hooks/notify.sh:59-70 | Fully generic Windows toast notification; zero domain coupling |
| .claude/hooks/pre-compact.sh | W (mapping.txt: 'L144 design/gdd/*.md 글롭') — agrees. | TAKE-MODIFY |  | Repoint the design/gdd/*.md glob at line 144 to the new document directory. | .claude/hooks/pre-compact.sh:61-87; .claude/hooks/pre-compact.sh:105-126; .claude/hooks/pre-compact.sh:144-156 | Checkpoint-by-reference injection, bounded git-status lists, and compaction logging are fully generic and high-value |
| .claude/hooks/post-compact.sh | K — agrees. | TAKE |  | Fully generic reminder hook gated on features.session_state; no domain coupling anywhere. | .claude/hooks/post-compact.sh:44-51 | Fully generic reminder hook gated on features.session_state; no domain coupling anywhere. |
| .claude/hooks/session-stop.sh | K — agrees; flagged in reuse_patterns as high-value for hedge fund specifically. | TAKE |  | Fully generic; the content-hash-guarded state archive and the subagent spawn-tally/cost report are directly valuable for the task's investor-ODD/audit-trail requirement... | .claude/hooks/session-stop.sh:71-84; .claude/hooks/session-stop.sh:110-169 | Fully generic; the content-hash-guarded state archive and the subagent spawn-tally/cost report are directly valuable for the task's investor-ODD/audit-trail requirement... |
| .claude/hooks/log-agent.sh | K — agrees. | TAKE |  | Fully generic audit-trail hook; directly implements the 'investment decision records and audit trails' requirement named in the task. | .claude/hooks/log-agent.sh:76-79 | Fully generic audit-trail hook; directly implements the 'investment decision records and audit trails' requirement named in the task. |
| .claude/hooks/log-agent-stop.sh | K — agrees. | TAKE |  | Mirror of log-agent.sh for completion events; fully generic. | .claude/hooks/log-agent-stop.sh:76 | Mirror of log-agent.sh for completion events; fully generic. |
| .claude/hooks/log-instructions.sh | K (mapping.txt notes the same unwired state: '로드된 규칙·지침 파일 기록(settings.json에는 미연결)'). My... | TAKE-MODIFY |  | Add an 'InstructionsLoaded' hook entry to the new settings.json pointing at this script (does not exist upstream). | .claude/hooks/log-instructions.sh:29-53; .claude/settings.json:35-158 | Fully generic diagnostic that traces which rule/instruction file actually reached the model |
| .claude/hooks/yaml-helper.sh | W (mapping.txt: 'L472 engine.name 열거값, L1236-1239 엔진별 code root') — agrees with... | TAKE-MODIFY |  | Rewrite enum table lines 460-483 (drop game-specific rows, add jurisdiction/archetype); rewrite resolve_code_root lines 1206-1252 (new case arms or remove entirely if no... | .claude/hooks/yaml-helper.sh:460-483; .claude/hooks/yaml-helper.sh:1135-1177; .claude/hooks/yaml-helper.sh:1206-1252 | This IS the transplant core Strategy C names explicitly ('config resolver yaml-helper.sh') |

### 5.2 scripts (8)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/scripts/adr-dep-graph.sh | D for T2 (mapping.txt: 'T2에서는 ADR을 만들지 않으므로 쓸 곳이 없음'). Hedge-fund verdict SHARPLY DIFFERS... | TAKE |  | Fully generic ADR-dependency-graph and cycle-detector; reads docs/architecture/adr-*.md and a '## ADR Dependencies'/'**Depends On**' markdown convention. | .claude/scripts/adr-dep-graph.sh:1-31; .claude/scripts/adr-dep-graph.sh:108-143 | Fully generic ADR-dependency-graph and cycle-detector; reads docs/architecture/adr-*.md and a '## ADR Dependencies'/'**Depends On**' markdown convention |
| .claude/scripts/artifact-check.sh | K (mapping.txt: '경로는 카탈로그 데이터에서 읽음') — agrees. | TAKE |  | The script body is 100% generic and data-driven — all game-specificity lives in the external workflow-catalog.yaml it reads, not in this script's ~250 lines of... | .claude/scripts/artifact-check.sh:1-16; .claude/scripts/artifact-check.sh:225-262 | The script body is 100% generic and data-driven — all game-specificity lives in the external workflow-catalog.yaml it reads, not in this script's ~250 lines of... |
| .claude/scripts/gdd-structure-check.sh | R (mapping.txt: '게임 W R M L'). Aligns with T2's characterization; content is 100%... | TAKE-MODIFY |  | The grep-based section-presence-checker mechanism (tier-aware caller contract, reports presence only per its own header) is clean and reusable, but the entire... | .claude/scripts/gdd-structure-check.sh:30-46; .claude/scripts/gdd-structure-check.sh:49-55 | The grep-based section-presence-checker mechanism (tier-aware caller contract, reports presence only per its own header) is clean and reusable, but the entire... |
| .claude/scripts/migrate-v1-config.sh | K (mapping.txt: '주석과 메시지에만 부수적 언급'). My hedge-fund verdict DIFFERS from T2's K: T2's K... | LEAVE |  | None recommended; do not transplant. | .claude/scripts/migrate-v1-config.sh:3-27; .claude/scripts/migrate-v1-config.sh:490-493; .claude/scripts/migrate-v1-config.sh:595 | This script's entire reason for existing is migrating CCGS's OWN v1.0-to-v1.1 legacy file format |
| .claude/scripts/project-coherence.sh | D for T2, R for T1 (mapping.txt). Hedge-fund verdict leans toward T2's D (LEAVE) rather... | LEAVE |  | Every one of its 6 checks (engine version vs VERSION.md, vs installed binary, rendering/physics vs project.godot, build-command vs export_presets.cfg) is... | .claude/scripts/project-coherence.sh:79-119; .claude/scripts/project-coherence.sh:121-131; .claude/scripts/project-coherence.sh:148-191 | Every one of its 6 checks (engine version vs VERSION.md, vs installed binary, rendering/physics vs project.godot, build-command vs export_presets.cfg) is... |
| .claude/scripts/review-receipts.sh | K — agrees; flagged in reuse_patterns as especially high-value for a regulated entity. | TAKE |  | Fully generic content-hash (git hash-object) based 'has this document changed since it was last reviewed' tracker, plus section-level delta hashing. | .claude/scripts/review-receipts.sh:1-30; .claude/scripts/review-receipts.sh:130-146 | Fully generic content-hash (git hash-object) based 'has this document changed since it was last reviewed' tracker, plus section-level delta hashing |
| .claude/scripts/review-scope.sh | W (mapping.txt: 'L34 design/gdd 글롭, L38-44 제외 목록') — agrees. | TAKE-MODIFY |  | Repoint GDD_GLOB (line 34) and not_a_system_gdd() exclusion list (lines 38-44) to the new document directory/naming convention. | .claude/scripts/review-scope.sh:34; .claude/scripts/review-scope.sh:38-44; .claude/scripts/review-scope.sh:63-64 | The mechanism (find the most recent dated cross-review report, git-diff everything changed since it, follow declared Dependencies-section links into scope) is a strong,... |
| .claude/scripts/rotate-session-state.sh | K — agrees. | TAKE |  | Fully generic; rotates active.md's free-form narrative into a dated log while preserving the CHECKPOINT block, refuses safely on a malformed file, writes atomically. | .claude/scripts/rotate-session-state.sh:47-53; .claude/scripts/rotate-session-state.sh:97-103 | Fully generic; rotates active.md's free-form narrative into a dated log while preserving the CHECKPOINT block, refuses safely on a malformed file, writes atomically |

### 5.3 other infrastructure files (not counted in the 232)

settings.json, statusline.sh, project.yaml, .gitignore, coordination-rules.md, director-gates.md, model-tiers.md, automation-modes.md, workflow-modes.md, context-management.md, workflow-catalog.yaml, effects-map.md, code-root-resolution.md, and the CCGS Skill Testing Framework files. These support the 232 counted components. They are not counted themselves.

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/statusline.sh | Not itemized as its own row in mapping.txt's infra table, but named in review.txt's... | TAKE-MODIFY |  | Delete or fully rewrite lines 60-136 (auto-detect fallback) to match the new project.stage vocabulary and artifact set; keep everything else unmodified. | .claude/statusline.sh:60-136; .claude/statusline.sh:112-114; .claude/statusline.sh:138-175 | ctx%, model, rigor-posture, and the Epic>Feature>Task breadcrumb (reading active.md's STATUS block) are fully generic and high value (lines 37-58, 138-206) |
| .claude/settings.json | Not itemized as a separate row in mapping.txt's infra table; assessed independently... | TAKE-MODIFY |  | Update the hooks block to list only the kept hook files (drop entries for any hook marked LEAVE above); consider adding an InstructionsLoaded entry for... | .claude/settings.json:7-34; .claude/settings.json:35-158 | The overall shape (allow/deny permission philosophy, per-event hook wiring) is fully generic and directly reusable |
| project.yaml | Not itemized in mapping.txt (this is the live config file, not a schema doc); assessed... | TAKE |  | The single-YAML-source-of-truth pattern, comment-driven guardrails, and the explicit rule against hand-seeding rigor-fronted sub-keys are all generic and worth keeping... | project.yaml:1-8; project.yaml:10-22 | The single-YAML-source-of-truth pattern, comment-driven guardrails, and the explicit rule against hand-seeding rigor-fronted sub-keys are all generic and worth keeping... |
| .gitignore | Not itemized in mapping.txt; assessed independently. | TAKE-MODIFY |  | Remove the three engine-specific blocks (lines 49-107) and the docs/consistency-failures.md line (34, unless a like-named skill is kept); keep everything else. | .gitignore:12-23; .gitignore:49-107; :130-137 | The Claude-Code-local section (lines 12-23) and the secrets section (lines 130-137) are exactly the highest-value lines for a regulated entity and should be kept... |
| .claude/docs/coordination-rules.md | Not itemized separately in mapping.txt (it is an infra doc, not in the... | TAKE-MODIFY |  | Add an explicit non-override clause for CRO/CCO output (current rule 5 only protects file directories, not review authority); make CRO/CCO co-equal Tier-1 escalation... | .claude/docs/coordination-rules.md:7-9; .claude/docs/coordination-rules.md:12-13 | Skeleton for the whole hedge-fund org topology (escalation lanes, delegation, propagation). |
| .claude/docs/director-gates.md | Per-gate T1/T2 table exists (mapping.txt:123-151); no single T2 verdict for the mechanism... | TAKE-MODIFY |  | Standardize on one verdict vocabulary (the 9 found in the 28 files must not be copied as-is); make CRO/CCO hard-block gates independent of `modes.review_mode` (currently... | .claude/docs/director-gates.md:123-135; .claude/docs/director-gates.md:75 | Overview doc for the 28 gate files (counted separately, §5.11). Skeleton for CIO/CRO/CCO review gates and the phase-gate launch panel. |
| .claude/docs/model-tiers.md | N/A (config/mechanism doc, not itemized in mapping.txt's config table beyond `modes.*`... | TAKE-MODIFY |  | Do not budget compliance guarantees on the model: pin until verified for agents (currently confirmed-unenforced for skills, unverified for agents). | .claude/docs/model-tiers.md:3-10; .claude/docs/model-tiers.md:18-21 | Model-tier assignment framework; usable as-is for cost/capability tiering once its unverified agent-level enforcement is tested. |
| .claude/docs/automation-modes.md + docs/COLLABORATIVE-DESIGN-PRINCIPLE.md + .claude/docs/workflow-modes.md | N/A (general infra doc; mapping.txt's config table marks `modes.automation` and... | TAKE-MODIFY |  | Add hedge-fund-specific always-ask categories (e.g. limit_changes, trade_execution, investor_communication) alongside the existing... | .claude/docs/automation-modes.md:130; docs/COLLABORATIVE-DESIGN-PRINCIPLE.md:455-463 | Q→O→D→Draft→Approval human-sign-off discipline is the closest existing thing to a four-eyes control at the workflow layer; automation_always_ask categories... |
| .claude/docs/context-management.md | Not separately assessed by the workers; carried by the infra MINIMUM TRANSPLANT SET... | TAKE-MODIFY |  | Prune the 2-3 GDD-specific example lines; the CHECKPOINT/STATUS marker contract and the two load-bearing conventions it documents are generic. | .claude/docs/context-management.md:(session-state contract) | Session-state and observation-vs-verdict conventions; part of the MINIMUM TRANSPLANT SET (§4). |
| .claude/docs/effects-map.md | Not separately assessed by the workers; cited throughout the infra CONFIG KEYS finding as... | TAKE-MODIFY |  | Rewrite one section per surviving or new config key (archetype, jurisdiction, risk.*, regulatory_calendar, controls.*) once P2 finalizes the schema; drop sections for... | .claude/docs/effects-map.md:2421 lines total | Per-key effect documentation; mechanism (one section per key, cites its readers) is generic. |
| .claude/docs/code-root-resolution.md | Not separately assessed by the workers. | CONDITIONAL | Q05=B and Q25=C/D | Only relevant if the fund creates a code root or an assets/-equivalent structured-data directory. | .claude/hooks/yaml-helper.sh:1206-1252 | Code-root resolution convention; applies only when a code pipeline exists. |
| .claude/docs/workflow-catalog.yaml | W (phase names + artifact paths renamed; structure kept) | TAKE-MODIFY |  | Reuse the schema as-is (phases: dict, steps with glob/pattern/min_count/any_of, required/repeatable) for the firm-setup track. INFERENCE: for a second,... | .claude/docs/workflow-catalog.yaml:1-19; .claude/skills/help/SKILL.md:70-77 (VERIFIER-CORRECTED from 96-105); .claude/scripts/artifact-check.sh:parser loop | Reuse the schema as-is (phases: dict, steps with glob/pattern/min_count/any_of, required/repeatable) for the firm-setup track. INFERENCE: for a second,... |
| CCGS Skill Testing Framework/catalog.yaml | K (mechanism kept); W (T2, content renamed) | TAKE-MODIFY |  | Confirmed by direct count: 74 skills + 49 agents = 123, matching the review's own figure. | CCGS Skill Testing Framework/catalog.yaml:1-14; CCGS Skill Testing Framework/catalog.yaml:grep -c count | Transplant the mechanism (skill+agent registry with spec path, priority, category, coverage-tracking fields); every name:/spec: path must be rewritten for the new HF... |
| CCGS Skill Testing Framework/quality-rubric.md | K (mechanism); content renamed per-category for T2 | TAKE-MODIFY |  | RD3 and D1/D4 map directly onto compliance-hold verdicts and CCO/CRO-equivalent control-function agents. | CCGS Skill Testing Framework/quality-rubric.md:116-121; CCGS Skill Testing Framework/quality-rubric.md:81-89; CCGS Skill Testing Framework/quality-rubric.md:186-191 | Mechanism transplants directly; category name-lists must be rewritten. AN1-AN4 map unmodified onto compliance/risk-monitoring skills, which must be read-only and... |
| CCGS Skill Testing Framework/ (static/spec/category/audit modes) | static:K/audit:degrades/spec:breaks/category:breaks (same for T2 per README's mode table) | TAKE-MODIFY |  | The README's own degrade/break table directly answers what happens when skill/agent names change, corroborating the review's existing silent-break finding with... | CCGS Skill Testing Framework/README.md:17-21 | Transplant all four modes' mechanism; static needs zero rewrite; spec/category/audit need the full registry rewrite described above. |
| CCGS Skill Testing Framework/templates/skill-test-spec.md | GAP -- never assessed by the original workers (verifier missing_components). | TAKE |  | Verifier correction: add this component. Fully generic behavior-spec template; no rewrite needed to transplant the mechanism. | CCGS Skill Testing Framework/templates/skill-test-spec.md:1- | Behavior-spec template for a new hedge-fund skill’s 5 AAA-03 test cases. |
| CCGS Skill Testing Framework/templates/agent-test-spec.md | GAP -- never assessed by the original workers (verifier missing_components). | TAKE |  | Verifier correction: add this component. Fully generic agent behavior-spec template. | CCGS Skill Testing Framework/templates/agent-test-spec.md:1- | Behavior-spec template for a new hedge-fund agent’s test cases. |

### 5.4 config keys (not counted in the 232)

| Config key | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| schema_version |  | TAKE |  |  | project.yaml:4; effects-map.md:2157-2171 | Generic process-control marker; no game content. |
| framework.version / last_upgraded |  | TAKE |  |  | project.yaml:6-8; effects-map.md:2182-2208 | Generic upstream-version tracking. |
| modes.rigor |  | TAKE |  |  | yaml-helper.sh:999,1014-1017; effects-map.md:457-527 | Single-question complexity dial; usable to calibrate IC/compliance rigor by fund stage. |
| workflow_overrides |  | TAKE |  |  | yaml-helper.sh:1504-1519; effects-map.md:704-772 | Generic per-system doc-requirement override. |
| modes.story_granularity |  | TAKE |  |  | effects-map.md (config-key table) | Generic story-sizing dial. |
| docs.density |  | TAKE |  |  | effects-map.md (config-key table) | Generic doc-verbosity dial. |
| performance.enforce |  | TAKE |  |  | yaml-helper.sh:469,1451-1480 | warn/block/off enforcement-level mechanism; reusable for any numeric-threshold check, including a future risk-limit breach. |
| features.session_state |  | TAKE |  |  | yaml-helper.sh:665-702; effects-map.md:1914-2000 | Generic, default on; directly serves the audit-trail need named in the task. |
| cadence.sprint_length / milestone_length |  | TAKE |  |  | effects-map.md:1496-1530 | RESERVED/unimplemented upstream too; generic recurring-cadence config, useful for board/IC meeting cadence once implemented. |
| modes.review_mode (full/lean/solo) |  | TAKE-MODIFY |  |  | yaml-helper.sh:461,970-976 | Gate-execution-depth dial; rename values, keep the chain; flag “solo” for restriction (SB-19). |
| modes.automation (collaborative/guided/autonomous) |  | TAKE-MODIFY |  |  | yaml-helper.sh:464,998 | Flag “autonomous” for restriction on regulated actions. |
| modes.automation_always_ask |  | TAKE-MODIFY |  |  | yaml-helper.sh:890-892 | Default list is scope_changes/file_deletions/schema_changes; add hedge-fund categories (risk_limit_changes, trade_related_actions, client_data_access). |
| modes.workflow (full/standard/minimal) |  | TAKE-MODIFY |  |  | yaml-helper.sh (doc-section-count dial) | Doc-section-count dial; reusable for IC-memo completeness tiers. |
| qa.level (minimal/standard/full) |  | TAKE-MODIFY |  |  | effects-map.md:1160-1206 | Rename to “review/validation level”; reusable for model-validation rigor tiers. |
| team.size (individual/small/studio) |  | TAKE-MODIFY |  |  | yaml-helper.sh:468,1016-1017 | Cosmetic rename only; SB-20 (control seats must not scale with this key). |
| project.stage |  | TAKE-MODIFY |  |  | yaml-helper.sh:473, 1057-1060, 1149-1177 (VERIFIER-CORRECTED from 1589-1614) | Single authoritative-value + gate-check-only-write + dual legacy-mirror mechanism is reusable; all 7 stage values are game-specific and must be replaced (SB-14, SB-22). |
| testing.strict.{logic,integration,visual,ui,config} |  | TAKE-MODIFY |  |  | effects-map.md:1107-1157 | Per-evidence-type block/advisory mechanism is generic; the 5-value type vocabulary needs redesign into a hedge-fund evidence taxonomy (SB-23, SB-24). |
| strict_gate_checks |  | TAKE-MODIFY |  |  | effects-map.md:1230-1253 (VERIFIER ADDITION) | RESERVED/NOT IMPLEMENTED upstream; no skill or hook reads it (SB-17). Implement it, or replace it with the protected-path hook design (§5 Control model), before relying on it for a compliance block. |
| features.token_budget_warn_at |  | TAKE |  |  | effects-map.md:2123-2139; yaml-helper.sh:528 (VERIFIER ADDITION) | Default 0.7; documented in 3 places in effects-map.md as read by pre-compact.sh/session-start.sh/statusline.sh, but only yaml-helper.sh:528’s local-override allow-list actually names it. Generic; transplant as-is, note... |
| commands.{build,test,run,smoke} |  | CONDITIONAL | Q25=C/D |  | effects-map.md:1732-1845 | OS-aware-map + fallback resolution is generic; content becomes e.g. `pytest tests/`, `python run_backtest.py`. |
| testing.framework |  | CONDITIONAL | Q25=C/D |  | effects-map.md:1070-1105 | Engine-specific table (gdunit4/unity-test-framework/unreal-automation); needs a pytest/coverage.py-equivalent row. |
| qa.coverage_minimum |  | CONDITIONAL | Q25=C/D |  | effects-map.md:1207-1226 | Mechanism generic; engine-specific coverage-report parsing (gdunit4/Unity/gcov) must be swapped. |
| naming.{classes,variables,constants,signals,files} |  | CONDITIONAL | Q25=C/D |  | effects-map.md:1847-1912 | Code-naming-convention block; drop the scenes/prefabs row (engine-only). |
| code-root-resolution.md + resolve_code_root() |  | CONDITIONAL | Q25=C/D |  | yaml-helper.sh:1206-1252 | Without a new case arm, returns empty forever on a non-quant fund; correct per its own “unresolved does not default” design, but only if the fund has no code pipeline at all (SB-06). |
| engine.name + specialists |  | LEAVE |  |  | yaml-helper.sh:472,1235-1248; effects-map.md:1689-1730 | Central game/tool-identity+routing key; its role is exactly the `archetype` gap (see below). Needs a brand-new key, not a port. |
| project.kind |  | LEAVE |  |  | effects-map.md:1646-1687 | Confirmed RESERVED/NOT IMPLEMENTED; “No skill or hook reads this setting” at line 1650. Dead weight even upstream. |
| platform.multiplayer |  | LEAVE |  |  | effects-map.md:1328-1368 | Real-time netcode routing; zero analogue. |
| platform.online |  | LEAVE |  |  | effects-map.md:1371-1406 | Cloud-saves/leaderboards/IAP; a stretch to repurpose as “calls external market-data/broker APIs”, speculative only, not recommended. |
| platform.cert_tier |  | LEAVE |  |  | effects-map.md:1408-1445 | Itch/Steam/console certification; zero analogue. |
| accessibility.target |  | LEAVE |  |  | effects-map.md:1447-1458 | Confirmed RESERVED/NOT IMPLEMENTED even upstream; Game Accessibility Guidelines content has zero analogue. |
| performance.target_framerate/frame_budget_ms/draw_call_limit/memory_ceiling_mb |  | LEAVE |  |  | effects-map.md:1532-1560 | Pure rendering-performance concept. If execution-latency SLAs matter for an HFT-adjacent strategy, a new `latency.*` key must be designed fresh; this is INFERENCE, not a rename target. |
| archetype (quant\|discretionary\|macro\|multi-strategy) |  | INFERENCE (new key) |  | Replaces engine.name’s routing role; drives which specialist agents spawn. | effects-map.md:1709-1716 (structural donor: engine.name routing) | Q05 answer sets this key. |
| jurisdiction (KR-FSC\|KY-CIMA\|US-SEC) |  | INFERENCE (new key) |  | Drives which regulatory checklist/calendar applies. | effects-map.md:1408-1445 (structural donor: platform.cert_tier) | Content must be authored fresh. |
| risk.leverage_cap_pct_nav / risk.var_limit / risk.concentration_limit / risk.loss_limit_daily |  | INFERENCE (new key) |  | No structural donor exists; highest-priority net-new key set given the legal 400%-of-NAV leverage cap. | HF-REF-06 §4.3 표4-3 | New risk-limit config block. |
| regulatory_calendar |  | INFERENCE (new key) |  | Filing deadlines, IC/board meeting cadence, audit windows. | effects-map.md:1496-1530 (structural donor: cadence.*) | cadence.sprint_length is a structural donor for the shape only. |
| code_pipeline.model_change_approval / code_pipeline.version_control_required |  | INFERENCE (new key) | Q25=C/D | Model-governance keys per HF-REF-12 §7.8, HF-REF-14 §8.5 (SRC-50) (2025 SEC Two Sigma case). | commands.* and testing.strict.* are the closest structural donors | New model-governance config. |
| controls.four_eyes_required_for: [trade_execution, valuation, nav_calculation] |  | INFERENCE (new key) |  | modes.automation_always_ask’s category-list shape is the closest donor, but four-eyes means a second human, not “ask a human”; the enforcement mechanism itself is new. | yaml-helper.sh:890-892 (structural donor: automation_always_ask) | New segregation-of-duties config. |
| controls.protected_paths |  | INFERENCE (new key) |  | Paths a PreToolUse hook refuses to write without a review-receipt (design-spec §5 Control model). | validate-commit.sh (structural donor: PreToolUse exit-2 pattern) | New hook-enforcement config. |

### 5.5 rules (13)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/rules/agent-memory.md | K | TAKE-MODIFY |  | Mechanism is fully domain-neutral; only the day-one example needs an HF equivalent. | .claude/rules/agent-memory.md:23-29 | Direct transplant of the mechanism; only the worked example needs swapping. |
| .claude/rules/ai-code.md | D (both T1 and T2) | LEAVE |  | Agrees with mapping.txt's D/D verdict for both T1 and T2. | .claude/rules/ai-code.md:9-13 | None -- vocabulary too game-specific to salvage. Write a fresh rule if a signal-generation component exists. |
| .claude/rules/data-files.md | W (T1); D (T2, per mapping infra row) | TAKE-MODIFY |  | Path needs to change from assets/data/** to config/data/**; worked example needs an HF replacement (e.g. | .claude/rules/data-files.md:8-12; .claude/rules/data-files.md:29-48 | Direct transplant for the fund's own parameter/config files (risk limits, fee schedules) -- serves context point 2 directly. |
| .claude/rules/design-docs.md | R (T2); W (T1) | TAKE-MODIFY |  | Strongest single-line evidence in rules/ that this rule transplants almost unmodified. | .claude/rules/design-docs.md:9-10; .claude/rules/design-docs.md:19-21 | Rule counterpart to game-design-document.md -> Strategy Design Doc; Formulas-required-when-numeric-rules test reads almost verbatim as an HF requirement. |
| .claude/rules/engine-code.md | D (both) | LEAVE |  | Agrees with D/D mapping. | .claude/rules/engine-code.md:8,11 | None -- too specific to real-time rendering/physics to salvage. |
| .claude/rules/gameplay-code.md | D (per mapping infra row; T1 was W) | CONDITIONAL | Q05=B | GENUINE DIVERGENCE FROM T2: T2 has no code pipeline so this is D there, but HF's quant archetype is much closer to T1 -- 'never hardcoded' and 'unit tests for all logic'... | .claude/rules/gameplay-code.md:8; .claude/rules/gameplay-code.md:12-15 | Becomes effectively 'quant-code.md' with light rewording -- highest-value rule transplant for the quant archetype. |
| .claude/rules/narrative.md | W (T2: 브랜드 보이스 규칙으로 전환) | LEAVE |  | Diverges from T2's W -- HF's need is compliance-gated disclosure, not brand voice. | .claude/rules/narrative.md:8-12 | None at core org-setup level; investor comms style is narrower and better served by a fresh investor-comms.md rule. |
| .claude/rules/network-code.md | D (per mapping infra row; T1 was W) | LEAVE |  | Multiplayer-netcode specific; HF's networking need is external API integration, a different shape. | .claude/rules/network-code.md:8,10 | None directly; write a fresh API-integration rule if needed (rate limits, failover, message versioning). |
| .claude/rules/prototype-code.md | K (both T1 and T2) | TAKE |  | This 'research must not be deployed without rewrite' rule is exactly the model-governance transition point the SEC Two Sigma case is about. | .claude/rules/prototype-code.md:32-36 | Direct transplant for the quant desk's research/backtesting scratch code. |
| .claude/rules/shader-code.md | D (both) | LEAVE |  | 100% graphics-shader specific; agrees with D/D. | .claude/rules/shader-code.md:1-9 | None whatsoever. |
| .claude/rules/skill-authoring.md | K (both T1 and T2) | TAKE |  | The five obligations are the single most valuable transplant in the rules/ directory for the quality-framework deliverable specifically. | .claude/rules/skill-authoring.md:9; .claude/rules/skill-authoring.md:21-36; .claude/rules/skill-authoring.md:70-79 | PRIORITY -- the meta-rule governing how ALL new hedge-fund skills/agents/gates must be written. Directly answers Strategy C's mandate. |
| .claude/rules/test-standards.md | K (both) | TAKE |  | Fully domain-neutral; only the GDScript code examples need language replacement. | .claude/rules/test-standards.md:15-18 | Direct transplant for any quant/trading code -- serves context point 3's model-governance test-discipline requirement. |
| .claude/rules/ui-code.md | W (T2, per mapping infra row) | CONDITIONAL | Q24=B | Gamepad/HUD content not relevant; only localization/accessibility principles survive, only if a portal is built. | .claude/rules/ui-code.md:9,14 | Trimmed subset (no hardcoded strings, mandatory accessibility) if a proprietary investor portal is built. |

### 5.6 templates (46)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/docs/templates/SKILL-CONTRACT-TEMPLATE.md | K | TAKE |  | The Identity&Scope / Input Contract / Output Contract / Hard-Soft Constraints / Handoff Configuration sections are live and generic; the file's own header flags the... | .claude/docs/templates/SKILL-CONTRACT-TEMPLATE.md:3-21 | Handoff-contract template for new HF skills (e.g. /investment-decision -> /trade-execution). Domain-neutral structure. |
| .claude/docs/templates/accessibility-requirements.md | W (디지털 접근성 점검표) | CONDITIONAL | Q24=B | Every feature row is game/console/mobile specific. | .claude/docs/templates/accessibility-requirements.md:57-156 | If built: trims to a generic web-accessibility checklist for the portal UI. Not a core org-setup document otherwise. |
| .claude/docs/templates/architecture-decision-record.md | D (none -- T2 does not write ADRs) | TAKE-MODIFY |  | Largest divergence from T2: T2 writes no ADRs, but HF's code/model pipeline needs ADRs MORE than T1 does -- change approval + version history is a named regulatory... | .claude/docs/templates/architecture-decision-record.md:41,71; scratchpad/mapping.txt (T2 infra row):adr-dep-graph.sh | Model-governance ADR: swap 'Engine Compatibility' section for 'Regulatory / Model-Risk Impact'. Records change approval + version history for trading/model code. |
| .claude/docs/templates/architecture-doc-from-code.md | D | CONDITIONAL | Q25=C/D | Headers are fully generic; only useful once a code pipeline exists. | .claude/docs/templates/architecture-doc-from-code.md:1-250 headers | Reverse-engineer an ADR from an already-built trading system component when no ADR was written at the time. |
| .claude/docs/templates/architecture-traceability.md | D | CONDITIONAL | Q25=C/D | Swap 'GDD' for 'Regulatory Requirement' or 'IC Policy'; otherwise generic matrix shape. | .claude/docs/templates/architecture-traceability.md:1-88 headers | Trace regulatory/IC-policy requirements to system controls/ADRs -- ODD evidence (context point 4). |
| .claude/docs/templates/art-bible.md | R (브랜드 가이드라인) | LEAVE |  | Visual-production specific with no reusable structure beyond what T2 already extracted as a generic brand-guide concept. | .claude/docs/templates/art-bible.md:48-73 | Not a standard org-setup artifact; at most a cosmetic pitch-deck style guide donor. |
| .claude/docs/templates/changelog-template.md | W (고객 업데이트 기록) | TAKE-MODIFY |  | Balance Changes table is a near-literal fit for logging risk/strategy-parameter changes with before/after values and rationale -- narrower, more compliance-critical than... | .claude/docs/templates/changelog-template.md:23-28 | Strategy/Model Change Log -- model-governance version history (context point 3), not customer messaging. |
| .claude/docs/templates/concept-doc-from-prototype.md | W (파일럿 캠페인 회고) | TAKE-MODIFY |  | 'Production Readiness Assessment' maps to 'Live Capital Readiness'. | .claude/docs/templates/concept-doc-from-prototype.md:146-168 | Strategy pilot / paper-trading-to-live-capital readiness assessment. |
| .claude/docs/templates/design-doc-from-implementation.md | D | CONDITIONAL | Q25=C/D | Structurally close to a strategy design doc reconstructed after the fact. | .claude/docs/templates/design-doc-from-implementation.md:53-147 | Reverse-document a trading system implementation; '5. Balance and Tuning' maps to parameter documentation. |
| .claude/docs/templates/difficulty-curve.md | D | LEAVE |  | Player-experience pacing document; no hedge-fund analog. | .claude/docs/templates/difficulty-curve.md:11-305 headers | None. |
| .claude/docs/templates/economy-model.md | D | CONDITIONAL | GAP (no Q-ID assigned) | Low priority; PPM/LPA legal docs normally cover this. | .claude/docs/templates/economy-model.md:31-53 | Structural donor only -- Currencies/Sources(Faucets)/Sinks(Drains)/Balance Targets mirror fee flows, hurdle rates, high-water marks. |
| .claude/docs/templates/faction-design.md | R (타깃/경쟁사 페르소나) | LEAVE |  | Narrative/worldbuilding specific; diverges from T2's R since T2's marketing-persona use case doesn't apply to HF org setup. | .claude/docs/templates/faction-design.md:1-98 headers | None for org setup. |
| .claude/docs/templates/game-brief.md | W (한 장짜리 캠페인 브리프) | TAKE-MODIFY |  | Core loop -> core investment process loop; MVP -> minimum viable fund launch scope. | .claude/docs/templates/game-brief.md:17-35 | Fund/Strategy one-pager for the minimal workflow tier. |
| .claude/docs/templates/game-concept.md | W (프로젝트 콘셉트 브리프) | TAKE-MODIFY |  | Larger rewrite than T2's W suggests -- MDA/Bartle sections must be deleted, not reworded, pushing real effort toward REDESIGN even though the surrounding skeleton... | .claude/docs/templates/game-concept.md:68-102,119-126; .claude/docs/templates/game-concept.md:219-231,279-304 | Fund/Strategy Concept Document -- keep Core Identity/Core Loop/Target LP Profile/Technical Considerations/Risks/MVP Definition; REMOVE MDA Aesthetics + Bartle Taxonomy... |
| .claude/docs/templates/game-design-document.md | R (크리에이티브/산출물 브리프) | TAKE-MODIFY |  | Formulas/Edge Cases/Dependencies/Tuning Knobs map almost verbatim onto position-sizing formulas, market-condition edge cases, data-feed dependencies, risk-parameter... | .claude/docs/templates/game-design-document.md:50-69; .claude/docs/templates/game-design-document.md:69-96; .claude/docs/templates/game-design-document.md:96-156 | PRIORITY -- becomes the Strategy Design Document: gives HF a formal, numeric-rules-bearing record for exposure limits/loss rules/leverage caps (context point 2) and the... |
| .claude/docs/templates/game-pillars.md | W (브랜드/크리에이티브 원칙) | TAKE-MODIFY |  | Pillar Conflict Resolution's priority-order mechanism maps to IC conflict resolution; escalation path swaps to CIO/IC chair. | .claude/docs/templates/game-pillars.md:207-227 | Firm Investment Philosophy / Pillars, referenced by IC decisions. |
| .claude/docs/templates/hud-design.md | D | CONDITIONAL | Q24=B | Low priority; most funds use vendor terminals. | .claude/docs/templates/hud-design.md:1-251 headers | Trading dashboard/terminal UI spec, only if not using a vendor OMS/EMS. |
| .claude/docs/templates/incident-response.md | W (위기 커뮤니케이션 대응) | TAKE-MODIFY |  | Strongest 1:1 structural match found: Timeline->Root Cause->Mitigation->Communication->Prevention->Sign-off is exactly the shape a trading-limit breach or NAV error... | .claude/docs/templates/incident-response.md:67-86; .claude/docs/templates/incident-response.md:125-130 | PRIORITY -- Operational Incident and Breach Log, named in the task's deliverable list. Answers context point 1 (CCO/CRO independent reporting lines). |
| .claude/docs/templates/interaction-pattern-library.md | R (웹 소재 패턴 라이브러리) | CONDITIONAL | Q24=B | Bundled with accessibility-requirements.md and ux-spec.md under the same conditional. | .claude/docs/templates/interaction-pattern-library.md:109-413 headers | UI component library for a proprietary portal only. |
| .claude/docs/templates/level-design-document.md | D | LEAVE |  | No analog. | .claude/docs/templates/level-design-document.md:1-106 headers | None. |
| .claude/docs/templates/milestone-definition.md | K | TAKE |  | Zero domain terms in structure; only the Type enum needs value swaps. | .claude/docs/templates/milestone-definition.md:1-79; .claude/docs/templates/milestone-definition.md:6 | Firm-setup milestones (FSC registration filed, compliance framework live, systems go-live, first close). |
| .claude/docs/templates/narrative-character-sheet.md | R (오디언스 페르소나) | LEAVE |  | Character/dialogue specific; diverges from T2's R since T2's marketing use case doesn't apply. | .claude/docs/templates/narrative-character-sheet.md:26-93 | None at org-setup level; LP persona work is a marketing/IR nicety. |
| .claude/docs/templates/pitch-document.md | W (고객 제안서) | TAKE-MODIFY |  | Business Model table maps onto fee structure/share classes/conflicts-of-interest policy; Comparable Titles -> comparable funds. | .claude/docs/templates/pitch-document.md:99-109; .claude/docs/templates/pitch-document.md:40-46 | Investor Pitch / Fund Deck, named in the task's deliverable list. |
| .claude/docs/templates/player-journey.md | R (고객 여정 지도) | CONDITIONAL | GAP (no Q-ID assigned) | Session-based engagement map; only loosely portable to investor lifecycle. | .claude/docs/templates/player-journey.md:58-198 | Low priority; not a standard org-setup document. |
| .claude/docs/templates/post-mortem.md | K | TAKE |  | Zero domain-specific terms. | .claude/docs/templates/post-mortem.md:1-70 | Investment Post-Trade Review, named in the task's deliverable list. |
| .claude/docs/templates/project-stage-report.md | W (프로젝트 단계 보고서) | TAKE-MODIFY |  | Category subsections need renaming to firm-setup categories (Regulatory Filings/Compliance Policies/Risk Framework/Trading Systems/Governance). | .claude/docs/templates/project-stage-report.md:21-78 | Firm-setup track's own 'where are we' audit. |
| .claude/docs/templates/prototype-report.md | R (파일럿/테스트 캠페인 보고서) | CONDITIONAL | Q05=B | PROCEED/PIVOT/KILL pattern is exactly the shape of a quant research go/no-go decision. | .claude/docs/templates/prototype-report.md:1-100 | Strategy Backtest/Paper-Trade go/no-go memo before committing capital. |
| .claude/docs/templates/release-checklist-template.md | D | LEAVE |  | Software-shipping specific; agrees with T2's D. | .claude/docs/templates/release-checklist-template.md:58-95 | None -- milestone-definition.md already covers go-live checklists. |
| .claude/docs/templates/release-notes.md | W (고객 산출물 노트) | TAKE-MODIFY |  | Balance Adjustments table maps to a Strategy Parameter Changes disclosure table for investors. | .claude/docs/templates/release-notes.md:27-32 | Investor Update / Monthly Letter cadence-report skeleton. |
| .claude/docs/templates/risk-register-entry.md | K | TAKE |  | Zero domain terms; directly serves context point 2. | .claude/docs/templates/risk-register-entry.md:10-14; .claude/docs/templates/risk-register-entry.md:41-51 | PRIORITY -- firm-setup and investment risk registers, named in the task's deliverable list. |
| .claude/docs/templates/session-state.md | K | TAKE |  | Pure engineering session-checkpoint mechanism, zero domain terms. | .claude/docs/templates/session-state.md:6-29 | Unmodified transplant, part of Strategy C's operating-foundation list. |
| .claude/docs/templates/sound-bible.md | D | LEAVE |  | Pure audio design; agrees with T2. | .claude/docs/templates/sound-bible.md:1-100 headers | None. |
| .claude/docs/templates/sprint-plan.md | K | TAKE |  | Generic structure; only DoD checklist items need swapping for compliance-sign-off items. | .claude/docs/templates/sprint-plan.md:55-65 | Firm-setup track's own sprint cadence. |
| .claude/docs/templates/systems-index.md | R (워크스트림/산출물 목록) | TAKE-MODIFY |  | Strong structural fit but content needs full rewrite -- the Categories enum is entirely game-specific. | .claude/docs/templates/systems-index.md:31,66-82 | Master 'Firm Systems Index' driving the firm-setup track (Foundation=legal entity+FSC+custody; Core=compliance+risk+trading infra; Feature=strategies;... |
| .claude/docs/templates/technical-design-document.md | D | CONDITIONAL | Q25=C/D | Lower priority than game-design-document.md; useful only if proprietary infra is built. | .claude/docs/templates/technical-design-document.md:11-25 | Technical/systems counterpart to the Strategy Design Doc -- OMS/EMS/market-data architecture. |
| .claude/docs/templates/test-evidence.md | W (산출물 검수/승인 기록) | TAKE-MODIFY |  | Sign-Off table's role list maps to (Portfolio Manager/Risk Officer/Independent Valuator). | .claude/docs/templates/test-evidence.md:80-88 | Trade/Model Validation Evidence or Independent Valuation Sign-off Record -- serves context point 5 (segregation of duties, 4-eyes). |
| .claude/docs/templates/test-plan.md | D | CONDITIONAL | Q25=C/D | Only needed once a code/model pipeline requires formal test planning. | .claude/docs/templates/test-plan.md:25-56 | Model/System Test Plan for the quant pipeline. |
| .claude/docs/templates/ux-spec.md | R (디지털 소재 크리에이티브 브리프) | CONDITIONAL | Q24=B | Bundled with the other investor-portal-conditional templates. | .claude/docs/templates/ux-spec.md:245-285 | Screen/flow spec for the portal only. |
| .claude/docs/templates/vertical-slice-report.md | D | LEAVE |  | Duplicate of prototype-report.md's shape at a much higher fidelity bar; agrees with T2's D. | .claude/docs/templates/vertical-slice-report.md:10-19,93 | None -- prototype-report.md covers the same PROCEED/PIVOT/KILL pattern better for the quant use case. |
| .claude/docs/templates/guidance/accessibility-requirements-guide.md | W | LEAVE |  | Bundled with its parent template's conditional. | .claude/docs/templates/guidance/accessibility-requirements-guide.md:1-9 | Same investor-portal=build conditional as its parent template. |
| .claude/docs/templates/guidance/hud-design-guide.md | D | LEAVE |  | Guidance file for a LEAVE-verdict template. | .claude/docs/templates/guidance/hud-design-guide.md:10-371 headers | None. |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-game-specific.md | D | LEAVE |  | Pure game UI patterns; agrees with T2's D. | .claude/docs/templates/guidance/interaction-pattern-library-guide-game-specific.md:9-148 headers | None. |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md | R | CONDITIONAL | Q24=B | Bundled under the investor-portal conditional. | .claude/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md:9-121 headers | Generic navigation/loading/error-state patterns. |
| .claude/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md | R | CONDITIONAL | Q24=B | Bundled under the investor-portal conditional. | .claude/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md:9-554 headers | Generic button/modal/toast/tooltip specs. |
| .claude/docs/templates/guidance/interaction-pattern-library-guide.md | R | CONDITIONAL | Q24=B | Bundled under the investor-portal conditional. | .claude/docs/templates/guidance/interaction-pattern-library-guide.md:3 | Index file for the pattern-library guidance set. |
| .claude/docs/templates/guidance/ux-spec-guide.md | R | CONDITIONAL | Q24=B | Bundled under the investor-portal conditional. | .claude/docs/templates/guidance/ux-spec-guide.md:3-434 headers | Authoring guidance for ux-spec.md, same conditional. |

### 5.7 director gates (28)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/docs/director-gates/cd-phase-gate.md | CD-PHASE-GATE K/K; TD-PHASE-GATE K/W; PR-PHASE-GATE K/K; AD-PHASE-GATE W/K (mapping.txt... | TAKE-MODIFY |  | Replace creative/visual readiness content with fund-launch readiness (regulatory filing status, custody/admin setup, risk-limit configuration, compliance manual... | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 | Launch-readiness / quarterly control-review panel (CIO+CRO+CCO+COO spawned in parallel). |
| .claude/docs/director-gates/td-phase-gate.md | CD-PHASE-GATE K/K; TD-PHASE-GATE K/W; PR-PHASE-GATE K/K; AD-PHASE-GATE W/K (mapping.txt... | TAKE-MODIFY |  | Replace creative/visual readiness content with fund-launch readiness (regulatory filing status, custody/admin setup, risk-limit configuration, compliance manual... | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 | Launch-readiness / quarterly control-review panel (CIO+CRO+CCO+COO spawned in parallel). |
| .claude/docs/director-gates/pr-phase-gate.md | CD-PHASE-GATE K/K; TD-PHASE-GATE K/W; PR-PHASE-GATE K/K; AD-PHASE-GATE W/K (mapping.txt... | TAKE-MODIFY |  | Replace creative/visual readiness content with fund-launch readiness (regulatory filing status, custody/admin setup, risk-limit configuration, compliance manual... | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 | Launch-readiness / quarterly control-review panel (CIO+CRO+CCO+COO spawned in parallel). |
| .claude/docs/director-gates/ad-phase-gate.md | CD-PHASE-GATE K/K; TD-PHASE-GATE K/W; PR-PHASE-GATE K/K; AD-PHASE-GATE W/K (mapping.txt... | TAKE-MODIFY |  | Replace creative/visual readiness content with fund-launch readiness (regulatory filing status, custody/admin setup, risk-limit configuration, compliance manual... | .claude/docs/director-gates/cd-phase-gate.md:21; .claude/docs/director-gates.md:156-164 | Launch-readiness / quarterly control-review panel (CIO+CRO+CCO+COO spawned in parallel). |
| .claude/docs/director-gates/td-system-boundary.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/td-architecture.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/td-adr.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/td-manifest.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/lp-feasibility.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/lp-code-review.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/ql-test-coverage.md | TD-SYSTEM-BOUNDARY K/D; TD-ARCHITECTURE K/D; TD-ADR K/D; TD-MANIFEST K/D; LP-FEASIBILITY... | CONDITIONAL | Q05=B and Q25=C/D | Rename ADR->model change record, GDD requirement->strategy spec requirement; TD-ADR's 'engine version stamped, post-cutoff API risks flagged' becomes 'data/library... | .claude/docs/director-gates/td-adr.md:16-21; .claude/docs/director-gates/lp-code-review.md:17-21 | Model-governance review chain: model/strategy architecture sign-off, per-change code review, test/backtest coverage review — directly addresses the SEC Two Sigma factual... |
| .claude/docs/director-gates/cd-pillars.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/cd-gdd-align.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/cd-systems.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/cd-narrative.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/cd-playtest.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/ad-concept-visual.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/ad-art-bible.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/ad-visual.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/nd-consistency.md | Mixed but mostly K/R/W for T2 (e.g. CD-PILLARS K/K, AD-ART-BIBLE R/W, AD-CONCEPT-VISUAL... | LEAVE |  | T2 (marketing/content agency) kept most of these because brand/creative identity is its core deliverable; a regulated asset manager's core control framework has no... | .claude/docs/director-gates/cd-pillars.md:17-22; .claude/docs/director-gates/ad-concept-visual.md:25 | No hedge-fund control-framework equivalent; at most a very thin IR/marketing-collateral consistency check, not part of the core control loop. |
| .claude/docs/director-gates/pr-scope.md | PR-SCOPE K/K; PR-SPRINT K/K; PR-MILESTONE K/K; PR-EPIC K/K (mapping.txt lines 138-142). | TAKE-MODIFY |  | Terminology only (sprint->cycle, milestone->regulatory/launch milestone); note the 3 distinct verdict vocabularies here (REALISTIC/OPTIMISTIC/UNREALISTIC;... | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 | Generic operations/PMO planning-feasibility panel (COO/PMO domain) — sprint/milestone/scope language translates directly to fund-ops planning cycles. |
| .claude/docs/director-gates/pr-sprint.md | PR-SCOPE K/K; PR-SPRINT K/K; PR-MILESTONE K/K; PR-EPIC K/K (mapping.txt lines 138-142). | TAKE-MODIFY |  | Terminology only (sprint->cycle, milestone->regulatory/launch milestone); note the 3 distinct verdict vocabularies here (REALISTIC/OPTIMISTIC/UNREALISTIC;... | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 | Generic operations/PMO planning-feasibility panel (COO/PMO domain) — sprint/milestone/scope language translates directly to fund-ops planning cycles. |
| .claude/docs/director-gates/pr-milestone.md | PR-SCOPE K/K; PR-SPRINT K/K; PR-MILESTONE K/K; PR-EPIC K/K (mapping.txt lines 138-142). | TAKE-MODIFY |  | Terminology only (sprint->cycle, milestone->regulatory/launch milestone); note the 3 distinct verdict vocabularies here (REALISTIC/OPTIMISTIC/UNREALISTIC;... | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 | Generic operations/PMO planning-feasibility panel (COO/PMO domain) — sprint/milestone/scope language translates directly to fund-ops planning cycles. |
| .claude/docs/director-gates/pr-epic.md | PR-SCOPE K/K; PR-SPRINT K/K; PR-MILESTONE K/K; PR-EPIC K/K (mapping.txt lines 138-142). | TAKE-MODIFY |  | Terminology only (sprint->cycle, milestone->regulatory/launch milestone); note the 3 distinct verdict vocabularies here (REALISTIC/OPTIMISTIC/UNREALISTIC;... | .claude/docs/director-gates/pr-scope.md:25; .claude/docs/director-gates/pr-milestone.md:24 | Generic operations/PMO planning-feasibility panel (COO/PMO domain) — sprint/milestone/scope language translates directly to fund-ops planning cycles. |
| .claude/docs/director-gates/td-change-impact.md | T1=K, T2=W ("범위 변경 영향") -- mapping.txt row 131. Missing from the original assessment;... | TAKE-MODIFY |  | Advisor override: scope-change impact review. Keep APPROVE/CONCERNS/REJECT verdicts. Retarget from design-scope change to strategy/limit-scope change. Owner: coo. | .claude/docs/director-gates/td-change-impact.md:25 | Scope-change impact review for a strategy, limit, or policy change touching more than one department; owner coo. |
| .claude/docs/director-gates/td-feasibility.md | T1=K, T2=R ("납품 실현 가능성") -- mapping.txt row 137. Missing from the original assessment;... | TAKE-MODIFY |  | Advisor override: strategy infrastructure feasibility review (data, borrow, execution). Keep VIABLE/CONCERNS/HIGH RISK verdicts. Owner: technology-lead/coo. | .claude/docs/director-gates/td-feasibility.md:24 | Feasibility check for a proposed strategy’s data, borrow, and execution infrastructure before build-out starts; owner technology-lead/coo. |
| .claude/docs/director-gates/td-engine-risk.md | T1=W, T2=D ("no counterpart") -- mapping.txt row 134. Missing from the original... | CONDITIONAL | Q05=B and Q25=C/D | Advisor override: library and vendor API version risk review. Retarget from post-cutoff engine-API risk to data-library and vendor-API version risk. | .claude/docs/director-gates/td-engine-risk.md:22 | Reviews library and vendor market-data/broker API version risk before a quant strategy build starts. |
| .claude/docs/director-gates/ql-story-ready.md | T1=K, T2=R ("산출물 준비도") -- mapping.txt row 148. Missing from the original assessment;... | CONDITIONAL | Q05=B and Q25=C/D | Advisor override: applies only where a code/model pipeline exists (Q25=C/D). Keep ADEQUATE/GAPS/INADEQUATE verdicts. | .claude/docs/director-gates/ql-story-ready.md:27 | Pre-sprint testability check for a story’s acceptance criteria, applied to a model-change story. |

### 5.8 agents (49)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/agents/creative-director.md | Aggregate only (K2/W19/R0/D28 for T2 agents); likely one of the 28 D or 19 W given zero... | LEAVE |  | All domain content (pillar methodology, MDA aesthetics, player psychology) has no hedge-fund analog; only the generic decision-workflow shell survives. | .claude/agents/creative-director.md:18-20; .claude/agents/creative-director.md:199-247 | No direct role; the 'Strategic Decision Workflow' protocol (highest-level consultant, present/recommend/defer to user) is reusable as a generic pattern for CIO's... |
| .claude/agents/technical-director.md | Aggregate only; T2 deleted essentially all code-governance gates this agent owns... | CONDITIONAL | Q05=B and Q25=C/D | Replace 'engine architecture' with 'trading/model platform architecture'; ADR format stays (Status/Context/Decision/Consequences/Alternatives). | .claude/agents/technical-director.md:80-94; .claude/agents/technical-director.md:138 | Skeleton for a Head of Quant Technology / model-architecture owner — ADR ownership, technology evaluation, performance budgets, technical-debt management all translate... |
| .claude/agents/producer.md | Aggregate only; production-management skills in mapping.txt's skills table (sprint-plan,... | TAKE-MODIFY |  | Rename sprint->ops cycle; the risk register (probability/impact/owner/mitigation) is directly reusable for an operational-risk (not market-risk) register. | .claude/agents/producer.md:89-90; .claude/agents/producer.md:107-113 | COO / Head of Operations / PMO — sprint planning, milestone tracking, risk register, cross-department coordination, retrospectives are all domain-neutral PM functions. |
| .claude/agents/qa-lead.md | Aggregate only; QL-TEST-COVERAGE gate this agent owns is K/R for T2 (still kept, just... | CONDITIONAL | Q05=B and Q25=C/D | Replace story-type table rows (Logic/Integration/Visual/UI/Config) with model-validation categories (backtest, live-shadow, data-quality, reporting). | .claude/agents/qa-lead.md:69-79; .claude/agents/qa-lead.md:13-16 | Model Validation / Independent Testing function — the Logic/Integration/Visual/UI/Config evidence-type table and 'shift-left' discipline map directly onto... |
| .claude/agents/lead-programmer.md | Aggregate only; both gates it owns are D for T2. | CONDITIONAL | Q05=B and Q25=C/D | Coding Standards Enforcement list (lead-programmer.md:84-91) reusable almost verbatim, substituting 'gameplay values' with 'strategy parameters'. | .claude/agents/lead-programmer.md:84-91; .claude/agents/lead-programmer.md:72-75 | Head of Quant Development / Model Governance Lead — code review, API design, coding-standards enforcement, 'no static singletons for game state' -> 'no hardcoded limits'... |
| .claude/agents/security-engineer.md | Aggregate only; no game-domain coupling at all in this agent's content (its game-specific... | TAKE-MODIFY |  | Rename 'anti-cheat'->fraud/market-abuse detection, 'save data'->investor/position data; the checklist (security-engineer.md:111-119) needs almost no structural change. | .claude/agents/security-engineer.md:82-87; .claude/agents/security-engineer.md:111-119 | CISO / Information Security — one of the strongest direct-content donors in the whole set: network security, data-at-rest encryption, privacy compliance... |
| .claude/agents/analytics-engineer.md | Aggregate only. | CONDITIONAL | Q09 (INFERENCE, no direct Q-ID) | Replace event naming convention (game.level.started) with a risk-metric taxonomy (risk.exposure.updated, risk.limit.breached). | .claude/agents/analytics-engineer.md:82-91; .claude/agents/analytics-engineer.md:74-76 | Risk/Performance Analytics or Investor Reporting analytics function — event taxonomy, funnel analysis, dashboard specification pattern transfers to a... |
| .claude/agents/release-manager.md | Aggregate only. | TAKE-MODIFY |  | Replace platform certification requirements with regulatory filing requirements (FSC registration, offering documents); semantic versioning reused for fund document... | .claude/agents/release-manager.md:66-78; .claude/agents/release-manager.md:93-105 | Fund Launch Manager — the staged, no-skip release pipeline (Build->Test->Cert->Submit->Verify->Launch) and version-numbering discipline map directly onto fund launch... |
| .claude/agents/community-manager.md | Aggregate only; devops-engineer and community-manager are the only two agents genuinely... | TAKE-MODIFY |  | Rename 'players'->investors, 'patch notes'->investor update; retarget model tier per founder decision (currently haiku, cheapest — flagged as a founder question given... | .claude/agents/community-manager.md:128-134; .claude/agents/community-manager.md:5 | Investor Relations — patch-notes structure becomes investor-update structure, crisis-communication protocol becomes incident/breach investor communication, and the... |
| .claude/agents/writer.md | Aggregate only. | TAKE-MODIFY |  | Replace dialogue/lore/item-description responsibilities with investor-letter/fact-sheet/pitch-deck copy responsibilities. | .claude/agents/writer.md:34-42; .claude/agents/writer.md:104-105 | Investor Letters / marketing collateral copywriter — the incremental section-by-section drafting workflow (skeleton file -> per-section approval -> session-state update)... |
| .claude/agents/systems-designer.md | Aggregate only. | TAKE-MODIFY |  | Retarget from combat/progression formulas to risk/exposure formulas; keep the mandatory-format enforcement verbatim. | .claude/agents/systems-designer.md:97-115; .claude/agents/systems-designer.md:141-158 | Quant model / risk-formula documentation owner — the 'Formula Output Format (Mandatory)' (named expression + variable table + output range + worked example) is a... |
| .claude/agents/economy-designer.md | Aggregate only. | CONDITIONAL | Q05=B/D (INFERENCE) | Replace item/loot registry with instrument/position registry. | .claude/agents/economy-designer.md:79-93 | Instrument/Position master-data steward — the entity-registry-awareness pattern (check canonical registry before defining a value, flag conflicting proposed values) maps... |
| .claude/agents/devops-engineer.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D | Rename build/CI targets to model-deployment targets; keep branching strategy verbatim. | .claude/agents/devops-engineer.md:79-85 | Infra/model-deployment engineer with code access control — branching strategy (main/develop/feature/release/hotfix) directly supports the SEC Two Sigma-relevant 'code... |
| .claude/agents/godot-specialist.md | T2 aggregate: 15 of the 19 T1-'redesign' agents in review.txt:208 are engine specialists,... | LEAVE |  | 100% Godot-specific technical content (GDScript typing, scene trees, shaders) with zero hedge-fund relevance; only the delegation shape is worth keeping. | .claude/agents/godot-specialist.md:4 | No domain content reuse; the lead+4-subspecialist Agent(...) delegation SHAPE (not content) is the reuse pattern (see reuse_patterns) — usable as a template for a future... |
| .claude/agents/godot-gdscript-specialist.md | T2 aggregate: 15 of the 19 T1-'redesign' agents in review.txt:208 are engine specialists,... | LEAVE |  | 100% Godot-specific technical content (GDScript typing, scene trees, shaders) with zero hedge-fund relevance; only the delegation shape is worth keeping. | .claude/agents/godot-specialist.md:4 | No domain content reuse; the lead+4-subspecialist Agent(...) delegation SHAPE (not content) is the reuse pattern (see reuse_patterns) — usable as a template for a future... |
| .claude/agents/godot-csharp-specialist.md | T2 aggregate: 15 of the 19 T1-'redesign' agents in review.txt:208 are engine specialists,... | LEAVE |  | 100% Godot-specific technical content (GDScript typing, scene trees, shaders) with zero hedge-fund relevance; only the delegation shape is worth keeping. | .claude/agents/godot-specialist.md:4 | No domain content reuse; the lead+4-subspecialist Agent(...) delegation SHAPE (not content) is the reuse pattern (see reuse_patterns) — usable as a template for a future... |
| .claude/agents/godot-shader-specialist.md | T2 aggregate: 15 of the 19 T1-'redesign' agents in review.txt:208 are engine specialists,... | LEAVE |  | 100% Godot-specific technical content (GDScript typing, scene trees, shaders) with zero hedge-fund relevance; only the delegation shape is worth keeping. | .claude/agents/godot-specialist.md:4 | No domain content reuse; the lead+4-subspecialist Agent(...) delegation SHAPE (not content) is the reuse pattern (see reuse_patterns) — usable as a template for a future... |
| .claude/agents/godot-gdextension-specialist.md | T2 aggregate: 15 of the 19 T1-'redesign' agents in review.txt:208 are engine specialists,... | LEAVE |  | 100% Godot-specific technical content (GDScript typing, scene trees, shaders) with zero hedge-fund relevance; only the delegation shape is worth keeping. | .claude/agents/godot-specialist.md:4 | No domain content reuse; the lead+4-subspecialist Agent(...) delegation SHAPE (not content) is the reuse pattern (see reuse_patterns) — usable as a template for a future... |
| .claude/agents/unity-specialist.md | Same as Godot family — D for T2. | LEAVE |  | 100% Unity-specific (ECS, Shader Graph, Addressables); no hedge-fund content. | .claude/agents/unity-specialist.md:4 | Same as Godot family — delegation shape only, via Agent(...) allow-list. |
| .claude/agents/unity-dots-specialist.md | Same as Godot family — D for T2. | LEAVE |  | 100% Unity-specific (ECS, Shader Graph, Addressables); no hedge-fund content. | .claude/agents/unity-specialist.md:4 | Same as Godot family — delegation shape only, via Agent(...) allow-list. |
| .claude/agents/unity-shader-specialist.md | Same as Godot family — D for T2. | LEAVE |  | 100% Unity-specific (ECS, Shader Graph, Addressables); no hedge-fund content. | .claude/agents/unity-specialist.md:4 | Same as Godot family — delegation shape only, via Agent(...) allow-list. |
| .claude/agents/unity-addressables-specialist.md | Same as Godot family — D for T2. | LEAVE |  | 100% Unity-specific (ECS, Shader Graph, Addressables); no hedge-fund content. | .claude/agents/unity-specialist.md:4 | Same as Godot family — delegation shape only, via Agent(...) allow-list. |
| .claude/agents/unity-ui-specialist.md | Same as Godot family — D for T2. | LEAVE |  | 100% Unity-specific (ECS, Shader Graph, Addressables); no hedge-fund content. | .claude/agents/unity-specialist.md:4 | Same as Godot family — delegation shape only, via Agent(...) allow-list. |
| .claude/agents/unreal-specialist.md | Same as Godot/Unity families — D for T2. | LEAVE |  | 100% Unreal-specific (GAS, Blueprint, UMG); no hedge-fund content. | .claude/agents/unreal-specialist.md:4 | Same as Godot/Unity families — delegation shape only. |
| .claude/agents/ue-gas-specialist.md | Same as Godot/Unity families — D for T2. | LEAVE |  | 100% Unreal-specific (GAS, Blueprint, UMG); no hedge-fund content. | .claude/agents/unreal-specialist.md:4 | Same as Godot/Unity families — delegation shape only. |
| .claude/agents/ue-blueprint-specialist.md | Same as Godot/Unity families — D for T2. | LEAVE |  | 100% Unreal-specific (GAS, Blueprint, UMG); no hedge-fund content. | .claude/agents/unreal-specialist.md:4 | Same as Godot/Unity families — delegation shape only. |
| .claude/agents/ue-replication-specialist.md | Same as Godot/Unity families — D for T2. | LEAVE |  | 100% Unreal-specific (GAS, Blueprint, UMG); no hedge-fund content. | .claude/agents/unreal-specialist.md:4 | Same as Godot/Unity families — delegation shape only. |
| .claude/agents/ue-umg-specialist.md | Same as Godot/Unity families — D for T2. | LEAVE |  | 100% Unreal-specific (GAS, Blueprint, UMG); no hedge-fund content. | .claude/agents/unreal-specialist.md:4 | Same as Godot/Unity families — delegation shape only. |
| .claude/agents/prototyper.md | Aggregate only; T2's skills table has no clean prototype-equivalent (mapping.txt does not... | CONDITIONAL | Q05=B | Replace HTML/Engine/Paper prototype paths with backtest/simulation/paper-trading research paths; keep PROCEED/PIVOT/KILL and the isolation rule verbatim. | .claude/agents/prototyper.md:161-162; .claude/agents/prototyper.md:7 | Quant Researcher / signal-research role — the falsifiable-hypothesis discipline, sunk-cost rule, and above all the hard isolation rule ('Prototypes must not import from... |
| .claude/agents/qa-tester.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D | Generic test-writing process with no game coupling beyond terminology; useful only if there is code/model logic to validate. | .claude/agents/qa-tester.md:3 | Test-case/backtest-scenario writer supporting the Model Validation function. |
| .claude/agents/engine-programmer.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D | Rendering/physics content is irrelevant, but 'performance-critical framework code' generalizes to a low-latency execution engine if that is ever built in-house. | .claude/agents/engine-programmer.md:3 | Core trading-platform/infra engineer (execution engine, data pipeline, memory/perf-critical framework code) if the fund builds its own execution infrastructure. |
| .claude/agents/gameplay-programmer.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D | Directly analogous role shape (implements a designed system as code) if strategies are coded in-house. | .claude/agents/gameplay-programmer.md:3 | Strategy/signal implementation engineer (translates a researched strategy into production code). |
| .claude/agents/ai-programmer.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D (ML) | Weakest fit among the code-pipeline-conditional agents — 'decision-making' generalizes but most content (pathfinding, NPC behavior) does not. | .claude/agents/ai-programmer.md:3 | ML/quant-signal engineer if the fund uses machine-learning models (behavior trees/state machines generalize weakly to signal/decision logic). |
| .claude/agents/network-programmer.md | Aggregate only; T2 removed platform.multiplayer entirely (mapping.txt config table line... | LEAVE |  | Multiplayer-specific content has minimal overlap with market-data feeds; not worth transplanting ahead of more direct donors. | .claude/agents/network-programmer.md:3 | Weak donor only for a market-data/execution connectivity role if the fund builds custom exchange/broker connectivity in-house — not a priority skeleton. |
| .claude/agents/tools-programmer.md | Aggregate only. | CONDITIONAL | Q25=C/D | Generic internal-tooling role with minimal game coupling beyond 'editor'. | .claude/agents/tools-programmer.md:3 | Internal tooling engineer (dashboards, debug utilities, pipeline automation) — generic internal-tools role, useful regardless of archetype if any internal engineering... |
| .claude/agents/ui-programmer.md | Aggregate only. | LEAVE |  | Game-UI-specific content (HUD, inventory screens) has little direct hedge-fund analog. | .claude/agents/ui-programmer.md:3 | Weak donor for an internal dashboard/PM-tool front-end role if the fund builds internal UI; not a priority. |
| .claude/agents/technical-artist.md | Aggregate only. | LEAVE |  | Entirely visual/rendering domain. | .claude/agents/technical-artist.md:3 | No hedge-fund parallel. |
| .claude/agents/performance-analyst.md | Aggregate only. | CONDITIONAL | Q05=B and Q25=C/D | Frame-time profiling generalizes cleanly to execution-latency profiling for a low-latency trading system. | .claude/agents/performance-analyst.md:3 | Latency/throughput profiling role for an execution engine, if one is built in-house (frame time -> order-to-execution latency). |
| .claude/agents/ux-designer.md | Aggregate only. | LEAVE |  | Game-UX-specific process (player onboarding flows) has weak fund relevance. | .claude/agents/ux-designer.md:3 | Weak donor for an internal reporting-dashboard UX role, low priority. |
| .claude/agents/accessibility-specialist.md | Aggregate only. | LEAVE |  | WCAG/colorblind-mode domain has no relevance to a control-framework build. | .claude/agents/accessibility-specialist.md:3 | No hedge-fund parallel. |
| .claude/agents/localization-lead.md | Aggregate only. | CONDITIONAL | Q07=B/C/D | Replace language locales with regulatory-jurisdiction locales. | .claude/agents/localization-lead.md:3 | Multi-jurisdiction documentation lead — i18n/locale-testing/translation-pipeline expertise seeds a role managing Korean FSC filings vs Cayman master-feeder vs US... |
| .claude/agents/live-ops-designer.md | Aggregate only. | LEAVE |  | No live-ops equivalent for a hedge fund's control framework. | .claude/agents/live-ops-designer.md:3 | No hedge-fund parallel (seasonal content/battle passes). |
| .claude/agents/art-director.md | Aggregate only; AD-* gates are mostly Keep for T2 (marketing agency needs brand identity)... | LEAVE |  | Owns AD-* gates, all LEAVE for the same reason above. | .claude/agents/art-director.md:3 | Weak donor only if the fund wants a formal pitch-deck/investor-collateral visual-identity role; not part of the control framework. |
| .claude/agents/audio-director.md | Aggregate only. | LEAVE |  | No sonic-identity need in a fund's operations. | .claude/agents/audio-director.md:3 | No hedge-fund parallel. |
| .claude/agents/sound-designer.md | Aggregate only. | LEAVE |  | No audio need. | .claude/agents/sound-designer.md:3 | No hedge-fund parallel. |
| .claude/agents/narrative-director.md | Aggregate only; T2 review characterizes narrative team skills as closer to 'brand voice... | LEAVE |  | No story/world-building need in a fund. | .claude/agents/narrative-director.md:3 | No direct hedge-fund role; owns ND-CONSISTENCY (LEAVE for the same reasons as the other creative gates). |
| .claude/agents/world-builder.md | Aggregate only. | LEAVE |  | No world/lore need. | .claude/agents/world-builder.md:3 | No hedge-fund parallel. |
| .claude/agents/level-designer.md | Aggregate only. | LEAVE |  | No spatial/level design need. | .claude/agents/level-designer.md:3 | No hedge-fund parallel. |
| .claude/agents/game-designer.md | Aggregate only. | LEAVE |  | No mechanics-design need in a fund; protocol shape only. | .claude/agents/game-designer.md:3 | No direct role; the 'Question-First Workflow' collaboration-protocol shape it shares with 9 other design agents is a reusable consultant-role template for a Head of... |

### 5.9 skills — management (25)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/skills/sprint-plan/SKILL.md | K (mapping.txt: "게임 의존 없음" — no game dependency) | TAKE |  | None required to run. Optional: repoint the two design/gdd/ references at whatever policy/procedure doc root the hedge fund adopts (e.g. design/policy/) — cosmetic only. | .claude/skills/sprint-plan/SKILL.md:97; .claude/skills/sprint-plan/SKILL.md:99 | Sprint execution engine for both firm-setup workstreams (FSC filing, IM/PPM drafting, custody/prime-broker onboarding) and fund-launch/ongoing-ops sprints; the... |
| .claude/skills/sprint-status/SKILL.md | K ("게임 의존 없음") | TAKE |  | None. | .claude/skills/sprint-status/SKILL.md:1 | Fast read-only status snapshot for any active workstream (regulatory filing sprint, fund-launch sprint, ops sprint) with stale-item detection (>4 days no update)... |
| .claude/skills/retrospective/SKILL.md | K ("게임 의존 없음") | TAKE |  | None. Optionally wire in as the mandatory post-incident review after /hotfix (already the case — hotfix/SKILL.md:214 calls /retrospective hotfix). | .claude/skills/retrospective/SKILL.md:1 | Sprint/milestone retrospectives; and, chained from a hotfix, the post-incident review a regulator/ODD reviewer would expect after any live trading or compliance incident. |
| .claude/skills/scope-check/SKILL.md | K ("게임 의존 없음") | TAKE |  | Reword line 157 'core player experience' → 'core mandate / investor experience' (one line). | .claude/skills/scope-check/SKILL.md:25; .claude/skills/scope-check/SKILL.md:157 | Scope-creep detection against the original firm-setup or fund-launch plan — flags additions (e.g. an unplanned second fund vehicle, an unplanned jurisdiction) with a... |
| .claude/skills/settings/SKILL.md | K ("오류 메시지 예시에만 엔진 이름" — engine name appears only in an error-message example) | TAKE |  | None to the skill itself. project.yaml's *schema* (a separate artifact, not this skill) needs hedge-fund keys defined (e.g. firm.jurisdiction, fund.structure) for this... | .claude/skills/settings/SKILL.md:456 | Single view/change surface for firm-level config (rigor, automation mode, testing strictness) once the schema is redefined for the new project.yaml. |
| .claude/skills/skill-test/SKILL.md | K ("프레임워크 중립. 전환 작업의 회귀 안전망" — framework-neutral; the transition's regression safety net) | TAKE |  | None to the skill. `CCGS Skill Testing Framework/quality-rubric.md` and `catalog.yaml` need new category rubrics once hedge-fund skill categories (e.g. 'compliance',... | .claude/skills/skill-test/SKILL.md:1 | Regression safety net for the whole Strategy-C transplant: run /skill-test static all after every newly-authored compliance/risk/quant skill to catch missing... |
| .claude/skills/skill-improve/SKILL.md | K ("프레임워크 중립") | TAKE |  | None. | .claude/skills/skill-improve/SKILL.md:1 | Iterative hardening loop for newly-authored hedge-fund skills during the build-out phase. |
| .claude/skills/estimate/SKILL.md | W (mapping: T1=K, T2=W, "GDD 용어만 교체" — only GDD terminology needs swapping) | TAKE-MODIFY |  | Swap 'design/gdd/' for the chosen policy/design doc root; replace the example 'gameplay, UI' in the Systems-affected row with e.g. 'risk engine, OMS, reporting'. | .claude/skills/estimate/SKILL.md:16; .claude/skills/estimate/SKILL.md:67 | Effort estimation for both build-out tasks (policy authoring, integration work) and, if a quant archetype is chosen, model/strategy implementation tasks — the... |
| .claude/skills/milestone-review/SKILL.md | W (mapping: T1=K, T2=W, "일반 PM 검토" — general PM review) | TAKE |  | None required. Optionally rename 'Feature Completeness' table header to 'Deliverable/Control Completeness' for house style. | .claude/skills/milestone-review/SKILL.md:1 | Milestone go/no-go review for firm-setup checkpoints (e.g. 'FSC application submitted', 'first fund closed') with the same Producer-verdict-driven AskUserQuestion... |
| .claude/skills/help/SKILL.md | W (mapping: T1=W, T2=W, "라우팅 로직은 일반적이고 단계 이름은 workflow-catalog.yaml에서 읽음" — routing logic... | TAKE-MODIFY |  | Rewrite lines 66-90 (stage detection + phase mapping) in the same commit as the new workflow-catalog.yaml; keep the artifact-check.sh delegation pattern (Step 4) and the... | .claude/skills/help/SKILL.md:70; .claude/skills/help/SKILL.md:71; .claude/skills/help/SKILL.md:77 | Fast orientation ('where am I, what's next') across firm-setup and fund-launch tracks once the catalog and this table are rewritten together. |
| .claude/skills/onboard/SKILL.md | W (mapping: T1=W, T2=W, "역할 목록(프로그래머·디자이너·내러티브·QA) 교체" — swap the role list) | TAKE-MODIFY |  | INFERENCE: replace the role branches with hedge-fund functions — portfolio manager/quant researcher (scan code root + model docs), risk officer (scan risk policy + limit... | .claude/skills/onboard/SKILL.md:58; .claude/skills/onboard/SKILL.md:60 | Role-specific onboarding doc for new hires or new Claude agent instances across the eventual org chart — especially useful for onboarding a CRO/CCO into an... |
| .claude/skills/bug-triage/SKILL.md | W (mapping: T1=K, T2=W, "일반 애자일 분류 방식" — general agile triage method) | TAKE-MODIFY |  | INFERENCE: reword S1-S4 for trading/ops impact, e.g. S1='Trading halted, risk-limit breach undetected, or data loss'; S2='Major system degraded, manual workaround... | .claude/skills/bug-triage/SKILL.md:97; .claude/skills/bug-triage/SKILL.md:98 | Systemic-trend detection (Section 3, deviation check) becomes exactly the kind of pattern an ODD reviewer or SEC exam would expect to see documented: repeated incidents... |
| .claude/skills/bug-report/SKILL.md | R (mapping: T1=K, T2=R, "Scene/Level 필드 정도만 게임 용어" — only the Scene/Level field is game... | TAKE-MODIFY |  | Replace the Category enum (line 59) with Trading / Risk / Compliance / Data / Reporting / Model / Infra; replace Scene/Level (line 67) and Game State (line 68) with... | .claude/skills/bug-report/SKILL.md:59; .claude/skills/bug-report/SKILL.md:67; .claude/skills/bug-report/SKILL.md:48 | Structured incident record with reproduction steps, root cause and closure record — the base evidentiary unit for a model-governance/audit-trail requirement (SEC Two... |
| .claude/skills/hotfix/SKILL.md | R (mapping: T1=K, T2=R, "일반 SRE 핫픽스 절차" — generic SRE hotfix procedure) | TAKE-MODIFY |  | INFERENCE: add a fourth mandatory approver (risk/compliance) alongside lead-programmer/qa-tester/producer for any fix touching a trading, risk-limit, or valuation code... | .claude/skills/hotfix/SKILL.md:107; .claude/skills/hotfix/SKILL.md:111; .claude/skills/hotfix/SKILL.md:161 | Emergency change-control workflow for a live trading-system or risk-engine defect — the exact scenario the SEC Two Sigma matter concerned (an undocumented, unapproved... |
| .claude/skills/tech-debt/SKILL.md | R (mapping: T1=K, T2=R, "scan 모드의 코드 스멜 검색만 코드 전용" — only scan mode's code-smell search... | TAKE-MODIFY |  | Rename the register 'Technical Debt Register' → 'Control Gap Register'; extend Phase 2A's scan indicators beyond code TODO/FIXME to also grep compliance/risk documents... | .claude/skills/tech-debt/SKILL.md:45; .claude/skills/tech-debt/SKILL.md:114 | Single register tracking both code debt (quant model shortcuts, risk-engine workarounds) and control gaps (missing written procedures, unassigned compliance... |
| .claude/skills/start/SKILL.md | R (mapping: T1=W, T2=R, "/brainstorm→/setup-engine→/map-systems 경로 표") | TAKE-MODIFY | Q14, Q17 (RESOLVED) | Advisor override: transplant is certain; changes depend on Q14 and Q17 (see §8). Once sequencing is decided: replace Phase 2's four options (No idea/Vague idea/Clear concept/Existing work) with a firm-stage equivalent (e | .claude/skills/start/SKILL.md:63; .claude/skills/start/SKILL.md:309; .claude/skills/start/SKILL.md:313 | First-session onboarding for the new repository, setting project.stage, modes.rigor and modes.automation before any regulatory-track work starts. |
| .claude/skills/project-stage-detect/SKILL.md | R (mapping: T1=W, T2=R, "GDD·ADR·코드 파일 수로 단계를 추정" — infers stage from GDD/ADR/code file... | TAKE-MODIFY |  | Replace the 7-row stage table with regulatory/operational milestones (INFERENCE: e.g. Formation → Registration Filed → Registration Granted → Fund Formation Docs →... | .claude/skills/project-stage-detect/SKILL.md:123; .claude/skills/project-stage-detect/SKILL.md:107; .claude/skills/project-stage-detect/SKILL.md:118 | Ongoing 'where are we, really' check comparing the founder's claimed stage against actually-observed filings/docs/code — catching e.g. a claimed 'Registration Granted'... |
| .claude/skills/adopt/SKILL.md | R (mapping: T1=W, T2=R, "GDD 8개 섹션 이름(Player Fantasy 포함)을 준수 점수 기준으로 고정" — hardcodes the... | TAKE-MODIFY |  | Redefine the 8-section GDD schema (line 135-136) as whatever regulatory-document schema is chosen (e.g. required IM/PPM sections); redefine ADR's 5 critical sections... | .claude/skills/adopt/SKILL.md:135; .claude/skills/adopt/SKILL.md:159; .claude/skills/adopt/SKILL.md:272 | Brownfield compliance-readiness audit: distinguishes 'we have a risk policy document' from 'the risk policy document actually has the sections a regulator or ODD... |
| .claude/skills/gate-check/ | R (mapping: T1=R, T2=R, "단계 기준이 게임 기준: 플레이테스트 횟수, 재미 검증, 플랫폼 인증" — phase criteria are... | TAKE-MODIFY | Q14, Q17 (RESOLVED) | Advisor override: transplant is certain; changes depend on Q14 and Q17 (see §8). Once decided: if CCO/CRO are mandatory-every-gate, they must sit outside the `workflow`-scaled panel (a 5th, always-spawned seat, not folde | .claude/skills/gate-check/SKILL.md:390; .claude/skills/gate-check/SKILL.md:394; .claude/skills/gate-check/SKILL.md:484 | PASS/CONCERNS/NOT ASSESSED/FAIL phase-gate verdicts for advancing between firm-setup milestones (e.g. Registration Filed → Registration Granted) and fund-launch... |
| .claude/skills/consistency-check/SKILL.md | W (mapping: T1=W, T2=W, "엔티티·아이템·공식 스키마를 공통 사실 레지스트리로 일반화" — generalize the... | TAKE-MODIFY |  | Replace design/registry/entities.yaml's entity/item/formula/constant schema with a regulatory-value registry (e.g. leverage cap 400% NAV, position limits, loss-rule... | .claude/skills/consistency-check/SKILL.md:17; .claude/skills/consistency-check/SKILL.md:64; .claude/skills/consistency-check/SKILL.md:104 | Write-time safety net catching e.g. the risk policy document stating a 350% leverage sub-limit while the IM states 400%, or a limit changed in one document without the... |
| .claude/skills/quick-design/SKILL.md | W (mapping: T1=W, T2=W, "MDA 미학 기준의 전환 조건" — redirect condition keyed to MDA aesthetics) | TAKE-MODIFY |  | INFERENCE: replace the two MDA-aesthetic mentions (lines 146, 291) with a policy-materiality test (e.g. 'does this change alter a regulatory representation or a... | .claude/skills/quick-design/SKILL.md:146; .claude/skills/quick-design/SKILL.md:291; .claude/skills/quick-design/SKILL.md:18 | Lightweight, auditable record for small parameter/procedure tuning (e.g. tightening an internal risk threshold within the board-approved range) without invoking the full... |
| .claude/skills/changelog/SKILL.md | R (mapping: T1=W, T2=R, "커밋을 Game과 Framework로 가르는 필터" — the filter splitting commits into... | TAKE-MODIFY |  | Rename the Game/Framework classification to Trading-Platform/Model vs. Internal-Tooling; keep the hard-stop-on-zero-match discipline (line 58-70) verbatim — it is... | .claude/skills/changelog/SKILL.md:30; .claude/skills/changelog/SKILL.md:117; .claude/skills/changelog/SKILL.md:64 | Auto-generated, provenance-checked internal changelog from git history — the audit-trail evidence a model-governance regime (SEC Two Sigma-style) requires for what... |
| .claude/skills/patch-notes/SKILL.md | R (mapping: T1=W, T2=R, "changelog와 같은 출처 필터" — same source filter as changelog) | CONDITIONAL | GAP (no Q-ID assigned) | If IR comms is in scope: INFERENCE — repoint at investor-facing quarterly/monthly updates, replacing the jargon-translation table with an... | .claude/skills/patch-notes/SKILL.md:129; .claude/skills/patch-notes/SKILL.md:3 | If pursued: automated first-draft investor updates summarizing operational/platform changes in LP-readable language, gated by human (IR/compliance) review before... |
| .claude/skills/day-one-patch/SKILL.md | R (mapping: T1=W, T2=R, "골드 마스터, 심사 피드백 같은 용어만 게임" — only terms like gold master and cert... | TAKE-MODIFY |  | Replace 'gold master'/'cert feedback'/platform-cert language (lines 20-22, 79) with 'production release build'/'custodian or regulator feedback'; replace the... | .claude/skills/day-one-patch/SKILL.md:20; .claude/skills/day-one-patch/SKILL.md:46; .claude/skills/day-one-patch/SKILL.md:151 | Scoped, rollback-first emergency-fix process for issues surfacing immediately after a fund's live-trading go-live or a regulatory filing's approval, before the first... |
| .claude/skills/localize/SKILL.md | R (mapping: T1=W, T2=R, "RTL 점검이 engine.name별 API로 분기" — RTL checks branch per... | LEAVE |  | N/A — not recommended for transplant even with modification. If bilingual investor documents become necessary, author a new, much smaller skill from scratch; at most... | .claude/skills/localize/SKILL.md:17; .claude/skills/localize/SKILL.md:292; .claude/skills/localize/SKILL.md:239 | None directly. Coverage-matrix formatting pattern only, if a translation-coverage tracker is ever built. |

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

| Component | T2 verdict | HF verdict (Q25=A/B) | HF verdict (Q25=C/D) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/skills/architecture-decision/SKILL.md | D -- T2 has no code architecture at all; hedge-fund quant branch reintroduces it. | LEAVE | TAKE-MODIFY | Q25=A/B: no engineering decisions to record | .claude/skills/architecture-decision/SKILL.md:169-209; .claude/skills/architecture-decision/SKILL.md:490-498; .claude/skills/architecture-decision/CONTRACT.md:56-57 | Model/architecture change-approval record with a single narrow approving authority. |
| .claude/skills/architecture-review/SKILL.md | D -- no ADRs exist in T2 to trace. | LEAVE | TAKE-MODIFY | Q25=A/B: skeleton donor only for the traceability-matrix idea | .claude/skills/architecture-review/SKILL.md:432-482; .claude/skills/architecture-review/SKILL.md:286-349; .claude/skills/architecture-review/SKILL.md:185-202 | Requirement-to-evidence traceability matrix for model validation lineage. |
| .claude/skills/create-architecture/SKILL.md | D -- no architecture doc needed for a document-delivery org. | LEAVE | TAKE-MODIFY | Phase 0a engine context -> compute/data-stack context. Layer map (Presentation/Feature/Core/Foundation/Platform) -> Reporting & Compliance / Portfolio Construction &... | .claude/skills/create-architecture/SKILL.md:59-92; .claude/skills/create-architecture/SKILL.md:212-230; .claude/skills/create-architecture/SKILL.md:425-460 | Master architecture blueprint + explicit CRO/CTO sign-off gate before a data/model pipeline is built. |
| .claude/skills/create-control-manifest/SKILL.md | D -- T2 builds no control manifest since it produces no ADRs. | TAKE-MODIFY | TAKE-MODIFY | Applies under BOTH branches -- (a) as a compliance/trading-rules sheet derived from IC/compliance decisions, (b) additionally as a code-forbidden-patterns sheet for the... | .claude/skills/create-control-manifest/SKILL.md:110-117; .claude/skills/create-control-manifest/SKILL.md:129-139; .claude/skills/create-control-manifest/SKILL.md:219-222 | Trading & Compliance Control Manifest carrying exposure limits, loss rules and the leverage cap as machine-checkable guardrails. |
| .claude/skills/create-epics/SKILL.md | R -- T2's PRD-based epic structure is directly reusable even without a code layer. | TAKE-MODIFY | TAKE-MODIFY | Q25=A/B: narrow (create-epics has no minimal-tier synthesis of its own; Q25=C/D: full pipeline | .claude/skills/create-epics/SKILL.md:164-176; .claude/skills/create-epics/SKILL.md:28-40; .claude/skills/create-epics/CONTRACT.md:36-44 | Epic-per-functional-module scope document with governance/requirement traceability tables. |
| .claude/skills/create-stories/SKILL.md | R -- T2 keeps the flow/role structure but rewrites Visual/Feel and the... | TAKE-MODIFY | TAKE-MODIFY | Q25=A/B: narrow (minimal-tier only, drop Story Type entirely; Q25=C/D: full (retype Logic/Integration/Config-Data, drop Visual/Feel, drop or repurpose UI | .claude/skills/create-stories/SKILL.md:169-180; .claude/skills/create-stories/SKILL.md:211-246; .claude/skills/create-stories/SKILL.md:389-399 | Story decomposition with embedded requirement/decision-record traceability and pre-written validation specs. |
| .claude/skills/story-readiness/SKILL.md | R -- structurally reusable, only vocabulary changes. | TAKE-MODIFY | TAKE-MODIFY | Q25=A/B: reduced (drop Architecture Completeness section entirely, keep Design Completeness/Scope Clarity/Open Questions/DoD as a deliverable pre-flight gate; Q25=C/D:... | .claude/skills/story-readiness/SKILL.md:36-44; .claude/skills/story-readiness/SKILL.md:259-271; .claude/skills/story-readiness/SKILL.md:275-279 | Pre-implementation (or pre-publication) readiness gate with explicit could-not-evaluate handling. |
| .claude/skills/story-done/SKILL.md | R -- reusable process shape, evidence table needs rewriting. | CONDITIONAL | TAKE-MODIFY | Q25=A/B: narrow (deliverable close-out with deviation log, drop all code-specific checks; Q25=C/D: full | .claude/skills/story-done/SKILL.md:228-234; .claude/skills/story-done/SKILL.md:360-368; .claude/skills/story-done/SKILL.md:371-397 | Model-change closure record: acceptance-criteria verification, deviation log, independent coverage review, named-approver sign-off. |
| .claude/skills/dev-story/SKILL.md | D -- entirely code-implementation machinery, absent in T2. | LEAVE | TAKE-MODIFY | Q25=A/B: nothing to implement; Q25=C/D: heaviest rewrite in the batch (modelled-on skeleton donor, not a direct transplant | .claude/skills/dev-story/SKILL.md:241-251; .claude/skills/dev-story/SKILL.md:303-316; .claude/skills/dev-story/SKILL.md:471-486 | Mandatory-secondary-reviewer trigger keyed to a risk classification that overrides self-reported risk. F-09 CORRECTION: the spawned second agent is a pre-screen, not... |
| .claude/skills/code-review/SKILL.md | D -- no code exists to review in T2. | LEAVE | TAKE-MODIFY | Phase 2 Engine Specialists -> data/quant-infra specialists. Phase 6 'Game-Specific Concerns' (frame-rate independence, hot-path allocations) -> 'Quant/Data-Specific... | .claude/skills/code-review/SKILL.md:18-45; .claude/skills/code-review/SKILL.md:75-98; .claude/skills/code-review/SKILL.md:132-138 | Decision-record-compliance code review with mandatory finding verification before any defect is reported. |
| .claude/skills/test-setup/SKILL.md | D -- no test infrastructure exists or is needed in T2. | LEAVE | TAKE-MODIFY | Q25=C/D: at the skeleton level only | .claude/skills/test-setup/SKILL.md:163-233; .claude/skills/test-setup/SKILL.md:238-372; .claude/skills/test-setup/SKILL.md:375-407 | Directory + CI scaffold enforcing 'no merge if tests fail' as a code-access-control-adjacent policy. |
| .claude/skills/test-helpers/SKILL.md | D -- no test code exists in T2. | LEAVE | TAKE-MODIFY | Q25=C/D: regenerate all code blocks for the actual quant test framework | .claude/skills/test-helpers/SKILL.md:34-61; .claude/skills/test-helpers/SKILL.md:145-157; .claude/skills/test-helpers/SKILL.md:365-404 | Assertion/factory helper generator grounded in strategy-spec Formulas sections, never guessing an unconfirmed API. |
| .claude/skills/smoke-check/SKILL.md | D -- no build or test suite exists to smoke-check in T2. | LEAVE | TAKE-MODIFY | Replace engine test-run commands (Godot/Unity/Unreal) with the quant pipeline's actual runner. Replace manual smoke batches with fund-specific critical-path items (data... | .claude/skills/smoke-check/SKILL.md:140-160; .claude/skills/smoke-check/SKILL.md:419-463; .claude/skills/smoke-check/SKILL.md:480-500 | Daily pre-trading-day pipeline health gate (data/risk/reconciliation checks). |
| .claude/skills/regression-suite/SKILL.md | D -- no code tests exist to curate in T2. | LEAVE | TAKE-MODIFY | Q25=A/B: pure code-test curation, nothing to curate; Q25=C/D: near-direct transplant | .claude/skills/regression-suite/SKILL.md:156-172; .claude/skills/regression-suite/SKILL.md:307-321 | Curated regression-coverage register tied to closed model incidents, proving a defect cannot silently recur. |
| .claude/skills/test-evidence-review/SKILL.md | R -- reusable process shape, evidence criteria need rewriting per story type. | TAKE-MODIFY | TAKE-MODIFY | Q25=A/B: narrow (Section 5 manual-evidence-quality half only: criterion linkage, sign-off completeness, artifact retention, staleness; Q25=C/D: full (Section 4... | .claude/skills/test-evidence-review/SKILL.md:123-127; .claude/skills/test-evidence-review/SKILL.md:149-154; .claude/skills/test-evidence-review/SKILL.md:208-224 | Quality-not-just-existence review of model validation evidence and sign-off completeness. |
| .claude/skills/test-flakiness/SKILL.md | D -- no CI test logs exist in T2. | LEAVE | TAKE-MODIFY | JUnit-XML/engine log parsing -> pytest/CI output parsing. Drop 'Scene/prefab load race' cause; replace with 'data snapshot / point-in-time race' (test depends on live... | .claude/skills/test-flakiness/SKILL.md:109-127; .claude/skills/test-flakiness/SKILL.md:211-219 | Backtest/pipeline flakiness triage with a quarantine-not-delete discipline (itself an audit trail of known gaps). |
| .claude/skills/security-audit/SKILL.md | D -- 2 of 6 categories are already NOT SOURCEABLE even for Unity/Unreal within CCGS... | TAKE-MODIFY | TAKE-MODIFY | Q25=A/B: narrow (Categories 1 record-tamper-evidence, 4 credential-exposure, 6 dependency-inventory only; Q25=C/D: broad (all applicable categories) PLUS a fresh... | .claude/skills/security-audit/SKILL.md:104-126; .claude/skills/security-audit/SKILL.md:152-166; .claude/skills/security-audit/SKILL.md:185-191 | Category-by-category audit with an explicit never-guess-the-pattern-set discipline; new Category 7 covers code access control. |
| .claude/skills/propagate-design-change/SKILL.md | D -- T2 makes no ADRs to cascade to. VERIFIER CORRECTION: the original review rated this... | TAKE-MODIFY | TAKE-MODIFY | Applies under BOTH branches with near-identical mechanism -- only the source-document and Decision-Record renaming differs. | .claude/skills/propagate-design-change/SKILL.md:51-66; .claude/skills/propagate-design-change/SKILL.md:130-151; .claude/skills/propagate-design-change/SKILL.md:185-210 | Design/policy-change impact propagation onto governing decision records, independent of whether code exists. |
| .claude/skills/reverse-document/SKILL.md | D -- T2 has no implementation to reverse-engineer from, despite structural reuse value at... | LEAVE | TAKE-MODIFY | Q25=A/B: design/architecture targets presume code to reverse-engineer from | .claude/skills/reverse-document/SKILL.md:117-144; .claude/skills/reverse-document/SKILL.md:185-192; .claude/skills/reverse-document/SKILL.md:221-246 | Backfilling a Model/Strategy Spec from undocumented legacy code, with inferred intent explicitly and permanently marked as unconfirmed. |
| .claude/skills/qa-plan/SKILL.md | R -- reusable shape, Story Type table needs replacing. | CONDITIONAL | TAKE-MODIFY | Q25=A/B: narrow (manual-QA-checklist skeleton only, subject to a consolidation decision with story-readiness/test-evidence-review -- see founder_questions | .claude/skills/qa-plan/SKILL.md:153-159; .claude/skills/qa-plan/SKILL.md:225-241; .claude/skills/qa-plan/SKILL.md:71-93 | Pre-cycle test/review plan classifying stories by type with explicit entry/exit criteria. |
| .claude/skills/team-qa/SKILL.md | R -- T1-equivalent, near 1:1 correspondence even at T2 for the orchestration shape. | CONDITIONAL | TAKE-MODIFY | Q25=A/B: /TAKE-MODIFY reduced (Strategy->Deliverable-Review-Plan->Manual-Review->Sign-Off shape for IC memos/DDQ responses, itself subject to the same consolidation... | .claude/skills/team-qa/SKILL.md:274-297; .claude/skills/team-qa/SKILL.md:43-66 | QA-cycle orchestration ending in an APPROVED/CONDITIONS/NOT-APPROVED/NOT-ASSESSED verdict that cannot be vacuously satisfied. |
| .claude/skills/team-release/SKILL.md | R -- nearly 1:1 correspondence with T1, minimal game coupling. | TAKE-MODIFY | TAKE-MODIFY | Applies under BOTH branches -- (a) as a major-deliverable-launch orchestration (strategy write-up, fund launch, new share class), (b) as a full release-engineering... | .claude/skills/team-release/SKILL.md:161-176; .claude/skills/team-release/SKILL.md:179-186; .claude/skills/team-release/SKILL.md:91,145 | Go/no-go release orchestration with a mandatory, unconditionally-gated approval step before any irreversible action. |
| .claude/skills/release-checklist/SKILL.md | R -- T2 keeps the Store->customer-deliverable relabeling, hedge-fund reuse is weaker than... | LEAVE | CONDITIONAL | Q25=A/B: nearly the entire body is storefront certification or code-build verification, neither exists; Q25=C/D: /TAKE-MODIFY narrow (Build Verification + Quality Gates... | .claude/skills/release-checklist/SKILL.md:122-148; .claude/skills/release-checklist/SKILL.md:218-227; .claude/skills/release-checklist/SKILL.md:19-55 | Narrow deployment-package build/quality verification checklist, mostly redundant with team-release. |
| .claude/skills/launch-checklist/SKILL.md | R -- the only skill in this area where T2 itself agrees the structure survives despite... | TAKE-MODIFY | TAKE-MODIFY | Applies under BOTH branches -- (a) drop Code Readiness/Infrastructure content but keep the department slots for any tooling that exists; (b) keep Code... | .claude/skills/launch-checklist/SKILL.md:19-55; .claude/skills/launch-checklist/SKILL.md:108-329; .claude/skills/launch-checklist/SKILL.md:323-328 | Cross-departmental fund/strategy launch-readiness gate with a single go/no-go and named executive sign-offs. |
| .claude/skills/perf-profile/SKILL.md | D -- no code performance to profile in a document-delivery org. | LEAVE | TAKE-MODIFY | Q25=A/B: no code to profile; Q25=C/D: budget-resolution + NOT-ASSESSED discipline + Phase 5 decision framework transplant near-verbatim | .claude/skills/perf-profile/SKILL.md:19-46; .claude/skills/perf-profile/SKILL.md:78-114; .claude/skills/perf-profile/SKILL.md:201-213 | Latency/capacity profiling against committed budgets with an explicit accept/fix/escalate decision framework. |
| .claude/skills/soak-test/SKILL.md | D -- no running system exists in T2 to soak-test. | LEAVE | CONDITIONAL | Q25=A/B: no running system to observe; Q25=C/D: contingent on whether the fund runs anything continuously (see founder_questions) -- if yes, TAKE-MODIFY the... | .claude/skills/soak-test/SKILL.md:102-114; .claude/skills/soak-test/SKILL.md:150-158; .claude/skills/soak-test/SKILL.md:276-286 | Extended-run leak/drift detection for any continuously-running live trading or risk-monitoring system. |

### 5.11 skills — design-domain donors (23)

| Component | T2 verdict | HF verdict | Condition (Q-ID) | Required changes | Evidence | Donor / HF use |
|---|---|---|---|---|---|---|
| .claude/skills/brainstorm/SKILL.md | T2 (mapping.txt:9): R/R, coupling C, effort L — identical to T1, no difference to explain | LEAVE |  | Body is MDA/Bartle/player-psychology (game-specific), so LEAVE stands. | .claude/skills/brainstorm/SKILL.md:262-268; .claude/skills/brainstorm/SKILL.md:269-272 | Donor for a 'fund thesis / mandate brainstorm' skill: pillar + anti-pillar + per-pillar 'design test' pattern. |
| .claude/skills/map-systems/SKILL.md | T2 (mapping.txt:30): R/R, coupling C, effort L — identical to T1 | LEAVE |  | Fully game-specific decomposition heuristics (inventory→item DB, combat→damage math etc.), so LEAVE. | .claude/skills/map-systems/SKILL.md:172-193; .claude/skills/map-systems/SKILL.md:211-222 | Donor for a strategy/workstream decomposition skill: dependency-layering + circular-dependency detection + priority tiers. |
| .claude/skills/design-system/SKILL.md | T2 (mapping.txt:22): R/R, coupling C, effort L — identical to T1 | LEAVE |  | LEAVE as a literal skill — 8 game-design sections (Player Fantasy, Tuning Knobs) don't apply. | .claude/skills/design-system/SKILL.md:495-546; .claude/skills/design-system/SKILL.md:1162-1202; .claude/skills/design-system/SKILL.md:699-726 | The single richest donor in this batch: seeds an 'investment memo authoring' skill. |
| .claude/skills/design-review/SKILL.md | T2 (mapping.txt:21): R/R, coupling C, effort L — identical to T1 | LEAVE |  | Game-specific completeness checklist and specialist table (game-designer, economy-designer, ai-programmer) don't transplant. | .claude/skills/design-review/SKILL.md:183-219; .claude/skills/design-review/SKILL.md:296-307; .claude/skills/design-review/SKILL.md:47-86 | Donor for 'Investment Committee (IC) memo review': adversarial parallel specialist review + NOT ASSESSED ranking + freshness-skip receipt. |
| .claude/skills/review-all-gdds/SKILL.md | T2 (mapping.txt:45): R/R, coupling C,P, effort L — identical to T1 | LEAVE |  | Body is entirely game-economy/pillar-drift content, LEAVE stands. | .claude/skills/review-all-gdds/SKILL.md:159-181; .claude/skills/review-all-gdds/SKILL.md:383-408; .claude/skills/review-all-gdds/SKILL.md:500-541 | Donor for a 'cross-policy / cross-strategy consistency review' skill: dependency bidirectionality, rule-contradiction scan, formula-range compatibility, economic-loop... |
| .claude/skills/prototype/SKILL.md | T2 (mapping.txt:38): R/R, coupling C, effort L — identical to T1 | LEAVE |  | Content (HTML/Engine/Paper prototype paths, jam timing) is 100% game-specific — LEAVE. | .claude/skills/prototype/SKILL.md:76-84; .claude/skills/prototype/SKILL.md:375-399; .claude/skills/prototype/SKILL.md:478-487 | Strongest donor for a paper-trading pilot skill with PROCEED/PIVOT/KILL: falsifiable hypothesis, structured one-at-a-time debrief, sunk-cost and KILL-confirmation... |
| .claude/skills/vertical-slice/SKILL.md | T2 (mapping.txt:75): R/R, coupling C,P, effort L — identical to T1 | LEAVE |  | Game-loop content is entirely game-specific (LEAVE), but the skeleton is distinct from /prototype's — this is a full-pipeline dry run at production quality, not a cheap... | .claude/skills/vertical-slice/SKILL.md:62-66; .claude/skills/vertical-slice/SKILL.md:220-228; .claude/skills/vertical-slice/SKILL.md:322-330 | Donor for an end-to-end investment-cycle dry run: falsifiable validation question, scope discipline, day-by-day velocity log, PROCEED/PIVOT/KILL with a distinct KILL... |
| .claude/skills/art-bible/SKILL.md | T2 (mapping.txt:5): W/W, coupling C,V, effort M — same both targets (unlike T1/T2 in most... | LEAVE |  | Visual identity/color/shape-language content is 100% game-specific — LEAVE, no direct hedge-fund analogue (a fund has no 'art bible'). | .claude/skills/art-bible/SKILL.md:329-334; .claude/skills/art-bible/SKILL.md:138-142 | Donor for the collaborative-authoring discipline itself, not for its content: 'never draft yourself, every section comes from a specialist agent' + batched multi-section... |
| .claude/skills/asset-audit/SKILL.md | T2 (mapping.txt:6): W/W, coupling C,V, effort M — same both targets | LEAVE |  | Naming-convention/texture-budget content is game-specific (LEAVE). | .claude/skills/asset-audit/SKILL.md:18-22; .claude/skills/asset-audit/SKILL.md:42-52 | Donor for the 'NOT ASSESSED, never a fabricated estimate' input-integrity pattern, applicable to any hedge-fund data-quality report (security-master audit,... |
| .claude/skills/asset-spec/SKILL.md | T2 (mapping.txt:7): W/W, coupling C, effort M — T2 explicitly repurposes this as a... | CONDITIONAL | GAP (no Q-ID assigned) | T2 (agency) kept this nearly as-is because content production IS its business; a hedge fund's core business is not marketing production, so the default is weaker than... | .claude/skills/asset-spec/SKILL.md:325-335; .claude/skills/asset-spec/SKILL.md:339-349 | If in-house collateral production is wanted: donor for an 'investor collateral spec' skill — entity/screen inventory, sequential cross-project asset-ID assignment, and a... |
| .claude/skills/balance-check/SKILL.md | T2 (mapping.txt:8): T1=R, T2=D (removed) — hedge fund diverges sharply from T2 here | LEAVE |  | T2 (a content/consulting agency) rightly removed this outright — an agency has no numeric game-formula domain to check. | .claude/skills/balance-check/SKILL.md:94-99; .claude/skills/balance-check/SKILL.md:18-32 | The strongest numeric-rule donor in the whole review area: dominant-strategy/'strictly better with no tradeoff' detection generalises directly to leverage-cap (400%... |
| .claude/skills/content-audit/SKILL.md | T2 (mapping.txt:15): R/R, coupling C, effort L — identical to T1 | LEAVE |  | Game content-count logic (enemies, levels, items) doesn't transplant, LEAVE. | .claude/skills/content-audit/SKILL.md:196-217; .claude/skills/content-audit/SKILL.md:43-57 | Donor for a 'mandate vs. executed portfolio' reconciliation audit: planned-vs-implemented gap table with COMPLETE/IN PROGRESS/EARLY/NOT STARTED status and a HIGH... |
| .claude/skills/playtest-report/SKILL.md | T2 (mapping.txt:35): T1=W, T2=R — T2 needed more rework than T1 (a content agency's... | LEAVE |  | Session-info template (build, tester, platform) is game-specific, LEAVE. | .claude/skills/playtest-report/SKILL.md:107-119; .claude/skills/playtest-report/SKILL.md:123-140 | Donor for a 'post-trade / incident post-mortem' skill: four-bucket finding routing (design/balance/bug/polish → strategy/risk-parameter/operational-incident/process)... |
| .claude/skills/ux-design/SKILL.md | T2 (mapping.txt:73): T1=W, T2=D — T2 removed it outright (an agency does not build... | CONDITIONAL | GAP (no Q-ID assigned) | T2 removed it flat (D) because a marketing/consulting agency has no UI-implementation pipeline at all — its content overlap with UX authoring is near zero. | .claude/skills/ux-design/SKILL.md:568-589; .claude/skills/ux-design/SKILL.md:622-648 | If an investor portal is built: donor for a spec-authoring skill with retrofit-mode section-status detection and a fixed cross-reference/coverage check. |
| .claude/skills/ux-review/SKILL.md | T2 (mapping.txt:74): T1=W, T2=D — removed for the same reason as ux-design | CONDITIONAL | GAP (no Q-ID assigned) | Read-only checklist against UX-spec sections doesn't transplant literally (LEAVE), consistent with T2's D. | .claude/skills/ux-review/SKILL.md:242-254 | Donor for the 'gate against an uncommitted standard reports NOT ASSESSED, never COMPLIANT' pattern — reusable well beyond UI, e.g. an IC gate checking a strategy against... |
| .claude/skills/setup-engine/SKILL.md | T2 (mapping.txt:49): T1=R, T2=D — T2 removed outright (an agency has no tech-stack... | CONDITIONAL | GAP (no Q-ID assigned) | Entire 1,254-line body is engine/rendering/naming-table content (T1=R, T2=D, both correct — no game-adjacent value for a fund). | .claude/skills/setup-engine/SKILL.md:60-64; .claude/skills/setup-engine/SKILL.md:88-106; .claude/skills/setup-engine/SKILL.md:162-174 | Donor for the guided-selection interaction pattern only: prior-experience short-circuit, platform-elimination-first ordering, an honest-tradeoffs comparison table, and a... |
| .claude/skills/team-audio/SKILL.md | T2 (mapping.txt:59): D/D — same as T1, no hedge-fund-relevant domain at all | LEAVE |  | Audio-direction content has no hedge-fund analogue at all — flat LEAVE, matching T2's D exactly (no divergence). | .claude/skills/team-audio/SKILL.md:46-53; .claude/skills/team-audio/SKILL.md:93-93 | Orchestration skeleton donor (see reuse_patterns): Phase-0 config resolve, team.size active-set collapse with mandatory 'Active set' announcement, bounded... |
| .claude/skills/team-combat/SKILL.md | T2 (mapping.txt:60): D/D — same as T1 | LEAVE |  | Combat-mechanic content has no hedge-fund analogue, matches T2's D exactly. | .claude/skills/team-combat/SKILL.md:142-153; .claude/skills/team-combat/SKILL.md:155-160; .claude/skills/team-combat/SKILL.md:181-191 | Fullest example of the gated sequential+parallel orchestration skeleton: Design→Architecture(engine-validation gate)→parallel... |
| .claude/skills/team-level/SKILL.md | T2 (mapping.txt:61): D/D — same as T1 | LEAVE |  | Level-layout content has no fund analogue, matches T2's D. | .claude/skills/team-level/SKILL.md:111-120; .claude/skills/team-level/SKILL.md:136-144; .claude/skills/team-level/SKILL.md:176-181 | Best example of an ordering-dependency lesson (visual targets are INPUTS to layout, not outputs of it) plus a missing-dependency handling pattern (adjacent-area check)... |
| .claude/skills/team-live-ops/SKILL.md | T2 (mapping.txt:62): R/R — identical to T1, no divergence | LEAVE |  | Season/battle-pass content is game-specific, but this is the only team-* skill in the batch that already implements a real policy-compliance gate end-to-end, including... | .claude/skills/team-live-ops/SKILL.md:159-161; .claude/skills/team-live-ops/SKILL.md:161-164 | The single best orchestration-level donor for an IC compliance gate: check design output against a named policy file, block sign-off on a violation, force... |
| .claude/skills/team-narrative/SKILL.md | T2 (mapping.txt:63): T1=R, T2=W — T2 needed less rework (a content agency has a... | LEAVE |  | Story/dialogue content has no fund analogue (LEAVE), but T2 rated this W not R because a content agency's narrative team maps almost directly onto its own domain — a... | .claude/skills/team-narrative/SKILL.md:92-105; .claude/skills/team-narrative/SKILL.md:155-155 | Donor for two generic conventions: (1) a fixed per-agent destination-path table with an explicit 'not a free choice' rationale tied to downstream readers; (2)... |
| .claude/skills/team-polish/SKILL.md | T2 (mapping.txt:64): T1=R, T2=D — T2 removed it (an agency has no performance/hardening... | LEAVE |  | Performance/VFX/audio-polish content is fully game-specific — LEAVE, and T2's D is right for an agency, so the divergence is explained by domain fit rather than... | .claude/skills/team-polish/SKILL.md:160-167; .claude/skills/team-polish/SKILL.md:110-116 | Donor for a 'pre-launch operational readiness' team skill: Assessment→Optimization→parallel specialist polish→Hardening(soak/stress/regression)→binary... |
| .claude/skills/team-ui/SKILL.md | T2 (mapping.txt:67): T1=W, T2=D — T2 removed it outright (agency has no UI implementation... | LEAVE |  | UX/visual-design pipeline content has no fund analogue — LEAVE, matching T2's D. | .claude/skills/team-ui/SKILL.md:115-118; .claude/skills/team-ui/SKILL.md:120-129 | Donor for two input-integrity conventions worth reusing verbatim: (1) report the presence/ABSENT status of every context input before designing anything, not just the... |

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
