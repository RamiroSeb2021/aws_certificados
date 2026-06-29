# Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA

> Fuente: `AWS-AIF-C01-v4.pdf`.
> Extracción local desde PDF leído en el workspace.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Redacción, headings, casing y listas mejoradas.
- Enfoque de estudio para AWS Certified AI Practitioner.

## Conceptos fundamentales

### Seguridad en IA

- Protección contra amenazas, vulnerabilidades y accesos no autorizados.
- Asegura funcionamiento confiable y seguro.
- Evita riesgos que comprometan integridad o privacidad de datos.

### Gobernanza en IA

- Políticas, directrices y mecanismos de supervisión.
- Gestiona IA conforme a objetivos organizacionales.
- Mejora confianza y asegura aporte de valor.

### Responsabilidad en IA

- Desarrollo y uso transparente, justo y ético.
- Incluye evaluación de riesgos, mitigación de sesgos y prevención de daños no intencionados.
- Debe considerarse en diseño, desarrollo, despliegue, monitoreo y evaluación.

### Cumplimiento en IA

- Adhesión a leyes, normativas y estándares en sectores como salud, finanzas y legal.
- Garantiza operación dentro de marcos legales y éticos.

## Dimensiones de IA responsable

- Equidad.
- Capacidad de explicación.
- Privacidad y seguridad.
- Seguridad.
- Capacidad de control.
- Veracidad y solidez.
- Gobernanza.
- Transparencia.

### Error de examen / Punto de confusión

- En preguntas de GenAI, no confundir dimensiones generales de IA responsable con riesgos especialmente asociados a salidas generativas.
- Propiedad intelectual, toxicidad y alucinaciones aparecen como riesgos fuertes de GenAI porque el modelo puede generar contenido similar a material protegido, contenido dañino o afirmaciones plausibles pero incorrectas.
- Privacidad, seguridad, explicabilidad y transparencia siguen siendo importantes, pero pueden funcionar como categorías más generales según cómo esté redactado el escenario.

## Herramientas y servicios AWS

- Evaluaciones de modelos en Amazon Bedrock: comparar y seleccionar FM con métricas.
- Guardrails de Bedrock: evitar temas no deseados y filtrar contenido dañino.
- SageMaker Clarify: detectar/mitigar sesgos y explicar predicciones.
- SageMaker Model Monitor: detectar predicciones inexactas y problemas de modelo.
- Amazon Augmented AI: revisión humana cuando sea necesario.
- SageMaker: gobernanza de proyectos ML con control y visibilidad.

## AWS AI Service Cards y Responsible AI Policy

- AI Service Cards documentan casos de uso previstos, consideraciones de equidad, diseño responsable, mejores prácticas y rendimiento.
- Responsible AI Policy prohíbe usos como desinformación, violación de privacidad, suplantación, abuso o daños.
- Para decisiones importantes, se deben implementar guardrails y pruebas humanas.
- Usuarios son responsables de evaluar precisión y adecuación de salidas probabilísticas o inexactas.

## Cumplimiento normativo

- Fuente menciona estándares/regulaciones: ISO 42001, SOC 2, leyes de responsabilidad algorítmica, GDPR, EEOC y NIST.
- SageMaker Model Cards apoyan transparencia, cumplimiento y auditoría documentando origen de datos, fuentes, licencias, sesgos, pruebas y consideraciones.

### Error de examen / Punto de confusión

- Si el escenario pide documentar usos previstos, riesgos, entrenamiento, rendimiento o resultados de evaluación de un modelo, pensar en **SageMaker Model Cards**.
- No confundir con **SageMaker Model Monitor**, que vigila calidad, drift, sesgo y rendimiento en producción.
- No confundir con **AWS CloudTrail** o **AWS Config**: ayudan a auditar actividad/API o configuración de recursos, no a crear documentación específica del modelo.

## Gobernanza de datos

- Ciclo de vida de datos: creación, almacenamiento, uso/procesamiento, transferencia, archivado, eliminación.
- Registro: captura y almacenamiento de actividades/transacciones.
- Residencia de datos: almacenar en regiones que cumplen regulación local.
- Monitoreo: anomalías, acceso no autorizado y rendimiento.
- Análisis: patrones, tendencias y relaciones.
- Retención: conservar datos solo el tiempo necesario.

## Protocolos de gobernanza

- Políticas: administración de datos, entrenamiento, verificación, monitoreo, seguridad, mitigación de sesgos y privacidad.
- Cadencia de revisión: incluir expertos, legal, cumplimiento y usuarios finales.
- Estrategia de revisión: modelo, calidad de datos, robustez, políticas y requisitos regulatorios.
- Frameworks de gobernanza: directrices y mejores prácticas.
- Estándares de transparencia: documentar limitaciones, capacidades y casos de uso.
- Capacitación del equipo: sesgos y prácticas responsables.

## Seguridad y privacidad

- Defensa en profundidad: políticas, físico, perímetro, redes, hosts, aplicaciones y datos.
- Consideraciones: seguridad de aplicaciones, detección de amenazas, gestión de vulnerabilidades, infraestructura, prompt injection, cifrado en reposo y tránsito.
- IAM es fundamental para control de acceso y mínimo privilegio.
- GuardDuty ayuda a identificar y responder ataques.
- Cifrado en reposo protege datos almacenados; cifrado en tránsito protege datos entre sistemas.

## Servicios AWS para gobernanza

- AWS Config: audita y monitorea configuraciones.
- AWS Artifact: informes de cumplimiento y acuerdos legales.
- AWS Audit Manager: recopila evidencia para auditorías.
- AWS CloudTrail: registra actividad API.
- Amazon Inspector: análisis automatizado de vulnerabilidades.
- AWS Trusted Advisor: recomendaciones de seguridad, rendimiento y costes.

## Modelo de responsabilidad compartida y uso aceptable

- AWS: seguridad del cloud.
- Cliente: seguridad dentro del cloud.
- Política de uso aceptable prohíbe actividades ilegales, fraude, violación de derechos, violencia/terrorismo/daños graves, explotación infantil, ataques a seguridad/integridad/disponibilidad y spam.

## Claves de examen

- Clarify = sesgo + explicabilidad.
- Model Cards = documentación, transparencia y auditoría.
- Guardrails = control de GenAI.
- IAM/mínimo privilegio = acceso seguro.
- CloudTrail = actividad API; Config = configuración; Audit Manager = evidencia; Artifact = reportes/acuerdos.
