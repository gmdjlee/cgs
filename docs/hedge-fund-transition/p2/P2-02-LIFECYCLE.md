# HFT-P2-02 — Lifecycle catalog design

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-02 |
| Title | Lifecycle catalog design |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | PLAN.md §6.0-6.3, §8 (P2 task 2); ORG-BLUEPRINT.md §11, §11A; evidence/design-addendum-01.md §3, §6; TRANSPLANT-MANIFEST.md §6 (SB-07, SB-10, SB-14, SB-22); .claude/docs/workflow-catalog.yaml; .claude/scripts/artifact-check.sh; .claude/hooks/yaml-helper.sh; .claude/skills/help/SKILL.md; .claude/skills/gate-check/SKILL.md, CONTRACT.md; .claude/skills/project-stage-detect/SKILL.md; .claude/skills/ux-design/SKILL.md; .claude/docs/quick-start.md |
| Writing standard | ASD-STE100 |

## 2. Purpose

This document sets the design for the draft lifecycle catalog,
`docs/hedge-fund-transition/p2/workflow-catalog.draft.yaml`. That file is a
draft replacement for `.claude/docs/workflow-catalog.yaml` (PLAN.md §8, P2
task 2). This document explains the design choices, lists every CCGS reader
of the live catalog that needs a change, and records the founder decisions
the design still needs.

## 3. The stage axis

DEC-21 sets one stage axis: the setup stages S1-S8 and the growth stages
G1-G3 (PLAN.md §6.2; ORG-BLUEPRINT.md §11.1, §11.2). `project.stage` stays
one scalar (F-11; PLAN.md §6.2). The draft catalog's `phases:` key holds
these 11 stages, plus one proposed stage (§4 below), each keyed by its
lower-case id (`s1` .. `s8`, `g1` .. `g3`).

**S1-S8** (source: HF-REF-05 표 4-2, HF-REF-18 표 10-1; ORG-BLUEPRINT.md
§11.1):

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

**G1-G3** (source: HF-REF-08 표 6-2; ORG-BLUEPRINT.md §11.2): G1 founding
stage, G2 growth stage, G3 institutionalization stage. G1-G3 match the
three organization stages in PLAN.md §6.1.

The draft catalog's `required_artifacts` per stage come from the "Outputs"
and "Exit criteria" columns of ORG-BLUEPRINT.md §11.1 (S1-S8) and the
"Features" column of §11.2 (G1-G3). These are legal and organizational
deliverables, not repo files, so each step's `artifact:` block carries a
`note:` (the catalog's existing fallback for a step whose completion is not
glob-detectable: the live catalog already uses this convention, for
example its `implement` step, workflow-catalog.yaml:322-325) rather than a
`glob:`.

The per-idea investment cycle (HF-REF-09 §7.1: idea, analysis, portfolio,
pre-check, execution, monitoring, post-review) is not a stage. It runs
inside a stage, once per idea (ORG-BLUEPRINT.md §11.3). It is out of the
draft catalog's `phases:` axis by design and is not modeled in this file.

## 4. The proposed pre-setup stage

Wave W1 runs now, before fund setup starts (PLAN.md §8 task 2; DEC-21). The
draft catalog adds a stage before S1, id `pre-setup`, label "S0:
Information core (PROPOSED)", `status: PROPOSED`. Its gate uses DEC-27's
first-milestone definition (one daily briefing, one stock through screen,
pitch, red-team review, synthesis, and the virtual investment committee) as
its required artifacts, because DEC-27 is the only founder-set completion
bar for the W1-only period. This is a design proposal, not a settled fact.
See founder decision P2-L-01.

## 5. W1 information cycles

DEC-21 pairs the stage axis with information cycles: daily, weekly, and
monthly (PLAN.md §6.2). The addendum adds an on-demand form (DEC-14; §11A.1)
and a founder-request-only form for `/refresh-facts` (DEC-35). These cycles
run **beside** the stage axis, not as stages. `project.stage` never takes a
cycle name.

