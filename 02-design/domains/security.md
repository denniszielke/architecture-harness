# Security Design

> Status: Draft
> Canonical owner: Security architect - name to be assigned
> Required reviewers: Identity, data, privacy, platform, application, engineering, and operations owners
> Gate: G2, G3, and G6
> Last reviewed: Not reviewed

## Security objectives

- [Confidentiality, integrity, availability, privacy, accountability, safety, and recovery objectives traced to risks and requirements.]

## Trust boundaries and identities

| Boundary | Human identity | Workload or agent identity | Authentication | Authorization | Privileged path |
|---|---|---|---|---|---|
| [Boundary] | [Entra or other identity context] | [Managed/workload identity] | [Mechanism] | [Policy/role/attribute] | [JIT/PIM/break glass] |

## Data protection

| Data class | At rest | In transit | In use | Key ownership | Secret handling | Export control |
|---|---|---|---|---|---|---|
| [Class] | [Control] | [Control] | [Control] | [Owner] | [Method] | [Policy] |

## Threat model

| Threat or abuse case | Asset and boundary | Prevent | Detect | Respond and recover | Residual risk owner |
|---|---|---|---|---|---|
| [Threat] | [Asset/boundary] | [Control] | [Telemetry] | [Action] | [Role] |

Include compromised identity, privilege escalation, data exfiltration, insecure API, supply-chain compromise, malicious or vulnerable dependency, secret leakage, policy bypass, denial of service, unsafe deployment, logging exposure, prompt injection, poisoned grounding, excessive agent permissions, and unauthorized tool action when applicable.

## Secure delivery and operation

- Threat review and security requirements before implementation.
- Infrastructure, identity, policy, application, container, dependency, and secret scanning.
- Signed or attestable artifacts, provenance, SBOM, protected environments, and least-privilege pipelines.
- Central security telemetry with correlation, retention, access protection, alert ownership, and tested response.
- Vulnerability, patch, key, certificate, privileged access, incident, evidence, and exception processes.

## Open security decisions

| Question | Risk | ADR or action | Evidence needed |
|---|---|---|---|
| [Material boundary or control choice] | `RISK-NNN` | `ADR-NNN` | [Threat analysis/test/source] |
