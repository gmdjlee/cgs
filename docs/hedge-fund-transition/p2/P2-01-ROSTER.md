# HFT-P2-01 — Final Wave Roster, Model Tiers, and Tool Allow-Lists

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-01 |
| Title | Final wave roster, model tiers, and tool allow-lists |
| Version | 0.1 |
| Date | 2026-09-25 |
| Status | Draft for founder approval |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | [ORG-BLUEPRINT.md](../ORG-BLUEPRINT.md) §6, §8, §11A; [design-addendum-01.md](../evidence/design-addendum-01.md) §4, §5, Erratum 01; [PLAN.md](../PLAN.md) §6.0, §8 (P2 task list, P3 task 11); [TRANSPLANT-MANIFEST.md](../TRANSPLANT-MANIFEST.md) §5.8; `.claude/docs/model-tiers.md`; `.claude/agents/producer.md`, `.claude/agents/godot-specialist.md` (frontmatter pattern) |
| Writing standard | ASD-STE100 |

This document covers P2 task 1 (finalize the wave roster) and P2 task 9
(map every W2 and W3 agent to a model tier). PLAN.md:459-461,475-476.

## 2. Purpose and scope

This document sets the final agent roster for waves W1, W2, and W3 (29
agent definitions), plus the 4 Q25 conditional agents as off rows. It
proposes a model tier for every agent under DEC-38, and a tool allow-list
for every W1 agent. It does not build any agent file. It does not decide
the sector-cluster run mode or every ambiguous model tier; Section 5 lists
these as founder decisions.

This document is a DRAFT. DEC-36 lets a draft go with no approval. Only a
change to final status needs the founder's approval receipt.
decisions.md:36 (see PLAN.md:250 for the DEC-38 text this table applies).

## 3. Final roster table

Columns: **Org tier** is the tier from ORG-BLUEPRINT.md §6 (1, 2, or 3).
**Model tier (proposed)** applies the DEC-38 rule (Section 4). **Judgment
output?** flags whether the role's normal output matches the Section 4
definition; for W1 this is informational only, because DEC-38 already
fixes the W1 model tier by name. **Source** cites the ORG-BLUEPRINT.md §6
row (by line) and, for the five new W1 roles and the Erratum 01 count
fix, the addendum.

### 3.1 Wave W1 — 11 agents (ORG-BLUEPRINT.md:304-311)

| # | Agent | Wave | Org tier | Reports to | Model tier (proposed) | Judgment output? | CCGS donor skeleton | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | cio | W1 | 1 | CEO (user) | Opus (DEC-38) | Yes — writes the synthesis (DEC-16) | creative-director (protocol shape only) | ORG-BLUEPRINT.md:267 |
| 2 | cro | W1 | 1 | user (CEO); never cio (DEC-10) | Opus (DEC-38) | Yes — gives the non-overridable risk verdict | technical-director (Strategic Decision Workflow shape); systems-designer (Formula Output Format) | ORG-BLUEPRINT.md:268 |
| 3 | chief-of-staff | W1 | 1 | user | Opus (DEC-38) | Yes — compiles the briefing and report; must not change a conclusion | producer (coordination, milestone tracking) | ORG-BLUEPRINT.md:298; addendum §4 (design-addendum-01.md:64) |
| 4 | portfolio-manager | W1 | 2 | cio | Sonnet (DEC-38) | Yes — sizing proposals are a recommendation | game-designer (Question-First Workflow shape only) | ORG-BLUEPRINT.md:271 |
| 5 | head-of-research | W1 | 2 | cio | Sonnet (DEC-38) | Yes — leads sector-analyst output into a research view | game-designer (Question-First Workflow shape only) | ORG-BLUEPRINT.md:273 |
| 6 | market-strategist | W1 | 2 | cio | Sonnet (DEC-38) | Yes — writes the house-view base case | systems-designer (Formula Output Format for indicators) | ORG-BLUEPRINT.md:299; addendum §4 (design-addendum-01.md:65) |
| 7 | research-analyst | W1 | 3 | cio (stage 1) / head-of-research (stage 2+) | Sonnet — Tier-3 judgment exception (DEC-38) | Yes — writes the bull case and full note | game-designer (Question-First Workflow shape only) | ORG-BLUEPRINT.md:281 |
| 8 | red-team-analyst | W1 | 3 | cio | Sonnet — Tier-3 judgment exception (DEC-38) | Yes — writes the bear case | design-review (adversarial reviewer brief) | ORG-BLUEPRINT.md:300; addendum §4 (design-addendum-01.md:66) |
| 9 | data-steward | W1 | 3 | chief-of-staff | Haiku (DEC-38) | No — registry and freshness tracking, no verdict | economy-designer (canonical registry) | ORG-BLUEPRINT.md:302; addendum §4 (design-addendum-01.md:68) |
| 10 | idea-screener | W1 | 3 | head-of-research | Haiku (DEC-38) | No — ranked screen evidence, not a conclusion | balance-check (outlier detection) | ORG-BLUEPRINT.md:301; addendum §4 (design-addendum-01.md:67) |
| 11 | trader | W1 | 3 | cio (stage 1) / head-of-trading (stage 2+) | Haiku (DEC-38) | No — execution information only (DEC-30) | No domain donor; lead-programmer (Implementation Workflow shape only) | ORG-BLUEPRINT.md:282 |

