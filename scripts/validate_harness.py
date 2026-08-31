#!/usr/bin/env python3
"""Validate the architecture harness structure and local Markdown links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "architecture-harness.json"

REQUIRED_AGENTS = {
    "Program Orchestrator",
    "Preparation Foundation",
    "Solution Design Partner",
    "Architecture Partner",
    "ADR Proposal Partner",
    "Engineering Manager",
}

EXPECTED_PHASES = {
    "00": ("00-framing", "00-framing/00-framing-plan.md", "G0"),
    "01": ("01-preparation", "01-preparation/10-preparation-plan.md", "G1"),
    "02": ("02-design", "02-design/20-design-phase-plan.md", "G2"),
    "03": ("03-architecture", "03-architecture/30-architecture-phase-plan.md", "G3"),
    "04": ("04-implementation", "04-implementation/40-implementation-phase-plan.md", "G4"),
    "05": ("05-sizing", "05-sizing/50-sizing-plan.md", "G5"),
    "06": ("06-operations", "06-operations/60-operations-plan.md", "G6"),
    "07": ("07-presentation", "07-presentation/70-presentation-plan.md", "G7"),
}

ALLOWED_SKILL_FRONTMATTER = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}

REFERENCE_DEFINITION_RE = re.compile(
    r"^[ \t]{0,3}\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))",
    re.MULTILINE,
)
REFERENCE_USE_RE = re.compile(r"(?<!!)\[([^\]]+)\]\[([^\]]*)\]")
EXTERNAL_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
IDENTIFIER_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d{2,3}\b")
TASK_IDENTIFIER_RE = re.compile(
    r"TASK-(?:FRM|PREP|DES|ARC|IMP|SIZE|OPS|PRES)-\d{2}"
)
TEST_IDENTIFIER_RE = re.compile(r"TEST-(?:IMP|SIZE|OPS)-\d{3}")
ACCEPTED_PLACEHOLDER_RE = re.compile(
    r"\[(?:replace|describe|add|role|owner|name|date|value|scope|link|"
    r"source|target|threshold|purpose|outcome|boundary|question|action)\b"
    r"[^\]\n]*\](?!\s*[\[(])",
    re.IGNORECASE,
)


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def repository_path(relative: str) -> Path | None:
    if not relative or Path(relative).is_absolute():
        return None
    resolved = (ROOT / relative).resolve()
    return resolved if is_within(resolved, ROOT) else None


def has_exact_case(path: Path) -> bool:
    if not path.exists() or not is_within(path, ROOT):
        return False
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        try:
            entries = {entry.name for entry in current.iterdir()}
        except OSError:
            return False
        if part not in entries:
            return False
        current /= part
    return True


def normalize_reference_label(label: str) -> str:
    return " ".join(label.split()).casefold()


def markdown_heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    occurrences: dict[str, int] = {}
    for heading in re.findall(
        r"^[ \t]{0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$",
        path.read_text(encoding="utf-8"),
        re.MULTILINE,
    ):
        plain = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", heading)
        plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain)
        plain = re.sub(r"<[^>]+>", "", plain)
        plain = re.sub(r"[`*_~]", "", plain).strip().casefold()
        slug = re.sub(r"[^\w\- ]", "", plain)
        slug = re.sub(r"\s+", "-", slug)
        index = occurrences.get(slug, 0)
        occurrences[slug] = index + 1
        anchors.add(slug if index == 0 else f"{slug}-{index}")
    return anchors


def frontmatter_value(text: str, key: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    match = re.search(
        rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$",
        text[4:end],
        re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    end = text.find("\n---\n", 4)
    if end == -1:
        return set()
    return set(re.findall(r"^([A-Za-z][A-Za-z0-9-]*):", text[4:end], re.MULTILINE))


def load_manifest(errors: list[str]) -> dict[str, object]:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid architecture-harness.json: {exc}")
        return {}
    if not isinstance(manifest, dict):
        errors.append("architecture-harness.json must contain a JSON object")
        return {}
    return manifest


def validate_required_paths(manifest: dict[str, object], errors: list[str]) -> None:
    required = manifest.get("requiredArtifacts")
    if not isinstance(required, list) or not required:
        errors.append("Manifest must define a non-empty requiredArtifacts list")
        return

    for relative in required:
        if not isinstance(relative, str):
            errors.append("Every requiredArtifacts entry must be a string")
            continue
        path = repository_path(relative)
        if path is None:
            errors.append(f"Required artifact escapes the repository: {relative}")
        elif not path.is_file():
            errors.append(f"Missing required file: {relative}")
        elif not has_exact_case(path):
            errors.append(f"Required artifact has incorrect path casing: {relative}")


def validate_manifest(manifest: dict[str, object], errors: list[str]) -> None:
    phases = manifest.get("phases")
    gates = manifest.get("gates")
    if not isinstance(phases, list):
        errors.append("Manifest phases must be a list")
        return
    if not isinstance(gates, dict) or not gates:
        errors.append("Manifest gates must be a non-empty object")
        return
    expected_gates = {f"G{number}" for number in range(8)}
    if set(gates) != expected_gates:
        errors.append("Manifest must define exactly the gates G0 through G7")
    if [phase.get("id") for phase in phases if isinstance(phase, dict)] != [
        f"{number:02d}" for number in range(8)
    ]:
        errors.append("Manifest must define phases 00 through 07 in order")

    exit_gates: list[str] = []
    for phase in phases:
        if not isinstance(phase, dict):
            errors.append("Every manifest phase must be an object")
            continue
        phase_id = phase.get("id", "?")
        for key in (
            "folder",
            "plan",
            "mayStartAfter",
            "exitGateRequires",
            "exitGate",
        ):
            if key not in phase:
                errors.append(f"Manifest phase {phase_id} is missing {key}")

        folder_value = phase.get("folder")
        plan_value = phase.get("plan")
        expected = EXPECTED_PHASES.get(str(phase_id))
        if expected and (
            folder_value != expected[0]
            or plan_value != expected[1]
            or phase.get("exitGate") != expected[2]
        ):
            errors.append(
                f"Manifest phase {phase_id} must use folder {expected[0]}, "
                f"plan {expected[1]}, and exit gate {expected[2]}"
            )
        folder = repository_path(folder_value) if isinstance(folder_value, str) else None
        plan = repository_path(plan_value) if isinstance(plan_value, str) else None

        if folder is None or not folder.is_dir():
            errors.append(f"Manifest phase {phase_id} folder does not exist: {folder_value}")
        elif not has_exact_case(folder):
            errors.append(f"Manifest phase {phase_id} folder has incorrect casing: {folder_value}")
        if plan is None or not plan.is_file():
            errors.append(f"Manifest phase {phase_id} plan does not exist: {plan_value}")
        elif not has_exact_case(plan):
            errors.append(f"Manifest phase {phase_id} plan has incorrect casing: {plan_value}")
        elif folder is not None and not is_within(plan, folder):
            errors.append(
                f"Manifest phase {phase_id} plan must be inside {folder_value}: {plan_value}"
            )

        exit_gate = phase.get("exitGate")
        if isinstance(exit_gate, str):
            exit_gates.append(exit_gate)
        if exit_gate not in gates:
            errors.append(f"Manifest phase {phase_id} has unknown exit gate: {exit_gate}")

        for key in ("mayStartAfter", "exitGateRequires"):
            dependencies = phase.get(key)
            if not isinstance(dependencies, list):
                errors.append(f"Manifest phase {phase_id} {key} must be a list")
                continue
            unknown = [gate for gate in dependencies if gate not in gates]
            if unknown:
                errors.append(
                    f"Manifest phase {phase_id} {key} has unknown gates: "
                    f"{', '.join(map(str, unknown))}"
                )
                continue
            if len(dependencies) != len(set(dependencies)):
                errors.append(
                    f"Manifest phase {phase_id} {key} contains duplicate gates"
                )
            exit_number = int(str(exit_gate)[1:]) if exit_gate in gates else -1
            invalid_order = [
                gate
                for gate in dependencies
                if isinstance(gate, str)
                and gate.startswith("G")
                and gate[1:].isdigit()
                and int(gate[1:]) >= exit_number
            ]
            if invalid_order:
                errors.append(
                    f"Manifest phase {phase_id} {key} must reference earlier gates: "
                    f"{', '.join(invalid_order)}"
                )
    if len(exit_gates) != len(set(exit_gates)):
        errors.append("Each phase must have a unique exit gate")

    realization_strategies = manifest.get("realizationStrategies")
    expected_strategies = {
        "Buy",
        "Configure",
        "Build",
        "Reuse",
        "Integrate",
        "Retire",
    }
    if not isinstance(realization_strategies, list) or set(realization_strategies) != expected_strategies:
        errors.append(
            "Manifest realizationStrategies must define Buy, Configure, Build, "
            "Reuse, Integrate, and Retire"
        )

    ultimate_delivery = manifest.get("ultimateDelivery")
    if not isinstance(ultimate_delivery, dict):
        errors.append("Manifest must define the ultimateDelivery object")
    else:
        artifact_value = ultimate_delivery.get("artifact")
        artifact = (
            repository_path(artifact_value)
            if isinstance(artifact_value, str)
            else None
        )
        if ultimate_delivery.get("deliverableId") != "DEL-001":
            errors.append("Manifest ultimateDelivery must use DEL-001")
        if ultimate_delivery.get("gate") != "G7":
            errors.append("Manifest ultimateDelivery must use G7")
        if artifact is None or not artifact.is_file():
            errors.append(
                f"Manifest ultimate delivery artifact does not exist: {artifact_value}"
            )
        elif not has_exact_case(artifact):
            errors.append(
                f"Manifest ultimate delivery artifact has incorrect casing: "
                f"{artifact_value}"
            )
        required_artifacts = manifest.get("requiredArtifacts", [])
        if artifact_value not in required_artifacts:
            errors.append(
                "Manifest ultimate delivery artifact must be listed in "
                "requiredArtifacts"
            )


def validate_frontmatter(errors: list[str]) -> None:
    names: set[str] = set()
    for path in sorted((ROOT / ".github/agents").glob("*.agent.md")):
        text = path.read_text(encoding="utf-8")
        name = frontmatter_value(text, "name")
        description = frontmatter_value(text, "description")
        if not name or not description:
            errors.append(f"Agent frontmatter is incomplete: {path.relative_to(ROOT)}")
        elif name in names:
            errors.append(f"Duplicate agent name '{name}': {path.relative_to(ROOT)}")
        else:
            names.add(name)

    missing_agents = REQUIRED_AGENTS - names
    if missing_agents:
        errors.append(f"Missing required agents: {', '.join(sorted(missing_agents))}")

    for path in sorted((ROOT / ".github/skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        name = frontmatter_value(text, "name")
        description = frontmatter_value(text, "description")
        unsupported = frontmatter_keys(text) - ALLOWED_SKILL_FRONTMATTER
        if unsupported:
            errors.append(
                f"Skill has unsupported frontmatter fields "
                f"{', '.join(sorted(unsupported))}: {path.relative_to(ROOT)}"
            )
        if not name or not description:
            errors.append(f"Skill frontmatter is incomplete: {path.relative_to(ROOT)}")
        elif name != path.parent.name:
            errors.append(
                f"Skill name '{name}' must match directory '{path.parent.name}': "
                f"{path.relative_to(ROOT)}"
            )
        elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"Skill name is not portable: {path.relative_to(ROOT)}")
        if description and len(description) > 1024:
            errors.append(f"Skill description exceeds 1024 characters: {path.relative_to(ROOT)}")
        if len(text.splitlines()) > 500:
            errors.append(f"Skill exceeds 500 lines: {path.relative_to(ROOT)}")

    for path in sorted((ROOT / ".github/prompts").glob("*.prompt.md")):
        text = path.read_text(encoding="utf-8")
        if not frontmatter_value(text, "name") or not frontmatter_value(text, "description"):
            errors.append(f"Prompt frontmatter is incomplete: {path.relative_to(ROOT)}")


def validate_controlled_artifacts(
    manifest: dict[str, object], errors: list[str]
) -> None:
    phases = manifest.get("phases", [])
    phase_plans = {
        repository_path(phase["plan"])
        for phase in phases
        if isinstance(phase, dict) and isinstance(phase.get("plan"), str)
    }
    artifact_states = manifest.get("artifactStates", [])
    allowed_artifact_states = (
        set(artifact_states) if isinstance(artifact_states, list) else set()
    )
    allowed_adr_states = {
        "Proposed",
        "Accepted",
        "Rejected",
        "Deferred",
        "Superseded",
    }
    for phase_number in range(8):
        matches = list(ROOT.glob(f"{phase_number:02d}-*"))
        if len(matches) != 1:
            errors.append(f"Expected one folder for phase {phase_number:02d}")
            continue
        folder = matches[0]
        plan_files = [path for path in phase_plans if path and is_within(path, folder)]
        if len(plan_files) != 1:
            errors.append(f"Phase {phase_number:02d} has no phase plan")

        for path in folder.rglob("*.md"):
            relative = path.relative_to(ROOT)
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            status_match = re.search(r"^> Status:\s*(.+?)\s*$", text, re.MULTILINE)
            if not status_match:
                errors.append(f"Controlled artifact has no status header: {relative}")
                continue
            status = status_match.group(1)
            allowed_states = (
                allowed_adr_states
                if "03-architecture/decisions" in relative.as_posix()
                else allowed_artifact_states
            )
            if status not in allowed_states:
                errors.append(f"Controlled artifact has invalid status '{status}': {relative}")
                continue
            if status == "Accepted":
                if ACCEPTED_PLACEHOLDER_RE.search(text):
                    errors.append(f"Accepted artifact contains placeholders: {relative}")
                for marker in (
                    "name to be assigned",
                    "Not available",
                    "Not reviewed",
                    "Not run",
                    "Not decided",
                ):
                    if marker in text:
                        errors.append(
                            f"Accepted artifact contains unresolved marker '{marker}': {relative}"
                        )

        for plan in plan_files:
            text = plan.read_text(encoding="utf-8")
            task_header = next(
                (
                    [cell.strip() for cell in line.strip().strip("|").split("|")]
                    for line in text.splitlines()
                    if line.lstrip().startswith("|") and "Task ID" in line
                ),
                [],
            )
            if "Status" not in task_header or "Evidence" not in task_header:
                errors.append(
                    f"Phase plan task table must track status and evidence: "
                    f"{plan.relative_to(ROOT)}"
                )


def parse_inline_destinations(text: str) -> list[str]:
    destinations: list[str] = []
    cursor = 0
    while True:
        start_marker = text.find("](", cursor)
        if start_marker == -1:
            break
        start = start_marker + 2
        if start < len(text) and text[start] == "<":
            close_angle = text.find(">", start + 1)
            if close_angle == -1:
                cursor = start
                continue
            target = text[start + 1 : close_angle]
            if target:
                destinations.append(target)
            close_parenthesis = text.find(")", close_angle + 1)
            cursor = close_parenthesis + 1 if close_parenthesis != -1 else close_angle + 1
            continue

        depth = 1
        escaped = False
        end = start
        while end < len(text):
            character = text[end]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    break
            end += 1
        if depth != 0:
            cursor = start
            continue

        content = text[start:end].strip()
        if content.startswith("<"):
            close = content.find(">")
            target = content[1:close] if close != -1 else ""
        else:
            target = content.split(None, 1)[0] if content else ""
        if target:
            destinations.append(target.replace("\\(", "(").replace("\\)", ")"))
        cursor = end + 1
    return destinations


def validate_link_target(path: Path, target: str, errors: list[str]) -> None:
    decoded = unquote(target)
    target_path, separator, fragment = decoded.partition("#")
    if EXTERNAL_SCHEME_RE.match(target_path):
        return
    resolved = path if not target_path else (path.parent / target_path).resolve()
    if not is_within(resolved, ROOT):
        errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target_path}")
    elif not resolved.exists():
        errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target_path}")
    elif not has_exact_case(resolved):
        errors.append(
            f"Local link has incorrect path casing: {path.relative_to(ROOT)} -> "
            f"{target_path}"
        )
    elif separator and fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
        if fragment not in markdown_heading_anchors(resolved):
            errors.append(
                f"Broken Markdown anchor: {path.relative_to(ROOT)} -> {target}"
            )


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        definitions = {
            normalize_reference_label(label): angle_target or plain_target
            for label, angle_target, plain_target in REFERENCE_DEFINITION_RE.findall(text)
        }

        for target in parse_inline_destinations(text):
            validate_link_target(path, target, errors)
        for target in definitions.values():
            validate_link_target(path, target, errors)
        for visible_text, label in REFERENCE_USE_RE.findall(text):
            resolved_label = normalize_reference_label(label or visible_text)
            if resolved_label not in definitions:
                errors.append(
                    f"Missing Markdown reference '{label or visible_text}': "
                    f"{path.relative_to(ROOT)}"
                )


def validate_markdown_tables(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        expected_cells: int | None = None
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            if not line.startswith("|"):
                expected_cells = None
                continue
            cells = len(re.split(r"(?<!\\)\|", line.strip().strip("|")))
            if expected_cells is None:
                expected_cells = cells
            elif cells != expected_cells:
                errors.append(
                    f"Markdown table column mismatch: {path.relative_to(ROOT)}:"
                    f"{line_number} expected {expected_cells}, found {cells}"
                )


def validate_identifier_prefixes(
    manifest: dict[str, object], errors: list[str]
) -> None:
    configured = manifest.get("identifierPrefixes")
    if not isinstance(configured, dict) or not configured:
        errors.append("Manifest must define identifierPrefixes")
        return
    prefixes = sorted(
        (prefix for prefix in configured if isinstance(prefix, str)),
        key=len,
        reverse=True,
    )
    for path in ROOT.rglob("*.md"):
        for identifier in IDENTIFIER_RE.findall(path.read_text(encoding="utf-8")):
            if not any(identifier.startswith(f"{prefix}-") for prefix in prefixes):
                errors.append(
                    f"Identifier prefix is not registered: {path.relative_to(ROOT)} -> "
                    f"{identifier}"
                )
            elif identifier.startswith("TASK-") and not TASK_IDENTIFIER_RE.fullmatch(
                identifier
            ):
                errors.append(
                    f"Invalid task namespace: {path.relative_to(ROOT)} -> {identifier}"
                )
            elif identifier.startswith("TEST-") and not TEST_IDENTIFIER_RE.fullmatch(
                identifier
            ):
                errors.append(
                    f"Invalid test namespace: {path.relative_to(ROOT)} -> {identifier}"
                )


def main() -> int:
    errors: list[str] = []
    manifest = load_manifest(errors)
    if manifest:
        validate_required_paths(manifest, errors)
        validate_manifest(manifest, errors)
    validate_frontmatter(errors)
    validate_controlled_artifacts(manifest, errors)
    validate_links(errors)
    validate_markdown_tables(errors)
    if manifest:
        validate_identifier_prefixes(manifest, errors)

    if errors:
        print("Architecture harness validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    markdown_count = len(list(ROOT.rglob("*.md")))
    print(f"Architecture harness validation passed ({markdown_count} Markdown files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
