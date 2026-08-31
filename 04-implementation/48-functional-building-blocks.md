# Functional Building Blocks

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Product, architecture, data, security, integration, test, and operations owners
> Gate: G4
> Last reviewed: Not reviewed

Functional building blocks translate the accepted architecture into cohesive implementation responsibilities. They are specifications, not source-code modules or deployment artifacts.

## Building block index

| ID | Name | Responsibility | Realization | Capabilities and requirements | User stories | Dependencies | Context package | Downstream owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| `FBB-001` | [Verb-noun building block] | [One cohesive responsibility] | `REAL-NNN` with strategy Build | `CAP/REQ/DES/NFR-NNN` | `US-NNN` | `DEP-NNN` | `CTX-NNN` | [Role/team] | Proposed/Ready/Blocked |

## Building block specification

### FBB-NNN - Building block name

**Outcome and responsibility**

[State the outcome, single responsibility, and explicit exclusions.]

**Traceability**

- Capabilities and requirements: [IDs and links]
- Capability realization: `REAL-NNN`
- Architecture and ADRs: [links]
- User stories and tests: [IDs and links]
- Risks and assumptions: [IDs and links]

**State and contracts**

| Concern | Specification |
|---|---|
| Authoritative state | [Owned state or none] |
| Inputs and outputs | [API, event, message, data, file, or human contracts] |
| Data and classification | [Entities, purpose, classification, retention, locality] |
| Dependencies | [Required and optional dependencies plus fallback] |
| Compatibility and migration | [Versioning, schema, rollout, correction] |

**Identity and security**

[Define human and workload identities, authorization, secrets, trust boundaries, abuse cases, controls, and audit.]

**Failure and recovery**

[Define validation, timeout, retry, idempotency, replay, reconciliation, degraded mode, rollback, restore, and escalation.]

**Non-functional and operating contract**

| Quality or operation | Requirement |
|---|---|
| Scale and performance | [NFR and workload link] |
| Availability and recovery | [SLO/RTO/RPO link] |
| Observability and evidence | [Logs, metrics, traces, audit, expected records] |
| Deployment and configuration | [Target, configuration, feature, and environment boundaries] |
| Ownership and support | [Build, service, security, data, and support roles] |
| Cost driver | [Scale unit and measurement] |

**Ready for context generation when**

- responsibility and exclusions are unambiguous;
- material ADRs are accepted or explicitly blocking;
- contracts, identities, data, failure behavior, NFRs, operating ownership, and tests are linked; and
- downstream engineering can implement the block without making a hidden architecture decision.