### 3.2 Wave W2 — 12 more agents, 23 total (ORG-BLUEPRINT.md:313-324; Erratum 01, design-addendum-01.md:150-158)

| # | Agent | Wave | Org tier | Reports to | Model tier (proposed) | Judgment output? | CCGS donor skeleton | Source |
|---|---|---|---|---|---|---|---|---|
| 12 | ceo-office | W2 | 1 | CEO (human) / board | Opus (Tier 1) | Yes — drafts the business plan, the 3-year model, and board material | producer | ORG-BLUEPRINT.md:266; Erratum 01 (design-addendum-01.md:150-158) |
| 13 | cco | W2 | 1 | user (CEO), DEC-10 | Opus (Tier 1) | Yes — non-overridable compliance verdict (a compliance interpretation) | technical-director (Strategic Decision Workflow shape); security-engineer (per-change review checklist) | ORG-BLUEPRINT.md:269 |
| 14 | coo | W2 | 1 | CEO | Opus (Tier 1) | Yes — runs accounting, budget, HR, and contract management for the CEO | producer | ORG-BLUEPRINT.md:270 |
| 15 | fund-operations-lead | W2 | 2 | coo | Sonnet (Tier 2) | No exception needed — Tier 2 is already Sonnet | release-manager (strict, no-skip staged pipeline) | ORG-BLUEPRINT.md:272 |
| 16 | technology-lead | W2 | 2 | coo | Sonnet (Tier 2) | No exception needed | technical-director | ORG-BLUEPRINT.md:276 |
| 17 | legal-counsel-liaison | W2 | 2 | ceo-office; dotted line to cco | Sonnet (Tier 2) | No exception needed. Must not give legal advice (§4) | No domain donor; game-designer (Question-First Workflow shape only) | ORG-BLUEPRINT.md:277 |
| 18 | investor-relations | W2 | 3 | coo (stage 1) / investor-relations-lead (stage 2+) | Sonnet — Tier-3 judgment exception | Yes — drafts DDQ answers, the monthly report, and the investor letter (external-party draft) | community-manager (discipline only) | ORG-BLUEPRINT.md:283 |
| 19 | compliance-analyst | W2 | 3 | cco | Haiku (Tier 3) | No — checks a log against a checklist; cco gives the interpretation | security-engineer (per-change review checklist) | ORG-BLUEPRINT.md:285 |
| 20 | regulatory-reporting-specialist | W2 | 3 | cco | Sonnet — Tier-3 judgment exception | Yes — drafts the regulatory filings in §10 (an external-party draft, to the FSC/FSS) | release-manager (staged pipeline; version numbering) | ORG-BLUEPRINT.md:286 |
| 21 | operations-analyst | W2 | 3 | fund-operations-lead | Haiku (Tier 3) | No — a detection control (flags a mismatch); not a verdict | qa-tester (checklist and case writing) | ORG-BLUEPRINT.md:287 |
| 22 | fund-accountant | W2 | 3 | fund-operations-lead | Haiku (Tier 3) | No — an internal NAV check, a detection control; not the final NAV | economy-designer (canonical registry awareness) | ORG-BLUEPRINT.md:288 |
| 23 | security-officer | W2 | 3 | technology-lead | Haiku (Tier 3) | No — monitors system status and backup/DR logs | security-engineer | ORG-BLUEPRINT.md:290 |

