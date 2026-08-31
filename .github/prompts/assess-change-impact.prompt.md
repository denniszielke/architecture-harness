---
name: "Assess Architecture Change Impact"
description: "Trace a changed input through architecture artifacts, select the smallest replay set, and identify gates to recheck."
argument-hint: "Describe the changed fact, assumption, objective, scope, decision, product constraint, test result, or operating dependency"
---

Use the architecture impact-analysis skill.

1. Identify the canonical source and compare old and new meaning.
2. Create or update a `CHG-NNN` entry.
3. Traverse direct identifiers and links, then phase-plan dependencies.
4. Identify affected artifacts, tasks, ADRs, tests, evidence, risks, costs, operations procedures, and presentation claims.
5. Mark only the affected task set for replay and explain why unaffected accepted work remains valid.
6. Preserve historical decisions and gate records.
7. Update the canonical source first, then dependent summaries after replay.
8. Report evidence invalidated, validation required, and gates to recheck.
