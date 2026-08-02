# Amazon RDS Proxy

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 185.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 10: Proxy RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [RDS Proxy concepts and terminology](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html).
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
- **Proxy:** intermediario entre la aplicación y la base de datos.
  - **Ejemplo:** la aplicación abre una conexión al proxy en vez de conectarse directamente al writer.
- **Conexión de base de datos:** canal mantenido entre un cliente y el motor para enviar operaciones y recibir respuestas.
  - **Ejemplo:** cada ejecución de una función podría abrir una conexión nueva si no existe un proxy.
- **Connection pooling (agrupación de conexiones):** mantenimiento y reutilización de conexiones existentes.
  - **Ejemplo:** cien solicitudes de aplicación pueden compartir un número menor de conexiones subyacentes en momentos diferentes.
- **Multiplexación:** reutilización organizada de una conexión subyacente para operaciones de distintos clientes cuando es seguro hacerlo.
  - **Ejemplo:** el proxy ejecuta una transacción y después reutiliza la conexión para otra sesión compatible.
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** RDS Proxy dirige conexiones a la instancia RDS apropiada.
- **Lambda — AWS Lambda:** servicio que ejecuta código en respuesta a eventos sin que el cliente administre servidores.
  - **Ejemplo:** muchas invocaciones simultáneas pueden intentar abrir conexiones a la misma base.
- **Serverless:** modelo donde AWS administra y escala la infraestructura del servicio.
  - **Ejemplo:** la capacidad de RDS Proxy se ajusta con la carga sin elegir servidores del proxy.
- **AZ — Availability Zone:** Zona de Disponibilidad aislada dentro de una región.
  - **Ejemplo:** la infraestructura del proxy se despliega de forma altamente disponible entre varias AZ.
- **IAM — AWS Identity and Access Management:** servicio de identidades y permisos.
  - **Ejemplo:** el proxy puede exigir autenticación IAM en configuraciones compatibles.
- **VPC — Virtual Private Cloud:** red virtual aislada controlada por el cliente en AWS.
  - **Ejemplo:** la aplicación accede al proxy dentro de la VPC.

- **CPU — Central Processing Unit:** capacidad de procesamiento utilizada para ejecutar operaciones.
  - **Ejemplo:** reducir la creación de conexiones deja más CPU de la base disponible para consultas.

## Idea central

RDS Proxy administra conexiones; no copia datos ni reemplaza el diseño de réplicas.

**Ejemplo integrador:** mil invocaciones Lambda se conectan al endpoint del proxy. El proxy comparte conexiones hacia RDS y reduce la presión de memoria y CPU provocada por abrir conexiones nuevas.

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
