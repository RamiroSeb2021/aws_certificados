# Amazon Bedrock

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.
- Precios y límites se conservan como aparecen en fuente; pueden cambiar con el tiempo.

## Qué es

- Servicio totalmente administrado que ofrece modelos fundacionales (FM) de alto rendimiento.
- Permite construir aplicaciones de IA generativa en AWS.
- No requiere entrenar modelos con datos propios para empezar.
- Opcionalmente permite personalizar modelos con datos propios para dar más contexto.

## Modelos base

- Antes de usar un modelo base se debe solicitar permiso.
- Modelos Amazon Titan: aprobación inmediata según fuente.
- Modelos de terceros: pueden requerir información adicional.
- Cobro según tarifas del tercero a través de AWS.

## Comparación de modelos en fuente

| Modelo | Tokens máximos | Características | Casos de uso | Precio fuente |
|---|---:|---|---|---|
| Amazon Titan Text Express | 8K | Texto de alto rendimiento, +100 idiomas | Contenido, clasificación, educación | Entrada `$0.0008`, salida `$0.0016` por 1K tokens |
| Llama 2 70b-chat | 4K | Tareas a gran escala y diálogos, principalmente inglés | Generación de texto, servicio al cliente | Entrada `$0.0019`, salida `$0.0025` por 1K tokens |
| Claude 2.1 | 200K | Generación de texto en varios idiomas | Análisis, pronóstico, comparación de documentos | Entrada `$0.008`, salida `$0.024` por 1K tokens |
| Stable Diffusion SDXL 1.0 | 77 tokens/prompt | Generación de imágenes | Publicidad, medios | `$0.04-$0.08` por imagen |

## Personalización de modelos

### Modelo fundacional y preentrenamiento

- Un foundation model se entrena inicialmente con grandes volúmenes de datos, normalmente no supervisados o auto-supervisados.
- Ese entrenamiento inicial aprende patrones generales antes de adaptar el modelo a tareas concretas.
- Entrenar o preentrenar un modelo desde cero ofrece máxima flexibilidad, pero exige más datos, cómputo, tiempo y coste.
- Para la mayoría de escenarios de examen, si ya existe un FM útil, adaptar el modelo suele ser más razonable que crear uno desde cero.

### Fine-tuning

- Ajusta un modelo preentrenado para una tarea específica usando datos adicionales.
- Evita entrenar desde cero.
- Usa menos datos y recursos que reentrenar un FM completo.
- Se integra con S3 para almacenar datos.
- Formato fuente: pares `prompt` / `completion`.
- En Bedrock, pensar en personalización privada del modelo: no se modifica el FM base público; se crea/adapta una copia privada para el caso de uso.

### Continuous pre-training

- Mejora modelos preentrenados con datos sin etiquetar.
- Aplicable a Amazon Titan Text Express y Lite según fuente.
- Adapta el modelo a dominios como finanzas, medicina o derecho.
- Usa aprendizaje por transferencia.
- Formato fuente: entradas `input` de texto.

### Comparación de personalización

| Enfoque | Cuándo encaja | Qué cambia |
|---|---|---|
| In-context learning | Dar ejemplos o contexto en el prompt | No cambia pesos del modelo |
| RAG | Responder con información recuperada externa | No cambia pesos; mejora contexto |
| Fine-tuning | Adaptar a tarea específica con ejemplos | Ajusta una copia/modelo personalizado |
| Continuous pre-training | Adaptar conocimiento general a dominio con texto no etiquetado | Sigue entrenando sobre dominio |
| Pre-training desde cero | Necesidad extrema de control/flexibilidad | Crea modelo nuevo; mayor coste |

## RAG y bases de conocimiento

- Bases de conocimiento: aportan contexto privado de empresa desde fuentes como S3, SharePoint y web crawler.
- RAG: recupera datos empresariales y enriquece el prompt para respuestas más relevantes y precisas.
- Casos de uso: atención al cliente, asistentes virtuales con información actualizada, búsqueda avanzada.
- Bases vectoriales mencionadas: OpenSearch Service, DocumentDB, Aurora, RDS for PostgreSQL y Neptune.

