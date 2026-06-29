# Ajuste de modelos GenAI

> Fuente: `AWS-AIF-C01-v4.pdf`, páginas 121-132 y 158-160.
> Apunte creado para reforzar Fine-Tuning, Continuous Pre-training, Transfer Learning y enfoques de personalización en Amazon Bedrock.
> No se agrega contenido AWS externo; se organiza y profundiza solo lo que aparece en la fuente.

## Idea central

En GenAI normalmente no entrenas un modelo fundacional desde cero.

- Un **modelo fundacional (FM)** ya fue entrenado con grandes cantidades de datos generales.
- Ese modelo puede usarse directamente para generar texto, clasificar, resumir o responder preguntas.
- Si el resultado no se adapta bien a tu caso, puedes **personalizarlo**.
- La personalización busca mejorar el comportamiento del modelo sin pagar el coste de entrenar un FM completo desde cero.

La pregunta de examen suele estar en elegir **qué tipo de ajuste corresponde al problema**.

## Entrenar desde cero vs usar un modelo preentrenado

### Entrenar desde cero

Entrenar un FM desde cero o parcialmente implica:

- mayor inversión;
- grandes cantidades de datos;
- computación intensa;
- más tiempo y recursos.

Este enfoque no suele ser la respuesta cuando el escenario ya habla de un **modelo de lenguaje preentrenado**.

### Usar un modelo preentrenado

Un modelo preentrenado permite:

- rapidez de implementación;
- costes reducidos;
- capacidad de personalización;
- reducción de riesgos;
- facilidad de integración.

En Amazon Bedrock, los modelos fundacionales pueden usarse como modelos base para aplicaciones de GenAI y, opcionalmente, personalizarse con datos propios.

## Fine-Tuning

El **Fine-Tuning** o ajuste fino toma un modelo ya entrenado con datos generales y lo ajusta para que funcione mejor en una **tarea específica** usando datos adicionales.

### Para qué sirve

Sirve cuando el modelo debe aprender un patrón de entrada/salida concreto:

- resumir textos de una forma específica;
- responder preguntas con un estilo esperado;
- clasificar entradas;
- generar salidas siguiendo ejemplos de la organización.

### Formato mental para recordarlo

Fine-Tuning = **“te muestro ejemplos de cómo quiero que respondas”**.

En la fuente aparece como pares:

```json
{"prompt": "<prompt1>", "completion": "<expected generated text>"}
{"prompt": "what is AWS", "completion": "it's Amazon Web Services"}
```

Es decir, el dataset enseña al modelo una relación entre una solicitud y una respuesta esperada.

## Fine-Tuning basado en instrucciones

El **Instruction-based fine-tuning** ajusta el FM para seguir instrucciones específicas.

Úsalo mentalmente cuando el escenario diga:

- “quiero que siga instrucciones mejor”;
- “quiero que responda con cierto formato”;
- “quiero que ejecute una tarea textual concreta”;
- “quiero mejorar resumen, Q&A o clasificación”.

Este enfoque está alineado con tareas específicas.

## Domain adaptation fine-tuning

El **Domain adaptation fine-tuning** adapta el modelo a un dominio, estilo o conjunto de datos específico.

Úsalo mentalmente cuando el escenario diga:

- hay datos propios de una industria, empresa o dominio;
- se quiere que las respuestas parezcan del mismo tipo que un dataset existente;
- el modelo debe adaptarse a descripciones, documentos o lenguaje de un ámbito concreto;
- no se habla solo de seguir instrucciones, sino de parecerse al dominio de los datos.

### Ejemplo de examen: descripciones de productos

Si el escenario dice:

> “Generar descripciones de productos para e-commerce usando un conjunto de datos de descripciones existentes del sitio”.

La clave es que el modelo debe adaptarse al **dominio y estilo** de esas descripciones existentes.

Respuesta esperada: **Domain adaptation fine-tuning**.

No es simplemente “Transfer Learning”, porque Transfer Learning es el concepto general. La opción más específica es adaptar el modelo al dominio/dataset.

### Error de examen / Punto de confusión

- No elegir instruction-based fine-tuning si el enunciado no se centra en seguir instrucciones, sino en adaptar el modelo al estilo o dominio de un dataset existente.
- “Descripciones existentes del sitio”, “lenguaje del dominio” o “contenido similar al dataset” apuntan a domain adaptation fine-tuning.

## Continuous Pre-training

El **Continuous Pre-training** o entrenamiento previo continuo mejora modelos preentrenados usando **datos sin etiquetar**.

### Para qué sirve

Sirve para aportar conocimiento más profundo de un dominio:

- medicina;
- finanzas;
- derecho;
- datos clínicos;
- datos financieros.

La fuente indica que es aplicable a modelos **Amazon Titan Text Express y Lite**.

### Formato mental para recordarlo

Continuous Pre-training = **“lee mucho texto de mi dominio para entenderlo mejor”**.

En la fuente aparece como entradas simples:

```json
{"input": "<input text>"}
{"input": "AWS stands for Amazon Web Services"}
```

No necesita pares pregunta/respuesta. Usa texto sin etiquetar.

## Transfer Learning

El **Transfer Learning** consiste en reutilizar un modelo ya entrenado en una tarea para aplicarlo a una nueva tarea relacionada.

La fuente remarca dos ideas importantes:

- ahorra recursos al aprovechar conocimiento adquirido en el entrenamiento inicial;
- **Fine-Tuning es un tipo específico de Transfer Learning**.

### Cómo pensarlo en examen

Transfer Learning es el paraguas conceptual.

Fine-Tuning y Continuous Pre-training son formas más concretas de aprovechar un modelo ya entrenado.

