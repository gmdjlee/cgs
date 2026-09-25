# project.yaml config schema

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-04 |
| Title | project.yaml config schema |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | `/home/user/cgs/project.yaml`; `docs/hedge-fund-transition/TRANSPLANT-MANIFEST.md` §5.4, §10; `docs/hedge-fund-transition/PLAN.md` §6, §7, §8; `docs/hedge-fund-transition/ORG-BLUEPRINT.md` §6, §7, §10; `docs/hedge-fund-transition/evidence/design-addendum-01.md` §5; `.claude/docs/effects-map.md`; `.claude/hooks/yaml-helper.sh`; `.claude/docs/automation-modes.md`; `.claude/docs/model-tiers.md`; `.claude/docs/config-resolution.md`; `docs/hedge-fund-transition/QUESTIONS.md`; `/tmp/.../scratchpad/decisions.md` (DEC-01 to DEC-38) |
| Writing standard | ASD-STE100 |

## 1. Scope

This document defines the `project.yaml` schema for the new hedge-fund
repository (DEC-04). It covers PLAN.md §8, P2, task 4: keep every §5.4 key
with verdict TAKE or TAKE-MODIFY, add the new keys the task names, resolve
the `modes.automation` gap (DEC-36), and set the `project.stage` default.
The companion draft file is
[`project.draft.yaml`](project.draft.yaml).

Out of scope: the full `project.stage` enum (HFT-P2-02 owns it), the
notification-channel and price-provider choices (P2 tasks 7 and 8), the W2
and W3 agent-to-tier map (HFT-P2-01, P2 task 9), and the evidence-type
taxonomy redesign for `testing.strict.*`.

## 2. Kept CCGS keys (§5.4 TAKE)

These keys keep their CCGS shape and meaning unchanged
(TRANSPLANT-MANIFEST.md §5.4).

| Key | Type | Allowed values | Default | Owner | Wave | DEC | CCGS reader |
|---|---|---|---|---|---|---|---|
| `schema_version` | integer | any | `1` | Advisor | All | n/a | File-metadata check only, not a behavior reader: `.claude/hooks/yaml-helper.sh:582-590` (exempt from the local-scope warning); written by `.claude/scripts/migrate-v1-config.sh:569`. |
| `framework.version` / `framework.last_upgraded` | string / date | any | `1.1.1` / `2026-09-24` | Advisor | All | n/a | No behavior reader found (`grep -rn "framework\.version" .claude/hooks .claude/scripts` returns nothing); file-metadata only, per `config-resolution.md:156-158`. |
| `modes.rigor` | enum | `minimal`, `standard`, `full` | `standard` (Advisor proposal; CCGS default `minimal`; see P2-S-04) | Founder | All | n/a | Read at `.claude/hooks/yaml-helper.sh:999,1014-1054`; fronts `modes.workflow`, `docs.density`, `qa.level`, `modes.story_granularity`, `modes.review_mode`, `team.size` (`config-resolution.md:160-214`). |
| `workflow_overrides` | map | `system_overrides.<name>: minimal\|standard\|full`, plus 3 booleans | `{}` | Founder / system owner | All | n/a | Read at `.claude/hooks/yaml-helper.sh:1504-1519`. The 3 booleans (`edge_cases`, `tuning_knobs`, `art_bible_strict`) are GDD/engine-specific; their hedge-fund equivalents are not defined here (GAP, out of scope for this task). |
| `modes.story_granularity` | enum | `coarse`, `balanced`, `fine` | fronted by `modes.rigor` | Founder | All | n/a | Read at `.claude/hooks/yaml-helper.sh:1015-1017` (rigor expansion), enum-checked at line 465. No direct existing reader beyond the expansion table itself was found outside `yaml-helper.sh`. |
| `docs.density` | enum | `terse`, `balanced`, `thorough` | fronted by `modes.rigor` | Founder | All | n/a | Same mechanism as the row above; enum at `.claude/hooks/yaml-helper.sh:466`. |
| `performance.enforce` | enum | `warn`, `block`, `off` | `warn` | cro (future reuse) | All | n/a | Read at `.claude/hooks/yaml-helper.sh:469,1451-1457` (the one non-rigor-fronted key with a central default). Kept for a future risk-limit-breach reuse (TRANSPLANT-MANIFEST.md §5.4). |
| `features.session_state` | enum | `on`, `off` | `on` | Advisor | All | n/a | Read at `.claude/hooks/yaml-helper.sh:665-676` (`session_state_enabled()`), used by `log-agent.sh` on every subagent spawn. |
| `cadence.sprint_length` / `cadence.milestone_length` | string (duration) | any | `1w` / `4w` (INFERENCE placeholder) | Advisor | All | n/a | No reader found (`grep -rn "cadence\." .claude/hooks .claude/skills` returns nothing). Reusable later for IC or board meeting cadence once a skill reads it (TRANSPLANT-MANIFEST.md §5.4). New reader needed if used. |
| `features.token_budget_warn_at` | float (0-1) | any | `0.7` | Advisor | All | n/a | Documented but **not wired**: `.claude/hooks/yaml-helper.sh:528` lists the key; `pre-compact.sh`, `session-start.sh`, and `statusline.sh` do not read it yet (TRANSPLANT-MANIFEST.md §5.4). New reader needed: a P3 task. |

