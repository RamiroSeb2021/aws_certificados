# Fundamentos de Prompt Engineering

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Qué es

- Prompt: instrucción dada a un modelo de lenguaje para guiar respuesta o comportamiento.
- Prompt Engineering: disciplina para desarrollar y optimizar prompts.
- Ayuda a entender capacidades y limitaciones de LLM.

## Elementos de un prompt

- Contexto: información externa o adicional que dirige mejores respuestas.
- Datos de entrada: entrada sobre la que se desea respuesta.
- Instrucción: tarea específica que debe realizar el modelo.
- Indicador de salida: tipo o formato esperado.
- No todos los componentes son necesarios en todos los prompts.

## Optimización

- Prompts simples pueden funcionar, pero resultados dependen de información y diseño.
- Prompt optimizado guía al LLM para respuestas más relevantes y precisas.
- Buen prompt puede incluir instrucciones, contexto, datos de entrada e indicador de salida.

## Prompting negativo

- Técnica para indicar qué evitar al generar contenido.
- Funciona junto con instrucciones positivas.
- Reduce iteraciones al eliminar desde inicio elementos no deseados.
- Ejemplos fuente: evitar tecnicismos, descripciones largas o detalles avanzados.

## Técnicas de prompting

- Zero-shot: tarea sin ejemplos previos.
- Few-shot: algunos ejemplos; un ejemplo = one-shot/single-shot.
- Chain of Thought (CoT): razonamiento paso a paso para tareas complejas.
- Otras técnicas listadas: auto-consistencia, conocimiento generado, prompt chaining, Tree of Thoughts, RAG, ReAct, Reflexion, CoT multimodal, prompt de grafo, entre otras.

## Configuraciones del prompt

- System prompt: define comportamiento del modelo.
- Temperatura (0 a 1): creatividad y diversidad.
- Top P (0 a 1): selección entre palabras más probables; valores altos permiten variedad.
- Top K: limita número de opciones; valores bajos generan respuestas más coherentes.
- Longitud máxima: tamaño máximo de respuesta.
- Secuencias de detención: cuándo detener generación.

### Parámetros de inferencia: cómo no confundirlos

- **Top K** limita el número de tokens candidatos que el modelo puede considerar para la próxima palabra.
- **Top P** limita por probabilidad acumulada: el modelo considera el conjunto mínimo de tokens cuya probabilidad suma el umbral definido.
- **Temperatura** controla aleatoriedad: baja = respuestas más deterministas; alta = más variación.
- **Secuencias de detención** no hacen la respuesta más creativa ni más precisa; solo indican dónde cortar la generación.
- Para respuestas más predecibles, pensar en temperatura baja y Top P bajo; Top K bajo también ayuda, pero no reemplaza el control de aleatoriedad.

## Latencia

- Latencia = tiempo de procesamiento y respuesta.
- Factores que afectan: tamaño de modelo, tipo de modelo, tokens de entrada y tokens de salida.
- Fuente indica que Top P, Top K y temperatura no afectan latencia.

## Coste y tokens en prompts

- En modelos generativos, el coste suele estar muy ligado a tokens procesados: entrada + salida.
- Few-shot prompting aumenta calidad contextual, pero cada ejemplo adicional consume tokens.
- Para reducir coste mensual, primero revisar longitud del prompt, cantidad de ejemplos, contexto repetido y longitud esperada de respuesta.
- Provisioned Throughput conviene cuando se necesita capacidad estable o garantizada; no es la primera palanca para ahorrar en uso variable o bajo.

## Buenas prácticas

- Ser claro y específico.
- Indicar longitud deseada.
- Incluir contexto relevante.
- Evitar preguntas demasiado amplias.
- Especificar formato de respuesta.

## Riesgos y limitaciones

- Toxicidad: respuestas ofensivas o inapropiadas; depende de cultura y contexto.
- Alucinaciones: afirmaciones creíbles pero incorrectas o inventadas.
- Prompt injection: usuario malicioso manipula entrada para cambiar comportamiento.
- Exposure: modelo revela información sensible.
- Prompt leaking: divulgación no intencional de prompts o entradas internas.
- Jailbreaking: manipulación para ignorar medidas de seguridad.
- Poisoning: introducción de datos maliciosos o sesgados en entrenamiento.

### Riesgos de prompts y datos manipulados

- **Poisoning**: datos de entrenamiento, interacción o contexto fueron manipulados para alterar respuestas del modelo.
- **Jailbreaking**: usuario intenta que el modelo ignore restricciones o políticas.
- **Hijacking**: atacante secuestra la lógica de interacción para redirigir comportamiento hacia una intención maliciosa.
- **Exposure**: fuga o revelación de información sensible.
- Si el escenario habla de datos manipulados que influyen en respuestas incorrectas o peligrosas, la pista fuerte es poisoning; si habla de saltarse reglas, la pista fuerte es jailbreaking.

## Claves de examen

- Prompt Engineering no entrena modelo; diseña instrucciones.
- Zero-shot = sin ejemplos.
- Few-shot = con ejemplos.
- CoT = paso a paso.
- Top K = cantidad de candidatos; Top P = probabilidad acumulada; temperatura = aleatoriedad.
- Menos tokens = menor coste potencial en GenAI.
- Riesgos frecuentes: alucinación, inyección de prompt, fuga de prompts y jailbreaking.
