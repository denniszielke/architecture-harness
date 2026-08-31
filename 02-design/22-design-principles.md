# Design Principles

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Business, security, data, engineering, and operations owners
> Gate: G2
> Last reviewed: Not reviewed

Adapt these starter principles to the project. Preserve links to the vision and record material exceptions through the ADR process.

| ID | Principle | Observable design consequence | Exception path |
|---|---|---|---|
| `DPR-001` | Outcomes and capabilities precede products | Product selection traces to an accepted need and comparison | ADR |
| `DPR-002` | Identity is explicit across every trust boundary | Human, workload, service, and agent identities are authenticated and authorized | Security review and ADR |
| `DPR-003` | Data has an accountable owner and declared purpose | Authority, classification, lineage, quality, retention, and permitted use are visible | Data owner decision |
| `DPR-004` | Interfaces are contracts | APIs, events, messages, and data products are versioned, observable, and testable | ADR for material compatibility trade-off |
| `DPR-005` | Failure, recovery, and replay are designed paths | Timeouts, retries, idempotency, degraded modes, reconciliation, and restore are explicit | Risk acceptance |
| `DPR-006` | Least privilege and secure defaults apply | Access is denied unless purpose and policy permit it; secrets are not embedded | Security exception |
| `DPR-007` | Automation is reproducible and reviewable | Environments, policy, build, release, tests, and rollback are version controlled | Time-bounded exception |
| `DPR-008` | Observability is part of the contract | Logs, metrics, traces, audit, correlation, redaction, and ownership are defined | NFR review |
| `DPR-009` | AI is bounded, attributable, and replaceable | Grounding, tool permissions, evaluation, human control, safe fallback, and versioning are explicit | AI risk decision |
| `DPR-010` | Prototype evidence is not production proof | Shortcuts and production deltas remain visible and owned | Gate condition |
| `DPR-011` | Cost and sustainability are architecture signals | Unit economics, scale drivers, idle cost, and optimization levers are measurable | G5 condition |
| `DPR-012` | Prefer modular, evolvable boundaries | Responsibilities are cohesive, coupling is explicit, and replacements have bounded blast radius | ADR |
