# Code Generation Plan

> Status: Draft
> Canonical owner: Engineering lead - name to be assigned
> Required reviewers: Architecture, security, platform, data, test, and repository owners
> Gate: G4
> Last reviewed: Not reviewed

## Purpose

Define how humans and coding agents create implementation artifacts without bypassing architecture, security, review, or evidence controls.

## Generation units

| Unit | Source specification | Target location | Generator or agent | Required review | Tests | Regeneration rule |
|---|---|---|---|---|---|---|
| [API, schema, infrastructure, pipeline, component, test, runbook] | [Canonical link] | [Path] | [Tool/agent] | [Owner] | [Checks] | [Overwrite/merge/never regenerate] |

## Guardrails

- Generate from accepted requirements, contracts, and ADRs or from an explicitly bounded experiment.
- Reuse repository patterns and shared components before adding new abstractions.
- Never place credentials, personal data, proprietary examples, or unapproved endpoints in prompts or generated files.
- Require human review for security boundaries, identity, authorization, data handling, infrastructure, destructive actions, and consequential AI tools.
- Pin and scan dependencies; do not add a dependency when the platform or standard library already meets the need.
- Keep generated code small, typed, testable, observable, and replaceable.
- Record tool/model version when generation materially affects provenance or assurance.
- Treat generated tests as implementation artifacts that still require independent acceptance criteria.

## Prompt inputs

[List the minimum context an agent receives: task ID, canonical requirements, interfaces, constraints, existing patterns, acceptance tests, target paths, prohibited changes, and validation commands.]

## Review and evidence

[Define pull-request checks, code ownership, threat-sensitive review, test evidence, artifact provenance, and how rejected generation is corrected.]
