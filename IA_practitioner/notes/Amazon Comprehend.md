# Amazon Comprehend

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Qué es

- Servicio de procesamiento de lenguaje natural (NLP).
- Usa Machine Learning para descubrir información y conexiones valiosas en textos.

## Capacidades principales

- Identificar idioma del texto.
- Extraer información clave: palabras y frases importantes.
- Analizar sentimiento: positivo, negativo o neutro.

### Sentimiento vs otros servicios

- Para feedback de clientes en texto y detección de sentimiento positivo, negativo, neutral o mixto, Amazon Comprehend es la pista directa.
- Amazon Translate traduce idiomas; no interpreta sentimiento como objetivo principal.
- Amazon Textract extrae texto/datos de documentos; no analiza sentimiento por sí mismo.
- Amazon Polly convierte texto en voz; no entiende ni clasifica el texto.
- Amazon Bedrock puede resolver tareas NLP con FM, pero si el examen pide servicio específico de análisis de sentimiento administrado, Comprehend suele ser el encaje más directo.

## Amazon Comprehend Medical

- Servicio NLP para textos clínicos no estructurados.
- Extrae información médica relevante desde notas médicas y resultados de pruebas.
- Guarda resultados en buckets S3.
- Cumple normativas de privacidad permitiendo almacenamiento seguro en S3.

## Casos de uso médicos

- Mejora de documentación clínica.
- Análisis de datos de estudios clínicos.
- Cumplimiento de normativas de privacidad.

## Claves de examen

- Comprehend = entender texto, sentimiento, idioma, entidades/frases.
- Comprehend Medical = NLP para textos clínicos.
- Diferenciar de Translate: no traduce como objetivo principal.
- Diferenciar de Textract/Polly: extraer texto o leerlo en voz alta no equivale a analizar sentimiento.