Si el examen ofrece una opción más específica que encaja con el caso, elegí la específica.

## Fine-Tuning vs Continuous Pre-training

| Concepto | Usa datos | Objetivo | Pensalo como |
|---|---|---|---|
| Fine-Tuning | Datos con ejemplos `prompt` / `completion` | Adaptar el modelo a una tarea específica | “Respondé así” |
| Instruction-based fine-tuning | Instrucciones y respuestas esperadas | Mejorar seguimiento de instrucciones | “Seguí este formato/tarea” |
| Domain adaptation fine-tuning | Datos del dominio o estilo objetivo | Adaptar el modelo a un ámbito o dataset específico | “Hablá como este dominio” |
| Continuous Pre-training | Datos sin etiquetar | Profundizar conocimiento del dominio | “Leé más sobre este ámbito” |
| Transfer Learning | Modelo ya entrenado reutilizado | Ahorrar recursos y adaptar conocimiento previo | “Reutilizá lo aprendido” |

## RAG no es Fine-Tuning

RAG aparece cerca de estos temas, pero NO cambia el modelo.

- **RAG** recupera información externa y la agrega al prompt como contexto.
- El FM no se modifica.
- No requiere entrenamiento.
- Sirve cuando se necesita información contextual, privada o actualizada.

En la fuente de costes de Bedrock se diferencia así:

- Prompt Engineering: no requiere entrenamiento.
- RAG: el FM no cambia.
- Fine-Tuning basado en instrucciones: el FM se ajusta con instrucciones específicas.
- Fine-Tuning de adaptación de dominio: más computación para adaptar el FM.

## Hiperparámetros en el ajuste de modelos

Los **hiperparámetros** son configuraciones externas que controlan el comportamiento del modelo durante el entrenamiento.

La fuente destaca:

- **Learning Rate**: si es muy alta, el modelo aprende demasiado rápido y puede saltar a conclusiones equivocadas; si es muy baja, aprende muy lento.
- **Batch Size**: lotes grandes requieren más memoria y dan resultados más estables; lotes pequeños aprenden más rápido pero con resultados menos consistentes.
- **Epochs**: cuántas veces el modelo ve los datos; demasiadas épocas pueden causar sobreajuste.

## Overfitting y Underfitting en ajustes

Al ajustar un modelo, el objetivo no es memorizar el dataset, sino generalizar.

### Overfitting

El modelo se adapta demasiado a los datos de entrenamiento.

- Puede rendir bien en entrenamiento.
- Puede fallar en datos nuevos.
- Se asocia a alta varianza.
- Soluciones de fuente: simplificar el modelo, aplicar regularización o aumentar datos de entrenamiento.

#### Error de examen / Punto de confusión

- Si el modelo funciona bien con datos de entrenamiento pero mal con datos de prueba, pensar en overfitting.
- En términos de bias/variance, la pista es bajo sesgo en entrenamiento pero alta varianza o mayor variabilidad al generalizar.

### Underfitting

El modelo es demasiado simple para capturar las tendencias.

- Rinde mal incluso en entrenamiento.
- Se asocia a alto bias.
- Solución de fuente: incrementar la complejidad del modelo.

## Señales de examen

### Si ves “modelo preentrenado”

Pensá en reutilización, no en entrenamiento desde cero.

### Si ves “tarea específica”

Pensá en Fine-Tuning.

Ejemplos:

- resumir;
- Q&A;
- clasificación;
- generar respuestas con formato esperado.

### Si ves “datos sin etiquetar”

Pensá en Continuous Pre-training.

### Si ves “nuevo dominio”

Pensá en Continuous Pre-training o Domain adaptation fine-tuning según el tipo de dato:

- mucho texto sin etiquetar del dominio → Continuous Pre-training;
- ejemplos del estilo/salida que querés generar → Domain adaptation fine-tuning.

### Si ves “descripciones existentes del sitio”

Pensá en Domain adaptation fine-tuning.

El objetivo no es descubrir patrones sin etiquetas desde cero, sino adaptar un modelo preentrenado al estilo y dominio de las descripciones existentes.

## Mapa rápido de descarte

| Opción | Cuándo descartarla |
|---|---|
| Unsupervised pre-training | Si el modelo ya está preentrenado y no se pide entrenar desde cero con datos generales. |
| Transfer Learning | Si aparece una opción más específica como Fine-Tuning o Domain adaptation fine-tuning. |
| Domain adaptation fine-tuning | No descartarla si el caso habla de adaptar el modelo a datos, estilo o dominio propio. |
| Instruction-based fine-tuning | Descartarla si el foco no es seguir instrucciones, sino imitar/adaptarse a un dominio de datos. |

## Resumen para memorizar

- **Transfer Learning**: concepto general de reutilizar un modelo entrenado.
- **Fine-Tuning**: ajustar un modelo preentrenado para una tarea específica.
- **Instruction-based fine-tuning**: ajustar para seguir instrucciones y formatos.
- **Domain adaptation fine-tuning**: ajustar para un dominio, lenguaje o dataset específico.
- **Continuous Pre-training**: seguir preentrenando con datos sin etiquetar para profundizar conocimiento de dominio.
- **RAG**: agregar contexto externo sin cambiar el modelo.

## Preguntas de repaso activo

1. ¿Por qué Fine-Tuning no es lo mismo que entrenar un FM desde cero?
2. ¿Qué pista del enunciado te lleva a Continuous Pre-training?
3. ¿Por qué Transfer Learning puede ser demasiado general como respuesta de examen?
4. Si una empresa quiere generar descripciones parecidas a las de su catálogo existente, ¿qué enfoque conviene?
5. ¿Cuál es la diferencia clave entre RAG y Fine-Tuning?
