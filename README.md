# Architecture Harness

A fork-ready, agent-assisted method for taking a cloud solution from an initial scenario to an evidence-backed design, target architecture, implementation, sizing model, operating model, and decision presentation.

The harness is product-independent through logical design and Microsoft-cloud-ready during architecture mapping. Microsoft Fabric, Databricks, AKS, Azure Container Apps, API Management, Event Hubs, Service Bus, Microsoft 365, Copilot, Copilot Studio, and Microsoft Entra ID are candidates, not defaults. Material product choices require evidence and an architecture decision record (ADR).

## Who this is for

Use the harness when a project needs to:

- turn an incomplete business or technical scenario into a governed architecture;
- keep business outcomes, requirements, design, products, implementation, operations, and evidence connected;
- evaluate cloud platforms without selecting products before requirements are understood;
- make security, resilience, sizing, cost, deployment, and operations part of the architecture process;
- revisit only the affected work when an input, assumption, dependency, or decision changes; and
- prepare clear readiness and investment decisions without overstating prototype evidence.

The repository is a starter, not a completed reference architecture. A new project is expected to replace placeholders, add domain-specific requirements, and assign real owners and decision authorities.

## What the harness contains

- Eight phase folders from framing through presentation.
- One plan per phase with tasks, dependencies, completion checks, status, evidence, and replay rules.
- G0-G7 readiness gates.
- Stable identifiers and canonical ownership rules.
- Change-impact and task-level replay.
- An ADR process and reusable ADR template.
- Registers for assumptions, requirements, risks, gates, evidence, sizing, tests, and claims.
- GitHub Copilot custom agents, portable agent skills, and VS Code prompt files.
- A manifest-driven validator and GitHub Actions workflow.

## Quick start

### 1. Fork and clone

Fork this repository, clone the fork, and create a project branch:

```bash
git clone https://github.com/<your-account>/<your-project>.git
cd <your-project>
git switch -c project/initial-framing
```

Do not fill every template immediately. Start with the source scenario and let the phase plans identify the next dependency-ready work.

### 2. Add the source scenario

Open [00-framing/03-scenario.md](00-framing/03-scenario.md) and record:

- each source and its provenance;
- the current situation and desired change;
- known stakeholders and decision authorities;
- organizational, data, system, environment, and jurisdictional boundaries; and
- missing information as open questions.

Preserve supplied source wording where material. Put interpretations and unverified beliefs in [00-framing/02-assumptions.md](00-framing/02-assumptions.md), not in the source record.

### 3. Start with the Program Orchestrator

In a supported GitHub Copilot agent surface, select **Program Orchestrator** and use:

```text
Assess this new project. Read the framing sources, governance, phase plans,
open changes, and gate register. Identify the smallest dependency-ready task,
its owner, required output, completion check, and evidence.
```

In VS Code, the `/start-architecture-project` prompt provides the same starting workflow. Prompt files are VS Code conveniences; custom agents and skills contain the portable behavior used by supported cloud agent surfaces.

### 4. Execute one bounded task

Use the specialist selected by the Program Orchestrator. For example:

```text
Preparation Foundation: build the G0 framing package from the supplied scenario.
Do not select products or invent owners, facts, evidence, or approval.
```

Update the task row in the owning phase plan:

- `Not started`
- `Ready`
- `Blocked`
- `In progress`
- `Replay required`
- `Complete with evidence`

A task is complete only when its completion check is met and its evidence is linked.

### 5. Validate before review

Run:

```bash
python3 scripts/validate_harness.py
```

The validator checks required artifacts, phase and gate consistency, controlled statuses, agent and skill metadata, identifier namespaces, local links and anchors, path casing, and task-table structure. The same validation runs in GitHub Actions.

## How the lifecycle works

The phases are progressive but not strictly sequential.

