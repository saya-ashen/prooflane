---
name: prooflane
description: Use when evaluating a project, repository, or product docs with an evidence-first method, especially when blind or double-blind review is needed to reduce branding and prestige bias.
license: MIT
compatibility: opencode
---

# Project Evidence Audit

Use this skill as the entrypoint for project evaluation when you need evidence
over marketing language.

## What this skill does

- Runs standard evidence-first review for a single project.
- Runs blind review by generating a neutral brief and invoking
  `@blind-reviewer`.
- Runs multi-project double-blind comparison with normalized project briefs.

## Required operating rule

Prefer verifiable evidence over self-description.

Treat these as unsupported unless independently validated:

- marketing adjectives and superlatives
- prestige cues (founders, funding, famous logos)
- ranking claims without method
- slogans and brand language

## Workflow

1. Collect source material (repo, docs, product pages, benchmark links).
2. Separate each major point into `Claim`, `Evidence`, and `Inference` where
   needed.
3. Pick review mode:
   - standard review
   - blind review
   - multi-project double-blind comparison
4. If blind mode is requested:
   - create a `Neutral Evidence Brief`
   - remove identity and subjective framing
   - invoke `@blind-reviewer` with only the neutralized brief
5. If multi-project comparison is requested:
   - create one neutral brief per project
   - label as `Project A`, `Project B`, `Project C`
   - normalize section order and evidence density
   - invoke `@blind-reviewer` on anonymized briefs
   - reveal identity only after ranking is complete

## Input-output contract (required)

Before invoking `@blind-reviewer`, prepare input that satisfies
`reference/input-output-contract.md`.

Minimum handoff package per project:

- one `Neutral Evidence Brief` with all required sections
- evidence points structured as `Claim`, `Evidence`, and `Inference` when needed
- source links or source identifiers for each non-trivial evidence point
- contamination status from `reference/blind-mode-checklist.md`

If the package fails contract checks, revise before handoff.

## Handoff and fallback policy

Use this sequence for blind and double-blind runs:

1. Run contamination and contract checks.
2. If failed, revise the brief and re-check (max 2 revisions).
3. If still failed after 2 revisions, return a constrained result with explicit
   `Missing information` and `Risk notes` instead of fabricating certainty.
4. Pass only neutralized, contract-compliant material to `@blind-reviewer`.

Do not convert missing evidence into inferred positives.

## Required neutral brief structure

```md
# Neutral Evidence Brief: Project X

## Verified capabilities

## Technical and implementation signals

## Maintenance and activity signals

## Adoption or external validation

## Constraints and trade-offs

## Missing information

## Risk notes
```

## Files to use

- `reference/rubric.md`
- `reference/output-template.md`
- `reference/blind-mode-checklist.md`
- `reference/evidence-rules.md`
- `reference/input-output-contract.md`
- `reference/examples.md`
