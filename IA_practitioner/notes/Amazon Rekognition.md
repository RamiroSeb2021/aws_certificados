# Amazon Rekognition

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Qué es

- Servicio para reconocimiento de imágenes y análisis de videos.
- Automatiza y reduce coste de análisis multimedia.
- Integra análisis avanzado de contenido multimedia.
- Escala y se paga según uso.

## Casos de uso

- Verificación de identidad.
- Moderación de contenido.
- Análisis de datos en tiempo real.
- Detección de objetos.
- Detección de texto.
- Etiquetas personalizadas.

## Moderación de contenido

- Detecta contenido inapropiado, no deseado u ofensivo automáticamente.
- Permite adaptadores de moderación personalizados.
- Se entrena con imágenes etiquetadas para mejorar precisión.
- Se adapta a casos específicos.
- Integra con Amazon Augmented AI (A2I) para revisión humana cuando hay dudas.

## Claves de examen

- Rekognition = imágenes/video.
- Para detectar objetos, rostros, texto en imagen, etiquetas o moderación multimedia: Amazon Rekognition.
- Para documentos escaneados con formularios/tablas: Amazon Textract.

### Error de examen / Punto de confusión

- Rekognition sirve para analizar imágenes y video; puede detectar objetos, rostros, etiquetas, texto en imagen o contenido inapropiado.
- Si el foco es comprensión de documentos escaneados, formularios, tablas u OCR documental, Textract suele ser mejor encaje.
- Para leer documentos en voz alta, Rekognition no reemplaza la combinación Textract + Polly.
