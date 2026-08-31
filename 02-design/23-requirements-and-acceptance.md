# Requirements and Acceptance

> Status: Draft
> Canonical owner: Solution architect - name to be assigned
> Required reviewers: Business, data, security, engineering, operations, and test owners
> Gate: G2
> Last reviewed: Not reviewed

This artifact owns product-independent requirement and quality statements. Architecture maps them to mechanisms; the implementation handoff maps them to planned work, building blocks, tests, and expected evidence.

## Functional and design requirements

| ID | Requirement or invariant | Source | Priority | Acceptance scenario | Owner role | Linked design |
|---|---|---|---|---|---|---|
| `REQ-001` | [Observable product-independent behavior] | `OBJ/SCP-NNN` | [Priority] | [Given/when/then or other check] | [Role] | [Link] |
| `DES-001` | [Required logical boundary, authority, contract, or design invariant] | `VIS/ASM/REQ-NNN` | [Priority] | [Reviewable consequence] | [Role] | [Link] |

## Non-functional requirements

| ID | Quality attribute scenario | Measure | Target or threshold | Conditions and scope | Acceptance method | Owner role |
|---|---|---|---|---|---|---|
| `NFR-001` | [Stimulus, environment, expected response] | [Unit] | [Threshold] | [Population/window/exclusions] | [Test, review, or exercise] | [Role] |

## Requirement rules

- Requirements state observable need, not an implementation product.
- Mandatory constraints remain explicit and cannot be traded away through a weighted score.
- Every requirement links backward to an approved need and forward to design, architecture, implementation context, a planned test, external evidence, or an evidence gap.
- A changed requirement starts impact replay and may require a superseding ADR or gate reassessment.
- Architecture realization belongs in [../03-architecture/35-non-functional-architecture.md](../03-architecture/35-non-functional-architecture.md); test plans belong in the implementation handoff and results remain in downstream evidence stores.
