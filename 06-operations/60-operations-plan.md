# Operations Plan

> Status: Draft
> Canonical owner: Service owner or operations lead - name to be assigned
> Required reviewers: Product, architecture, security, engineering, support, data, and FinOps owners
> May start after: G1 for operating-model design; G4 and G5 evidence required for G6
> Exit gate: G6 - Operational readiness accepted
> Last reviewed: Not reviewed

## Purpose

Define how the solution is owned, observed, secured, changed, supported, recovered, scaled, rolled out, and retired in the intended operating context.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-OPS-01` | Establish service ownership | G1 design start; refine at G3 | [61-roles-and-responsibilities.md](61-roles-and-responsibilities.md) | Every service and procedure has an accountable role | Not started | Not available |
| `TASK-OPS-02` | Automate standard procedures | G4 | [62-standard-operating-procedure-automation.md](62-standard-operating-procedure-automation.md) | High-frequency and high-risk procedures are versioned and tested | Not started | Not available |
| `TASK-OPS-03` | Operationalize security | G3, G4 | [63-security-concept.md](63-security-concept.md) | Identity, vulnerability, threat, incident, and evidence processes are owned | Not started | Not available |
| `TASK-OPS-04` | Plan rollout and deployment | G4, G5 | [64-rollout-and-deployment.md](64-rollout-and-deployment.md) | Promotion, migration, rollback, onboarding, and communication are testable | Not started | Not available |
| `TASK-OPS-05` | Establish service continuity | G4, G5 | [65-service-management-and-continuity.md](65-service-management-and-continuity.md) | SLO, incident, backup, recovery, continuity, and vendor paths are exercised | Not started | Not available |
| `TASK-OPS-06` | Prepare G6 review | `TASK-OPS-01`-`TASK-OPS-05` | Gate recommendation | Owners can operate and recover the service with accepted risk | Not started | Not available |

## G6 criteria

- Service, platform, data, security, vendor, support, and business ownership are accepted.
- Monitoring, alerting, on-call, escalation, communication, incident, and problem processes are tested.
- Access, secrets, keys, certificates, vulnerabilities, patches, policy, and evidence procedures are owned and measurable.
- Deployment, rollback, migration, onboarding, offboarding, capacity, budget, backup, restore, failover, and continuity procedures are exercised.
- SLOs, error budgets, service hours, support model, dependency obligations, and residual risks are accepted.
- Operational evidence exists for the intended scope; designed-only procedures are clearly labeled.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Architecture or dependency | `TASK-OPS-01`, affected procedure | Monitoring, security, continuity, rollout |
| Deployment process | `TASK-OPS-02`, `TASK-OPS-04` | Access, rollback, release evidence |
| Threat, incident, or policy | `TASK-OPS-03` | Design, architecture, procedures, training |
| Workload, SLO, or cost threshold | `TASK-OPS-05` | Capacity, on-call, budget, continuity |
| Team or vendor responsibility | `TASK-OPS-01` | Escalation, access, contracts, runbooks |

Recheck G6 when ownership, intended operating context, service objectives, security posture, deployment, or continuity evidence changes.
