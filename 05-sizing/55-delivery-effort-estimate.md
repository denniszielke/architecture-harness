# Delivery Effort Estimate

> Status: Draft
> Canonical owner: Engineering lead with FinOps or delivery lead - names to be assigned
> Required reviewers: Product, architecture, engineering, platform, data, security, test, operations, procurement, and finance owners
> Gate: G5
> Last reviewed: Not reviewed

This artifact owns delivery effort for the architecture-defined solution. It estimates the human effort needed to buy, configure, build, reuse, integrate, migrate, validate, transition, and retire capabilities. It does not commit a team, schedule, budget, or implementation result.

## Estimate context

| Attribute | Value |
|---|---|
| Architecture and realization baseline | [Commit, tag, or review date] |
| Scope and delivery increments | [Links] |
| Estimate date and horizon | [Date and period] |
| Estimation method | [Analogous, bottom-up, parametric, expert, range] |
| Working calendar | [Days, availability, location assumptions] |
| Included roles and suppliers | [Roles] |
| Labor-rate treatment | Effort only / internal rates / supplier rates / blended rates |
| Contingency treatment | [Method and percentage/range] |
| Exclusions | [Procurement lead time, waiting time, tax, travel, support, or other exclusions] |

## Work-package effort

| ID | Realization or building block | Work package | Strategy | Delivery wave | Role | Low person-days | Base person-days | High person-days | Elapsed-time driver | Dependencies | Estimate source | Confidence | Assumptions and exclusions |
|---|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|
| `EFF-001` | `REAL/FBB-NNN` | [Outcome or work package] | Buy/Configure/Build/Reuse/Integrate/Retire | [Wave] | [Role] | [Days] | [Days] | [Days] | [Critical path or wait] | `DEP-NNN` | [Evidence or method] | Low/Medium/High | [Conditions] |

Use one row per work-package, role, and wave combination. Repeat the work-package and realization reference when several roles contribute so role and wave totals can be reproduced.

## Required effort categories

Include categories that materially apply:

- product evaluation, procurement, licensing, contracting, and vendor onboarding;
- platform, landing zone, identity, network, policy, security, and environment enablement;
- product configuration, extension, and tenant or workspace setup;
- custom application, integration, data, AI, automation, and infrastructure engineering;
- data discovery, cleansing, migration, reconciliation, archival, and decommissioning;
- threat modeling, privacy, assurance, model-risk, and control implementation;
- contract, functional, security, performance, resilience, accessibility, and user acceptance testing;
- release, deployment, observability, backup, recovery, and service-management enablement;
- documentation, training, change management, rollout, hypercare, and operations transition;
- program, product, architecture, engineering management, and technical governance; and
- contingency for unresolved assumptions, dependencies, and delivery risk.

## Effort by role

| Role or team | Low person-days | Base person-days | High person-days | Peak concurrent capacity | Availability assumption | Gap or sourcing action |
|---|---:|---:|---:|---:|---|---|
| [Role/team] | [Days] | [Days] | [Days] | [FTE] | [Assumption] | [Hire, partner, train, allocate] |

## Effort by realization strategy

| Strategy | Low person-days | Base person-days | High person-days | Main drivers | Main uncertainty |
|---|---:|---:|---:|---|---|
| Buy/Configure/Build/Reuse/Integrate/Retire | [Days] | [Days] | [Days] | [Drivers] | [Uncertainty] |

## Delivery-wave and elapsed-time view

| Wave | Outcome | Entry dependencies | Low elapsed time | Base elapsed time | High elapsed time | Required roles | Exit condition |
|---|---|---|---|---|---|---|---|
| [Wave] | [Outcome] | [IDs] | [Weeks] | [Weeks] | [Weeks] | [Roles] | [Condition] |

Person-days are additive effort; elapsed duration depends on sequencing, parallelism, team capacity, procurement, approvals, environments, and external dependencies. Do not derive elapsed time by simply dividing effort by headcount.

## Role-by-wave effort

| Delivery wave | Role or team | Low person-days | Base person-days | High person-days | Peak concurrent FTE | Capacity or sourcing assumption |
|---|---|---:|---:|---:|---:|---|
| [Wave] | [Role/team] | [Days] | [Days] | [Days] | [FTE] | [Internal, partner, vendor, hire, train] |

## Optional labor-cost conversion

| Role or supplier | Rate basis | Currency | Rate source and date | Low cost | Base cost | High cost | Commercial exclusions |
|---|---|---|---|---:|---:|---:|---|
| [Role/supplier] | [Per day/hour/fixed] | [Currency] | [Source/date] | [Cost] | [Cost] | [Cost] | [Exclusions] |

Keep confidential rates in an approved restricted source when they cannot be stored in this repository. The architecture-validated scenario may cite a bounded total or state that monetary labor cost is restricted.

## Confidence and calibration

| Estimate or driver | Confidence | Evidence needed | Re-estimate trigger | Downstream owner |
|---|---|---|---|---|
| `EFF-NNN` | Low/Medium/High | [Spike, supplier quote, backlog refinement, implementation result] | [Change threshold] | [Role/team] |

External implementation evidence may calibrate the estimate through change control. G5 confirms that effort is sufficiently bounded for the requested decision; it does not approve a delivery commitment.
