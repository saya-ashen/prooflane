# Scoring Rubric

Use this rubric for standard review, blind review, and double-blind comparison.

## Scoring dimensions

Score each dimension on a 1-5 scale when enough evidence exists.

## Weights

Use these default weights when computing a provisional total:

- Evidence quality: 0.25
- Product maturity: 0.20
- Technical clarity: 0.15
- Maintainability and activity: 0.15
- External validation: 0.15
- Risk transparency: 0.10

### 1. Evidence quality
- **5**: multiple concrete, cross-checkable signals from code, docs, change history, or external validation
- **3**: some concrete support, but uneven depth or coverage
- **1**: mostly self-description with little verifiable support

### 2. Product maturity
- **5**: clearly scoped functionality, operating constraints documented, realistic positioning
- **3**: plausible product shape but incomplete operational details
- **1**: concept-heavy, little evidence of real product readiness

### 3. Technical clarity
- **5**: architecture, interfaces, limitations, and trade-offs are clearly visible
- **3**: partial technical detail with notable gaps
- **1**: mostly vague statements with little implementation substance

### 4. Maintainability and activity
- **5**: visible updates, issue handling, documentation upkeep, and signs of maintainable structure
- **3**: some evidence of maintenance but inconsistent signals
- **1**: stale or unclear maintenance posture

### 5. External validation
- **5**: meaningful third-party usage, evaluation, or external technical review
- **3**: some validation but weak methodology or low coverage
- **1**: claims of adoption without verifiable support

### 6. Risk transparency
- **5**: openly documents limitations, trade-offs, and open problems
- **3**: some caveats present, but incomplete
- **1**: benefits emphasized while trade-offs remain mostly hidden

## Important guidance

- Do not force a score when evidence is thin. Mark the dimension as uncertain.
- Missing evidence should lower confidence, not automatically imply failure.
- In blind review mode, never use identity prestige as a scoring factor.

## Scoring procedure (for reproducibility)

### Step 1: Assign per-dimension scores

- Use 1-5 where evidence is sufficient.
- Mark as `uncertain` where evidence is not sufficient.

### Step 2: Compute weighted mean on scored dimensions

Let `W_scored` be the sum of weights for dimensions with numeric scores.

- If `W_scored` is 0, do not produce a numeric total.
- Else:

`weighted_mean_1_to_5 = sum(weight_i * score_i) / W_scored`

### Step 3: Convert to 0-100 scale

`provisional_total_0_to_100 = ((weighted_mean_1_to_5 - 1) / 4) * 100`

### Step 4: Report evidence coverage

`evidence_coverage = W_scored`

Interpretation:

- `>= 0.85`: broad coverage
- `0.60-0.84`: partial coverage
- `< 0.60`: thin coverage

### Step 5: Confidence calibration

- High confidence: `evidence_coverage >= 0.85` and no critical contamination.
- Medium confidence: `evidence_coverage >= 0.60` and no critical contamination.
- Low confidence: `evidence_coverage < 0.60`, or contamination unresolved, or
  substantial missing sections.
