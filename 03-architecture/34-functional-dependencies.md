# Functional and Delivery Dependencies

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Program, platform, data, security, engineering, operations, procurement, and vendor owners
> Gate: G3 and continuous review
> Last reviewed: Not reviewed

| ID | Dependent capability or task | Dependency | Type | Owner | Required by | Failure impact | Fallback or decoupling | Evidence/status |
|---|---|---|---|---|---|---|---|---|
| `DEP-001` | `CAP/TASK-ARC/IMP-NNN` | [Capability, service, team, decision, data, contract, quota, license, policy, environment, or vendor] | [Hard/soft/external/transitional] | [Role] | [Date/gate/task] | [Impact] | [Fallback] | [Status/link] |

## Dependency rules

- A hard dependency blocks the dependent task unless an explicit experiment or exception bounds the impact.
- A shared platform dependency must declare service levels, ownership, onboarding, support, change notification, and exit behavior.
- An external SaaS or provider dependency must declare data, identity, network, contractual, continuity, and concentration implications.
- Transitional coupling must have an exit task and trigger.
- Critical dependencies appear in resilience tests, implementation sequencing, and operational procedures.

## Dependency views

Maintain a dependency graph or diagram when the table no longer makes critical paths, cycles, or blast radius obvious. Link graph nodes to stable IDs rather than duplicating detail.
