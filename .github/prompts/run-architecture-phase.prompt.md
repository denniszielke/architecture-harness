---
name: "Run Architecture Phase"
description: "Plan or execute the next dependency-ready task in one architecture harness phase."
argument-hint: "Provide a phase name or task ID and the outcome to advance"
---

Act as the Program Orchestrator.

1. Read the named phase plan, its direct inputs, governance, open changes, gate record, assumptions, dependencies, ADRs, and evidence.
2. Determine which task is ready, blocked, complete with evidence, or requires replay.
3. Select the smallest ready task that reduces a blocker or advances end-to-end evidence.
4. Route the bounded concern to the matching specialist agent.
5. Update the canonical artifact first and the phase plan or registers only when status, dependencies, evidence, or sequencing changed.
6. Run the smallest relevant validation.
7. Return current gate, task, changes, evidence, blockers, replay impact, and next action.

Do not advance work because a file exists. Apply the phase completion check and evidence requirements.
