# Architecture Decision Process

> Status: Draft
> Canonical owner: Solution or enterprise architect - name to be assigned
> Required reviewers: Decision-specific domain owners
> Gate: G3 and continuous architecture governance
> Last reviewed: Not reviewed

## When an ADR is required

Create an ADR when a choice:

- changes a trust, tenant, organization, region, jurisdiction, data, identity, or decision-authority boundary;
- selects or rejects a strategic platform, store, runtime, model, integration, security, deployment, or operating pattern;
- materially affects security, privacy, reliability, performance, scale, cost, portability, operations, or assurance;
- creates long-lived coupling, migration cost, concentration, duplication, or technical debt;
- resolves a significant quality-attribute or stakeholder trade-off;
- establishes an exception or supersedes an accepted decision.

Routine, reversible implementation choices within accepted boundaries do not need an ADR.

## Lifecycle

| State | Meaning | Permitted action |
|---|---|---|
| `Proposed` | Context, options, recommendation, and evidence are ready for review | Gather reviews; keep `Decision` empty |
| `Accepted` | Named authority accepted the decision and consequences | Implement conditions and validation |
| `Rejected` | Authority declined the proposal | Record reason and next action |
| `Deferred` | Authority moved the choice to a named trigger or gate | Record bounded impact and fallback |
| `Superseded` | A later accepted ADR replaces it | Link both records and migrate traceability |

Only the named decision authority may set `Accepted`, `Rejected`, or `Deferred`.

## Decision workflow

1. **Frame:** one decision question, scope, authority, reviewers, due gate, linked requirements, and prototype/target distinction.
2. **Research:** current authoritative product facts, service limits, regional availability, identity, networking, security, lifecycle, licensing, operations, and cost.
3. **Compare:** at least two credible alternatives plus retain, do nothing, or defer when meaningful. Test mandatory constraints before preferences.
4. **Propose:** recommendation, rationale, consequences, risks, proof obligations, implementation conditions, fallback, and revisit triggers.
5. **Decide:** authority records the outcome and conditions.
6. **Propagate:** update architecture, dependencies, backlog, tests, operations, cost, risks, and claims.
7. **Validate:** attach evidence and revisit on the declared triggers.

## Evidence standard

For each external source, record title, publisher, URL, retrieval date, relevant finding, and limitation. For each experiment, record version, environment, data, configuration, method, expected result, actual result, and limitation.

## Supersession

Never rewrite accepted historical rationale to fit a new choice. Create a new ADR with a new ID, link both records, set the old ADR to `Superseded` only after the new decision is accepted, and review all dependent artifacts and gates.

Use [decisions/adr-template.md](decisions/adr-template.md) and maintain [decisions/README.md](decisions/README.md).
