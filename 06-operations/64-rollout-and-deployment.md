# Rollout and Deployment

> Status: Draft
> Canonical owner: Release or service owner - name to be assigned
> Required reviewers: Product, architecture, engineering, security, data, support, and business owners
> Gate: G6
> Last reviewed: Not reviewed

This artifact operationalizes the target delivery topology and release design. Architecture owns the target pattern; implementation owns pipeline behavior; this artifact owns rollout waves, operational authorization, migration, communication, and hypercare.

## Rollout units

| Wave | Scope | Entry criteria | Deployment method | Validation | Rollback trigger | Owner |
|---|---|---|---|---|---|---|
| [Pilot/wave/tenant/region/user group] | [Scope] | [Criteria] | [Blue-green/canary/ring/in-place] | [Checks] | [Trigger] | [Role] |

## Readiness per wave

- Environment, quota, license, identity, network, policy, data, backup, support, and training readiness.
- Version and compatibility across infrastructure, application, schema, data, integration, model, prompt, and configuration.
- Change approval, communication, maintenance window, stakeholder, and vendor coordination.
- Pre-deployment backup and rollback or roll-forward validation.
- Health, security, data quality, business outcome, performance, and cost verification.
- Hypercare ownership, exit criteria, and lessons carried into the next wave.

## Migration and coexistence

[Define data migration, reconciliation, dual run, cutover, compatibility, source-of-truth changes, decommissioning, and evidence.]

## Failed rollout

[Define stop authority, containment, rollback, user communication, data correction, incident linkage, and criteria to retry.]
