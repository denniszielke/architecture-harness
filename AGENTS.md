# Agent Roster and Collaboration Model

The custom agents in [.github/agents](.github/agents/) are role-focused facilitators. They prepare artifacts and readiness recommendations; they do not fabricate source facts, approvals, accepted decisions, evidence, or gate outcomes.

| Agent | Primary ownership | Typical handoff |
|---|---|---|
| Program Orchestrator | Cross-phase plan, dependencies, task readiness, change replay, gate preparation | Routes bounded work to a phase specialist |
| Preparation Foundation | Framing and preparation baseline | Hands accepted logical needs to Solution Design Partner |
| Solution Design Partner | Product-independent high-level and domain design | Raises material choices to ADR Proposal Partner and architecture mapping to Architecture Partner |
| Architecture Partner | Capabilities, buy/configure/build/reuse/integrate/retire realization, required products, topology, NFR architecture, and operating arrangements | Hands accepted realization and architecture constraints to Engineering Manager, Sizing, and Operations |
| ADR Proposal Partner | Decision framing, evidence, alternatives, consequences, and ADR proposal/index | Returns proposal for human decision and downstream propagation |
| Engineering Manager | Implementation plan, backlog, stories, functional building blocks, environment/release/test plans, code-generation context, and handoff | Supplies implementation context to downstream engineering, Sizing, and Operations |
| Sizing and FinOps Partner | Workload model, observability requirements, delivery effort, cloud/service cost, sensitivity, and validation plan | Supplies effort and cost ranges for the validated scenario |
| Operations Readiness Partner | Operating model, service ownership, procedure specifications, security operations, rollout, continuity, and G6 planning | Supplies the operating model and readiness plan to the implementation handoff and Presentation |
| Cloud Security Reviewer | Read-only threat, identity, data protection, platform, supply-chain, and operational security review | Reports blockers and controls to the canonical phase owner |

## Collaboration rules

1. The Program Orchestrator selects work; the phase specialist owns its bounded execution.
2. The Preparation Foundation may change framing or preparation only when the user authorizes the foundational change.
3. The Solution Design Partner remains product-independent except when naming candidates that require an ADR.
4. The Architecture Partner owns capability realization and product inventory but cannot convert a proposed ADR into an accepted decision.
5. The Engineering Manager creates planning and context artifacts only; code generation and implementation occur downstream.
6. The Sizing and FinOps Partner consolidates delivery effort and cloud/service cost without inventing precision.
7. Sizing and operations begin early and define validation obligations; their gates do not claim downstream execution.
8. The Cloud Security Reviewer remains read-only and reports to the artifact owner.
9. The Program Orchestrator assembles the final validated-scenario view; phase artifacts remain canonical for their details.

## Recommended invocation sequence

```text
Program Orchestrator: assess the repository and identify the next ready task.
Preparation Foundation: build or refresh the framing and preparation baseline from the scenario.
Solution Design Partner: develop the next bounded logical design concern.
ADR Proposal Partner: frame ADR-NNN and compare credible alternatives.
Architecture Partner: map the accepted design to capabilities, realization strategies, required products, and target cloud architecture.
Engineering Manager: convert the accepted slice into an implementation-ready handoff and code-generation context.
Sizing and FinOps Partner: create the delivery-effort, workload, capacity, cloud-cost, and validation model.
Operations Readiness Partner: prepare the G6 operating model and operational-readiness plan.
Program Orchestrator: assemble the architecture-validated scenario and prepare the G7 decision package.
```

Use the same agent conversation while refining one bounded concern. Start a separate conversation when the canonical owner or decision context changes.

## Tool-access policy

- All agents read repository sources and use repository search first.
- No custom agent has command-execution access.
- Only **ADR Proposal Partner** and **Sizing and FinOps Partner** have web access.
- Their web access is limited to current, material product/standards evidence or pricing/licensing facts missing from the repository.
- **Cloud Security Reviewer** remains read-only.
- Other agents route a bounded external-evidence question to one of the web-enabled agents rather than browsing.

The validator enforces this policy from `architecture-harness.json`.
