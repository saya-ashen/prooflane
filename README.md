# Project Evidence Audit

Reusable skill repository for evidence-first project review, with a dedicated
blind-review subagent.

## Directory structure

```text
prooflane/
├── README.md
├── agents/
│   └── blind-reviewer.md
└── skills/
    └── prooflane/
        ├── SKILL.md
        └── reference/
            ├── blind-mode-checklist.md
            ├── evidence-rules.md
            ├── examples.md
            ├── input-output-contract.md
            ├── output-template.md
            └── rubric.md
```

## Components

- `skills/prooflane/SKILL.md`: primary workflow and trigger conditions.
- `agents/blind-reviewer.md`: subagent for anonymized blind scoring.
- `skills/prooflane/reference/input-output-contract.md`: handoff schema between
  orchestrator and blind reviewer.
- `skills/prooflane/reference/rubric.md`: weighted and reproducible scoring.
- `skills/prooflane/reference/blind-mode-checklist.md`: contamination severity
  gates and actions.
- `skills/prooflane/reference/examples.md`: minimal examples for each mode.

## Supported modes

- Standard evidence-first review.
- Blind review for one project.
- Multi-project double-blind comparison.

## Suggested prompts

- `Use project-evidence-audit to evaluate this repo in blind mode.`
- `Extract a neutral evidence brief, then let @blind-reviewer score it.`
- `Compare three projects in double-blind mode and rank by product maturity.`
