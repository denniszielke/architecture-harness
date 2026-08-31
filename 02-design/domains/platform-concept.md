# Platform Concept

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Platform, data, security, engineering, operations, and FinOps owners
> Gate: G2
> Last reviewed: Not reviewed

## Platform intent

[Describe the reusable platform capabilities needed by application, data, integration, AI, security, and operations concerns.]

## Logical platform zones

| Zone | Responsibility | Workload types | Data handled | Isolation need | Scaling driver | Owner role |
|---|---|---|---|---|---|---|
| [Experience, API, integration, application, data, AI, management, security, observability] | [Responsibility] | [Workloads] | [Data] | [Boundary] | [Driver] | [Role] |

## Environment model

| Environment | Purpose | Data class | Connectivity | Promotion source | Reset or teardown |
|---|---|---|---|---|---|
| [Development/test/preproduction/production/sandbox] | [Purpose] | [Allowed data] | [Boundary] | [Artifact] | [Method] |

## Platform capabilities

- Identity and policy enforcement.
- Network and private connectivity.
- Application runtime and orchestration.
- Data ingestion, engineering, serving, and governance.
- API, event, message, and workflow mediation.
- AI model, retrieval, agent, tool, prompt, and evaluation lifecycle when in scope.
- Secrets, keys, certificates, configuration, and feature management.
- Build, release, policy, observability, cost, backup, and recovery automation.

## Modularity and extension

[Define shared platform responsibilities, workload-owned responsibilities, extension points, isolation boundaries, versioning, and how one capability can be replaced without uncontrolled change.]

## Candidate product mappings

Microsoft Fabric, Databricks, AKS, Azure Container Apps, API Management, Event Hubs, Service Bus, Microsoft 365, Copilot, Copilot Studio, and Microsoft Entra ID are possible product families. Architecture must compare only credible candidates against the approved requirements and record material choices through ADRs.
