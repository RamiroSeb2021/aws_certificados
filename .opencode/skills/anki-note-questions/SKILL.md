---
name: anki-note-questions
description: "Trigger: Anki questions, flashcards from notes, preguntas desde apuntes. Creates active-recall cards from study notes."
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## Activation Contract

Load this skill when converting study notes, AWS notes, transcripts, summaries, or course material into Anki-style questions/flashcards.

## Hard Rules

- Do not invent facts beyond the provided notes; preserve the source language and official terminology.
- Make each card test one idea only: short prompt, short answer, fast recall.
- Split long definitions, lists, processes, comparisons, and “wall of text” answers into multiple mini-cards.
- Prefer active recall over recognition: the learner must answer before seeing the answer.
- Use cloze deletion for sequences, formulas, lists, grouped terms, or exact wording worth memorizing.
- Mark uncertain source content as a caveat; never silently “fix” it with outside knowledge.

## Decision Gates

| Source shape | Card strategy |
|---|---|
| Concept or definition | Basic Q/A, plus reverse-angle card when useful. |
| List, process, formula, sequence | Cloze cards; group all blanks or reveal step-by-step intentionally. |
| Comparison table | One card per distinction; avoid asking for the whole table. |
| Diagram/image reference | Add visual prompt or Image Occlusion suggestion. |
| Exam-oriented notes | Favor scenario prompts that still answer from the notes only. |

## Execution Steps

1. Identify atomic facts: concepts, definitions, steps, limits, caveats, examples, and confusions.
2. Convert each fact into mini-cards using `references/question-structure.md`.
3. Add tags from the source topic, exam, section, and card type.
4. Remove duplicate or oversized cards; split anything that requires a paragraph answer.
5. Return cards in a copy/paste table or CSV-ready shape from `assets/anki-csv-template.md`.

## Output Contract

Return generated cards with columns: `Front`, `Back`, `Type`, `Tags`, and optional `Caveat`. Include a brief count by card type.

## References

- `references/question-structure.md` — card structure rules derived from `anki_tuto.txt`.
- `assets/anki-csv-template.md` — CSV-ready output format for Anki import.
