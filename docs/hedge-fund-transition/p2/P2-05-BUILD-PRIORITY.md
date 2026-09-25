# HFT-P2-05: Skill build priority and deferred components

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-05 |
| Title | Skill build priority and deferred components |
| Version | 1.0 |
| Date | 2026-09-25 |
| Status | Approved by the founder (AR-P2-0001, 2026-09-25) |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | [PLAN.md](../PLAN.md) §6.0, §8 (P2, P5, P6); [ORG-BLUEPRINT.md](../ORG-BLUEPRINT.md) §6, §11A; [TRANSPLANT-MANIFEST.md](../TRANSPLANT-MANIFEST.md) §4, §9.3, §9.4, §10.3; [evidence/design-addendum-01.md](../evidence/design-addendum-01.md) §6 |
| Writing standard | ASD-STE100 |

This document covers P2 task 5 (PLAN.md §8, P2, task 5): "Set the skill
build priority from the Q22 and Q23 answers."

## 2. Scope and method

DEC-26 (Q22) and DEC-27 (Q23) set the founder's build priority. This
document turns those two decisions into one ordered build sequence for
P5 (the pilot) and P6 (the full W1 roster), lists the foundation
transplants that must exist before either phase starts, and proposes a
place for every skill DEC-26 left unordered. It then resolves the 16
DEFERRED transplant rows from TRANSPLANT-MANIFEST.md §10.3.

Every order number below is one continuous sequence across P5 and P6,
because P5's pilot builds are the first 13 items of the same W1 roster
and skill set that P6 completes.

## 3. Foundation transplants (must exist before P5 or P6 starts)

TRANSPLANT-MANIFEST.md §4 (Table 4-1) sets the minimum transplant set
and its group order. §9.3 adds the W1-specific support components. Both
run in Phase P3, ahead of P5.

**Table 3-1. Foundation transplant order**

| Order | Group | Component(s) | Purpose | Depends on | Citation |
|---|---|---|---|---|---|
| F1 | 1 | `project.yaml` (new schema), then `.claude/hooks/yaml-helper.sh` | Config file and the resolver every other kept file sources | Nothing | TRANSPLANT-MANIFEST.md §4 Table 4-1 rows 1 |
| F2 | 2 | `session-start.sh`, `pre-compact.sh`, `post-compact.sh`, `session-stop.sh`, `rotate-session-state.sh`, `session-state.md` template, `context-management.md` | Session-state hooks, all gated on the same `session_state_enabled()` check | F1 | TRANSPLANT-MANIFEST.md §4 Table 4-1 rows 2 |
| F3 | 3 | `validate-commit.sh`, `validate-push.sh`, `artifact-check.sh` (+ a fresh `workflow-catalog.yaml`), `adr-dep-graph.sh` | Gate-invocation support; the one blocking hook in the repo | F1 | TRANSPLANT-MANIFEST.md §4 Table 4-1 rows 3 |
| F4 | 4 | `log-agent.sh`, `log-agent-stop.sh`, `log-instructions.sh` (wired into `settings.json` in this same step) | Audit-trail hooks | F1 | TRANSPLANT-MANIFEST.md §4 Table 4-1 rows 4 |
| F5 | 5 | `validate-skill-change.sh` | Fires on a skill edit; advises `/skill-test` | None | TRANSPLANT-MANIFEST.md §4 Table 4-1 row 5 |
| F6 | 6 | `.claude/settings.json` (rewritten last) | Hook wiring, permissions, statusline wiring | F1-F5 | TRANSPLANT-MANIFEST.md §4 Table 4-1 row 6 |
| F7 | 7 | `statusline.sh`, `notify.sh` (optional) | ctx%/model/rigor display; desktop notification | F1 | TRANSPLANT-MANIFEST.md §4 Table 4-1 row 7 |
| F8 | 8, split | `validate-assets.sh` (TAKE-MODIFY): point its path filter at `config/risk/`. `code-root-resolution.md` stays off. | Limit-file path validation; SB-08 | F1 | TRANSPLANT-MANIFEST.md §10.3 (DEC-19) and §10.4 note 2; code-root-resolution.md stays off because Q25 = B (DEC-29). Erratum E-01 (HFT-P2-00 §5). |
| F9 | W1 support | `.claude/skills/gate-check/` | PASS/CONCERNS/NOT ASSESSED/FAIL verdict, every W1 product needs it | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F10 | W1 support | `.claude/skills/consistency-check/SKILL.md`, rewritten as the fact registry | Fact registry every stock call and house-view cites (DEC-16) | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F11 | W1 support | `.claude/skills/skill-test/SKILL.md` | Static and category checks on every new W1 skill | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F12 | W1 support | `.claude/skills/sprint-plan/SKILL.md`, `.claude/skills/sprint-status/SKILL.md` | Runs the W1 build cycle | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F13 | W1 support | `.claude/skills/scope-check/SKILL.md` | Catches scope creep past the W1 roster | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F14 | W1 support | `.claude/skills/retrospective/SKILL.md` | Closes each build cycle | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |
| F15 | W1 support | `.claude/skills/help/SKILL.md`, `.claude/skills/onboard/SKILL.md` | Orientation once the W1 agents exist | F1-F6 | TRANSPLANT-MANIFEST.md §9.3 |

