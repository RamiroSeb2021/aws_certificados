# Repaso activo - Examen de práctica 1

> Objetivo: entrenar el criterio para no volver a caer en las mismas trampas.
> Fuente: errores del examen, feedback local, `IA_practitioner/notes/` y `AWS-AIF-C01-v4.pdf`.
> Las capturas quedan como evidencia en `preguntas/` y `feedback/`, pero este archivo NO es un listado de preguntas.

## Cómo usar este repaso

1. Leé la **regla mental** de cada bloque.
2. Tapá la respuesta y contestá las **preguntas de práctica**.
3. Revisá la **trampa del examen**: ahí está el patrón que te hizo fallar.
4. Si dudás, abrí el apunte indicado y repasá solo esa sección.

---

## 1. Riesgos de GenAI vs principios generales de IA responsable

### Regla mental

Cuando el examen pregunte por **riesgos propios de GenAI**, pensá primero en lo que el modelo puede **generar**:

- alucinaciones;
- toxicidad;
- problemas de propiedad intelectual;
- contenido dañino o no deseado.

Cuando pregunte por **IA responsable en general**, pensá en dimensiones más amplias:

- privacidad y seguridad;
- explicabilidad;
- transparencia;
- equidad;
- gobernanza.

### Trampa del examen

Privacidad, seguridad, explicabilidad y transparencia son correctas en IA responsable, pero no siempre son la mejor respuesta si el foco es **salidas generativas**.

### Preguntas de práctica

- Si un chatbot inventa una respuesta convincente pero falsa, ¿qué riesgo es?
- Si una app genera texto parecido a material protegido, ¿qué riesgo aparece?
- Si el escenario pide justificar decisiones y documentar límites del sistema, ¿estamos en riesgo generativo específico o IA responsable general?

### Apunte para reforzar

- `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`

---

## 2. Ajuste de modelos: domain adaptation vs instruction-based

### Regla mental

Si el escenario habla de adaptar el modelo a un **dominio, estilo, industria o dataset existente**, pensá en:

> **Domain adaptation fine-tuning**

Si el escenario habla de que el modelo siga **instrucciones, formatos o tareas concretas**, pensá en:

> **Instruction-based fine-tuning**

### Trampa del examen

“Generar descripciones parecidas a las ya existentes” no es simplemente “seguir instrucciones”. La pista fuerte es que hay un **estilo/dominio** que el modelo debe aprender.

### Preguntas de práctica

- Una tienda quiere generar descripciones con el mismo estilo de su catálogo histórico. ¿Qué ajuste encaja mejor?
- Una empresa quiere que el modelo responda siempre en JSON con campos fijos. ¿Qué ajuste encaja mejor?
- Si el dataset no tiene pares `prompt/completion`, sino mucho texto del dominio, ¿qué enfoque te empieza a sonar?

### Apunte para reforzar

- `IA_practitioner/notes/Ajuste de modelos GenAI.md`

---

## 3. Overfitting, bias y variance

### Regla mental

Si el modelo va muy bien en entrenamiento pero mal en prueba, pensá:

> **Overfitting: bajo sesgo, alta varianza**

El modelo aprendió demasiado los datos de entrenamiento y generaliza mal.

### Trampa del examen

No confundas “mal rendimiento en test” con “alto sesgo”. Alto sesgo suele indicar un modelo demasiado simple que falla incluso al aprender patrones importantes.

### Preguntas de práctica

- Si el accuracy de entrenamiento es alto y el de prueba baja mucho, ¿qué problema hay?
- ¿Overfitting se asocia más con alta varianza o alto sesgo?
- ¿Qué ayuda más contra overfitting: simplificar/regularizar/aumentar datos o hacer el modelo todavía más complejo?

### Apunte para reforzar

- `IA_practitioner/notes/Ajuste de modelos GenAI.md`

---

## 4. Latencia de inferencia

### Regla mental

La latencia depende sobre todo de cuánto trabajo debe hacer el modelo:

- tamaño/tipo de modelo;
- cantidad de tokens de entrada;
- cantidad de tokens generados en la salida.

Temperatura, Top P y Top K cambian el comportamiento de generación, pero la fuente remarca que **no son los factores principales de latencia**.

### Trampa del examen

Los parámetros de creatividad suenan técnicos y tentadores, pero si la pregunta dice “latencia”, buscá tokens y tamaño del modelo.

### Preguntas de práctica

- ¿Qué suele tardar más: una respuesta de 20 tokens o una de 2.000 tokens?
- Si el prompt incluye mucho contexto, ¿qué pasa con la latencia?
- ¿Top P aumenta directamente la latencia según la fuente del curso?

### Apunte para reforzar

- `IA_practitioner/notes/Métricas de evaluación e inferencia.md`

---

## 5. Bases vectoriales y búsqueda por similitud

### Regla mental

