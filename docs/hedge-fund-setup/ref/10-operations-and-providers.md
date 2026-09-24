---
id: "HF-REF-10"
title: "7.4 오퍼레이션과 기준가 산정"
source: "docs/hedge-fund-setup/hedge_fund_setup_report.md"
source_lines: "584-614"
source_sha256: "73dcac968ef8db58db0e2364625ee85bf24ff2ba2547297d5a4ba1f55ec7dc5a"
as_of: "2026-09-24"
sections: ["7.4 오퍼레이션과 기준가 산정", "7.5 서비스 제공자"]
domains: ["operations", "service-providers"]
volatility: "medium"
volatility_note: "Regulatory values, thresholds, rates, or deadlines. Re-verify before compliance use."
sources: ["SRC-25", "SRC-27", "SRC-36"]
related: []
---

> This chunk is a verbatim extract of the source report. It is general information. It is not legal, tax, or investment advice. Read HF-REF-00 for the full notice.

<!-- chunk-body:start -->
### 7.4 오퍼레이션과 기준가 산정

**표 7-2** 거래 한 건의 처리 과정

| 단계 | 내용 | 담당 |
|---|---|---|
| 체결 | 주문 체결과 체결 내역 확인 | 트레이더, 브로커 |
| 확인·배분 | 펀드별 체결 수량 배분, 매매 확인 | 오퍼레이션 |
| 결제 | 국내 주식 기준 체결일로부터 2영업일 후 결제 | PB, 수탁사 |
| 대사 | 운용사·PB·수탁사(또는 사무관리사)의 잔고와 현금을 매일 대조 | 오퍼레이션 |
| 기준가 산정 | 사무관리회사가 산정하고 운용사가 독립적으로 검증 | 사무관리회사, 운용사 |
| 보고 | 투자자 보고서, 규제 보고 | IR, 준법감시인 |

오퍼레이션의 핵심 원칙은 **운용사가 스스로 펀드의 가치를 확정하지 않는 것**입니다. 펀드 재산은 독립된 수탁사가 보관하고, 기준가는 독립된 사무관리회사가 산정하며, 운용사는 그 결과를 내부 기록과 대조하여 검증합니다. 역사상 최대 규모의 금융 사기로 꼽히는 매도프 사건은 자산 보관과 가치 산정을 운용 주체가 사실상 통제했기 때문에 오랫동안 드러나지 않았습니다. 기관 투자자가 독립 사무관리와 독립 보관을 투자의 전제 조건으로 요구하는 이유가 여기에 있습니다.

### 7.5 서비스 제공자

**표 7-3** 서비스 제공자 선정 기준

| 서비스 | 국내 | 해외 | 선정 기준 |
|---|---|---|---|
| 프라임 브로커(PBS) | 자기자본 3조원 이상 종합금융투자사업자 | HFR 집계 상위: 골드만삭스, UBS, JP모건, 모건스탠리 | 대차 가능 물량, 대차 수수료와 신용공여 금리, 시스템 연계, 신규 운용사 지원 수준 |
| 수탁·보관 | 신탁업자(주로 은행), 일부 증권사 | 커스터디언 (PB가 겸영하는 경우가 많음) | 소규모·비시장성 자산 펀드 수탁 가능 여부, 감시 역량 |
| 사무관리·펀드 관리 | 일반사무관리회사 | HFR 집계 상위: Citco, SS&C | 기준가 정확성, 보고 품질, 독립성 |
| 회계 감사 | 회계법인 | 대형 회계법인 등 | 헤지펀드 감사 경험 |
| 법무 | 법무법인 | 역외 법무법인, 미국 법무법인 | 펀드 설립과 규제 대응 경험 |
| 판매 | 증권사·은행 PB·WM 채널, 운용사 직판 | 판매 대행사(placement agent), PB의 투자자 소개 | 고객 기반, 상품 승인 절차, 판매 보수 |
| 기술 | 주문·리스크·데이터 시스템 공급사 | 주문·리스크·데이터 시스템 공급사 | 비용, 확장성, 보안 |

국내에서는 라임·옵티머스 사태 이후 수탁 기관이 소규모 사모펀드나 비상장 자산이 포함된 펀드의 수탁을 꺼리는 경향이 나타났습니다. 수탁사를 구하기 어려운 운용사가 PBS를 통해 수탁을 연계하는 사례도 있으므로, 수탁사 확보는 등록 신청 전에 협의를 시작해야 하는 항목입니다.

<!-- chunk-body:end -->

Previous: [HF-REF-09](09-investment-risk-execution.md) · Index: [README](README.md) · Next: [HF-REF-11](11-fees-and-fundraising.md)
