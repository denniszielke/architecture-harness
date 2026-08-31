# Sizing and Performance Tests

> Status: Draft
> Canonical owner: Performance test lead - name to be assigned
> Required reviewers: Architecture, engineering, data, security, operations, and FinOps owners
> Gate: G5
> Last reviewed: Not reviewed

| Test ID | Workload scenario | Architecture/configuration | Data shape | Duration | Success criteria | Actual result | Cost observed | Evidence |
|---|---|---|---|---|---|---|---|---|
| `TEST-SIZE-001` | [Steady/peak/burst/endurance/growth/failure/recovery] | [Versioned setup] | [Representative data] | [Time] | [NFR threshold] | Not run | Not measured | [Link] |

Register durable results and their limitations in [../04-implementation/48-evidence-index.md](../04-implementation/48-evidence-index.md).

## Test progression

1. Component benchmark for obvious bottlenecks.
2. End-to-end steady-state test.
3. Peak and burst behavior.
4. Endurance and accumulation behavior.
5. Dependency throttling, outage, retry, replay, and recovery load.
6. Scale-out and scale-in transitions.
7. Failover and reduced-capacity operation.
8. Cost and observability overhead.

## Test quality

- Warm-up, run, and cool-down periods are explicit.
- Data distribution and query or event mix match the workload model.
- Client, network, dependency, and telemetry bottlenecks are distinguished.
- Repeats and variance are recorded.
- Autoscale minimum, maximum, step, delay, and cooldown are visible.
- Tests stop safely when cost, quota, stability, or security thresholds are crossed.

## Extrapolation

[Explain any difference between tested and target scale, the model used to extrapolate, confidence, nonlinear risks, and the next trigger for a larger test.]
