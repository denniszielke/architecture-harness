# Release and Deployment Automation

> Status: Draft
> Canonical owner: Platform or release engineering lead - name to be assigned
> Required reviewers: Engineering, security, architecture, test, and operations owners
> Gate: G4 and G6
> Last reviewed: Not reviewed

## Change path

```text
Work item -> reviewed change -> build -> quality/security checks
-> immutable artifact -> environment checks -> deployment
-> verification -> evidence -> promotion or rollback
```

## Pipeline controls

| Stage | Inputs | Automated checks | Approval | Artifact/evidence | Failure action |
|---|---|---|---|---|---|
| [Build/test/deploy/verify/promote] | [Versioned inputs] | [Checks] | [Role or policy] | [Output] | [Stop/rollback] |

## Required automation

- Reproducible builds with pinned dependencies and artifact provenance.
- Unit, contract, integration, migration, security, policy, infrastructure, and acceptance checks.
- Secret, dependency, code, container, infrastructure, and license scanning as applicable.
- Immutable application, infrastructure, data-contract, model, prompt, rule, and configuration versions.
- Environment-specific configuration without source changes.
- Deployment strategy, health verification, rollback, roll-forward, and failed-migration handling.
- Release notes linking scope, commits, artifacts, ADRs, tests, evidence, and known limitations.

## Separation of duties

[Define who may author, review, approve, deploy, operate, and use emergency access. State where automation enforces the separation.]

## Rollback and recovery

[Define compatibility window, state/data migration reversal, feature disablement, prior artifact restoration, and evidence capture.]
