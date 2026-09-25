# HFT-P2-06: Korean-English term map

## 1. Document control

| Field | Value |
|---|---|
| Document ID | HFT-P2-06 |
| Title | Korean-English term map |
| Version | 1.0 |
| Date | 2026-09-25 |
| Status | Approved by the founder (AR-P2-0001, 2026-09-25) |
| Owner | Advisor (main session) |
| Author | Worker |
| Inputs | [ORG-BLUEPRINT.md](../ORG-BLUEPRINT.md) §3-§6; [QUESTIONS.md](../QUESTIONS.md) §6 (용어 설명); [PLAN.md](../PLAN.md) Appendix B; report chunks under `docs/hedge-fund-setup/ref/` (HF-REF-02, 04, 05, 06, 08, 09, 19) |
| Writing standard | ASD-STE100 |

This document covers P2 task 6 (PLAN.md §8, P2, task 6): "Build the
Korean-English term map for shared documents."

## 2. Use rule (read this before the tables)

DEC-33 sets the general split: ASD-STE100 English for agents, skills,
rules, and procedures; Korean for briefings, reports, on-demand
answers, alerts, the dashboard, and regulatory and investor documents.

Three exceptions narrow that split:

1. **Organization and legal role names stay Korean everywhere,
   including inside an English technical document.** ORG-BLUEPRINT.md
   states its own rule: "Keep the Korean role name as the technical
   name. An English gloss follows the first use" (ORG-BLUEPRINT.md:104).
   Table 3-1 and Table 4-1 below carry that rule in their Use rule
   column.
2. **Verdict words stay English everywhere, including inside a Korean
   information product.** "판정 어휘는 PASS, CONCERNS, FAIL, NOT ASSESSED
   네 가지로 통일합니다" (QUESTIONS.md:963): the gate vocabulary stays as
   these four English words, with no Korean gloss.
3. **A skill or command name (`/daily-briefing`, `/house-view`, and so
   on) stays English and unglossed everywhere.** It is a technical
   identifier, the same way a file path stays unglossed. The Korean
   term in Table 6-1 below names the delivered product, not the
   command that generates it.

Every other row uses the DEC-33 split: the Korean term in a Korean
information product; the English term in a technical document.

## 3. Organization roles (ORG-BLUEPRINT.md §3)

The Korean role name is the technical name (§2 rule 1). Citation for
every row: HF-REF-08 표 6-1, unless the row states a different one
(ORG-BLUEPRINT.md:130-132).

