---
name: udemy-wrong-questions
description: "Trigger: Udemy wrong questions, exam screenshots, preguntas incorrectas. Builds focused AWS AI Practitioner study repairs."
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## Activation Contract

Load this skill when the user provides AWS AI Practitioner wrong exam questions as text, screenshots, or a folder of captures and wants study notes repaired or extended.

## Hard Rules

- Use `IA_practitioner/AWS-AIF-C01-v4.pdf` and `IA_practitioner/notes/` as source material before adding any concept.
- Do not preserve full proprietary Udemy question text unless the user owns/provides it for personal study; summarize the tested concept instead.
- Do not invent exam facts. If the PDF/notes do not support the concept, mark the addition as “Complemento pendiente de verificar” unless the user explicitly asks for official AWS docs.
- Follow the note style in `../aws-course-notes/references/note-style.md` for any Markdown edits.
- Keep one note per aligned topic; create a new `.md` only when no existing note category fits.

## Decision Gates

| Situation | Action |
|---|---|
| Screenshots attached | Extract question, answers, selected/wrong choice, correct choice, and explanation if visible. |
| Folder path provided | Inspect supported image files in stable order and process each capture. |
| Concept exists in notes | Add a concise “Error de examen / Punto de confusión” section to that note. |
| Concept absent but category exists | Add a short conceptual subsection to the closest note. |
| No aligned category | Create `IA_practitioner/notes/<Tema>.md` using the existing note style. |

## Execution Steps

1. Build a wrong-question inventory: topic, confused concept, why the selected answer fails, why the correct answer fits.
2. Search existing `IA_practitioner/notes/*.md` for each concept and map it to the best note before editing.
3. Cross-check against the PDF/source notes; preserve source wording when possible and add caveats for unsupported details.
4. Update or create Markdown notes with exam-focused conceptual repairs, not raw question dumps.
5. Produce a concise study plan grouped by weak concept, with priority, what to reread, and one active-recall prompt per topic.

## Output Contract

Return changed files, question-to-note mapping, unsupported/caveated items, and a concise conceptual study plan ordered by priority.

## References

- `../aws-course-notes/references/note-style.md` — project Markdown style for AWS course notes.
