# Code-Generation Context Contract

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Architecture, security, platform, data, test, and repository owners
> Gate: G4
> Last reviewed: Not reviewed

## Purpose

Define the context that a downstream human or coding agent must receive before generating implementation artifacts. The architecture harness prepares and validates this context; it does not generate code.

## Context packages

| Context ID | Functional building block | Source specifications | Intended downstream target | Required review | Planned tests | Refresh trigger |
|---|---|---|---|---|---|---|
| `CTX-001` | `FBB-NNN` | [Requirements, ADRs, contracts, NFRs, stories, operating model] | [Implementation repository/component] | [Owner roles] | `TEST-IMP-NNN` | [Changed canonical input] |

## Guardrails

- Use only accepted requirements, contracts, architecture, and ADRs, plus explicitly labeled assumptions.
- Include exact scope, exclusions, authoritative state, interfaces, dependencies, identity, data, security, failure, recovery, NFR, observability, deployment, and operating requirements.
- Identify unresolved decisions as blockers; do not ask a coding agent to resolve them implicitly.
- Never include credentials, personal data, proprietary examples, or unapproved endpoints.
- Require human review for trust boundaries, identity, authorization, data handling, infrastructure, destructive actions, and consequential AI tools.
- State repository conventions, reuse expectations, allowed dependencies, target paths, acceptance tests, and validation commands when the downstream repository is known.
- Version the context and link every canonical input so a changed source can trigger replay.

## Required context sections

1. Outcome, scope, exclusions, and linked user stories.
2. Functional building block responsibility and authoritative state.
3. Requirements, ADRs, NFRs, risks, and inherited constraints.
4. API, event, message, data, schema, and migration contracts.
5. Human, workload, pipeline, agent, privileged, and emergency identities.
6. Security, privacy, policy, evidence, and supply-chain controls.
7. Failure, retry, idempotency, replay, reconciliation, rollback, and recovery behavior.
8. Deployment target, configuration, secrets, feature, environment, and dependency boundaries.
9. Logs, metrics, traces, audit, SLO, cost, and operational ownership.
10. Planned tests, acceptance, expected evidence, prohibited decisions, and escalation path.

## Downstream response contract

The downstream workflow should return:

- implementation commit, pull request, and artifact identifiers;
- deviations, new assumptions, unresolved decisions, and architecture conflicts;
- tests executed and evidence locations;
- measured performance, cost, security, and operational findings;
- production or operating gaps; and
- any `CHG-NNN` request needed to replay architecture-harness artifacts.

Return architecture conflicts, deviations, failed assumptions, and new decision needs through [49-implementation-handoff.md](49-implementation-handoff.md) and the [change impact register](../01-preparation/16-change-impact-register.md). Keep code, test output, measurements, and operational records downstream; add only stable references and bounded metadata to the [external evidence register](../01-preparation/19-external-evidence-register.md).