F8 runs in part: `validate-assets.sh` transplants with a new path filter for `config/risk/` (DEC-19). `code-root-resolution.md` stays off, because Q25 = B (DEC-29). Erratum E-01 corrected this row after approval (HFT-P2-00 §5).

## 4. P5 and P6 build sequence

Columns: **CCGS donor** cites TRANSPLANT-MANIFEST.md §9.4 Table 9-1 for
a skill and ORG-BLUEPRINT.md §6 ("CCGS donor skeleton" column) for an
agent. Where neither document names a donor, the donor is Worker
INFERENCE and is marked so.

**Table 4-1. P5 pilot slice (DEC-27)**

| Order | Skill or agent | Phase | Owner agent | CCGS donor | Depends on | DEC |
|---|---|---|---|---|---|---|
| 1 | chief-of-staff (agent) | P5 | n/a | producer | Foundation (§3) | DEC-27, DEC-09 |
| 2 | `/daily-briefing` (skill) | P5 | chief-of-staff | sprint-status, the read-only status snapshot (INFERENCE; no donor named in §9.4) | 1 | DEC-27, DEC-26, DEC-14 |
| 3 | idea-screener (agent) | P5 | n/a | balance-check (outlier detection) | Foundation (§3) | DEC-27 (agent build is INFERENCE: PLAN.md §8 P5 task 3 names the skill, not the agent, but `/idea-screen` needs its owner agent to exist) |
| 4 | `/idea-screen` (skill) | P5 | idea-screener | balance-check, the outlier-detection mechanism | 3 | DEC-27, DEC-26 |
| 5 | research-analyst (agent) | P5 | n/a | game-designer (Question-First Workflow shape only) | Foundation (§3) | DEC-27 (agent build is INFERENCE, same reason as row 3) |
| 6 | `/stock-pitch` (skill) | P5 | research-analyst | design-system, the section-cycle draft flow | 5 | DEC-27, DEC-23 |
| 7 | red-team-analyst (agent) | P5 | n/a | design-review (adversarial reviewer brief) | Foundation (§3) | DEC-27 (agent build is INFERENCE, same reason as row 3) |
| 8 | `/red-team-review` (skill) | P5 | red-team-analyst | design-review, the adversarial reviewer brief | 6, 7 | DEC-27, DEC-16 |
| 9 | cio (agent) | P5 | n/a | creative-director (protocol shape only) | Foundation (§3) | DEC-27 (agent build is INFERENCE, same reason as row 3) |
| 10 | `/cio-synthesis` (skill) | P5 | cio | team-\* skeleton, the bull/bear/synthesis sequence | 8, 9 | DEC-27, DEC-16 |
| 11 | cro (agent) | P5 | n/a | technical-director (Strategic Decision Workflow shape); systems-designer (Formula Output Format) | Foundation (§3) | DEC-27 (agent build is INFERENCE: needed only for its virtual investment committee seat, DEC-22) |
| 12 | portfolio-manager (agent) | P5 | n/a | game-designer (Question-First Workflow shape only) | Foundation (§3) | DEC-27 (agent build is INFERENCE, same reason as row 11) |
| 13 | Virtual investment committee (design step) | P5 | cio, cro, portfolio-manager, red-team-analyst (seats) | team-combat, the fullest orchestration template (INFERENCE) | 9, 11, 12, 7 | DEC-27, DEC-22 |

