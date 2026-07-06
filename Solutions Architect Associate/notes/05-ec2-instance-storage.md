# Almacenamiento de instancias EC2

> Fuente: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
> Páginas fuente: 93–117
> Índice Udemy relacionado: sección 7 `Almacenamiento de instancias EC2`
> Método: extracción local con `pdftotext -layout`.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Se mantiene el contraste entre EBS, snapshots, AMI, EC2 Instance Store y EFS.
- Se conservan valores de tamaño, IOPS, rendimiento, porcentajes y límites presentes en fuente.
- Las comparaciones se estructuran en tablas cuando la fuente ya compara explícitamente conceptos.

## Amazon EBS

### Qué es un volumen EBS

- `Elastic Block Store` es una unidad de red que se puede adjuntar a instancias mientras se ejecutan.
- Permite persistir datos incluso después de finalizar instancias.
- A nivel CCP, solo puede montarse en una instancia a la vez.
- Está vinculado a una zona de disponibilidad específica.
- Analogía fuente: “memoria USB de red”.
- Nivel gratuito mencionado: 30 GB mensuales de EBS de tipo Propósito General SSD o Magnético.

### Características del volumen EBS

- No es unidad física; usa red para comunicarse con la instancia y puede tener algo de latencia.
- Se puede separar de una instancia EC2 y conectar a otra rápidamente.
- Está bloqueado en una AZ; un volumen en `us-east-1a` no puede adjuntarse a `us-east-1b`.
- Para trasladar un volumen, primero hay que crear un snapshot.
- Tiene capacidad aprovisionada: tamaño en GB e IOPS.
- Se factura toda capacidad aprovisionada.
- Puede aumentar capacidad con el tiempo.

### Atributo “Borrar al terminar”

- Controla comportamiento de EBS cuando termina una instancia EC2.
- Por defecto, el volumen EBS root se elimina.
- Por defecto, otros volúmenes EBS adjuntos no se eliminan.
- Se puede controlar desde consola AWS o AWS CLI.
- Caso de uso: preservar volumen root cuando termina la instancia.

## Snapshots de EBS

- Snapshot es una copia de seguridad de un volumen EBS en un momento dado.
- No es necesario separar el volumen para crear snapshot, pero se recomienda.
- Se pueden copiar snapshots entre AZ o regiones.

### Características de snapshots

- Archivo de snapshots EBS:
  - permite mover un snapshot a un nivel de archivo de menor costo, 75% más barato según la fuente;
  - restauración del archivo tarda entre 24 y 72 horas.
- Papelera de reciclaje para snapshots EBS:
  - permite configurar reglas para retener snapshots eliminados;
  - ayuda a recuperarlos tras borrado accidental;
  - retención especificable de 1 día a 1 año.

## AMI

- AMI significa `Amazon Machine Image`.
- Es una personalización de instancia EC2.
- Puede incluir software, configuración, sistema operativo y monitorización propios.
- Mejora tiempo de arranque/configuración porque el software está preempaquetado.
- Se construye para una región específica y puede copiarse entre regiones.
- Se pueden lanzar instancias EC2 desde:
  - AMI pública proporcionada por AWS;
  - AMI propia creada y mantenida por el usuario;
  - AMI de AWS Marketplace hecha por otra persona y potencialmente vendida.

### Proceso AMI desde instancia EC2

1. Iniciar instancia EC2 y personalizarla.
2. Detener instancia para integridad de datos.
3. Construir AMI; esto también crea snapshots EBS.
4. Lanzar instancias desde otras AMIs.

## EC2 Instance Store

- EBS ofrece unidades de red con rendimiento bueno pero limitado.
- Para disco de hardware de alto rendimiento, la fuente usa EC2 Instance Store.
- Ofrece mejor rendimiento de E/S e IOPS muy altas.
- Pierde almacenamiento si la instancia se detiene; es efímero.
- Bueno para buffer, caché, datos de memoria virtual y contenido temporal.
- Hay riesgo de pérdida de datos si falla el hardware.
- Backups y replicación son responsabilidad del usuario.

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

## EBS Multi-Attach

- Aplica a familia `io1/io2`.
- Adjunta el mismo volumen EBS a varias instancias EC2 en la misma AZ.
- Cada instancia tiene permisos completos de lectura y escritura.
- Caso de uso: mayor disponibilidad de aplicaciones en clusters Linux, por ejemplo Teradata.
- Las aplicaciones deben gestionar escrituras concurrentes.
- Hasta 16 instancias EC2 a la vez.
- Debe usarse sistema de archivos compatible con clúster; la fuente indica “no XFS, EX4, etc.”.

