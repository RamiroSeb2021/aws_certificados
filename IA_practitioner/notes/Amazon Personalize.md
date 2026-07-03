# Amazon Personalize

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Qué es

- Servicio para construir aplicaciones con recomendaciones personalizadas en tiempo real.
- Fuente indica que amazon.com lo usa para personalizar experiencia de clientes.
- Se integra en sitios web existentes, aplicaciones, SMS y sistemas de marketing por correo electrónico.

## Casos de uso

- Recomendaciones de productos basadas en historial de compras.
- Personalización de contenido y sugerencias de consumo para usuarios.

## Recomendaciones y similitud vectorial

- Amazon Personalize se enfoca en recomendaciones personalizadas usando comportamiento, historial e interacciones de usuarios.
- Si además el escenario pide búsqueda eficiente por similitud entre contenidos, puede aparecer Amazon OpenSearch Service como base para búsqueda vectorial.
- Personalize responde “qué recomendar a este usuario”; OpenSearch vectorial responde “qué elementos son similares a este contenido/embedding”.
- Amazon Neptune modela grafos y relaciones; no es la primera opción cuando la pista explícita es búsqueda vectorial para contenido similar.

## Claves de examen

- Personalize = recomendaciones personalizadas.
- Si escenario habla de historial, preferencias, productos o contenido recomendado: Amazon Personalize.
- Si escenario combina recomendación personalizada + similitud vectorial, pensar en Personalize + OpenSearch Service.
