---
id: "HF-REF-12"
title: "7.8 기술 인프라"
source: "docs/hedge-fund-setup/hedge_fund_setup_report.md"
source_lines: "643-659"
source_sha256: "73dcac968ef8db58db0e2364625ee85bf24ff2ba2547297d5a4ba1f55ec7dc5a"
as_of: "2026-09-24"
sections: ["7.8 기술 인프라"]
domains: ["technology", "risk"]
volatility: "low"
volatility_note: "Structure, principles, examples, or definitions. Stable."
sources: ["SRC-50"]
related: []
---

> This chunk is a verbatim extract of the source report. It is general information. It is not legal, tax, or investment advice. Read HF-REF-00 for the full notice.

<!-- chunk-body:start -->
### 7.8 기술 인프라

**표 7-5** 헤지펀드 기술 스택의 구성 요소

| 구성 요소 | 기능 | 설립 초기 권장 방식 |
|---|---|---|
| 주문관리·체결관리(OMS·EMS) | 주문 생성, 사전 컴플라이언스 점검, 체결 관리 | 구매 또는 PB 제공 시스템 활용 |
| 포트폴리오 관리(PMS) | 포지션, 손익, 성과 기여 분석 | 구매 |
| 리스크 엔진 | 익스포저, VaR, 스트레스 테스트 | 구매 후 내부 지표 추가 |
| 공매도 잔고관리 | 계좌별 매도 가능 잔고 통제, 거래소 보고 | PB 연계 또는 구매 |
| 데이터 | 시장·재무·대체 데이터, 데이터 품질 관리 | 필요한 데이터부터 단계적으로 구매 |
| 리서치 환경 | 분석·백테스트 코드, 모델 저장소 | 퀀트 전략은 자체 구축, 버전 관리 필수 |
| 투자자 보고·CRM | 보고서 생성, 투자자 관리 | 구매 |
| 보안·업무 연속성 | 접근 통제, 로그, 백업, 재해 복구 | 외부 전문 업체와 계약 |

원칙은 **차별화의 원천만 직접 만들고 나머지는 구매하는 것**입니다. 퀀트 운용사라면 리서치와 신호 생성은 자체 역량이어야 하지만, 주문 시스템이나 투자자 보고 시스템까지 직접 만들 이유는 없습니다. 모델을 운용에 쓰는 운용사라면 모델 변경 승인, 코드 접근 권한, 변경 이력 관리를 컴플라이언스 규정에 포함해야 합니다. 2025년 1월 SEC가 투시그마에 9,000만 달러의 과징금을 부과한 사건은 모델 취약점을 알고도 수년간 방치하고 한 직원의 무단 모델 변경을 감독하지 못한 결과였습니다.

<!-- chunk-body:end -->

Previous: [HF-REF-11](11-fees-and-fundraising.md) · Index: [README](README.md) · Next: [HF-REF-13](13-firm-economics.md)
