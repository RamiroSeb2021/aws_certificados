---
name: ai-practitioner-question-search
description: "Trigger: AWS AI Practitioner, AIF-C01, pregunta de examen. Answers by searching IA_practitioner Markdown notes first."
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## Activation Contract

Load this skill when the user asks a study question, exam-style question, comparison, definition, or doubt about AWS Certified AI Practitioner / AIF-C01 using this repo.

## Hard Rules

- Search `IA_practitioner/*.md` before answering; do not rely on memory alone.
- Use `IA_practitioner/AWS-AIF-C01-v4.pdf` only as fallback when Markdown notes do not cover the question.
- Do not invent AWS facts beyond local notes unless the user explicitly asks for current external validation.
- Cite the Markdown files used, and call out when evidence is missing or ambiguous.
- Keep Spanish explanations natural; preserve official AWS service names in English.

## Decision Gates

| Situation | Action |
|---|---|
| User asks about one service | Read that service note plus related notes if comparison is implied. |
| User asks exam-style multiple choice | Search each option, eliminate with evidence, then pick best answer. |
| Question spans responsible AI/security/governance | Include `Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`. |
| Notes conflict with current AWS knowledge | Answer from notes and mark caveat; verify official AWS docs only if requested. |

## Execution Steps

1. Extract keywords: service names, feature names, exam verbs, and answer options.
2. Search `IA_practitioner/*.md` with those keywords; read the most relevant files.
3. Build answer from evidence: direct answer, why, exam trap, and files consulted.
4. If no local evidence exists, say so and suggest which file/source to inspect next.

## Output Contract

Return concise study help: `Respuesta`, `Por qué`, `Trampa de examen` when useful, and `Fuentes` with file paths.

## References

- `references/question-workflow.md` — local lookup heuristics and service map.