**Table 3-1. Organization functions**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| Chief executive officer (CEO) | 대표이사(CEO) | This role runs the firm, manages external relations, and raises capital. | ORG-BLUEPRINT.md:112; HF-REF-05 표 4-1 | Korean term is the technical name, in every document. |
| Chief investment officer (CIO) | 최고투자책임자(CIO) | This role sets investment philosophy, makes the final portfolio decision, and sets the risk budget. | ORG-BLUEPRINT.md:113; HF-REF-05 표 4-1 | Korean term is the technical name, in every document. |
| Portfolio manager (PM) | 포트폴리오 매니저(PM)·운용역 | This role runs a strategy or book and owns the performance result. | ORG-BLUEPRINT.md:114; HF-REF-05 표 4-1 | Korean term is the technical name, in every document. |
| Analyst / quant researcher | 애널리스트·퀀트 리서처 | This role analyzes companies, industries, and research models. | ORG-BLUEPRINT.md:115 | Korean term is the technical name, in every document. |
| Trader | 트레이더 | This role executes orders and manages stock loans and liquidity. | ORG-BLUEPRINT.md:116 | Korean term is the technical name, in every document. |
| Chief risk officer (CRO) | 위험관리 담당(CRO) | This role sets and checks limits, runs stress tests, and manages liquidity, with a reporting line separate from the CIO. | ORG-BLUEPRINT.md:117; HF-REF-06 §4.5 | Korean term is the technical name, in every document. See §4 for the legal-role form, 위험관리책임자, and P2-T-02. |
| Compliance officer (CCO) | 준법감시인(CCO) | This role sets internal-control standards, manages conflicts of interest, and handles regulatory reporting. It must not also do asset management. | ORG-BLUEPRINT.md:118; HF-REF-06 §4.5 | Korean term is the technical name, in every document. |
| Operations | 오퍼레이션 | This role confirms trades, settles trades, and reconciles balances between the firm, the prime broker, and the custodian. | ORG-BLUEPRINT.md:119 | Korean term is the technical name, in every document. |
| Fund accounting / NAV internal check | 펀드 회계·기준가(내부검증) | This role checks the NAV result the administrator computes. | ORG-BLUEPRINT.md:120 | Korean term is the technical name, in every document. |
| CFO / COO | CFO·COO | This role runs firm accounting, budget, HR, and contract management. | ORG-BLUEPRINT.md:121 | English abbreviation is the technical name in this row; no separate Korean role name is stated in the chunk. |
| IT, data, and security | IT·데이터·보안 | This role runs systems, manages data, and handles cybersecurity and business continuity. | ORG-BLUEPRINT.md:122 | Korean/English mixed label is the technical name, in every document. |
| Investor relations / marketing (IR) | IR·마케팅 | This role manages investor relations, works with the distributor, and answers due-diligence questionnaires. | ORG-BLUEPRINT.md:123 | Korean/English mixed label is the technical name, in every document. |
| Legal | 법무 | This role reviews fund rules and contracts, normally through an outside law firm. | ORG-BLUEPRINT.md:124 | Korean term is the technical name, in every document. |
| Board and auditor | 이사회·감사 | This role sits at the top of the org chart and oversees the CEO. | ORG-BLUEPRINT.md:125 | Korean term is the technical name, in every document. |
| Investment committee (IC) | 투자위원회 | This body keeps minutes and the decision record when it runs, as investment-discipline evidence. | ORG-BLUEPRINT.md:126; HF-REF-09 §7.1 | Korean term is the technical name, in every document. See Table 6-1 for the agent-organization form, 가상 투자위원회. |
| Asset valuation committee | 자산 평가 위원회 | This body runs the valuation rule that stops overvaluation of a non-marketable or distressed asset. | ORG-BLUEPRINT.md:127 | Korean term is the technical name, in every document. |
| Capital allocation committee | 자본배분위원회 | This body decides capital allocation per trading pod. It applies only to a multi-manager archetype. | ORG-BLUEPRINT.md:128 | Korean term is the technical name, in every document. Not applicable: DEC-05 selected the single-manager fundamental archetype. |

## 4. Legal roles (ORG-BLUEPRINT.md §4; law text)

**Table 4-1. Legal roles**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| Investment-management staff (professional) | 투자운용인력 | The law requires 3 or more full-time staff in this role, at a registered general private fund manager. | HF-REF-05 표 4-1; `docs/hedge-fund-setup/ref/05-kr-registration-and-roadmap.md:31,42`; 시행령 제271조의2 제4항 제1호 | Korean term is the technical name, in every document. |
| Compliance officer | 준법감시인 | This statutory role sets internal-control standards. The law forbids combining it with asset management. | HF-REF-06 §4.5; `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:65`; Act on Corporate Governance of Financial Companies | Korean term is the technical name, in every document. Same role as Table 3-1's 준법감시인(CCO). |
| Risk management officer | 위험관리책임자 | This role sets limits, runs stress tests, and reports independently of the CIO. The law lets a small firm combine it with the compliance-officer role, after legal review. | HF-REF-06 §4.5; `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:65`; QUESTIONS.md:950 | Korean term is the technical name, in the law-citing form. ORG-BLUEPRINT.md uses 위험관리 담당(CRO) as the organization-chart label for the same role (Table 3-1). See P2-T-02. |

