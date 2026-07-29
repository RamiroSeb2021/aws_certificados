# Amazon RDS Proxy

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 185.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 10: Proxy RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## ¿Qué es Amazon RDS Proxy?

Es un proxy de base de datos totalmente administrado. La aplicación se conecta al proxy; el proxy mantiene, agrupa y reutiliza conexiones hacia RDS o Aurora.

### Problema que resuelve

- Abrir demasiadas conexiones consume CPU y memoria de la base de datos.
- Cargas como AWS Lambda pueden crear muchos clientes concurrentes.
- RDS Proxy comparte conexiones existentes y reduce conexiones abiertas y tiempos de espera.

## Características de la fuente

- Serverless, autoescalable y altamente disponible en múltiples AZ.
- Reduce el tiempo de failover de RDS y Aurora hasta 66 %, según fuente.
- Soporta RDS para MySQL, PostgreSQL y MariaDB; y Aurora compatible con MySQL y PostgreSQL.
- Para la mayoría de aplicaciones no exige cambios de código.
- Aplica autenticación IAM y guarda credenciales en AWS Secrets Manager.
- No es accesible públicamente: se accede desde la VPC.

## Proxy vs réplica

- **Proxy:** administra conexiones; no crea una copia de los datos.
- **Read Replica:** mantiene una copia asíncrona para descargar lecturas.
- Pueden resolver problemas diferentes y no son sustitutos directos.
