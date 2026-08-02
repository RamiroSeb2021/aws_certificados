# AWS Course Notes Style

Use this style when converting raw AWS course material into neutral/professional Spanish study notes. The observed `IA_practitioner/notes/` folder is a style source and example, not the boundary of this skill.

## Language

- Write generated explanatory prose in neutral/professional Spanish.
- Assume no prior networking knowledge and only limited systems and cloud knowledge. Use plain language before specialized terminology.
- Expand every acronym on first use with its full English name, a Spanish translation when useful, its meaning, and its purpose in context.
- Keep AWS service names in official casing when clear: `Amazon EC2`, `Amazon S3`, `IAM`, `CloudFront`, `Route 53`, `CloudWatch`, `CloudTrail`, `DynamoDB`, `ElastiCache`, `AWS Organizations`.
- Keep official AWS, service, and ML terms in English/casing when the source uses them: `Amazon Bedrock`, `SageMaker Model Monitor`, `Guardrails`, `RAG`, `Fine-tuning`, `Prompt Engineering`, `foundation models`, `tokens`, `batch`, `serverless`, `data drift`, `n-gramas`.
- Preserve source labels such as `EXAMEN`, `TIP PARA EXAMEN`, warnings, and caveats when they carry study intent.
- Do not use conversational persona slang in generated notes.

## Structure

- One H1 for the course note title.
- H2 for major sections, AWS domains, or source sections.
- H3 for individual services, comparisons, pricing blocks, responsibility model blocks, and short conceptual groups.
- Prefer bullets for facts, capabilities, caveats, responsibilities, and use cases.
- Use tables only for explicit comparisons or compact category matrices already present in the source.
- Introduce prerequisites before concepts that depend on them. For each new technical concept, use this order: definition, why it matters, and an immediate concrete example.

## General AWS Study-Note Pattern

Use this shape for AWS study notes when the source is a PDF, ODT, transcript, rough extraction, or partial course context:

- Start with one H1, then a blockquote metadata block:
  - `Fuente: <source>`.
  - Local extraction/method note and any provided supplemental context.
  - Separate the course source from complementary official AWS sources and link every official source consulted.
  - State that no unsupported content is added and that official complements are clearly identified.
- Put `## Criterio de edición` near the top.
- Common short-note H2s: `Qué es`, `Casos de uso / conceptos`, and final `Claves de repaso` or `Claves de examen` when applicable.
- Longer conceptual notes may use topic-specific H2/H3 sections instead of forcing the short-note shape.
- Use `Error de examen / Punto de confusión` or a close equivalent when the source implies traps, service boundaries, or common confusions.
- Prefer concise bullets; definitions often use `Term: explanation`.
- Introduce source examples as `Ejemplo de la fuente:` or `Caso de la fuente:`.
- Introduce a newly written teaching example as `Ejemplo:` and ensure every detail is supported by the course or an official AWS source.
- Use tables only for compact comparisons already implied by source, especially choose-the-right-service or metric comparisons.
- Preserve caveats with phrases such as `según fuente`, `como aparece en fuente`, and `puede cambiar con el tiempo` for prices or limits.

## Complementing Extraction Gaps

- Use the provided course material as the primary source: neighboring text, pages, sections, screenshots, transcripts, or rough notes.
- Before drafting, consult at least one current official AWS source for the topic when internet access is available, even if the course explanation appears complete.
- When the course omits a prerequisite, is ambiguous, or may be outdated, research current official AWS documentation. Prefer `docs.aws.amazon.com`, then official service pages, FAQs, or AWS-authored articles.
- Label external additions as `Complemento oficial de AWS:` or an equivalent heading and cite the exact URL.
- Do not fill gaps from memory or third-party material. If official verification is unavailable, preserve the fragment and mark it as unresolved.
- If internet access is unavailable, continue from the course source and state that current official verification remains pending.
- If an inferred heading or grouping improves readability, ensure every factual claim remains traceable to the course or a cited official AWS source.

## Recall and Exam Aids

- `Claves de repaso` or `Claves de examen` summarizes distinctions, service mappings, or recall anchors supported by the course or cited official AWS sources.
- Exam-confusion sections must remain traceable to their sources; do not introduce unsupported facts to make a trap more complete.
- If the course hints at a caveat but does not fully explain it, preserve the caveat and add a separately labeled official clarification when available.

## Editing Boundaries

- Correct obvious typos and casing when technical meaning is unchanged.
- Do not add unrelated facts, assumed exam tips, or unsupported details. Any current clarification, limit, or service behavior must come from a cited official AWS source and remain clearly separate from course-derived content.
- Do not remove rough notes, incomplete phrases, or source artifacts that may reflect the learner's intent.
- If a phrase looks factually suspicious, preserve what the course says, verify it officially, and add a clear caveat rather than silently rewriting it.

## Preservation Checklist

- All AWS services, features, identity concepts, architecture concepts, pricing/cost details, caveats, and examples present in the source still appear in the Markdown.
- Source-derived comparisons remain source-derived; tables do not add new dimensions beyond the provided material.
- Unclear extraction artifacts are preserved, clarified from provided context or official AWS documentation, or explicitly marked as uncertain.
- Every acronym is expanded and explained on first use.
- Every newly introduced concept has an immediate concrete example, and every prerequisite appears before concepts that depend on it.
- Every technical claim is traceable to the course or a cited official AWS source.
