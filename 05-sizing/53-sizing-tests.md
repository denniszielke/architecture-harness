# Sizing Validation Plan

> Status: Draft
> Canonical owner: Performance test lead - name to be assigned
> Required reviewers: Architecture, engineering, data, security, operations, and FinOps owners
> Gate: G5
> Last reviewed: Not reviewed

| Test ID | Workload scenario | Planned architecture/configuration | Data shape | Duration | Success criteria | Required observations | Downstream owner | External evidence |
|---|---|---|---|---|---|---|---|---|
| `TEST-SIZE-001` | [Steady/peak/burst/endurance/growth/failure/recovery] | [Versioned setup] | [Representative data] | [Time] | [NFR threshold] | [Latency, throughput, saturation, errors, cost] | [Role/team] | [Link when available] |

Register relevant downstream results and their limitations in the [external evidence register](../01-preparation/19-external-evidence-register.md).

## Planned test progression

1. Component benchmark for obvious bottlenecks.
2. End-to-end steady-state test.
3. Peak and burst behavior.
4. Endurance and accumulation behavior.
5. Dependency throttling, outage, retry, replay, and recovery load.
6. Scale-out and scale-in transitions.
7. Failover and reduced-capacity operation.
8. Cost and observability overhead.

## Validation-plan quality

- Warm-up, run, and cool-down periods are explicit.
- Data distribution and query or event mix match the workload model.
- Client, network, dependency, and telemetry bottlenecks are distinguished.
- Required repeats, variance, and confidence treatment are specified.
- Autoscale minimum, maximum, step, delay, and cooldown are visible.
- Stop conditions protect cost, quota, stability, data, and security boundaries.

## Extrapolation

[Define how downstream results will be compared with target scale, the model used to extrapolate, confidence treatment, nonlinear risks, and the trigger for a larger test.]

This artifact is a validation specification. Test execution and results belong to the downstream implementation or performance-testing environment.
