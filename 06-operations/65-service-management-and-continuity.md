# Service Management and Continuity

> Status: Draft
> Canonical owner: Service owner - name to be assigned
> Required reviewers: Business, engineering, platform, security, data, support, continuity, and vendor owners
> Gate: G6
> Last reviewed: Not reviewed

This artifact translates the logical resilience design and NFR architecture into a service-management and continuity plan. Those artifacts own required behavior and mechanisms; this artifact owns planned processes, exercises, continuity, recovery, and evidence expectations.

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

| Scenario | Business workaround | Technical recovery | Dependency action | Exercise frequency | Expected evidence |
|---|---|---|---|---|---|
| [Region/service/data/identity/network/vendor/team failure] | [Continuity mode] | [Procedure] | [Action] | [Frequency] | [Link] |

## Exercise specification

Specify scenario, participants, environment, injected failure, expected behavior, success criteria, required detection and recovery observations, RTO/RPO measurement, data-integrity checks, communication, manual-effort and cost measures, and downstream owner.

## Operational test and exercise register

| Test ID | Scenario or procedure | Planned environment | Expected result | Required evidence | Downstream owner | Status |
|---|---|---|---|---|---|---|
| `TEST-OPS-001` | [Incident, restore, failover, continuity, rollout, access, or security operation] | [Context] | [Threshold] | [Record, logs, measurements, review] | [Role/team] | Planned |

Register relevant downstream results and limitations in the [external evidence register](../01-preparation/19-external-evidence-register.md).

## Retirement and exit

[Define data and configuration export, evidence retention, identity and access removal, dependency removal, resource deletion, contract exit, knowledge transfer, and proof of closure.]

G6 confirms that the operating model and validation plan are ready. It does not prove that the service has operated or recovered successfully.
