---
name: aws-course-notes
description: "Trigger: AWS course notes, ODT/PDF course inputs, Cloud Practitioner notes. Creates preserved-content Markdown notes in the project style."
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
| Term seems wrong but source is ambiguous | Preserve it and add a caveat only if needed. |
| Style conflict | Follow `references/note-style.md`. |

## Execution Steps

1. Extract text locally and save an intermediate artifact outside the repo or in an explicit working path.
2. Infer source structure, then write chunked Markdown with clear H1/H2/H3 headings, short lists, and tables only when already implied.
3. Normalize AWS service casing and obvious typos without changing technical meaning.
4. Verify no AWS concepts were added beyond the source.

## Output Contract

Return files changed, extraction method, inferred style, and caveats about preservation or extraction quality.

## References

- `references/note-style.md` — project style for AWS course notes.
- `assets/note-template.md` — starter Markdown shape for future notes.
