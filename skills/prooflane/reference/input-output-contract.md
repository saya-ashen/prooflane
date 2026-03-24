# Blind Review Input-Output Contract

This contract defines the minimum structure and quality gate for blind review
handoff and expected outputs.

## Input contract (from orchestrating skill to `@blind-reviewer`)

### Required top-level blocks

Each project brief must include:

1. `# Neutral Evidence Brief: Project X`
2. `## Verified capabilities`
3. `## Technical and implementation signals`
4. `## Maintenance and activity signals`
5. `## Adoption or external validation`
6. `## Constraints and trade-offs`
7. `## Missing information`
8. `## Risk notes`

### Required evidence shape

For each material claim (anything that can affect ranking or score), include:

- `Claim`: what is being asserted
- `Evidence`: concrete support from source material
- `Source`: URL, file path, commit, issue, release note, or benchmark reference
- `Inference` (optional): interpretation derived from evidence

If the claim has no concrete support, mark it as weakly supported.

### Normalization requirements for multi-project comparison

- same section order for each project
- similar evidence density (avoid one project having substantially richer detail)
- identity labels only (`Project A`, `Project B`, `Project C`)

### Contamination gate

If critical contamination is present (see `blind-mode-checklist.md`), do not hand
off to `@blind-reviewer` until cleaned.

## Output contract (from `@blind-reviewer`)

### One project

Must include:

- `# Blind Review Result`
- evidence-backed strengths
- evidence-backed risks
- weakly supported positives
- provisional score (with evidence coverage)
- confidence and uncertainty

### Multiple projects

Must include:

- `# Double-Blind Comparison`
- provisional ranking
- explanation for each rank
- major uncertainties
- evidence needed to change ranking

## Failure handling

If input is incomplete or contaminated:

- explicitly label the result as provisional
- list missing or contaminated elements
- lower confidence
- avoid positive inference from unsupported claims