### Error de examen / Punto de confusión

- Para búsqueda por similitud con embeddings o vectores, pensar en servicios/base de datos que puedan almacenar y consultar vectores.
- Según la fuente, OpenSearch Service, DocumentDB y Neptune aparecen asociados a bases de datos de vectores para RAG; S3, QuickSight o Redshift no son la respuesta directa cuando la pista es búsqueda vectorial eficiente.

## Guardrails y agentes

- Guardrails: controles para uso seguro, ético y responsable.
- Permiten temas denegados, filtros de contenido, defensa contra jailbreak/prompt injection y eliminación de PII/datos sensibles.
- Agentes de Bedrock: asistentes que interactúan con usuarios y ejecutan tareas.
- Pueden conectarse a bases de datos, APIs, Lambda y bases de conocimiento.

## Evaluación de modelos

- Permite evaluar, comparar y seleccionar FM.
- Evaluación automática: métricas predefinidas como precisión, robustez y toxicidad.
- Evaluación humana: criterios subjetivos, expertos o equipo gestionado por AWS.
- Solo se elige un tipo de tarea por trabajo de evaluación.
- Métricas explicadas: ROUGE, BLEU y BERTScore.

### Error de examen / Punto de confusión

- Si el escenario pide comparar LLMs o elegir el mejor FM para una tarea, pensar en **Amazon Bedrock Model Evaluation**.
- Si además pide bloquear temas, filtrar contenido dañino, proteger PII o aplicar controles de seguridad/responsabilidad, pensar en **Amazon Bedrock Guardrails**.
- No confundir con Amazon Lex: Lex ayuda a construir interfaces conversacionales, no a evaluar FM ni aplicar guardrails de Bedrock.

## Métricas de negocio en GenAI

- Las métricas técnicas evalúan comportamiento del modelo: precisión, robustez, toxicidad, calidad de respuesta o latencia.
- Las métricas de negocio evalúan valor para la organización: conversión, retención, reducción de tiempo operativo, satisfacción del cliente o ingresos.
- En ecommerce, si la pregunta pide valor generado por una aplicación GenAI, la tasa de conversión suele medir mejor impacto de negocio que tokens generados o tamaño del dataset.

## Bedrock vs SageMaker JumpStart

- Bedrock encaja cuando se quiere consumir foundation models administrados mediante API, sin entrenar, alojar ni gestionar el modelo.
- SageMaker JumpStart ofrece modelos y soluciones preconfiguradas dentro de SageMaker, pero el escenario puede implicar despliegue o gestión de endpoints.
- Para generar imágenes con FM administrados y sin experiencia de ML, la pista fuerte es Bedrock.

## Costes en fuente

- Bajo demanda: tokens procesados e imágenes generadas.
- Batch: múltiples predicciones, salida en S3, descuentos de hasta 50% según fuente.
- Rendimiento aprovisionado: cobro por hora y compromisos; requerido para modelos personalizados.
- Importación de modelos: importación gratuita; se cobra inferencia.
- Personalización: tokens durante entrenamiento y almacenamiento mensual.
- Evaluación: automática paga inferencia; humana agrega coste por tarea humana.

### Error de examen / Punto de confusión

- Si la pista es reducir coste en prompts diarios, reducir tokens de entrada/salida suele ser la opción directa.
- Agregar ejemplos few-shot mejora contexto pero sube tokens.
- Provisioned Throughput no es sinónimo de ahorro; encaja cuando se necesita capacidad garantizada o cargas sostenidas.

## Claves de examen

- Bedrock = GenAI administrada con FM.
- RAG = contexto externo sin cambiar FM.
- Fine-tuning = adaptar a tarea específica.
- Continuous pre-training = conocimiento de dominio con datos sin etiquetar.
- Guardrails = seguridad, temas bloqueados, PII, jailbreak e inyección de prompts.
- Fine-tuning = tarea específica; continuous pre-training = dominio; RAG = contexto externo; in-context learning = ejemplos/contexto en prompt.
- Para profundizar ajustes de modelos GenAI: ver `Ajuste de modelos GenAI.md`.
