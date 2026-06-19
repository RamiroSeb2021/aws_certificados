# Amazon SageMaker

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.
- Conceptos dudosos o dependientes del tiempo se conservan como aparecen en fuente.

## Qué es

- Servicio totalmente gestionado de Machine Learning.
- Permite construir, entrenar y desplegar modelos de ML de forma rápida y segura.
- Soporta frameworks y algoritmos como TensorFlow, PyTorch, MXNet, entre otros.
- Permite traer algoritmos propios en contenedores Docker.
- Facilita entrenamiento distribuido que escala según necesidad.

## Flujo típico de ML

1. Obtención de datos.
2. Limpieza y preparación.
3. Elección del modelo.
4. Entrenamiento.
5. Evaluación.
6. Despliegue.
7. Monitoreo, colección de datos y evaluación continua.

## Componentes clave

### SageMaker Studio

- Interfaz unificada para desarrollar, entrenar, desplegar y monitorizar modelos.
- Incluye selección de IDE administrado, herramientas end-to-end de ML, exploración/ajuste/evaluación/despliegue de FM y ejecución segura.

### SageMaker Data Wrangler

- Prepara datos para ML con interfaz visual y lenguaje natural.
- Accede a datos tabulares, texto e imágenes desde S3, Athena, Redshift y más de 50 fuentes externas.
- Genera informes de calidad: faltantes, duplicados, anomalías.
- Ofrece más de 300 transformaciones predefinidas en PySpark.
- Permite visualizaciones, estimación de poder predictivo y automatización de flujos de preparación.

### SageMaker Feature Store

- Almacena, comparte y gestiona características para modelos ML.
- Catálogo centralizado para crear, organizar y reutilizar features.
- Soporta almacenamiento offline para entrenamiento y online para inferencia en tiempo real.
- Incluye linaje, viaje en el tiempo, seguridad y controles granulares.

### Automatic Model Tuning (AMT)

- Optimiza automáticamente hiperparámetros.
- Reduce ajuste manual y ejecuta experimentos en paralelo.
- Compatible con amplia variedad de algoritmos integrados.

### Deployment & Inference

- Inferencia en tiempo real: baja latencia.
- Inferencia serverless: sin administrar servidores ni escalado manual.
- Inferencia batch: grandes volúmenes sin respuesta inmediata.
- Inferencia asincrónica: solicitudes largas que no requieren respuesta inmediata.

### Model Monitor

- Monitorea modelos en producción.
- Captura estadísticas de entrada/salida, anomalías y deriva.
- Envía alertas con CloudWatch.
- Detecta data drift, problemas de calidad de datos, desempeño del modelo, sesgo y deriva de explicabilidad.

### Model Registry

- Almacén central para modelos versionados.
- Gestiona versiones, aprobaciones, control de acceso y auditoría.
- Facilita integración CI/CD.

### SageMaker Pipelines

- Gestiona flujos de trabajo de ML desde preprocesamiento hasta despliegue.
- Reutiliza componentes, programa workflows y permite scripts propios.

### Role Manager

- Facilita creación y gestión de roles IAM específicos para SageMaker.
- Usa plantillas y permisos granulares.

### Model Cards y Model Dashboard

- Model Cards documentan propósito, datos, métricas, limitaciones y detalles críticos del modelo.
- Model Dashboard centraliza visualización, búsqueda y monitoreo de modelos.

### JumpStart, Canvas, MLflow, Clarify y Ground Truth

- JumpStart: modelos y soluciones preconfiguradas, incluyendo FM públicos y propietarios.
- Canvas: creación de modelos sin programación, con interfaz drag-and-drop.
- MLflow en SageMaker: seguimiento de experimentos, métricas, parámetros y despliegues.
- Clarify: detección de sesgos y explicabilidad.
- Ground Truth: creación de datasets etiquetados, RLHF y etiquetado humano vía Mechanical Turk o proveedores externos.

## Claves de examen

- SageMaker = plataforma end-to-end de ML.
- Data Wrangler = preparación visual de datos.
- Feature Store = repositorio centralizado de features.
- AMT = ajuste automático de hiperparámetros.
- Model Monitor = drift, calidad, rendimiento y alertas.
- Clarify = sesgo y explicabilidad.
- Ground Truth = etiquetado humano/datasets.
