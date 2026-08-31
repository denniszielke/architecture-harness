# Application and AI Experience

> Status: Draft
> Canonical owner: Application or experience architect - name to be assigned
> Required reviewers: Business, security, data, AI risk, engineering, accessibility, and operations owners
> Gate: G2
> Last reviewed: Not reviewed

## User and channel model

| Persona or system actor | Task | Channel | Information allowed | Action authority | Accessibility need |
|---|---|---|---|---|---|
| [Actor] | [Task] | [Web, mobile, Microsoft 365, Copilot, Copilot Studio, API] | [Scope] | [Authority] | [Need] |

## Application responsibilities

[Define interaction, workflow, domain, policy, and data-access boundaries. Keep business rules and authoritative state out of presentation channels unless explicitly owned there.]

## AI or agent use cases

| Use case | Beneficiary | Allowed inputs | Allowed outputs | Prohibited actions | Human control | Deterministic fallback |
|---|---|---|---|---|---|---|
| [Use case] | [Role] | [Data] | [Assistance] | [Boundary] | [Review/approval] | [Fallback] |

## AI lifecycle requirements

- Intended use, risk classification, owner, model and deployment version.
- Prompt, grounding, retrieval, tool, identity, policy, and output versioning.
- Access trimming to the initiating identity and task purpose.
- Offline and online evaluation for quality, safety, security, bias, latency, cost, and fallback.
- Tool allowlists, argument validation, confirmation for consequential actions, and complete traces.
- Content filtering, prompt-injection defense, sensitive-data handling, output labeling, and incident response.
- Promotion, rollback, monitoring, revalidation, and retirement.

## Experience failure paths

Include unavailable model, stale or missing grounding, unsafe output, revoked permission, tool failure, partial workflow state, user correction, escalation, and accessible degraded operation.

Channel and product selections require architecture mapping and, when material, an ADR.
