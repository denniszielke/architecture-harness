# Environment Setup

> Status: Draft
> Canonical owner: Platform engineering lead - name to be assigned
> Required reviewers: Architecture, security, data, engineering, operations, and FinOps owners
> Gate: G4 and G6
> Last reviewed: Not reviewed

## Environment inventory

| Environment | Purpose | Tenant/account/subscription | Region | Data allowed | Connectivity | Deployment source | Owner |
|---|---|---|---|---|---|---|---|
| [Development/test/preproduction/production/sandbox] | [Purpose] | [Boundary] | [Region] | [Classification] | [Network path] | [Pipeline/artifact] | [Role] |

## Bootstrap sequence

1. Validate identity, subscription/account, region, quota, naming, and policy prerequisites.
2. Provision management, network, identity, key, logging, security, data, integration, runtime, and experience resources through approved automation.
3. Apply diagnostic, retention, backup, budget, tagging, policy, and access baselines.
4. Deploy versioned code, configuration, contracts, data, models, prompts, and rules as applicable.
5. Run environment, isolation, policy, security, connectivity, backup, and smoke tests.
6. Produce a configuration inventory and evidence package.

## Guardrails

- Treat Microsoft Entra ID and managed or workload identities as starter candidates pending the project's identity ADR or inherited standard; never embed credentials.
- Separate human, workload, deployment, agent, and emergency identities.
- Deny public or cross-boundary access unless explicitly designed, approved, and tested.
- Keep secrets in an approved secret store and rotate through an owned procedure.
- Apply least-privilege pipeline permissions and protected environment approvals.
- Tag ownership, environment, data class, cost center, and lifecycle.

## Reset, teardown, and recovery

[Document safe reset, data reload, teardown, state preservation, backup, restore, and orphan-resource detection.]

## Validation commands

```text
[Add repository-specific bootstrap, validate, deploy, smoke-test, rollback, and teardown commands.]
```
