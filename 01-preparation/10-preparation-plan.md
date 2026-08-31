# Preparation Plan

> Status: Draft
> Canonical owner: Product or program lead - name to be assigned
> Required reviewers: Sponsor, business owner, solution architect, engineering lead
> Entry gate: G0 - Framing sufficient for preparation
> Exit gate: G1 - Preparation baseline accepted
> Last reviewed: Not reviewed

## Purpose

Convert the framing package into an executable, governed program baseline: narrative, objectives, scope, deliverables, roles, dependencies, evidence expectations, and gate criteria.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-PREP-01` | Reconcile framing | G0 recommendation | Framing consistency findings | Conflicts and missing evidence are recorded | Not started | Not available |
| `TASK-PREP-02` | Build stakeholder narrative | `TASK-PREP-01` | [11-narrative.md](11-narrative.md) | Current and future experience has a bounded story | Not started | Not available |
| `TASK-PREP-03` | Define measurable objectives | `TASK-PREP-01` | [12-objectives.md](12-objectives.md) | Objectives have measures and evidence plans | Not started | Not available |
| `TASK-PREP-04` | Set scope and exclusions | `TASK-PREP-02`, `TASK-PREP-03` | [13-scope.md](13-scope.md) | In, out, deferred, and experimental work is explicit | Not started | Not available |
| `TASK-PREP-05` | Define deliverables and acceptance | `TASK-PREP-04` | [14-deliverables.md](14-deliverables.md) | Each deliverable has an owner, inputs, acceptance, and evidence | Not started | Not available |
| `TASK-PREP-06` | Establish governance and traceability | `TASK-PREP-01` | [15-governance.md](15-governance.md), registers | Roles, lifecycle, identifiers, change control, and gates are usable | Not started | Not available |
| `TASK-PREP-07` | Prepare G1 review | `TASK-PREP-02`-`TASK-PREP-06` | Gate recommendation | Conditions and unresolved dependencies are visible | Not started | Not available |

## G1 criteria

- Objectives trace to source facts, assumptions, and goals.
- Scope is sufficient to define a thin, testable end-to-end slice.
- Deliverables have acceptance criteria and evidence expectations.
- Accountable roles and decision authorities are named or explicitly unassigned.
- Change, risk, ADR, and gate processes are usable.
- Downstream phases can identify their inputs without copying the baseline.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Framing meaning or goal | `TASK-PREP-01`-`TASK-PREP-05` as linked | All phases and gates |
| Objective or measure | `TASK-PREP-03` | Design acceptance, tests, sizing, claims |
| Scope or exclusion | `TASK-PREP-04`, `TASK-PREP-05` | Design, ADRs, backlog, cost, operating model |
| Governance or authority | `TASK-PREP-06` | Controlled headers, ADRs, gate records |
| Deliverable acceptance | `TASK-PREP-05` | Phase plans, tests, presentation evidence |

Use [16-change-impact-register.md](16-change-impact-register.md) to select the smallest replay set. Do not reopen unaffected accepted work without a traceable dependency.