| Phase | Main outcome | May start after | Exit gate requires | Exit gate |
|---|---|---|---|---|
| [00-framing](00-framing/) | Source-grounded vision, assumptions, scenario, and goals | Project input | Framing criteria | G0 |
| [01-preparation](01-preparation/) | Objectives, scope, deliverables, governance, and execution baseline | G0 | G0 | G1 |
| [02-design](02-design/) | Product-independent logical design and measurable requirements | G1 | G1 | G2 |
| [03-architecture](03-architecture/) | Capabilities, products, topology, dependencies, NFR realization, and decisions | G2 | G2 | G3 |
| [04-implementation](04-implementation/) | Reproducible implementation and bounded evidence | G3 | G3 | G4 |
| [05-sizing](05-sizing/) | Workload model, tests, capacity, cost, and scaling triggers | G2 | G3 and G4 | G5 |
| [06-operations](06-operations/) | Service ownership, procedures, security operations, rollout, and continuity | G1 | G3, G4, and G5 | G6 |
| [07-presentation](07-presentation/) | Traceable business, architecture, evidence, and decision story | G0 | G1-G6 | G7 |

The distinction is important:

- `mayStartAfter` identifies when useful work can begin.
- `exitGateRequires` identifies the prior gates required before the phase exit gate can be accepted.

This permits early work on cost, operating responsibilities, and presentation evidence without claiming those phases are ready.

## Phase-by-phase usage

### 00 - Framing

**Goal:** understand the problem before designing a solution.

1. Capture source material and limitations in [00-framing/03-scenario.md](00-framing/03-scenario.md).
2. Record unverified beliefs in [00-framing/02-assumptions.md](00-framing/02-assumptions.md).
3. Define the mission, future state, principles, and non-goals in [00-framing/01-vision.md](00-framing/01-vision.md).
4. Define measurable or explicitly unmeasured value in [00-framing/04-business-goals.md](00-framing/04-business-goals.md).
5. Use [00-framing/00-framing-plan.md](00-framing/00-framing-plan.md) to assess G0 readiness.

Recommended agent: **Preparation Foundation**.

Do not select cloud products in this phase. A product named in a supplied source remains source context, not an accepted architecture.

### 01 - Preparation

**Goal:** establish the controlled project baseline.

1. Turn the scenario into a stakeholder and change narrative.
2. Define measurable objectives and measurement gaps.
3. Classify scope as in scope, out of scope, deferred, or experimental.
4. Define deliverables with observable acceptance and evidence.
5. Assign accountable roles or retain explicit role placeholders.
6. Baseline governance, identifiers, risk, change, and gate handling.

The core control artifacts are:

- [01-preparation/15-governance.md](01-preparation/15-governance.md)
- [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md)
- [01-preparation/17-gate-register.md](01-preparation/17-gate-register.md)
- [01-preparation/18-risk-register.md](01-preparation/18-risk-register.md)

Recommended agents: **Preparation Foundation** and **Program Orchestrator**.

### 02 - Design

**Goal:** define how the solution must behave without preselecting products.

Use [02-design/21-high-level-design.md](02-design/21-high-level-design.md) for the cross-domain model and the files under [02-design/domains](02-design/domains/) for bounded concerns:

- data model and data-platform behavior;
- platform concept;
- integration patterns;
- application and AI experience;
- operating model;
- resilience; and
- security.

Record product-independent functional, design, and non-functional requirements in [02-design/23-requirements-and-acceptance.md](02-design/23-requirements-and-acceptance.md).

Recommended agent: **Solution Design Partner**.

Raise a decision question when the design reaches a material trust, data, platform, runtime, integration, security, resilience, cost, or portability choice. Do not hide that choice in a diagram.

### 03 - Architecture

**Goal:** map the accepted logical design to deployable cloud products and operating arrangements.

1. Define enterprise capabilities in [03-architecture/31-enterprise-capabilities.md](03-architecture/31-enterprise-capabilities.md).
2. Reconcile product-independent functional domains.
3. Compare credible products and patterns against mandatory constraints.
4. Define target topology, environments, regions, networks, identities, data locations, management planes, and ownership.
5. Record functional and delivery dependencies.
6. Map NFRs to architecture mechanisms, telemetry, and validation.
7. Resolve implementation-blocking choices through ADRs.

Recommended agents:

- **Architecture Partner** for target mapping and topology.
- **ADR Proposal Partner** for material choices.
- **Cloud Security Reviewer** for a read-only threat-led review.
- **Sizing and FinOps Partner** for the indicative G3 estimate.

Microsoft cloud services in the templates are candidates. Select them only when their capabilities, limits, region, identity, networking, availability, lifecycle, support, licensing, cost, and portability fit the accepted requirements.

