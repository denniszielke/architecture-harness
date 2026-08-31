# Implementation Handoff

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Product, architecture, security, data, test, operations, and receiving engineering owners
> Gate: G4
> Last reviewed: Not reviewed

## Handoff scope

| ID | Delivery increment | Receiving repository or team | Architecture baseline | Included building blocks | Included contexts | Status |
|---|---|---|---|---|---|---|
| `HND-001` | [Thin end-to-end increment] | [Repository/team] | [Commit, tag, or review date] | `FBB-NNN` | `CTX-NNN` | Draft/Ready/Blocked/Transferred |

## Package checklist

- [ ] Accepted objectives, scope, architecture, and ADRs are linked.
- [ ] Capability realization and required product inventory are complete.
- [ ] Backlog items and user stories are sequenced and owned.
- [ ] Functional building blocks have complete responsibility and contract specifications.
- [ ] Environment prerequisites and security guardrails are defined.
- [ ] Prototype and spike plans identify downstream execution owners.
- [ ] Release and deployment automation requirements are defined.
- [ ] Code-generation context packages are complete and versioned.
- [ ] Test plans and expected evidence are linked.
- [ ] Sizing assumptions and operating-model inputs are included.
- [ ] Delivery-effort inputs distinguish product acquisition/configuration, integration, custom build, migration, validation, and transition work.
- [ ] Unresolved decisions, assumptions, risks, and exclusions are explicit.
- [ ] The receiving team accepts the context and feedback path.

## Downstream boundary

The receiving implementation workflow owns:

- source and infrastructure code;
- dependency and repository choices within accepted boundaries;
- executable tests and pipelines;
- cloud provisioning and deployments;
- generated artifacts and releases;
- measured implementation, performance, cost, security, and operational results; and
- code-level backlog and delivery status.

The architecture harness retains ownership of the source scenario, objectives, logical design, target architecture, ADRs, NFRs, implementation context, sizing model, operating model, and presentation claims.

## Feedback contract

| Finding type | Downstream action | Harness action |
|---|---|---|
| Missing implementation detail within accepted boundaries | Resolve in the implementation repository and link the result | No architecture replay |
| Architecture ambiguity or conflict | Stop the affected work and report the exact conflict | Create `CHG-NNN` and replay affected tasks |
| New material product or boundary choice | Provide evidence and alternatives | Create or supersede an ADR |
| Failed assumption, test, NFR, security control, or sizing model | Return conditions and evidence | Reassess linked artifacts and gates |
| Implementation or operational evidence | Store in the downstream evidence location | Register the external evidence and update bounded claims |

## Transfer record

| Date | From | To | Package version | Conditions | Accepted by | Follow-up |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [Architecture role] | [Engineering role/team] | [Commit/tag] | [Conditions] | [Name/role] | [Items] |

G4 confirms that the handoff is ready. It does not approve code, implementation completion, deployment, or production readiness.
