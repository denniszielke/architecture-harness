# Operating Model Design

> Status: Draft
> Canonical owner: Service owner or operations lead - name to be assigned
> Required reviewers: Business, architecture, security, engineering, support, and FinOps owners
> Gate: G2 and G6
> Last reviewed: Not reviewed

## Responsibility model

| Capability or service | Product owner | Engineering owner | Service owner | Security owner | Data owner | Support tier |
|---|---|---|---|---|---|---|
| [Capability] | [Role] | [Role] | [Role] | [Role] | [Role] | [Tier] |

## Lifecycle model

Describe how a change moves through request, design, decision, build, validation, release, operation, incident, improvement, and retirement.

## Operating scenarios

| Scenario | Trigger | Primary owner | Expected response | Escalation | Evidence |
|---|---|---|---|---|---|
| Provision, deploy, scale, rotate, onboard, offboard, incident, restore, rollback, failover, audit, cost anomaly, or retire | [Trigger] | [Role] | [Response] | [Path] | [Record] |

## Automation boundary

Identify procedures that should be automated, approvals that must remain explicit, break-glass behavior, segregation of duties, and how automation is tested and versioned.

## Service model inputs

- Service hours, support tiers, SLOs, error budgets, maintenance windows, and communication.
- Ownership across platform and workload teams.
- Security operations, vulnerability, patch, identity, key, and certificate processes.
- Data operations, quality, retention, backup, restore, and legal hold.
- FinOps review, budget thresholds, unit cost, and capacity adjustment.
- Vendor support, service health, dependency, continuity, portability, and exit.