### 3.3 Wave W3 — 6 more agents, 29 total (ORG-BLUEPRINT.md:325-328)

| # | Agent | Wave | Org tier | Reports to | Model tier (proposed) | Judgment output? | CCGS donor skeleton | Source |
|---|---|---|---|---|---|---|---|---|
| 24 | head-of-trading | W3 | 2 | cio | Sonnet (Tier 2) | No exception needed | release-manager (no-skip pipeline; halt on a failed step) | ORG-BLUEPRINT.md:274 |
| 25 | investor-relations-lead | W3 | 2 | coo | Sonnet (Tier 2) | No exception needed. Also drafts external IR material | community-manager (no-unverified-claims rule; crisis communication) | ORG-BLUEPRINT.md:275 |
| 26 | risk-analytics-lead | W3 | 2 | cro | Sonnet (Tier 2) | No exception needed. DEC-38 reserves Opus for cio, cro, chief-of-staff only | analytics-engineer (metric taxonomy; dashboard specification) | ORG-BLUEPRINT.md:278 |
| 27 | investor-communications-writer | W3 | 3 | investor-relations-lead | Sonnet — Tier-3 judgment exception | Yes — drafts IR reports for investors (external-party draft) | writer | ORG-BLUEPRINT.md:289 |
| 28 | risk-analyst | W3 | 3 | cro | Haiku (Tier 3) — GAP, see P2-R-01 | Ambiguous — see Section 5, P2-R-01 | systems-designer (Formula Output Format) | ORG-BLUEPRINT.md:284 |
| 29 | governance-secretary | W3 | 3 | ceo-office / board | Haiku (Tier 3) — GAP, see P2-R-02 | Ambiguous — see Section 5, P2-R-02 | producer (records; milestone tracking) | ORG-BLUEPRINT.md:291 |

### 3.4 Off — 4 Q25 conditional agents (Q25 = B, DEC-29)

These four agents stay off. They activate only if a later round changes
Q25 to C or D. decisions.md:29; ORG-BLUEPRINT.md:329-331.

| # | Agent | Wave | Org tier | Reports to | Model tier (proposed) | Judgment output? | CCGS donor skeleton | Source |
|---|---|---|---|---|---|---|---|---|
| 30 | quant-research-lead | Off (CONDITIONAL, Q25 = C/D) | 2 | cio | N/A — off | N/A — off | prototyper (research isolation rule; PROCEED/PIVOT/KILL) | ORG-BLUEPRINT.md:279 |
| 31 | model-governance-lead | Off (CONDITIONAL, Q25 = C/D) | 2 | cro; never to research | N/A — off | N/A — off | lead-programmer (standards enforcement; code review); qa-lead (evidence-type table) | ORG-BLUEPRINT.md:280 |
| 32 | quant-researcher | Off (CONDITIONAL, Q25 = C/D) | 3 | quant-research-lead | N/A — off | N/A — off | prototyper (isolation rule; worktree isolation) | ORG-BLUEPRINT.md:292 |
| 33 | data-engineer | Off (CONDITIONAL, Q25 = C/D) | 3 | technology-lead | N/A — off | N/A — off | devops-engineer (branching strategy; CI); engine-programmer (data pipeline code) | ORG-BLUEPRINT.md:293 |

**Count check.** W1 = 11 (3.1). W1 + W2 = 11 + 12 = 23 (3.1 + 3.2). W1 +
W2 + W3 = 23 + 6 = 29 (3.1 + 3.2 + 3.3). Off = 4 (3.4). This matches
ORG-BLUEPRINT.md:336 and PLAN.md:459-461. Excluded from every table above:
the 4 "not applicable" agents (valuation-analyst, macro-economist,
pod-lead, capital-allocation-support). DEC-05 and DEC-06 rule these out;
they are not part of the 29-plus-4 count. ORG-BLUEPRINT.md:332-334.

