# Control model and virtual investment committee

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-03 |
| Title | Control model and virtual investment committee |
| Version | 1.0 |
| Date | 2026-09-25 |
| Status | Approved by the founder (AR-P2-0001, 2026-09-25) |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | `docs/hedge-fund-transition/PLAN.md` §6.3, §7, §8 (P2), glossary; `docs/hedge-fund-transition/ORG-BLUEPRINT.md` §8, §9, §11.3, §11A; `docs/hedge-fund-transition/AAA-QUALITY-BAR.md` (`control` category, CT1-CT5); `docs/hedge-fund-transition/TRANSPLANT-MANIFEST.md` §5.2; `docs/hedge-fund-transition/evidence/design-spec.md`; `.claude/docs/director-gates/*.md`; `.claude/docs/director-gates.md`; `.claude/docs/effects-map.md`; `.claude/skills/*/SKILL.md`; `.claude/scripts/review-receipts.sh`; `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md` (HF-REF-06) |
| Writing standard | ASD-STE100 |

This document covers P2 work-breakdown tasks 3 (control model) and 10
(virtual investment committee), `docs/hedge-fund-transition/PLAN.md` §8.

---

## 1. Verdict vocabulary

PLAN.md §6.3 sets one vocabulary for every gate in the new organization:
**PASS, CONCERNS, FAIL, NOT ASSESSED** (PLAN.md:306). Use the precedence
below to combine verdicts. Read it top to bottom; the first rule that
applies wins.

| Precedence | Rule | Source |
|---|---|---|
| 1 | FAIL beats CONCERNS. | PLAN.md:307 |
| 2 | CONCERNS beats NOT ASSESSED. | PLAN.md:307 |
| 3 | NOT ASSESSED beats PASS. | PLAN.md:307 |

A missing input never reads as PASS. It reads as NOT ASSESSED (P-09,
PLAN.md:389).

### 1.1 Why a mapping is needed

F-07 records that the 28 `.claude/docs/director-gates/*.md` files use 9
different verdict vocabularies, though the index file
`.claude/docs/director-gates.md:123-135` documents only 3
(`docs/hedge-fund-transition/evidence/design-spec.md:37`). SB-18 names
the resulting defect: the gate-verdict parser is keyed to the single
word "REJECT" and misses the other 8 vocabularies
(`docs/hedge-fund-transition/evidence/design-spec.md:50`). Every one of
these vocabularies must map onto PASS / CONCERNS / FAIL / NOT ASSESSED
before P4 rewrites the gate files (PLAN.md, P4 task 1).

### 1.2 Director-gate vocabularies (the 9 that F-07 counts)

| # | Source vocabulary | Files (file:line for the `**Verdicts**:` line) | Maps to |
|---|---|---|---|
| 1 | APPROVE / CONCERNS / REJECT | `.claude/docs/director-gates/ad-art-bible.md:26`, `ad-visual.md:23`, `cd-gdd-align.md:23`, `cd-narrative.md:24`, `cd-pillars.md:24`, `cd-playtest.md:23`, `cd-systems.md:27`, `lp-code-review.md:23`, `nd-consistency.md:24`, `td-adr.md:23`, `td-architecture.md:24`, `td-change-impact.md:25`, `td-engine-risk.md:22`, `td-manifest.md:26`, `td-system-boundary.md:31` | APPROVE -> PASS; CONCERNS -> CONCERNS; REJECT -> FAIL |
| 2 | READY / CONCERNS / NOT READY | `.claude/docs/director-gates/ad-phase-gate.md:26`, `cd-phase-gate.md:21`, `pr-phase-gate.md:22`, `td-phase-gate.md:22` | READY -> PASS; CONCERNS -> CONCERNS; NOT READY -> FAIL |
| 3 | CONCEPTS / STRONG / CONCERNS | `.claude/docs/director-gates/ad-concept-visual.md:25` | CONCEPTS -> CONCERNS (multiple valid options is not a pass); STRONG -> PASS; CONCERNS -> CONCERNS. GAP: this gate has no fail-equivalent tier (F-07); a hedge-fund gate must add one, since NOT ASSESSED and FAIL both need a reachable state (P-09). |
| 4 | FEASIBLE / CONCERNS / INFEASIBLE | `.claude/docs/director-gates/lp-feasibility.md:23` | FEASIBLE -> PASS; CONCERNS -> CONCERNS; INFEASIBLE -> FAIL |
| 5 | REALISTIC / CONCERNS / UNREALISTIC | `.claude/docs/director-gates/pr-epic.md:30`, `pr-sprint.md:24` | REALISTIC -> PASS; CONCERNS -> CONCERNS; UNREALISTIC -> FAIL |
| 6 | ON TRACK / AT RISK / OFF TRACK | `.claude/docs/director-gates/pr-milestone.md:24` | ON TRACK -> PASS; AT RISK -> CONCERNS; OFF TRACK -> FAIL |
| 7 | REALISTIC / OPTIMISTIC / UNREALISTIC | `.claude/docs/director-gates/pr-scope.md:25` | REALISTIC -> PASS; OPTIMISTIC -> CONCERNS; UNREALISTIC -> FAIL |
| 8 | ADEQUATE / GAPS / INADEQUATE | `.claude/docs/director-gates/ql-story-ready.md:27`, `ql-test-coverage.md:23` | ADEQUATE -> PASS; GAPS -> CONCERNS; INADEQUATE -> FAIL |
| 9 | VIABLE / CONCERNS / HIGH RISK | `.claude/docs/director-gates/td-feasibility.md:24` | VIABLE -> PASS; CONCERNS -> CONCERNS; HIGH RISK -> FAIL |

