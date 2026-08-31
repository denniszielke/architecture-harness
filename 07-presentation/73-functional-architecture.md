# Functional Architecture Presentation View

> Status: Draft
> Canonical owner: Presentation lead, sourced from functional architecture
> Required reviewers: Business owner and solution architect
> Gate: G7
> Last reviewed: Not reviewed

## Audience message

[Explain how capabilities work together to produce the outcome in one sentence.]

## Simplified functional flow

| Step | Actor or domain | Capability | Information or decision | Control/evidence | Outcome |
|---|---|---|---|---|---|
| 1 | [Actor/domain] | `CAP-NNN` | [Flow] | [Control] | [Outcome] |

## Human and system authority

[Show who requests, recommends, executes, approves, overrides, and audits consequential actions.]

## Diagram rules

- Source the detailed model from [../03-architecture/32-functional-architecture.md](../03-architecture/32-functional-architecture.md).
- Do not add products to a functional view.
- Show one main journey and only the boundaries needed to understand it.
- Include failure or fallback when it materially affects trust in the proposal.
