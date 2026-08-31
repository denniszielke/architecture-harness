# Implementation Planning and Handoff Plan

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Architecture, security, data, test, operations, and product owners
> Entry gate: G3 - Architecture ready for implementation planning
> Exit gate: G4 - Implementation handoff ready
> Last reviewed: Not reviewed

## Purpose

Translate accepted scope, design, architecture, and decisions into an implementation-ready handoff. The phase defines what downstream engineering and code-generation workflows need; it does not create source code, infrastructure, pipelines, deployments, prototypes, or test results.

## Delivery principles

- Decompose the architecture into cohesive functional building blocks and thin end-to-end increments.
- Make every building block traceable to user stories, requirements, ADRs, NFRs, security controls, dependencies, and operating ownership.
- Define environment, release, deployment, test, observability, recovery, and evidence expectations before code generation starts.
- Frame high-risk uncertainty as a prototype or spike plan with explicit questions, methods, stop criteria, and downstream owners.
- Keep code-generation context bounded, versioned, product-aware, and free of unresolved material decisions.
- Hand off plans and context only. Execution occurs in a downstream implementation repository or delivery workflow.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-IMP-01` | Baseline implementation scope and backlog | G3 package and realization map | [41-backlog.md](41-backlog.md) | Work traces to accepted scope, capability realization, products, design, ADRs, NFRs, and acceptance | Not started | Not available |
| `TASK-IMP-02` | Define environment prerequisites and guardrails | `TASK-IMP-01` | [42-environment-setup.md](42-environment-setup.md) | Each environment has a purpose, boundary, prerequisites, controls, and validation plan | Not started | Not available |
| `TASK-IMP-03` | Frame prototypes and spikes when required | `TASK-IMP-01` | Optional [43-prototypes.md](43-prototypes.md) | Each material uncertainty has a bounded downstream experiment plan or an explicit not-applicable rationale | Not started | Not available |
| `TASK-IMP-04` | Define user stories and functional building blocks | `TASK-IMP-01` | [45-user-stories.md](45-user-stories.md), [48-functional-building-blocks.md](48-functional-building-blocks.md) | Stories and building blocks form a complete, traceable thin slice | Not started | Not available |
| `TASK-IMP-05` | Define release and deployment automation requirements | `TASK-IMP-02`, `TASK-IMP-04` | [44-release-and-deployment-automation.md](44-release-and-deployment-automation.md) | Pipeline stages, controls, promotion, rollback, and evidence expectations are specified | Not started | Not available |
| `TASK-IMP-06` | Define code-generation context | `TASK-IMP-04`, `TASK-IMP-05` | [46-code-generation-context.md](46-code-generation-context.md) | A downstream coding workflow can consume each bounded context without making architecture decisions | Not started | Not available |
| `TASK-IMP-07` | Define test and validation plan | `TASK-IMP-03`-`TASK-IMP-06` | [47-test-and-validation.md](47-test-and-validation.md) | Planned tests trace to requirements, risks, stories, building blocks, and expected evidence | Not started | Not available |
| `TASK-IMP-08` | Assemble the implementation handoff | `TASK-IMP-01`-`TASK-IMP-07` | [49-implementation-handoff.md](49-implementation-handoff.md) | The package is complete, versioned, bounded, and accepted by receiving roles | Not started | Not available |
| `TASK-IMP-09` | Prepare G4 review | `TASK-IMP-08` | Gate recommendation | Readiness, blockers, assumptions, decisions, and downstream obligations are explicit | Not started | Not available |

## G4 criteria

- The implementation backlog is sequenced, owned, and traceable to accepted architecture.
- Buy, configure, reuse, integrate, and retire work is distinguished from custom build work.
- User stories and functional building blocks define responsibilities, contracts, data, identities, failure behavior, NFRs, observability, operating ownership, and acceptance.
- Environment prerequisites and security guardrails are implementation-ready.
- Prototype and spike plans resolve named uncertainties without claiming execution when documentation and accepted evidence are insufficient.
- Release, deployment, rollback, migration, and supply-chain controls are specified.
- Test and validation plans define expected results, evidence, and execution ownership.
- Code-generation context packages contain sufficient canonical context and explicit prohibited decisions.
- The downstream repository, receiving roles, unresolved blockers, and change-feedback path are identified.
- No implementation or operational result is required or implied by G4.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Scope, design, capability, or accepted ADR | `TASK-IMP-01`, `TASK-IMP-04` | Context packages, tests, release, sizing, operations |
| Capability realization or required product | `TASK-IMP-01`, `TASK-IMP-04`, `TASK-IMP-06` | Backlog, custom blocks, product configuration, effort, cost, handoff |
| Environment, service tier, or policy | `TASK-IMP-02` | Deployment plan, security, sizing, operating procedures |
| New or changed uncertainty | `TASK-IMP-03` | ADR evidence plan, sizing validation, downstream backlog |
| Contract or data model | `TASK-IMP-04` | Stories, context packages, migration, test plan |
| Deployment or supply-chain control | `TASK-IMP-05` | Environment plan, context packages, operations |
| Acceptance or NFR threshold | `TASK-IMP-07` | Stories, building blocks, sizing, operations, claims |
| Downstream repository or delivery model | `TASK-IMP-08` | Context format, ownership, feedback, gate readiness |

Record changed inputs in the [change impact register](../01-preparation/16-change-impact-register.md). Recheck G4 when the handoff scope, building blocks, context contract, validation plan, receiving boundary, or accepted architecture changes.