### 04 - Implementation

**Goal:** produce a reproducible thin end-to-end implementation and bounded evidence.

1. Convert accepted scope and decisions into the implementation backlog.
2. Establish reproducible and isolated environments.
3. Use experiments for material uncertainty.
4. Implement a thin vertical slice before broadening layers.
5. Automate build, policy, security checks, deployment, verification, rollback, reset, and evidence capture.
6. Test normal, invalid, duplicate, unauthorized, dependency-failure, recovery, and acceptance paths.
7. Index durable evidence in [04-implementation/48-evidence-index.md](04-implementation/48-evidence-index.md).

Recommended agent: **Engineering Manager**.

Implement only accepted constraints or explicitly bounded experiments. If engineering discovers that an assumption or architecture decision is wrong, stop the affected work and use change-impact replay.

### 05 - Sizing

**Goal:** replace architectural guesses with traceable ranges and measured evidence.

Sizing has two passes:

1. **Indicative at G3:** build workload assumptions and compare candidate capacity and cost ranges.
2. **Calibrated after G4:** use implementation measurements to refine capacity, performance, cost, and scaling triggers.

Include steady, peak, burst, seasonal, growth, retention, retry, replay, failure, recovery, redundancy, non-production, observability, security, licensing, support, and network effects where relevant.

Recommended agent: **Sizing and FinOps Partner**.

Never hide list-price assumptions, negotiated discounts, commitment models, currency, region, retrieval date, uncertainty, or exclusions.

### 06 - Operations

**Goal:** show that accountable teams can operate, secure, change, recover, and retire the service.

1. Assign service, product, engineering, data, security, support, and vendor responsibilities.
2. Automate frequent and high-risk procedures with authorization, safety checks, rollback, and evidence.
3. Operationalize identity, vulnerability, threat, incident, secret, key, certificate, data, and supply-chain controls.
4. Define rollout waves, migration, coexistence, validation, hypercare, rollback, and decommissioning.
5. Exercise incident response, backup, restore, failover, reduced-capacity operation, and continuity.

Recommended agents:

- **Operations Readiness Partner**
- **Cloud Security Reviewer**
- **Engineering Manager** for automation changes

A written runbook is designed evidence. Operational readiness requires executed procedures and reviewed results in the intended scope.

### 07 - Presentation

**Goal:** prepare a decision package that is accurate at executive and technical altitude.

1. State the audience, decision authority, requested decision, alternatives, and consequence of delay.
2. Register every material claim in [07-presentation/75-claim-and-evidence-register.md](07-presentation/75-claim-and-evidence-register.md).
3. Build the business-value story.
4. Simplify the accepted architecture and functional views without changing their meaning.
5. Explain ownership, rollout, support, security, cost, resilience, and remaining gaps.
6. Review claims, timing, accessibility, objections, and distribution constraints.

Recommended agent: **Program Orchestrator**, with the phase owners reviewing claims sourced from their artifacts.

Never repair an upstream inconsistency only in the presentation. Correct the canonical source and replay the affected claim.

## Using the agents

The detailed roster and collaboration rules are in [AGENTS.md](AGENTS.md).

| Agent | Use it for |
|---|---|
| Program Orchestrator | Current-state assessment, task selection, dependency management, replay, and gate preparation |
| Preparation Foundation | Framing and preparation artifacts |
| Solution Design Partner | Product-independent design and requirements |
| Architecture Partner | Capabilities, product mapping, topology, dependencies, and NFR realization |
| ADR Proposal Partner | Decision framing, research, alternatives, consequences, and proposed ADRs |
| Engineering Manager | Backlog, environments, experiments, code, automation, tests, and evidence |
| Sizing and FinOps Partner | Workload, telemetry, performance, capacity, cost, and sensitivity |
| Operations Readiness Partner | Service ownership, procedures, rollout, support, security operations, and continuity |
| Cloud Security Reviewer | Read-only security and threat review |

### Example agent prompts

Start or resume the program:

```text
Assess the current repository state. Identify open changes, blocked assumptions,
ready tasks, missing evidence, and the next recommended phase task.
```

Develop one design concern:

