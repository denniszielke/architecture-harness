# Data Model and Data Platform Behavior

> Status: Draft
> Canonical owner: Data architect - name to be assigned
> Required reviewers: Data owner, security, privacy, integration, engineering, and operations owners
> Gate: G2
> Last reviewed: Not reviewed

## Purpose and boundaries

[State what information the solution must represent, which domains own it, and what this design does not own.]

## Data domains and authority

| Data domain or product | Purpose | Authoritative owner/system | Consumers | Classification | Residency or locality | Retention |
|---|---|---|---|---|---|---|
| [Domain] | [Purpose] | [Owner/system] | [Consumers] | [Class] | [Boundary] | [Rule] |

## Conceptual model

| Entity or aggregate | Identity | Key relationships | Lifecycle | Invariants | Evidence or lineage |
|---|---|---|---|---|---|
| [Entity] | [Stable identifier] | [Relationships] | [States] | [Rules] | [Provenance] |

## Data flow and transformation

| Stage | Input contract | Transformation responsibility | Output contract | Quality checks | Replay or correction |
|---|---|---|---|---|---|
| [Ingest, operational, analytical, serving, archive] | [Contract] | [Component] | [Contract] | [Checks] | [Behavior] |

## Data contract minimum

- Owner, purpose, schema, version, compatibility, identifiers, classification, and permitted use.
- Quality thresholds, freshness, completeness, reconciliation, quarantine, and correction.
- Lineage, source timestamps, processing timestamps, consent or legal-basis references where required.
- Retention, deletion, legal hold, archival, portability, and destruction.
- Access policy, encryption, masking, tokenization, sharing, and export controls.

## Platform behavior

Define logical responsibilities for operational state, lake or warehouse storage, streaming, transformation, semantic serving, search, vector retrieval, graph projection, catalog, governance, and archival. Do not select Fabric, Databricks, or another platform here unless an accepted constraint already governs the choice.

## Open decisions and evidence

| Question | ADR or task | Evidence needed |
|---|---|---|
| [Material store, platform, tenancy, sharing, or lifecycle choice] | `ADR-NNN` | [Experiment, source, constraint] |
