# Amazon Aurora — conceptos avanzados

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 175–179.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 7: Amazon Aurora - Conceptos avanzados.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Aurora endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html), [Aurora serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html), [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) y [Aurora machine learning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-ml.html).
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo desde fundamentos.
- Cada concepto nuevo incluye una explicación sencilla y un ejemplo inmediato.
- Las siglas se desarrollan y explican en su primera aparición conceptual.
- Los límites y cifras del curso se preservan como contenido de la fuente y pueden cambiar; los complementos actuales se identifican por separado.

## Antes de empezar: conceptos y siglas

- **AWS — Amazon Web Services:** proveedor de servicios de nube utilizado en estas notas.
  - **Ejemplo:** AWS opera servicios de computación, almacenamiento, bases de datos y redes.
- **Endpoint:** nombre estable mediante el que una aplicación se conecta a un destino o grupo de destinos.
  - **Ejemplo:** un endpoint personalizado puede dirigir consultas analíticas a réplicas grandes.
- **Serverless:** modelo en el que el servicio administra la capacidad subyacente y la ajusta dentro de la configuración permitida; no significa que no existan servidores.
  - **Ejemplo:** Aurora Serverless aumenta capacidad cuando crece la carga sin que el cliente cambie manualmente la clase de instancia.
- **Proxy:** intermediario que recibe conexiones del cliente y las administra hacia el destino real.
  - **Ejemplo:** la aplicación se conecta a un proxy y este reutiliza conexiones hacia la base de datos.
- **DR — Disaster Recovery (recuperación ante desastres):** capacidad para recuperar el servicio después de una interrupción grave.
  - **Ejemplo:** una región secundaria de Aurora Global Database puede promoverse durante un desastre regional.
- **RTO — Recovery Time Objective (objetivo de tiempo de recuperación):** tiempo máximo objetivo para restaurar el servicio.
  - **Ejemplo:** un RTO de un minuto expresa la meta de recuperar operación dentro de ese intervalo.
- **SQL — Structured Query Language:** lenguaje de bases de datos relacionales.
  - **Ejemplo:** una consulta SQL puede solicitar una predicción integrada mediante Aurora Machine Learning.
- **ML — Machine Learning (aprendizaje automático):** técnicas que permiten a un modelo producir predicciones a partir de datos.
  - **Ejemplo:** un modelo puede estimar riesgo de fraude para una transacción.
- **T-SQL — Transact-SQL:** extensión de SQL utilizada por Microsoft SQL Server.
  - **Ejemplo:** Babelfish permite que ciertas aplicaciones envíen comandos T-SQL a Aurora PostgreSQL.
- **AWS SCT — AWS Schema Conversion Tool:** herramienta que ayuda a convertir esquemas y código de base de datos entre motores.
  - **Ejemplo:** convierte parte de un esquema de SQL Server hacia PostgreSQL.
- **AWS DMS — AWS Database Migration Service:** servicio para mover y replicar datos entre almacenes compatibles.
  - **Ejemplo:** copia datos desde la base de origen hacia Aurora durante una migración.

- **RDS — Amazon Relational Database Service:** plataforma administrada de bases de datos que incluye servicios como Aurora y RDS Proxy.
  - **Ejemplo:** una aplicación Aurora puede utilizar RDS Proxy para agrupar conexiones en una configuración compatible.

## Idea central

Estas funciones resuelven problemas distintos: endpoints separan cargas, Serverless ajusta capacidad, Global Database extiende el clúster entre regiones y Machine Learning conecta consultas con predicciones.

**Ejemplo integrador:** una aplicación usa el writer endpoint para operaciones normales, un endpoint personalizado para análisis y una región secundaria para recuperación ante desastres.

> **Complemento oficial de AWS:** la explicación de “flota de proxies” del documento fuente corresponde al modelo histórico de Aurora Serverless v1. Aurora Serverless v2 escala la capacidad de writers y readers dentro de un rango de ACU; puede combinarse con RDS Proxy, pero no debe explicarse como el mismo mecanismo.

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
