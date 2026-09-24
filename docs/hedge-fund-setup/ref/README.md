# Hedge Fund Setup Report — Reference Chunks

This index describes the chunk set in this folder. Read it before you load
any chunk.

## Purpose

These files are extracts from `hedge_fund_setup_report.md`. The source
report is long. One chunk covers one topic area. An AI agent loads only the
chunks that its domain needs. This keeps context small. This keeps context
relevant.

## How to use

1. Read this index first.
2. Find your domain in the domain table.
3. Load only the chunks that it lists.
4. Check volatility and as_of.
5. Re-verify medium or high values before use.
6. Cite as `HF-REF-NN §x.y`.

## Chunk table

| id | file | title | source lines | bytes | volatility | domains |
|---|---|---|---|---|---|---|
| HF-REF-00 | [00-front-matter.md](00-front-matter.md) | 헤지펀드 운용사 설립 가이드 | 1-28 | 2,120 | low | glossary |
| HF-REF-01 | [01-executive-summary.md](01-executive-summary.md) | 핵심 요약 | 29-58 | 3,949 | high | market-data, registration, constraints, governance |
| HF-REF-02 | [02-industry-and-market.md](02-industry-and-market.md) | 1. 헤지펀드의 정의와 산업 현황 | 59-135 | 9,064 | high | market-data, fund-regulation |
| HF-REF-03 | [03-founding-decisions.md](03-founding-decisions.md) | 2. 설립 전 핵심 의사결정 | 136-205 | 8,114 | medium | strategy, offshore, fundraising-ir |
| HF-REF-04 | [04-legal-structure.md](04-legal-structure.md) | 3. 법적 구조 | 206-270 | 6,006 | low | legal-structure, service-providers |
| HF-REF-05 | [05-kr-registration-and-roadmap.md](05-kr-registration-and-roadmap.md) | 4. 국내 설립 절차 | 271-332 | 5,461 | medium | registration, organization |
| HF-REF-06 | [06-kr-fund-rules-controls-tax.md](06-kr-fund-rules-controls-tax.md) | 4.3 펀드 설정과 운용 규제 | 333-397 | 8,501 | medium | fund-regulation, short-selling, internal-control, tax |
| HF-REF-07 | [07-offshore-setup.md](07-offshore-setup.md) | 5. 해외 설립 절차 | 398-447 | 6,549 | medium | offshore, fund-regulation |
| HF-REF-08 | [08-organization.md](08-organization.md) | 6. 조직도 | 448-537 | 8,072 | low | organization, governance, compensation |
| HF-REF-09 | [09-investment-risk-execution.md](09-investment-risk-execution.md) | 7. 운영 방식 | 538-583 | 4,771 | low | investment-process, risk, trading |
| HF-REF-10 | [10-operations-and-providers.md](10-operations-and-providers.md) | 7.4 오퍼레이션과 기준가 산정 | 584-614 | 2,989 | medium | operations, service-providers |
| HF-REF-11 | [11-fees-and-fundraising.md](11-fees-and-fundraising.md) | 7.6 보수 구조 | 615-642 | 4,408 | high | fees, fundraising-ir |
| HF-REF-12 | [12-technology-infrastructure.md](12-technology-infrastructure.md) | 7.8 기술 인프라 | 643-659 | 1,686 | low | technology, risk |
| HF-REF-13 | [13-firm-economics.md](13-firm-economics.md) | 7.9 운용사 손익 구조와 손익분기 (예시) | 660-697 | 3,109 | low | firm-economics |
| HF-REF-14 | [14-constraints-and-risks.md](14-constraints-and-risks.md) | 8. 제약 조건과 리스크 | 698-760 | 8,108 | medium | constraints, risk, failure-lessons |
| HF-REF-15 | [15-benchmark-rankings.md](15-benchmark-rankings.md) | 9. 세계 최고 헤지펀드 벤치마크 | 761-819 | 5,288 | high | benchmark, market-data |
| HF-REF-16 | [16-benchmark-operating-models.md](16-benchmark-operating-models.md) | 9.3 운용사별 운영 모델 분석 | 820-868 | 10,590 | high | benchmark, governance |
| HF-REF-17 | [17-success-factors.md](17-success-factors.md) | 9.5 공통 성공 요인과 설립 시사점 | 869-884 | 2,081 | low | benchmark, governance, risk |
| HF-REF-18 | [18-execution-checklist.md](18-execution-checklist.md) | 10. 실행 체크리스트 | 885-908 | 2,375 | low | checklist, registration |
| HF-REF-19 | [19-glossary.md](19-glossary.md) | 부록 | 909-943 | 3,051 | low | glossary |
| HF-REF-20 | [20-sources.md](20-sources.md) | 부록 B. 참고 자료 | 944-1013 | 10,672 | medium | sources |

