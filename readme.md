# Project Evidence Audit

Reusable skill repository for evidence-first project review, with a dedicated blind-review subagent.

## Directory structure

```text
project-evidence-audit/
├── readme.md
├── SKILL.md
├── agents/
│   └── blind-reviewer.md
└── reference/
    ├── blind-mode-checklist.md
    ├── evidence-rules.md
    ├── output-template.md
    └── rubric.md
```

## Components

- `SKILL.md`: primary workflow and trigger conditions.
- `agents/blind-reviewer.md`: subagent for anonymized blind scoring.
- `reference/`: scoring rubric, output template, and blind mode checklist.

## Supported modes

- Standard evidence-first review.
- Blind review for one project.
- Multi-project double-blind comparison.

## Suggested prompts

- `Use project-evidence-audit to evaluate this repo in blind mode.`
- `Extract a neutral evidence brief, then let @blind-reviewer score it.`
- `Compare three projects in double-blind mode and rank by product maturity.`
