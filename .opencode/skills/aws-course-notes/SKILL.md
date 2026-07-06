---
name: aws-course-notes
description: "Trigger: AWS course notes, ODT/PDF/transcript inputs, study-note style. Creates source-preserving Markdown AWS notes."
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## Activation Contract

Load this skill when turning AWS course material from ODT, PDF, transcript, or rough notes into project-local Markdown study notes.

## Hard Rules

- Do not invent AWS content, services, features, limits, prices, exam tips, or definitions.
- Preserve every service, component, feature, identity concept, and caveat found in the source.
- Improve wording, headings, casing, structure, and scanability only when meaning stays unchanged.
- Keep uncertain, incomplete, or source-odd notes visible instead of silently deleting them.
- Use safe local extraction commands only; never send course inputs to external services.

## Decision Gates

| Situation | Action |
|---|---|
| Source is ODT | Prefer `pandoc <file>.odt -t gfm`; fallback to local unzip/XML extraction. |
| Source is PDF | Prefer local text extraction; preserve page/section order. |
| Missing or poorly extracted context | Complement gaps only from provided source/context; mark unresolved uncertainty instead of inventing AWS facts. |
| Study-note style needed | Apply the general AWS study-note pattern from `references/note-style.md`; `IA_practitioner/notes/` is an observed style source, not a scope boundary. |
| Term seems wrong but source is ambiguous | Preserve it and add a caveat only if needed. |
| Style conflict | Follow `references/note-style.md`. |

## Execution Steps

1. Extract text locally and save an intermediate artifact outside the repo or in an explicit working path.
2. Apply the general local shape: source metadata, `Criterio de edición`, concise H2/H3 concept chunks, source-derived examples/comparisons, caveats, and final recall or exam keys when applicable.
3. Normalize AWS service casing and obvious typos without changing technical meaning.
4. Add examples, comparisons, and exam-confusion callouts only when directly derived from the source.
5. Verify no AWS facts, services, prices, limits, exam tips, or definitions were added beyond the source.

## Output Contract

Return files changed, extraction method, inferred style, and caveats about preservation or extraction quality.

## References

- `references/note-style.md` — project style for AWS course notes.
- `assets/note-template.md` — starter Markdown shape for future notes.
