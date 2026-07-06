# AWS Course Notes Style

Use this style when converting raw AWS course material into neutral/professional Spanish study notes. The observed `IA_practitioner/notes/` folder is a style source and example, not the boundary of this skill.

## Language

- Write generated explanatory prose in neutral/professional Spanish.
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

## General AWS Study-Note Pattern

Use this shape for AWS study notes when the source is a PDF, ODT, transcript, rough extraction, or partial course context:

- Start with one H1, then a blockquote metadata block:
  - `Fuente: <source>`.
  - Local extraction/method note and any provided supplemental context.
  - `No se agrega contenido AWS nuevo; se preserva significado de fuente.` or an equivalent source-preservation caveat.
- Put `## Criterio de edición` near the top.
- Common short-note H2s: `Qué es`, `Casos de uso / conceptos`, and final `Claves de repaso` or `Claves de examen` when applicable.
- Longer conceptual notes may use topic-specific H2/H3 sections instead of forcing the short-note shape.
- Use `Error de examen / Punto de confusión` or a close equivalent when the source implies traps, service boundaries, or common confusions.
- Prefer concise bullets; definitions often use `Term: explanation`.
- Introduce source examples as `Ejemplo de la fuente:` or `Caso de la fuente:`.
- Use tables only for compact comparisons already implied by source, especially choose-the-right-service or metric comparisons.
- Preserve caveats with phrases such as `según fuente`, `como aparece en fuente`, and `puede cambiar con el tiempo` for prices or limits.

## Complementing Extraction Gaps

- Complement missing or poorly extracted context only from material the user provided: neighboring extracted text, source pages/sections, screenshots, rough notes, or explicit user context.
- Do not fill gaps with general AWS knowledge, current documentation, pricing, limits, service features, or assumed exam facts unless the user explicitly asks for external verification.
- If the provided context is insufficient, keep the fragment visible and qualify it with `extracción incompleta`, `según fuente`, or a final caveat.
- If an inferred heading or grouping improves readability, ensure every factual claim remains traceable to the provided source/context.

## Recall and Exam Aids

- `Claves de repaso` or `Claves de examen` summarizes only source-derived distinctions, service mappings, or recall anchors.
- Exam-confusion sections must clarify boundaries already supported by source; do not introduce new AWS facts to make a trap more complete.
- If the source hints at a caveat but does not fully explain it, keep the caveat visible and qualify it rather than expanding beyond source.

## Editing Boundaries

- Correct obvious typos and casing when technical meaning is unchanged.
- Do not add missing AWS facts, current pricing, updated limits, or official clarifications unless the source says them.
- Do not remove rough notes, incomplete phrases, or source artifacts that may reflect the learner's intent.
- If a phrase looks factually suspicious, preserve it and mention caveat in final response instead of rewriting the concept.

## Preservation Checklist

- All AWS services, features, identity concepts, architecture concepts, pricing/cost details, caveats, and examples present in the source still appear in the Markdown.
- Source-derived comparisons remain source-derived; tables do not add new dimensions beyond the provided material.
- Unclear extraction artifacts are either preserved, clarified from provided context, or explicitly marked as uncertain.
- Final recall/exam keys are omitted when the source does not support them.