## 5. Fund terms (report chunks)

**Table 5-1. Fund and regulatory terms**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| General private fund (the current legal name for a Korean hedge fund) | 일반 사모펀드 (일반 사모집합투자기구) | Since the 2021 reform, the law classifies a private fund by investor type (general or institution-only), not by purpose. This is the hedge fund's current legal name. | `docs/hedge-fund-setup/ref/02-industry-and-market.md:25` (HF-REF-02) | Use this term in every Korean information product and every technical document. This is the fund type DEC-05 and DEC-07 point to (Korea-first, single-manager fundamental). |
| Professional-purpose private fund (superseded classification) | 전문투자형 사모펀드 | This was the pre-2021 classification, by fund purpose (professional-purpose versus management-participation). The 2021 reform replaced it with the investor-based classification above. | `docs/hedge-fund-setup/ref/02-industry-and-market.md:25` (HF-REF-02) | Historical or legal-history reference only. Do not use it as the fund's current legal name. See P2-T-04. |
| Net asset value (NAV) / reference price | NAV / 기준가(격) | This is the fund's net assets divided by its unit count. An independent administrator computes it; the firm checks it separately. | QUESTIONS.md:955 (HF-REF-19); `docs/hedge-fund-setup/ref/04-legal-structure.md:39,51` (HF-REF-04) | Use 기준가 or 기준가격 in a Korean information product. Use NAV in a technical document. |
| Leverage | 레버리지 | The sum of derivative risk value, guarantees, borrowings, and effective borrowing must stay at or under 400% of net assets. | `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:31` (HF-REF-06 §4.3 표 4-3); 자본시장법 제249조의7 제1항 | Use 레버리지 in a Korean information product. Use leverage in a technical document. |
| Short selling | 공매도 | Korea fully reopened short selling on 2025-03-31, with a mandatory balance-management system to prevent naked short selling. | `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:45-49` (HF-REF-06 §4.4) | Use 공매도 in a Korean information product. Use short selling in a technical document. |
| Securities transaction tax | 증권거래세 | This tax is 0.20% of the sale amount for a KOSPI or KOSDAQ trade, from 2026-01-01. A high-turnover strategy must budget for it. | `docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:77` (HF-REF-06 §4.6) | Use 증권거래세 in a Korean information product. Use securities transaction tax in a technical document. |

## 6. Control terms (PLAN.md, QUESTIONS.md)

**Table 6-1. Control-model terms**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| PASS / CONCERNS / FAIL / NOT ASSESSED (verdict words) | (none, stays English) | This is the one gate-verdict vocabulary. A gate uses exactly these four words. | QUESTIONS.md:963; PLAN.md P-09 (line 387) | Stays English in every document, including a Korean information product (§2 rule 2). |
| Approval receipt | 승인 기록 | This is a recorded, hashed approval for a protected-path change, a stage advance, a final-status change, or a commit. It names the approver's role and the content hash. | PLAN.md Appendix B (lines 905-907); QUESTIONS.md:966 | Use 승인 기록 in a Korean information product. Use approval receipt in a technical document. |
| Pre-screen | 사전 검토 (INFERENCE) | An agent's review of another agent's work, in the same session, is not an independent review. A human with an independent reporting line must still sign. | PLAN.md Appendix B (lines 895-897), F-09 | No Korean term is stated in the loaded chunks or QUESTIONS.md. Proposed term is INFERENCE. See P2-T-03. |
| Fixed control seat | 통제 좌석 | This is the cro or cco role. It stays active in every gate, whatever `team.size`, `modes.review_mode`, or `modes.workflow` is set to. | QUESTIONS.md:964; F-04, F-05, F-06 | Use 통제 좌석 in a Korean information product. Use fixed control seat (or fixed seat) in a technical document. |
| NOT ASSESSED | (none, stays English) | A control decision with no approval receipt reads NOT ASSESSED, not FAIL. | PLAN.md Appendix B (lines 901-904); QUESTIONS.md:963 | Stays English everywhere (§2 rule 2); it is one of the four verdict words above. |