## 4. Model-tier rule (DEC-38)

**The rule.** Tier 1 uses Opus. Tier 2 uses Sonnet. Tier 3 uses Haiku,
except that a Tier 3 agent that writes a judgment output uses Sonnet.
decisions.md:38; PLAN.md:250.

**W1 is fixed by name in DEC-38**, not derived from the rule: Opus for
cio, cro, and chief-of-staff; Sonnet for portfolio-manager,
head-of-research, market-strategist, research-analyst, and
red-team-analyst; Haiku for data-steward, idea-screener, and trader.
decisions.md:38.

**Judgment output, defined for W2 and W3 (this document).** A judgment
output is one of:

1. A recommendation.
2. A verdict.
3. A synthesis.
4. A draft for an external party: a regulator, an investor, or a
   counterparty.
5. A legal or compliance interpretation.

A routine output (a log entry, a reconciliation flag, a status check, a
registry update) is not a judgment output. This definition extends
DEC-38 and ORG-BLUEPRINT.md:445-447 (DEC-20's judgment/routine split for
review depth); it is INFERENCE, because DEC-38 states the exception rule
but does not itself define "judgment output" beyond the W1 examples.

**Applying the rule to every W2 and W3 agent.**

| Agent | Wave | Org tier | Judgment output? | One-line reason | Model tier |
|---|---|---|---|---|---|
| ceo-office | W2 | 1 | — (Tier 1, rule not needed) | Tier 1 is Opus regardless of judgment status. | Opus |
| cco | W2 | 1 | — (Tier 1, rule not needed) | Tier 1 is Opus regardless of judgment status. | Opus |
| coo | W2 | 1 | — (Tier 1, rule not needed) | Tier 1 is Opus regardless of judgment status. | Opus |
| fund-operations-lead | W2 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status. | Sonnet |
| technology-lead | W2 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status. | Sonnet |
| legal-counsel-liaison | W2 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status. | Sonnet |
| investor-relations | W2 | 3 | Yes | Drafts a DDQ answer, a monthly report, or an investor letter: a draft for an external party (definition item 4). | Sonnet |
| compliance-analyst | W2 | 3 | No | Checks a pre-trade log and a sales-material checklist; the cco gives the compliance interpretation, not this agent (ORG-BLUEPRINT.md:118). | Haiku |
| regulatory-reporting-specialist | W2 | 3 | Yes | Drafts the fund-setup report and the quarterly report in §10, both filed to the FSC or FSS: a draft for an external party (definition item 4). | Sonnet |
| operations-analyst | W2 | 3 | No | Automates trade confirmation and flags a reconciliation mismatch: a detection control, not a verdict (ORG-BLUEPRINT.md:483 control 4). | Haiku |
| fund-accountant | W2 | 3 | No | Runs the internal NAV check against the administrator's figure: a detection control; the final NAV stays a human sign-off (ORG-BLUEPRINT.md:484 control 5). | Haiku |
| security-officer | W2 | 3 | No | Monitors system status and backup/disaster-recovery logs: a status check, not a verdict. | Haiku |
| head-of-trading | W3 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status. | Sonnet |
| investor-relations-lead | W3 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status; also drafts external IR material. | Sonnet |
| risk-analytics-lead | W3 | 2 | — (Tier 2, rule not needed) | Tier 2 is Sonnet regardless of judgment status. DEC-38 keeps Opus to cio, cro, and chief-of-staff only. | Sonnet |
| investor-communications-writer | W3 | 3 | Yes | Drafts IR reports that reach investors: a draft for an external party (definition item 4). | Sonnet |
| risk-analyst | W3 | 3 | Ambiguous | Runs a formula-defined stress test (systems-designer donor, Formula Output Format); this reads as routine output, but the result can feed the cro's verdict as an input synthesis. GAP — see Section 5, P2-R-01. | Haiku (default; not settled) |
| governance-secretary | W3 | 3 | Ambiguous | Keeps board and investment-committee minutes, an internal record; but ORG-BLUEPRINT.md:589-592 states these minutes become operational-due-diligence evidence for an institutional investor, an external party. GAP — see Section 5, P2-R-02. | Haiku (default; not settled) |

