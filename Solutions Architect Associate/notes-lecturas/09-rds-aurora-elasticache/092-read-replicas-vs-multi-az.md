# RDS Read Replicas vs Multi-AZ

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 164–168.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 2: Réplicas de lectura RDS vs Multi AZ.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) y [Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).
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
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** una instancia RDS para PostgreSQL puede tener réplicas según el diseño elegido.
- **Réplica:** copia de datos mantenida a partir de una fuente principal.
  - **Ejemplo:** los cambios de la base principal se envían a otra instancia.
- **Read Replica (réplica de lectura):** copia destinada principalmente a atender consultas de lectura y descargar trabajo de la fuente.
  - **Ejemplo:** los reportes consultan la réplica mientras las compras escriben en la principal.
- **Replicación asíncrona:** la principal no espera a que la réplica aplique cada cambio antes de continuar.
  - **Ejemplo:** una compra recién guardada puede tardar un momento en aparecer en la réplica.
- **Consistencia eventual:** una copia puede estar temporalmente atrasada, pero converge si dejan de llegar cambios.
  - **Ejemplo:** un reporte puede mostrar durante unos segundos el total anterior.
- **Multi-AZ — múltiples Availability Zones:** implementación de alta disponibilidad que coloca componentes en Zonas de Disponibilidad distintas.
  - **Ejemplo:** si falla la AZ de la instancia principal, RDS puede cambiar a la instancia en espera.
- **Replicación síncrona:** la operación espera la confirmación requerida del destino antes de completarse.
  - **Ejemplo:** la implementación mantiene una copia de espera alineada para recuperación.
- **Failover (conmutación por error):** cambio hacia un recurso de reemplazo cuando el principal falla.
  - **Ejemplo:** el nombre DNS pasa a dirigir conexiones hacia la instancia en espera.
- **DNS — Domain Name System:** sistema que traduce nombres a direcciones de red.
  - **Ejemplo:** la aplicación conserva el endpoint de RDS aunque cambie la instancia activa.
- **DR — Disaster Recovery (recuperación ante desastres):** preparación para restaurar servicio y datos después de una interrupción grave.
  - **Ejemplo:** una réplica entre regiones puede formar parte de una estrategia de DR.

## Idea central

Read Replica responde principalmente a rendimiento de lectura; Multi-AZ responde principalmente a disponibilidad. Son objetivos diferentes.

**Ejemplo integrador:** el sitio envía `SELECT` de reportes a una Read Replica. La instancia principal también tiene una copia en espera Multi-AZ para failover; esa espera no se usa como réplica de lectura en la implementación Multi-AZ de instancia descrita por el curso.

> **Complemento oficial de AWS:** actualmente también existen clústeres Multi-AZ de RDS con dos instancias lectoras. No deben confundirse con la implementación Multi-AZ tradicional de una instancia principal y una espera no legible que compara el documento fuente.

## ¿Qué es exactamente una réplica de lectura?

Una réplica de lectura es otra instancia de base de datos que recibe una copia de los cambios de la instancia principal. La aplicación escribe en la principal y puede enviar consultas de lectura a las réplicas para descargar trabajo de lectura.

- La replicación es asíncrona (el curso la etiqueta `ASYNC`, abreviación de *asynchronous*), por lo que la réplica puede ir ligeramente retrasada: las lecturas son finalmente consistentes.
- La fuente indica hasta 15 réplicas, dentro de una AZ, entre AZ o entre regiones.
- Las réplicas sirven para `SELECT`; no para `INSERT`, `UPDATE` o `DELETE`.
- La aplicación debe usar la cadena de conexión de la réplica.
- Una réplica puede promoverse para convertirse en una base de datos independiente.

## Réplica de lectura vs Multi-AZ

| Aspecto | Réplica de lectura | Multi-AZ |
| --- | --- | --- |
| Objetivo | Escalar lecturas. | Alta disponibilidad y recuperación ante fallos. |
| Replicación | Asíncrona. | Síncrona. |
| Acceso de la aplicación | La aplicación usa endpoints/cadenas de conexión de lectura. | Un nombre DNS con failover automático hacia la instancia en espera. |
| Lecturas | Se usa para consultas de lectura. | La instancia en espera no se usa para escalar. |
| Fallo | Puede promoverse, pero no es el mecanismo descrito de failover automático. | Conmutación automática por pérdida de AZ, red, instancia o almacenamiento. |

## Caso de uso de la fuente

- Producción recibe carga normal.
- Una aplicación de reporting necesita ejecutar análisis.
- Se crea una réplica y el reporting consulta allí; la carga adicional no afecta a la principal.

## Conversión de Single-AZ a Multi-AZ

- Se modifica la base de datos sin detenerla.
- RDS toma un snapshot, restaura una base en otra AZ y establece replicación síncrona.

## Clave de examen

- **Read Replica = rendimiento de lectura.**
- **Multi-AZ = disponibilidad y disaster recovery.**
- Una Read Replica también debe configurarse como Multi-AZ si se quiere usar con el objetivo de DR indicado en la fuente.
