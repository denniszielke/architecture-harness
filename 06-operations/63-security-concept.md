# Operational Security Concept

> Status: Draft
> Canonical owner: Security operations owner - name to be assigned
> Required reviewers: Service, identity, platform, data, engineering, privacy, and incident owners
> Gate: G6
> Last reviewed: Not reviewed

This artifact operationalizes the logical [security design](../02-design/domains/security.md) and target architecture. It does not duplicate their requirements or decisions.

## Security operating model

| Security function | Prevent | Detect | Respond/recover | Owner | Evidence and metric |
|---|---|---|---|---|---|
| Identity, data, network, workload, supply chain, vulnerability, threat, incident, AI, or evidence | [Control] | [Signal] | [Procedure] | [Role] | [Metric/link] |

## Identity operations

- Joiner, mover, leaver; role and entitlement review; PIM/JIT; workload identity lifecycle.
- Break-glass storage, activation, monitoring, testing, and post-use review.
- Secret, key, and certificate issuance, rotation, revocation, expiry, and recovery.
- Agent, tool, and automation identity scopes and action review where applicable.

## Security operations

- Vulnerability intake, prioritization, remediation, exception, and verification.
- Security posture and policy drift detection with owned remediation.
- Threat detection mapped to trust boundaries, assets, and likely abuse cases.
- Incident classification, containment, forensics, evidence preservation, communication, recovery, and learning.
- Dependency, artifact, image, model, prompt, data, and pipeline provenance review.

## Security evidence

| Evidence | Source | Retention | Access | Review frequency | Owner |
|---|---|---|---|---|---|
| [Alert, access review, scan, incident, key rotation, restore, exercise] | [System] | [Period] | [Roles] | [Frequency] | [Role] |

## Residual risk and exceptions

[Link approved exceptions and residual risks. State expiry, compensating control, owner, and revisit trigger.]
