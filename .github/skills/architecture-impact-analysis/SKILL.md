---
name: architecture-impact-analysis
description: "Trace changed inputs and select task-level replay across the architecture harness. Use this skill whenever a fact, assumption, goal, objective, scope item, requirement, design, ADR, product constraint, test result, price, dependency, or operating responsibility changes."
---

# Architecture Impact Analysis

## Prerequisites

- The changed input or evidence and its canonical source.
- `01-preparation/16-change-impact-register.md`.
- Directly linked artifacts and relevant phase plans.

## Workflow

1. Identify the canonical record and compare old and new meaning.
2. Classify the change as correction, new evidence, assumption outcome, scope change, decision change, implementation finding, service change, or operating change.
3. Create or update `CHG-NNN`.
4. Traverse direct identifiers and links.
5. Traverse phase-plan dependencies from the earliest affected task.
6. Identify ADRs, tests, evidence, risks, estimates, procedures, gates, and claims that are invalidated or need review.
7. Choose the smallest replay set that restores consistency.
8. Preserve unaffected accepted work and historical records.
9. Update the canonical source first; close the change only after validation and review.

## Error handling

| Failure | Action |
|---|---|
| Old meaning is unavailable | Record the evidence gap and do not rewrite accepted history |
| No stable links exist | Search by record ID and concept, then add missing traceability |
| Impact crosses an accepted ADR | Propose a superseding ADR; do not edit the old rationale |
| Gate evidence becomes invalid | Mark readiness for reassessment without erasing the prior decision |
| Change scope is unbounded | Split into separate `CHG` records by canonical source |

## Output format

```text
Change ID and classification:
Canonical old/new meaning:
Directly affected records:
Tasks to replay in order:
Evidence invalidated or required:
ADRs and gates to recheck:
Unaffected work preserved:
Owner and next action:
```

## Post-Run Reflection

Apply [core section 5](../core/SKILL.md#5-post-run-reflection-continuous-improvement), especially for missing dependency or replay rules.

## References

- [Shared protocols](../core/SKILL.md)
- [Change register](../../../01-preparation/16-change-impact-register.md)