Row 13's minutes record and the pilot log close P5 (PLAN.md §8 P5,
outputs list).

**Table 4-2. P6 group 1: market and stock information, plus the roster
completion (DEC-26)**

| Order | Skill or agent | Phase | Owner agent | CCGS donor | Depends on | DEC |
|---|---|---|---|---|---|---|
| 14 | data-steward (agent) | P6 | n/a | economy-designer (canonical registry) | Foundation (§3) | DEC-26 (agent build is INFERENCE placement: needed before its two owned skills, rows 15-16 and 17) |
| 15 | `/coverage-config` (skill) | P6 | data-steward | settings, the single config view/change surface (INFERENCE; no donor named in §9.4) | 14 | DEC-26 unordered (placement below), DEC-15 |
| 16 | `/refresh-facts` (skill) | P6 | data-steward | consistency-check, the fact-registry mechanism (reused; F10) | 14, F10 | DEC-26 unordered (placement below), DEC-35 |
| 17 | `/event-alert` (skill) | P6 | data-steward | consistency-check, the change-detection mechanism (INFERENCE; no donor named in §9.4) | 14 | DEC-26 |
| 18 | market-strategist (agent) | P6 | n/a | systems-designer (Formula Output Format for indicators) | Foundation (§3) | DEC-26 (agent build is INFERENCE: needed for row 19) |
| 19 | `/house-view` (skill) | P6 | market-strategist, red-team-analyst, cio | team-\* skeleton, the bull/bear/synthesis sequence | 18, 7 (red-team-analyst), 9 (cio) | DEC-26, DEC-16 |
| 20 | head-of-research (agent) | P6 | n/a | game-designer (Question-First Workflow shape only) | Foundation (§3) | DEC-09 §6.1 roster completion (INFERENCE placement: no product skill in the 14 blocks on it) |
| 21 | trader (agent) | P6 | n/a | No domain donor; lead-programmer (Implementation Workflow shape only) | Foundation (§3) | DEC-09 §6.1 roster completion (INFERENCE placement, same reason as row 20) |

Rows 20-21 finish the 11-agent W1 roster (PLAN.md §8 P6 task 1;
ORG-BLUEPRINT.md §6.1). Placing them last is INFERENCE: DEC-26 orders
the 14 information-product skills, not the agent roster, and no
product skill's owner is head-of-research or trader.

**Table 4-3. P6 group 2: risk, portfolio, and quality products (DEC-26)**

| Order | Skill or agent | Phase | Owner agent | CCGS donor | Depends on | DEC |
|---|---|---|---|---|---|---|
| 22 | `/risk-report` (skill) | P6 | cro | security-audit, the category-by-category audit pattern (INFERENCE; no donor named in §9.4) | 11 (cro) | DEC-26, DEC-06, DEC-25 (capacity estimates) |
| 23 | `/portfolio-review` (skill) | P6 | portfolio-manager | content-audit, the mandate-vs-executed-portfolio reconciliation donor (INFERENCE; no donor named in §9.4) | 12 (portfolio-manager) | DEC-26, DEC-25 (capacity estimates) |
| 24 | `/call-review` (skill) | P6 | cio, chief-of-staff | post-mortem and playtest-report | 10 (cio), 2 (chief-of-staff); needs at least one closed call, satisfied by the P5 pilot | DEC-26, DEC-24 |

