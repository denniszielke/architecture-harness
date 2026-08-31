# Integration Patterns

> Status: Draft
> Canonical owner: Integration architect - name to be assigned
> Required reviewers: Application, data, security, engineering, operations, and test owners
> Gate: G2
> Last reviewed: Not reviewed

## Integration inventory

| ID | Producer | Consumer | Intent | Interaction style | Contract | Security boundary | SLO |
|---|---|---|---|---|---|---|---|
| `INT-001` | [Producer] | [Consumer] | [Command/query/event/data movement] | [API/event/message/batch/file] | [Link] | [Boundary] | [Target] |

## Pattern selection guide

| Need | Preferred logical pattern | Required behavior |
|---|---|---|
| Immediate validated response | Synchronous API | Authentication, authorization, timeout, idempotency, rate control, versioning |
| State-change notification | Event | Immutable fact, schema version, ordering scope, duplicate handling, replay |
| Reliable work dispatch | Command or queue | Explicit recipient, delivery semantics, retry, dead letter, poison handling |
| High-volume telemetry or stream | Stream | Partitioning, checkpoint, retention, backpressure, late data |
| Large analytical exchange | Batch or data product | Manifest, integrity, reconciliation, lineage, rerun, correction |
| Human or external approval | Workflow handoff | Authority, timeout, escalation, evidence, cancellation |

## Contract requirements

- Purpose, owner, version, compatibility, schema, identity, authorization, and data classification.
- Correlation, causation, timestamps, ordering scope, deduplication key, and idempotency behavior.
- Timeout, retry budget, circuit break, dead letter, replay, reconciliation, and error ownership.
- Observability fields and content-protection rules.
- Consumer migration and deprecation policy.

## Failure scenarios

| Failure | Detection | Safe behavior | Recovery | Evidence |
|---|---|---|---|---|
| Duplicate, delay, outage, invalid schema, unauthorized request, partial commit, or replay | [Signal] | [Behavior] | [Action] | [Trace/test] |

Product mappings such as API Management, Event Hubs, Service Bus, or native platform integration remain architecture decisions.