```text
Design the event-driven integration concern for REQ-012.
Cover normal, duplicate, delayed, unauthorized, failed dependency, replay,
and recovery behavior. Keep the design product-independent and identify ADRs.
```

Map a target architecture:

```text
Map the accepted integration design to credible Azure service alternatives.
Compare Event Hubs, Service Bus, and other relevant patterns against ordering,
delivery, replay, throughput, identity, network, operations, cost, and exit needs.
Do not accept the decision.
```

Plan implementation:

```text
Convert the accepted vertical slice into the smallest evidence-producing
implementation increment. Define dependencies, guardrails, tests, environment,
rollback, evidence, and production delta.
```

Prepare a gate:

```text
Prepare the G3 readiness recommendation. Assess every criterion against current
evidence, distinguish designed from demonstrated behavior, and leave the actual
gate decision to the named authority.
```

## Day-to-day task workflow

For every task:

1. Read [architecture-harness.json](architecture-harness.json), governance, the owning phase plan, direct inputs, open changes, and relevant gate record.
2. Confirm the phase `mayStartAfter` condition and direct task dependencies.
3. Set the task to `Ready` or `Blocked`.
4. Assign the accountable role and expected output.
5. Define completion and evidence before authoring.
6. Set the task to `In progress`.
7. Update the canonical artifact first.
8. Update summaries, links, plans, and registers only when needed.
9. Run the smallest relevant validation.
10. Link evidence and set `Complete with evidence`, or record the exact blocker.

Do not mark a task complete because its file exists.

## Canonical ownership and evidence

Each material statement has one owner:

```text
source or assumption
  -> goal, objective, and scope
  -> requirement and design
  -> capability, architecture, and ADR
  -> implementation item and test
  -> evidence
  -> presentation claim
```

Other artifacts summarize and link rather than copy the detail.

Use the evidence classes consistently:

| Class | Meaning |
|---|---|
| Source fact | Directly supported by a cited source |
| Assumption | Unverified and assigned a validation action |
| Target | Desired measurable state, not an achieved result |
| Proposal | Candidate direction awaiting decision |
| Accepted decision | Choice recorded by the named authority |
| Designed | Specified but not executed |
| Demonstrated | Executed under stated test conditions |
| Operational evidence | Observed in the intended live operating context |
| Future commitment | Planned work with ownership and dependencies |

## Architecture decisions

Use [03-architecture/36-architecture-decision-process.md](03-architecture/36-architecture-decision-process.md) when a choice:

- changes a trust, tenant, organization, region, jurisdiction, data, identity, or decision-authority boundary;
- selects a strategic platform, store, runtime, AI model, integration, security, deployment, or operating pattern;
- materially affects security, privacy, reliability, performance, scale, cost, portability, or operations;
- creates long-lived coupling, migration cost, concentration, duplication, or debt; or
- establishes an exception or supersedes an accepted decision.

To create an ADR:

1. Add a decision question to [03-architecture/decisions/README.md](03-architecture/decisions/README.md).
2. Copy [03-architecture/decisions/adr-template.md](03-architecture/decisions/adr-template.md).
3. Compare at least two credible alternatives and retain, defer, or do nothing when meaningful.
4. Evaluate mandatory constraints before weighted preferences.
5. Record current evidence, limitations, consequences, implementation conditions, validation, fallback, and revisit triggers.
6. Keep `## Decision` empty while the ADR is `Proposed`.
7. Let only the named decision authority set `Accepted`, `Rejected`, or `Deferred`.
8. Propagate the decision to affected design, architecture, backlog, tests, sizing, operations, risks, and claims.

Never rewrite an accepted ADR to fit a later choice. Create a new ADR and supersede the old one after the new decision is accepted.

## Responding to changed inputs

Do not restart the entire project when an input changes.

1. Add a `CHG-NNN` row to [01-preparation/16-change-impact-register.md](01-preparation/16-change-impact-register.md).
2. Record the canonical source, old meaning, and new meaning.
3. Follow direct identifiers and links.
4. Identify affected tasks, decisions, tests, evidence, risks, estimates, procedures, gates, and claims.
5. Mark only affected tasks `Replay required`.
6. Update the canonical source first.
7. Re-run the affected tasks in dependency order.
8. Revalidate evidence and reassess impacted gates.
9. Close the change after affected owners review the reconciliation.

