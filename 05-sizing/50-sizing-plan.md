# Sizing Plan

> Status: Draft
> Canonical owner: Performance or FinOps lead - name to be assigned
> Required reviewers: Business, architecture, data, engineering, test, operations, and finance owners
> May start after: G2 with an indicative model; G4 evidence required for calibrated estimates
> Exit gate: G5 - Sizing confidence accepted
> Last reviewed: Not reviewed

## Purpose

Turn workload assumptions and measured implementation behavior into capacity, performance, availability, and cost estimates with confidence ranges and scaling triggers. Indicative G3 estimates inform architecture decisions; G4 measurements calibrate the G5 estimate.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-SIZE-01` | Build workload model | G2 design; refine at G3/G4 | [51-sizing-assumptions.md](51-sizing-assumptions.md) | Users, data, throughput, retention, growth, and peaks are bounded | Not started | Not available |
| `TASK-SIZE-02` | Define telemetry and unit measures | `TASK-SIZE-01` | [52-observability-and-key-metrics.md](52-observability-and-key-metrics.md) | Each driver has an observable measure | Not started | Not available |
| `TASK-SIZE-03` | Build indicative capacity and cost estimate | `TASK-SIZE-01`, `TASK-SIZE-02`, candidate product map | [54-sizing-and-cost-estimation.md](54-sizing-and-cost-estimation.md) | G3 product and topology comparisons have traceable ranges and sensitivity | Not started | Not available |
| `TASK-SIZE-04` | Design and run sizing tests | `TASK-SIZE-01`, G4 environment | [53-sizing-tests.md](53-sizing-tests.md) | Tests cover representative, peak, failure, and growth cases | Not started | Not available |
| `TASK-SIZE-05` | Calibrate capacity and cost | `TASK-SIZE-03`, `TASK-SIZE-04` | [54-sizing-and-cost-estimation.md](54-sizing-and-cost-estimation.md) | Measured behavior replaces or bounds indicative assumptions | Not started | Not available |
| `TASK-SIZE-06` | Define scale and budget actions | `TASK-SIZE-05` | Thresholds and owner actions | Scale, throttle, optimize, or redesign triggers are explicit | Not started | Not available |
| `TASK-SIZE-07` | Prepare G5 review | `TASK-SIZE-01`-`TASK-SIZE-06` | Gate recommendation | Confidence, gaps, and financial exposure are visible | Not started | Not available |

## G5 criteria

- Workload units, steady state, peaks, seasonality, retention, growth, and failure cases are defined.
- Tests use representative data and architecture or declare the extrapolation gap.
- Capacity and cost include application, data, integration, AI, network, observability, security, backup, non-production, licenses, support, and people where relevant.
- Rates have source, region, currency, date, commercial assumptions, and exclusions.
- Estimates include low/base/high or equivalent sensitivity ranges.
- Scaling, optimization, budget, and re-test triggers have owners.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Volume, growth, concurrency, or retention | `TASK-SIZE-01` | Tests, capacity, cost, operations |
| Architecture product, tier, region, or topology | `TASK-SIZE-03`, then `TASK-SIZE-04`-`TASK-SIZE-05` when implemented | NFRs, release, operations |
| Test result or optimization | `TASK-SIZE-05` | Scale thresholds, budget, claims |
| Pricing, licensing, or support model | `TASK-SIZE-03`, `TASK-SIZE-05` | Business value and gate evidence |
| SLO, RTO, or RPO | `TASK-SIZE-01`, `TASK-SIZE-03`, `TASK-SIZE-04` | Redundancy, operations, cost |

Recheck G5 when a cost driver, representative workload, pricing basis, or required service level materially changes.