## 7. Product terms (ORG-BLUEPRINT.md §11A; addendum §6; QUESTIONS.md)

**Table 7-1. W1 information-product terms**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| Daily briefing | 일간 브리핑 | This is the one-page daily product: market, portfolio, risk, and watch-list events. | QUESTIONS.md:477, 596; ORG-BLUEPRINT.md:602 | Use 일간 브리핑 for the delivered product in a Korean information product. The command `/daily-briefing` stays unglossed (§2 rule 3). |
| House view | 하우스 뷰 | This is the organization's combined view of market direction: a base scenario, a bear case, and a CIO synthesis with a confidence level. | QUESTIONS.md:969 | Use 하우스 뷰 for the delivered product in a Korean information product. The command `/house-view` stays unglossed. |
| Bull case | 강세 논거 | This is the case for a stock or a market direction, written before the bear case and the synthesis. | QUESTIONS.md:386 | Use 강세 논거 in a Korean information product. Use bull case in a technical document. |
| Bear case | 약세 논거 | This is the case against a bull case or a house-view change, written by the red-team-analyst, who must not also be the bull case's author. | QUESTIONS.md:386, 970 (DEC-16) | Use 약세 논거 in a Korean information product. Use bear case in a technical document. |
| CIO synthesis | CIO 종합 | This is the cio's synthesis of the bull case and the bear case, with a confidence level and open questions for the user. | QUESTIONS.md:386, 477 | Use CIO 종합 in a Korean information product. The command `/cio-synthesis` stays unglossed. |
| Virtual investment committee | 가상 투자위원회 | This body seats the cio, cro, portfolio-manager, and red-team-analyst agents. Each presents a review; the user decides; minutes are kept. | QUESTIONS.md:520 (DEC-22) | Use 가상 투자위원회 in a Korean information product. Use virtual investment committee in a technical document. Not the same body as Table 3-1's 투자위원회 (a human committee). |
| Call record | 콜 기록 | This record tracks every stock call's and house-view change's direction, target, and deadline, against the later outcome. | QUESTIONS.md:971 (DEC-24) | Use 콜 기록 in a Korean information product. The command `/call-review` stays unglossed. |
| Model portfolio | 모의 포트폴리오 | This is a hypothetical portfolio that records the agent organization's calls, tracked against a benchmark. Agents record positions here; they never draft or send a live order. | QUESTIONS.md:553, 930 (DEC-24, DEC-30) | Use 모의 포트폴리오 in a Korean information product. Use model portfolio in a technical document. |

## 8. Wave and stage terms (ORG-BLUEPRINT.md §11; addendum §3; QUESTIONS.md)

**Table 8-1. Wave and lifecycle-stage terms**

