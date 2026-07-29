# Informe QA de extracción PDF

## Fuente

- PDF: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
- Manifiesto: `Solutions Architect Associate/notes-lecturas/_metadata/extraction-manifest.yml`
- Artefactos temporales: `/tmp/saa-render`
- Método: `pdftotext -layout` + renderizado Poppler y revisión visual
- Fecha: 2026-07-28

## Cobertura

- PDF total: 880 páginas.
- Alcance revisado: páginas 57, 79–92, 94–117, 119–192 y 194–200.
- OCR requerido: ninguno.
- Páginas omitidas: demos y lecturas no solicitadas.

## Calidad

- Capa de texto: buena.
- Orden y límites de sección: verificados contra `course-content.md` e `indice-lecturas.md`.
- Diagramas revisados: placement groups, ENI, hibernación, ALB/NLB/GWLB, TLS/SNI, ASG, RDS Multi-AZ, Aurora, ElastiCache y DNS.

## Preservación

- [x] Cada nota identifica páginas fuente.
- [x] Los nombres AWS se normalizaron sin cambiar significado.
- [x] Las cifras del PDF se conservaron como datos de la fuente.
- [x] No se publicó la extracción completa del PDF.
- [x] El complemento externo se limita al archivo de puertos y queda identificado.

## Caveats

- El PDF contiene límites y valores que pueden quedar desactualizados.
- La lectura de puertos no está desarrollada como diapositiva en la sección 9; se complementó con la diapositiva 57 y documentación oficial AWS.
- Los archivos existentes de `notes/` se conservaron sin modificación.
