---
name: pdf-course-extraction
description: "Trigger: PDF extraction, entender PDF, procesar PDF, course PDF. Creates controlled local extraction manifests and QA for course PDFs."
license: Apache-2.0
metadata:
  author: "sebastian_rodriguez"
  version: "1.0"
---

## Activation Contract

Load this skill when a course PDF must be understood, extracted, audited, or converted into structured study notes with page traceability.

## Hard Rules

- Use local extraction first; do not send copyrighted course PDFs to external or cloud services unless the user explicitly approves that exact file and service.
- Preserve page order, source wording, caveats, and section boundaries; improve structure only after extraction evidence exists.
- Do not invent content, AWS facts, service limits, exam tips, or missing diagram text.
- Keep page traceability from source PDF to chunks, images, tables, notes, and QA findings.
- Store intermediate artifacts in an explicit working path; never overwrite source PDFs.

## Decision Gates

| Situation | Action |
|---|---|
| PDF has a usable native text layer | Prefer PyMuPDF4LLM `page_chunks` and `write_images` locally. |
| Text is missing, garbled, or scanned | Use local OCR only for affected pages and mark OCR caveats. |
| Tables or diagrams drive meaning | Extract images/tables and require manual review before final notes. |
| User requests Textract, cloud OCR, or external AI | Stop and get explicit approval for file, service, scope, and privacy risk. |
| Coverage or traceability is incomplete | Do not finalize notes; return QA gaps and next review steps. |

## Execution Steps

1. Inspect PDF metadata, page count, text layer quality, diagrams, tables, and copyright sensitivity.
2. Create a manifest from `assets/extraction-manifest.template.yml` with source, artifact roots, extraction profile, sections, and QA gates.
3. Extract page chunks locally; write page images and table/image artifacts when useful.
4. Apply OCR only to pages that need it; label OCR-derived content in artifacts and caveats.
5. Build section notes from traced chunks, following `aws-course-notes` style when producing AWS study notes.
6. Run QA coverage, extraction quality, table/image review, and hallucination/preservation checks using `assets/qa-report.template.md`.
7. Return files changed, manifest path, method, QA result, and caveats.

## Output Contract

Return: files created/modified, source PDF, extraction method, manifest path, artifact root, QA report path, coverage status, manual-review pages, and caveats.

## References

- `assets/extraction-manifest.template.yml` — manifest template for controlled extraction.
- `assets/qa-report.template.md` — QA report template for coverage and preservation checks.
- `references/pdf-extraction-pipeline.md` — recommended local-first PDF extraction pipeline.
