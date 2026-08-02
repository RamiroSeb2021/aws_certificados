# Visión general de Amazon RDS y autoescalado de almacenamiento

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 161–163.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 1: Visión general de Amazon RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/what-is-rds.html) y [RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html).
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
- **Base de datos:** sistema organizado para almacenar y consultar información.
  - **Ejemplo:** una tienda guarda clientes, pedidos y productos en una base de datos.
- **Base de datos relacional:** organiza datos en tablas relacionadas mediante columnas y claves.
  - **Ejemplo:** una tabla `pedidos` puede relacionarse con una tabla `clientes` mediante un identificador.
- **SQL — Structured Query Language (lenguaje de consulta estructurado):** lenguaje utilizado para definir, consultar y modificar datos relacionales.
  - **Ejemplo:** `SELECT * FROM productos` solicita filas de la tabla `productos`.
- **RDS — Amazon Relational Database Service:** servicio administrado para ejecutar motores de bases de datos relacionales.
  - **Ejemplo:** RDS puede operar una base PostgreSQL sin que el cliente instale el sistema operativo del servidor.
- **Motor de base de datos:** software que almacena y procesa los datos.
  - **Ejemplo:** PostgreSQL, MySQL y Oracle son motores diferentes.
- **Servicio administrado:** servicio donde AWS asume tareas operativas definidas, mientras el cliente sigue diseñando y usando la base.
  - **Ejemplo:** AWS aplica mantenimiento de infraestructura, pero el cliente decide tablas, consultas y permisos de sus usuarios.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales.
  - **Ejemplo:** al instalar una base en EC2, el cliente administra más aspectos del sistema operativo que en RDS estándar.
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques usado bajo ciertas configuraciones de RDS.
  - **Ejemplo:** el almacenamiento de una instancia RDS puede crecer mediante Storage Autoscaling.
- **SSH — Secure Shell:** protocolo de acceso remoto cifrado.
  - **Ejemplo:** RDS estándar no permite iniciar una sesión SSH en el servidor subyacente.
- **CPU — Central Processing Unit:** capacidad de procesamiento utilizada por la base.
  - **Ejemplo:** aumentar almacenamiento no aumenta automáticamente la CPU disponible para ejecutar consultas.

- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región de AWS.
  - **Ejemplo:** una implementación Multi-AZ coloca componentes en zonas distintas.

## Idea central

RDS administra la infraestructura y tareas repetitivas del motor; el cliente continúa siendo responsable del diseño de datos, consultas, acceso y capacidad adecuada.

**Ejemplo integrador:** una tienda crea PostgreSQL en RDS. AWS gestiona backups y mantenimiento; el equipo crea las tablas. Si queda poco espacio, Storage Autoscaling puede aumentar el almacenamiento hasta el máximo configurado.

> **Complemento oficial de AWS:** la lista de motores y capacidades cambia. La documentación actual incluye opciones no reflejadas en el documento fuente, como Amazon RDS for Db2 en regiones compatibles.

## Qué es Amazon RDS

- RDS significa `Relational Database Service`.
- Es un servicio administrado para bases de datos relacionales que utilizan SQL.
- Motores mencionados: PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server y Aurora.

## RDS administrado vs base de datos en EC2

- RDS automatiza aprovisionamiento y parcheo del sistema operativo.
- Ofrece copias continuas y restauración a un punto en el tiempo.
- Incluye dashboards de monitorización, réplicas de lectura, Multi-AZ, ventanas de mantenimiento y escalado.
- El almacenamiento se respalda con EBS, según la fuente `gp2` o `io1`.
- En RDS estándar no se accede por SSH a la instancia subyacente.

## Autoescalado de almacenamiento

- Aumenta dinámicamente el almacenamiento cuando RDS detecta poco espacio libre.
- Se define un umbral máximo para limitar el crecimiento.
- La fuente indica que modifica el almacenamiento si:
  - queda menos del 10 % del almacenamiento asignado;
  - esa condición dura al menos 5 minutos;
  - han pasado 6 horas desde la última modificación.
- Es útil para cargas imprevisibles y soporta los motores RDS enumerados en la diapositiva.

## Claves de repaso

- RDS reduce trabajo operativo; no elimina la necesidad de diseñar motor, capacidad, disponibilidad y seguridad.
- Autoescalado de almacenamiento aumenta espacio, no capacidad de CPU ni número de réplicas.