Example:

```text
The transaction peak assumption changed from 500 to 2,000 events per second.
Assess the impact, create CHG-NNN, identify the smallest replay set, and list
the NFRs, ADRs, sizing tests, costs, operating procedures, and gates to recheck.
```

Preserve unaffected accepted work and historical gate decisions.

## Running a gate review

A gate is a human decision supported by evidence, not an automated status and not a document-completeness check.

For G0-G7:

1. Read the phase exit criteria.
2. Verify the manifest's `exitGateRequires`.
3. Check open changes, assumptions, ADRs, dependencies, risks, tests, and evidence.
4. Classify criteria as ready, ready with conditions, blocked, not evidenced, or not applicable with rationale.
5. Record a readiness recommendation in [01-preparation/17-gate-register.md](01-preparation/17-gate-register.md).
6. Leave the decision, authority, and date unchanged until the actual authority acts.
7. Append the real outcome to the gate decision history.

Agents can prepare recommendations. They cannot invent approval or accepted residual risk.

## Identifiers

Use stable identifiers to connect artifacts. Common examples are:

- `SRC-001`, `ASM-001`, `GOAL-001`, `OBJ-001`, and `SCP-001`
- `REQ-001`, `DES-001`, `NFR-001`, and `CAP-001`
- `ADR-001`, `RISK-001`, `DEP-001`, and `CHG-001`
- `IMP-001`, `US-001`, `EVID-001`, and `CLAIM-001`
- `TASK-DES-01`, `TASK-ARC-01`, and other phase task IDs
- `TEST-IMP-001`, `TEST-SIZE-001`, and `TEST-OPS-001`

The complete registry is in [architecture-harness.json](architecture-harness.json). Do not renumber accepted records or reuse retired decision IDs.

## Customizing a fork

Safe customizations include:

- replacing the Microsoft cloud candidate list with another cloud ecosystem;
- adding domain-specific design artifacts under the owning phase;
- adding assurance, privacy, regulatory, safety, or model-risk roles and artifacts;
- extending identifier prefixes in [architecture-harness.json](architecture-harness.json);
- adding specialist agents or skills for recurring project workflows; and
- adding implementation-specific source, infrastructure, tests, and runbooks.

When adding or removing a required starter artifact:

1. identify its canonical owner;
2. update the owning phase plan;
3. update `requiredArtifacts` in [architecture-harness.json](architecture-harness.json);
4. update links and agent instructions;
5. run the validator; and
6. document any changed gate or replay behavior.

Avoid creating a root document when a phase folder already owns the content.

## Working without GitHub Copilot

The harness does not require an AI agent. A team can use the same process manually:

1. select the next ready task from the phase plan;
2. assign the accountable role;
3. update the canonical artifact;
4. review against the completion check;
5. attach evidence;
6. run validation; and
7. prepare the gate recommendation.

Agents accelerate discovery, consistency checking, and drafting. Human owners remain responsible for facts, architecture decisions, risk acceptance, and gates.

## Repository map

```text
.github/
  agents/       Role-based Copilot agents
  prompts/      VS Code prompt files
  skills/       Portable architecture workflows
  workflows/    Harness validation
00-framing/     Vision, assumptions, scenario, and goals
01-preparation/ Objectives, scope, governance, changes, gates, and risks
02-design/      Product-independent design and requirements
03-architecture/Capabilities, cloud mapping, topology, NFRs, and ADRs
04-implementation/Backlog, environments, automation, tests, and evidence
05-sizing/      Workload, observability, performance, capacity, and cost
06-operations/  Ownership, procedures, security operations, rollout, continuity
07-presentation/Business value, architecture views, operating model, and claims
scripts/        Repository validation
```

## Deliberate limits

This starter does not contain:

- a preselected reference architecture;
- production-ready infrastructure or application code;
- approved owners, accepted decisions, or gate outcomes;
- legal, regulatory, privacy, or compliance conclusions;
- production data, credentials, or cloud configuration;
- demonstrated test, scale, resilience, cost, or operating evidence; or
- a promise that every project needs every candidate technology.

Add project-specific assurance and delivery controls when the scenario, industry, data, jurisdictions, organization, or risk profile requires them.
