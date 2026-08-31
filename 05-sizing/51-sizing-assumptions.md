# Sizing Assumptions

> Status: Draft
> Canonical owner: Performance or FinOps lead - name to be assigned
> Required reviewers: Business, architecture, data, engineering, and operations owners
> Gate: G5
> Last reviewed: Not reviewed

| ID | Workload dimension | Unit | Low | Base | High | Peak or seasonality | Growth | Source or assumption | Validation |
|---|---|---|---:|---:|---:|---|---|---|---|
| `SIZE-A-001` | [Users, requests, events, jobs, records, files, tokens, models, tenants, storage] | [Unit/time] | [Value] | [Value] | [Value] | [Factor/window] | [Rate] | `SRC/ASM-NNN` | [Test/telemetry] |

## Architecture overhead

Capture redundancy, retries, replay, dead letters, indexes, caches, replicas, backups, logs, traces, non-production, deployment overlap, failover reserve, and recovery processing.

## Distribution assumptions

[Record payload and record sizes, partition/cardinality, hot/cold split, read/write ratio, query complexity, concurrency distribution, token/input/output size, batch windows, and data locality.]

## Confidence

| Assumption | Confidence | Sensitivity | Action if wrong |
|---|---|---|---|
| `SIZE-A-001` | Low/Medium/High | [Cost/performance/availability effect] | [Measure, cap, scale, redesign] |
