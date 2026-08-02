# Amazon Aurora

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 170–174.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 5: Amazon Aurora.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) y [Aurora endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html).
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
- **Aurora:** motor de base de datos relacional creado por AWS, compatible con determinadas versiones de MySQL y PostgreSQL.
  - **Ejemplo:** una aplicación que usa un controlador MySQL compatible puede conectarse a un clúster Aurora MySQL.
- **RDS — Amazon Relational Database Service:** plataforma administrada bajo la que se opera Amazon Aurora.
  - **Ejemplo:** Aurora utiliza interfaces de administración de Amazon RDS.
- **Clúster:** conjunto coordinado de almacenamiento y una o más instancias de base de datos.
  - **Ejemplo:** un clúster Aurora puede tener un writer y varias réplicas lectoras.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región.
  - **Ejemplo:** el almacenamiento de un clúster Aurora regional mantiene copias entre tres AZ.
- **Writer (escritor):** instancia que procesa las modificaciones de datos del clúster.
  - **Ejemplo:** una orden nueva se envía al writer endpoint.
- **Reader (lector):** réplica que puede procesar consultas de solo lectura.
  - **Ejemplo:** un reporte se conecta al reader endpoint para descargar trabajo del writer.
- **Endpoint:** nombre de conexión estable que dirige al rol o instancia adecuada.
  - **Ejemplo:** la aplicación configura el writer endpoint en vez del hostname de una instancia concreta.
- **Failover:** promoción de otra instancia para asumir el rol principal después de un fallo.
  - **Ejemplo:** si el writer falla, Aurora promueve una réplica y el endpoint dirige las conexiones al nuevo writer.
- **ms — milisegundo:** milésima parte de un segundo, utilizada para medir tiempos muy pequeños.
  - **Ejemplo:** `10 ms` equivale a `0,01` segundos.

## Idea central

Aurora separa el almacenamiento distribuido del cómputo de las instancias y ofrece endpoints por función para simplificar lectura, escritura y failover.

**Ejemplo integrador:** la aplicación escribe pedidos mediante el writer endpoint y ejecuta reportes mediante el reader endpoint. Si cambia el writer, la aplicación conserva el mismo nombre de conexión.

## Qué es Amazon Aurora

- Tecnología propietaria de AWS compatible con controladores PostgreSQL y MySQL.
- La fuente afirma rendimiento hasta 5 veces el de MySQL en RDS y más de 3 veces el de PostgreSQL en RDS.
- El almacenamiento crece automáticamente en incrementos de 10 GB hasta 256 TB.
- Puede tener hasta 15 réplicas con retraso de replicación indicado como inferior a 10 ms.
- La fuente indica un coste 20 % superior a RDS, compensado por mayor eficiencia.

## Alta disponibilidad

- Mantiene 6 copias de los datos en 3 AZ.
- Necesita 4 de 6 copias para escrituras y 3 de 6 para lecturas.
- Incluye autorreparación mediante replicación entre pares.
- Una instancia writer realiza escrituras; el writer y hasta 15 réplicas realizan lecturas.
- Recuperación automática del writer en menos de 30 segundos, según fuente.

## Endpoints

- **Writer endpoint:** apunta a la instancia principal de escritura.
- **Reader endpoint:** actúa como conexión balanceada hacia las réplicas.
- El escalado automático puede añadir réplicas cuando aumenta la carga de lectura.

## Por qué es importante

- Aurora integra almacenamiento distribuido, alta disponibilidad, failover y escalado de lectura como propiedades del clúster.
- No hay que confundir “compatible con MySQL/PostgreSQL” con que Aurora sea esos motores sin cambios: es una tecnología propia que expone compatibilidad.
