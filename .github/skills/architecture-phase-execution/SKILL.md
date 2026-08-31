---
name: architecture-phase-execution
description: "Execute or re-run a phase or individual task in the architecture harness. Use this skill whenever the user asks to start, continue, redo, replay, plan, or complete framing, preparation, design, architecture, implementation, sizing, operations, or presentation work."
---

# Architecture Phase Execution

## Prerequisites

- An architecture-harness repository with `architecture-harness.json`.
- Read access to governance, the relevant phase plan, and direct inputs.
- Edit and execution access only when the user requests artifact changes.

## Workflow

1. Read the manifest, governance, phase plan, open change records, gate record, and direct inputs.
2. Classify task status as `Not started`, `Ready`, `Blocked`, `In progress`, `Replay required`, or `Complete with evidence`.
3. Select one bounded task with satisfied dependencies.
4. State canonical owner, expected output, exclusions, evidence, completion check, and handoff.
5. Execute through the matching specialist agent or repository workflow.
6. Update the canonical artifact before summaries, plans, and registers.
7. Run the smallest relevant validation.
8. Prepare a readiness recommendation only when phase criteria are evidenced.

## Error handling

| Failure | Action |
|---|---|
| Entry gate or dependency missing | Mark blocked and identify the exact owner/action |
| Material decision unresolved | Route to the ADR Proposal Partner |
| Input changed | Use the impact-analysis skill before execution |
| Validation failed | Keep task incomplete and report evidence |
| Scope is ambiguous | Ask one focused question about the outcome or boundary |

## Output format

```text
Phase and gate:
Selected task and why ready:
Canonical artifacts:
Changes and evidence:
Blockers or decisions:
Replay and gate impact:
Next recommended action:
```

## Post-Run Reflection

Apply [core section 5](../core/SKILL.md#5-post-run-reflection-continuous-improvement) and update only reusable harness behavior.

## References

- [Shared protocols](../core/SKILL.md)
- The phase plan identified in `architecture-harness.json`
