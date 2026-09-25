# HFT-P3-00 — Phase P3 Local Handoff

## Document control

| Field | Value |
|---|---|
| Document ID | HFT-P3-00 |
| Title | Phase P3 local handoff: repository bootstrap and foundation transplant |
| Version | 1.0 |
| Date | 2026-09-25 |
| Status | Issued. The founder approved Phase P2 (AR-P2-0001) and asked for P3 to run locally. |
| Owner | Advisor (planning session) |
| Reader | The founder, and the local Claude Code session that runs P3 |
| Writing standard | ASD-STE100 |

## 1. Purpose

Phase P3 runs in a local Claude Code session on the founder's machine,
in a new repository (DEC-04). The planning session cannot create that
repository, because its GitHub access covers `gmdjlee/cgs` only.

This document is the complete starting context for the local session.
It states the state at handoff, the files to read, the prerequisites,
the steps, the exit checks, and a start prompt. A local session that
reads this document does not need the planning conversation.

## 2. State at handoff

| Item | State | Record |
|---|---|---|
| P0 reference chunks | Done | `docs/hedge-fund-setup/ref/` (21 chunks); `python3 docs/hedge-fund-setup/tools/split_report.py --check` |
| P1 founder decisions | Done: 38 decisions, DEC-01 to DEC-38 | [QUESTIONS.md](QUESTIONS.md); [PLAN.md](PLAN.md) Table 6.0-1 |
| P2 target design | Done: approved 2026-09-25 | [p2/P2-00-INDEX.md](p2/P2-00-INDEX.md) §5, receipt AR-P2-0001 |
| P3 bootstrap | Not started | This document |
| Planning source | Branch `claude/kind-dijkstra-idznze` of `gmdjlee/cgs`, pull request #1 (draft) | https://github.com/gmdjlee/cgs/pull/1 |
| CCGS baseline | v1.1.1, commit `7ed2c3e` | PLAN.md §1 |

## 3. Read order for the local session

Read these files in this order before any change. Each row states why.

| # | File (in the planning set) | Why |
|---|---|---|
| 1 | This document | Steps, checks, and rules for P3 |
| 2 | [PLAN.md](PLAN.md) §6 (mission, decisions, control model) and §8 (P3, P4) | The authority for scope and tasks |
| 3 | [p2/P2-00-INDEX.md](p2/P2-00-INDEX.md) §4, §4A, §5 | The 25 approved design answers and their consequences |
| 4 | [TRANSPLANT-MANIFEST.md](TRANSPLANT-MANIFEST.md) §4, §6, §10 | What to copy, in which order; the silent breaks; resolved verdicts |
| 5 | [p2/P2-05-BUILD-PRIORITY.md](p2/P2-05-BUILD-PRIORITY.md) §3 | Foundation transplant order F1 to F15 |
| 6 | [p2/P2-04-CONFIG-SCHEMA.md](p2/P2-04-CONFIG-SCHEMA.md) and [p2/project.draft.yaml](p2/project.draft.yaml) | The new `project.yaml` |
| 7 | [p2/P2-02-LIFECYCLE.md](p2/P2-02-LIFECYCLE.md) and [p2/workflow-catalog.draft.yaml](p2/workflow-catalog.draft.yaml) | The new stage enum and catalog; the reader-update list |
| 8 | [p2/P2-03-CONTROL-MODEL.md](p2/P2-03-CONTROL-MODEL.md) §4 | The approval receipt format and path |
| 9 | [p2/P2-07-CHANNEL-AND-DATA.md](p2/P2-07-CHANNEL-AND-DATA.md) | Telegram channel and KIS data facts, with GAP marks |
| 10 | [AAA-QUALITY-BAR.md](AAA-QUALITY-BAR.md) §9 | The two lint helpers P3 builds |

## 4. Prerequisites (founder actions before the session starts)

| # | Item | Needed for | Note |
|---|---|---|---|
| 1 | git, Python 3 with PyYAML, and the Claude Code CLI | Every step | `yaml-helper.sh` needs Python 3 (TRANSPLANT-MANIFEST.md §4, row 1) |
| 2 | A new, empty, private GitHub repository. The founder picks the name. | P3 task 1 (DEC-04) | Private, because the planning set names the fund's design |
| 3 | A local clone of `gmdjlee/cgs`, branch `claude/kind-dijkstra-idznze` | Source of the planning set | Or pull request #1 after the merge |
| 4 | A Telegram bot token (from BotFather) | R-17, P2-D-01 | Store it only in `data/private/` (DEC-32) |
| 5 | A KIS Developers Open API app key and secret | R-16, P2-D-03 | A brokerage account is needed. Store the keys only in `data/private/`. No agent reads them. |
| 6 | An OpenDART API key | DEC-31 | Store it only in `data/private/` |

Items 4 to 6 can wait until P3 step 7. Do not paste any key into a
prompt, a document, or a commit.

