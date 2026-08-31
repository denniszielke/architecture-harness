# High-Level Design

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Business, data, security, engineering, operations, and test owners
> Gate: G2
> Last reviewed: Not reviewed

## Design intent

[Explain how the proposed logical solution enables the approved objectives and thin end-to-end slice. Link rather than repeat preparation content.]

## System context

| Actor or external system | Need or responsibility | Information exchanged | Trust or ownership boundary |
|---|---|---|---|
| [Actor/system] | [Need] | [Information] | [Boundary] |

## Logical capabilities and components

| Requirement ID | Logical component | Responsibility | Authoritative state | Inputs and outputs | Failure behavior |
|---|---|---|---|---|---|
| `REQ-NNN` | [Product-independent component] | [Single responsibility] | [State or none] | [Contracts] | [Safe failure/degraded mode] |

## End-to-end flow

1. [Actor intent and input.]
2. [Validation, authorization, and processing.]
3. [Data, event, or workflow transition.]
4. [Human or deterministic decision authority.]
5. [Evidence, response, and observable outcome.]

Describe normal, duplicate, delayed, invalid, unauthorized, unavailable-dependency, recovery, and replay paths.

## Scenario-to-design realization

| Scenario step | Objective | Required behavior | Logical components | Decision or handoff | Failure or exception | Acceptance |
|---|---|---|---|---|---|---|
| `SCN-NNN` | `OBJ-NNN` | `REQ/DES-NNN` | [Components] | [Authority/handoff] | [Behavior] | [Method] |

## Decision and authority model

| Decision or action | Recommends | Executes | Approves | Evidence retained |
|---|---|---|---|---|
| [Material action] | [Role/system] | [Role/system] | [Authority] | [Required trace] |

## Domain ownership

- [Data model](domains/data-model.md)
- [Platform concept](domains/platform-concept.md)
- [Integration patterns](domains/integration-patterns.md)
- [Application and AI experience](domains/application-and-ai-experience.md)
- [Operating model](domains/operating-model.md)
- [Resilience](domains/resilience.md)
- [Security](domains/security.md)
- [Requirements and acceptance](23-requirements-and-acceptance.md)

## Prototype and target distinction

| Concern | Prototype or experiment | Target design | Delta and risk |
|---|---|---|---|
| [Concern] | [Bounded behavior] | [Required behavior] | [Work/decision/evidence gap] |

## Decision-driving questions

| Candidate ADR | Question | Why material | Due gate |
|---|---|---|---|
| `ADR-NNN` | [Product, boundary, pattern, or trade-off question] | [Long-lived consequence] | G3 |
