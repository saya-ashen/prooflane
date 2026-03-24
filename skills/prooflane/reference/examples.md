# Examples

Minimal examples for each mode.

## 1) Standard evidence-first review (single project)

```md
# Taskflow-Core Review

## Claim / Evidence / Inference highlights
- Claim: Task creation rejects empty titles.
- Evidence: `src/taskflow/service.py` raises `TaskValidationError` on blank
  title.
- Inference: Input validation is explicit and testable.

## Scores
- Evidence quality: 4
- Product maturity: 3
- Technical clarity: 4
- Maintainability and activity: 3
- External validation: uncertain
- Risk transparency: 4
```

## 2) Blind review handoff (single project)

```md
# Neutral Evidence Brief: Project X

## Verified capabilities
- Claim: Supports task create/list/complete/delete.
- Evidence: Service and API modules expose these operations.
- Source: repo files and tests.

## Technical and implementation signals
- Claim: Uses explicit typed interfaces.
- Evidence: type hints and focused service/repository split.
- Source: source files.

## Maintenance and activity signals
- Evidence: test coverage exists for core behavior.

## Adoption or external validation
- No independent validation found in provided material.

## Constraints and trade-offs
- No persistence layer.

## Missing information
- No release process evidence.

## Risk notes
- Limited operational readiness evidence beyond local usage.
```

## 3) Double-blind comparison handoff (multi-project)

```md
# Neutral Evidence Brief: Project A
... (same section order)

# Neutral Evidence Brief: Project B
... (same section order)

# Neutral Evidence Brief: Project C
... (same section order)
```

Checklist for this mode:

- each project uses identical section ordering
- identity labels only (A/B/C)
- evidence density is reasonably balanced
