# IA Practitioner PDF Renderer

Docker-based renderer for the Markdown notes in `IA_practitioner/notes/`.

From the repository root:

```bash
tools/render-ia-practitioner-pdfs.sh
```

The wrapper builds `aws-certificados/ia-practitioner-pdf-renderer:local` and renders every `*.md` note to `IA_practitioner/rendered-pdfs/`.

The generated PDFs are ignored by Git.
