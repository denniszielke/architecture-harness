# Framing Plan

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Executive sponsor, business owner, solution architect
> Entry: A problem statement, opportunity, or scenario source
> Exit gate: G0 - Framing sufficient for preparation
> Last reviewed: Not reviewed

## Purpose

Turn supplied source material into a bounded vision, explicit assumptions, a neutral scenario, and measurable business goals without choosing products or inventing facts.

## Inputs

- Source brief, stakeholder notes, policies, constraints, and existing-system evidence.
- Known deadlines, budget boundaries, jurisdictions, organizational standards, and decision authorities.
- Existing measurements with provenance and limitations.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-FRM-01` | Capture source and provenance | Source material | [03-scenario.md](03-scenario.md) source inventory | Every material source statement is cited or marked unknown | Not started | Not available |
| `TASK-FRM-02` | Define vision and guardrails | `TASK-FRM-01` | [01-vision.md](01-vision.md) | Future state, principles, non-goals, and boundaries are reviewable | Not started | Not available |
| `TASK-FRM-03` | Establish assumptions | `TASK-FRM-01` | [02-assumptions.md](02-assumptions.md) | High-impact unknowns have owners, validation actions, and consequences | Not started | Not available |
| `TASK-FRM-04` | Define business goals | `TASK-FRM-01`, `TASK-FRM-02`, `TASK-FRM-03` | [04-business-goals.md](04-business-goals.md) | Goals have measures or explicit measurement gaps | Not started | Not available |
| `TASK-FRM-05` | Prepare G0 review | `TASK-FRM-01`-`TASK-FRM-04` | Readiness recommendation in [../01-preparation/17-gate-register.md](../01-preparation/17-gate-register.md) | Conflicts, conditions, and open questions are visible | Not started | Not available |

## G0 criteria

- The problem, affected stakeholders, desired change, constraints, and non-goals are explicit.
- The in-scope business scenario is decomposed into stable end-to-end steps and exception paths.
- Source facts and assumptions are visibly different.
- Goals are outcome-oriented rather than a product list.
- No unrecorded decision is presented as approved.
- Open questions are bounded enough for preparation planning.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Source correction or new evidence | `TASK-FRM-01` | Vision, assumptions, goals, all downstream links |
| Stakeholder or business-priority change | `TASK-FRM-02`, `TASK-FRM-04` | Objectives, scope, design priorities, presentation |
| Assumption validated or rejected | `TASK-FRM-03` | Every artifact linked to the assumption |
| Constraint or non-goal change | `TASK-FRM-02` | Scope, design, ADRs, backlog, sizing, operations |

Record every material change as `CHG-NNN` in the [change impact register](../01-preparation/16-change-impact-register.md). Reopen G0 only when the accepted framing meaning or gate conditions changed.
