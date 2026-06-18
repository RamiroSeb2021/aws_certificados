# Repository Guidelines

## Qué es este repo

- Repositorio personal de apuntes para certificaciones AWS.
- Dominio actual: documentación de estudio para Cloud Practitioner y AI Practitioner.
- No es una aplicación, API, librería ni infraestructura desplegable.

## Realidad verificada del repo

- `IA_practitioner/` contiene PDF fuente y apuntes Markdown separados por tema de AWS AI Practitioner.
- `cloud_practitioner/` contiene ODT fuente y un Markdown consolidado del curso Cloud Practitioner.
- `.opencode/skills/aws-course-notes/` contiene skill local para convertir material AWS a apuntes Markdown.
- No hay comandos de build/test verificados para producto ejecutable.

**Documentado ≠ implementado**: si algún apunte describe servicios AWS, arquitecturas o flujos, eso es contenido de estudio, no implementación en este repo.

## Fuentes de verdad

| Tema | Fuente |
|---|---|
| Overview humano | `README.md` |
| Reglas para agentes | `AGENTS.md` |
| Estilo de apuntes AWS | `.opencode/skills/aws-course-notes/references/note-style.md` |
| AI Practitioner fuente | `IA_practitioner/AWS-AIF-C01-v4.pdf` |
| Cloud Practitioner fuente | `cloud_practitioner/Notas curso Cloud Practitioner CFL-CO2 2026.odt` |

## Mapa del repo

```text
IA_practitioner/      Apuntes y fuente PDF de AWS Certified AI Practitioner
cloud_practitioner/   Apuntes y fuente ODT de AWS Certified Cloud Practitioner
.opencode/skills/     Skills locales usadas para generar/normalizar apuntes
README.md             Introducción y orden de lectura
AGENTS.md             Instrucciones operativas para agentes
```

## Reglas para asistentes

- Verificar árbol real antes de afirmar que existe archivo, script, comando o carpeta.
- Tratar este repo como documentación; no inventar comandos de ejecución.
- Preservar idioma español con términos AWS oficiales en inglés cuando la fuente los use.
- No agregar contenido AWS nuevo a apuntes derivados si el usuario pidió basarse en curso fuente.
- Si algo parece desactualizado o raro en fuente, conservarlo y marcar caveat; no corregir con conocimiento externo salvo pedido explícito.
- No borrar fuentes originales (`.pdf`, `.odt`) sin aprobación explícita.
- No hacer commit, push, limpieza masiva ni operaciones destructivas sin pedido explícito.

## Skills locales

| Skill | Cuándo usar | Ruta |
|---|---|---|
| `aws-course-notes` | Convertir PDFs/ODT/transcripts AWS a apuntes Markdown | `.opencode/skills/aws-course-notes/SKILL.md` |
| `anki-note-questions` | Crear preguntas Anki/flashcards desde apuntes respetando estructura de repaso activo | `.opencode/skills/anki-note-questions/SKILL.md` |
| `create-readme` | Crear o actualizar `README.md` | global skill |
| `create-agents-md` | Crear o actualizar `AGENTS.md` | global skill |
| `cognitive-doc-design` | Mejorar documentación para lectura rápida | global skill |

## Auto-invoke obligatorio

- Para apuntes AWS desde curso local: cargar `aws-course-notes` primero.
- Para preguntas Anki desde apuntes: cargar `anki-note-questions` primero.
- Para README: cargar `create-readme` y aplicar diseño cognitivo.
- Para AGENTS.md: cargar `create-agents-md`.

## Comandos seguros verificados

```bash
git status --short
git diff -- '*.md'
```

## Comandos situacionales

```bash
# Usar solo si hace falta inspeccionar archivos versionados
git ls-files
```

## Gotchas

- AI Practitioner agrupa `Amazon Lex & Connect` como un solo tema en el curso; mantener un solo archivo `IA_practitioner/Amazon Lex & Connect.md`.
- Los apuntes de AI Practitioner fueron generados desde PDF y separados por tema; mantener consistencia de encabezado y criterio de edición.
- El curso PDF incluye aviso de derechos de autor y uso personal; no publicar ni redistribuir material fuente.
- Precios, límites y nombres de servicios AWS pueden cambiar; si el usuario necesita exactitud actual, verificar documentación oficial.
