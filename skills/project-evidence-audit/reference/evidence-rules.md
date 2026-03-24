# Project Evidence Audit Rules

This repository provides an evidence-first project review workflow.

## Default operating rule

Always prefer verifiable evidence over project self-description.

Never treat the following as core positive evidence unless independently supported:
- marketing adjectives
- comparative claims such as "best", "leading", or "state of the art"
- prestige cues such as founder reputation, funding, or famous customers mentioned without supporting detail
- branding language and slogans

## Review modes

### 1. Standard review
Use for normal project evaluation when identity cues are acceptable.

### 2. Blind review
Use when the user asks for blind review, neutral review, debiased review, or when promotional framing may distort judgment.

For blind review:
1. Read the original materials.
2. Extract verifiable facts only.
3. Remove brand and subjective cues.
4. Produce a `Neutral Evidence Brief`.
5. Invoke `@blind-reviewer` with only the neutral brief.
6. Present the subagent result as the conclusion.

### 3. Multi-project double-blind comparison
Use when comparing two or more projects fairly.

For double-blind comparison:
1. Build one neutral brief per project.
2. Replace project identities with labels such as `Project A`, `Project B`, `Project C`.
3. Ensure each brief follows the same section order:
   - verified capabilities
   - implementation and technical signals
   - maintenance and activity signals
   - adoption or usage evidence
   - constraints and missing information
   - risks
4. Avoid leaking identity through unique slogans, company names, founder names, funding, or trademark references.
5. Invoke `@blind-reviewer` on the anonymized set.
6. Reveal identity only after the blind comparison is complete.

## Required structure for a Neutral Evidence Brief

Use this structure:

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

## Evidence rules

- Distinguish `Claim`, `Evidence`, and `Inference` whenever ambiguity matters.
- If a point is derived only from self-description, label it as low-confidence or promotional.
- Missing evidence is itself a signal; do not silently fill gaps.
- Prefer code, docs detail, changelogs, issue activity, benchmarks with methodology, and external validation over landing-page copy.

## Files to consult

- Read `reference/rubric.md` when you need scoring criteria.
- Read `reference/output-template.md` when you need output structure.
- Read `reference/blind-mode-checklist.md` when preparing or checking blind-review inputs.
