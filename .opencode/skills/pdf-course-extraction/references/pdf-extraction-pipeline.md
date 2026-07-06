# Local-first PDF extraction pipeline

Use this reference when applying `pdf-course-extraction`. It documents a recommended pipeline, not installed repo dependencies.

## Recommended flow

1. Inspect the PDF locally: page count, metadata, native text quality, tables, images, and diagram density.
2. Create a section manifest from `assets/extraction-manifest.template.yml` before generating notes.
3. Prefer PyMuPDF4LLM page chunks for PDFs with a usable text layer.
4. Enable image writing so diagrams and slide screenshots remain reviewable.
5. Use local OCR only for pages with missing or garbled text; record OCR pages and caveats in the manifest.
6. Build notes section-by-section from traced page chunks.
7. Run QA with `assets/qa-report.template.md` before presenting notes as complete.

## Minimal Python example

This is an example shape only. Do not claim these packages are installed until verified in the active environment.

```python
from pathlib import Path
import pymupdf4llm

source_pdf = Path("path/to/course.pdf")
artifact_root = Path("work/pdf-extraction/course")
image_root = artifact_root / "images"
artifact_root.mkdir(parents=True, exist_ok=True)
image_root.mkdir(parents=True, exist_ok=True)

chunks = pymupdf4llm.to_markdown(
    str(source_pdf),
    page_chunks=True,
    write_images=True,
    image_path=str(image_root),
)

for chunk in chunks:
    page = chunk.get("metadata", {}).get("page", "unknown")
    (artifact_root / f"page-{page}.md").write_text(chunk["text"], encoding="utf-8")
```

## QA gates

- Page coverage: every expected page is extracted, skipped with reason, or assigned manual review.
- Order preservation: notes follow PDF page order unless the manifest explicitly maps a different section order.
- Traceability: every note section cites source page ranges.
- Preservation: ambiguous source text is kept visible; no invented content is added.
- Visual review: diagram-heavy or table-heavy pages are checked against image artifacts before final notes.

## Cloud escalation

Use Textract, cloud OCR, or external AI only after explicit user approval. Approval must name the PDF, service, scope, and privacy/copyright tradeoff.
