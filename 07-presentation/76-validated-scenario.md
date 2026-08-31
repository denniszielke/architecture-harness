# Architecture-Validated Scenario

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Business, product, architecture, engineering, security, data, operations, FinOps, finance, and decision-authority roles
> Gate: G7
> Last reviewed: Not reviewed

This is the final integrated delivery of the architecture harness. It shows how the approved business scenario is achieved, which capabilities and products are required, what is bought, configured, built, reused, integrated, or retired, what delivery effort and cloud services are expected to cost, how the solution is operated, and which claims are validated or remain conditional.

It is a derived decision view. Canonical detail remains in the linked phase artifacts.

## Meaning of architecture-validated

`Architecture-validated` means:

- every in-scope scenario step and objective traces to logical behavior and required capabilities;
- each capability has a bounded realization strategy and accepted product decision where required;
- custom responsibilities have functional building blocks and code-generation context;
- delivery effort and cloud/service cost are estimated with ranges, sources, assumptions, and confidence;
- operating ownership, rollout, security, support, and continuity plans exist;
- required downstream validation and evidence are explicit; and
- unresolved assumptions, decisions, risks, dependencies, and evidence gaps are visible.

It does not mean that code exists, products are procured, environments are deployed, business outcomes are achieved, or production readiness and operating effectiveness are demonstrated.

## End-to-end scenario realization

| Scenario step | Scope item | Goal or objective | Required behavior | Capability | Realization strategy | Required product/service | Custom building block/context | Governing ADR | Delivery effort | Cloud/service cost | Operating owner | Validation status | Evidence or gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCN-NNN` | `SCP-NNN` | `GOAL/OBJ-NNN` | `REQ/DES/NFR-NNN` | `CAP-NNN` | Buy/Configure/Build/Reuse/Integrate/Retire | `PROD-NNN` or Not applicable | `FBB/CTX-NNN` or Not applicable | `ADR-NNN` | `EFF-NNN` | `COST-NNN` | [Role/team] | Validated/Conditional/Blocked/Out of scope | `EVID/RISK/ASM/DEP-NNN` |

## Business outcome coverage

| Goal or objective | Scenario coverage | Realization coverage | Measurement method | Architecture confidence | External evidence | Remaining condition |
|---|---|---|---|---|---|---|
| `GOAL/OBJ-NNN` | [Steps] | [Capabilities/realizations] | [Metric and method] | Low/Medium/High | [Link or Not available] | [Condition] |

## Required products and services

Source: [capability realization and product inventory](../03-architecture/37-capability-realization.md).

| Product or service | Capabilities supplied | Required tier or scope | Commercial model | Environments | Cloud/service cost range | Decision and confidence |
|---|---|---|---|---|---|---|
| `PROD-NNN` | `CAP-NNN` | [Tier/scope] | [License/consumption/allocation] | [Environments] | [Low/base/high] | `ADR-NNN`, [confidence] |

## Buy, configure, build, reuse, integrate, and retire summary

| Strategy | Capability count | Required products | Custom building blocks | Base delivery effort | Base cloud/service cost | Main risk or dependency |
|---|---:|---|---|---:|---:|---|
| Buy/Configure/Build/Reuse/Integrate/Retire | [Count] | [Product IDs] | [FBB IDs] | [Person-days] | [Cost/period] | [IDs] |

## Delivery effort

Source: [delivery effort estimate](../05-sizing/55-delivery-effort-estimate.md).

| View | Low | Base | High | Confidence | Main assumptions |
|---|---:|---:|---:|---|---|
| Total person-days | [Days] | [Days] | [Days] | [Level] | [Assumptions] |
| Elapsed duration | [Weeks] | [Weeks] | [Weeks] | [Level] | [Capacity/dependency assumptions] |
| Optional labor cost | [Cost] | [Cost] | [Cost] | [Level/restricted] | [Rate basis] |

### Effort by role and wave

| Delivery wave | Role or team | Low person-days | Base person-days | High person-days | Peak FTE or sourcing condition |
|---|---|---:|---:|---:|---|
| [Wave] | [Role/team] | [Days] | [Days] | [Days] | [Condition] |

## Cloud and service cost

Source: [sizing and cost estimation](../05-sizing/54-sizing-and-cost-estimation.md).

| Cost view | Low | Base | High | Period | Confidence | Main drivers and exclusions |
|---|---:|---:|---:|---|---|---|
| One-time cloud/service enablement | [Cost] | [Cost] | [Cost] | One-time | [Level] | [Drivers] |
| Non-production run cost | [Cost] | [Cost] | [Cost] | [Month/year] | [Level] | [Drivers] |
| Production run cost | [Cost] | [Cost] | [Cost] | [Month/year] | [Level] | [Drivers] |
| Licenses and support | [Cost] | [Cost] | [Cost] | [Period] | [Level] | [Commercial assumptions] |

## Operating model

| Service or capability | Product/service owner | Engineering owner | Service owner | Security/data owner | Support model | Readiness condition |
|---|---|---|---|---|---|---|
| `CAP/PROD/FBB-NNN` | [Role] | [Role] | [Role] | [Role] | [Tier/hours] | [Condition] |

## Validation and decision status

| Dimension | Status | Canonical evidence | Conditions or gaps | Owner | Due action |
|---|---|---|---|---|---|
| Scenario and objectives | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Logical design | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Capability realization and products | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Implementation handoff | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Delivery effort | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Cloud/service cost | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| Operating model | Validated/Conditional/Blocked | [Links] | [Conditions] | [Role] | [Action] |
| External evidence | Available/Partial/Not available | [Links] | [Limitations] | [Role] | [Action] |

## Overall assessment

Use one recommendation:

- `Architecture-validated`: complete enough for the stated decision with no unresolved blocker.
- `Architecture-validated with conditions`: decision may proceed with explicit conditions, owners, and due actions.
- `Not ready`: one or more material scenario, realization, product, effort, cost, operating, or evidence gaps block the decision.

Record the requested decision, recommendation, conditions, residual-risk requests, and links to the actual gate decision. Do not use this artifact to record approval on behalf of the decision authority.
