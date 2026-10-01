# AGENTS.md

## Repository purpose

This repository contains one portable Agent Skill: `tu-vi-dau-so-research`.

## Quality rules

- Keep `SKILL.md` below 500 lines when practical.
- Put detailed knowledge in one-level `references/` files.
- Do not add deterministic or harmful fortune-telling claims.
- Every new analytical rule needs source, school, conditions, counterevidence, and tests.
- Preserve Vietnamese terminology and UTF-8 encoding.

## Validation

```bash
python3 scripts/validate_skill.py .
python3 scripts/validate_case.py examples/sample-case.json
python3 -m unittest discover -s tests -v
```

## Versioning

Update `CHANGELOG.md` and the `metadata.version` value in `SKILL.md` together.
