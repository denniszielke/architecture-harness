# Architecture Harness Repository Instructions

## Governing sources

- Treat `architecture-harness.json` as the phase, gate, and identifier manifest.
- Treat `01-preparation/15-governance.md` as the canonical source for lifecycle, accountability, evidence classes, traceability, change control, and gate rules.
- Treat `01-preparation/16-change-impact-register.md` as the canonical change and replay record.
- Treat `01-preparation/17-gate-register.md` as the canonical gate record.
- Treat `01-preparation/19-external-evidence-register.md` as the index of evidence produced outside the architecture harness.
- Treat `03-architecture/37-capability-realization.md` as the canonical buy, configure, build, reuse, integrate, or retire mapping and required product inventory.
- Treat `07-presentation/76-validated-scenario.md` as the final integrated delivery; it must link to canonical sources rather than duplicate them.
- Treat each phase plan as the owner of that phase's tasks, dependencies, outputs, completion checks, and replay rules.
- In `architecture-harness.json`, `mayStartAfter` controls when useful phase work may begin; `exitGateRequires` controls which prior gates must be satisfied before the phase exit gate can be accepted.

## Evidence discipline

Always distinguish:

- source fact;
- assumption;
- target;
- proposal;
- accepted decision;
- designed behavior or control;
- demonstrated result;
- operational evidence; and
- future commitment.

Never present one class as another. Do not invent facts, owners, approvals, accepted decisions, test results, costs, or gate outcomes. Use role placeholders when names are unavailable.

## Folder ownership

| Folder | Content it owns |
|---|---|
| `00-framing/` | Source context, vision, assumptions, scenario, and business goals |
| `01-preparation/` | Narrative, objectives, scope, deliverables, governance, change impacts, gates, risks, and external evidence references |
| `02-design/` | Product-independent logical behavior and bounded domain designs |
| `03-architecture/` | Capabilities, functional architecture, capability realization, required products, topology, dependencies, NFR realization, and ADRs |
| `04-implementation/` | Implementation plan, backlog, stories, functional building blocks, environment/release/test plans, code-generation context, and handoff |
| `05-sizing/` | Workload assumptions, observability requirements, sizing model, validation plan, delivery effort, cloud/service cost, and confidence |
| `06-operations/` | Operating model, service ownership, procedure specifications, security operations, rollout, support, and continuity plans |
| `07-presentation/` | Architecture-validated scenario and decision-focused synthesis linked to canonical facts and evidence |

Before adding an artifact, search for an existing canonical owner. Extend or link instead of duplicating content. Use lowercase, hyphenated filenames and preserve numeric phase prefixes for phase-owned artifacts.

## Controlled artifacts

- Preserve the standard header: status, canonical owner, required reviewers, gate, and last review date.
- New artifacts start in `Draft` unless actual review evidence supports another state.
- Stable accepted identifiers are never deleted or renumbered.
- Preserve accepted historical meaning through supersession rather than silent rewriting.
- Update a phase plan when its tasks, dependencies, evidence, completion checks, or gate criteria change.

## Protected baselines

Do not change accepted framing or preparation merely to make a downstream product, implementation, or presentation appear consistent. When new information changes the baseline:

1. Record `CHG-NNN` in the change impact register.
2. Update the canonical source first.
3. Identify direct links and phase tasks to replay.
4. Update affected summaries, decisions, tests, evidence, and claims.
5. Recheck impacted gates without erasing prior gate history.

## Design and architecture boundary

- Design remains product-independent and defines logical behavior, authority, contracts, failure handling, security, resilience, and operations.
- Architecture maps approved capabilities to deployable products and topology.
- A product mention in design is a candidate or inherited constraint, not an accepted choice.
- Material choices follow `03-architecture/36-architecture-decision-process.md`.
- A `Proposed` ADR leaves its `Decision` section empty.
- Only the named decision authority may accept, reject, or defer an ADR.

An ADR is required for material trust, tenant, region, jurisdiction, data, identity, platform, store, runtime, AI, integration, security, deployment, resilience, cost, portability, or long-lived coupling choices.

## Cloud architecture expectations

- Logical design remains product-independent. The starter is Microsoft-cloud-ready, but a fork may substitute another cloud ecosystem.
- Trace products such as Microsoft Fabric, Databricks, AKS, Azure Container Apps, API Management, Event Hubs, Service Bus, Microsoft 365, Copilot, Copilot Studio, and Microsoft Entra ID to approved requirements and credible comparisons.
- Map every in-scope capability to one bounded realization strategy: buy, configure, build, reuse, integrate, or retire.
- Identify every required product or service with its tier, scope, commercial model, cost driver, support lifecycle, owner, and governing ADR.
- Check current region, quota, limit, identity, networking, encryption, lifecycle, licensing, support, availability, and cost evidence.
- Define human, workload, deployment, agent, privileged, and emergency identities.
- Design security, privacy, observability, resilience, operations, cost, portability, and retirement with each capability.
- Keep platform and workload responsibilities explicit.
- Prefer modular boundaries, versioned contracts, reproducible automation, safe failure, and bounded blast radius.

## Implementation handoff boundary

- Decompose accepted architecture into a thin end-to-end backlog, user stories, functional building blocks, planned tests, and bounded context packages.
- Define environment, release, deployment, migration, security, observability, recovery, sizing, and operating expectations.
- Do not create or modify application code, infrastructure code, pipelines, cloud resources, generated artifacts, releases, or implementation test results in this harness.
- Route code generation and delivery to a downstream implementation repository or workflow.
- Treat unresolved material decisions as blockers rather than asking a coding agent to decide implicitly.
- Record downstream evidence by reference with provenance, conditions, result, and limitation.
- G4, G5, and G6 approve plans and handoffs, not implementation completion, demonstrated scale, or operating effectiveness.

## Ultimate delivery

The final G7 package must answer:

- how each in-scope business scenario step is achieved;
- which capabilities are required;
- whether each capability is bought, configured, built, reused, integrated, or retired;
- which products, services, tiers, licenses, and custom functional building blocks are required;
- the low, base, and high delivery effort by role and wave;
- the low, base, and high cloud/service cost with commercial assumptions;
- who owns and operates each realized capability; and
- which parts are architecture-validated, conditional, blocked, or supported by external evidence.

Do not mark the scenario architecture-validated while any in-scope step lacks realization, product/build mapping, effort, cost, operating ownership, or an explicit blocker.

## Validation

Run the smallest relevant tests, then `python3 scripts/validate_harness.py`. Do not mark a task or gate complete when required validation failed or evidence is missing.
