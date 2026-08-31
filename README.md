# Architecture Harness

A minimal, agent-assisted repository template for moving a cloud solution from an initial idea to an evidence-backed architecture, implementation plan, operating model, and decision presentation.

The harness is intentionally scenario-neutral and product-independent through logical design. Its starter mapping guidance is Microsoft-cloud-ready: it supports data platforms such as Microsoft Fabric or Databricks; application platforms such as AKS or Azure Container Apps; integration services such as API Management, Event Hubs, and Service Bus; user experiences such as Microsoft 365, Copilot, and Copilot Studio; and identity anchored in Microsoft Entra ID. These are candidates, not defaults, and a fork can substitute another cloud ecosystem. Material product choices require an architecture decision record (ADR).

## What this repository provides

- Eight governed phases with a plan and minimal starter artifacts in each phase.
- Readiness gates from framing through presentation.
- Stable identifiers and one canonical owner for each fact, requirement, decision, result, and claim.
- Task-level replay rules so changed inputs can be propagated without restarting the whole project.
- GitHub Copilot custom agents, reusable prompts, and skills for the core architecture roles.
- A lightweight validator and CI workflow for structure, metadata, links, and phase/gate consistency.

## Phase model

| Phase | Purpose | Exit gate |
|---|---|---|
| [00-framing](00-framing/) | Establish the source scenario, vision, assumptions, and business goals | G0 - Framing sufficient for preparation |
| [01-preparation](01-preparation/) | Baseline objectives, scope, deliverables, governance, and execution | G1 - Preparation baseline accepted |
| [02-design](02-design/) | Define product-independent behavior and bounded design concerns | G2 - Logical design ready for architecture |
| [03-architecture](03-architecture/) | Map capabilities and design to deployable products, topology, NFRs, and decisions | G3 - Architecture ready for implementation |
| [04-implementation](04-implementation/) | Turn accepted scope and decisions into backlog, environments, code, automation, and evidence | G4 - Implementation evidence accepted |
| [05-sizing](05-sizing/) | Validate workload assumptions, capacity, observability, performance, and cost | G5 - Sizing confidence accepted |
| [06-operations](06-operations/) | Define ownership, service management, security operations, rollout, and recovery | G6 - Operational readiness accepted |
| [07-presentation](07-presentation/) | Build a traceable business and architecture decision story | G7 - Decision package ready |

Sizing starts after logical design with an indicative model and is calibrated with implementation evidence. Operations starts after preparation and becomes gateable after architecture, implementation, and sizing evidence exist. Presentation work starts after framing and collects evidence throughout.

## Start a project

1. Fork this repository and create a project branch.
2. Replace the placeholders in [00-framing/03-scenario.md](00-framing/03-scenario.md) with the supplied scenario. Preserve source wording and provenance.
3. Select the **Program Orchestrator** custom agent and ask it to assess the repository and propose the next ready task.
4. Complete only the tasks whose dependencies are ready. Keep artifacts in `Draft` until actual review occurs.
5. Record input changes in [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md), rerun affected tasks, and recheck dependent gates.
6. Create ADR proposals for material choices; only a named decision authority may change a proposal to an accepted decision.
7. Run the validator before review:

   ```bash
   python3 scripts/validate_harness.py
   ```

## Operating rules

1. **One canonical owner.** A fact, assumption, requirement, decision, design detail, result, or claim is maintained in one artifact and linked elsewhere.
2. **Evidence states are not interchangeable.** Keep source facts, assumptions, proposals, accepted decisions, designed controls, demonstrated results, and operational evidence distinct.
3. **Logical design precedes product mapping.** Product names in design are candidates until an accepted ADR governs the material choice.
4. **Security and operations are continuous.** Identity, data protection, threat handling, observability, resilience, deployment, cost, and support are designed with the capability.
5. **A gate is a recorded decision, not document completeness.** Agents may recommend readiness but cannot invent approval.
6. **Changes replay through links.** Re-run the smallest affected task set, then review downstream artifacts and gate evidence.
7. **A prototype is bounded evidence.** It does not prove production scale, compliance, resilience, or operating effectiveness.

## Agent roster

The repository includes the requested agents:

- Program Orchestrator
- Preparation Foundation
- Solution Design Partner
- Architecture Partner
- ADR Proposal Partner
- Engineering Manager

It also includes focused Sizing and FinOps, Operations Readiness, and Cloud Security reviewers so cost, operation, and security are not deferred to the end. See [AGENTS.md](AGENTS.md).

Custom agents, repository instructions, `AGENTS.md`, and agent skills are usable by supported GitHub Copilot cloud and IDE agent surfaces. Files under [.github/prompts](.github/prompts/) are VS Code slash-command conveniences; equivalent portable behavior is held in the custom agents and skills because cloud agents do not consume prompt files.

## Repository control plane

- [architecture-harness.json](architecture-harness.json) is the machine-readable phase, gate, and identifier manifest.
- [01-preparation/15-governance.md](01-preparation/15-governance.md) owns lifecycle, accountability, evidence, and change rules.
- [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md) records changed inputs and required replay.
- [01-preparation/17-gate-register.md](01-preparation/17-gate-register.md) records readiness recommendations and actual gate decisions.
- [01-preparation/18-risk-register.md](01-preparation/18-risk-register.md) owns cross-phase risk and residual-risk decisions.
- [03-architecture/36-architecture-decision-process.md](03-architecture/36-architecture-decision-process.md) and [03-architecture/decisions/README.md](03-architecture/decisions/README.md) govern material decisions.
- [04-implementation/48-evidence-index.md](04-implementation/48-evidence-index.md) indexes reproducible evidence used by gates and claims.

## Deliberate limits

This starter does not contain a preselected reference architecture, production-ready infrastructure, legal or compliance conclusions, approved owners, accepted decisions, test results, or cloud credentials. Project teams must add domain-specific assurance artifacts when the scenario, industry, data, jurisdictions, or organizational policy require them.
