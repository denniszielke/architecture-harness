# Prototype and Spike Plan

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Decision owner, architecture, security, test, and affected domain owners
> Gate: G3 or G4 as linked
> Last reviewed: Not reviewed

| Experiment ID | Question | Linked assumption/ADR/NFR | Hypothesis | Planned method and environment | Stop criteria | Expected evidence | Downstream owner | Decision impact |
|---|---|---|---|---|---|---|---|---|
| `EXP-001` | [One material uncertainty] | [IDs] | [Expected observation] | [Reproducible method] | [Enough/unsafe/too costly] | [Logs, metrics, traces, cost, finding] | [Role/team] | [Decision or change path] |

## Experiment record minimum

- Exact question and why documentation alone is insufficient.
- Product, version, region, tier, configuration, identity, network, and dependency context.
- Data volume, shape, sensitivity, generation, and expected result.
- Commands or automation needed to reproduce the experiment.
- Expected observations, logs, metrics, traces, cost, failure, and variance records.
- Security, budget, data, and cleanup guardrails.
- The owner and repository that will execute the plan.
- The decision, sizing model, or design artifact that consumes the result.

This harness frames experiments but does not execute them. A downstream result may support or reject a proposal after it is registered as external evidence. It cannot by itself accept an ADR or prove production readiness.