## Cifrado de EBS

Al crear un volumen EBS cifrado:

- Datos en reposo se cifran dentro del volumen.
- Datos en movimiento entre instancia y volumen se cifran.
- Snapshots quedan cifrados.
- Volúmenes creados desde snapshot quedan cifrados.
- Cifrado y descifrado son transparentes.
- Impacto mínimo en latencia.
- Usa claves KMS con AES-256.
- Copiar un snapshot no cifrado permite cifrado.
- Snapshots de volúmenes cifrados están cifrados.

### Cifrar un volumen EBS existente

1. Crear snapshot del volumen EBS.
2. Cifrar snapshot mediante copia.
3. Crear nuevo volumen EBS desde snapshot; el volumen queda cifrado.
4. Adjuntar volumen cifrado a instancia original.

## Amazon EFS

- `Elastic File System` es NFS gestionado que puede montarse en muchas EC2.
- Funciona con instancias EC2 en multi-AZ.
- Fuente lo describe como alta disponibilidad, escalable, caro —3x `gp2`— y pago por uso.
- Casos de uso: gestión de contenidos, servicio web, intercambio de datos, WordPress.
- Usa protocolo NFSv4.1.
- Usa grupo de seguridad para controlar acceso.
- Compatible con AMI basadas en Linux, no Windows.
- Cifrado en reposo mediante KMS.
- Sistema de archivos POSIX similar a Linux con API estándar de archivos.
- Escala automáticamente y no requiere planificar capacidad.

### Rendimiento y almacenamiento EFS

- Escala a miles de clientes NFS concurrentes y 10 GB+/s de rendimiento.
- Crece automáticamente hasta escala de petabytes.
- Modos de rendimiento definidos al crear EFS:
  - Propósito general: predeterminado, sensible a latencia, por ejemplo servidor web o CMS.
  - E/S máxima: mayor latencia, más rendimiento, altamente paralelo, por ejemplo Big Data o procesamiento de medios.
- Modos de throughput:
  - Ráfaga: `1 TB = 50 MiB/s + ráfaga hasta 100 MiB/s`.
  - Aprovisionado: fija rendimiento independientemente del tamaño, por ejemplo `1 GiB/s` para `1 TB`.
- Clases de almacenamiento:
  - Estándar: archivos de acceso frecuente.
  - EFS-IA: coste de recuperación, menor precio de almacenamiento, habilitable con política de ciclo de vida.
- Disponibilidad y durabilidad:
  - Estándar: Multi-AZ, ideal para producción.
  - One Zone: una AZ, útil para desarrollo, backup activado por defecto, compatible con EFS One Zone-IA.
- La fuente menciona más de 90% de ahorro de costes.

## EBS vs EFS vs Instance Store

| Servicio | Recordatorio de fuente |
| --- | --- |
| EBS | Volúmenes adjuntos a una instancia a la vez; bloqueados a AZ; migración entre AZ mediante snapshot y restauración; backups consumen IO y no deberían ejecutarse con mucho tráfico; root EBS se termina por defecto si instancia se termina, salvo desactivación. |
| EFS | Puede montarse en cientos de instancias a través de AZ; comparte archivos de sitio web como WordPress; solo Linux/POSIX; precio más elevado que EBS; puede usar EFS-IA para ahorrar costes. |
| EC2 Instance Store | Alto rendimiento local; efímero; útil para caché, buffer y temporales; backups y replicación a cargo del usuario. |

## Claves de repaso

- EBS es almacenamiento de red por AZ; para moverlo entre AZ, usar snapshot.
- Root EBS se borra por defecto al terminar instancia; volúmenes adicionales no.
- Snapshots permiten copia entre AZ/región y opciones de archivo/recycle bin.
- AMI empaqueta configuración/software y crea snapshots EBS durante su construcción.
- Instance Store da alto rendimiento local, pero es efímero.
- EFS es NFS gestionado multi-AZ para muchas EC2 Linux, más caro que EBS y escalable automáticamente.

## Caveats de extracción

- La página 108 solo contiene enlace de resumen AWS; no se expandió con documentación externa.
- La fuente usa “EX4” en la advertencia de Multi-Attach; se preserva tal como aparece, aunque puede requerir revisión manual.
- Varias páginas incluyen diagramas de AZ y montaje; se preserva significado textual, no el diseño visual.
