# Presentation Plan

> Status: Draft
> Canonical owner: Presentation lead - name to be assigned
> Required reviewers: Sponsor, product, architecture, engineering, operations, test, security, and finance owners
> May start after: G0; final inputs are accepted artifacts and bounded evidence from all phases
> Exit gate: G7 - Decision package ready
> Last reviewed: Not reviewed

## Purpose

Turn approved facts, decisions, and demonstrated evidence into a concise decision story. The presentation is a synthesis, not a new canonical source or a product catalog.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-PRES-01` | Confirm audience and requested decision | G0 and sponsor input | Presentation brief | Decision, alternatives, authority, time, and objections are explicit | Not started | Not available |
| `TASK-PRES-02` | Build claim and evidence register | Accepted and demonstrated sources | [75-claim-and-evidence-register.md](75-claim-and-evidence-register.md) | Every material claim has a class, source, caveat, and reviewer | Not started | Not available |
| `TASK-PRES-03` | Create value story | `TASK-PRES-01`, `TASK-PRES-02` | [71-business-value-story.md](71-business-value-story.md) | Problem, change, evidence, investment, risk, and ask form one argument | Not started | Not available |
| `TASK-PRES-04` | Prepare architecture views | G2-G6 artifacts | [72-architecture-patterns.md](72-architecture-patterns.md), [73-functional-architecture.md](73-functional-architecture.md) | Views are accurate, audience-appropriate, and traceable | Not started | Not available |
| `TASK-PRES-05` | Explain operating model | G6 package | [74-operating-model.md](74-operating-model.md) | Accountability, rollout, support, security, cost, and continuity are visible | Not started | Not available |
| `TASK-PRES-06` | Review and rehearse | `TASK-PRES-01`-`TASK-PRES-05` | Gate recommendation | Claims, timing, accessibility, demo, objections, and requested decision are ready | Not started | Not available |

## G7 criteria

- The audience, decision authority, requested decision, alternatives, and consequence of delay are explicit.
- Every material claim is classified and linked to its canonical source.
- Targets, proposals, accepted decisions, designed controls, demonstrated results, operational evidence, and future commitments are visibly distinct.
- Architecture views preserve actual boundaries and do not imply unapproved sharing, scale, compliance, or service capability.
- Costs include assumptions, range, date, and exclusions.
- Risks, limitations, production gaps, and unresolved decisions are visible.
- Content is accessible, reviewed, timed, and distribution-appropriate.

## Input change and replay

Any upstream `CHG-NNN` must identify affected claims and views. Re-run the linked presentation tasks after canonical artifacts are updated. Never repair a source conflict only in the deck.