## 5. Steps

The step numbers follow PLAN.md §8 P3 where a task exists. "Check"
states the exit evidence for the step.

### Step 1. Create the repository (P3 task 1; DEC-04)

```bash
mkdir <new-repo> && cd <new-repo> && git init
git remote add origin <new private GitHub repository URL>
# CCGS upstream (UPGRADING.md, Strategy A)
git remote add upstream https://github.com/Donchitos/Claude-Code-Game-Studios.git
git fetch upstream
git cat-file -t 7ed2c3e     # must print "commit"
```

If `7ed2c3e` is missing upstream, add `gmdjlee/cgs` as a second remote
and use it as the source of the v1.1.1 files. Keep every foundation
file at its CCGS path (P-06), so later fixes arrive by `UPGRADING.md`
Strategy A2 (selective checkout) or B (cherry-pick).

Check: `git remote -v` lists `origin` and `upstream`.

### Step 2. Bring in the planning set and the reference chunks

Copy these paths from the `gmdjlee/cgs` branch into the new repository,
at the same paths:

- `docs/hedge-fund-transition/` (the plan, the decisions, the P2 package)
- `docs/hedge-fund-setup/` (the source report, the 21 chunks, and
  `tools/split_report.py`)

Check: `python3 docs/hedge-fund-setup/tools/split_report.py --check`
prints 183 quotes checked and 0 missing.

### Step 3. Protect private data first (P4 task 10, moved earlier)

Do this before any key or holding enters the machine. P2 moved secrets
into P3 (R-16, R-17), so this P4 task runs first.

1. Create `data/private/` and add it to `.gitignore` (DEC-32).
2. Add `production/dashboard/` to `.gitignore` (P2-D-02).
3. Keep `production/session-state/` and `production/session-logs/`
   in `.gitignore` (CCGS convention).
4. Add a `settings.json` deny rule for `data/private/**` for agent file
   reads. The adapter scripts read the keys through Bash only.

Check: `git check-ignore data/private/x production/dashboard/x` prints
both paths.

### Step 4. Transplant the foundation (P3 task 2)

Use the order in P2-05 §3, rows F1 to F15. Use a selective checkout
from `7ed2c3e`, for example:

```bash
git checkout 7ed2c3e -- .claude/hooks/yaml-helper.sh
```

1. F1: write `project.yaml` from `p2/project.draft.yaml`, then
   transplant `yaml-helper.sh`.
2. F2 to F5: session-state hooks, gate support, audit-log hooks, and
   `validate-skill-change.sh`.
3. F6: rewrite `.claude/settings.json` last, so its hook list matches
   the kept files. Keep the Step 3 deny rule.
4. F7: `statusline.sh` and `notify.sh`.
5. F8 (erratum E-01): transplant `validate-assets.sh` and point its
   path filter at `config/risk/` (DEC-19; SB-08). Do not transplant
   `code-root-resolution.md` (Q25 = B).
6. F9 to F15: the W1 support skills (`gate-check`,
   `consistency-check`, `skill-test`, `sprint-plan`, `sprint-status`,
   `scope-check`, `retrospective`, `help`, `onboard`).
7. Install `p2/workflow-catalog.draft.yaml` as
   `.claude/docs/workflow-catalog.yaml`. Read it with
   `artifact-check.sh` before F3 finishes (TRANSPLANT-MANIFEST.md §4,
   group 3).
8. Write a new `CLAUDE.md` for the fund. Keep the collaboration
   protocol. Do not import an engine reference (SB-16).

Check: every kept file exists at its CCGS path. `git diff --stat
7ed2c3e -- <kept paths>` shows only the planned changes.

### Step 5. Apply the approved config decisions (P3 task 4)

| Decision | Change |
|---|---|
| P2-L-01 | Add the stage enum `pre-setup`, `s1`-`s8`, `g1`-`g3` to `yaml-helper.sh`; set `project.stage: pre-setup` |
| P2-S-01 | Add `draft_free` to the `modes.automation` enum (`yaml-helper.sh:464` in CCGS) and to `automation-modes.md`. Behavior: no prompt for a draft; approval before a final-status change or a commit (DEC-36). |
| P2-S-02 | Rename the values of `qa.level` and `modes.review_mode` before any reader is built. Record the old-to-new map in `P2-04` form in the new repository. Name the new values with the founder. |
| P2-S-04 | Keep `modes.rigor: standard` |
| P2-C-03 | Create `production/control/receipts.log`. Its first entry is AR-P2-0001 (copy the fields from HFT-P2-00 §5). Keep limits in `config/risk/`. |
| P2-L-03 | Record in the `gate-check` rewrite plan that the `gate:` block replaces the reference files (the rewrite itself is P4 task 1) |

Check: source the helper and read the three keys. Each value must
resolve with no enum warning:

