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
- Assume the learner has no networking background and only limited systems and cloud knowledge. Define every prerequisite before using it to explain another concept.
- On first use of every acronym, give its full English name, a Spanish translation when useful, its plain-language meaning, and why it matters in context.
- Follow every newly introduced technical concept immediately with a concrete, beginner-friendly example. Do not leave definitions without examples.
- Support every technical claim with either the provided course source or a current official AWS source. Never present model knowledge as sourced fact.
- When internet access is available, consult at least one current official AWS source for the note topic before drafting, even when the course source appears sufficient.
- Treat the course PDF, ODT, transcript, or notes as the primary source. Use official AWS documentation to clarify missing beginner context, verify current behavior, or resolve ambiguity; identify that material as a complement.
- Prefer `docs.aws.amazon.com` and official `aws.amazon.com` service pages, FAQs, or AWS-authored articles. Do not use third-party sources when an official source is available.
- If neither the course source nor an accessible official source supports a claim, omit it or mark it as unresolved. Never fill the gap by guessing.
- Preserve every service, component, feature, identity concept, and caveat found in the source.
- Improve wording, headings, casing, structure, and scanability only when meaning stays unchanged.
- Keep uncertain, incomplete, or source-odd notes visible instead of silently deleting them.
- Use safe local extraction commands only; never send course inputs to external services.

## Decision Gates

| Situation | Action |
|---|---|
| Source is ODT | Prefer `pandoc <file>.odt -t gfm`; fallback to local unzip/XML extraction. |
| Source is PDF | Prefer local text extraction; preserve page/section order. |
| A term depends on an unexplained concept | Insert a short prerequisite definition and immediate example before continuing. |
| An acronym appears | Expand and explain it on first use; do not merely spell it out. |
| Source explains the fact adequately | Preserve it and cite the relevant page, section, or source location. |
| Source lacks beginner context or may be outdated | Research current official AWS sources, cite them, and label the addition as complementary context. |
| Internet access is unavailable | Continue from the course source only and state that current official verification remains pending. |
| Course and current AWS documentation differ | Preserve what the course says, add a clearly labeled current caveat, and never silently merge both claims. |
| Official verification is unavailable | Mark the point as unresolved; do not infer or invent an explanation. |
| Study-note style needed | Apply the general AWS study-note pattern from `references/note-style.md`; `IA_practitioner/notes/` is an observed style source, not a scope boundary. |
| Term seems wrong but source is ambiguous | Preserve it and add a caveat only if needed. |
| Style conflict | Follow `references/note-style.md`. |

## Execution Steps

1. Extract text locally and save an intermediate artifact outside the repo or in an explicit working path.
2. Build a dependency order: explain foundational terms before AWS-specific concepts that depend on them.
3. Research the topic in at least one current official AWS source when internet access is available. Verify each technical statement against the course or official source and record the supporting page, section, or URL.
4. Apply the general local shape: source metadata, `Criterio de edición`, concise H2/H3 concept chunks, caveats, and final recall or exam keys when applicable.
5. For each concept, write in this order: plain-language definition, why it matters, and an immediate concrete example. Expand and explain acronyms on first use.
6. Clearly distinguish course-derived content from official AWS complementary context. Normalize AWS service casing and obvious typos without changing meaning.
7. Audit the finished note: every acronym is explained, every new concept has an example, prerequisites appear before dependent terms, and every technical claim has traceable support.

## Output Contract

Return files changed, extraction method, sources consulted, official URLs used, inferred style, unresolved points, and caveats about preservation or extraction quality.

## References

- `references/note-style.md` — project style for AWS course notes.
- `assets/note-template.md` — starter Markdown shape for future notes.
