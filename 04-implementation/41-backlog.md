# Implementation Backlog

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Product, architecture, security, test, and operations owners
> Gate: G4
> Last reviewed: Not reviewed

| ID | Outcome or work item | Type | Realization | Priority | Dependencies | Design/ADR links | Product or building blocks | Acceptance and planned tests | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `IMP-001` | [Thin-slice outcome] | Feature | `REAL-NNN` | [Priority] | [IDs] | [Links] | `PROD/FBB-NNN` | `TEST-IMP-NNN` | [Role] | Proposed/Ready/Blocked |

## Backlog types

- `Feature`: user or system outcome.
- `Enabler`: platform, data, integration, security, or operational capability.
- `Experiment`: bounded question with stop criteria.
- `Control`: security, privacy, policy, evidence, or quality requirement.
- `Debt`: explicit prototype-to-target gap.
- `Migration`: data, interface, configuration, or operating-state transition.
- `Hardening`: production security, resilience, performance, or operational work.

## Ready rule

An item is ready for downstream engineering only when its outcome, owner, dependencies, acceptance, security implications, data and contracts, building blocks, environment assumptions, ADR status, test plan, and expected evidence are sufficient to implement without silently making a material decision.

This backlog is a planning artifact. Downstream delivery tooling owns implementation status such as in progress, built, tested, released, or operated.
