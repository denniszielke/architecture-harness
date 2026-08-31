# Observability and Key Metrics

> Status: Draft
> Canonical owner: Service owner or observability lead - name to be assigned
> Required reviewers: Business, architecture, security, engineering, operations, test, and FinOps owners
> Gate: G5 and G6
> Last reviewed: Not reviewed

This artifact owns measurable signals and unit metrics. The design and NFR artifacts own required behavior; operations owns alert response and service procedures.

| Metric ID | Signal | Purpose | Source | Dimensions | Target or threshold | Retention | Owner | Action |
|---|---|---|---|---|---|---|---|---|
| `MET-001` | [Metric/log/trace/audit/business event] | [SLO, sizing, security, cost, quality] | [Component] | [Safe dimensions] | [Threshold] | [Period] | [Role] | [Runbook/scale action] |

## Required signal groups

- Business outcome and journey completion.
- Availability, latency, errors, saturation, throughput, queue age, and backlog.
- Data freshness, completeness, quality, lineage, and reconciliation.
- Identity, authorization, privilege, policy, vulnerability, threat, and audit.
- Resource utilization, capacity units, storage, network, tokens, licenses, and unit cost.
- Deployment, configuration, version, feature, model, prompt, and dependency health.
- Recovery, backup, restore, failover, and continuity status.

## Signal protection

Define classification, minimization, redaction, sampling, access, retention, export, correlation, clock synchronization, and incident preservation. Do not put secrets, full sensitive payloads, or unbounded user content in telemetry.

## Service objectives

| SLI | SLO | Window | Error budget | Alerting policy | Owner action |
|---|---|---|---|---|---|
| [Indicator] | [Target] | [Window] | [Budget] | [Burn-rate/threshold] | [Runbook] |