## 3. Kept-and-modified CCGS keys (§5.4 TAKE-MODIFY)

| Key | Type | Allowed values | Default | Owner | Wave | DEC | CCGS reader | Required change (§5.4) |
|---|---|---|---|---|---|---|---|---|
| `modes.review_mode` | enum | `full`, `lean`, `solo` | fronted by `modes.rigor` | Founder | All | DEC-18 (fixed-seat exception) | `.claude/hooks/yaml-helper.sh:461,970-976`. | Rename the 3 values for a control panel; flag `solo` for restriction on control gates. **Not applied in this draft**: no concrete new names were given (INFERENCE gap). `cro`/`cco` stay active at every value of this key regardless (DEC-18; `controls.fixed_seats` below is the actual mechanism). |
| `modes.automation` | enum | `collaborative`, `guided`, `autonomous` (CCGS); see §6 below | `collaborative` (CCGS) / `draft_free` (proposed) | Founder | All | DEC-36 | `.claude/hooks/yaml-helper.sh:464,998`; ~30 `SKILL.md` files read it directly (see §6). | No CCGS value matches DEC-36. See §6 for the full analysis and the founder decision item. |
| `modes.automation_always_ask` | array of string | see §6.2 | `[scope_changes, file_deletions, schema_changes]` (CCGS) | Founder | All | DEC-36 | `.claude/hooks/yaml-helper.sh:890-892,894-910` (`is_always_ask_category`); recognized-category table at `automation-modes.md:132-149`. | Keep the default list; add hedge-fund categories. See §6.2. |
| `modes.workflow` | enum | `minimal`, `standard`, `full` | fronted by `modes.rigor` | Founder | All | n/a | `.claude/hooks/yaml-helper.sh:1011-1017`; drives ~5 behaviors (`effects-map.md:527-534`). | Keep the doc-section-count dial; reuse the 3 tiers for IC-memo completeness (unchanged in this draft). |
| `qa.level` | enum | `minimal`, `standard`, `full` | fronted by `modes.rigor` | Founder | All | n/a | Read by 10 `SKILL.md` files (`grep -rl "qa\.level" .claude/skills/*/SKILL.md`). | §5.4 recommends renaming the key to a review/validation level. **Not renamed in this draft** (INFERENCE). A key rename is a P3+ code change, not a P2 schema decision. The key keeps its CCGS name and path (P-06). |
| `team.size` | enum | `individual`, `small`, `studio` | fronted by `modes.rigor` | Founder | All | n/a | `.claude/hooks/yaml-helper.sh:468,1016-1017`. | Rename the enum values only (cosmetic); no cro/cco seat scaling. **Values kept as-is in this draft**: §5.4 names no concrete replacement strings (INFERENCE gap). |
| `project.stage` | string | `pre-setup`, `s1`-`s8`, `g1`-`g3` (see §5; HFT-P2-02) | `pre-setup` (proposed) | gate-check only | All | DEC-21 | `.claude/hooks/yaml-helper.sh:473,1057-1060,1149-1177` (single authoritative value, dual legacy-mirror at `production/stage.txt`, gate-check-only write). | Replace the 7 CCGS stage names with the fund's lifecycle stages. See §5. |
| `testing.strict.{logic,integration,visual,ui,config}` | map of boolean | `true`, `false` | unset (per-skill default) | Founder / cro | All | n/a | `.claude/hooks/yaml-helper.sh:474-478,500-504` (enum-checked, no central default by design; `config-resolution.md:216-221`). | Redesign the 5 type names into a hedge-fund evidence taxonomy. **Out of scope for HFT-P2-04.** Left as an empty map in the draft. A later task owns the taxonomy. |
| `strict_gate_checks` | boolean | `true`, `false` | `true` | n/a | All | DEC-17 | No reader found in `.claude/hooks/yaml-helper.sh` (`grep -n "strict_gate_checks"` returns nothing). | Keep the key. Do not rely on it: DEC-17 uses a cro verdict plus a recorded approval instead. A control decision with no receipt reads NOT ASSESSED whatever this key holds. |

