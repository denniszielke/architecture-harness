# Presentation Plan

> Status: Draft
> Canonical owner: Presentation lead - name to be assigned
> Required reviewers: Sponsor, product, architecture, engineering, operations, test, security, and finance owners
> May start after: G0; final inputs are accepted harness artifacts and any cited external evidence
> Exit gate: G7 - Architecture-validated scenario and decision package ready
> Last reviewed: Not reviewed

## Purpose

Turn approved facts, decisions, architecture, implementation handoff, sizing model, operating model, and any cited external evidence into a concise decision story. The presentation is a synthesis, not a new canonical source or a product catalog.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-PRES-01` | Confirm audience and requested decision | G0 and sponsor input | Presentation brief | Decision, alternatives, authority, time, and objections are explicit | Not started | Not available |
| `TASK-PRES-02` | Build claim and evidence register | Accepted and demonstrated sources | [75-claim-and-evidence-register.md](75-claim-and-evidence-register.md) | Every material claim has a class, source, caveat, and reviewer | Not started | Not available |
| `TASK-PRES-03` | Create value story | `TASK-PRES-01`, `TASK-PRES-02` | [71-business-value-story.md](71-business-value-story.md) | Problem, change, evidence, investment, risk, and ask form one argument | Not started | Not available |
| `TASK-PRES-04` | Prepare optional audience-specific views | G2-G6 artifacts | Optional [architecture patterns](72-architecture-patterns.md), [functional architecture](73-functional-architecture.md), and [operating model](74-operating-model.md) views | Any view required for the decision audience is accurate, traceable, or explicitly not applicable | Not started | Not available |
| `TASK-PRES-05` | Assemble the architecture-validated scenario | G1-G6 packages | [76-validated-scenario.md](76-validated-scenario.md) | Every scenario step maps to realization, product or custom build, effort, cloud cost, operating owner, and validation status | Not started | Not available |
| `TASK-PRES-06` | Review and rehearse | `TASK-PRES-01`-`TASK-PRES-03`, `TASK-PRES-05`; `TASK-PRES-04` when required | Gate recommendation | Claims, timing, accessibility, objections, caveats, validated-scenario conditions, and requested decision are ready | Not started | Not available |

## G7 criteria

- The audience, decision authority, requested decision, alternatives, and consequence of delay are explicit.
- Every material claim is classified and linked to its canonical source.
- Targets, proposals, accepted decisions, designed controls, externally demonstrated results, operational evidence, and future commitments are visibly distinct.
- Canonical architecture sources and any optional audience views preserve actual boundaries and do not imply unapproved sharing, scale, compliance, or service capability.
- Costs include assumptions, range, date, and exclusions.
- Every in-scope scenario step identifies how it is achieved, its required capabilities, buy/configure/build/reuse/integrate/retire strategy, products or custom building blocks, delivery effort, cloud/service cost, and operating owner.
- Delivery effort and cloud/service cost have separate low/base/high ranges and confidence.
- Risks, limitations, production gaps, and unresolved decisions are visible.
- Content is accessible, reviewed, timed, and distribution-appropriate.

## Input change and replay

Any upstream `CHG-NNN` must identify affected claims and views. Re-run the linked presentation tasks after canonical artifacts are updated. Never repair a source conflict only in the deck.