None of the 9 has a NOT ASSESSED tier today. Every hedge-fund gate built
from these donors in P4 must add one, so a missing input has somewhere
to read instead of defaulting to the closest PASS-like word (P-09,
CT2).

### 1.3 Skill-level vocabularies (supplementary; outside the F-07 count)

`.claude/skills/*/SKILL.md` files define their own verdict sets for
whole review skills, separately from the director-gates the skills
call. These are additional evidence of the same problem (P-09), found
by grepping `.claude/skills/*/SKILL.md`.

| Source vocabulary | File:line | Maps to |
|---|---|---|
| NOT ASSESSED / APPROVED / APPROVED WITH SUGGESTIONS / CHANGES REQUIRED / MAJOR REVISION | `.claude/skills/code-review/SKILL.md:232`, `:242` | NOT ASSESSED -> NOT ASSESSED; APPROVED -> PASS; APPROVED WITH SUGGESTIONS -> CONCERNS; CHANGES REQUIRED / MAJOR REVISION -> FAIL |
| APPROVED / NOT ASSESSED / NEEDS REVISION / MAJOR REVISION NEEDED | `.claude/skills/ux-review/SKILL.md:3`, `:259` | APPROVED -> PASS; NEEDS REVISION -> CONCERNS; MAJOR REVISION NEEDED -> FAIL; NOT ASSESSED -> NOT ASSESSED |
| APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED / NOT ASSESSED | `.claude/skills/design-review/SKILL.md:294` | Same mapping as the row above |
| READY / NEEDS WORK / BLOCKED / NOT ASSESSED | `.claude/skills/story-readiness/SKILL.md:3` | READY -> PASS; NEEDS WORK -> CONCERNS; BLOCKED -> FAIL; NOT ASSESSED -> NOT ASSESSED |
| ADEQUATE / INCOMPLETE / MISSING / NOT ASSESSED | `.claude/skills/test-evidence-review/SKILL.md:3`, `:249` | ADEQUATE -> PASS; INCOMPLETE -> CONCERNS; MISSING -> FAIL; NOT ASSESSED -> NOT ASSESSED |
| NOT ASSESSED / APPROVED / APPROVED WITH CONDITIONS / NOT APPROVED | `.claude/skills/team-qa/SKILL.md:264` | APPROVED -> PASS; APPROVED WITH CONDITIONS -> CONCERNS; NOT APPROVED -> FAIL; NOT ASSESSED -> NOT ASSESSED |
| APPROVED / APPROVED WITH CONDITIONS (TD sign-off) | `.claude/skills/create-architecture/SKILL.md:453` | APPROVED -> PASS; APPROVED WITH CONDITIONS -> CONCERNS |
| PROCEED / PIVOT / KILL | `.claude/skills/prototype/SKILL.md:3`, `:413` | PROCEED -> PASS; PIVOT -> CONCERNS; KILL -> FAIL. INFERENCE: this vocabulary answers "build or not," a different question from a document verdict; a hedge-fund equivalent (for example a strategy pilot) should keep a distinct decision word and cite it, not silently reuse PASS/CONCERNS/FAIL. |
| PASS / PASS WITH WARNINGS / NOT ASSESSED | `.claude/skills/day-one-patch/SKILL.md:190` | PASS -> PASS; PASS WITH WARNINGS -> CONCERNS; NOT ASSESSED -> NOT ASSESSED |
| COMPLIANT / WARNINGS / NON-COMPLIANT / NOT ASSESSED | `.claude/skills/skill-test/SKILL.md:154-159` (the `static all` summary line and per-skill result column) | COMPLIANT -> PASS; WARNINGS -> CONCERNS; NON-COMPLIANT -> FAIL; NOT ASSESSED -> NOT ASSESSED |