The draft catalog models this as a new top-level `cycles:` section (sibling
to `phases:`), grouped `daily`, `weekly`, `monthly`, `on_demand`. Every W1
product in ORG-BLUEPRINT.md §11A / addendum §6 appears in the section below.
Cadence is taken from ORG-BLUEPRINT.md §11A / addendum §6, except
`/refresh-facts`: the addendum's cadence table (addendum §6, written before
round 8) says "Quarterly"; DEC-35 (round 8) overrides this to "the founder's
request only, no fixed schedule". The draft catalog follows DEC-35, the
later and more specific decision. This is a **resolved conflict**, recorded
here so the founder sees it, not a founder decision item.

| Cycle | Products | Source |
|---|---|---|
| Daily | /daily-briefing, /event-alert, /risk-report (summary form) | ORG-BLUEPRINT.md §11A; DEC-14 |
| Weekly | /weekly-report, /house-view, /idea-screen, /portfolio-review, /risk-report (full form) | ORG-BLUEPRINT.md §11A; DEC-14 |
| Monthly | /call-review | ORG-BLUEPRINT.md §11A; DEC-24 |
| On demand | /ask, /stock-pitch → /red-team-review → /cio-synthesis → virtual investment committee, /coverage-config, /refresh-facts | ORG-BLUEPRINT.md §11A; DEC-14, DEC-16, DEC-22, DEC-35 |

`/risk-report` has two cadence forms per DEC-14 and addendum §6 (a daily
summary and a weekly full report), so it appears twice, once per cycle,
distinguished by a `form:` field on each entry. Every other product appears
exactly once. Verified by parsing the draft file and checking each of the
14 ORG-BLUEPRINT.md §11A products resolves to exactly one cycle location
(§9 below).

The virtual investment committee (DEC-22) is not a slash-command skill; it
is a virtual body the W1 roster convenes after `/cio-synthesis`. It is
listed in the `on_demand` cycle with `sequence: 4` so a reader can render
the bull-bear-synthesis-committee order as a pipeline (DEC-16, DEC-22,
DEC-23). In W1, chief-of-staff keeps its minutes (INFERENCE,
ORG-BLUEPRINT.md §11.3: the blueprint itself marks this INFERENCE and
defers the owner confirmation to P2).

### 5.1 Readers that ignore the `cycles:` section, and why

`.claude/scripts/artifact-check.sh` never opens `cycles:`. Its parser sets
`in_phases = (s == "phases:")` at every 0-indent line
(artifact-check.sh:138). The next 0-indent key after the `phases:` block,
`cycles:` in this draft, flips that flag back off, so the parser's
per-step logic (ind == 6, `- id:`) never runs against it
(artifact-check.sh:125-181). Verified empirically: running
`artifact-check.sh` against a fixture root holding this draft file reports
`PHASES: 12` and 17 steps, none of them from `cycles:` or `waves:` (§9
below). No code change is needed in this script for the `cycles:` section to
be safely inert to it.

`.claude/hooks/yaml-helper.sh` never opens `.claude/docs/workflow-catalog.yaml`
at all: it resolves `project.yaml` and `project.local.yaml` only. Its one
mention of the catalog is a comment (yaml-helper.sh:1221) about an `any_of`
convention, not a read. It is unaffected by `cycles:` for the same reason:
it never reads the file. It still needs a change for the stage axis itself
(§6, row 2).

## 6. CCGS readers of `workflow-catalog.yaml`: every one, and its change

Found by `grep -rln "workflow-catalog" .claude/` and cross-checked against
TRANSPLANT-MANIFEST.md §6's SB-07, SB-10, SB-14, and SB-22, which name four
of these exact break points. This is the SB-/silent-break risk PLAN.md §8
task 2 asks this document to close.