Si el escenario habla de **embeddings**, **vectores**, **búsqueda por similitud** o **RAG**, pensá en almacenes que soporten consultas vectoriales.

En la fuente aparecen asociados a este tema:

- Amazon OpenSearch Service;
- Amazon DocumentDB;
- Amazon Aurora / RDS for PostgreSQL;
- Amazon Neptune.

### Trampa del examen

S3 almacena objetos, QuickSight visualiza datos y Redshift analiza datos estructurados a escala. No son la respuesta directa cuando la pista es búsqueda vectorial eficiente.

### Caveat de fuente

El feedback del examen menciona `Amazon Neptune ML`. El PDF local respalda `Neptune` dentro del contexto de bases para RAG/vectorización, pero no deja igual de explícito el nombre `Neptune ML`.

### Preguntas de práctica

- Si necesitás buscar documentos similares por embeddings, ¿pensás primero en S3 o en una base/vector store?
- ¿QuickSight sirve para visualizar o para búsqueda semántica vectorial?
- En RAG, ¿la base vectorial guarda texto crudo solamente o representaciones numéricas/embeddings?

### Apunte para reforzar

- `IA_practitioner/notes/Amazon Bedrock.md`

---

## 6. Tipos de inferencia

### Regla mental

Elegí el tipo de inferencia por el **tiempo de respuesta requerido** y el **volumen de trabajo**.

| Pista del escenario | Tipo de inferencia |
|---|---|
| Respuesta inmediata, baja latencia | Tiempo real |
| Mucho volumen offline, no urgente | Por lotes / batch |
| Solicitudes largas que no necesitan respuesta inmediata | Asincrónica |
| No querés administrar servidores ni capacidad | Serverless |

### Trampa del examen

“Sin administrar servidores” apunta a serverless. “Grandes lotes offline” apunta a batch. No son lo mismo.

### Preguntas de práctica

- Procesar millones de registros durante la noche, ¿real-time o batch?
- Una app que responde al usuario mientras espera, ¿batch o real-time?
- Una solicitud pesada que puede completarse después, ¿sincrónica inmediata o asincrónica?

### Apunte para reforzar

- `IA_practitioner/notes/Métricas de evaluación e inferencia.md`

---

## 7. Bedrock vs SageMaker JumpStart

### Regla mental

Si querés consumir foundation models administrados mediante API, sin entrenar ni alojar modelos, pensá en:

> **Amazon Bedrock**

Si el escenario habla de arrancar proyectos de ML con modelos/soluciones preconfiguradas dentro de SageMaker, pensá en:

> **SageMaker JumpStart**

### Trampa del examen

JumpStart suena atractivo porque tiene modelos listos, pero si el caso pide GenAI administrada, generación de imágenes con FM y poca gestión operativa, la opción fuerte es Bedrock.

### Preguntas de práctica

- Una empresa sin experiencia de ML quiere generar imágenes usando FM administrados. ¿Bedrock o JumpStart?
- Si el equipo quiere explorar, personalizar y desplegar modelos desde SageMaker, ¿qué servicio encaja?
- ¿Bedrock exige entrenar el FM desde cero?

### Apunte para reforzar

- `IA_practitioner/notes/Amazon Bedrock.md`

---

## 8. Textract, Rekognition, Polly y Kendra

### Regla mental

Usá esta tabla para decidir rápido:

| Necesidad | Servicio |
|---|---|
| Extraer texto, escritura a mano, tablas o formularios de documentos | Amazon Textract |
| Analizar imágenes/video, detectar objetos, rostros, etiquetas o moderación | Amazon Rekognition |
| Convertir texto en voz natural | Amazon Polly |
| Buscar respuestas en repositorios empresariales | Amazon Kendra |

### Trampa del examen

Rekognition analiza imágenes, pero si el caso es **documento escaneado/OCR/formularios/tablas**, Textract suele ser la pieza principal.

Kendra busca sobre contenido empresarial; no reemplaza OCR ni análisis de imágenes.

Polly necesita texto disponible: si el texto está en una foto/documento, primero hay que extraerlo.

### Preguntas de práctica

- Una app debe leer en voz alta texto manuscrito en una imagen. ¿Qué combinación tiene sentido?
- Un sistema debe detectar objetos o moderar imágenes. ¿Textract o Rekognition?
- Una empresa quiere que empleados busquen respuestas en documentos internos. ¿Kendra o Polly?

### Apuntes para reforzar

- `IA_practitioner/notes/Amazon Textract.md`
- `IA_practitioner/notes/Amazon Rekognition.md`
- `IA_practitioner/notes/Amazon Polly.md`
- `IA_practitioner/notes/Amazon Kendra.md`

---

## 9. SageMaker Model Cards vs Model Monitor vs Dashboard vs CloudTrail/Config

### Regla mental

Cuando el escenario pida **documentar el modelo**, pensá en:

> **SageMaker Model Cards**