**Table 4-4. P6: the four DEC-26 unordered skills (placement proposal, INFERENCE)**

| Order | Skill | Phase | Owner agent | CCGS donor | Depends on | DEC |
|---|---|---|---|---|---|---|
| 15 | `/coverage-config` | P6 | data-steward | settings (INFERENCE) | data-steward (row 14) | DEC-26 unordered; DEC-15 |
| 16 | `/refresh-facts` | P6 | data-steward | consistency-check (reused, F10) | data-steward (row 14), F10 | DEC-26 unordered; DEC-35 |
| 25 | `/weekly-report` | P6 | chief-of-staff | changelog, the provenance-checked summary generator (INFERENCE) | Group 1 (14-21) and group 2 (22) | DEC-26 unordered; DEC-14 |
| 26 | `/ask` | P6 | chief-of-staff | help, the routing mechanism (INFERENCE) | Every other W1 product (1-25), so it has sources to route to | DEC-26 unordered; DEC-14 |

Reasoning for each placement (INFERENCE; see the founder decision
item in §6, ID P2-B-01):

- **`/coverage-config` before the rest of group 1** (rows 15, ahead of
  17-19). It sets the coverage universe, sector clusters, and data
  sources (ORG-BLUEPRINT.md §11A). `/idea-screen`, `/event-alert`, and
  `/house-view` all read that universe. The brief's own example gives
  this same placement.
- **`/refresh-facts` next to `/coverage-config`** (row 16). Both skills
  belong to data-steward and both need only the fact registry (F10),
  which the foundation phase already transplants. Neither depends on
  another information product.
- **`/weekly-report` after group 2, not only after group 1.** The
  brief's example places it "after group 1, because it compiles their
  outputs." ORG-BLUEPRINT.md §11A's own product table gives
  `/weekly-report`'s output as "House view, sector reviews, pick-list
  changes, **risk review**." The risk-review component is `/risk-report`'s
  output (group 2, row 22), so `/weekly-report` cannot compile a
  complete week until group 2 also exists. This document departs from
  the brief's illustrative placement for that reason.
- **`/ask` last.** It routes a question to the right agent's answer,
  with sources (ORG-BLUEPRINT.md §11A). It has the most value once
  every other product exists to route to.

## 5. The 16 DEFERRED transplant rows (TRANSPLANT-MANIFEST.md §10.3)

TRANSPLANT-MANIFEST.md §10.3 leaves 16 rows DEFERRED. Table 5-1 lists
every row and proposes a resolution. Rows are grouped for the founder
decisions in §6.

**Table 5-1. DEFERRED rows and proposed resolution**