| # | Reader | File:line | What it does today | Change needed | SB ref |
|---|---|---|---|---|---|
| 1 | Artifact parser | `.claude/scripts/artifact-check.sh:68` (CATALOG path), `:125-181` (hand-rolled indentation parser) | Walks `phases:` → `- id:` steps → `artifact:` block, keyed on exact indentation, not real YAML | None to the parser itself: the draft keeps the same `phases:`/`steps:`/`artifact:` shape on purpose (§9 confirms it still parses). Its CALLERS (rows 2-5) must pass the new stage ids as `--phase` values. | SB-10 |
| 2 | Stage enum validator | `.claude/hooks/yaml-helper.sh:473` (`project.stage::Concept\|Systems Design\|...`); fall-through checks at `:843-846` (Python enum validation) and `:1149-1151` (`resolve_setting`) | Rejects any `project.stage` value not in the fixed 7-name list. The rejection is silent past a `notes:` line almost nobody reads | Replace the enum value list with `pre-setup\|s1\|s2\|s3\|s4\|s5\|s6\|s7\|s8\|g1\|g2\|g3`. No change needed at `:843-846` or `:1149-1151`: they read the table generically. | SB-14 (also SB-07's pattern, for the sibling `engine.name` enum) |
| 3 | `/help` | `.claude/skills/help/SKILL.md:37` (instruction to read the whole catalog file), `:70-77` (hardcoded `project.stage` value → catalog phase key table) | An LLM-executed instruction: read the raw file, then look up the resolved `project.stage` string in a 7-row hand-written table to find the matching phase key | Rewrite the `:70-77` table for the 12 new stage ids (a 1:1 identity map once project.stage values equal phase keys, §7). Add an explicit instruction to also read and surface the `cycles:` section (today's due daily/weekly/monthly products), since the current instructions never mention it and an LLM reader has no cue to use it. | SB-22 |
| 4 | `/gate-check` | `.claude/skills/gate-check/SKILL.md:4` (argument-hint enum), `:24-34` (7-stage table), `:100-105` (gate → reference-file table), `:241-242` (`--phase` call into artifact-check.sh) | Hardcodes the 7 game-dev phases, a gate-reference-file per adjacent pair, and calls row 1's script with the old phase ids | Rewrite the argument-hint and stage table to the 12 new ids and `next_phase` chain; rewrite or replace each `gate-*.md` reference file for the fund-domain gates; update the seat/verdict handling to read each stage's `gate:` block (control_seats, verdict_vocabulary) instead of the fixed director-panel width (also closes SB-21, a separate but related risk on the same file). | none named directly; adjacent to SB-21 |
| 5 | `/gate-check` contract | `.claude/skills/gate-check/CONTRACT.md:11,20-25,28,37,41,46,50,63-67` | Documents the same 7-phase vocabulary as a machine-readable handoff contract, including the target-phase enum and the phase-to-file table | Update every phase-name reference to the 12 new ids, in the same commit as row 4. CONTRACT.md and SKILL.md must not drift: this file's own SB-11 names that exact risk. | adjacent to SB-11 |
| 6 | `/project-stage-detect` | `.claude/skills/project-stage-detect/SKILL.md:105-122` (heuristics intro), `:123-131` (7-row stage-indicator table) | Does not open `workflow-catalog.yaml` directly; carries its own hardcoded copy of the phase list and a game-dev artifact heuristic per phase (concept doc, systems index, engine config, source-file counts) | Replace the indicator table with fund-domain heuristics per new stage (for example: `pre-setup` if the W1 roster exists and no S1 artifact is on file; `s1` if a business plan exists and no corporate registration; and so on through G1-G3). It never reads `cycles:` and does not need to, because cadence is not a stage. | none named; same failure shape as SB-22 |
| 7 | `/ux-design` | `.claude/skills/ux-design/SKILL.md:62` | Cites the catalog only to say three places (including it) all check `design/accessibility-requirements.md` at a fixed path | None. The path check is stage-independent. | none |
| 8 | Quick-start index | `.claude/docs/quick-start.md:282` | One description line: "workflow-catalog.yaml: 7-phase pipeline definition (read by /help)" | Update the phase count and description to match the new 12-stage-plus-cycles shape, for accuracy (documentation only, not executable). | none |

Not a direct reader of `workflow-catalog.yaml`, but a downstream consumer of
`project.stage` that inherits row 2's fix once applied: `statusline.sh`
(stage display; SB-09 covers its own separate game-file heuristic),
`detect-gaps.sh`, `session-start.sh`. These are out of this document's scope
(workflow-catalog.yaml readers only) and are not re-listed here.

## 7. The `project.stage` vocabulary simplification

The live catalog uses two different vocabularies for the same concept: catalog
phase keys are lower-kebab (`systems-design`), while `project.stage` values are
Title Case with spaces (`Systems Design`). The only link between them is the
hand-written table at `.claude/skills/help/SKILL.md:70-77`. This is exactly
the table SB-22 names as a silent-break point. The draft catalog sets
`project.stage` values equal to the phase keys themselves (`s1`, `g2`,
`pre-setup`, all lower-case, no spaces), so that table becomes an identity
map. This removes the SB-22 failure mode rather than re-implementing it for
new names. This is a P2 implementation choice under DEC-21, not itself a
founder decision. No vocabulary alternative was on the table in the
decision log.

## 8. The gate on every stage

Each `phases:` entry in the draft carries a `gate:` block (PLAN.md §6.3;
DEC-17, DEC-18):

- **`required_artifacts`**: the exit-criteria list, from ORG-BLUEPRINT.md
  §11.1 (S1-S8) or §11.2 (G1-G3).
- **`control_seats`**: `cro` from W1 (active at every stage, including
  `pre-setup`); `cco` joins from W2's activation stage onward, `s1` through
  `g3` (DEC-18). `pre-setup`'s gate lists `[cro]` only, because W2 (and so
  `cco`) has not activated yet (`waves_active: [w1]`).
- **`verdict_vocabulary`**: `[PASS, CONCERNS, FAIL, "NOT ASSESSED"]` on
  every gate, unchanged from PLAN.md §6.3. Precedence (not repeated per
  gate; global): FAIL beats CONCERNS, CONCERNS beats NOT ASSESSED, NOT
  ASSESSED beats PASS.
- **`wave_trigger`**: the wave-activation fact for that stage (§9 below
  confirms every stage carries one).

Per DEC-17, a control decision at any gate needs the cro verdict (and cco's,
once active) plus a recorded founder approval receipt; a decision without a
receipt reads NOT ASSESSED. The draft catalog does not encode the receipt
mechanism itself. DEC-17 already rules out a protected-path hook, so the
receipt stays a recorded-approval convention, not a YAML field.

## 9. Wave triggers on the stage entries

DEC-21 and addendum §3 set two triggers:

- **W2 activates at S1** (addendum §3; PLAN.md §6.1). The draft sets
  `waves_active: [w1, w2]` starting at the `s1` entry and holding through
  `g1`.
- **W3 activates at G2 or G3** (addendum §3; HF-REF-08 표 6-2). The draft
  sets `waves_active: [w1, w2, w3]` starting at the `g2` entry (the first
  stage where the trigger can be true) and holding through `g3`.

Verified by parsing the draft file: every one of the 12 `phases:` entries
has a non-empty `gate` key and a `waves_active` list (§3 code run below).

```
$ python3 -c "
import yaml
d = yaml.safe_load(open('docs/hedge-fund-transition/p2/workflow-catalog.draft.yaml'))
phases = d['phases']
print('missing gate:', [k for k,v in phases.items() if 'gate' not in v])
print('missing waves_active:', [k for k,v in phases.items() if 'waves_active' not in v])
print('stage count:', len(phases))
"
missing gate: []
missing waves_active: []
stage count: 12
```

The draft file parses under `python3 -c "import yaml,sys;
yaml.safe_load(open(sys.argv[1]))"` with no error (PyYAML is present in
this environment; confirmed by running the check directly, not assumed).
`.claude/scripts/artifact-check.sh` was also run directly against a fixture
copy of the draft file: it reports `PHASES: 12`, all 12 stage ids present,
17 steps, 17 `NO_CHECK` (every step's artifact is a `note:`, which is
correct: these are external/legal deliverables, not repo globs, per §3).

## 10. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-L-01 | Does the pre-S1 period get a formal `project.stage` value (`pre-setup`, label "S0: Information core"), or does it stay unstaged (no `project.stage` value until S1)? | **A.** Adopt `pre-setup` as a real, gated stage (as drafted): it gets a `gate:` block, appears in `/help` and `/gate-check`, and `project.stage` can be set to it. **B.** Track the W1-only period informally (a note in session state), leave `project.stage` unset until S1 begins, and drop the `pre-setup` entry from the catalog. **C.** Adopt `pre-setup` but without a gate (no PASS/CONCERNS/FAIL verdict for it, informational only). **D.** Use a different label than "S0: Information core" for the same stage. | **A**. DEC-21 already says W1 runs on the stage axis's near side ("before S1", PLAN.md §8 task 2). `/gate-check`, `/help`, and `/project-stage-detect` all key off `project.stage`. Leaving it unset (Option B) makes every one of those three tools report "no stage detected" for the entire period the founder is actually using the product. Source: DEC-21, DEC-27 (first-milestone criteria used as its gate). |
| P2-L-02 | Should `/refresh-facts`'s addendum §6 cadence ("Quarterly") be corrected in the addendum itself, or does DEC-35's later, more specific answer ("founder's request only") simply supersede it as drafted, with no addendum edit? | **A.** Leave addendum §6 as historical record; the draft catalog (and any future document) cites DEC-35 as authoritative. **B.** Edit addendum §6's table to say "Founder request only (DEC-35)", replacing "Quarterly". **C.** Add a footnote to addendum §6 pointing to DEC-35 without changing the cell text. | Resolved by the Advisor: **A**. The addendum is a frozen record (`evidence/design-addendum-01.md:7`, "Status: Frozen record of Advisor decisions"). PLAN.md, ORG-BLUEPRINT.md, and this draft already cite DEC-35 as the authority. Not asked of the founder. |
| P2-L-03 | `/gate-check`'s per-adjacent-pair reference files (`gate-systems-design.md` etc., `.claude/skills/gate-check/references/`) need full rewrites for the 11 new stage transitions (`pre-setup` to `s1` through `g2` to `g3`). Should P3 write one reference file per transition (11 files, matching the live convention), or should the `gate:` block already in this draft catalog (required_artifacts, control_seats, verdict_vocabulary) replace the reference-file convention entirely? | **A.** Keep one reference file per transition (11 files), each expanding on its stage's `gate:` block with fuller checklist prose, as the live catalog does today. **B.** Retire the reference-file convention; `/gate-check` reads the `gate:` block directly and generates its checklist from `required_artifacts` at run time, no separate files. **C.** Hybrid: keep reference files only for the S1-S8 setup transitions (legal/regulatory, needing more prose) and read the `gate:` block directly for G1-G3 (organizational, shorter). | **B**. The `gate:` block already carries every fact the live reference files exist to hold (required artifacts, seats, verdict vocabulary; PLAN.md §6.3). A second copy of the same facts is exactly the drift risk `.claude/rules/skill-authoring.md` obligation 2 and TRANSPLANT-MANIFEST.md's SB-11 warn about (a reference file edited without its SKILL.md, or vice versa). Source: PLAN.md §6.3; skill-authoring.md; TRANSPLANT-MANIFEST.md §6 SB-11. This recommendation is P3-scope to execute; P2 records the design call only. |

## 11. Traceability

| P2 task / DEC-NN | Section |
|---|---|
| P2 task 2 (draft lifecycle catalog) | §3, §5, whole `workflow-catalog.draft.yaml` |
| DEC-21 (stage axis + information cycles; one `project.stage` scalar) | §3, §5, §7 |
| DEC-14 (delivery cadence: daily, weekly, on-demand, alerts) | §5 |
| DEC-16 (bull/bear/synthesis method) | §5 |
| DEC-17 (agent verdict + user approval; NOT ASSESSED without a receipt) | §8 |
| DEC-18 (fixed control seats: cro from W1, cco from W2) | §8 |
| DEC-22 (virtual investment committee, minutes) | §5 |
| DEC-23 (/stock-pitch 8-section format) | §5 |
| DEC-24 (/call-review cadence) | §5 |
| DEC-27 (first milestone) | §4 |
| DEC-35 (/refresh-facts on founder request only) | §5, P2-L-02 |
| TRANSPLANT-MANIFEST.md §6 SB-07, SB-10, SB-14, SB-22 (silent-break risk) | §6 |
