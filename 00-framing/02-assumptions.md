# Assumptions

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Business, architecture, security, data, engineering, and operations owners
> Gate: G0 and continuous review
> Last reviewed: Not reviewed

An assumption is not a fact. Add only assumptions that affect outcomes, scope, architecture, implementation, sizing, operation, or assurance.

| ID | Domain | Assumption | Status | Owner role | Validation method | Due task or gate | Impact if false | Linked artifacts |
|---|---|---|---|---|---|---|---|---|
| `ASM-001` | [Business, data, security, platform, integration, AI, delivery, cost, or operations] | [Unverified belief] | Open | [Role] | [Evidence or experiment] | [Task/Gate] | [Consequence] | [Links] |

## Status values

- `Open`: not yet tested.
- `Supported`: current evidence supports the assumption within stated limits.
- `Rejected`: evidence contradicts the assumption; start change-impact replay.
- `Superseded`: replaced by a linked assumption or accepted decision.

## Review rule

When an assumption changes, create a `CHG-NNN` record before updating dependent artifacts. Preserve the old statement and evidence when it influenced an accepted gate or decision.
