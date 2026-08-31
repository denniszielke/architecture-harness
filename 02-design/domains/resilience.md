# Resilience Design

> Status: Draft
> Canonical owner: Solution architect or service owner - name to be assigned
> Required reviewers: Business, platform, data, security, engineering, operations, and test owners
> Gate: G2, G3, and G6
> Last reviewed: Not reviewed

## Critical journeys and objectives

| Journey or capability | Criticality | Availability target | RTO | RPO | Maximum degraded period | Data-loss consequence |
|---|---|---|---|---|---|---|
| [Journey] | [Tier] | [Target] | [Time] | [Time] | [Time] | [Impact] |

## Failure model

| Failure domain | Example | Detection | Containment | Degraded mode | Recovery | Test |
|---|---|---|---|---|---|---|
| Identity, region, zone, network, runtime, data, integration, AI, dependency, deployment, or operator | [Failure] | [Signal] | [Boundary] | [Behavior] | [Procedure] | `TEST-<phase>-NNN` |

## Resilience mechanisms

- Stateless or recoverable compute, queueing, backpressure, retry budgets, idempotency, and replay.
- Data redundancy, backup, point-in-time restore, integrity validation, and reconstruction.
- Zone and region strategy driven by business objectives and service capability.
- Dependency isolation, circuit breaking, fallback, manual continuity, and safe shutdown.
- Version-compatible rollback, configuration recovery, and infrastructure recreation.
- Regular exercises with observed recovery time, data loss, manual effort, and unresolved gaps.

## Evidence needed

[List architecture experiments, implementation tests, restore exercises, failover tests, chaos scenarios, and operational drills needed to move from designed to demonstrated or operational evidence.]
