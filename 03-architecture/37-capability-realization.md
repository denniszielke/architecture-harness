# Capability Realization and Product Inventory

> Status: Draft
> Canonical owner: Solution or enterprise architect - name to be assigned
> Required reviewers: Business, product, engineering, platform, security, operations, procurement, and FinOps owners
> Gate: G3
> Last reviewed: Not reviewed

This artifact is the canonical source for how each required capability is realized. It connects business outcomes and product-independent capabilities to purchased products, configured platforms, reused enterprise services, integrations, custom functional building blocks, and retirement actions.

## Realization strategies

| Strategy | Meaning | Minimum evidence |
|---|---|---|
| `Buy` | Acquire a commercial product or managed service that owns the capability | Product fit, constraints, licensing, support, security, operations, cost, exit, and accepted ADR |
| `Configure` | Realize the capability mainly through supported product configuration or low-code composition | Configuration boundary, extension limits, ownership, lifecycle, licensing, and accepted product decision |
| `Build` | Create custom code or infrastructure for the capability | Bounded custom responsibility, interfaces, security/NFR constraints, effort drivers, and downstream owner; concrete building blocks and contexts follow at G4 |
| `Reuse` | Consume an existing internal platform, service, component, or process | Service contract, owner, SLO, capacity, cost allocation, constraints, and onboarding approval |
| `Integrate` | Assemble the capability by orchestrating existing products or services without one product owning it | Integration ownership, contracts, failure behavior, operating responsibility, and dependency evidence |
| `Retire` | Remove or replace an existing capability or component | Migration, coexistence, data/evidence retention, decommissioning, and exit plan |

Use one primary strategy per bounded capability responsibility. Split a capability into multiple rows when different responsibilities use different strategies.

## Capability realization map

| ID | Capability | Scenario and objective | Strategy | Product or service | Custom-build boundary or G4 building block | Governing ADR | Dependencies | Delivery effort | Cloud/service cost | Operating owner | Validation and gaps | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `REAL-001` | `CAP-NNN` | `SCN/OBJ-NNN` | Buy/Configure/Build/Reuse/Integrate/Retire | `PROD-NNN` or Not applicable | [Bounded custom responsibility; `FBB-NNN` assigned at G4] | `ADR-NNN` | `DEP-NNN` | `EFF-NNN` | `COST-NNN` | [Role/team] | [Evidence or gap] | Proposed/Decided/Blocked |

## Required product and service inventory

| ID | Product or service | Vendor or internal provider | Capabilities | SKU, tier, or edition | Deployment scope | Quantity or consumption driver | License or commercial model | Governing ADR | Cost-model row | Lifecycle and exit | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PROD-001` | [Product, managed service, or internal platform] | [Provider] | `CAP-NNN` | [Required tier] | [Tenant/account/region/environment] | [Users, capacity, requests, storage, nodes, tokens] | [License, reservation, consumption, allocation] | `ADR-NNN` | [Link] | [Support lifecycle and replacement] | [Role/team] |

## Realization decision rules

- Trace every in-scope capability to an approved objective and scenario step.
- Do not mark `Buy`, `Configure`, or `Reuse` as decided until the product or service constraints and governing decision are accepted.
- At G3, a `Build` realization requires a bounded custom responsibility, interfaces, architecture constraints, effort drivers, and receiving owner. G4 creates the concrete functional building blocks and code-generation contexts.
- Record hybrid realization as separate bounded responsibilities rather than `Buy and build` in one ambiguous row.
- Include identity, data, integration, security, resilience, observability, support, skills, licensing, migration, cost, and exit implications.
- A product that provides multiple capabilities still requires explicit ownership and configuration boundaries for each capability.
- A shared enterprise service is not free or dependency-free; record service levels, onboarding, support, allocation, and exit.
- Products evaluated but not selected belong in the governing ADR, not in the required product inventory.

## Completeness summary

| Scenario or objective | Required capabilities | Realization decided | Products identified | Custom-build boundaries identified | Effort estimated | Cloud cost estimated | Operating owner identified | Open gaps |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Scenario/objective] | [Count] | [Count] | [Count] | [Count] | [Count] | [Count] | [Count] | [IDs] |

G3 is not ready while an in-scope capability lacks a bounded realization strategy, governing decision where required, or an explicit blocker.
