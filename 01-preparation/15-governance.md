# Governance and Traceability

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Sponsor, architecture, security, engineering, operations, and assurance owners
> Gate: G1 and continuous governance
> Last reviewed: Not reviewed

## Governance principles

1. One accountable owner exists for each controlled artifact.
2. A proposal is not an accepted decision.
3. An assumption is not a source fact.
4. A designed control is not implementation or operational evidence.
5. A prototype result is bounded by its data, environment, method, and limitations.
6. Changed inputs propagate through explicit links and task-level replay.
7. Agents may recommend readiness but cannot record human approval.

## Roles

| Role | Accountable for | Required decisions or reviews |
|---|---|---|
| Executive sponsor | Vision, business goals, funding direction, business risk | G0, objectives, scope, investment decision |
| Product or program lead | Integrated plan, dependencies, scope, change, risks, gates | G1 and cross-phase coordination |
| Business owner | Narrative, journeys, operating outcomes, adoption | Framing and logical design review |
| Solution or enterprise architect | Design coherence, target architecture, NFRs, ADR process | G2 and G3 recommendations |
| Data owner or architect | Data purpose, model, quality, lineage, platform behavior | Data design and product mapping review |
| Security and privacy owner | Threats, identity, protection, policy, residual risk | Security reviews and exceptions |
| Engineering lead | Backlog, environments, implementation, automation, evidence | G4 recommendation |
| Test and evidence lead | Test strategy, reproducibility, measurement evidence | G4 and G5 evidence review |
| FinOps or finance owner | Cost model, rates, sensitivity, budget guardrails | G5 recommendation |
| Service owner or operations lead | Support, SLOs, procedures, rollout, recovery | G6 recommendation |
| Presentation lead | Decision narrative, claim traceability, review | G7 recommendation |
| Gate authority | Gate decision and conditions | Accept, hold, or return a gate |

Use role placeholders until named people are provided. Never invent assignments.

## Artifact lifecycle

| State | Meaning | Downstream use |
|---|---|---|
| `Draft` | Material authoring is active | Exploration only |
| `In review` | Stable enough for named review | Gate preparation only |
| `Accepted` | Actual authority and reviewers approved it, with conditions recorded | Approved dependency |
| `Blocked` | A named unresolved input prevents completion | Not gateable without an explicit exception |
| `Superseded` | A linked accepted replacement exists | Historical reference |

## Phase task lifecycle

| State | Meaning |
|---|---|
| `Not started` | Dependencies have not yet been assessed |
| `Ready` | Entry conditions and direct dependencies are satisfied |
| `Blocked` | A named input, decision, owner, or environment is missing |
| `In progress` | The accountable role is executing the bounded task |
| `Replay required` | A changed input invalidated part of the task output or evidence |
| `Complete with evidence` | The completion check is met and evidence is linked |

## Evidence classes

| Class | Meaning |
|---|---|
| Source fact | Directly supported by a cited source |
| Assumption | Unverified statement with validation ownership |
| Target | Desired measurable state; not a forecast or achieved result |
| Proposal | Candidate direction awaiting decision |
| Accepted decision | Recorded authority accepted a choice |
| Designed | Specified but not executed |
| Demonstrated | Executed under stated test conditions by a cited external source or downstream workflow |
| Operational evidence | Observed in the intended live operating context by a cited external source |
| Future commitment | Planned work with ownership and dependencies |

## Traceability chain

```text
SRC/ASM -> GOAL/OBJ/SCP -> CAP/REQ/DES/NFR
        -> ADR/control/RISK -> TASK/IMP -> TEST/EVID -> CLAIM
```

Not every record needs every link. Every implementation-handoff item and presentation claim must trace backward to an approved need and forward to expected evidence, cited external evidence, or an explicit gap.

## Canonical record owners

| Record | Canonical owner |
|---|---|
| Source, assumption, goal | `00-framing/` artifact matching the record type |
| Objective, scope, change, gate, risk | `01-preparation/` register matching the record type |
| Capability | `03-architecture/31-enterprise-capabilities.md` |
| Requirement, design invariant, NFR statement | `02-design/23-requirements-and-acceptance.md` |
| NFR realization | `03-architecture/35-non-functional-architecture.md` |
| Architecture decision | `03-architecture/decisions/` and its index |
| Phase task | The owning phase plan using `TASK-<phase>-NN` |
| Implementation item | `04-implementation/41-backlog.md` |
| User story | `04-implementation/45-user-stories.md` |
| Functional building block | `04-implementation/48-functional-building-blocks.md` |
| Code-generation context | `04-implementation/46-code-generation-context.md` |
| Implementation handoff | `04-implementation/49-implementation-handoff.md` |
| Implementation test (`TEST-IMP`) | `04-implementation/47-test-and-validation.md` |
| Sizing test (`TEST-SIZE`) | `05-sizing/53-sizing-tests.md` |
| Operational test or exercise (`TEST-OPS`) | `06-operations/65-service-management-and-continuity.md` |
| External evidence | `01-preparation/19-external-evidence-register.md` |
| Presentation claim | `07-presentation/75-claim-and-evidence-register.md` |

Tests use phase namespaces: `TEST-IMP-NNN`, `TEST-SIZE-NNN`, and `TEST-OPS-NNN`. The phase register owns the test plan. The [external evidence register](19-external-evidence-register.md) references results produced outside the architecture harness.

## Architecture-to-engineering boundary

The harness owns architecture definition and implementation context. It may specify:

- implementation scope, backlog, user stories, and functional building blocks;
- environment, release, deployment, migration, test, and operational requirements;
- code-generation context and prohibited decisions;
- sizing models and validation plans; and
- operating models, procedures, rollout, recovery, and readiness plans.

The downstream implementation workflow owns source code, infrastructure code, pipelines, deployments, test execution, generated artifacts, releases, and measured implementation or operating results. Link relevant results back as external evidence; do not copy delivery artifacts into this repository.

## Change control

1. Record a material changed input as `CHG-NNN` in [16-change-impact-register.md](16-change-impact-register.md).
2. Identify the canonical source and compare old and new meaning.
3. Traverse direct links, then phase-plan dependencies.
4. Mark affected tasks `Replay required`; do not rewrite accepted history silently.
5. Update the canonical owner first, then summaries and downstream artifacts.
6. Re-run tests and gate checks whose evidence or conditions changed.
7. Close the change only when affected links, decisions, evidence, and gates are reconciled.

## Gate decisions

A gate record includes scope, date, authority, readiness recommendation, evidence reviewed, decision (`Accepted`, `Accepted with conditions`, `Hold`, or `Returned`), conditions, dissent, accepted risks, and follow-up owners. Document completeness alone is not a gate decision.