## Domain table

Find your domain. Load only the listed chunk ids.

| domain | chunk ids |
|---|---|
| benchmark | HF-REF-15, HF-REF-16, HF-REF-17 |
| checklist | HF-REF-18 |
| compensation | HF-REF-08 |
| constraints | HF-REF-01, HF-REF-14 |
| failure-lessons | HF-REF-14 |
| fees | HF-REF-11 |
| firm-economics | HF-REF-13 |
| fund-regulation | HF-REF-02, HF-REF-06, HF-REF-07 |
| fundraising-ir | HF-REF-03, HF-REF-11 |
| glossary | HF-REF-00, HF-REF-19 |
| governance | HF-REF-01, HF-REF-08, HF-REF-16, HF-REF-17 |
| internal-control | HF-REF-06 |
| investment-process | HF-REF-09 |
| legal-structure | HF-REF-04 |
| market-data | HF-REF-01, HF-REF-02, HF-REF-15 |
| offshore | HF-REF-03, HF-REF-07 |
| operations | HF-REF-10 |
| organization | HF-REF-05, HF-REF-08 |
| registration | HF-REF-01, HF-REF-05, HF-REF-18 |
| risk | HF-REF-09, HF-REF-12, HF-REF-14, HF-REF-17 |
| service-providers | HF-REF-04, HF-REF-10 |
| short-selling | HF-REF-06 |
| sources | HF-REF-20 |
| strategy | HF-REF-03 |
| tax | HF-REF-06 |
| technology | HF-REF-12 |
| trading | HF-REF-09 |

## Source table

Each source has an id, SRC-01 to SRC-63. HF-REF-20 holds the full table
with links. This table shows which content chunks (HF-REF-01 to HF-REF-19)
cite each source. HF-REF-20 cites all 63 by definition, so it is left out
of the "cited by" column below.

