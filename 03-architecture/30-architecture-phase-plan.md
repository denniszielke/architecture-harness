# Architecture Phase Plan

> Status: Draft
> Canonical owner: Solution or enterprise architect - name to be assigned
> Required reviewers: Data, platform, security, engineering, operations, test, and FinOps owners
> Entry gate: G2 - Logical design ready for architecture
> Exit gate: G3 - Architecture ready for implementation planning
> Last reviewed: Not reviewed

## Purpose

Turn accepted logical design into a deployable, secure, operable, scalable, and cost-aware target architecture. Map capabilities to products and topology, expose dependencies, define NFR realization, and govern material choices through ADRs.

## Evaluation lenses

Review the architecture across security, reliability, operational excellence, performance efficiency, cost optimization, sustainability, data governance, privacy, portability, and organizational fit. Use current provider guidance and service constraints as evidence, not as automatic approval.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-ARC-01` | Baseline capabilities and requirements | G2 package | [31-enterprise-capabilities.md](31-enterprise-capabilities.md) | Capabilities and requirements have stable links | Not started | Not available |
| `TASK-ARC-02` | Define functional architecture | `TASK-ARC-01` | [32-functional-architecture.md](32-functional-architecture.md) | Domains, interactions, and authority are product-independent and coherent | Not started | Not available |
| `TASK-ARC-03` | Map target solution architecture | `TASK-ARC-01`, `TASK-ARC-02` | [33-target-solution-architecture.md](33-target-solution-architecture.md) | Products, environments, topology, ownership, and constraints are explicit | Not started | Not available |
| `TASK-ARC-04` | Analyze dependencies | `TASK-ARC-02`, `TASK-ARC-03` | [34-functional-dependencies.md](34-functional-dependencies.md) | Critical, optional, organizational, and external dependencies are visible | Not started | Not available |
| `TASK-ARC-05` | Realize NFRs | `TASK-ARC-03`, `TASK-ARC-04` | [35-non-functional-architecture.md](35-non-functional-architecture.md) | Quality attributes map to mechanisms and tests | Not started | Not available |
| `TASK-ARC-06` | Resolve blocking decisions | `TASK-ARC-03`-`TASK-ARC-05` | ADR proposals and decisions | Blocking choices have actual authority outcomes or explicit gate conditions | Not started | Not available |
| `TASK-ARC-07` | Prepare G3 review | `TASK-ARC-01`-`TASK-ARC-06` | Gate recommendation | Implementation-planning boundaries, risks, validation obligations, and unresolved items are clear | Not started | Not available |

## G3 criteria

- Every selected product and shared service has one clear responsibility and owner.
- Topology shows tenants, subscriptions/accounts, regions, environments, networks, trust boundaries, identities, data locations, and management planes.
- Service availability, quotas, limits, licensing, lifecycle, support, networking, identity, encryption, and portability constraints are evidenced.
- NFRs map to architecture mechanisms, observability, and validation.
- Deployment, configuration, promotion, rollback, backup, recovery, and decommissioning are defined.
- Indicative capacity, cost range, sensitivity, and major cost drivers inform product and topology decisions.
- Blocking ADRs have valid decisions or explicit gate conditions.
- Implementation-handoff, sizing, security, and operations validation obligations are linked.
- Prototype architecture and target production architecture are visibly different where needed.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Logical component or responsibility | `TASK-ARC-01`, `TASK-ARC-02` | Product map, dependencies, ADRs, backlog |
| Product capability, availability, or lifecycle | `TASK-ARC-03`, related ADR | NFRs, sizing, implementation, operations |
| NFR or scale target | `TASK-ARC-05` | Topology, service tiers, tests, cost |
| Trust, data, tenant, or region boundary | `TASK-ARC-03` and security review | ADRs, data, integration, operations |
| Accepted or superseded ADR | Affected `TASK-ARC` tasks | Design summaries, backlog, tests, costs, claims |
| External platform or organizational dependency | `TASK-ARC-04` | Risk, sequencing, fallback, gate readiness |

Use the [change impact register](../01-preparation/16-change-impact-register.md) and preserve historical ADR rationale. Recheck G3 when a blocking decision, topology, material dependency, or NFR realization changes.
