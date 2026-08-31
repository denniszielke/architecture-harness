# Architecture Decision Index

[../36-architecture-decision-process.md](../36-architecture-decision-process.md) governs this directory. Copy [adr-template.md](adr-template.md) for each decision and use a lowercase, zero-padded filename such as `adr-001-application-runtime.md`.

## Decision backlog and index

| ID | Decision question or title | Status | Owner | Decision authority | Due gate | Dependencies | File |
|---|---|---|---|---|---|---|---|
| `ADR-001` | [Material decision question] | Not started | [Role] | [Role/name] | G3 | [IDs] | [Create when proposal is reviewable] |

`Not started` is an index planning state, not an ADR lifecycle state.

## Rules

- Never reuse an accepted identifier.
- A `Proposed` ADR keeps `## Decision` empty.
- Product preference is not a decision until requirements, disqualifiers, alternatives, evidence, and consequences are reviewable.
- Update this index when an ADR is created or its lifecycle metadata changes.
- Only the recorded authority changes an ADR to `Accepted`, `Rejected`, or `Deferred`.
- Superseding decisions use a new ID and link both records.
