# Fundamentos de EC2

> Fuente: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
> Páginas fuente: 41–77
> Índice Udemy relacionado: sección 5 `Fundamentos de EC2`
> Método: extracción local con `pdftotext -layout`.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Se agrupan conceptos de EC2, tipos de instancia, seguridad, SSH y opciones de compra según el orden de las páginas fuente.
- Se conservan precios, porcentajes y caveats como aparecen en la fuente, marcándolos como ilustrativos cuando la fuente lo indica.
- Las tablas se usan solo para compactar comparaciones presentes en las diapositivas.

## Amazon EC2 como IaaS

- EC2 es una de las ofertas más populares de AWS.
- EC2 significa `Elastic Compute Cloud` y se presenta como Infraestructura como Servicio (IaaS).
- EC2 consiste principalmente en la capacidad de:
  - alquilar máquinas virtuales mediante EC2;
  - almacenar datos en unidades virtuales mediante EBS;
  - distribuir carga entre máquinas mediante ELB;
  - escalar servicios mediante Auto Scaling Group (ASG), también llamado grupo de autoescalado.
- Conocer EC2 es fundamental para entender el funcionamiento del Cloud.

## Tamaño y configuración de instancias EC2

Al lanzar una instancia EC2 se elige o configura:

- Sistema operativo: Linux, Windows o Mac OS.
- Potencia de cálculo y núcleos CPU.
- Memoria RAM.
- Almacenamiento:
  - conectado a red: EBS y EFS;
  - hardware: EC2 Instance Store.
- Tarjeta de red: velocidad e IP pública.
- Reglas de firewall: grupo de seguridad.
- Script de arranque: EC2 User Data.

### EC2 User Data

- Permite arrancar instancias con un script.
- `Bootstrapping` significa lanzar comandos cuando una máquina inicia.
- El script se ejecuta una sola vez en el primer arranque.
- Sirve para automatizar tareas de arranque:
  - instalar actualizaciones;
  - instalar software;
  - descargar archivos comunes de Internet;
  - otras tareas que se definan.
- Se ejecuta con usuario root.

## Tipos de instancias EC2

- AWS ofrece tipos de instancia optimizados para diferentes casos de uso.
- Convención de nombre de ejemplo: `m5.2xlarge`:
  - `m`: clase de instancia;
  - `5`: generación;
  - `2xlarge`: tamaño dentro de la clase.
- La fuente indica que listas de tipos evolucionan con el tiempo y recomienda consultar el sitio de AWS para información más reciente.

| Familia / foco | Uso según fuente |
| --- | --- |
| Propósito general | Diversidad de cargas como servidores web o repositorios de código; equilibrio entre computación, memoria y red. En el curso se usa `t2.micro`. |
| Computación optimizada | Procesamiento por lotes, transcodificación de medios, servidores web de alto rendimiento, HPC, modelado científico y aprendizaje automático, servidores de juegos. |
| Memoria optimizada | Grandes conjuntos de datos en memoria; bases de datos relacionales/no relacionales de alto rendimiento, cachés distribuidas, bases de datos en memoria para BI, procesamiento en tiempo real de grandes datos no estructurados. |
| Almacenamiento optimizado | Acceso alto y secuencial de lectura/escritura sobre grandes conjuntos de datos locales; OLTP de alta frecuencia, bases relacionales y NoSQL, caché para bases en memoria como Redis, aplicaciones de data warehouse y sistemas de archivos distribuidos. |

La fuente incluye una tabla de ejemplo con `t2.micro`, `t2.xlarge`, `c5d.4xlarge`, `r5.16xlarge` y `m5.8xlarge`, comparando vCPU, memoria, almacenamiento, rendimiento de red y ancho de banda EBS.

## Grupos de seguridad

- Son base de seguridad de red en AWS.
- Controlan cómo se permite tráfico dentro o fuera de instancias EC2.
- Solo contienen reglas de permiso.
- Sus reglas pueden referenciar IP o grupo de seguridad.
- Actúan como firewall en instancias EC2.
- Regulan:
  - acceso a puertos;
  - rangos IP autorizados IPv4 e IPv6;
  - red de entrada hacia la instancia;
  - red saliente desde la instancia.

### Detalles importantes

- Pueden adjuntarse a múltiples instancias.
- Están bloqueados a combinación de región y VPC.
- Viven “fuera” de EC2: si el tráfico está bloqueado, la instancia no lo ve.
- Es buena práctica mantener grupo de seguridad separado para acceso SSH.
- Si una aplicación no es accesible y hay timeout, la fuente lo asocia a problema de grupo de seguridad.
- Si hay “conexión rechazada”, la fuente lo asocia a error de aplicación o aplicación no lanzada.
- Todo tráfico de entrada está bloqueado por defecto.
- Todo tráfico de salida está autorizado por defecto.

### Puertos clásicos

| Puerto | Uso |
| ---: | --- |
| 22 | SSH para iniciar sesión en instancia Linux. |
| 21 | FTP para subir archivos a un archivo compartido. |
| 22 | SFTP para subir archivos usando SSH. |
| 80 | HTTP para sitios web no seguros. |
| 443 | HTTPS para sitios web seguros. |
| 3389 | RDP para iniciar sesión en instancia Windows. |

## SSH e Instance Connect

- SSH permite controlar una máquina remota usando línea de comandos.
- La fuente trata SSH como una función importante para instancias EC2.
- Para Linux / Mac OS X se menciona configuración de OpenSSH `~/.ssh/config`.
- Para Windows se menciona Putty.
- EC2 Instance Connect permite conectarse desde el navegador.
- Con EC2 Instance Connect no hace falta usar el archivo de claves descargado.
- La fuente explica que AWS carga temporalmente una clave en EC2.
- Funciona out-of-the-box solo con Amazon Linux 2.
- El puerto 22 debe seguir abierto.