**Rule for P4**: every new hedge-fund gate, skill, and template uses
PASS / CONCERNS / FAIL / NOT ASSESSED directly. It does not invent a
10th vocabulary. Where a CCGS donor skill is TAKE-MODIFY
(`TRANSPLANT-MANIFEST.md`), the modification includes replacing its
verdict words with this table's target column.

---

## 2. Fixed control seats (DEC-18)

DEC-18 keeps two control seats active in every gate and every
`/cio-synthesis` run, with no mode that removes them: the cro (from
wave W1) and the cco (from wave W2) (PLAN.md:230; PLAN.md:308-309;
`ORG-BLUEPRINT.md:470-476`). This is CT1 in the AAA control category:
"the cro or cco seat runs in every mode... a grep for a conditional
skip finds none" (`AAA-QUALITY-BAR.md:168`).

### 2.1 Config values that cannot remove a fixed seat

| Config key | What it normally does | Why it cannot touch cro/cco |
|---|---|---|
| `modes.workflow` | Sets director-panel width: `minimal` -> PR only, `standard` -> TD + PR, `full` -> all four (`.claude/docs/effects-map.md:376`, `:433`). Also scales the gate-check panel (SB-21). | DEC-18 exempts the cro/cco seat from this scaling. The panel-width rule applies to the other directors only. |
| `modes.review_mode` | `lean` skips per-skill director gates unless they are PHASE-GATE type; `solo` skips all director gate spawning (`.claude/skills/team-combat/SKILL.md:32-34`; SB-19: "review_mode=lean skips per-skill control gates" today). | DEC-18 makes the cro/cco gate run regardless of `lean` or `solo`. A control gate is not an optional per-skill gate. |
| `team.size` | `individual` collapses non-core agents into the nearest core agent (`.claude/skills/team-combat/SKILL.md:40-41`); SB-20: "team.size=individual collapses CRO/CCO" today. | DEC-18 keeps cro and cco as their own seats at every `team.size` value. They are never folded into cio or another agent. |

`docs/hedge-fund-transition/PLAN.md`'s glossary records the same rule
under **fixed control seat**: "It does not scale down with
`modes.workflow`, `modes.review_mode`, or `team.size`" (PLAN.md,
glossary entry "fixed control seat", PLAN.md:898). P4 task 2 implements this by
removing the cro/cco gate's dependency on all three keys in the
transplanted gate files (PLAN.md, P4 task 2).

### 2.2 A missing seat reads NOT ASSESSED

If a gate or a `/cio-synthesis` run cannot reach the cro (or, from W2,
the cco) seat for any reason, its verdict is NOT ASSESSED, never PASS.
This follows directly from the precedence rule in Section 1 and from
CT2: "the component's verdict is NOT ASSESSED, not PASS, when its
policy or limit file is missing" (`AAA-QUALITY-BAR.md:169`). The same
discipline applies to a missing reviewer, not only a missing file.
Section 6.3 below applies this same rule to a missing seat at the
virtual investment committee.

---

## 3. Review depth by output type (DEC-20)

DEC-20 sets two review depths: judgment outputs (a stock call, the
house view, a limit) get full review; routine outputs (the daily
briefing) get lean review (PLAN.md:232; PLAN.md:311-312). DEC-20 names
three examples. The table below classifies all 14 W1 products from
`ORG-BLUEPRINT.md` §11A (the DEC-26 build list). A classification not
named directly by DEC-20 is marked INFERENCE, with its reason.

