# Sizing Plan

> Status: Draft
> Canonical owner: Performance or FinOps lead - name to be assigned
> Required reviewers: Business, architecture, data, engineering, test, operations, and finance owners
> May start after: G2 with an indicative model; G4 handoff provides implementation context
> Exit gate: G5 - Sizing model and validation plan ready
> Last reviewed: Not reviewed

## Purpose

Turn workload assumptions, architecture constraints, service characteristics, and available external evidence into a capacity and cost model with confidence ranges, observability requirements, validation plans, and scaling triggers. The harness does not execute performance tests or claim calibrated implementation results.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-SIZE-01` | Build workload model | G2 design; refine at G3/G4 | [51-sizing-assumptions.md](51-sizing-assumptions.md) | Users, data, throughput, retention, growth, peaks, and confidence are bounded | Not started | Not available |
| `TASK-SIZE-02` | Define telemetry and unit measures | `TASK-SIZE-01` | [52-observability-and-key-metrics.md](52-observability-and-key-metrics.md) | Each driver has an observable measure | Not started | Not available |
| `TASK-SIZE-03` | Build indicative capacity and cost estimate | `TASK-SIZE-01`, `TASK-SIZE-02`, candidate product map | [54-sizing-and-cost-estimation.md](54-sizing-and-cost-estimation.md) | G3 product and topology comparisons have traceable ranges and sensitivity | Not started | Not available |
| `TASK-SIZE-04` | Define sizing validation plan | `TASK-SIZE-01`-`TASK-SIZE-03`, G4 context | [53-sizing-tests.md](53-sizing-tests.md) | Planned tests cover representative, peak, failure, recovery, and growth cases | Not started | Not available |
| `TASK-SIZE-05` | Define scale, budget, and calibration actions | `TASK-SIZE-02`-`TASK-SIZE-04` | Thresholds, downstream owners, and feedback path | Scale, throttle, optimize, redesign, budget, and re-estimate triggers are explicit | Not started | Not available |
| `TASK-SIZE-06` | Prepare G5 review | `TASK-SIZE-01`-`TASK-SIZE-05` | Gate recommendation | Assumptions, ranges, confidence, validation, gaps, and financial exposure are visible | Not started | Not available |

## G5 criteria

- Workload units, steady state, peaks, seasonality, retention, growth, and failure cases are defined.
- The validation plan defines representative data, architecture, workloads, methods, thresholds, and expected evidence.
- Capacity and cost include application, data, integration, AI, network, observability, security, backup, non-production, licenses, support, and people where relevant.
- Rates have source, region, currency, date, commercial assumptions, and exclusions.
- Estimates include low/base/high or equivalent sensitivity ranges.
- Scaling, optimization, budget, calibration, and re-estimation triggers have downstream owners.
- External measurements are linked and bounded when available; their absence remains an explicit confidence limitation.
- G5 does not claim that performance, scale, or cost has been demonstrated.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Volume, growth, concurrency, or retention | `TASK-SIZE-01` | Tests, capacity, cost, operations |
| Architecture product, tier, region, or topology | `TASK-SIZE-03`, `TASK-SIZE-04` | NFRs, handoff, operations |
| External test result or optimization finding | `TASK-SIZE-01`, `TASK-SIZE-03`, `TASK-SIZE-05` | Confidence, thresholds, risks, claims |
| Pricing, licensing, or support model | `TASK-SIZE-03`, `TASK-SIZE-05` | Business value and gate evidence |
| SLO, RTO, or RPO | `TASK-SIZE-01`, `TASK-SIZE-03`, `TASK-SIZE-04` | Redundancy, operations, cost |

Recheck G5 when a cost driver, representative workload, pricing basis, required service level, validation method, or relevant external result materially changes.