| SRC id | category | short title | cited by |
|---|---|---|---|
| SRC-01 | 국내 법령 | 자본시장법 제249조~제249조의18 | HF-REF-01, HF-REF-03, HF-REF-04, HF-REF-05, HF-REF-06, HF-REF-09, HF-REF-18 |
| SRC-02 | 국내 법령 | 시행령 제271조의2 (등록요건) | HF-REF-01, HF-REF-05, HF-REF-18 |
| SRC-03 | 국내 제도 | 금융위, 사모펀드 하위규정 시행 (2021) | HF-REF-03, HF-REF-06 |
| SRC-04 | 국내 제도 | 김·장, 자본시장법 개정 해설 | HF-REF-05 |
| SRC-05 | 국내 제도 | 아주경제, 최소 투자금 Q&A | HF-REF-01 |
| SRC-06 | 국내 제도 | 메트로서울, 투자자 100인 확대 | HF-REF-06 |
| SRC-07 | 공매도 | 금융위, 공매도 전면 재개 | HF-REF-01, HF-REF-03, HF-REF-06 |
| SRC-08 | 공매도 | 금융위, 공매도 법규 개정 완료 | HF-REF-06 |
| SRC-09 | 공매도 | 금융위, 공매도 시행령 입법예고 | HF-REF-06, HF-REF-09 |
| SRC-10 | 공매도 | 자본시장연구원, 공매도 제도개선 | HF-REF-06, HF-REF-09 |
| SRC-11 | 세제 | 삼일PwC, 증권거래세 개정 해설 | HF-REF-01, HF-REF-03, HF-REF-06, HF-REF-09 |
| SRC-12 | 세제 | 더팩트, 증권거래세 인상 해설 | HF-REF-03, HF-REF-06, HF-REF-09 |
| SRC-13 | 국내 시장 | 금감원, 2025 자산운용사 실적 | HF-REF-02 |
| SRC-14 | 국내 시장 | 서플, 2026 2분기 자산운용사 실적 | HF-REF-01, HF-REF-02, HF-REF-13, HF-REF-14 |
| SRC-15 | 국내 시장 | 더벨, 2025 헤지펀드 리그테이블 | HF-REF-01, HF-REF-02 |
| SRC-16 | 국내 시장 | 더벨, 전략별 수익률 (게재본) | HF-REF-02 |
| SRC-17 | 국내 시장 | KB의 생각, 한국형 헤지펀드 | HF-REF-02 |
| SRC-18 | 국내 시장 | KDI, 국내 헤지펀드 출범 규모 | HF-REF-02 |
| SRC-19 | 국내 시장 | 이데일리, 상위사 쏠림 (2014) | HF-REF-16 |
| SRC-20 | 내부통제 | SBS Biz, 책무구조도 설명회 | HF-REF-01, HF-REF-05, HF-REF-06, HF-REF-18 |
| SRC-21 | 내부통제 | 금융위, 책무구조도 제출 시기 | HF-REF-05, HF-REF-06, HF-REF-18 |
| SRC-22 | 내부통제 | 헤럴드경제, 금감원 CEO 설명회 | HF-REF-06 |
| SRC-23 | 내부통제 | SBS Biz, 사모운용사 위반 사례 | HF-REF-06 |
| SRC-24 | 서비스 제공자 | 뉴스토마토, PBS 개관 | HF-REF-04 |
| SRC-25 | 서비스 제공자 | MTN, 수탁 기피 현상 | HF-REF-10 |
| SRC-26 | 보수 | 한국경제, 2011 헤지펀드 보수 | HF-REF-11 |
| SRC-27 | 국내 사례 | 참여연대, 라임·옵티머스 논평 | HF-REF-01, HF-REF-02, HF-REF-10, HF-REF-14, HF-REF-16 |
| SRC-28 | 국내 사례 | 딜사이트, 2025 ETF 리그테이블 | HF-REF-16 |
| SRC-29 | 국내 사례 | 스마트투데이, ETF 보수 수익 | HF-REF-16 |
| SRC-30 | 국내 사례 | 딜사이트, VIP자산운용 펀드 | HF-REF-16 |
| SRC-31 | 글로벌 시장 | HFR, 2026 2분기 산업 보고서 | HF-REF-01, HF-REF-02 |
| SRC-32 | 글로벌 시장 | Hedgeweek, 2026 2분기 자산 급증 | HF-REF-02 |
| SRC-33 | 글로벌 시장 | HFR, 2025 4분기 5조 달러 돌파 | HF-REF-02 |
| SRC-34 | 글로벌 시장 | HFR, 2026 1분기 업계 자산 | HF-REF-02 |
| SRC-35 | 글로벌 시장 | HFR, 2026 1분기 설정·청산 | HF-REF-02 |
| SRC-36 | 글로벌 시장 | HFR, 2025 3분기 설정·보수·PB 순위 | HF-REF-01, HF-REF-02, HF-REF-10, HF-REF-11 |
| SRC-37 | 글로벌 시장 | The Full FX, 2026 1분기 평균 보수 | HF-REF-02, HF-REF-11 |
| SRC-38 | 벤치마크 | Hedge Fund Alpha, LCH 상위 20 | HF-REF-01, HF-REF-02, HF-REF-15, HF-REF-16, HF-REF-17 |
| SRC-39 | 벤치마크 | Institutional Investor, TCI 순이익 | HF-REF-15, HF-REF-16 |
| SRC-40 | 벤치마크 | Fortune·Bloomberg, 2025 성과 | HF-REF-15, HF-REF-16 |
| SRC-41 | 벤치마크 | With Intelligence, Billion Dollar Club | HF-REF-15, HF-REF-16 |
| SRC-42 | 벤치마크 | EnterpriseAM, 블룸버그 2026.9 자산 | HF-REF-02, HF-REF-14, HF-REF-15, HF-REF-16 |
| SRC-43 | 벤치마크 | Man Group, 2025 연간 실적 | HF-REF-15, HF-REF-16 |
| SRC-44 | 벤치마크 | Hedgeweek, Man Group 2026 상반기 | HF-REF-15, HF-REF-16 |
| SRC-45 | 벤치마크 | Hedgeweek, 보수 구조 투자자 반발 | HF-REF-11 |
| SRC-46 | 벤치마크 | eFinancialCareers, 밀레니엄 손실 한도 | HF-REF-08, HF-REF-16, HF-REF-17 |
| SRC-47 | 벤치마크 | Quant Enthusiasts, 시타델 손익 배분 | HF-REF-16 |
| SRC-48 | 벤치마크 | Rupak Ghose, 밀레니엄 지분 매각 | HF-REF-16 |
| SRC-49 | 벤치마크 | Institutional Investor, 르네상스 성과 | HF-REF-16 |
| SRC-50 | 벤치마크 | Charltons, SEC 투시그마 제재 | HF-REF-12, HF-REF-14, HF-REF-16 |
| SRC-51 | 벤치마크 | Forbes, 2024 상위 20 헤지펀드 | (unmapped) |
| SRC-52 | 벤치마크 | Altss, 규모 순위 집계 기준 | HF-REF-15 |
| SRC-53 | 미국 규제 | SEC·CFTC, Form PF 연장 (2025.9) | HF-REF-07, HF-REF-14 |
| SRC-54 | 미국 규제 | Deloitte, Form PF 추가 연장 (2026.9) | HF-REF-07, HF-REF-14 |
| SRC-55 | 미국 규제 | Holland & Knight, qualified client | HF-REF-07 |
| SRC-56 | 케이맨 | Mourant, 케이맨 뮤추얼펀드 가이드 | HF-REF-07 |
| SRC-57 | 케이맨 | Harneys, 케이맨 계속 의무 (2026) | HF-REF-07 |
| SRC-58 | EU | Regulation Tomorrow, AIFMD II 시행 | HF-REF-07, HF-REF-14 |
| SRC-59 | EU | Jones Day, AIFMD II 이행 | HF-REF-07, HF-REF-14 |
| SRC-60 | 신규 운용사 | AIMA, 신흥 운용사 실수 (2026) | HF-REF-11 |
| SRC-61 | 신규 운용사 | Institutional Investor, AIMA·Cowen 조사 | HF-REF-01, HF-REF-11 |
| SRC-62 | 신규 운용사 | HPT Group, 시딩 조건 | HF-REF-11 |
| SRC-63 | 신규 운용사 | Wikipedia, Jain Global 보수 할인 | HF-REF-11 |