| Skill | Owner agent | Cadence (§11A) | Depth | Reason |
|---|---|---|---|---|
| `/daily-briefing` | chief-of-staff | Each trading day | Lean | DEC-20 names "the daily briefing" as its routine-output example. |
| `/house-view` | market-strategist, red-team-analyst, cio | Weekly, and on regime change | Full | DEC-20 names "the house view" as a judgment output. |
| `/stock-pitch` | research-analyst | On idea | Full | INFERENCE: this is DEC-20's "stock call." It is the analyst's committed bull case, in the DEC-23 8-section format, and it opens the DEC-16 bull/bear/synthesis chain. |
| `/red-team-review` | red-team-analyst | For every pitch and house-view change | Full | INFERENCE: DEC-16 requires a bear case for every stock call and house-view change. Reviewing it at less depth than the case it attacks would let the pitch's depth set the ceiling, defeating the DEC-25 open-dissent principle. |
| `/cio-synthesis` | cio | After each red-team review | Full | INFERENCE, close to explicit: DEC-18 names "every cio synthesis" as a point where the cro (and cco) seat always joins, which only has force under full review. |
| `/idea-screen` | idea-screener | Weekly | Lean | INFERENCE: produces a ranked candidate list with screen evidence, not a call. A stock becomes a "call" only at `/stock-pitch`, which the DEC-26 build order places after it. |
| `/risk-report` | cro | Daily summary, weekly full | Full | INFERENCE: a cro output covering exposure, concentration, liquidity, and regulatory-limit proximity. It carries the same control judgment the limits it reports against carry (DEC-19), so it takes the "a limit" depth by association. |
| `/portfolio-review` | portfolio-manager | Weekly | Full | INFERENCE: "sizing proposals" allocate capital against exposure and loss limits (DEC-19), so this is closer to DEC-20's "a limit" than to a routine record. |
| `/call-review` | cio, chief-of-staff | Monthly | Lean | INFERENCE: tracks the record of past calls against outcomes and a model-portfolio benchmark (DEC-24). It re-examines calls that already had full review when made; it is a retrospective record, not a new judgment call. |
| `/weekly-report` | chief-of-staff | Weekly | Lean | INFERENCE: compiles house view, sector reviews, pick-list changes, and risk review into one page. `ORG-BLUEPRINT.md` §8 states chief-of-staff "must not change an analyst's conclusion" when compiling, so no new judgment is created here. |
| `/ask` | chief-of-staff | On demand | Lean | INFERENCE: routes an existing answer, with sources, from the agent that owns the topic. It does not originate a call. |
| `/event-alert` | data-steward | On event | Lean | INFERENCE: a disclosure, price-move, or limit-proximity notification of a fact. It flags; it does not conclude. |
| `/coverage-config` | data-steward | On change | Lean | INFERENCE: an administrative change to the coverage universe, sector clusters, or data sources. It is a setup action, not an investment judgment. |
| `/refresh-facts` | data-steward | On the user's request only (DEC-35) | Lean | INFERENCE: re-verifies existing values against their sources. It checks facts; it does not form a new judgment. |

**Founder note**: 12 of the 14 rows above are INFERENCE, because DEC-20
names only three examples. Section 7 below asks the founder to confirm
or correct this table (item P2-C-02).

---

## 4. Approval receipt (DEC-17, DEC-36)

### 4.1 What needs a receipt

DEC-17 requires a control decision to carry the cro verdict plus a
recorded approval by the user before it takes effect; there is no
protected-path hook (PLAN.md:229; PLAN.md:314-319). DEC-36 extends
approval to two more decision types: a change to final status, and
every commit (PLAN.md:248). `AAA-QUALITY-BAR.md`'s CT3 states the same
rule as a testable check (`AAA-QUALITY-BAR.md:171`).

| Decision type | Example | Source |
|---|---|---|
| A write to a protected path | `config/risk/**`, `policies/**` (PLAN.md:901-904, glossary entry "protected path"; `AAA-QUALITY-BAR.md:171`) | DEC-17 |
| A limit change | A loss, exposure, or leverage limit value in a config file (DEC-19) | DEC-17, DEC-19 |
| A change to a document's final status | For example, a policy document or a design document that moves from Draft to Approved | DEC-36 (PLAN.md:248) |
| A commit | Every commit needs a founder approval, per DEC-36's free-draft rule | DEC-36 (PLAN.md:248) |
| A stage advance | PLAN.md's glossary entry "approval receipt" names a stage advance alongside the other three | PLAN.md:905-907, glossary entry "approval receipt" |

