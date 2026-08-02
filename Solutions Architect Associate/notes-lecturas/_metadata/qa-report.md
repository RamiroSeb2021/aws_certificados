# Informe de aseguramiento de calidad (QA) de extracción del documento PDF

## Fuente

- PDF — Portable Document Format (formato de documento portátil): `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
- Manifiesto: `Solutions Architect Associate/notes-lecturas/_metadata/extraction-manifest.yml`
- Artefactos temporales: `/tmp/saa-render`
- Método: `pdftotext -layout` + renderizado Poppler y revisión visual
- Fecha de extracción inicial: 2026-07-28
- Fecha de revisión pedagógica y oficial: 2026-08-01

## Cobertura

- Documento fuente total: 880 páginas.
- Alcance revisado: páginas 57, 79–92, 94–117, 119–192 y 194–200.
- OCR — Optical Character Recognition (reconocimiento óptico de caracteres) requerido: ninguno.
- Páginas omitidas: demos y lecturas no solicitadas.

## Calidad

- Capa de texto: buena.
- Orden y límites de sección: verificados contra `course-content.md` e `indice-lecturas.md`.
- Diagramas revisados: placement groups, ENI, hibernación, ALB/NLB/GWLB, TLS/SNI, ASG, RDS Multi-AZ, Aurora, ElastiCache y DNS.

## Preservación

- [x] Cada nota identifica páginas fuente.
- [x] Los nombres AWS se normalizaron sin cambiar significado.
- [x] Las cifras del documento fuente se conservaron como datos del curso.
- [x] No se publicó la extracción completa del documento fuente.
- [x] Las 37 notas incluyen al menos una fuente oficial actual de AWS.
- [x] Cada nota desarrolla los conceptos fundamentales antes del detalle técnico.
- [x] Cada sigla conceptual se desarrolla o se identifica explícitamente como código o nombre reservado.
- [x] Cada concepto nuevo del bloque introductorio incluye un ejemplo inmediato.
- [x] Los complementos oficiales y las diferencias respecto al curso quedan identificados.

## Caveats

- El documento fuente contiene límites y valores que pueden quedar desactualizados; se conservaron como material del curso y se añadieron advertencias donde la documentación actual difiere.
- La lectura de puertos no está desarrollada como diapositiva en la sección 9; se complementó con la diapositiva 57 y documentación oficial de AWS.
- Las fuentes oficiales pueden cambiar después de esta revisión; para una decisión operativa deben consultarse nuevamente los enlaces de cada lectura.
