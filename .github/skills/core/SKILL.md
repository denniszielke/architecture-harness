---
name: core
description: "Shared architecture-harness protocols used by the phase execution, impact analysis, and gate review skills. Use when another harness skill references evidence classification, safe updates, errors, or post-run reflection."
---

# Architecture Harness Core

## 1. Canonical ownership

Update the artifact that owns a fact, assumption, requirement, decision, design detail, result, or claim. Summaries link to it.

## 2. Evidence classes

Keep source fact, assumption, target, proposal, accepted decision, designed behavior, demonstrated result, operational evidence, and future commitment distinct. Demonstrated and operational evidence must cite the external or downstream source that produced it.

## 3. Safe update order

1. Read governance, the relevant phase plan, and the current canonical artifact.
2. Update the canonical source.
3. Update direct dependents and summaries.
4. Run relevant validation.
5. Update readiness records last.

## 4. Error handling

| Condition | Required action |
|---|---|
| Missing source or authority | Record an open question or assumption; do not invent it |
| Conflicting accepted artifacts | Stop the affected task, record the conflict, and route change control |
| Unresolved material choice | Create or refine a Proposed ADR |
| Missing evidence | Mark the criterion not evidenced; do not create success-shaped text |
| Failed validation | Keep the task incomplete and report the failure |
| Restricted or sensitive content | Do not copy it into prompts, examples, logs, or new artifacts |

## 5. Post-run reflection (continuous improvement)

After a run, record only durable improvements:

- missing task dependency or replay trigger;
- ambiguous canonical ownership;
- validation that should be automated;
- recurring evidence or handoff gap;
- agent or skill instruction that caused incorrect routing.

Record the improvement as a `CHG-NNN` proposal with affected artifacts and evidence. Do not modify governance, repository instructions, skills, or the validator unless the user explicitly authorizes that harness change.
