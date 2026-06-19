# AWS Certificados

Repositorio personal de apuntes de estudio para certificaciones AWS. Contiene material convertido a Markdown desde cursos locales, con foco en lectura rápida, repaso y preparación de examen.

## Estado actual

- Apuntes de **AWS Certified Cloud Practitioner (CLF-C02)** en `cloud_practitioner/`.
- Apuntes de **AWS Certified AI Practitioner (AIF-C01)** en `IA_practitioner/notes/`.
- No hay aplicación ejecutable ni scripts de build verificados; este repo es principalmente documentación.

## Estructura

```text
.
├── IA_practitioner/
│   ├── AWS-AIF-C01-v4.pdf
│   ├── anki/
│   ├── notes/
│   │   ├── Amazon Bedrock.md
│   │   ├── Amazon Q.md
│   │   ├── Amazon SageMaker.md
│   │   └── ...
│   └── rendered-pdfs/      # generado e ignorado por Git
├── cloud_practitioner/
│   ├── Notas curso Cloud Practitioner CFL-CO2 2026.odt
│   └── notas_curso_cloud_practitioner_cfl-c02_2026.md
├── AGENTS.md
└── README.md
```

## Ruta sugerida: AI Practitioner

Orden basado en el curso `IA_practitioner/AWS-AIF-C01-v4.pdf`:

1. `IA_practitioner/notes/Amazon Translate.md`
2. `IA_practitioner/notes/Amazon Comprehend.md`
3. `IA_practitioner/notes/Amazon Transcribe.md`
4. `IA_practitioner/notes/Amazon Polly.md`
5. `IA_practitioner/notes/Amazon Rekognition.md`
6. `IA_practitioner/notes/Amazon Textract.md`
7. `IA_practitioner/notes/Amazon Kendra.md`
8. `IA_practitioner/notes/Amazon Lex & Connect.md`
9. `IA_practitioner/notes/Amazon Personalize.md`
10. `IA_practitioner/notes/Amazon Bedrock.md`
11. `IA_practitioner/notes/Fundamentos de Prompt Engineering.md`
12. `IA_practitioner/notes/Amazon Q.md`
13. `IA_practitioner/notes/Amazon SageMaker.md`
14. `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`

Para regenerar los PDFs de estos apuntes desde Docker:

```bash
tools/render-ia-practitioner-pdfs.sh
```

Los PDFs se generan en `IA_practitioner/rendered-pdfs/` y no se versionan.

## Ruta sugerida: Cloud Practitioner

- Leer `cloud_practitioner/notas_curso_cloud_practitioner_cfl-c02_2026.md` de arriba hacia abajo.
- El archivo preserva el orden y contenido del curso original convertido desde ODT.

## Criterio de edición de apuntes

- Se preserva significado del material fuente.
- Se mejora estructura, headings, casing y legibilidad.
- No se agregan servicios, precios, límites o features que no estén en la fuente.
- Precios, límites y nombres pueden cambiar con el tiempo; revisar documentación oficial AWS antes del examen.

## Fuentes locales

- `IA_practitioner/AWS-AIF-C01-v4.pdf`
- `cloud_practitioner/Notas curso Cloud Practitioner CFL-CO2 2026.odt`

> Nota: el PDF del curso indica restricciones de uso personal. No compartas material protegido fuera de tu uso autorizado.
