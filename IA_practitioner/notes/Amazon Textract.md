# Amazon Textract

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Qué es

- Servicio que extrae automáticamente texto, escritura a mano y datos de documentos escaneados.
- Procesa documentos como PDFs e imágenes.

## Casos de uso

- Facturas y reportes financieros.
- Registros médicos y reclamaciones de seguros.
- Formularios de impuestos.
- Documentos de identificación.
- Pasaportes.

## Claves de examen

- Textract = extraer texto/datos de documentos.
- Diferenciar de Rekognition: Rekognition analiza imágenes/video; Textract entiende documentos escaneados.

### Error de examen / Punto de confusión

- Si el escenario pide extraer texto impreso, escritura a mano, formularios o tablas desde documentos/PDF/imágenes, la pieza principal es Textract.
- Para una app que lee contenido en voz alta desde documentos fotografiados: Textract extrae el texto y Polly lo convierte a voz.