## 4. New keys (PLAN.md §8, P2 task 4)

| Key | Type | Allowed values | Default | Owner | Wave | DEC | Reader |
|---|---|---|---|---|---|---|---|
| `archetype` | enum | `single_manager_fundamental`, `quant`, `multi_manager_platform`, `macro`, `hybrid` | `single_manager_fundamental` | Founder | All | DEC-05 | New reader needed. Routes specialist/conditional agent activation, replacing `engine.name`'s routing role (TRANSPLANT-MANIFEST.md §5.4; ORG-BLUEPRINT.md §7). |
| `strategy` | enum | `long_biased` (INFERENCE: other values not yet named) | `long_biased` | Founder | All | DEC-06 | New reader needed. Turns on the downside-defense risk output (bear-market stress, net exposure) in `/risk-report`. |
| `jurisdiction` | array of string | regulator codes, e.g. `KR-FSC`, `KY-CIMA` | `[KR-FSC]` | Founder | W1 (KR), W2+ (Cayman) | DEC-07 | New reader needed. A list, because Cayman joins later (TRANSPLANT-MANIFEST.md §5.4). |
| `risk.limits_config` | string (path) | any repo-relative path | `config/risk/limits.yaml` | cro drafts, founder approves | W1 | DEC-19 | New reader needed. Points to the file holding the leverage, VaR, concentration, and daily-loss limits. **No numbers live in `project.yaml`.** This refines TRANSPLANT-MANIFEST.md §5.4's `risk.leverage_cap_pct_nav` etc. leaf-key suggestion into a path. PLAN.md P-05 keeps limits data-driven, never in code or prose (DEC-19). |
| `risk.registry` | string (path) | any repo-relative path | `config/risk/limits-registry.yaml` | cro | W1 | DEC-19 | New reader needed. Stores each limit with an `as_of` date and an effective date (PLAN.md:323-324, "Registry"). |
| `regulatory_calendar` | string (path) | any repo-relative path | `config/regulatory/calendar.yaml` | cco | W2 | n/a (task item; DEC-13 sets the W2 trigger) | New reader needed. Filing deadlines, IC/board cadence, audit windows (ORG-BLUEPRINT.md §10). `cadence.sprint_length` above supplies the structural shape only (TRANSPLANT-MANIFEST.md §5.4). |
| `coverage.markets` | array of string | `KR`, `US` | `[KR]` | data-steward | W1 (KR), later (US) | DEC-15 | New reader needed (`/coverage-config` skill target). |
| `coverage.sector_taxonomy` | enum | `KRX`, `GICS` | `KRX` | data-steward | W1 (KRX), later (GICS) | DEC-15 | New reader needed. Becomes GICS when US equities join. |
| `coverage.clusters` | array of string | any (INFERENCE, addendum §5) | the 6 clusters listed in `project.draft.yaml` | data-steward | W1 | design-addendum-01.md §5 (INFERENCE, "for the founder to confirm") | New reader needed. Config data, changeable without code (design-addendum-01.md §5). |
| `data_sources.opendart.{adapter,enabled}` | string / boolean | `opendart` / `true`, `false` | `opendart` / `true` | data-steward | W1 | DEC-31 | New reader needed. Disclosures and financials. |
| `data_sources.price.{adapter,enabled}` | string or null / boolean | any / `true`, `false` | `null` / `false` | data-steward | W1 | DEC-31 | New reader needed. **Placeholder**, pending founder decision `P2-D-03` in `P2-07-CHANNEL-AND-DATA.md` (see §7). |
| `data_sources.web_search.{adapter,enabled}` | string / boolean | `web_search` / `true`, `false` | `web_search` / `true` | data-steward | W1 | DEC-31 | New reader needed. Regulation, news, macro context. |
| `delivery.dashboard.{enabled,path}` | boolean / string (path) | `true`, `false` / any repo-relative path | `true` / `production/dashboard` | chief-of-staff | W1 | DEC-28 | New reader needed. |
| `delivery.notification.{channel,enabled}` | string or null / boolean | any / `true`, `false` | `null` / `false` | chief-of-staff | W1 | DEC-28 | New reader needed. **Placeholder**, pending founder decision `P2-D-01` in `P2-07-CHANNEL-AND-DATA.md` (see §7). |
| `controls.four_eyes` | array of string | `trade_execution`, `valuation`, `nav_calculation` | all 3 | cco | W2 | DEC-17 | New reader needed. Named `controls.four_eyes` per PLAN.md §8 task 4; the evidence citation is TRANSPLANT-MANIFEST.md §5.4's `controls.four_eyes_required_for` row (same concept, PLAN.md's shorter name is used here). |
| `controls.approval_required_for` | array of string | `risk_limit_change`, `final_status_change`, `commit` | all 3 | Founder | All | DEC-17, DEC-36 | New reader needed. The decision types that need a recorded founder-approval receipt (§6.1). |
| `controls.fixed_seats` | array of string | `cro`, `cco` | `[cro, cco]` | n/a | cro from W1, cco from W2 | DEC-18 | New reader needed. Never skipped, whatever `modes.review_mode` / `modes.workflow` / `team.size` say. |
| `review.depth_by_output` | map of string to enum | keys: any output name; values: `full`, `lean` | `{stock_call: full, house_view: full, limit: full, daily_briefing: lean}` | cio | W1 | DEC-20 | New reader needed. |
| `agents.model_tiers` | map of string to enum | `opus`, `sonnet`, `haiku` | W1 rows per DEC-38 (see `project.draft.yaml`) | Advisor | W1 now; W2/W3 pending | DEC-38 | New reader needed. W2/W3 rows come from HFT-P2-01 (PLAN.md §8 P2 task 9). The judgment exception (a Tier-3 agent writing a judgment output uses `sonnet`) is a rule for the reader to apply, not a config value. See `.claude/docs/model-tiers.md` for the CCGS statement of the same rule (unverified for agents, `model-tiers.md:18-21`). |
| `data.private_dir` | string (path) | any repo-relative path | `data/private` | Founder | W1 | DEC-32 | New reader needed. Must be added to `.gitignore` (P3 task). No classification scheme in W1. |
| `language.technical` | string | `en-STE100` | `en-STE100` | Advisor | All | DEC-33 | New reader needed. Agents, skills, rules, procedures. |
| `language.products` | string | `ko` | `ko` | Advisor | All | DEC-33 | New reader needed. Briefings, reports, alerts, the dashboard, regulatory and investor documents. |
| `language.responses` | string | `ko` | `ko` | Advisor | All | DEC-33 | New reader needed. Responses to the user. |

