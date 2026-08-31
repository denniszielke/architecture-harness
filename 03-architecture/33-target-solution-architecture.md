# Target Solution Architecture

> Status: Draft
> Canonical owner: Solution or enterprise architect - name to be assigned
> Required reviewers: Platform, data, security, engineering, operations, FinOps, and service owners
> Gate: G3
> Last reviewed: Not reviewed

## Architecture context

[State target outcomes, architecture style, inherited constraints, and the boundary between enterprise platforms and project-owned components.]

## Capability-to-product mapping

| Capability or responsibility | Selected product or service | Deployment scope | Owner | Key configuration or tier | Constraint evidence | Governing ADR |
|---|---|---|---|---|---|---|
| `CAP-NNN` | [Selected only after decision] | [Tenant/account/subscription/region/environment] | [Role/team] | [Tier/pattern] | [Source/test] | `ADR-NNN` |

## Candidate cloud families

Evaluate only products relevant to approved requirements. Candidates may include:

- Data and analytics: Microsoft Fabric, Databricks, managed databases, object storage, graph, search, and catalog services.
- Applications: AKS, Azure Container Apps, functions, workflow, managed web platforms, and serverless runtimes.
- Integration: API Management, Event Hubs, Service Bus, event routing, data integration, and managed file exchange.
- Experience: web or mobile applications, Microsoft 365, Copilot, Copilot Studio, Teams, and APIs.
- Identity and security: Microsoft Entra ID, workload identity, managed identities, key and secret management, policy, posture, and threat protection.
- Management: infrastructure as code, CI/CD, observability, security operations, cost management, backup, and recovery.

The list makes the starter Microsoft-cloud-ready; it is not a default architecture. A fork may replace the ecosystem. Compare credible alternatives and current service facts through ADRs.

## Deployment topology

Document:

- Organization, tenant, management group, subscription or account, project, workspace, cluster, namespace, and resource boundaries.
- Development, test, preproduction, production, sandbox, and shared-service separation.
- Regions, zones, network ingress/egress, private access, DNS, service endpoints, firewalls, and hybrid connectivity.
- Human, workload, pipeline, agent, privileged, and emergency identities.
- Data location, encryption, key ownership, backup, restore, replication, retention, and deletion.
- Management, policy, observability, security, deployment, and support planes.

## Component deployment

| Component | Runtime or service | Scale unit | State | Network exposure | Identity | Availability and recovery | Cost driver |
|---|---|---|---|---|---|---|---|
| [Component] | [Service] | [Unit] | [State] | [Boundary] | [Identity] | [Mechanism] | [Driver] |

## Delivery and lifecycle

[Describe infrastructure as code, policy as code, build, artifact provenance, configuration, environment promotion, database/data/model/prompt changes, release, rollback, backup, restore, migration, and retirement.]

## Current-to-target delta

| Current or prototype element | Target treatment | Decision or work item | Risk until resolved |
|---|---|---|---|
| [Element] | Retain, harden, replace, split, migrate, or retire | `ADR/IMP-NNN` | `RISK-NNN` |