**Applicability note (F-12, PLAN.md R-10).** P3 measures whether an
agent's `model:` frontmatter field changes the model that actually runs
the agent. PLAN.md:511-512,815. If the field does not apply, every tier
in Section 3 and this section is intent only; every agent then runs on
the session model. `.claude/docs/model-tiers.md` (frontmatter block)
confirms the field is unverified for agents, unlike a skill's `model:`
field, which is confirmed not applied.

## 5. Tool allow-lists (proposed)

**Rules applied to every list below:**

- No agent gets a tool that sends an order or a message to a third
  party. decisions.md:30 (DEC-30); ORG-BLUEPRINT.md:734 (R-14). None of
  the lists in this section include such a tool.
- An agent that needs disclosures or financials gets the OpenDART MCP
  server's tools. decisions.md:31 (DEC-31). This document names the
  server generically. **P3 confirms the exact tool names** once the
  server is wired into the new repository.
- An agent that needs regulation, news, or macro information gets
  WebSearch. decisions.md:31 (DEC-31); ORG-BLUEPRINT.md:670-674 (§11A.7).
- Only data-steward and the analysis scripts (run through Bash) touch
  the gitignored holdings directory. decisions.md:32 (DEC-32). No other
  agent's `tools:` list gives direct file access to that directory; an
  agent that needs a holdings-derived figure gets it from data-steward's
  output or from a script's result, not by reading the directory itself.
- red-team-analyst cannot be delegated the bull case it attacks.
  design-addendum-01.md:66. Its `Agent(...)` list stays empty for this
  reason, not only because §8 names no reports for it.

### 5.1 Wave W1 tool allow-lists

`Agent(...)` follows ORG-BLUEPRINT.md §8's delegation matrix
(ORG-BLUEPRINT.md:421-438), limited to the agents active in W1. cio's
full §8 spawn list also names head-of-trading, quant-research-lead,
quant-researcher, macro-economist, pod-lead, and capital-allocation-support;
these stay out of the W1 list because none of them are active in W1
(W3 or off). chief-of-staff's list is not named in §8 (a new W1 role);
it is INFERENCE, set from its own "reports to" reversed (Section 3.1).

| Agent | `tools:` (proposed) | `Agent(...)` allow-list (proposed) | Note |
|---|---|---|---|
| cio | Read, Glob, Grep, Write, Edit, WebSearch | Agent(portfolio-manager, research-analyst, trader, head-of-research, market-strategist, red-team-analyst) | WebSearch supports the house-view synthesis (DEC-31). W1-active subset of ORG-BLUEPRINT.md:434, plus market-strategist and red-team-analyst: both report to cio (Section 3.1), and cio runs the bull, bear, and synthesis process (addendum §4). The cio never passes a bull case to red-team-analyst as its own work (DEC-16). Advisor addition. |
| cro | Read, Glob, Grep, Write, Edit, Bash, WebSearch, OpenDART MCP server tools | — (empty in W1; §8 names risk-analytics-lead and risk-analyst, both W3) | Bash runs the stress-test and limit scripts (DEC-29). OpenDART supports the 15-year management-participation check and shareholder disclosures (ORG-BLUEPRINT.md:497) — INFERENCE. No direct holdings-directory access (DEC-32). |
| chief-of-staff | Read, Glob, Grep, Write, Edit | Agent(data-steward, cio, cro, market-strategist, head-of-research, portfolio-manager) | INFERENCE: §8 does not name this new role. data-steward reports to it. The other five supply the briefing, the weekly report, and routed /ask answers (addendum §4, §6). chief-of-staff compiles; it does not change a conclusion. Advisor addition. |
| portfolio-manager | Read, Glob, Grep, Write, Edit, Bash | — (empty; no agent names portfolio-manager as its W1 "reports to") | Bash runs the model-portfolio sizing scripts (DEC-29). |
| head-of-research | Read, Glob, Grep, Write, Edit, WebSearch | Agent(research-analyst, idea-screener) | §8's reversed-reports-to row (ORG-BLUEPRINT.md:438); both reports are W1-active. |
| market-strategist | Read, Glob, Grep, Write, Edit, WebSearch, Bash | — (empty) | WebSearch for macro, rates, FX, flows, regime (DEC-31). Bash for indicator calculation scripts — INFERENCE, by analogy to DEC-29's calculation-script rule. |
| research-analyst | Read, Glob, Grep, Write, Edit, WebSearch, OpenDART MCP server tools, Bash | — (empty) | OpenDART for the financial-analysis section of /stock-pitch (DEC-31). Bash for the valuation-section scripts — INFERENCE, by analogy to DEC-29. |
| red-team-analyst | Read, Glob, Grep, Write, Edit, WebSearch, OpenDART MCP server tools, Bash | — (empty; see the rule above) | Needs the same source access as research-analyst to attack the case independently. |
| idea-screener | Read, Glob, Grep, Write, Bash, OpenDART MCP server tools | — (empty) | Bash runs the valuation, earnings, and event screens (DEC-29, an explicit "screens" match). |
| data-steward | Read, Glob, Grep, Write, Edit, Bash, WebSearch, OpenDART MCP server tools | — (empty) | The only W1 agent with direct access to the gitignored holdings directory, alongside the analysis scripts it runs through Bash (DEC-32). |
| trader | Read, Glob, Grep, Write, Bash | — (empty) | No order-side tool (DEC-30). Bash runs TCA and cost scripts — INFERENCE. No WebSearch or OpenDART: execution information comes from exchange or broker data (DEC-31), not disclosures or web search. |

