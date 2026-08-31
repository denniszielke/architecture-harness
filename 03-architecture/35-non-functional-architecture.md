# Non-Functional Architecture

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Business, security, platform, data, engineering, operations, test, and FinOps owners
> Gate: G3, G5, and G6
> Last reviewed: Not reviewed

## NFR register

| Requirement ID | Quality attribute | Accepted scenario and target | Architecture mechanism | Observability | Validation | Owner |
|---|---|---|---|---|---|---|---|
| `NFR-NNN` | [Security/reliability/performance/scale/operability/cost/privacy/accessibility/portability] | [Link to design requirement] | [Mechanism] | [Signal] | `TEST-<phase>-NNN` | [Role] |

The requirement and threshold are canonical in [../02-design/23-requirements-and-acceptance.md](../02-design/23-requirements-and-acceptance.md). This artifact owns architecture realization and trade-offs.

## Required quality scenarios

- Security: identity compromise, unauthorized data path, secret exposure, policy drift, and supply-chain compromise.
- Reliability: zone, region, dependency, data, deployment, and operator failures.
- Performance: steady, peak, burst, batch-window, concurrency, and latency-sensitive paths.
- Scale: data volume, throughput, users, tenants, partitions, models, events, and retention growth.
- Operations: detection, diagnosis, recovery, rollback, onboarding, patching, and routine change.
- Cost: baseline, peak, idle, growth, failure, retention, egress, licensing, and support.
- Portability: service replacement, data export, configuration recreation, and provider exit.

## Trade-offs

| NFR tension | Chosen balance or proposal | Consequence | ADR |
|---|---|---|---|
| [Example: consistency versus availability] | [Position] | [Consequence] | `ADR-NNN` |

## Evidence maturity

Mark each NFR as `Specified`, `Designed`, `Tested`, or `Observed in operation`. Never infer a higher level from documentation alone.