| English term | Korean term | Definition | Source | Use rule |
|---|---|---|---|---|
| Activation wave | 활성화 웨이브 | This concept replaces "activation stage." It turns on a set of agents and skills together, on the trigger the wave states, not on a fixed organization-stage schedule. | QUESTIONS.md:968 (DEC-13) | Use 활성화 웨이브 in a Korean information product. Use activation wave in a technical document. |
| Wave W1, information core | W1(정보 핵심) | This wave is the 11-agent information core. It turns on now. | QUESTIONS.md:968; evidence/design-addendum-01.md:54 | Use W1(정보 핵심) in a Korean information product. Use "wave W1" or "the information core" in a technical document. |
| Wave W2, fund operation | W2(펀드 운영) | This wave adds compliance, operations, NAV check, IR, and regulatory-reporting functions. It turns on when the founder starts fund setup (setup stage S1). | QUESTIONS.md:968; evidence/design-addendum-01.md:55 | Use W2(펀드 운영) in a Korean information product. Use "wave W2" or "fund operation" in a technical document. |
| Wave W3, institutionalization | W3(기관화) | This wave adds dedicated teams and governance roles. It turns on at growth stage 2 or 3. | QUESTIONS.md:968; evidence/design-addendum-01.md:56 | Use W3(기관화) in a Korean information product. Use "wave W3" or "institutionalization" in a technical document. |
| Setup stage (axis) | 설립 단계 | This is the S1-S8 axis: business design through the first fund launch. It starts when the founder starts fund setup. | ORG-BLUEPRINT.md:531; QUESTIONS.md:485, 490 | Use 설립 단계 in a Korean information product. Use "setup stage" in a technical document. The 8 individual stage names (S1 사업 설계 to S8 첫 펀드 설정) are already Korean-labeled at ORG-BLUEPRINT.md:538-545; this table does not repeat them. |
| Growth stage (axis) | 성장 단계 | This is the G1-G3 axis: founding stage through institutionalization. | ORG-BLUEPRINT.md:547; QUESTIONS.md:490 | Use 성장 단계 in a Korean information product. Use "growth stage" in a technical document. The 3 individual stage names (G1 설립기 to G3 기관화) are already Korean-labeled at ORG-BLUEPRINT.md:553-555; this table does not repeat them. |

## 9. New mission-reset agent roles (ORG-BLUEPRINT.md §6, rows 33-37)