**Unmapped sources:** SRC-51 (Forbes, 2024 상위 20 헤지펀드). No sentence
in HF-REF-01 to HF-REF-19 states a fact, figure, or event that this source
covers. This is a GAP, not an error. Re-check SRC-51 by hand before you
remove it from the source table.

## Integrity

Source file: `docs/hedge-fund-setup/hedge_fund_setup_report.md`

Source sha256:
`73dcac968ef8db58db0e2364625ee85bf24ff2ba2547297d5a4ba1f55ec7dc5a`

Run this command from the repository root to check the chunk set:

```
python3 docs/hedge-fund-setup/tools/split_report.py --check
```

This command reassembles all chunk bodies and compares them to the source.
It prints byte counts and both sha256 values.

The command also checks the `source_evidence` field in `manifest.json`. It
makes sure that every quote in `source_evidence` is a real substring of
its own chunk's body. It prints the number of quotes it checked and the
number it could not find.

The command exits 0 when the bytes match and it finds every quote. It
exits 1 on a byte mismatch, or on a missing quote, or on both.

## Regeneration

Run this command from the repository root to regenerate the chunk set:

```
python3 docs/hedge-fund-setup/tools/split_report.py
```

Follow this rule: edit the source report first. Then run the command
above. Never edit a chunk body by hand.

## Notice

The source report carries this notice in Korean, at line 8:

> **일러두기** 이 리포트는 공개 자료를 바탕으로 정리한 일반 정보이며, 법률·세무·투자 자문이 아닙니다. 수치는 각 출처가 발표한 기준 시점을 따르고, 기준 시점은 표와 본문에 함께 적었습니다. 비용·일정·손익분기처럼 가정에 기반한 수치는 "예시"로 표시했습니다. 실제 설립 과정에서는 금융감독원 사전 상담과 법무법인·회계법인의 검토를 반드시 거쳐야 합니다.

A faithful ASD-STE100 English version follows:

> This report gives general information from public sources. It is not
> legal advice. It is not tax advice. It is not investment advice. Each
> figure uses the reference date from its source. The report shows each
> reference date in the table or the text. The report shows cost,
> schedule, and break-even figures as examples. These figures use
> assumptions. Before you start a fund, get advice from the Financial
> Supervisory Service. Also get advice from a law firm and an accounting
> firm.
