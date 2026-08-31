# Design Phase Plan

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Business, data, security, engineering, operations, and test owners
> Entry gate: G1 - Preparation baseline accepted
> Exit gate: G2 - Logical design ready for architecture
> Last reviewed: Not reviewed

## Purpose

Turn approved objectives, scope, journeys, and constraints into a coherent product-independent design. Define what the solution must do, how responsibilities and authority are bounded, how information moves, how failures are handled, and what must be decided before implementation.

## Design boundary

- Design owns logical behavior and responsibilities.
- Architecture owns product selection, deployment topology, and long-lived technical choices.
- The implementation-handoff phase owns downstream planning and context; the downstream implementation workflow owns executable realization and results.
- A product may appear in design only as a candidate or inherited constraint with a linked decision.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-DES-01` | Reconcile preparation inputs | G1 package | Design baseline and open issues | Objectives, scope, assumptions, and constraints are consistent | Not started | Not available |
| `TASK-DES-02` | Define cross-domain design | `TASK-DES-01` | [21-high-level-design.md](21-high-level-design.md) | Actors, boundaries, components, flows, authority, and failure paths are clear | Not started | Not available |
| `TASK-DES-03` | Establish design principles | `TASK-DES-01` | [22-design-principles.md](22-design-principles.md) | Principles have observable consequences | Not started | Not available |
| `TASK-DES-04` | Develop bounded domain designs | `TASK-DES-02`, `TASK-DES-03` | [domains](domains/) | Each concern has one canonical owner and explicit interfaces | Not started | Not available |
| `TASK-DES-05` | Define acceptance and NFR inputs | `TASK-DES-04` | [23-requirements-and-acceptance.md](23-requirements-and-acceptance.md) | Behavior and quality attributes are measurable | Not started | Not available |
| `TASK-DES-06` | Build decision backlog | `TASK-DES-04`, `TASK-DES-05` | ADR backlog in [../03-architecture/decisions/README.md](../03-architecture/decisions/README.md) | Every material unresolved choice is visible | Not started | Not available |
| `TASK-DES-07` | Prepare G2 review | `TASK-DES-01`-`TASK-DES-06` | Gate recommendation | Gaps, decisions, risks, and evidence needs are explicit | Not started | Not available |

## G2 criteria

- The thin end-to-end journey covers normal, exceptional, degraded, and recovery paths.
- Logical components have non-overlapping responsibilities and authoritative state.
- Data ownership, contracts, classification, lineage, retention, and quality are specified.
- API, event, message, batch, and human handoffs include failure and replay behavior.
- Identity, authorization, privacy, threat, audit, and secure-by-default behavior are designed.
- Reliability, observability, scale, deployment, support, and cost drivers are measurable.
- AI or agentic behavior has explicit permissions, grounding, evaluation, human control, and fallback where applicable.
- Prototype shortcuts and production deltas are visible.
- Material product and pattern choices are in the ADR backlog.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Objective, journey, or scope | `TASK-DES-01`, `TASK-DES-02` | All domain designs, ADR backlog, tests |
| Data source, classification, or authority | Data model domain | Platform, integration, security, resilience, architecture |
| User or operating responsibility | Operating model and high-level design | Security, experience, architecture, operations |
| NFR or failure assumption | Resilience domain | Platform, integration, target architecture, sizing |
| Security or policy constraint | Security domain | Every affected trust boundary, ADR, backlog, test |
| AI use or autonomy boundary | Application and AI experience | Data, security, integration, ADRs, evaluation |

Record the change and affected task IDs in the [change impact register](../01-preparation/16-change-impact-register.md). Recheck G2 when accepted logical behavior, authority, or quality requirements changed.