A free draft (an agent writing or editing a document with no approval
prompt) needs no receipt. Only the five decision types above do
(DEC-36).

### 4.2 What an agent does with no receipt

A control decision without a matching receipt reads NOT ASSESSED, not
PASS (DEC-17; PLAN.md:318; CT3: "A decision without a receipt reads NOT
ASSESSED, never PASS", `AAA-QUALITY-BAR.md:171`). No hook blocks the
underlying write: "No hook blocks the write (DEC-17); the receipt check
is the control" (`AAA-QUALITY-BAR.md:171`). Revisit hook enforcement
before real capital arrives (R-03, PLAN.md:808).

### 4.3 Receipt fields

| Field | Content |
|---|---|
| ID | A unique receipt identifier, assigned in order (for example `AR-0001`). |
| Decision type | One of the five rows in Section 4.1. |
| Target file path | The protected path, config file, or document the decision covers. |
| Content hash | The `git hash-object` value of the target at approval time, from `review-receipts.sh hash` (Section 4.4). |
| CRO verdict reference | The PASS/CONCERNS/FAIL/NOT ASSESSED verdict the cro (or, from W2, the cco) gave, and where that verdict is recorded. |
| Approver | The user (the founder and CIO; DEC-03). No agent may approve on the founder's behalf (P-02, CT4). |
| Date and time | ISO 8601, the moment of approval. |
| Scope | A one-line statement of what this approval covers (for example, "loss limit change, long-biased book, effective 2026-10-01"). |
| Notes | Free text: conditions, a documented exception (P-03), or a cross-reference to the committee minutes (Section 6). |

### 4.4 Basis: `.claude/scripts/review-receipts.sh`

`TRANSPLANT-MANIFEST.md` marks this script TAKE, unchanged
(`TRANSPLANT-MANIFEST.md:229`). It is a content-hash change detector,
not an approval-receipt writer: it stamps `Reviewed-Content-Hash: <path>
<hash>` lines into an append-only receipt file and later reports
`UNCHANGED` / `CHANGED` / `NEW` / `UNRESOLVED` for a path against the
latest stamp (`.claude/scripts/review-receipts.sh:32-76`). It emits
facts, never verdicts; the calling skill decides what to do with them
(`.claude/scripts/review-receipts.sh:27-30`).

| What transplants unchanged | What changes for the hedge fund |
|---|---|
| `hash_file()` and the `hash` mode: `git hash-object`, with a `sha1sum` fallback that deliberately produces a different (safe-direction) hash so a tool mismatch reads CHANGED, never falsely UNCHANGED (`.claude/scripts/review-receipts.sh:81-90`, `:170-185`). | The receipt file itself gains fields the script does not produce: decision type, CRO verdict reference, approver, scope, and notes (Section 4.3). The script's one output line (`Reviewed-Content-Hash: <path> <hash>`) becomes one field inside a larger receipt record; it is not itself the receipt. |
| The `check` mode's "latest stamp wins" append-only design (`.claude/scripts/review-receipts.sh:75-76`, `:205-226`) and its `RECEIPT: NONE` / `UNRESOLVED` reporting for an absent or unmatched path (`.claude/scripts/review-receipts.sh:96-124`, `:193-203`). | A caller must add the approver and decision-type fields alongside the hash line; the script has no such fields and does not read or write them. This is new process, not a script change. |
| The `sections-hash` / `sections-check` modes, usable later for a delta re-review of a long policy document (`.claude/scripts/review-receipts.sh:56-73`). | Not used for a first-cut approval receipt; deferred until a policy document needs section-level tracking. |

### 4.5 Storage path proposal

INFERENCE: no existing CCGS convention names a receipt-log path for
this purpose. `production/` already holds two gitignored, ephemeral
subdirectories (`session-state/`, `session-logs/`;
`.claude/docs/directory-structure.md`), which are the wrong place for
receipts, since a receipt is audit evidence that must survive a
session. Propose a new, git-tracked path, matching the
`production/qa/evidence/` naming pattern coding-standards.md already
uses for retained evidence:

```
production/control/
  receipts.log        # append-only; one receipt record per approval (Section 4.3 fields)
```

The limit files stay under `config/risk/` (Section 5.1), the protected
path that PLAN.md's glossary and CT3 already name.

`receipts.log` is a single append-only file, so `review-receipts.sh`'s
"latest stamp wins" model (Section 4.4) applies to it directly: a later
receipt for the same target path supersedes an earlier one for
NOT-ASSESSED checks, with no record deleted. The founder confirms this
path in Section 7 (item P2-C-03).

---

## 5. Initial limits (DEC-19)

DEC-19 sets the drafting and approval path: the cro drafts loss and
exposure limits for the long-biased book (DEC-06); the founder
approves them; the limits live in config files, not in code or skill
prose (PLAN.md:231; PLAN.md:320-322; P-05, PLAN.md:366-368). This
document does not propose a numeric limit. The cro agent drafts the
numbers later, in Phase P4 task 9, after the founder approves this
design (PLAN.md, P4 task 9: "The cro agent drafts the values after P6
builds it. The founder approves them.").

### 5.1 File layout proposal

INFERENCE, following the DEC-19 rule that limits "live in config
files" and P-05's rule that they never live in code or skill prose:

```
config/risk/
  limits.yaml             # loss, exposure, and leverage limits for the long-biased book
  limits-registry.yaml    # as_of and effective date per limit
```

These paths match the `risk.*` keys in the config schema draft
(HFT-P2-04, `project.draft.yaml`). `config/risk/**` is the protected
path that PLAN.md's glossary and CT3 name (`AAA-QUALITY-BAR.md:171`).

Each limit entry carries an `as_of` date and an effective date, per the
regulatory value registry rule in Section 6.3 (PLAN.md:323-324). A
change to this file is a protected-path write (Section 4.1) and needs
an approval receipt (Section 4) before it takes effect (DEC-17).

### 5.2 Legal limit reference

The statutory leverage cap is 400% of net asset value (NAV). Derivative
risk value, guarantees, borrowings, and effective borrowing together
must stay at or under this cap:

> 레버리지 | 파생상품 위험평가액, 채무보증, 차입금, 실질적 차입의 합계가
> 순자산의 400% 이내 | 법 제249조의7 제1항

Source: HF-REF-06 §4.3, 표 4-3 (`docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:31`).
This chunk is marked `volatility: medium` with the note "Regulatory
values, thresholds, rates, or deadlines. Re-verify before compliance
use" (`docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:10`).
`ORG-BLUEPRINT.md:489` (control point #10) already applies this figure
as a hard block, owned by cro/cco, and instructs: "Set the internal
limit lower than the statutory limit" (`ORG-BLUEPRINT.md:489`, citing
HF-REF-06 §4.3 표 4-3 and HF-REF-09 §7.2 표 7-1). This document
carries the 400%-of-NAV statutory ceiling forward as the reference the
cro must draft under. It sets no internal number.

---

## 6. Virtual investment committee (DEC-22)

DEC-22 seats four members: cio, cro, portfolio-manager, and
red-team-analyst. They present; the user decides; minutes are kept
(PLAN.md:234). `ORG-BLUEPRINT.md` §11.3 already runs this committee as
a virtual body inside the per-idea investment cycle and marks its
minutes owner INFERENCE (`ORG-BLUEPRINT.md:589-592`). This section
finalizes the design task 10 of the P2 work breakdown asks for (PLAN.md,
P2 task 10).

### 6.1 Trigger (DEC-16)

The committee convenes for every stock call and every house-view
change (DEC-16, PLAN.md:228). These are the same two judgment outputs
Section 3 marks Full review.

### 6.2 Sequence

| Step | Actor | Output |
|---|---|---|
| 1 | research-analyst (via `/stock-pitch`, for a stock call) or market-strategist (via `/house-view`, for a house-view change) | The bull case, or the market-direction case. |
| 2 | red-team-analyst (via `/red-team-review`) | The bear case against step 1. It must never write the case it attacks (`ORG-BLUEPRINT.md:452-455`, bull/bear/synthesis rule). |
| 3 | cio (via `/cio-synthesis`) | Synthesis, confidence level, and open questions. Written only after both the bull case and the bear case exist. |
| 4 | cio, cro, portfolio-manager, and red-team-analyst | A recorded presentation of the case to the user, referencing steps 1-3. |
| 5 | The user (founder and CIO). No agent decides (DEC-09, DEC-30). | The decision, recorded. |
| 6 | The minutes owner (Section 6.6) | The minutes record, per the template in Section 6.5. |
| 7 | cio, chief-of-staff (via `/call-review`) | An entry tracking the call against its outcome, and against the model portfolio's benchmark (DEC-24). |

### 6.3 Quorum rule

All four seats (cio, cro, portfolio-manager, red-team-analyst) must be
present for the committee's record to carry a decision verdict. This
follows Section 2's fixed-seat rule: the cro seat never scales down
with `modes.workflow`, `modes.review_mode`, or `team.size` (DEC-18). If
the cro seat (or, from W2, the cco seat where applicable) is missing
from a committee session for any reason, the session's record reads
NOT ASSESSED, not a decision (Section 2.2, precedence rule in Section
1). The user may still decide without a complete committee record, but
the record itself must show NOT ASSESSED, so a later review does not
mistake an incomplete session for a cleared one.

### 6.4 Open-dissent rule (DEC-25)

DEC-25 puts "documented principles and open dissent" first among the
organization's principles (PLAN.md:237; `ORG-BLUEPRINT.md:686-688`).
The minutes record every committee member's position, not only the
majority view. A member who disagrees with the emerging synthesis
states the disagreement and its reason; the minutes record both,
whatever the user ultimately decides. A dissent is never edited or
removed by another agent (non-override rule, `ORG-BLUEPRINT.md:440-443`,
restated for this process in `ORG-BLUEPRINT.md:459-460`'s bull/bear/synthesis
rule: "No agent may edit a cro verdict").

### 6.5 Minutes template

| Field | Content |
|---|---|
| Minutes ID | A unique identifier (for example `IC-0001`). |
| Date and time | ISO 8601. |
| Trigger | Stock call (`/stock-pitch`) or house-view change (`/house-view`), with the target name. |
| Bull case reference | The `/stock-pitch` or `/house-view` output this session reviewed. |
| Bear case reference | The `/red-team-review` output. |
| Synthesis reference | The `/cio-synthesis` output, with its confidence level. |
| Attendance | Which of the four seats (cio, cro, portfolio-manager, red-team-analyst) were present. Quorum per Section 6.3. |
| Positions and dissent | One row per member: their position, and, if it differs from the final decision, the dissent and its reason (Section 6.4). |
| User decision | The decision the user made, in the user's own words. |
| Capacity estimate | The capacity estimate the output carried (DEC-25: "W1 products carry capacity estimates"). |
| Follow-up | Any open question carried into `/cio-synthesis`'s "open questions" field, or into the next `/call-review`. |

### 6.6 Minutes owner

`ORG-BLUEPRINT.md` marks chief-of-staff as the minutes owner in W1, and
marks that choice INFERENCE, pending P2 confirmation
(`ORG-BLUEPRINT.md:591-592`). This document does not settle it: Section
7, item P2-C-01, asks the founder to confirm or change the owner.

### 6.7 Pre-screen label (F-09)

Every agent review inside this sequence, including the cro's verdict
and the committee's presentation, is a pre-screen, not an independent
review: "A subagent in the same session is not an independent reviewer
for segregation of duties. It is a pre-screen. A human with an
independent reporting line must sign"
(`docs/hedge-fund-transition/evidence/design-spec.md:39`, F-09; restated
at PLAN.md's pre-screen rule, PLAN.md:326-328). The user's decision in
step 5 is that required human sign-off. Present every committee output
to the user with this label, so the user never mistakes a pre-screen
for a cleared, independent review.

---

## 7. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-C-01 | Who owns the virtual investment committee's minutes? | A: chief-of-staff (the `ORG-BLUEPRINT.md` §11.3 default, INFERENCE) records every session's minutes, in addition to its other information-product duties. B: cio, as the committee's synthesis author, records the minutes directly. C: a dedicated minutes-taking step inside `/cio-synthesis` writes the minutes as part of that skill's own output. D: no fixed owner; whichever agent is present last in the sequence (Section 6.2) writes the minutes. | Recommend A. `ORG-BLUEPRINT.md` already assumes chief-of-staff for W1 and only flags it INFERENCE (`ORG-BLUEPRINT.md:591-592`); chief-of-staff already compiles every other W1 information product (§11A), so minutes-keeping fits its existing role and adds no new agent. |
| P2-C-02 | Does the founder accept the review-depth classification in Section 3 for the 12 W1 products DEC-20 does not name directly? | A: accept the table in Section 3 as drafted. B: promote every cro and portfolio-manager output to Full (widens `/risk-report` and `/portfolio-review`'s current Full to also cover any other control-adjacent output later added). C: demote `/red-team-review` and `/cio-synthesis` to Lean, treating them as process steps inside the `/stock-pitch` / `/house-view` review rather than separate judgment outputs. D: the founder reclassifies each of the 12 rows individually. | Recommend A. DEC-20 sets the principle (judgment outputs get Full, routine outputs get Lean) but names only 3 of 14 products; Section 3's reasoning applies that principle consistently, and P4 task 8 needs a settled table before it encodes review depth in the gate files. |
| P2-C-03 | Does the founder accept the `production/control/` storage path proposal in Sections 4.5 and 5.1 for approval receipts, with limits under `config/risk/`? | A: accept `production/control/receipts.log` for receipts and `config/risk/limits.yaml` for limits, as proposed. B: use a different tracked directory (the founder names one). C: keep receipts inside the existing `production/session-logs/` convention, accepting that it is currently gitignored and would need that exclusion removed for this one subdirectory. D: split receipts into one file per decision type, instead of one append-only log. | Recommend A. No existing CCGS convention names this path (INFERENCE); `production/control/` follows the same domain-plus-evidence-type naming `production/qa/evidence/` already uses, and a single append-only log matches `review-receipts.sh`'s existing "latest stamp wins" design (Section 4.4), so no new mechanism is needed to read it. |
| P2-C-04 | Should the CONCEPTS/STRONG/CONCERNS vocabulary's missing fail-equivalent tier (Section 1.2, row 3) be fixed now, in P2, or left for P4 task 1? | A: leave it for P4 task 1, alongside the other 8 vocabularies' rewrite. B: fix it now, in this document, by adding a FAIL-mapped tier and asking the founder to name it. C: retire this vocabulary's donor gate outright rather than give it a fail tier, if the hedge-fund organization has no equivalent gate. | Recommend A. P4 task 1 ("Write the single verdict vocabulary into every gate file," PLAN.md, P4 task 1) is the phase PLAN.md assigns this rewrite to; fixing one file now would split the vocabulary rewrite across two phases for no benefit, since P2's job is the target design, not the file edits themselves (PLAN.md §8, P2 entry/exit criteria). |

---

## Founder decisions recorded (2026-09-25)

The founder answered the items above. HFT-P2-00 §4 is the register; §4A states the consequences.

| ID | Answer |
|---|---|
| P2-C-01 | A: chief-of-staff keeps the minutes |
| P2-C-02 | A: accept the table |
| P2-C-03 | A: `production/control/receipts.log`; limits in `config/risk/` |
| P2-C-04 | A: fix in P4 task 1 |

## 8. Traceability

| P2 task / DEC-NN | Covered in |
|---|---|
| P2 task 3 (finalize the control model: verdict vocabulary, fixed seats, approval-receipt rules) | Sections 1, 2, 4 |
| P2 task 10 (design the virtual investment committee) | Section 6 |
| DEC-16 (bull case, bear case, synthesis for every stock call and house-view change) | Sections 3, 6.1, 6.2 |
| DEC-17 (agent verdict plus user approval; no protected-path hook; a decision without a receipt reads NOT ASSESSED) | Section 4 |
| DEC-18 (fixed control seats; not removed by `modes.workflow`, `modes.review_mode`, `team.size`) | Section 2, Section 6.3 |
| DEC-19 (cro drafts loss and exposure limits; founder approves; limits live in config files) | Section 5 |
| DEC-20 (review depth by output type: judgment full, routine lean) | Section 3 |
| DEC-22 (virtual investment committee: cio, cro, portfolio-manager, red-team-analyst present; user decides; minutes kept) | Section 6 |
| DEC-24 (`/call-review` tracks every call against its outcome; model portfolio against a benchmark) | Section 6.2, step 7 |
| DEC-25 (documented principles and open dissent first; capacity estimates; numeric limits stay in config) | Section 6.4, Section 5 |
| DEC-36 (free drafts need no approval; final status and every commit need a founder approval receipt) | Section 4.1 |
| F-07 (28 director-gate files, 9 verdict vocabularies) | Section 1 |
| F-09 (a same-session agent review is a pre-screen, not an independent review) | Section 6.7 |
| P-09 (one verdict vocabulary; a missing input reads NOT ASSESSED, never PASS) | Section 1, Section 2.2 |