### 5.2 Wave W2/W3 tool allow-lists — INFERENCE, by function

W2 and W3 agent files are not yet drafted; P3 and later phases confirm
the exact list per agent. This table groups the 18 W2/W3 agents by
function and gives a proposed baseline, marked INFERENCE throughout.

| Function | Agents | `tools:` baseline (INFERENCE) | Note |
|---|---|---|---|
| Firm management and operations | ceo-office, coo, fund-operations-lead, operations-analyst | Read, Glob, Grep, Write, Edit, Bash | No OpenDART or WebSearch by default; add per-agent if a role needs external filings or market news. |
| Compliance and legal | cco, compliance-analyst, regulatory-reporting-specialist, legal-counsel-liaison | Read, Glob, Grep, Write, Edit, WebSearch | WebSearch for regulation and rule changes (DEC-31). No OpenDART baseline; regulatory-reporting-specialist adds it if a filing needs company-level data. |
| IR and investor communications | investor-relations, investor-relations-lead, investor-communications-writer | Read, Glob, Grep, Write, Edit, WebSearch | No order- or message-sending tool (DEC-30, R-14); a draft stays a draft until the founder sends it. |
| Technology and security | technology-lead, security-officer | Read, Glob, Grep, Write, Edit, Bash | No holdings-directory access baseline (DEC-32); add only if a specific task needs it, logged per DEC-32's reason requirement. |
| Fund accounting | fund-accountant | Read, Glob, Grep, Write, Edit, Bash | Bash runs the shadow-NAV and fee-calculation scripts. |
| Risk (W3) | risk-analytics-lead, risk-analyst | Read, Glob, Grep, Write, Edit, Bash, WebSearch, OpenDART MCP server tools | Mirrors the W1 cro list (Section 5.1); risk-analyst's exact list depends on P2-R-01 (Section 6). |
| Trading (W3) | head-of-trading | Read, Glob, Grep, Write, Bash | No order-side tool (DEC-30), matching the W1 trader row. |
| Governance (W3) | governance-secretary | Read, Glob, Grep, Write, Edit | Minutes and succession tracking; no external-data tool baseline. |

