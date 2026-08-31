# Service Management and Continuity

> Status: Draft
> Canonical owner: Service owner - name to be assigned
> Required reviewers: Business, engineering, platform, security, data, support, continuity, and vendor owners
> Gate: G6
> Last reviewed: Not reviewed

This artifact operationalizes the logical resilience design and NFR architecture. Those artifacts own required behavior and mechanisms; this artifact owns live service processes, exercises, continuity, and recovery evidence.

## Service definition

| Attribute | Value |
|---|---|
| Service and business owner | [Roles] |
| Users and critical journeys | [Links] |
| Service hours and support model | [Hours/tiers] |
| SLOs and error budgets | [Links] |
| Critical dependencies | [Links] |
| RTO/RPO and continuity mode | [Targets] |
| Data, security, and evidence classification | [Classes] |

## Management processes

| Process | Trigger | Owner | Target | Tool or record | Escalation |
|---|---|---|---|---|---|
| Incident, request, problem, change, release, capacity, availability, continuity, vendor, cost, or retirement | [Trigger] | [Role] | [Target] | [System] | [Path] |

## Continuity and recovery

| Scenario | Business workaround | Technical recovery | Dependency action | Exercise frequency | Evidence |
|---|---|---|---|---|---|
| [Region/service/data/identity/network/vendor/team failure] | [Continuity mode] | [Procedure] | [Action] | [Frequency] | [Link] |

## Exercise record

Record scenario, participants, environment, injected failure, expected behavior, actual detection and recovery, RTO/RPO achieved, data integrity, communication, manual effort, cost, unresolved gaps, and follow-up owner.

## Operational test and exercise register

| Test ID | Scenario or procedure | Environment | Expected result | Actual result | Evidence | Owner | Status |
|---|---|---|---|---|---|---|---|
| `TEST-OPS-001` | [Incident, restore, failover, continuity, rollout, access, or security operation] | [Context] | [Threshold] | Not run | `EVID-NNN` | [Role] | Planned |

Register durable results and limitations in [../04-implementation/48-evidence-index.md](../04-implementation/48-evidence-index.md).

## Retirement and exit

[Define data and configuration export, evidence retention, identity and access removal, dependency removal, resource deletion, contract exit, knowledge transfer, and proof of closure.]
