# Gate Register

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Gate authority and affected phase owners
> Gate: G0-G7
> Last reviewed: Not reviewed

Agents and phase owners may write readiness recommendations. Only an actual gate authority may record a decision.

| Gate | Scope or baseline | Readiness recommendation | Evidence reviewed | Decision | Authority | Date | Conditions, risks, or follow-up |
|---|---|---|---|---|---|---|---|
| G0 | Framing | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G1 | Preparation | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G2 | Design | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G3 | Architecture | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G4 | Implementation handoff | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G5 | Delivery effort, sizing model, and validation plan | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G6 | Operating model and readiness plan | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |
| G7 | Architecture-validated scenario and decision package | Not assessed | [Links] | Not decided | [Role/name] | - | [Open actions] |

## Decision values

- `Not decided`
- `Accepted`
- `Accepted with conditions`
- `Hold`
- `Returned`

If a changed input invalidates evidence or a gate condition, link the `CHG-NNN` record and mark the readiness recommendation for reassessment. Preserve the original decision record and add a dated review note rather than silently replacing history.

## Gate decision history

Append one row per actual decision or reassessment. The summary above shows current state; this table preserves history.

| Event ID | Gate | Baseline or change | Date | Authority | Decision | Evidence reviewed | Conditions, dissent, and accepted risk | Supersedes event |
|---|---|---|---|---|---|---|---|---|
| `GATE-EVENT-001` | [G0-G7] | [Scope/commit/CHG-NNN] | [YYYY-MM-DD] | [Role/name] | [Accepted/Accepted with conditions/Hold/Returned] | [Links] | [Record] | [Event or Not applicable] |
