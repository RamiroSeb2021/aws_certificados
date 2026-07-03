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

## Computer Vision

- Computer Vision es el campo de IA enfocado en procesar y analizar imágenes o video para extraer información útil.
- Para clasificación visual, detección de objetos o análisis de imágenes médicas/productos/medios, pensar primero en visión por computadora.
- Redes neuronales o CNN son técnicas/modelos que pueden usarse dentro de visión por computadora, pero no son el campo de aplicación.

## Moderación de contenido

- Detecta contenido inapropiado, no deseado u ofensivo automáticamente.
- Permite adaptadores de moderación personalizados.
- Se entrena con imágenes etiquetadas para mejorar precisión.
- Se adapta a casos específicos.
- Integra con Amazon Augmented AI (A2I) para revisión humana cuando hay dudas.

## Entrenamiento con etiquetas personalizadas

- Para entrenar un modelo visual supervisado, los datos deben estar etiquetados según las categorías que se quiere aprender.
- Rekognition Custom Labels se orienta a detectar objetos o escenas específicas con ejemplos etiquetados.
- Si el requisito central es crear etiquetas a gran escala o incorporar retroalimentación humana/RLHF para mejorar datasets, SageMaker Ground Truth suele ser mejor encaje.
- No confundir clasificación visual con Amazon Personalize, Translate o Comprehend: esos servicios no entrenan clasificadores de imagen/video por contenido visual.

## Claves de examen

- Rekognition = imágenes/video.
- Computer Vision = campo para imágenes/video; CNN/red neuronal = técnica posible, no categoría de problema.
- Para detectar objetos, rostros, texto en imagen, etiquetas o moderación multimedia: Amazon Rekognition.
- Para documentos escaneados con formularios/tablas: Amazon Textract.

### Error de examen / Punto de confusión

- Rekognition sirve para analizar imágenes y video; puede detectar objetos, rostros, etiquetas, texto en imagen o contenido inapropiado.
- Si el foco es comprensión de documentos escaneados, formularios, tablas u OCR documental, Textract suele ser mejor encaje.
- Para leer documentos en voz alta, Rekognition no reemplaza la combinación Textract + Polly.
