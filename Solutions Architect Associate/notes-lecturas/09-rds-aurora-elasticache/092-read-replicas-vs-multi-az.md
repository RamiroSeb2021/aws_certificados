# RDS Read Replicas vs Multi-AZ

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 164–168.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 2: Réplicas de lectura RDS vs Multi AZ.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## ¿Qué es exactamente una réplica de lectura?

Una réplica de lectura es otra instancia de base de datos que recibe una copia de los cambios de la instancia principal. La aplicación escribe en la principal y puede enviar consultas de lectura a las réplicas para descargar trabajo de lectura.

- La replicación es asíncrona (`ASYNC`), por lo que la réplica puede ir ligeramente retrasada: las lecturas son finalmente consistentes.
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
