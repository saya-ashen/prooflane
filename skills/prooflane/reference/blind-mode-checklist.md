# Blind Mode Checklist

Use this checklist before sending material to `@blind-reviewer`.

## Remove or neutralize
- project name
- company name
- founder names
- funding mentions
- slogans and taglines
- prestige customer logos without detailed evidence
- explicit superlatives and self-judgments
- ranking claims without methodology

## Preserve
- concrete functionality
- architecture or implementation details
- maintenance signals
- issue / release / changelog evidence
- measurable constraints and trade-offs
- benchmarks with methodology
- pricing and packaging if relevant to buyer analysis

## Contamination check
Ask:
1. Would a reviewer be able to guess the identity from branding or prestige cues alone?
2. Are there subjective adjectives left in the brief?
3. Did any unsupported marketing claim survive the cleaning step?
4. Are all compared projects normalized into the same section order?
5. Is evidence density reasonably balanced across projects?

If contamination remains, revise the brief before handoff.

## Severity and action policy

### Critical contamination (must block handoff)

Any one of the following is enough to block:

- explicit project/company/founder identity
- funding round details as prestige signal
- named customer logo prestige without technical evidence
- unique slogan/tagline that reveals identity

Action:

1. reject handoff
2. rewrite neutral brief
3. re-run checklist before handoff

### Moderate contamination (requires rewrite, then proceed)

- superlative language (`best`, `leading`, `state of the art`)
- unsupported ranking statements
- subjective self-judgment not tied to evidence

Action:

1. rewrite affected sections
2. re-run checklist
3. proceed only if no critical contamination remains

### Normalization gate for multi-project comparisons

If any project has materially higher evidence density than others (for the same
section), rebalance before handoff.
