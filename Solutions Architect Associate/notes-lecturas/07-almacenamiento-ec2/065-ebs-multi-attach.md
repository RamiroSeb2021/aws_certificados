# EBS Multi-Attach

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 109.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 9: Multi-Attach EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Attach an EBS volume to multiple EC2 instances using Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html).
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
  - **Ejemplo:** un volumen EBS puede contener datos compartidos por una aplicación de clúster.
- **Multi-Attach:** función que permite conectar un mismo volumen EBS compatible a varias instancias simultáneamente.
  - **Ejemplo:** dos nodos de una aplicación pueden ver el mismo volumen `io2`.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales de AWS.
  - **Ejemplo:** cada nodo del clúster puede ser una instancia EC2 distinta.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región.
  - **Ejemplo:** el volumen y todas las instancias conectadas mediante Multi-Attach deben estar en la misma AZ.
- **SSD — Solid-State Drive:** almacenamiento de estado sólido; `io1` e `io2` son tipos SSD con IOPS aprovisionadas.
  - **Ejemplo:** Multi-Attach no se activa en un volumen HDD `st1`.
- **Escritura concurrente:** situación en la que varias computadoras intentan modificar el almacenamiento al mismo tiempo.
  - **Ejemplo:** dos instancias actualizan simultáneamente el mismo archivo compartido.
- **Sistema de archivos de clúster:** sistema diseñado para coordinar el acceso simultáneo desde varios servidores.
  - **Ejemplo:** evita que dos nodos dañen las estructuras del disco al escribir a la vez.
- **XFS y EXT4:** sistemas de archivos habituales de Linux que no están diseñados por sí solos para acceso simultáneo desde varios servidores.
  - **Ejemplo:** montar el mismo EXT4 con lectura y escritura en dos instancias puede corromper datos.

- **HDD — Hard Disk Drive:** almacenamiento basado en discos magnéticos, no compatible con Multi-Attach.
  - **Ejemplo:** un volumen `st1` HDD no puede habilitar Multi-Attach.
- **IOPS — Input/Output Operations Per Second:** operaciones de lectura o escritura procesadas por segundo.
  - **Ejemplo:** `io2` permite aprovisionar IOPS para una carga crítica.
- **EXT4 — Fourth Extended Filesystem:** sistema de archivos común de Linux que no coordina por sí solo acceso simultáneo desde varios servidores.
  - **Ejemplo:** montar el mismo EXT4 con escritura en dos instancias puede dañar datos.

## Idea central

Multi-Attach comparte el dispositivo de bloques, pero NO coordina las escrituras de la aplicación.

**Ejemplo integrador:** tres nodos acceden al mismo volumen `io2`; la aplicación y el sistema de archivos de clúster deben ordenar las escrituras para mantener datos consistentes.

## EBS Multi-Attach

- Aplica a familia `io1/io2`.
- Adjunta el mismo volumen EBS a varias instancias EC2 en la misma AZ.
- Cada instancia tiene permisos completos de lectura y escritura.
- Caso de uso: mayor disponibilidad de aplicaciones en clusters Linux, por ejemplo Teradata.
- Las aplicaciones deben gestionar escrituras concurrentes.
- Hasta 16 instancias EC2 a la vez.
- Debe usarse sistema de archivos compatible con clúster; la fuente indica “no XFS, EX4, etc.”; `EX4` se conserva como errata de la fuente y se interpreta como `EXT4`.
