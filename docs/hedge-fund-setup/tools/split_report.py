#!/usr/bin/env python3
"""Split hedge_fund_setup_report.md into reference chunks for AI agents.

Modes
-----
default   : read the source report, write one Markdown chunk file per entry
            in CHUNKS to ../ref/, and write ../ref/manifest.json.
--check   : reassemble every chunk body (the bytes between the
            "<!-- chunk-body:start -->" / "<!-- chunk-body:end -->" markers)
            in id order, concatenate them, and compare the result byte-for-
            byte against the source report. Prints observations only (byte
            counts, both sha256 values, match/mismatch, first differing
            offset). Never prints a verdict beyond that -- the exit code is
            the signal: 0 on match, 1 on mismatch.

This script does not write ref/README.md; that file is authored by hand.

Stdlib only. Python 3.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

TOOLS_DIR = Path(__file__).resolve().parent
BASE_DIR = TOOLS_DIR.parent                      # .../docs/hedge-fund-setup
SOURCE_PATH = BASE_DIR / "hedge_fund_setup_report.md"
OUT_DIR = BASE_DIR / "ref"
SOURCE_REL_PATH = "docs/hedge-fund-setup/hedge_fund_setup_report.md"

AS_OF = "2026-09-24"

BODY_START_MARK = "<!-- chunk-body:start -->\n"
BODY_END_MARK = "<!-- chunk-body:end -->\n"

NOTICE_LINE = (
    "> This chunk is a verbatim extract of the source report. It is general "
    "information. It is not legal, tax, or investment advice. Read HF-REF-00 "
    "for the full notice.\n"
)

VOLATILITY_NOTES = {
    "high": "Market data, rankings, or fee statistics. Re-verify before external use.",
    "medium": "Regulatory values, thresholds, rates, or deadlines. Re-verify before compliance use.",
    "low": "Structure, principles, examples, or definitions. Stable.",
}

# ---------------------------------------------------------------------------
# Chunk table
# ---------------------------------------------------------------------------
# (id, filename, start_line, end_line_or_None_for_EOF, volatility, domains,
#  source_numbers, related_ids)
#
# Line numbers are 1-indexed, inclusive, and were confirmed against the
# source report's actual headings before this table was written (see the
# boundary check the generator performs at start-up).
#
# `source_evidence` is the hard-coded, hand-verified mapping from this
# chunk's body to the Appendix B source rows (SRC-01..SRC-NN, assigned in
# row order by the generator itself -- see build_source_catalog()). It is a
# dict of SRC-id -> a short verbatim quote (at most 80 characters) copied
# from this chunk's own body. A source id appears here only when the quote
# shows its publisher, law article, or specific fact is explicitly present
# in the chunk body. Chunks with no defensible match are left with an
# empty dict rather than guessed at. `--check` verifies every quote is an
# exact substring of its chunk's body (see run_check()). `sources`, in the
# front matter and the manifest, is derived as sorted(source_evidence)
# rather than hand-maintained separately, so the two can never drift.
#
# `related_ids` is hard-coded from two rules: (1) the body explicitly
# cross-references another chapter ("5장에서 자세히 다룹니다" -> chapter 5,
# i.e. HF-REF-07), and (2) two chunks share 2 or more domains. Both rules
# were checked by hand against every chunk pair; only genuine matches are
# listed.

CHUNKS = [
    ("HF-REF-00", "00-front-matter.md", 1, 28, "low",
     ["glossary"],
     {},
     []),
    ("HF-REF-01", "01-executive-summary.md", 29, 58, "high",
     ["market-data", "registration", "constraints", "governance"],
     {
      "SRC-01": "자본시장법 제249조의7",
      "SRC-02": "자본시장법 시행령 제271조의2",
      "SRC-05": "3억원 (레버리지 200% 초과 펀드는 5억원)",
      "SRC-07": "2025년 3월 31일 공매도 전면 재개와 함께 도입된 무차입공매도 방지 전산·내부통제 의무",
      "SRC-11": "2026년 1월부터 0.20%로 오른 증권거래세",
      "SRC-14": "436개사, 적자 비율 47.9%",
      "SRC-15": "40조원 돌파, 운용 펀드 950개 이상",
      "SRC-20": "책무구조도 제출 의무",
      "SRC-27": "라임·옵티머스 사태 이후 강화된 판매사·수탁사의 운용 감시 제도",
      "SRC-31": "5.6조 달러 (사상 최대, 15분기 연속 증가)",
      "SRC-36": "운용보수 1.18%, 성과보수 16.29%",
      "SRC-38": "운용자산 16.6%, 설립 이후 누적 순이익 41.0%",
      "SRC-61": "약 6,400만 달러"},
     []),
    ("HF-REF-02", "02-industry-and-market.md", 59, 135, "high",
     ["market-data", "fund-regulation"],
     {
      "SRC-13": "507개사, 1,937.3조원",
      "SRC-14": "4조 1,553억원 (2025년 연간 실적 상회)",
      "SRC-15": "40조원 돌파, 운용 펀드 950개 이상",
      "SRC-16": "롱바이어스드 | 62.61%",
      "SRC-17": "2011년 12월 '한국형 헤지펀드'라는 이름으로 도입되었습니다",
      "SRC-18": "2011년 12월 약 1,490억원 규모로 출범했습니다",
      "SRC-27": "2019년 10월 당시 업계 1위였던 라임자산운용의 환매 중단 사태",
      "SRC-31": "업계 운용자산 | 5.6조 달러 | 2026년 2분기 말 | HFR",
      "SRC-32": "2026년 2분기에는 한 분기에만 4,093억 달러가 늘어",
      "SRC-33": "2025년 4분기에 처음으로 5조 달러를 넘어 5.15조 달러로 한 해를 마쳤고",
      "SRC-34": "2026년 1분기 말 기준 주식 헤지(Equity Hedge) 전략의 자산이 1.58조 달러",
      "SRC-35": "166개 / 129개 (청산은 2년 만에 최다)",
      "SRC-36": "신규 설정 펀드 수 | 561개 (2021년 이후 최다)",
      "SRC-37": "업계 평균 운용보수 | 1.32%",
      "SRC-38": "상위 20개 운용사는 2025년 말 업계 운용자산의 16.6%를 운용하면서",
      "SRC-42": "9대 헤지펀드의 운용자산은 2025년 초 이후 2,240억 달러 늘었고"},
     ["HF-REF-07"]),
    ("HF-REF-03", "03-founding-decisions.md", 136, 205, "medium",
     ["strategy", "offshore", "fundraising-ir"],
     {
      "SRC-01": "레버리지 400% 한도",
      "SRC-03": "비시장성 자산이 50%를 넘으면 개방형 펀드 불가",
      "SRC-07": "2025년 공매도 전면 재개로 롱숏 전략의 운용 여건은 정상화되었지만",
      "SRC-11": "2026년부터 0.20%로 오른 증권거래세를 비용 모델에 반드시 반영해야 합니다",
      "SRC-12": "증권거래세 0.20%"},
     []),
    ("HF-REF-04", "04-legal-structure.md", 206, 270, "low",
     ["legal-structure", "service-providers"],
     {
      "SRC-01": "설정 후 2주 이내 보고",
      "SRC-24": "자기자본 3조원 이상 증권사만 영위 가능"},
     []),
    ("HF-REF-05", "05-kr-registration-and-roadmap.md", 271, 332, "medium",
     ["registration", "organization"],
     {
      "SRC-01": "등록하지 않고 영업하는 것은 금지됩니다(자본시장법 제249조)",
      "SRC-02": "10억원 이상 (법률은 5억원 이상으로 정하고, 시행령이 10억원으로 규정)",
      "SRC-04": "2021년 개정법은 자기자본 유지 요건 미준수, 일정 기간의 미영업",
      "SRC-20": "책무구조도 작성",
      "SRC-21": "책무구조도 작성"},
     []),
    ("HF-REF-06", "06-kr-fund-rules-controls-tax.md", 333, 397, "medium",
     ["fund-regulation", "short-selling", "internal-control", "tax"],
     {
      "SRC-01": "설정일부터 2주일 이내 금융위원회 보고",
      "SRC-03": "비시장성 자산 비중이 50%를 넘으면 개방형(수시 환매형) 설정 불가",
      "SRC-06": "투자자 수 | 100인 이하, 일반투자자는 49인 이하",
      "SRC-07": "2025년 3월 31일 전 종목을 대상으로 재개되었습니다",
      "SRC-08": "대차 상환기간 | 공매도 목적 대차는 90일 이내에서 정하고",
      "SRC-09": "계좌별 잔고 관리 | 법인·기관투자자는 내부통제기준에 따라",
      "SRC-10": "무차입공매도를 막기 위한 제도가 대폭 강화되었고",
      "SRC-11": "2026년 1월 1일 양도분부터 코스피 0.20%",
      "SRC-12": "코스닥 0.20%, 코넥스 0.10% (2025년 코스피·코스닥 각 0.15%)",
      "SRC-20": "중소형 금융투자업자 1,007개사는 2026년 7월 2일까지 책무구조도를 금융감독원에 제출",
      "SRC-21": "2026년 7월 2일까지 책무구조도를 금융감독원에 제출해야 했습니다",
      "SRC-22": "금융감독원은 2025년 9월 신설 사모운용사 대표이사 설명회에서",
      "SRC-23": "금융감독원이 공개한 사모운용사의 흔한 위반 유형은"},
     []),
    ("HF-REF-07", "07-offshore-setup.md", 398, 447, "medium",
     ["offshore", "fund-regulation"],
     {
      "SRC-53": "2024년 개정안의 준수 기한이 여러 차례 연기되어 2027년 7월 1일로 변경",
      "SRC-54": "2024년 개정안의 준수 기한이 여러 차례 연기되어 2027년 7월 1일로 변경",
      "SRC-55": "2026년 6월 29일부터 운용사에 맡긴 자산 140만 달러 이상",
      "SRC-56": "케이맨 제도는 해외 헤지펀드가 가장 많이 사용하는 역외 관할권입니다",
      "SRC-57": "회계연도 종료 후 6개월 이내 CIMA에 제출",
      "SRC-58": "개정 지침(AIFMD II)의 국내법 전환 기한은 2026년 4월 16일이었으며",
      "SRC-59": "강화된 감독 보고 의무는 2027년 4월부터 적용됩니다"},
     []),
    ("HF-REF-08", "08-organization.md", 448, 537, "low",
     ["organization", "governance", "compensation"],
     {
      "SRC-02": "등록 요건 위반(투자운용인력 3명 미만)",
      "SRC-46": "5% 손실을 내면 자본이 줄어들고 7.5% 손실을 내면 퇴출된다"},
     []),
    ("HF-REF-09", "09-investment-risk-execution.md", 538, 583, "low",
     ["investment-process", "risk", "trading"],
     {
      "SRC-01": "법정 레버리지 비율(순자산의 400%)",
      "SRC-09": "공매도 주문은 펀드 계좌별 잔고 범위 안에서만 나가도록 시스템으로 통제",
      "SRC-10": "공매도 주문은 펀드 계좌별 잔고 범위 안에서만 나가도록 시스템으로 통제",
      "SRC-11": "증권거래세 0.20%와 매매 수수료를 포함한 총 거래 비용",
      "SRC-12": "증권거래세 0.20%와 매매 수수료를 포함한 총 거래 비용"},
     []),
    ("HF-REF-10", "10-operations-and-providers.md", 584, 614, "medium",
     ["operations", "service-providers"],
     {
      "SRC-25": "소규모 사모펀드나 비상장 자산이 포함된 펀드의 수탁을 꺼리는 경향",
      "SRC-27": "라임·옵티머스 사태 이후 수탁 기관이",
      "SRC-36": "HFR 집계 상위: 골드만삭스, UBS, JP모건, 모건스탠리"},
     []),
    ("HF-REF-11", "11-fees-and-fundraising.md", 615, 642, "high",
     ["fees", "fundraising-ir"],
     {
      "SRC-26": "2011년 한국형 헤지펀드 출범 당시 운용보수 0.3~1%",
      "SRC-36": "2025년 3분기 신규 펀드 평균 16.29%",
      "SRC-37": "업계 평균 1.32% (2026년 1분기)",
      "SRC-45": "멀티전략 투자자 몫은 2021년 이익 1달러당 54센트에서 2023년 41센트로 감소",
      "SRC-60": "AIMA는 2026년 글에서 해외 기준 최소 출범 예산이 과거 25만 달러에서",
      "SRC-61": "AIMA와 Cowen이 2022년에 발표한 조사에서 기관 투자자의 80.8%는",
      "SRC-62": "시드 투자자는 통상 2,500만~1억 달러를 투자하고",
      "SRC-63": "2024년 Jain Global은 2.5억 달러 이상 약정 투자자에게 성과보수 10%를 제시"},
     []),
    ("HF-REF-12", "12-technology-infrastructure.md", 643, 659, "low",
     ["technology", "risk"],
     {
      "SRC-50": "2025년 1월 SEC가 투시그마에 9,000만 달러의 과징금을 부과한 사건"},
     []),
    ("HF-REF-13", "13-firm-economics.md", 660, 697, "low",
     ["firm-economics"],
     {
      "SRC-14": "국내 사모운용사의 절반 가까이가 적자를 내는 구조적 이유"},
     []),
    ("HF-REF-14", "14-constraints-and-risks.md", 698, 760, "medium",
     ["constraints", "risk", "failure-lessons"],
     {
      "SRC-14": "국내 사모운용사 적자 비율 47.9%",
      "SRC-27": "라임·옵티머스 | 2019~2020",
      "SRC-42": "2026년 9월 블룸버그 보도에서 한 투자 전문가는 멀티전략 펀드들이",
      "SRC-50": "SEC 과징금 9,000만 달러와 1억 6,500만 달러 자발적 상환",
      "SRC-53": "Form PF 등 보고 의무 (개정안 준수 기한 2027년 7월 1일)",
      "SRC-54": "Form PF 등 보고 의무 (개정안 준수 기한 2027년 7월 1일)",
      "SRC-58": "AIFMD II 유동성 관리 수단, 위탁·실체 요건",
      "SRC-59": "AIFMD II 유동성 관리 수단, 위탁·실체 요건"},
     []),
    ("HF-REF-15", "15-benchmark-rankings.md", 761, 819, "high",
     ["benchmark", "market-data"],
     {
      "SRC-38": "LCH Investments는 매년 설립 이후 투자자에게 안겨 준 누적 순이익",
      "SRC-39": "TCI는 189억 달러를 벌어 단일 운용사 기준 사상 최대 연간 순이익을 기록했고",
      "SRC-40": "Bridgewater | Pure Alpha II | +34%",
      "SRC-41": "헤지펀드 자산이 10억 달러를 넘는 551개 운용사가 2025년 상반기 말 3.6조 달러를 운용했으며",
      "SRC-42": "2026년 9월 블룸버그 보도에 따르면 밀레니엄은 970억 달러를 운용하며",
      "SRC-43": "Man Group | 영국 런던 | 퀀트 | 665",
      "SRC-44": "맨그룹의 전체 운용자산은 2026년 6월 말 2,536억 달러로 사상 최대를 기록했습니다",
      "SRC-52": "헤지펀드 운용 규모는 집계 기준에 따라 크게 달라집니다"},
     []),
    ("HF-REF-16", "16-benchmark-operating-models.md", 820, 868, "high",
     ["benchmark", "governance"],
     {
      "SRC-19": "상위 2개 운용사(삼성, 브레인)의 설정액 점유율이 2014년 54.1%",
      "SRC-27": "2019년 10월 환매 중단 사태를 일으켰고, 옵티머스 사태와 합쳐 2조원 이상의 피해",
      "SRC-28": "2025년 ETF 순자산 증가율이 307%에 달했고",
      "SRC-29": "운용보수 수익은 점유율 4위 운용사보다 많았습니다",
      "SRC-30": "2025년 7월 목표수익률 17%를 제시한 단위형·개방형 일반 사모펀드",
      "SRC-38": "누적 순이익 904억 달러로 업계 1위를 지키고 있고",
      "SRC-39": "2025년 189억 달러의 순이익으로 단일 운용사 기준 사상 최대 연간 기록",
      "SRC-40": "2025년 Oculus가 28.2%, Composite가 18.5%를 기록했고",
      "SRC-41": "처음으로 주식 전략보다 많은 자산을 늘렸다고 분석했습니다",
      "SRC-42": "2026년 9월에는 회사 전체 운용자산이 1,400억 달러를 넘었습니다",
      "SRC-43": "운용자산은 2025년 말 2,276억 달러에서",
      "SRC-44": "2026년 6월 말 2,536억 달러로 늘었습니다",
      "SRC-46": "운용팀이 5% 손실을 내면 자본이 줄고 7.5% 손실을 내면 퇴출된다",
      "SRC-47": "3개 주요 펀드는 2021년 초부터 2024년 9월까지 568억 달러의 이익을 냈고",
      "SRC-48": "2025년에는 운용사 지분 10~15%를 외부에 매각하는 방안을 검토한다는 보도",
      "SRC-49": "RIEF는 2024년에 22.7%로 2011년 이후 최고 수익률을 기록했습니다",
      "SRC-50": "9,000만 달러의 과징금을 부과했고, 회사는 피해 펀드에 1억 6,500만 달러를 자발적으로 상환"},
     ["HF-REF-17"]),
    ("HF-REF-17", "17-success-factors.md", 869, 884, "low",
     ["benchmark", "governance", "risk"],
     {
      "SRC-38": "상위 20개사 대부분의 2025년 유입 제한·자본 반환",
      "SRC-46": "밀레니엄의 수치화된 손실 규칙"},
     ["HF-REF-16"]),
    ("HF-REF-18", "18-execution-checklist.md", 885, 908, "low",
     ["checklist", "registration"],
     {
      "SRC-01": "설정 후 2주일 이내 금융위원회에 보고했는가",
      "SRC-02": "자기자본 10억원과 운영 적자 버퍼를 확보했는가",
      "SRC-20": "책무구조도를 작성했는가",
      "SRC-21": "책무구조도를 작성했는가"},
     []),
    ("HF-REF-19", "19-glossary.md", 909, 943, "low",
     ["glossary"],
     {},
     []),
    ("HF-REF-20", "20-sources.md", 944, None, "medium",
     ["sources"],
     {
      "SRC-01": "자본시장과 금융투자업에 관한 법률 제249조~제249조의18 (2026년 2월 3일 시행본)",
      "SRC-02": "자본시장법 시행령 제271조의2 (일반 사모집합투자업 등록 요건)",
      "SRC-03": "금융위원회, 사모펀드 투자자 보호·체계 개편 하위 규정 시행 (2021)",
      "SRC-04": "김·장 법률사무소, 사모펀드 규제 개편 관련 자본시장법 개정",
      "SRC-05": "아주경제, 사모펀드 10월 개편 Q&A (3억원·5억원 최소 투자금)",
      "SRC-06": "메트로서울, 사모펀드 투자자 100인 확대",
      "SRC-07": "금융위원회, 3월 31일부터 공매도 전면 재개",
      "SRC-08": "금융위원회, 공매도 제도개선 법규 개정 완료",
      "SRC-09": "금융위원회, 공매도 제도개선 후속 시행령 입법예고",
      "SRC-10": "자본시장연구원, 공매도 재개를 위한 제도개선 및 기대효과",
      "SRC-11": "삼일PwC, 2025년 세법 개정 해설 (증권거래세)",
      "SRC-12": "더팩트, 증권거래세 인상 해설",
      "SRC-13": "금융감독원, 2025년 자산운용회사 영업실적",
      "SRC-14": "서플, 2026년 2분기 자산운용회사 영업실적 보도",
      "SRC-15": "더벨, 2025년 한국형 헤지펀드 리그테이블",
      "SRC-16": "더벨 헤지펀드 리그테이블 전략별 수익률 보도 (게재본)",
      "SRC-17": "KB의 생각, 한국형 헤지펀드",
      "SRC-18": "KDI, 국내 헤지펀드 현황 (출범 규모)",
      "SRC-19": "이데일리, 국내 헤지펀드 3년 성장과 상위사 쏠림 (2014)",
      "SRC-20": "SBS Biz, 중소형 금융투자업자 책무구조도 설명회",
      "SRC-21": "금융위원회, 책무구조도 시범운영과 업권별 제출 시기",
      "SRC-22": "헤럴드경제, 금감원 신설 사모운용사 CEO 설명회",
      "SRC-23": "SBS Biz, 사모운용사 법규 위반 사례",
      "SRC-24": "뉴스토마토, PBS와 종합금융투자사업자",
      "SRC-25": "머니투데이방송, 사모펀드 수탁 기피와 증권사 수탁 진출",
      "SRC-26": "한국경제, 한국형 헤지펀드 출범 당시 보수 (2011)",
      "SRC-27": "참여연대, 라임·옵티머스 사태 논평",
      "SRC-28": "딜사이트, 2025년 ETF 리그테이블 (타임폴리오)",
      "SRC-29": "스마트투데이, ETF 보수 수익 (타임폴리오)",
      "SRC-30": "딜사이트, VIP자산운용 목표수익률 펀드",
      "SRC-31": "HFR, 2026년 2분기 Global Hedge Fund Industry Report",
      "SRC-32": "Hedgeweek, 2026년 2분기 헤지펀드 자산 급증",
      "SRC-33": "HFR, 2025년 4분기 업계 자산 5조 달러 돌파",
      "SRC-34": "HFR, 2026년 1분기 업계 자산",
      "SRC-35": "HFR, 2026년 1분기 펀드 설정·청산",
      "SRC-36": "HFR, 2025년 3분기 펀드 설정·보수·PB 순위",
      "SRC-37": "The Full FX, 2026년 1분기 평균 운용보수",
      "SRC-38": "Hedge Fund Alpha, LCH Investments 2025년 상위 20개 운용사",
      "SRC-39": "Institutional Investor, TCI의 2025년 순이익",
      "SRC-40": "Fortune·Bloomberg, 2025년 헤지펀드 성과",
      "SRC-41": "With Intelligence, Billion Dollar Club H1 2025",
      "SRC-42": "EnterpriseAM, 블룸버그 보도 인용 (2026년 9월 대형 헤지펀드 자산)",
      "SRC-43": "Man Group, 2025년 연간 실적",
      "SRC-44": "Hedgeweek, Man Group 2026년 상반기 운용자산",
      "SRC-45": "Hedgeweek, 멀티전략 펀드 보수 구조에 대한 투자자 반발",
      "SRC-46": "eFinancialCareers, 밀레니엄 손실 한도 규칙",
      "SRC-47": "Quant Enthusiasts, 시타델 채권 설명서 기반 손익 배분 분석",
      "SRC-48": "Rupak Ghose, 밀레니엄 지분 매각 보도 분석",
      "SRC-49": "Institutional Investor, 르네상스 외부 펀드 성과",
      "SRC-50": "Charltons Quantum, SEC의 투시그마 제재",
      "SRC-51": "Forbes, 2024년 상위 20개 헤지펀드",
      "SRC-52": "Altss, 헤지펀드 규모 순위와 집계 기준 차이",
      "SRC-53": "SEC·CFTC, Form PF 준수 기한 연장 (2025년 9월)",
      "SRC-54": "Deloitte, Form PF 준수 기한 추가 연장 (2026년 9월)",
      "SRC-55": "Holland & Knight, qualified client 기준 상향",
      "SRC-56": "Mourant, 케이맨 뮤추얼펀드 가이드",
      "SRC-57": "Harneys, 케이맨 등록 펀드 계속 의무 (2026)",
      "SRC-58": "Regulation Tomorrow, AIFMD II 시행",
      "SRC-59": "Jones Day, AIFMD II 이행",
      "SRC-60": "AIMA, 신흥 운용사가 출범 시 흔히 하는 실수 (2026)",
      "SRC-61": "Institutional Investor, AIMA·Cowen 신흥 운용사 조사 (2022)",
      "SRC-62": "HPT Group, 신흥 운용사 출범과 시딩 조건",
      "SRC-63": "Jain Global 보수 할인 사례"},
     []),
]

# Boundary lines this generator confirms before writing anything: (line,
# expected literal heading text at that line, 1-indexed).
BOUNDARY_CHECKS = [
    (1, "# 헤지펀드 운용사 설립 가이드"),
    (29, "## 핵심 요약"),
    (59, "## 1. 헤지펀드의 정의와 산업 현황"),
    (136, "## 2. 설립 전 핵심 의사결정"),
    (206, "## 3. 법적 구조"),
    (271, "## 4. 국내 설립 절차"),
    (333, "### 4.3 펀드 설정과 운용 규제"),
    (398, "## 5. 해외 설립 절차"),
    (448, "## 6. 조직도"),
    (538, "## 7. 운영 방식"),
    (584, "### 7.4 오퍼레이션과 기준가 산정"),
    (615, "### 7.6 보수 구조"),
    (643, "### 7.8 기술 인프라"),
    (660, "### 7.9 운용사 손익 구조와 손익분기 (예시)"),
    (698, "## 8. 제약 조건과 리스크"),
    (761, "## 9. 세계 최고 헤지펀드 벤치마크"),
    (820, "### 9.3 운용사별 운영 모델 분석"),
    (869, "### 9.5 공통 성공 요인과 설립 시사점"),
    (885, "## 10. 실행 체크리스트"),
    (909, "## 부록"),
    (944, "### 부록 B. 참고 자료"),
]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
SECTION_HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*$")
FENCE_RE = re.compile(r"^\s*```")

TABLE_ROW_RE = re.compile(r"^\|(.*)\|\s*$")
LINK_RE = re.compile(r"^\[(.*)\]\((.*)\)$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_source_lines() -> list[str]:
    with open(SOURCE_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    lines = text.splitlines(keepends=True)
    return lines


def check_boundaries(lines: list[str]) -> None:
    """Confirm every expected boundary line starts the heading we expect.

    Stops and reports (does not move anything silently) if a boundary is off.
    """
    problems = []
    for line_no, expected in BOUNDARY_CHECKS:
        actual = lines[line_no - 1].rstrip("\n") if line_no - 1 < len(lines) else None
        if actual != expected:
            problems.append(
                f"line {line_no}: expected {expected!r}, found {actual!r}"
            )
    if problems:
        print("BOUNDARY CHECK FAILED -- stopping without writing anything:",
              file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        sys.exit(2)


def extract_body(lines: list[str], start: int, end: int | None) -> str:
    """1-indexed, inclusive line range -> exact joined text."""
    end_idx = len(lines) if end is None else end
    return "".join(lines[start - 1:end_idx])


def first_heading_and_sections(body: str) -> tuple[str, list[str]]:
    """Return (title, sections) from a chunk body.

    title: the first heading of any level (#, ##, ### ...), verbatim text.
    sections: every ## / ### heading, verbatim text, in order.
    Lines inside fenced code blocks (```...```) are never treated as
    headings, since the report's mermaid diagrams live in such fences.
    """
    title = None
    sections = []
    in_fence = False
    for raw_line in body.splitlines():
        if FENCE_RE.match(raw_line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if title is None:
            m = HEADING_RE.match(raw_line)
            if m:
                title = m.group(2)
        m2 = SECTION_HEADING_RE.match(raw_line)
        if m2:
            sections.append(m2.group(2))
    if title is None:
        title = sections[0] if sections else ""
    return title, sections


def build_source_catalog(lines: list[str]) -> list[dict]:
    """Parse the Appendix B table (inside HF-REF-20's range) mechanically.

    Every row of the '부록 B. 참고 자료' table becomes one source entry,
    in row order, ids assigned SRC-01.. from that order. This is a
    lossless, automatic extraction of the table -- not a hand-authored
    guess -- since the table's own row order is the ground truth.
    """
    # Find the appendix table: header row "| 구분 | 자료 | 링크 |"
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "| 구분 | 자료 | 링크 |":
            header_idx = i
            break
    if header_idx is None:
        print("ERROR: could not find the Appendix B source table header",
              file=sys.stderr)
        sys.exit(2)

    rows = []
    i = header_idx + 2  # skip header + separator ("|---|---|---|")
    while i < len(lines):
        line = lines[i]
        m = TABLE_ROW_RE.match(line.rstrip("\n"))
        if not m:
            break
        cells = [c.strip() for c in m.group(1).split("|")]
        if len(cells) != 3:
            break
        category, title, link_cell = cells
        link_m = LINK_RE.match(link_cell)
        url = link_m.group(2) if link_m else link_cell
        rows.append({"category": category, "title": title, "url": url})
        i += 1

    catalog = []
    for n, row in enumerate(rows, start=1):
        catalog.append({
            "id": f"SRC-{n:02d}",
            "category": row["category"],
            "title": row["title"],
            "url": row["url"],
        })
    return catalog


def yaml_front_matter(fields: list[tuple[str, object]]) -> str:
    out = ["---\n"]
    for key, value in fields:
        out.append(f"{key}: {json.dumps(value, ensure_ascii=False)}\n")
    out.append("---\n")
    return "".join(out)


def write_chunks(lines: list[str], source_bytes: bytes, source_sha256: str,
                  catalog: list[dict]) -> list[dict]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    catalog_by_id = {c["id"]: c for c in catalog}
    manifest_chunks = []

    for idx, (cid, fname, start, end, volatility, domains, source_evidence,
              related) in enumerate(CHUNKS):
        body = extract_body(lines, start, end)
        end_line = len(lines) if end is None else end
        title, sections = first_heading_and_sections(body)
        body_bytes = body.encode("utf-8")
        sha256_body = sha256_bytes(body_bytes)
        src_ids = sorted(source_evidence.keys())
        for sid in src_ids:
            if sid not in catalog_by_id:
                print(f"ERROR: {cid} cites unknown source id {sid}",
                      file=sys.stderr)
                sys.exit(2)
            quote = source_evidence[sid]
            if len(quote) > 80:
                print(f"ERROR: {cid} source_evidence[{sid}] exceeds 80 "
                      f"characters", file=sys.stderr)
                sys.exit(2)
            if quote not in body:
                print(f"ERROR: {cid} source_evidence[{sid}] quote is not "
                      f"a substring of the chunk body: {quote!r}",
                      file=sys.stderr)
                sys.exit(2)

        front = yaml_front_matter([
            ("id", cid),
            ("title", title),
            ("source", SOURCE_REL_PATH),
            ("source_lines", f"{start}-{end_line}"),
            ("source_sha256", source_sha256),
            ("as_of", AS_OF),
            ("sections", sections),
            ("domains", domains),
            ("volatility", volatility),
            ("volatility_note", VOLATILITY_NOTES[volatility]),
            ("sources", src_ids),
            ("related", related),
        ])

        prev_link = ""
        if idx > 0:
            prev_cid, prev_fname = CHUNKS[idx - 1][0], CHUNKS[idx - 1][1]
            prev_link = f"Previous: [{prev_cid}]({prev_fname}) · "
        next_link = ""
        if idx < len(CHUNKS) - 1:
            next_cid, next_fname = CHUNKS[idx + 1][0], CHUNKS[idx + 1][1]
            next_link = f" · Next: [{next_cid}]({next_fname})"
        footer = f"{prev_link}Index: [README](README.md){next_link}\n"

        out_text = (
            front
            + "\n"
            + NOTICE_LINE
            + "\n"
            + BODY_START_MARK
            + body
            + BODY_END_MARK
            + "\n"
            + footer
        )
        out_path = OUT_DIR / fname
        out_bytes = out_text.encode("utf-8")
        out_path.write_bytes(out_bytes)

        manifest_chunks.append({
            "id": cid,
            "file": fname,
            "title": title,
            "source_lines": f"{start}-{end_line}",
            "bytes": len(body_bytes),
            "sha256_body": sha256_body,
            "volatility": volatility,
            "domains": domains,
            "sources": src_ids,
            "source_evidence": source_evidence,
            "related": related,
        })

    return manifest_chunks


def write_manifest(source_sha256: str, catalog: list[dict],
                    manifest_chunks: list[dict]) -> None:
    # HF-REF-20 is the Appendix B source table itself, so its own
    # source_evidence necessarily lists all catalog ids. Counting it here
    # would make every source "cited" and unmapped_sources always empty,
    # which defeats the field's purpose (see ref/README.md's Source table,
    # which excludes HF-REF-20 from "cited by" for the same reason).
    cited = set()
    for c in manifest_chunks:
        if c["id"] == "HF-REF-20":
            continue
        cited.update(c["sources"])
    unmapped = [c["id"] for c in catalog if c["id"] not in cited]

    manifest = {
        "source": SOURCE_REL_PATH,
        "source_sha256": source_sha256,
        "as_of": AS_OF,
        "chunks": manifest_chunks,
        "sources": catalog,
        "unmapped_sources": unmapped,
    }
    manifest_path = OUT_DIR / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run_generate() -> None:
    lines = load_source_lines()
    check_boundaries(lines)
    source_bytes = SOURCE_PATH.read_bytes()
    source_sha256 = sha256_bytes(source_bytes)
    catalog = build_source_catalog(lines)
    manifest_chunks = write_chunks(lines, source_bytes, source_sha256, catalog)
    write_manifest(source_sha256, catalog, manifest_chunks)
    print(f"Wrote {len(manifest_chunks)} chunk files and manifest.json to "
          f"{OUT_DIR}")
    print(f"Source sha256: {source_sha256}")
    print(f"Source catalog: {len(catalog)} entries (SRC-01..SRC-{len(catalog):02d})")


def run_check() -> int:
    """Reassemble chunk bodies in id order and compare to the source.

    Then check that every source_evidence quote in CHUNKS is an exact
    substring of its own chunk's body.

    Prints observations only -- byte counts, both sha256 values, a
    match/mismatch statement, the first differing byte offset on mismatch,
    and the source_evidence check counts (checked / missing, with the list
    of any missing). Exit 0 when the bytes match and no quote is missing.
    Exit 1 on a byte mismatch or on any missing quote.
    """
    source_bytes = SOURCE_PATH.read_bytes()
    source_sha256 = sha256_bytes(source_bytes)

    if not OUT_DIR.exists():
        print("OBSERVATION: ref/ does not exist -- nothing to check.")
        return 1

    chunk_ids_in_order = [c[0] for c in CHUNKS]
    files_by_id = {c[0]: c[1] for c in CHUNKS}
    evidence_by_id = {c[0]: c[6] for c in CHUNKS}

    reassembled_parts = []
    bodies_by_id = {}
    for cid in chunk_ids_in_order:
        fname = files_by_id[cid]
        chunk_path = OUT_DIR / fname
        if not chunk_path.exists():
            print(f"OBSERVATION: missing chunk file for {cid}: {chunk_path}")
            return 1
        with open(chunk_path, "r", encoding="utf-8", newline="") as f:
            text = f.read()
        start_idx = text.find(BODY_START_MARK)
        end_idx = text.find(BODY_END_MARK)
        if start_idx == -1 or end_idx == -1:
            print(f"OBSERVATION: markers not found in {fname}")
            return 1
        body = text[start_idx + len(BODY_START_MARK):end_idx]
        reassembled_parts.append(body)
        bodies_by_id[cid] = body

    reassembled_text = "".join(reassembled_parts)
    reassembled_bytes = reassembled_text.encode("utf-8")
    reassembled_sha256 = sha256_bytes(reassembled_bytes)

    print(f"OBSERVATION: source bytes = {len(source_bytes)}")
    print(f"OBSERVATION: reassembled bytes = {len(reassembled_bytes)}")
    print(f"OBSERVATION: source sha256 = {source_sha256}")
    print(f"OBSERVATION: reassembled sha256 = {reassembled_sha256}")

    byte_match = reassembled_bytes == source_bytes
    if byte_match:
        print("OBSERVATION: byte-for-byte match")
    else:
        print("OBSERVATION: byte-for-byte mismatch")
        limit = min(len(source_bytes), len(reassembled_bytes))
        first_diff = None
        for i in range(limit):
            if source_bytes[i] != reassembled_bytes[i]:
                first_diff = i
                break
        if first_diff is None:
            first_diff = limit
        print(f"OBSERVATION: first differing byte offset = {first_diff}")

    checked = 0
    missing = []
    for cid in chunk_ids_in_order:
        body = bodies_by_id[cid]
        for sid, quote in evidence_by_id[cid].items():
            checked += 1
            if quote not in body:
                missing.append((cid, sid, quote))

    print(f"OBSERVATION: source_evidence quotes checked = {checked}")
    print(f"OBSERVATION: source_evidence quotes missing = {len(missing)}")
    if missing:
        print("OBSERVATION: missing source_evidence quotes:")
        for cid, sid, quote in missing:
            print(f"  - {cid} {sid}: {quote!r}")

    return 0 if (byte_match and not missing) else 1


def main() -> int:
    if "--check" in sys.argv[1:]:
        return run_check()
    run_generate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
