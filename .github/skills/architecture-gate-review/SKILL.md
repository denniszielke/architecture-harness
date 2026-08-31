---
name: architecture-gate-review
description: "Prepare an evidence-based G0-G7 readiness recommendation. Use this skill whenever the user asks whether a phase is ready, wants a gate review, requests readiness criteria, or needs blockers and conditions for framing, preparation, design, architecture, implementation, sizing, operations, or presentation."
---

# Architecture Gate Review

## Prerequisites

- Gate ID from `architecture-harness.json`.
- Relevant phase plan and controlled artifacts.
- Open changes, assumptions, ADRs, dependencies, risks, tests, and evidence.

## Workflow

1. Resolve the gate scope, baseline, authority, and phase completion criteria.
2. Check every criterion against current repository evidence.
3. Classify criteria as `Ready`, `Ready with conditions`, `Blocked`, `Not evidenced`, or `Not applicable`.
4. Distinguish designed, demonstrated, and operational evidence.
5. Identify open changes or superseded decisions that invalidate evidence.
6. Record blockers, conditions, dissent, accepted-risk requests, owner roles, and due actions.
7. Write a readiness recommendation in the gate register.
8. Leave the gate decision untouched unless the actual authority provided it.

## Error handling

| Failure | Action |
|---|---|
| Gate scope is unclear | Ask for the baseline or delivery increment |
| Evidence is linked but unavailable | Mark not evidenced |
| Criterion is claimed complete without proof | Downgrade to designed or not evidenced |
| Blocking ADR remains Proposed | Mark blocked unless a valid gate condition explicitly permits deferral |
| Changed input affects the gate | Require impact replay before a final recommendation |

## Output format

```text
Gate and baseline:
Recommendation:
Criteria assessment:
Evidence strength:
Blockers:
Conditions and owners:
Risks or dissent:
Prior gates to reassess:
Authority action required:
```

## Post-Run Reflection

Apply [core section 5](../core/SKILL.md#5-post-run-reflection-continuous-improvement) for recurring evidence and criterion gaps.

## References

- [Shared protocols](../core/SKILL.md)
- [Gate register](../../../01-preparation/17-gate-register.md)