| Group | § | Component | Manifest wave/trigger | Proposed resolution (INFERENCE) | Reason |
|---|---|---|---|---|---|
| 1 | 5.5 | `.claude/rules/ui-code.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | The W1 HTML dashboard (DEC-28) is the only UI surface W1 builds; this is the only coding-rule donor for it in the manifest. |
| 1 | 5.6 | `.claude/docs/templates/accessibility-requirements.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Same dashboard; a one-user dashboard still benefits from a baseline accessibility check (AAA-QUALITY-BAR.md applies AAA-01..14 to every artifact, DEC-34). |
| 1 | 5.6 | `.claude/docs/templates/interaction-pattern-library.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Same dashboard; gives the dashboard's navigation and control patterns a donor instead of an ad hoc build. |
| 1 | 5.6 | `.claude/docs/templates/ux-spec.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Same dashboard; the dashboard needs a written spec before P6 builds it. |
| 1 | 5.6 | `.claude/docs/templates/guidance/interaction-pattern-library-guide-navigation-feedback.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Sub-guide of the interaction-pattern-library row above; same donor decision. |
| 1 | 5.6 | `.claude/docs/templates/guidance/interaction-pattern-library-guide-standard-controls.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Sub-guide of the interaction-pattern-library row above; same donor decision. |
| 1 | 5.6 | `.claude/docs/templates/guidance/interaction-pattern-library-guide.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Sub-guide of the interaction-pattern-library row above; same donor decision. |
| 1 | 5.6 | `.claude/docs/templates/guidance/ux-spec-guide.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | Sub-guide of the ux-spec row above; same donor decision. |
| 1 | 5.11 | `.claude/skills/ux-design/SKILL.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | The dashboard's spec-authoring skill; matches the templates above. |
| 1 | 5.11 | `.claude/skills/ux-review/SKILL.md` | W2; P2 may use for the W1 dashboard | Use in W1, adapted | The dashboard's review gate; matches the templates above. |
| 2 | 5.6 | `.claude/docs/templates/player-journey.md` | W2 | Wait for W2 | Investor-journey document; W1 has one user, the founder, not an investor journey (DEC-13). |
| 2 | 5.6 | `.claude/docs/templates/economy-model.md` | W2 | Wait for W2 | Fee and waterfall document; no fund exists to fee until W2 fund setup (DEC-13). |
| 2 | 5.9 | `.claude/skills/patch-notes/SKILL.md` | W2 | Wait for W2 | Investor-update drafting; no investors exist until W2 (DEC-13, DEC-08). |
| 2 | 5.11 | `.claude/skills/asset-spec/SKILL.md` | W2 | Wait for W2 | Investor-collateral spec donor; no investor-facing collateral exists until W2. |
| 3 | 5.6 | `.claude/docs/templates/prototype-report.md` | W1 (P2 decides) | Use in W1, adapted | `/call-review`'s per-call verdict (played out / thesis broken / still open) maps to the PROCEED/PIVOT/KILL memo shape (DEC-24). |
| 4 | 5.11 | `.claude/skills/setup-engine/SKILL.md` | W2 | Wait for W2 | Donor for custodian, administrator, or jurisdiction selection; none of these exist to select until fund setup starts (W2). |

## 6. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-B-01 | Where do `/coverage-config`, `/refresh-facts`, `/weekly-report`, and `/ask` go in the P6 build order, since DEC-26 does not order them? | A: as Table 4-4 proposes (coverage-config and refresh-facts early with data-steward; weekly-report after group 2; ask last). B: build all four immediately after group 1, before group 2. C: build all four last, after group 2. D: founder sets a different order. | A, with the reason each row states in §4. `/coverage-config` blocks the rest of group 1's data use; `/weekly-report` needs group 2's risk-review output; `/ask` benefits most once every product exists. Source: PLAN.md §8 P6 task 2; ORG-BLUEPRINT.md §11A. |
| P2-B-02 | Does the W1 HTML dashboard (DEC-28) reuse the 10 UI/UX DEFERRED rows in Table 5-1 group 1 now, or wait for W2? | A: reuse all 10, adapted, before P6 builds the dashboard. B: reuse only `ui-code.md` and `interaction-pattern-library.md` (the two coding-pattern donors); leave the rest for W2. C: wait for W2 entirely; build the dashboard with no donor. D: founder picks a different subset. | A. TRANSPLANT-MANIFEST.md §10.3 marks every row "P2 may use it for the W1 dashboard," and the dashboard is the only UI artifact W1 builds; a partial reuse (B) still leaves the dashboard's accessibility and spec steps ad hoc. Source: TRANSPLANT-MANIFEST.md §10.3 rows (Table 5-1 group 1). |
| P2-B-03 | Do the 4 investor-facing DEFERRED rows in Table 5-1 group 2 (`player-journey.md`, `economy-model.md`, `patch-notes/SKILL.md`, `asset-spec/SKILL.md`) wait for W2? | A: wait for W2 (as proposed). B: build `economy-model.md` early, in P6, to help the founder plan fee terms before fund setup. C: wait for W2 for all four, but flag `economy-model.md` as a P8 first task. D: founder sets a different schedule. | A. DEC-13 moved every investor-facing and fee/waterfall document to W2; none of the four has a W1 use. Source: TRANSPLANT-MANIFEST.md §10.3; PLAN.md DEC-13. |
| P2-B-04 | Does `/call-review` reuse `prototype-report.md`'s PROCEED/PIVOT/KILL memo shape (Table 5-1 group 3)? | A: reuse it, adapted to a call's outcome (played out / thesis broken / still open). B: design a fresh call-outcome format with no donor. C: reuse it only for the model-portfolio side of `/call-review`, not the per-call side. D: founder picks a different shape. | A. TRANSPLANT-MANIFEST.md §10.3 already flags this row "W1 (P2 decides)"; the three-way verdict shape is the closest existing donor to a call's pass/fail/open judgment. Source: TRANSPLANT-MANIFEST.md §10.3 row `prototype-report.md`; PLAN.md DEC-24. |
| P2-B-05 | Does `setup-engine/SKILL.md` (Table 5-1 group 4) wait for W2? | A: wait for W2 (as proposed). B: build early, in P6, as a placeholder for the eventual custodian/administrator/jurisdiction choice. | A. No custodian, administrator, or second jurisdiction exists to select until the founder starts fund setup (W2 trigger, DEC-13). Source: TRANSPLANT-MANIFEST.md §10.3 row `setup-engine/SKILL.md`. |

## Founder decisions recorded (2026-09-25)

The founder answered the items above. HFT-P2-00 §4 is the register; §4A states the consequences.

| ID | Answer |
|---|---|
| P2-B-01 | A: the proposed order |
| P2-B-02 | A: reuse all 10 for the W1 dashboard |
| P2-B-03 | A: wait for W2 |
| P2-B-04 | A: reuse the memo shape |
| P2-B-05 | A: wait for W2 |

## 7. Traceability

| P2 task / DEC-NN | Covered in |
|---|---|
| P2 task 5 (set the skill build priority) | §4, §5 |
| DEC-26 (Q22 first products) | §4 Table 4-2, 4-3, 4-4 |
| DEC-27 (Q23 first milestone) | §4 Table 4-1 |
| DEC-09, DEC-13 (mission reset, wave split) | §3, §4 Table 4-2 rows 20-21 |
| DEC-14 (delivery cadence) | §4 Table 4-1 row 2, Table 4-4 |
| DEC-15 (coverage rules) | §4 Table 4-2 row 15 |
| DEC-16 (bull/bear/synthesis) | §4 Table 4-1 rows 8, 10, 19 |
| DEC-22 (virtual investment committee) | §4 Table 4-1 row 13 |
| DEC-23 (stock-pitch depth) | §4 Table 4-1 row 6 |
| DEC-24 (call quality) | §4 Table 4-3 row 24; §5 Table 5-1 group 3; §6 P2-B-04 |
| DEC-25 (capacity estimates) | §4 Table 4-3 rows 22-23 |
| DEC-28 (delivery surface / dashboard) | §5 Table 5-1 group 1; §6 P2-B-02 |
| DEC-29 (Q25 = B, no code pipeline) | §3 Table 3-1 row F8 |
| DEC-34 (AAA scope) | §5 Table 5-1 group 1 |
| DEC-35 (fact freshness, manual) | §4 Table 4-1 row 16, Table 4-4 |
| §4 and §9.3 (foundation transplants) | §3 |
| §9.4 Table 9-1 (W1 skill donors) | §4 (donor column) |
| §10.3 (16 DEFERRED rows) | §5, §6 |
