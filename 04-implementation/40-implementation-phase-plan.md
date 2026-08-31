# Implementation Phase Plan

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Architecture, security, data, test, operations, and product owners
> Entry gate: G3 - Architecture ready for implementation
> Exit gate: G4 - Implementation evidence accepted
> Last reviewed: Not reviewed

## Purpose

Translate accepted scope, design, architecture, and decisions into a reproducible implementation that produces bounded evidence. Build a thin end-to-end path before expanding layers independently.

## Delivery principles

- Implement high-risk boundaries and uncertain behavior early.
- Make the deterministic path work before optional AI assistance.
- Generate or use approved non-production data unless production-data use is explicitly authorized.
- Automate provisioning, policy, build, tests, deployment, reset, rollback, and evidence capture where practical.
- Treat every shortcut as an owned target-production delta.
- Do not implement around unresolved blocking decisions without a bounded experiment and explicit approval.

## Work packages

| Task ID | Task | Depends on | Output | Complete when | Status | Evidence |
|---|---|---|---|---|---|---|
| `TASK-IMP-01` | Baseline implementation scope and backlog | G3 package | [41-backlog.md](41-backlog.md) | Work traces to accepted scope, design, ADRs, and tests | Not started | Not available |
| `TASK-IMP-02` | Establish environments and guardrails | `TASK-IMP-01` | [42-environment-setup.md](42-environment-setup.md) | Environments are reproducible, isolated, observable, and resettable | Not started | Not available |
| `TASK-IMP-03` | Prove risky assumptions | `TASK-IMP-01`, `TASK-IMP-02` | [43-prototypes.md](43-prototypes.md) | Experiments answer named questions with limitations | Not started | Not available |
| `TASK-IMP-04` | Implement the vertical slice | `TASK-IMP-02`, required `TASK-IMP-03` | Code, data, configuration, and user stories | The accepted journey runs end to end | Not started | Not available |
| `TASK-IMP-05` | Automate release and deployment | `TASK-IMP-02`, `TASK-IMP-04` | [44-release-and-deployment-automation.md](44-release-and-deployment-automation.md) | A reviewed change can be promoted and rolled back reproducibly | Not started | Not available |
| `TASK-IMP-06` | Validate and capture evidence | `TASK-IMP-03`-`TASK-IMP-05` | [47-test-and-validation.md](47-test-and-validation.md), [48-evidence-index.md](48-evidence-index.md) | Independent execution reproduces results and limitations | Not started | Not available |
| `TASK-IMP-07` | Prepare G4 review | `TASK-IMP-01`-`TASK-IMP-06` | Gate recommendation | Demonstrated behavior and remaining production gaps are explicit | Not started | Not available |

## G4 criteria

- A clean environment can be provisioned or initialized from version-controlled artifacts.
- The thin slice executes with versioned code, data, configuration, contracts, and dependencies.
- Security, quality, contract, integration, failure, recovery, performance-smoke, and acceptance tests run automatically where feasible.
- Build and deployment artifacts have provenance, dependency and secret checks, and review controls.
- Measurements include method, environment, data, actual result, and limitation.
- Rollback, reset, data recovery, and teardown are tested at the agreed scope.
- Prototype and production gaps remain visible and owned.

## Input change and replay

| Changed input | Rerun first | Then inspect |
|---|---|---|
| Scope, design, or accepted ADR | `TASK-IMP-01` | Stories, code plan, environments, tests, release |
| Environment, service tier, or policy | `TASK-IMP-02` | Automation, security tests, sizing, runbooks |
| Experiment result rejects an assumption | `TASK-IMP-03` and change-impact process | Design, architecture, ADR, backlog |
| Contract or data model | Affected story and contract tests | Integration, migration, replay, evidence |
| Deployment or supply-chain control | `TASK-IMP-05` | Environment setup, security, operations |
| Acceptance or NFR threshold | `TASK-IMP-06` | Implementation, sizing, gate evidence, claims |

Record changed inputs in the [change impact register](../01-preparation/16-change-impact-register.md). Recheck G4 when executable behavior, test conditions, evidence, or release controls changed.
