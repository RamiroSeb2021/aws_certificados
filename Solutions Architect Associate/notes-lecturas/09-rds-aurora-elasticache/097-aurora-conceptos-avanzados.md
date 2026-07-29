# Amazon Aurora — conceptos avanzados

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 175–179.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 7: Amazon Aurora - Conceptos avanzados.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Endpoints personalizados

- Agrupan un subconjunto de instancias Aurora.
- Caso de la fuente: dirigir consultas analíticas a réplicas de mayor capacidad.
- Tras definir endpoints personalizados, el Reader endpoint general puede dejar de usarse para esas consultas específicas.

## Aurora Serverless

- Instancia y escala automáticamente capacidad según uso real.
- Usa una flota de proxies administrada por Aurora entre cliente y capacidad de base de datos.
- Adecuado para cargas poco frecuentes, intermitentes o imprevisibles.
- No exige planificar capacidad y la fuente indica pago por segundo.

### ¿Qué es un proxy en este contexto?

Un proxy es una capa intermedia: la aplicación se conecta al proxy y el proxy administra cómo se conecta con las instancias reales de base de datos. Esto desacopla al cliente de una instancia concreta y permite que Aurora cambie o escale capacidad detrás de esa capa.

## Aurora Global

- Réplicas de lectura entre regiones para disaster recovery.
- Una región primaria de lectura/escritura.
- Hasta 10 regiones secundarias de solo lectura y hasta 16 réplicas por región secundaria, según fuente.
- La fuente indica replicación entre regiones inferior a 1 segundo y RTO de promoción inferior a 1 minuto.

## Aurora Machine Learning

- Permite obtener predicciones mediante consultas SQL.
- Integraciones mencionadas: Amazon SageMaker y Amazon Comprehend.
- Casos: fraude, anuncios, sentimiento y recomendaciones.

## Babelfish para Aurora PostgreSQL

- Permite que Aurora PostgreSQL entienda comandos destinados a Microsoft SQL Server, por ejemplo T-SQL.
- Busca reducir cambios de código al migrar aplicaciones SQL Server.
- La fuente relaciona la migración con AWS SCT y AWS DMS.
