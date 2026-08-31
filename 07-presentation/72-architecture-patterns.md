# Architecture Patterns Presentation View

> Status: Draft
> Canonical owner: Presentation lead, sourced from architecture artifacts
> Required reviewers: Solution architect, security, engineering, and operations owners
> Gate: G7
> Last reviewed: Not reviewed

## Pattern message

[State one audience-appropriate architecture thesis, such as modular responsibility boundaries, event-driven decoupling, governed data products, zero-trust identity, or automated operations.]

## Pattern cards

| Pattern | Problem addressed | Where applied | Benefit | Trade-off | Decision/evidence |
|---|---|---|---|---|---|
| [Pattern] | [Problem] | [Boundary] | [Benefit] | [Trade-off] | `ADR/NFR/EVID-NNN` |

## Cloud mapping

Show selected services only when an accepted ADR or inherited standard governs them. Group by architectural responsibility rather than vendor product inventory.

## Diagram rules

- Show trust, data, network, tenant, environment, and management boundaries that matter to the decision.
- Label product candidates as proposed and accepted products as decided.
- Distinguish target, prototype, and current state.
- Keep implementation detail in an appendix.
- Link the view to [../03-architecture/33-target-solution-architecture.md](../03-architecture/33-target-solution-architecture.md) and relevant ADRs.
