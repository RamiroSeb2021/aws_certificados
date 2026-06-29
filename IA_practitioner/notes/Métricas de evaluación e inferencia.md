# Métricas de evaluación e inferencia

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> Nota ampliada desde los conceptos mencionados en fuente; no se agregan servicios AWS nuevos.

## Criterio de edición

- Se profundizan las métricas ROUGE, BLEU y BERTScore mencionadas en la sección de evaluación de modelos en Amazon Bedrock.
- Se agrupa todo lo que la fuente menciona sobre inferencia: inferencia en el borde, tipos de inferencia en SageMaker, latencia, costes y monitoreo.
- Se preservan precios, ejemplos y límites como aparecen en la fuente; pueden cambiar con el tiempo.

## Métricas de evaluación de modelos

- Los modelos de lenguaje necesitan métricas para evaluar precisión y calidad.
- Estas métricas ayudan a comparar respuestas generadas por el modelo contra respuestas de referencia.
- En Amazon Bedrock, la evaluación puede ser:
  - Automática: usa métricas predefinidas.
  - Humana: usa criterios subjetivos o personalizados.
- Las métricas destacadas por la fuente para tareas de traducción automática y resumen de textos son:
  - ROUGE.
  - BLEU.
  - BERTScore.

### Contexto: respuesta generada vs. respuesta de referencia

En una evaluación automática se comparan tres elementos:

| Elemento | Qué representa |
|---|---|
| Pregunta o prompt de referencia | La entrada que recibe el modelo. |
| Respuesta generada | La salida producida por el modelo evaluado. |
| Respuesta de referencia | La salida esperada o aceptada para comparar. |

La puntuación sale de aplicar un algoritmo de evaluación sobre la respuesta generada y la referencia.

## ROUGE

**ROUGE** significa `Recall-Oriented Understudy for Gisting Evaluation`.

### Para qué sirve

- Evalúa la calidad de resúmenes.
- También puede usarse en sistemas de traducción automática.
- Se centra en cuánto contenido de la referencia aparece en el texto generado.
- Es especialmente útil cuando importa no perder información importante del texto original.

### Idea principal

ROUGE compara coincidencias entre:

- Texto de referencia.
- Texto generado por IA.

La intuición es: si el texto generado conserva muchas palabras, frases o secuencias importantes de la referencia, debería obtener mejor puntuación.

### ROUGE-N

- Mide coincidencias de `n-gramas`.
- Un `n-grama` es un grupo de `n` palabras consecutivas.
- ROUGE-1 compara palabras individuales.
- ROUGE-2 compara pares de palabras consecutivas.

Ejemplo de la fuente:

| Tipo | Texto |
|---|---|
| Referencia | `El ratón es perseguido por el gato en el jardín.` |
| Generado | `El gato persigue al ratón en el jardín.` |

Para ROUGE-1, coinciden palabras como:

- `el`.
- `gato`.
- `al`.
- `ratón`.
- `en`.
- `jardín`.

### ROUGE-L

- Evalúa la subsecuencia común más larga (`LCS`, Longest Common Subsequence).
- No se fija solo en palabras sueltas, sino en la secuencia más larga que ambos textos comparten en orden.
- Sirve para capturar si el texto generado conserva una estructura parecida a la referencia.

Ejemplo de la fuente:

- Subsecuencia común más larga: `El ratón en el jardín.`

### Cómo pensarlo para el examen

- ROUGE aparece muy asociado a resumen de textos.
- ROUGE mira coincidencias con la referencia.
- ROUGE-N = n-gramas.
- ROUGE-L = subsecuencia común más larga.

## BLEU

**BLEU** significa `Bilingual Evaluation Understudy`.

### Para qué sirve

- Evalúa la calidad de traducciones generadas por un modelo.
- Compara la traducción generada con una traducción de referencia hecha por una persona.
- Considera precisión: cuántas palabras o secuencias generadas coinciden con la referencia.

### Idea principal

BLEU no mira solo palabras individuales. También compara secuencias de varias palabras.

Esto evita que una traducción parezca buena solo porque contiene palabras correctas pero en un orden o contexto pobre.

### Ejemplo de la fuente

| Elemento | Texto |
|---|---|
| Oración en inglés | `The cat is sleeping on the sofa.` |
| Traducción generada por IA | `El gato duerme en el sofá.` |
| Traducción de referencia | `El gato está durmiendo en el sofá.` |

Coincidencias de 1-gramas:

- `El`.
- `gato`.
- `en`.
- `el`.
- `sofá`.

Coincidencias de 2-gramas:

- `El gato`.
- `en el`.
- `el sofá`.

### Cómo pensarlo para el examen

- BLEU aparece muy asociado a traducción automática.
- BLEU compara n-gramas de distintos tamaños.
- BLEU se orienta a precisión: cuánto de lo generado coincide con una referencia válida.

## BERTScore

### Para qué sirve