These 5 agents have no HF-REF chunk and no Korean role name in the
source documents (ORG-BLUEPRINT.md:298-302: "Not in HF-REF — new role
for the mission reset"). Table 9-1 proposes a Korean gloss for each,
for use only where a Korean information product needs to name the
producing agent (for example, a briefing's byline). Every term in this
table is INFERENCE.

**Table 9-1. New agent roles (INFERENCE)**

| English term | Proposed Korean term (INFERENCE) | Definition | Source | Use rule |
|---|---|---|---|---|
| chief-of-staff | 수석보좌역 (INFERENCE) | This agent writes the daily briefing and the weekly report, and routes on-demand questions to the right agent. | ORG-BLUEPRINT.md:298 | No source Korean term. Proposed gloss needs founder approval before use in a Korean product (P2-T-01). The agent ID `chief-of-staff` stays unglossed in a technical document (§2 rule 3). |
| market-strategist | 시장전략가 (INFERENCE) | This agent writes market analysis: macro, rates, FX, flows, and the KOSPI/KOSDAQ regime. | ORG-BLUEPRINT.md:299 | Same rule as chief-of-staff. See P2-T-01. |
| red-team-analyst | 레드팀 애널리스트 (INFERENCE, partly sourced) | This agent writes the bear case against every stock call and house-view change. | ORG-BLUEPRINT.md:300; QUESTIONS.md:970 ("레드팀" is sourced; "애널리스트" suffix is INFERENCE) | Same rule as chief-of-staff. See P2-T-01. |
| idea-screener | 종목 스크리너 (INFERENCE) | This agent runs valuation, earnings, and event screens that feed the sector analysts. | ORG-BLUEPRINT.md:301 | Same rule as chief-of-staff. See P2-T-01. |
| data-steward | 데이터 스튜어드 (INFERENCE) | This agent owns the data-source registry, adapters, and coverage config. | ORG-BLUEPRINT.md:302 | Same rule as chief-of-staff. See P2-T-01. |

## 10. Founder decisions needed

| ID | Question | Options | Recommendation |
|---|---|---|---|
| P2-T-01 | Table 9-1 proposes a Korean gloss for the 5 new mission-reset agent roles (chief-of-staff, market-strategist, red-team-analyst, idea-screener, data-steward). No source document gives one. Does the founder approve these glosses before a Korean information product uses them (for example, a briefing byline)? | A: approve Table 9-1 as written. B: approve with changes the founder specifies. C: use the English agent ID even in a Korean product (no Korean gloss at all). D: decide this later, when the first Korean product ships (P7 dry run). | No recommendation (founder judgment). The names carry no legal or regulatory weight; the choice is a style preference. Source: ORG-BLUEPRINT.md:298-302 (no HF-REF basis). |
| P2-T-02 | ORG-BLUEPRINT.md's organization chart uses 위험관리 담당(CRO); the law-citing chunk and the QUESTIONS.md glossary use 위험관리책임자. Which form does a Korean information product use for the CRO's byline or citation? | A: 위험관리 담당, matching the org chart. B: 위험관리책임자, matching the law-citing chunk. C: use both, with 위험관리책임자 only in a regulatory-filing context. D: founder picks a different form. | C. The chunk itself uses 위험관리책임자 only when citing the statutory basis (`docs/hedge-fund-setup/ref/06-kr-fund-rules-controls-tax.md:65`); ORG-BLUEPRINT.md's own org chart and roster use 위험관리 담당(CRO) everywhere else. Source: ORG-BLUEPRINT.md:117, 194-195; QUESTIONS.md:950. |
| P2-T-03 | Table 6-1 proposes 사전 검토 as the Korean gloss for "pre-screen." No source document gives a Korean term for this control concept. Does the founder approve it? | A: approve 사전 검토. B: approve a different term the founder specifies. C: leave "pre-screen" unglossed, English-only, like the verdict words. | No recommendation (founder judgment). This term appears mainly in technical control documents (English, DEC-33), so the practical impact of the gloss is low; it matters only if a Korean-language control note ever needs it. Source: PLAN.md Appendix B, lines 895-897 (F-09). |
| P2-T-04 | Table 5-1 recommends 일반 사모펀드 as the only current-usage term, and marks 전문투자형 사모펀드 historical-reference-only. Does the founder confirm this rule for every Korean information product and every technical document? | A: confirm as recommended. B: allow 전문투자형 사모펀드 in an investor-facing document too, since some investors may still use the older term informally. C: founder sets a different rule. | A. The 2021 reform replaced the purpose-based classification with the investor-based one; using the superseded term as a current label risks a compliance or investor-communication error. Source: `docs/hedge-fund-setup/ref/02-industry-and-market.md:25` (HF-REF-02). |

## Founder decisions recorded (2026-09-25)

The founder answered the items above. HFT-P2-00 §4 is the register; §4A states the consequences.

| ID | Answer |
|---|---|
| P2-T-01 | A: 수석보좌역, 시장전략가, 레드팀 애널리스트, 종목 스크리너, 데이터 스튜어드 |
| P2-T-02 | C: by context, as recommended |
| P2-T-03 | A: 사전 검토 |
| P2-T-04 | A: 일반 사모펀드 only |

## 11. Traceability

| P2 task / DEC-NN | Covered in |
|---|---|
| P2 task 6 (build the Korean-English term map) | §3-§10 |
| ORG-BLUEPRINT.md §3-§6 (organization roles, including Korean role names) | §3, §9 |
| Legal roles (투자운용인력, 준법감시인, 위험관리책임자) | §4 |
| Fund terms (전문투자형/일반 사모펀드, NAV/기준가, 레버리지, 공매도, 증권거래세) | §5 |
| Control terms (verdict words, approval receipt, pre-screen, fixed seat, NOT ASSESSED) | §6 |
| Product terms (daily briefing, house view, bull/bear case, CIO synthesis, virtual investment committee, call record, model portfolio) | §7 |
| Wave and stage terms | §8 |
| DEC-33 (document language) | §2 |
| DEC-16 (bull case, bear case, CIO synthesis) | §7 |
| DEC-22 (virtual investment committee) | §7 |
| DEC-24 (call record, model portfolio) | §7 |
| DEC-30 (agents never draft or send an order) | §7 (model portfolio row) |
| DEC-13 (activation waves replace activation stage) | §8 |
| DEC-17 (approval receipt) | §6 |
| DEC-18 (fixed control seats) | §6 |
