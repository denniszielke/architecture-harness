# Operations Plan

> Status: Draft
> Canonical owner: Service owner or operations lead - name to be assigned
> Required reviewers: Product, architecture, security, engineering, support, data, and FinOps owners
> May start after: G1 for operating-model design; G4 and G5 provide handoff and sizing context
> Exit gate: G6 - Operating model and operational-readiness plan ready
> Last reviewed: Not reviewed

## Purpose

Define how the solution should be owned, observed, secured, changed, supported, recovered, scaled, rolled out, and retired. The phase produces an operating model and readiness plan; it does not operate services, automate procedures, execute exercises, or prove production readiness.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-OPS-01` | Establish service ownership | G1 design start; refine at G3 | [61-roles-and-responsibilities.md](61-roles-and-responsibilities.md) | Every service and procedure has an accountable role | Not started | Not available |
| `TASK-OPS-02` | Define standard-procedure automation requirements | G4 | [62-standard-operating-procedure-automation.md](62-standard-operating-procedure-automation.md) | High-frequency and high-risk procedures have safe automation specifications | Not started | Not available |
| `TASK-OPS-03` | Define operational security model | G3, G4 | [63-security-concept.md](63-security-concept.md) | Identity, vulnerability, threat, incident, and evidence processes are owned and measurable | Not started | Not available |
| `TASK-OPS-04` | Plan rollout and deployment | G4, G5 | [64-rollout-and-deployment.md](64-rollout-and-deployment.md) | Promotion, migration, rollback, onboarding, communication, and validation are specified | Not started | Not available |
| `TASK-OPS-05` | Define service management and continuity validation | G4, G5 | [65-service-management-and-continuity.md](65-service-management-and-continuity.md) | SLO, incident, backup, recovery, continuity, vendor, and exercise plans are complete | Not started | Not available |
| `TASK-OPS-06` | Prepare G6 review | `TASK-OPS-01`-`TASK-OPS-05` | Gate recommendation | Operating ownership, plans, validation obligations, gaps, and risks are explicit | Not started | Not available |

## G6 criteria

- Service, platform, data, security, vendor, support, and business accountabilities are defined, with assignment gaps visible.
- Monitoring, alerting, on-call, escalation, communication, incident, and problem processes are specified.
- Access, secrets, keys, certificates, vulnerabilities, patches, policy, and evidence procedures have owners, controls, metrics, and validation plans.
- Deployment, rollback, migration, onboarding, offboarding, capacity, budget, backup, restore, failover, and continuity plans are implementation-ready.
- SLOs, error budgets, service hours, support model, dependency obligations, and residual-risk decisions are defined or explicitly open.
- Operational tests and exercises specify scenarios, methods, success criteria, expected evidence, and downstream owners.
- External operational evidence is linked when available; G6 does not claim operating effectiveness.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Architecture or dependency | `TASK-OPS-01`, affected procedure | Monitoring, security, continuity, rollout |
| Deployment process | `TASK-OPS-02`, `TASK-OPS-04` | Access, rollback, release validation |
| Threat, incident, or policy | `TASK-OPS-03` | Design, architecture, procedures, training |
| Workload, SLO, or cost threshold | `TASK-OPS-05` | Capacity, on-call, budget, continuity |
| Team or vendor responsibility | `TASK-OPS-01` | Escalation, access, contracts, runbooks |

Recheck G6 when ownership, intended operating context, service objectives, security posture, deployment, continuity planning, validation obligations, or relevant external evidence changes.
