# Amazon Lex & Connect

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.
- Se preserva agrupación del curso: Amazon Lex & Connect como tema conjunto.

## Amazon Lex

- Reconocimiento Automático de Voz (ASR): convierte habla en texto.
- Comprensión del Lenguaje Natural (NLU): reconoce intención detrás del texto y las llamadas.
- Se usa para construir interfaces conversacionales y bots de voz/texto.

## Amazon Connect

- Centro de contacto en la nube.
- Permite configurar y gestionar soluciones de atención al cliente.
- Proporciona herramientas para llamadas, chat, gestión de agentes y análisis de interacciones con clientes.

## Cómo trabajan juntos

- Amazon Connect gestiona la llamada o interacción del cliente.
- Amazon Lex interactúa con el usuario mediante ASR y NLU.
- AWS Lambda puede ejecutar lógica adicional, como consultar o modificar sistemas externos.
- Connect puede enviar confirmaciones por SMS u otros sistemas integrados.

## Ejemplo del curso

1. Usuario realiza llamada telefónica para solicitar reprogramación.
2. Amazon Connect gestiona la llamada y usa Amazon Lex para interactuar con usuario.
3. Consulta sobre programación activa función AWS Lambda.
4. Cuando se confirma nueva fecha, Amazon Connect envía mensaje de confirmación vía software de SMS.

## Amazon Q para Amazon Connect

- Permite gestionar interacciones de clientes mediante voz, chat y redes sociales.
- Amazon Q y Amazon Connect mejoran calidad de interacciones.
- Ofrecen respuestas automatizadas más precisas.

## Claves de examen

- Amazon Lex = bot conversacional con ASR + NLU.
- Amazon Connect = contact center cloud.
- Juntos cubren escenarios de atención al cliente automatizada.
- Si aparece llamada/chat + intención del usuario + centro de contacto, pensar en Lex & Connect.
