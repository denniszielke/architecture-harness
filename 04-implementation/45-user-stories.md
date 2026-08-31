# User Stories and Acceptance Scenarios

> Status: Draft
> Canonical owner: Product owner - name to be assigned
> Required reviewers: Business, architecture, engineering, security, test, and accessibility owners
> Gate: G4
> Last reviewed: Not reviewed

## Story template

### US-NNN - Outcome title

**As a** [actor]
**I need** [capability]
**So that** [measurable outcome]

**Traceability:** `OBJ-NNN`, `SCP-NNN`, `CAP-NNN`, `DES/NFR-NNN`, `ADR-NNN`

**Acceptance scenarios**

| Scenario | Given | When | Then | Evidence |
|---|---|---|---|---|
| Normal | [Context] | [Action] | [Outcome] | `TEST/EVID-NNN` |
| Unauthorized | [Context] | [Action] | [Denied and audited behavior] | `TEST/EVID-NNN` |
| Invalid or duplicate | [Context] | [Action] | [Safe behavior] | `TEST/EVID-NNN` |
| Dependency unavailable | [Context] | [Action] | [Degraded/fallback behavior] | `TEST/EVID-NNN` |
| Recovery or correction | [Context] | [Action] | [Reconciled behavior] | `TEST/EVID-NNN` |

**Non-functional acceptance**

- [Latency, throughput, availability, accessibility, security, observability, cost, or recovery threshold.]

**Out of scope**

- [Explicit exclusion.]