- Mide similitud semántica entre el texto generado y el texto de referencia.
- Permite reconocer significado parecido aunque las palabras sean distintas.

### Idea principal

BERTScore compara representaciones vectoriales de palabras o frases.

La fuente lo conecta con la idea de similitud entre vectores:

- Si dos términos tienen significado parecido, sus vectores deberían estar cerca.
- Si dos frases expresan una idea similar con palabras diferentes, BERTScore puede capturar esa cercanía semántica mejor que una métrica basada solo en coincidencias exactas.

### Ejemplo de la fuente

| Elemento | Texto |
|---|---|
| Referencia | `El coche se movió velozmente.` |
| Generado | `El automóvil aceleró rápidamente.` |

Aunque `coche` y `automóvil` no son la misma palabra exacta, tienen relación semántica. Lo mismo ocurre con `velozmente` y `rápidamente`.

### Cómo pensarlo para el examen

- BERTScore = similitud semántica.
- Es útil cuando las palabras difieren pero el significado se conserva.
- Se apoya en embeddings o vectores para comparar cercanía de significado.

## Comparación rápida: ROUGE vs BLEU vs BERTScore

| Métrica | Se usa mucho en | Qué compara | Idea clave |
|---|---|---|---|
| ROUGE | Resumen de textos | Coincidencias y subsecuencias con referencia | ¿Se conservó contenido importante? |
| BLEU | Traducción automática | Precisión de n-gramas | ¿La traducción generada coincide con una traducción humana? |
| BERTScore | Evaluación semántica | Similitud entre vectores | ¿El significado es parecido aunque cambien las palabras? |

## Evaluación automática y humana en Bedrock

### Evaluación automática

- Permite evaluar modelos de Amazon Bedrock con métricas como precisión, robustez y toxicidad.
- Usa conjuntos de datos integrados o datos personalizados.
- Los datos se envían a los modelos.
- Las respuestas se califican usando algoritmos de evaluación.
- Los resultados se presentan en informes visuales.

Ejemplo simplificado de la fuente:

```json
{
  "question": "¿Es Madrid la capital de España?",
  "answer": true
}
```

Métricas mencionadas para ese ejemplo:

- Precisión: `NLP-F1`.
- Robustez: `F1` y `deltaF1`.
- Toxicidad: `Toxicity`.

### Evaluación con trabajadores humanos

- Ideal para criterios subjetivos que requieren experiencia.
- Puede involucrar empleados, expertos o equipo gestionado por AWS.
- Permite revisión con interacciones simples:
  - Pulgar arriba / abajo.
  - Calificación de 1 a 5.
  - Elección entre respuestas.
- Puede usar conjuntos de datos integrados o personalizados.

## Inferencia

### Qué significa inferencia en estas notas

La fuente usa inferencia como el momento en que un modelo ya desplegado produce una predicción, clasificación o respuesta con datos nuevos.

Ejemplos en la fuente:

- Un modelo genera texto a partir de un prompt.
- Un dispositivo detecta un problema con una cámara.
- SageMaker despliega un modelo para predicciones en tiempo real.
- JumpStart permite desplegar modelos y ejecutar inferencias.

## Inferencia en el borde

### Definición

Inferencia en el borde significa realizar cálculos y predicciones directamente en dispositivos cercanos a donde se generan los datos, sin depender de un servidor en la nube.

Ejemplos de dispositivos mencionados:

- Cámaras.
- Sensores.
- Raspberry Pi.

### SLM en el dispositivo de borde

La fuente contrasta `Small Language Models (SLM)` en edge devices con modelos grandes en servidores remotos.

Ventajas de SLM en el dispositivo:

- Puede funcionar sin conexión a Internet.
- Tiene baja latencia por su tamaño pequeño.
- Puede hacer predicciones rápidamente.
- Puede actuar de inmediato y emitir una alerta.

Caso de la fuente:

- Dispositivo de seguridad en una fábrica.
- Usa una cámara para monitorizar.
- Si detecta un problema en tiempo real, la respuesta debe ser rápida.
- Un Raspberry Pi puede ejecutar un modelo pequeño localmente para una detección rápida.

### LLM en servidor remoto

Según la fuente, los `Large Language Models (LLM)` necesitan más potencia de procesamiento.

Características:

- Las predicciones tardan más en llegar al dispositivo.
- La latencia es mayor.
- Requieren conexión a Internet.
- Pueden servir para predicciones más complejas, como reconocimiento facial avanzado.

### Comparación para examen

| Situación | Mejor encaje según fuente | Motivo |
|---|---|---|
| Respuesta inmediata en fábrica | SLM en el borde | Baja latencia y puede funcionar sin conexión. |
| Predicción más compleja | LLM en servidor remoto | Más potencia y potencialmente más precisión, con mayor latencia. |

## Latencia del prompt

La fuente define latencia como el tiempo que tarda el modelo en procesar un prompt y devolver una respuesta.

Factores que afectan la latencia:

- Tamaño del modelo.
- Tipo de modelo.
- Número de tokens en la entrada.
- Número de tokens en la salida.

La fuente indica que estos parámetros no afectan a la latencia:

- Top P.
- Top K.
- Temperatura.

### Error de examen / Punto de confusión

- Si la pregunta dice “afecta directamente la latencia”, priorizar longitud de entrada y longitud de salida generada.
- Los parámetros de inferencia como temperatura, Top P o Top K modifican diversidad/aleatoriedad de la salida, pero no son la pista principal de latencia en la fuente.

## Inferencia en Amazon SageMaker

SageMaker Deployment & Inference se refiere a desplegar modelos de ML y realizar inferencias, es decir, predicciones o clasificaciones con nuevos datos.

### Inferencia en tiempo real

- Proporciona predicciones casi instantáneas.
- Es ideal para aplicaciones con requisitos de baja latencia.

### Inferencia serverless

- No requiere administrar servidores.
- No requiere preocuparse por escalabilidad manual.

### Inferencia por lotes

- También aparece como `batch`.
- Ideal para grandes volúmenes de datos.
- No requiere respuestas inmediatas.

### Error de examen / Punto de confusión

- Para procesamiento offline de grandes lotes de datos, elegir inferencia por lotes.
- Serverless reduce gestión de servidores y escalado manual, pero no reemplaza la pista de “grandes volúmenes offline”.

### Inferencia asincrónica

- Adecuada para solicitudes que tardan en procesarse.
- No necesita respuesta inmediata.

### Comparación rápida

| Tipo de inferencia | Cuándo usarla según fuente |
|---|---|
| Tiempo real | Respuestas casi instantáneas y baja latencia. |
| Serverless | Cuando no querés administrar servidores ni escalado manual. |
| Batch | Grandes volúmenes sin respuesta inmediata. |
| Asincrónica | Solicitudes largas sin necesidad de respuesta inmediata. |

## Inferencia y datos en SageMaker Feature Store

La fuente menciona que SageMaker Feature Store ofrece:

- Almacenamiento sin conexión para entrenamiento.
- Almacenamiento en línea para inferencia en tiempo real.
- Sincronización entre ambos para asegurar precisión del modelo.

La idea clave es que las características usadas para entrenar y las usadas para inferir deben mantenerse coherentes.

## Inferencia, despliegue y monitoreo

### Flujo típico de ML

En el flujo típico de Machine Learning de la fuente, inferencia aparece después del entrenamiento y evaluación:

1. Obtención de datos.
2. Limpieza y preparación.
3. Elección del modelo.
4. Entrenamiento.
5. Evaluación.
6. Despliegue.
7. Monitoreo, colección de datos y evaluación.

### Model Monitor

SageMaker Model Monitor permite monitorear modelos en producción.

Aspectos relacionados con inferencia:

- Captura estadísticas de entrada y salida del modelo.
- Configura alertas ante anomalías.
- Funciona con modelos desplegados en SageMaker.
- Puede detectar:
  - Data drift.
  - Problemas de calidad de datos.
  - Desempeño del modelo.
  - Sesgo.
  - Deriva de explicabilidad.

## Inferencia y costes en Amazon Bedrock

La fuente menciona costes relacionados con inferencia:

- Bajo demanda: cobro por tokens procesados en texto y por cada imagen generada.
- Batch: múltiples predicciones a la vez, salida en S3 y descuentos de hasta el 50% según fuente.
- Importación de modelos: importar un modelo personalizado a Bedrock es gratuito, pero se cobra por la inferencia del modelo.
- Evaluación automática: se paga solo por inferencia.
- Evaluación humana: agrega cobro por tarea humana.

## Inferencia y generación de texto

La fuente explica que los LLM generan texto prediciendo el siguiente token según contexto y probabilidades calculadas.

Ejemplo:

`Me gustaría comer patatas con _______`

| Siguiente token | Probabilidad |
|---|---:|
| Salsa | 0.60 |
| Queso | 0.25 |
| Ensalada | 0.10 |
| Guacamole | 0.05 |

Esto se conecta con la inferencia porque cada respuesta generada implica procesar el prompt y producir tokens de salida.

## Claves de examen

- ROUGE: resumen de textos, n-gramas y subsecuencia común más larga.
- BLEU: traducción automática y precisión de n-gramas.
- BERTScore: similitud semántica mediante vectores.
- Inferencia en el borde: baja latencia, dispositivo cercano a los datos, puede funcionar sin Internet.
- SLM local: respuesta rápida en edge device.
- LLM remoto: más potencia y predicciones complejas, pero mayor latencia y dependencia de Internet.
- SageMaker ofrece inferencia en tiempo real, serverless, batch y asincrónica.
- Prompt latency depende del modelo y tokens de entrada/salida, no de Top P, Top K ni temperatura según fuente.
- Model Monitor ayuda a vigilar modelos ya desplegados y sus datos de entrada/salida.
