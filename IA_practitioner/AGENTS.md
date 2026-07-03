# IA Practitioner — Agent Guidelines

## Qué es esta carpeta

- Apuntes de estudio para **AWS Certified AI Practitioner (AIF-C01)**.
- Fuente local principal: `AWS-AIF-C01-v4.pdf`.
- Los Markdown son notas derivadas del PDF, separadas por servicio o tema.
- Esto es documentación de estudio, no implementación ni laboratorio ejecutable.

## Fuentes de verdad

| Tema | Fuente |
|---|---|
| Curso fuente | `AWS-AIF-C01-v4.pdf` |
| Estilo de apuntes AWS | `../.opencode/skills/aws-course-notes/references/note-style.md` |
| Preguntas de estudio AIF-C01 | `../.opencode/skills/ai-practitioner-question-search/SKILL.md` |
| Reglas globales repo | `../AGENTS.md` |

## Uso obligatorio de skills

- Para responder preguntas de estudio o examen sobre AIF-C01, cargar `ai-practitioner-question-search`.
- Para crear o normalizar apuntes desde el PDF, cargar `aws-course-notes`.
- No contestar preguntas técnicas desde memoria solamente: buscar primero en `*.md` relacionados.

## Reglas para responder preguntas

- Buscar evidencia en Markdown locales antes de responder.
- Citar archivos usados en sección `Fuentes`.
- Si falta evidencia local, decirlo explícitamente y sugerir revisar PDF o documentación oficial AWS.
- No agregar facts AWS nuevos si el usuario pidió basarse en el curso local.
- Si la fuente parece desactualizada, conservar criterio de fuente y marcar caveat.
- Mantener español natural con nombres oficiales AWS en inglés.

## Mapa rápido de temas

| Pregunta sobre | Archivo probable |
|---|---|
| Traducción | `Amazon Translate.md` |
| NLP, entidades, sentimiento | `Amazon Comprehend.md` |
| Voz a texto | `Amazon Transcribe.md` |
| Texto a voz | `Amazon Polly.md` |
| Imagen/video | `Amazon Rekognition.md` |
| Documentos, formularios, tablas | `Amazon Textract.md` |
| Búsqueda empresarial | `Amazon Kendra.md` |
| Chatbots/contact center | `Amazon Lex & Connect.md` |
| Recomendaciones | `Amazon Personalize.md` |
| GenAI, FM, RAG, guardrails, agentes | `Amazon Bedrock.md` |
| Prompt engineering | `Fundamentos de Prompt Engineering.md` |
| Asistente empresarial/desarrollo | `Amazon Q.md` |
| ML, entrenamiento, MLOps, Clarify, Model Monitor | `Amazon SageMaker.md` |
| IA responsable, cumplimiento, seguridad | `Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md` |

## Formato sugerido para respuestas de estudio

```markdown
Respuesta: <respuesta directa>

Por qué:
- <evidencia breve>
- <comparación o descarte si aplica>

Trampa de examen: <confusión típica si aplica>

Fuentes:
- `IA_practitioner/<archivo>.md`
```

## Comandos seguros verificados

```bash
git status --short
git diff -- '*.md'
```

## Gotchas

- `Amazon Lex & Connect.md` agrupa Lex y Connect como un solo tema porque así quedó el curso.
- Precios, límites y nombres de servicios pueden cambiar; verificar documentación oficial AWS si el usuario pide exactitud actual.
- No borrar ni modificar `AWS-AIF-C01-v4.pdf` sin aprobación explícita.
