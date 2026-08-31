# Change Impact and Replay Register

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Owners of affected artifacts and gates
> Gate: Continuous
> Last reviewed: Not reviewed

Use one row per material input change. Minor editorial changes that do not alter meaning need no replay record.

| Change ID | Date | Changed input and canonical source | Old meaning | New meaning | Direct links | Tasks to replay | Gates to recheck | Owner role | Status |
|---|---|---|---|---|---|---|---|---|---|
| `CHG-001` | [YYYY-MM-DD] | [Path and record ID] | [Prior meaning] | [New meaning] | [Artifact/record links] | [Task IDs] | [Gate IDs] | [Role] | Open |

## Replay status

- `Open`: impact is not yet bounded.
- `Assessed`: affected artifacts, tasks, tests, decisions, and gates are identified.
- `In replay`: canonical and dependent updates are in progress.
- `Ready for review`: replay and validation are complete.
- `Closed`: required reviewers accepted the reconciliation; this is not itself a gate approval.

## Impact checklist

- Framing facts, assumptions, goals, constraints, or authorities.
- Objectives, scope, deliverables, acceptance, or governance.
- Logical behavior, data, integrations, security, resilience, or operating model.
- Capability mapping, topology, NFRs, ADRs, dependencies, or service constraints.
- Backlog, environments, automation, code, tests, or evidence.
- Workload model, telemetry, performance, capacity, cost, or sensitivity.
- Capability realization, required products, delivery effort, labor cost, or implementation waves.
- Roles, procedures, security operations, recovery, rollout, or support.
- Presentation claims, diagrams, value story, caveats, or requested decision.
- Architecture-validated scenario coverage or overall assessment.
