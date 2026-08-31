# Environment Setup Plan

> Status: Draft
> Canonical owner: Platform engineering lead - name to be assigned
> Required reviewers: Architecture, security, data, engineering, operations, and FinOps owners
> Gate: G4 and G6
> Last reviewed: Not reviewed

## Environment inventory

| Environment | Purpose | Tenant/account/subscription | Region | Data allowed | Connectivity | Provisioning source | Downstream owner |
|---|---|---|---|---|---|---|---|
| [Development/test/preproduction/production/sandbox] | [Purpose] | [Boundary] | [Region] | [Classification] | [Network path] | [Pipeline/artifact] | [Role] |

## Planned bootstrap sequence

1. Validate identity, subscription or account, region, quota, naming, policy, and landing-zone prerequisites.
2. Provision management, network, identity, key, logging, security, data, integration, runtime, and experience resources through downstream automation.
3. Apply diagnostic, retention, backup, budget, tagging, policy, and access baselines.
4. Deploy versioned code, configuration, contracts, data, models, prompts, and rules as applicable.
5. Run environment, isolation, policy, security, connectivity, backup, and smoke tests.
6. Produce the expected configuration inventory and evidence package.

## Guardrails

- Treat Microsoft Entra ID and managed or workload identities as starter candidates pending the project's identity ADR or inherited standard; never embed credentials.
- Separate human, workload, deployment, agent, and emergency identities.
- Deny public or cross-boundary access unless explicitly designed, approved, and included in the validation plan.
- Keep secrets in an approved secret store and rotate through an owned procedure.
- Apply least-privilege pipeline permissions and protected environment approvals.
- Tag ownership, environment, data class, cost center, and lifecycle.

## Reset, teardown, and recovery

[Document safe reset, data reload, teardown, state preservation, backup, restore, and orphan-resource detection.]

## Downstream execution contract

| Activity | Expected command or automation | Preconditions | Success criteria | Evidence |
|---|---|---|---|---|
| Bootstrap, validate, deploy, smoke test, rollback, teardown | [Defined in downstream repository] | [Identity, policy, quota, input artifacts] | [Observable outcome] | [Required record] |

This harness defines the plan and guardrails. It does not provision or modify cloud environments.
