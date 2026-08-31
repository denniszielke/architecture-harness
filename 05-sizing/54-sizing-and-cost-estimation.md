# Sizing and Cost Estimation

> Status: Draft
> Canonical owner: FinOps or finance owner - name to be assigned
> Required reviewers: Business, architecture, engineering, operations, procurement, and finance owners
> Gate: G5
> Last reviewed: Not reviewed

## Estimate context

| Attribute | Value |
|---|---|
| Architecture version | [Commit/tag/date] |
| Region and currency | [Region/currency] |
| Price source and retrieval date | [URL/export/date] |
| Commercial model | [List/reservation/commitment/agreement assumptions] |
| Environments included | [List] |
| Tax, support, people, and contingency treatment | [Included/excluded] |
| Estimate maturity | Architecture estimate / externally calibrated when evidence is available |

## Capacity estimate

| ID | Realization/product | Capability or service | Scale unit | Low | Base | High | Redundancy/headroom | Scale trigger | Source or external evidence |
|---|---|---|---|---:|---:|---:|---|---|---|
| `CAPEST-001` | `REAL/PROD-NNN` | [Capability/service] | [Unit] | [Value] | [Value] | [Value] | [Factor] | [Metric] | [Test/source] |

## Cost estimate

| ID | Realization/product | Cost category | Driver | Unit rate | Quantity | Low | Base | High | Optimization lever |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| `COST-001` | `REAL/PROD-NNN` | [Compute/data/integration/AI/network/observability/security/backup/license/support] | [Driver] | [Rate] | [Quantity] | [Cost] | [Cost] | [Cost] | [Lever] |

## Unit economics

| Unit | Base cost | Range | Main drivers | Measurement owner |
|---|---:|---|---|---|
| [Per user/transaction/event/job/tenant/model call/outcome] | [Cost] | [Low-high] | [Drivers] | [Role] |

## Sensitivity and risk

| Variable | Change | Cost/capacity effect | Threshold | Mitigation or decision |
|---|---|---|---|---|
| [Volume, retention, tokens, region, tier, availability, egress, license] | [+/-] | [Effect] | [Trigger] | [Action/ADR] |

Costs are estimates, not commitments. The same canonical model supports G3 product comparisons and the G5 handoff. When external implementation or performance evidence becomes available, update its assumptions and confidence through change control rather than creating a second model. Preserve source date, commercial exclusions, uncertainty, and the difference between sourced, assumed, and externally measured values.
