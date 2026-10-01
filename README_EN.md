# Tu Vi Dau So Research Skill

An open Agent Skill for structured research and interpretation of Vietnamese Zi Wei Dou Shu (Tử Vi Đẩu Số).

It prevents one-star fortune telling by requiring cross-palace analysis, transformations, timing layers, counterevidence, confidence labels, and case validation.

## Capabilities

- Normalize birth and chart data.
- Analyze Life/Body/Bureau and the core chart structure.
- Cross-reference career, finance, marriage, family, relocation, and traditional health tendencies.
- Analyze decade and annual cycles without overriding the natal structure.
- Compare possible birth times using dated life events.
- Compare sources and schools without hiding disagreements.
- Critique readings for vague claims, unsupported certainty, and missing counterevidence.
- Store anonymized validation cases using a JSON Schema.

## Install for Claude Code

```bash
git clone https://github.com/thanhan92-f1/tu-vi-dau-so-research.git
cd tu-vi-dau-so-research
bash scripts/install.sh --scope personal
```

Then invoke:

```text
/tu-vi-dau-so-research Analyze the chart structure and show evidence, counterevidence, conditions, and confidence for every major conclusion.
```

## Scope boundary

This skill studies a traditional interpretive system. It is not scientifically validated forecasting and must not replace medical, legal, financial, or mental-health professionals.

See the Vietnamese [`README.md`](README.md) for full documentation.
