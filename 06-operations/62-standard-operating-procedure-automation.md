# Standard Operating Procedure Automation

> Status: Draft
> Canonical owner: Operations automation lead - name to be assigned
> Required reviewers: Service, engineering, security, data, and support owners
> Gate: G6
> Last reviewed: Not reviewed

| SOP ID | Procedure | Trigger | Automation level | Approval | Safe checks | Rollback | Evidence | Owner |
|---|---|---|---|---|---|---|---|---|
| `SOP-001` | [Deploy/scale/rotate/restore/onboard/offboard/remediate/collect evidence] | [Trigger] | Manual/Assisted/Automated | [Authority] | [Preconditions] | [Recovery] | [Log/record] | [Role] |

## Automation rules

- Automate deterministic, repeatable steps; preserve explicit approval for consequential actions.
- Make procedures idempotent, bounded, observable, versioned, and safe to retry.
- Validate identity, environment, scope, health, capacity, backup, and change window before action.
- Redact sensitive values and keep immutable action and approval traces.
- Stop and escalate on failed preconditions; do not return success-shaped output.
- Test normal, partial failure, interruption, duplicate execution, rollback, and emergency paths.
- Separate diagnostic access from mutation and use least-privilege workload identities.

## Procedure template

1. Purpose and permitted scope.
2. Trigger and authorization.
3. Preconditions and safety checks.
4. Automated and manual steps.
5. Expected signals and completion criteria.
6. Failure, rollback, and escalation.
7. Evidence and post-action review.