```bash
source .claude/hooks/yaml-helper.sh
for k in project.stage modes.automation modes.rigor; do get_effective_yaml_key "$k"; done
validate_yaml_enum project.yaml    # yaml-helper.sh:704 (CCGS v1.1.1); prints nothing when every value is valid
```

Before Step 5, the unmodified CCGS helper rejects two approved values.
The planning session ran the check on `p2/project.draft.yaml` on
2026-09-25 and got:

```text
modes.automation: 'draft_free' is not a valid value (expected: collaborative|guided|autonomous)
project.stage: 'pre-setup' is not a valid value (expected: Concept|Systems Design|Technical Setup|Pre-Production|Production|Polish|Release)
```

After Step 5, the same check prints nothing and returns 0.

### Step 6. Fix the silent breaks for P3 (P3 task 3)

Fix and test SB-01 to SB-16 and SB-22 (TRANSPLANT-MANIFEST.md §6, phase
column "P3"). SB-17 to SB-21 and SB-23 to SB-28 belong to P4. Each SB
row states its test.

Also do P3 tasks 5 to 7: `settings.json` permissions and hooks,
`log-instructions.sh` and `statusline.sh` wiring, and the
`detect-gaps.sh` rewrite.

Check: one test result per SB row, kept as evidence.

### Step 7. Channel and data adapters (R-16, R-17)

1. Telegram (P2-D-01): install the official Telegram channel plugin,
   pair the bot, and start one long-running session with the channel
   (HFT-P2-07 §2.3, option B). A message carries a market summary
   only. It never carries holdings, positions, sizing, or personal
   data (P2-D-02).
2. KIS price adapter (P2-D-03): write the adapter with a read-only
   endpoint allow-list (quotes and history only). Write a test that
   fails if the adapter code names an order or transfer endpoint
   (R-16, DEC-30). Confirm the GAP facts in HFT-P2-07 §3.2: investor
   flows, short-selling data, rate limits. If KIS lacks a data type,
   add pykrx for that data type only.
3. OpenDART (DEC-31): set up an OpenDART MCP server or a direct API
   adapter. Record the exact tool names for the P2-01 allow-lists.

Check: the allow-list test passes; a test message reaches Telegram
with no holdings in it.

### Step 8. Helpers, test scaffold, and measurement (P3 tasks 8 to 11)

1. Build `.claude/scripts/ste-lint.sh` (observation only; AAA-12).
2. Build the Korean style-check helper (observation only; DEC-33;
   AAA-QUALITY-BAR.md §9.2).
3. Scaffold the test framework for the analysis scripts (DEC-29).
4. Measure whether the agent `model:` field changes the model that
   runs the agent (DEC-38, F-12, R-10). Record the result. If the field
   does not apply, record the tiers in P2-01 as intent only.

Check: both helpers print observations, never a verdict; the test
scaffold runs; the measurement note exists.

## 6. P3 exit criteria (PLAN.md §8)

1. The new repository's transplant set passes a reassembly-style
   check: every kept file matches `7ed2c3e` or has a recorded change.
2. The SB tests for P3 (Step 6) pass.
3. The founder approves the P3 result with a receipt in
   `production/control/receipts.log` (DEC-36).

## 7. Rules for the local session

- The founder makes every decision. Ask before a choice that the
  decision log does not settle. Give 4 or 5 options with a
  recommendation.
- DEC-36: write drafts freely. Get the founder's approval before a
  final-status change and before every commit.
- DEC-30: no code sends or drafts an order.
- DEC-32: no key, holding, or personal data leaves `data/private/`.
- DEC-33: technical documents in ASD-STE100 English; answers to the
  founder in Korean.
- Every fact carries a source: file:line, HF-REF-NN, F-NN, or DEC-NN.
  Mark an extension INFERENCE and an unsupported claim GAP.
- A helper in `.claude/scripts/` gives observations, never a verdict.
- Record a new decision as the next DEC number in the new repository's
  decision log. Do not edit the frozen `evidence/` files.
- Keep the session checkpoint in `production/session-state/active.md`
  (CCGS convention). It is gitignored; this document is the committed
  record.

## 8. Start prompt for the local session

Paste this prompt into the first local session, in the new repository,
after Step 2:

```text
Read docs/hedge-fund-transition/P3-LOCAL-HANDOFF.md first, then the files
in its Section 3, in order. We are running Phase P3 (repository bootstrap
and foundation transplant). P1 and P2 are done and approved (AR-P2-0001).
Follow the Section 5 steps and the Section 7 rules. Answer me in Korean.
Before each step, show me the plan for the step and ask for approval.
Do not commit without my approval. Start with Step 3.
```

## 9. What stays in the planning repository

- Pull request #1 on `gmdjlee/cgs` holds the planning set. Merging it
  is the founder's choice. The planning session keeps checking the pull
  request until it is merged or closed.
- A later change to an approved planning document needs a new receipt.
  Make the change in the new repository's copy, and record it there.