### Solución de problemas SSH

- Si SSH no funciona, la fuente recomienda:
  - volver a ver la clase;
  - leer guía de solución de problemas;
  - probar EC2 Instance Connect.
- Si funciona alguno de los métodos —SSH, Putty o EC2 Instance Connect— es suficiente para el curso.
- Si no funciona ninguno, la fuente indica que el curso no usará mucho SSH.

## Opciones de compra de instancias EC2

| Opción | Uso / rasgo principal según fuente |
| --- | --- |
| Bajo demanda | Carga corta, precio predecible, pago por segundos. Sin compromiso a largo plazo. Recomendado cuando no se puede predecir comportamiento de aplicación. |
| Reservadas | 1 o 3 años; cargas largas. Hasta 72% de descuento frente a bajo demanda. |
| Reservadas convertibles | Cargas largas con instancias flexibles. Permiten cambiar tipo, familia, SO, etc. Hasta 66% de descuento. |
| Savings Plans | Compromiso de cantidad de uso por 1 o 3 años; carga larga. Hasta 72% de descuento. |
| Spot | Cargas cortas, baratas, tolerantes a fallos; se pueden perder instancias. Hasta 90% frente a bajo demanda. |
| Hosts dedicados | Reserva de servidor físico completo; control de ubicación; útil para licencias complejas BYOL y requisitos regulatorios o cumplimiento. |
| Instancias dedicadas | Hardware dedicado; puede compartirse con otras instancias de la misma cuenta; sin control de ubicación. |
| Reservas de capacidad | Reserva capacidad bajo demanda en una AZ específica para cualquier duración, sin descuento de facturación. |

### Facturación y notas de compra

- Bajo demanda:
  - Linux o Windows: facturación por segundo después del primer minuto.
  - Otros sistemas operativos: facturación por hora.
  - Coste más alto, sin pago adelantado.
- Reservadas:
  - reservan atributos como tipo, región, ocupación y sistema operativo;
  - periodo de 1 o 3 años;
  - opciones de pago: sin pago inicial, pago inicial parcial, pago inicial total;
  - alcance regional o zonal;
  - se pueden comprar y vender en Marketplace de instancias reservadas.
- Savings Plans:
  - compromiso de uso, por ejemplo `10 $/hora` durante 1 o 3 años;
  - uso excedente se factura bajo demanda;
  - bloqueado a una familia de instancia y región;
  - flexible en tamaño, sistema operativo y tenencia.
- Reservas de capacidad:
  - se puede crear o cancelar en cualquier momento;
  - se cobra tarifa bajo demanda aunque se ejecuten instancias o no;
  - puede combinarse con reservadas regionales y Savings Plans para descuentos de facturación.

### Spot y Spot Fleets

- Las instancias Spot son rentables y útiles para cargas tolerantes a fallos:
  - batch jobs;
  - análisis de datos;
  - procesamiento de imágenes;
  - cargas distribuidas;
  - cargas con inicio y fin flexibles.
- No son adecuadas para trabajos críticos ni bases de datos.
- Se define precio máximo Spot y se obtiene instancia mientras precio actual sea menor que el máximo.
- Si precio actual supera el máximo, se puede detener o terminar la instancia con periodo de gracia de 2 minutos.
- Para terminar Spot según la fuente:
  - solo pueden cancelarse solicitudes Spot abiertas, activas o desactivadas;
  - cancelar una solicitud Spot no termina las instancias;
  - primero se cancela la solicitud y luego se terminan las instancias asociadas.

Spot Fleets:

- Conjunto de instancias Spot + opcionalmente instancias bajo demanda.
- Trata de alcanzar capacidad objetivo con restricciones de precio.
- Define pools de lanzamiento por tipo de instancia, SO y AZ.
- Puede tener varios pools.
- Deja de lanzar cuando alcanza capacidad o coste máximo.
- Estrategias de asignación:
  - `lowest price`: pool con menor precio, optimización de costes, carga corta;
  - `diversified`: distribución en todos los pools, gran disponibilidad, cargas largas;
  - `capacity optimized`: pool con capacidad óptima para el número de instancias;
  - `price capacity optimized`: grupos con mayor capacidad disponible y luego menor precio; fuente lo marca como recomendado para la mayoría de cargas.

## Claves de repaso

- EC2 combina máquinas virtuales, almacenamiento, balanceo y escalado como base IaaS.
- User Data automatiza primer arranque y corre como root.
- Grupos de seguridad solo permiten reglas; entrada bloqueada por defecto, salida permitida por defecto.
- Timeout apunta a grupo de seguridad; conexión rechazada apunta a aplicación o lanzamiento.
- EC2 Instance Connect evita usar archivo de claves, pero puerto 22 debe estar abierto y funciona out-of-the-box con Amazon Linux 2.
- Compra EC2: bajo demanda para corto e impredecible; reservadas/Savings Plans para largo; Spot para tolerante a fallos; hosts dedicados para hardware/licencias/regulación; reservas de capacidad para AZ específica sin descuento.

## Caveats de extracción

- Algunas páginas son diagramas o tablas visuales; se conservan datos textuales relevantes sin replicar layout.
- Los precios y descuentos de la página 73 son ejemplos de fuente; la propia fuente advierte que porcentajes pueden cambiar y que números exactos no son necesarios para el examen.
- La tabla resumen SSH de la página 58 se extrae con poco detalle textual; se preserva la guía verbal de páginas vecinas.
