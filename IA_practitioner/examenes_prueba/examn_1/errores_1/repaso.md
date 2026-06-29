# Repaso de errores - Examen de práctica 1

> Fuente de análisis: capturas locales en `preguntas/` y `feedback/`.
> No se conserva el texto completo propietario de las preguntas; se resume el concepto evaluado.

## Fundamentos de IA Generativa

### Riesgos específicos de GenAI

- **Pregunta 15** (`preguntas/pregunta_1.png`, `feedback/feedback_1.png`)
- Concepto evaluado: desafíos característicos de GenAI.
- Selección incorrecta visible: privacidad y seguridad; explicabilidad y transparencia.
- Respuesta correcta visible: propiedad intelectual, toxicidad y alucinaciones.
- Punto de confusión: privacidad, seguridad, explicabilidad y transparencia son dimensiones relevantes de IA responsable, pero el examen pedía desafíos especialmente asociados a salidas generativas.
- Nota reforzada: `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`.

### Ajuste de modelos preentrenados

- **Pregunta 33** (`preguntas/pregunta_5.png`, `feedback/feedback_5.png`)
- Concepto evaluado: adaptar un LLM preentrenado a descripciones de productos existentes.
- Selección incorrecta visible: instruction-based fine-tuning.
- Respuesta correcta visible: domain adaptation fine-tuning.
- Punto de confusión: si la pista es estilo/dominio/dataset propio, conviene domain adaptation; si la pista es seguir instrucciones o formatos, conviene instruction-based.
- Nota reforzada: `IA_practitioner/notes/Ajuste de modelos GenAI.md`.

### Sesgo, varianza y generalización

- **Pregunta 63** (`preguntas/pregunta_12.png`, `feedback/feedback_12.png`)
- Concepto evaluado: buen rendimiento en entrenamiento y mal rendimiento en prueba.
- Selección incorrecta visible: aumento de sesgo y menor varianza.
- Respuesta correcta visible: bajo sesgo pero mayor variabilidad.
- Punto de confusión: rendir bien en entrenamiento pero mal en prueba apunta a overfitting: el modelo aprendió demasiado el set de entrenamiento y generaliza mal.
- Nota reforzada: `IA_practitioner/notes/Ajuste de modelos GenAI.md`.

## Fundamentos de IA y ML

### Latencia de inferencia

- **Pregunta 22** (`preguntas/pregunta_2.png`, `feedback/feedback_2.png`)
- Concepto evaluado: factores que afectan directamente la latencia.
- Selección incorrecta visible: configuración de parámetros de inferencia; complejidad de arquitectura.
- Respuesta correcta visible: longitud de la secuencia de entrada y longitud de la salida generada.
- Punto de confusión: temperatura, Top P y Top K cambian comportamiento/aleatoriedad, pero la fuente remarca que la latencia depende sobre todo de modelo y tokens procesados/generados.
- Nota reforzada: `IA_practitioner/notes/Métricas de evaluación e inferencia.md`.

## Aplicaciones de modelos fundacionales

### Bases vectoriales y búsqueda por similitud

- **Pregunta 23** (`preguntas/pregunta_3.png`, `feedback/feedback_3.1.png`, `feedback/feedback_3.2.png`, `feedback/feedback_3.3.png`)
- Concepto evaluado: servicios adecuados para búsqueda por vectores/similitud en recomendaciones.
- Selección correcta visible: DocumentDB y OpenSearch; faltó Neptune ML.
- Respuesta correcta visible: Amazon Neptune ML, Amazon DocumentDB y Amazon OpenSearch Service.
- Punto de confusión: S3, QuickSight y Redshift no son el encaje directo para búsqueda vectorial eficiente.
- Caveat: el PDF fuente menciona OpenSearch, DocumentDB y Neptune como bases de vectores/RAG; el feedback usa `Neptune ML`, detalle que no queda igual de explícito en la fuente local.
- Nota reforzada: `IA_practitioner/notes/Amazon Bedrock.md`.

### Tipos de inferencia

- **Pregunta 30** (`preguntas/pregunta_4.png`, `feedback/feedback_4.1.png`, `feedback/feedback_4.2.png`)
- Concepto evaluado: procesamiento offline de grandes lotes.
- Selección incorrecta visible: inferencia serverless.
- Respuesta correcta visible: inferencia por lotes.
- Punto de confusión: serverless reduce gestión operativa; batch/lotes es la pista para grandes volúmenes offline sin respuesta inmediata.
- Nota reforzada: `IA_practitioner/notes/Métricas de evaluación e inferencia.md`.

### Bedrock vs SageMaker JumpStart