## 5. `project.stage` default

DEC-21 keeps `project.stage` a single scalar, combining the S1-S8 setup
stages and the G1-G3 growth stages (PLAN.md:296-302; ORG-BLUEPRINT.md §11).
HFT-P2-02 (the lifecycle catalog, PLAN.md §8 P2 task 2) proposes the full
enum, all lower-kebab: `pre-setup`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`,
`s7`, `s8`, `g1`, `g2`, `g3` (`P2-02-LIFECYCLE.md` §3, §7).

This schema adopts `pre-setup` as the `project.stage` default. Whether
`pre-setup` becomes a real, gated stage at all is **pending founder
decision P2-L-01** in `P2-02-LIFECYCLE.md` §10, not settled by this
document. HFT-P2-02 owns the enum; this document only consumes it.

## 6. `modes.automation` and DEC-36

DEC-36: agents write drafts with no approval prompt; a change to final
status and every commit need a founder approval. No CCGS `modes.automation`
value matches this exactly (`automation-modes.md:66-94`; DEC-36 itself
names the gap and assigns P2 to close it).

**Why no CCGS value fits.** The 3 CCGS modes vary how much the AI asks
*before acting* on a decision (`collaborative` asks always; `guided` asks
for major decisions only; `autonomous` asks almost never). DEC-36 varies
*when an approval gate applies*, not how often the AI asks: every draft is
free, and only 2 events need a receipt (a final-status change, a commit).
These are 2 different axes: a decision-frequency axis (CCGS) and an
outcome-gate axis (DEC-36). Stretching an existing value to cover both
risks conflating them in the same enum.

### 6.1 Two options

| Option | Mechanism | Upstream drift (PLAN.md R-08, P-06) | Skills touched | Exemption list (automation-modes.md:163-175) |
|---|---|---|---|---|
| (a) Change the meaning of `guided` | Redefine `guided` so it means "free drafts, approval before final status or a commit." This replaces its current major/minor-decision behavior. | High risk. `_yaml_helper_enums` (`.claude/hooks/yaml-helper.sh:460-483`) and `automation-modes.md` are foundation files. P-06 keeps them at identical paths for upstream merges (R-08: `UPGRADING.md` strategy A2 or B). An upstream CCGS change to `guided`'s meaning would silently change hedge-fund runtime behavior on the next merge. Local prose describing the old meaning would then misdescribe what runs. | ~30 `SKILL.md` files read `modes.automation` directly (`grep -rl "modes\.automation\b" .claude/skills/` = 30 files); `automation-modes.md` claims ~44 skills follow the pattern in total. Each of the 30 needs its `guided` branch reworded; no enum-cardinality change. | The 4 exempted skills (`hotfix`, `gate-check`, `day-one-patch`, `setup-engine`) stay collaborative regardless of the mode value. Unaffected either way. |
| (b) Add a new value, e.g. `draft_free` | Add a 4th enum value. `guided`'s current major/minor meaning is untouched. | Low risk. The 3 CCGS values and their documented meanings stay mergeable from upstream unchanged; only a local addition is layered on top. | Same ~30 files. Each needs a 4th branch added, not a reworded branch, plus the enum list at `yaml-helper.sh:464` extended. More total edits than (a), but each edit is additive, not a redefinition of shared vocabulary. | Same 4 skills, unaffected either way. |

### 6.2 Recommendation

**Recommend option (b): add a new value (`draft_free` in this draft).**
Reason: DEC-36's approval axis (draft vs. final status/commit) is
orthogonal to CCGS's decision-frequency axis (major vs. minor) that
`guided` already encodes. Overloading `guided` makes the same word mean two
different things depending on whether the reader has the CCGS or the
hedge-fund semantics in mind. This is exactly the ambiguity P-06 and R-08 exist to
avoid at a merge boundary. Source: PLAN.md P-06 (PLAN.md:371-374), R-08
(PLAN.md:813), DEC-36.

This is listed as founder decision **P2-S-01** below, because DEC-36
explicitly leaves the choice to P2 rather than settling it.

### 6.3 `modes.automation_always_ask` categories

| Category | Recognized by the helper today? | Evidence |
|---|---|---|
| `scope_changes` | Yes: CCGS default | `automation-modes.md:130,142-149`; `yaml-helper.sh:890-892` |
| `file_deletions` | Yes: CCGS default | Same as above |
| `schema_changes` | Yes: CCGS default | Same as above |
| `risk_limit_changes` | **No. A new category.** `is_always_ask_category` only checks membership in the configured list (`yaml-helper.sh:894-910`), so setting this string in `modes.automation_always_ask` works mechanically. No skill call-site checks for it yet. | TRANSPLANT-MANIFEST.md §5.4 `modes.automation_always_ask` row. |
| `trade_related_actions` | **No. A new category.** Same mechanism note as above. | Same manifest row. |
| `client_data_access` | **No. A new category.** Same mechanism note as above. | Same manifest row. |

`is_always_ask_category` is generic: it reads whatever list is configured
and checks membership (`yaml-helper.sh:894-910`), so the 3 new categories
are legal to configure today. What is missing is skill code that calls
`is_always_ask_category("risk_limit_changes")` (etc.) at the right decision
points. This is a P3+ implementation task, not a config-schema gap.

## 7. The price-provider and notification-channel placeholders

This task's instructions name HFT-P2-07 as the document that fills the
price-provider placeholder (DEC-31). PLAN.md §8's own P2 task list numbers
the notification-channel selection as task 7 and the price/data provider
selection as task 8 separately (PLAN.md:472-474), which first read as a
numbering mismatch against a single HFT-P2-07 document.

`P2-07-CHANNEL-AND-DATA.md` resolves this: it is one document, ID
HFT-P2-07, "Notification channel and price data provider," and its own
Scope section states it covers both P2 tasks 7 and 8
(`P2-07-CHANNEL-AND-DATA.md` §1). No numbering mismatch remains.

`data_sources.price` and `delivery.notification.channel` stay placeholders
in `project.draft.yaml`, because HFT-P2-07 records its selections as its
own founder decisions (`P2-D-01` for the channel, `P2-D-03` for the
provider), not yet settled facts this schema can adopt as a default.

## Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-S-01 | How should `modes.automation` express DEC-36 (free drafts, approval before final status or a commit)? | (A) Redefine `guided` to mean the DEC-36 behavior. (B) Add a new enum value (`draft_free` in this draft) alongside `collaborative`/`guided`/`autonomous`. | (B), because it does not overload `guided`'s existing CCGS meaning and keeps the 3 upstream values mergeable without redefinition (P-06, R-08). See §6. |
| P2-S-02 | Should `qa.level` and `modes.review_mode` keep their CCGS enum-value names, or take the new names TRANSPLANT-MANIFEST.md §5.4 recommends? | (A) Keep the CCGS names (as drafted here). (B) Rename now, before P3 implements the reader. (C) Rename later, after the skills that read these keys are rebuilt for the fund. | No recommendation (founder judgment). §5.4 names the change but not the replacement strings, so any choice here is a naming decision, not a mechanism decision. |
| P2-S-03 | Does `strategy` need more enum values now (e.g. `market_neutral`, `short_biased`), or does `long_biased` alone suffice until a second strategy is decided? | (A) `long_biased` only (as drafted). (B) Add the full hedge-fund strategy vocabulary now, unused until selected. | (A), because DEC-06 names only `long_biased` and no other value has a DEC or evidence citation yet. Adding unused values without a citation would be an invented fact. |
| P2-S-04 | Which `modes.rigor` value does the new repository start with? It fronts `modes.workflow`, `docs.density`, `qa.level`, `modes.story_granularity`, `modes.review_mode`, and `team.size` (`yaml-helper.sh:965-1017`). | (A) `minimal`, the CCGS default. (B) `standard`. (C) `full`. (D) `standard` now, and `full` from the W2 trigger (fund setup). | (B), Advisor proposal. DEC-34 requires AAA for every component, so `minimal` is too weak. `full` adds the maximum document and QA load to a one-user W1 build (DEC-37: 40 h per week). DEC-20 already sets full review for judgment outputs through `review.depth_by_output`, independent of this dial. |

Not listed: which document fills the `data_sources.price` and
`delivery.notification.channel` placeholders. `P2-07-CHANNEL-AND-DATA.md`
settles this (§7); its own founder decisions `P2-D-01` and `P2-D-03`
choose the actual values, which are out of scope for this document.

## Traceability

| P2 task / DEC | Section |
|---|---|
| PLAN.md §8 P2 task 4 (schema draft) | §1-§8 (whole document) |
| DEC-04 (new repository) | §1 |
| DEC-05 (archetype) | §4 (`archetype`) |
| DEC-06 (strategy) | §4 (`strategy`) |
| DEC-07 (jurisdiction) | §4 (`jurisdiction`) |
| DEC-13 (W1 information-first scope) | §4 (`regulatory_calendar` wave), §5 |
| DEC-15 (coverage) | §4 (`coverage.*`) |
| DEC-17 (control decisions need a receipt) | §3 (`strict_gate_checks`), §4 (`controls.four_eyes`, `controls.approval_required_for`), §6.1 |
| DEC-18 (fixed control seats) | §3 (`modes.review_mode` note), §4 (`controls.fixed_seats`) |
| DEC-19 (limits in config files) | §4 (`risk.*`) |
| DEC-20 (review depth by output) | §4 (`review.depth_by_output`) |
| DEC-21 (single stage scalar) | §5 |
| DEC-28 (delivery surface) | §4 (`delivery.*`), §7 (channel pending `HFT-P2-07`) |
| DEC-31 (data sources) | §4 (`data_sources.*`), §7 (provider pending `HFT-P2-07`) |
| DEC-32 (confidential data) | §4 (`data.private_dir`) |
| DEC-33 (document language) | §4 (`language.*`) |
| DEC-36 (approval scope) | §6, Founder decisions P2-S-01 |
| DEC-38 (model tiers) | §4 (`agents.model_tiers`) |
| §5.4 kept keys (TAKE) | §2 |
| §5.4 kept-and-modified keys (TAKE-MODIFY) | §3 |
| §10 note 4 (`code_pipeline.*` not added, Q25 = B) | §1 (out of scope, DEC-29) |
