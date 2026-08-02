# Tipos de volúmenes EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 104–108.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 8: Tipos de volúmenes EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html).
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
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques para EC2.
  - **Ejemplo:** una base de datos puede guardar sus archivos en un volumen EBS.
- **SSD — Solid-State Drive (unidad de estado sólido):** almacenamiento optimizado para operaciones frecuentes y baja latencia.
  - **Ejemplo:** `gp3` e `io2` son familias SSD de EBS.
- **HDD — Hard Disk Drive (unidad de disco duro):** almacenamiento orientado a grandes flujos secuenciales y menor coste.
  - **Ejemplo:** `st1` es apropiado para leer grandes archivos de registros de forma continua.
- **IOPS — Input/Output Operations Per Second:** número de operaciones de lectura o escritura por segundo.
  - **Ejemplo:** muchas consultas pequeñas de base de datos necesitan IOPS, no solo transferencia de archivos grandes.
- **PIOPS — Provisioned IOPS (IOPS aprovisionadas):** rendimiento de operaciones configurado explícitamente para el volumen.
  - **Ejemplo:** un volumen `io2` puede aprovisionarse para una carga que necesita rendimiento sostenido.
- **Throughput (rendimiento de transferencia):** cantidad total de datos transferidos por segundo.
  - **Ejemplo:** procesar archivos de varios gigabytes depende mucho del throughput.
- **GiB/TiB:** gibibyte y tebibyte, unidades binarias de capacidad.
  - **Ejemplo:** `1 TiB` equivale a `1024 GiB`.
- **MiB/s:** mebibytes por segundo, unidad binaria de transferencia.
  - **Ejemplo:** `500 MiB/s` expresa cuánto dato puede moverse por segundo.
- **Volumen de arranque:** disco que contiene el sistema operativo con el que inicia la instancia.
  - **Ejemplo:** el volumen raíz de Linux es un volumen de arranque.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que utilizan los volúmenes EBS.
  - **Ejemplo:** una instancia EC2 inicia desde un volumen `gp3`.

## Idea central

No existe un tipo EBS universalmente mejor: se elige según operaciones pequeñas, transferencia secuencial, latencia, durabilidad y coste.

**Ejemplo integrador:** un servidor general puede usar `gp3`; una base de datos crítica con IOPS sostenidas puede usar `io2`; un procesamiento secuencial de registros puede usar `st1`; datos fríos pueden usar `sc1`.

> **Complemento oficial de AWS:** las cifras del documento fuente pueden quedar desactualizadas. La tabla oficial actual permite, por ejemplo, valores superiores para `gp3` frente a los indicados en el curso. Para decisiones reales, use siempre los límites vigentes de la documentación enlazada.

## Tipos de volúmenes EBS

- Tipos mencionados:
  - `gp2` / `gp3` SSD: propósito general, equilibrio precio/rendimiento para variedad de cargas.
  - `io1` / `io2` SSD: mayor rendimiento para cargas de misión crítica con baja latencia o alto rendimiento.
  - `st1` HDD: bajo coste para cargas de acceso frecuente y alto rendimiento.
  - `sc1` HDD: HDD más barato para acceso menos frecuente.
- Se caracterizan por tamaño, rendimiento e IOPS.
- La fuente recomienda consultar documentación AWS en caso de duda.
- Solo `gp2/gp3` e `io1/io2` pueden usarse como volúmenes de arranque.

### Casos de uso por tipo

| Tipo | Datos de fuente |
| --- | --- |
| SSD propósito general | Rentable, baja latencia; volúmenes de arranque, escritorios virtuales, desarrollo y prueba; 1 GiB–16 TiB. |
| `gp3` | Base de 3.000 IOPS y 125 MiB/s; puede aumentar IOPS hasta 16.000 y rendimiento hasta 1000 MiB/s independientemente. |
| `gp2` | Volúmenes pequeños pueden usar ráfagas de IOPS hasta 3.000; tamaño e IOPS vinculados; IOPS máximas 16.000; 3 IOPS por GB, con 5.334 GB se llega al máximo. |
| PIOPS SSD `io1/io2` | Aplicaciones críticas con IOPS sostenidas o más de 16.000 IOPS; excelente para bases de datos sensibles a rendimiento y consistencia. |
| `io1/io2` | 4 GiB–16 TiB; PIOPS máximos: 64.000 para Nitro y 32.000 para otras instancias; PIOPS independientes del tamaño; `io2` más durabilidad y más IOPS por GiB al mismo precio que `io1`. |
| `io2 Block Express` | 4 GiB–64 TiB; latencia menor a un milisegundo; PIOPS máximas 256.000 con relación IOPS:GiB de 1.000:1. |
| HDD `st1` | No puede ser volumen de arranque; 125 GiB–16 TiB; Big Data, data warehouses, procesamiento de logs; rendimiento máximo 500 MiB/s e IOPS máximo 500. |
| HDD `sc1` | Datos de acceso poco frecuente; menor coste; rendimiento máximo 250 MiB/s e IOPS máximas 250. |