- **Pregunta 34** (`preguntas/pregunta_6.png`, `feedback/feedback_6.1.png`, `feedback/feedback_6.2.png`)
- Concepto evaluado: generación de imágenes con FM administrados sin entrenar/alojar modelos.
- Selección incorrecta visible: Amazon SageMaker JumpStart.
- Respuesta correcta visible: Amazon Bedrock.
- Punto de confusión: Bedrock es API administrada para consumir FM; JumpStart ayuda a desplegar modelos preconfigurados, pero puede requerir endpoint/gestión en SageMaker.
- Nota reforzada: `IA_practitioner/notes/Amazon Bedrock.md`.

### Textract, Rekognition y Kendra

- **Pregunta 43** (`preguntas/pregunta_7.png`, `feedback/feedback_7.1.png`, `feedback/feedback_7.2.png`)
- Concepto evaluado: procesar documentos legales escaneados y analizar imágenes con mínima gestión.
- Selección mixta visible: Rekognition correcta; Kendra incorrecta.
- Respuesta correcta visible: Amazon Textract y Amazon Rekognition.
- Punto de confusión: Kendra busca en contenido empresarial; no extrae texto de documentos escaneados ni analiza imágenes por sí mismo.
- Notas reforzadas: `IA_practitioner/notes/Amazon Textract.md`, `IA_practitioner/notes/Amazon Rekognition.md`, `IA_practitioner/notes/Amazon Kendra.md`.

### OCR y texto a voz

- **Pregunta 49** (`preguntas/pregunta_8.png`, `feedback/feedback_8.1.png`, `feedback/feedback_8.2.png`)
- Concepto evaluado: leer en voz alta texto impreso/manuscrito desde imágenes.
- Selección mixta visible: Polly correcta; Rekognition incorrecta.
- Respuesta correcta visible: Amazon Textract y Amazon Polly.
- Punto de confusión: Textract extrae texto de documentos/imágenes; Polly convierte texto a voz. Rekognition analiza imágenes/video, pero no es la pieza principal para OCR documental + lectura hablada.
- Notas reforzadas: `IA_practitioner/notes/Amazon Textract.md`, `IA_practitioner/notes/Amazon Polly.md`, `IA_practitioner/notes/Amazon Rekognition.md`.

## Directrices para una IA Responsable

### Documentación de modelos

- **Pregunta 50** (`preguntas/pregunta_9.png`, `feedback/feedback_9.1.png`, `feedback/feedback_9.2.png`)
- Concepto evaluado: registrar usos previstos, riesgos, entrenamiento y evaluación del modelo.
- Selección incorrecta visible: SageMaker Model Monitor.
- Respuesta correcta visible: SageMaker Model Cards.
- Punto de confusión: Model Monitor vigila modelos en producción; Model Cards documenta detalles críticos para transparencia, revisión y auditoría.
- Notas reforzadas: `IA_practitioner/notes/Amazon SageMaker.md`, `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`.

### Evaluar LLMs y proteger datos sensibles

- **Pregunta 58** (`preguntas/pregunta_10.png`, `feedback/feedback_10.png`)
- Concepto evaluado: comparar LLMs y aplicar protecciones de privacidad/seguridad.
- Selección mixta visible: Bedrock Guardrails correcta; Amazon Lex incorrecta.
- Respuesta correcta visible: Amazon Bedrock Model Evaluation y Amazon Bedrock Guardrails.
- Punto de confusión: Lex es conversación/NLU; no evalúa modelos fundacionales ni aplica guardrails de Bedrock.
- Notas reforzadas: `IA_practitioner/notes/Amazon Bedrock.md`, `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`.

### Auditoría y documentación para cumplimiento

- **Pregunta 62** (`preguntas/pregunta_11.png`, `feedback/feedback_11.png`)
- Concepto evaluado: documentar entrenamiento y rendimiento de modelos para auditoría.
- Selección incorrecta visible: SageMaker Model Monitor.
- Respuesta correcta visible: Amazon SageMaker Model Cards.
- Punto de confusión: CloudTrail registra actividad API y AWS Config evalúa configuración; para documentación del modelo, la pista es Model Cards.
- Notas reforzadas: `IA_practitioner/notes/Amazon SageMaker.md`, `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`.

## Plan de estudio corto

1. Repasar primero `Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`: separar riesgos de GenAI, guardrails, evaluación, Model Cards, CloudTrail y AWS Config.
2. Repasar `Amazon Bedrock.md`: Bedrock administrado, Guardrails, Model Evaluation, RAG y bases vectoriales.
3. Repasar `Métricas de evaluación e inferencia.md`: latencia por tokens, inferencia batch vs serverless vs tiempo real vs asincrónica.
4. Repasar `Amazon SageMaker.md`: Model Cards vs Model Monitor vs Model Dashboard vs Role Manager.
5. Repasar servicios de aplicación (`Textract`, `Rekognition`, `Polly`, `Kendra`) con una regla mental: documentos/OCR, imágenes/video, texto-a-voz, búsqueda empresarial.
6. Cerrar con `Ajuste de modelos GenAI.md`: domain adaptation, instruction-based fine-tuning, transfer learning, overfitting y bias/variance.
