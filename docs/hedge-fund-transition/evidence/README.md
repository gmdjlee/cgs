# Evidence — T2 Hedge-Fund Transition Plan

| Field | Value |
|---|---|
| Document ID | HFT-EVD-001 |
| Version | 0.1 |
| Date | 2026-09-24 |
| Status | Frozen snapshot |
| Baseline | CCGS v1.1.1 (7ed2c3e) |
| Writing standard | ASD-STE100 writing rules |

## Purpose

This folder keeps the working files that produced the plan documents. The
plan documents cite these files. Keep them so that a reader can check each
claim. Do not edit these files. They are a record of the analysis on
2026-09-24.

## Files

| File | Content | Made by |
|---|---|---|
| `design-spec.md` | The Advisor design decisions: facts F-01 to F-16, silent breaks SB-01 to SB-28, the roster, the lifecycle, the control model, the skill catalog, phases P0 to P9, the AAA bar, the risks, and the blueprint corrections. | Advisor |
| `question-spec.md` | The source specification of the 36 founder questions in 9 rounds. `../QUESTIONS.md` renders it in Korean. | Advisor |
| `wf1.json` | The raw result of the discovery workflow: the chunk split report, six area assessments, the org blueprint, and seven verifier reports. | Workers and verifiers |
| `assess-compact.md` | A readable digest of the six area assessments in `wf1.json`. | Advisor (script) |
| `orgmap.json` | The org blueprint result, taken from `wf1.json`. | Worker |
| `verifier-issues.md` | Every issue that the seven verifiers found. The plan documents apply these corrections. | Verifiers |
| `review.txt` | The plain text of `../../org-migration-review/index.html`. | Advisor (script) |
| `mapping.txt` | The per-component T1 and T2 verdict tables from the same review. | Advisor (script) |

## Verification record

- The seven verifiers checked 412 citations. They found 9 wrong citations.
  `verifier-issues.md` lists each one with its correction.
- The chunk split passed a byte-for-byte reassembly check. Run
  `python3 docs/hedge-fund-setup/tools/split_report.py --check` to repeat it.

## Notice

These files are analysis records. They are not legal, tax, or investment
advice.