## 6. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-R-01 | What model tier applies to risk-analyst (Tier 3, W3)? | **A.** Haiku — the role runs formula-defined stress tests (systems-designer donor shape); no recommendation, verdict, synthesis, external draft, or legal interpretation. **B.** Sonnet — the role's stress-test output is an input synthesis that feeds the cro's verdict, close enough to "synthesis" to count. **C.** Ask the cro to state, per output type, which risk-analyst products count as a synthesis and which stay formula output. **D.** Match risk-analytics-lead's tier (Sonnet) for consistency across the risk function, regardless of the judgment test. | Recommend **A** (Haiku), with **C** as a fallback if the founder wants finer control. Reason: ORG-BLUEPRINT.md:284 cites the systems-designer "Formula Output Format" donor, the same donor as market-strategist's indicator work, which this document does not treat as a synthesis. Source: ORG-BLUEPRINT.md:284; Section 4 (this document). |
| P2-R-02 | What model tier applies to governance-secretary (Tier 3, W3)? | **A.** Haiku — minutes and succession tracking are an internal record, not a recommendation, verdict, or external draft. **B.** Sonnet — ORG-BLUEPRINT.md:589-592 states investment-committee minutes become operational-due-diligence evidence for an institutional investor, which reads as a draft that reaches an external party. **C.** Sonnet only for investment-committee minutes; Haiku for board minutes and succession tracking (a split by output). **D.** Ask whether wave-W3 minutes will in fact reach an institutional investor before the fund has one (W3 triggers at growth stage 2-3, ORG-BLUEPRINT.md:325-328, ahead of most external due diligence). | Recommend **A** (Haiku), because W3 activates before the fund has outside investors in most growth paths, so the ODD-evidence use is a future case, not a current one; **D** narrows this further if the founder wants it checked against the growth-stage plan. Source: ORG-BLUEPRINT.md:325-328, 589-592. |
| P2-R-03 | Do research-analyst instances (one per sector cluster, DEC-11) all run at once, or on demand? | **A.** All 6 clusters run on every /weekly-report and /idea-screen cycle, whether or not a cluster has a live idea. **B.** Only clusters with an open idea or a coverage-universe event run; the others stay idle until data-steward's event-alert or idea-screener's ranked list flags one. **C.** A hybrid: all 6 run on a weekly cadence for /weekly-report, but only the flagged cluster runs on demand for /stock-pitch. **D.** The founder sets the run mode per cluster in `project.yaml` coverage config, so the mode can change without a code change. | No recommendation (founder judgment). This is a cost-versus-coverage trade-off the loaded chunks do not address; DEC-11 sets one instance per cluster (ORG-BLUEPRINT.md:93, addendum §5) but not a run cadence. Source: decisions.md:11; ORG-BLUEPRINT.md:637-650 (§11A.3); design-addendum-01.md:95-106 (§5). |

## Founder decisions recorded (2026-09-25)

The founder answered the items above. HFT-P2-00 §4 is the register; §4A states the consequences.

| ID | Answer |
|---|---|
| P2-R-01 | A: Haiku |
| P2-R-02 | A: Haiku |
| P2-R-03 | C: hybrid. All 6 clusters run once a week for the weekly report; at other times only a cluster with a signal runs |

## 7. Traceability

| P2 task / DEC-NN | Covered in |
|---|---|
| P2 task 1 (finalize the wave roster) | Section 3 |
| P2 task 9 (map every W2/W3 agent to a model tier) | Section 4 |
| DEC-09, DEC-13 (mission, wave split) | Section 2, Section 3 |
| DEC-10 (cro/cco reporting line) | Section 3.1, Section 3.2 |
| DEC-11 (sector-cluster instances) | Section 3.1 (row 7); Section 6 (P2-R-03) |
| DEC-16 (bull/bear/synthesis) | Section 3.1 (rows 1, 7, 8) |
| DEC-17, DEC-18, DEC-20 (control seats, review depth, judgment/routine split) | Section 4 (judgment-output definition) |
| DEC-29 (Q25 = B, conditional agents off) | Section 3.4 |
| DEC-30, R-14 (no order or third-party message tool) | Section 5 (rule list) |
| DEC-31 (OpenDART, exchange/broker data, WebSearch) | Section 5.1, Section 5.2 |
| DEC-32 (gitignored holdings directory) | Section 5 (rule list), Section 5.1 (data-steward, cro, trader rows) |
| DEC-36 (draft needs no approval) | Section 1, Section 2 |
| DEC-38, F-12, PLAN.md R-10 (model tiers, applicability measurement) | Section 4 |
| Erratum 01 (ceo-office stays in W2; 11/23/29) | Section 3.2, Section 3 count check |