Model Cards sirven para documentar:

- propósito del modelo;
- usos previstos;
- datos de entrenamiento;
- métricas;
- limitaciones;
- resultados de evaluación;
- riesgos y consideraciones para auditoría.

### Comparación rápida

| Pista | Servicio |
|---|---|
| Documentar modelo, entrenamiento, métricas y usos previstos | SageMaker Model Cards |
| Monitorear drift, calidad y rendimiento en producción | SageMaker Model Monitor |
| Ver y explorar modelos en una consola central | SageMaker Model Dashboard |
| Registrar llamadas/API de AWS | AWS CloudTrail |
| Auditar configuración de recursos AWS | AWS Config |

### Trampa del examen

“Auditoría” no siempre significa CloudTrail o Config. Si la auditoría trata sobre el **modelo** y su documentación, la respuesta suele ser Model Cards.

### Preguntas de práctica

- Te piden documentar usos previstos, riesgos y métricas de un modelo. ¿Qué elegís?
- Te piden detectar data drift en producción. ¿Model Cards o Model Monitor?
- Te piden saber quién llamó una API de AWS. ¿Model Cards o CloudTrail?

### Apuntes para reforzar

- `IA_practitioner/notes/Amazon SageMaker.md`
- `IA_practitioner/notes/Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`

---

## 10. Evaluación de LLMs y Guardrails en Bedrock

### Regla mental

Si el escenario pide comparar modelos fundacionales y elegir el mejor:

> **Amazon Bedrock Model Evaluation**

Si pide bloquear temas, filtrar contenido dañino, proteger PII o mitigar jailbreak/prompt injection:

> **Amazon Bedrock Guardrails**

### Trampa del examen

Amazon Lex sirve para interfaces conversacionales con ASR/NLU. No es la herramienta para evaluar foundation models ni aplicar Guardrails de Bedrock.

### Preguntas de práctica

- Una empresa quiere comparar varios LLMs con métricas. ¿Qué usás?
- Una app GenAI debe bloquear contenido sensible y temas prohibidos. ¿Qué usás?
- Un bot necesita entender intención del usuario en llamadas/chat. ¿Bedrock Guardrails o Lex?

### Apunte para reforzar

- `IA_practitioner/notes/Amazon Bedrock.md`

---

## Checklist rápido antes de responder

Antes de elegir una opción en el examen, preguntate:

1. ¿La pista habla de **generar contenido**? → Bedrock / riesgos GenAI / Guardrails.
2. ¿La pista habla de **documentar un modelo**? → Model Cards.
3. ¿La pista habla de **monitorear en producción**? → Model Monitor.
4. ¿La pista habla de **OCR/documentos**? → Textract.
5. ¿La pista habla de **imagen/video/rostros/objetos**? → Rekognition.
6. ¿La pista habla de **texto a voz**? → Polly.
7. ¿La pista habla de **búsqueda empresarial**? → Kendra.
8. ¿La pista habla de **embeddings/similitud/RAG**? → Vector store / OpenSearch / DocumentDB / Neptune.
9. ¿La pista habla de **grandes lotes offline**? → Batch inference.
10. ¿La pista habla de **adaptar a un dominio/estilo**? → Domain adaptation fine-tuning.

---

## Ruta de repaso recomendada

1. **Primero Bedrock**: Model Evaluation, Guardrails, RAG, bases vectoriales, Bedrock vs JumpStart.
2. **Después SageMaker**: Model Cards vs Monitor vs Dashboard.
3. **Después servicios preentrenados**: Textract, Rekognition, Polly, Kendra.
4. **Después inferencia**: latencia y tipos de inferencia.
5. **Cerrá con ajuste GenAI**: domain adaptation, instruction-based fine-tuning, overfitting y variance.

---

## Mapa mínimo a capturas originales

Usá esto solo si querés volver al feedback original:

| Tema | Capturas |
|---|---|
| Riesgos específicos de GenAI | `pregunta_1`, `feedback_1` |
| Latencia de inferencia | `pregunta_2`, `feedback_2` |
| Bases vectoriales / similitud | `pregunta_3`, `feedback_3.*` |
| Inferencia batch | `pregunta_4`, `feedback_4.*` |
| Domain adaptation fine-tuning | `pregunta_5`, `feedback_5` |
| Bedrock vs JumpStart | `pregunta_6`, `feedback_6.*` |
| Textract / Rekognition / Kendra | `pregunta_7`, `feedback_7.*` |
| Textract + Polly | `pregunta_8`, `feedback_8.*` |
| SageMaker Model Cards | `pregunta_9`, `feedback_9.*` |
| Bedrock Model Evaluation + Guardrails | `pregunta_10`, `feedback_10` |
| Auditoría y Model Cards | `pregunta_11`, `feedback_11` |
| Overfitting / bias / variance | `pregunta_12`, `feedback_12` |
