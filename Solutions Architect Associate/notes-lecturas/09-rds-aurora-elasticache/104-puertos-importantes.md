# Puertos importantes para EC2, RDS y ElastiCache

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 57; complemento oficial AWS.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 14: Lista de puertos que debes conocer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [RDS endpoints and ports](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.EndpointAndPort.html), [EC2 security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) y [Accessing ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/accessing-elasticache.html).
> Complemento: documentación oficial de Amazon RDS, Amazon ElastiCache y referencia de grupos de seguridad EC2
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
- **Puerto de red:** número lógico que identifica el servicio de destino dentro de una dirección IP.
  - **Ejemplo:** una solicitud puede llegar a `10.0.1.20:443`; la IP localiza la interfaz y `443` identifica el servicio HTTPS.
- **Protocolo:** reglas que dos sistemas siguen para comunicarse.
  - **Ejemplo:** HTTP define cómo un cliente solicita una página y cómo responde el servidor.
- **FTP — File Transfer Protocol:** protocolo clásico de transferencia de archivos sin cifrado incorporado.
  - **Ejemplo:** un servidor FTP escucha habitualmente en el puerto `21`.
- **SSH — Secure Shell:** protocolo cifrado de administración remota.
  - **Ejemplo:** Linux suele aceptar SSH en el puerto `22` cuando las reglas lo permiten.
- **SFTP — SSH File Transfer Protocol:** protocolo de transferencia de archivos que funciona sobre SSH.
  - **Ejemplo:** SFTP usa normalmente el mismo puerto `22` de SSH.
- **HTTP — Hypertext Transfer Protocol:** protocolo de la Web sin cifrado TLS incorporado.
  - **Ejemplo:** un servidor HTTP escucha habitualmente en el puerto `80`.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP protegido mediante TLS.
  - **Ejemplo:** un sitio HTTPS escucha habitualmente en el puerto `443`.
- **RDP — Remote Desktop Protocol:** protocolo de escritorio remoto usado habitualmente con Windows.
  - **Ejemplo:** un administrador autorizado accede a Windows mediante el puerto `3389`.
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** PostgreSQL en RDS usa normalmente el puerto `5432`, salvo que se configure otro.
- **IP — Internet Protocol:** sistema de direccionamiento de red.
  - **Ejemplo:** abrir un puerto sin limitar las IP o grupos de origen puede permitir más acceso del necesario.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales cuyos grupos de seguridad controlan puertos permitidos.
  - **Ejemplo:** una regla autoriza SSH al puerto `22` de una instancia EC2 solo desde la red administrativa.
- **SQL — Structured Query Language:** lenguaje de bases de datos relacionales.
  - **Ejemplo:** MySQL, PostgreSQL y Microsoft SQL Server aceptan consultas SQL usando sus respectivos puertos.
- **TLS — Transport Layer Security:** protocolo que protege comunicaciones en tránsito.
  - **Ejemplo:** HTTPS utiliza TLS normalmente en el puerto `443`.
- **OSS — Open Source Software:** software de código abierto; aparece en el nombre Redis OSS.
  - **Ejemplo:** ElastiCache admite versiones compatibles de Redis OSS.

## Idea central

Una dirección IP indica a qué interfaz llegar; un puerto indica a qué servicio entregar la comunicación. Abrir el puerto NO instala ni inicia el programa.

**Ejemplo integrador:** la aplicación se conecta al endpoint PostgreSQL en el puerto `5432`. El grupo de seguridad permite ese puerto solo desde las instancias de la aplicación, no desde todo Internet.

## Puertos clásicos del documento fuente

| Puerto | Protocolo/servicio | Uso descrito |
| ---: | --- | --- |
| 21 | FTP | Transferencia de archivos. |
| 22 | SSH | Acceso remoto a Linux. |
| 22 | SFTP | Transferencia segura sobre SSH. |
| 80 | HTTP | Sitios web sin TLS. |
| 443 | HTTPS | Sitios web con TLS. |
| 3389 | RDP | Acceso remoto a Windows. |

## Puertos de bases de datos y caché

| Puerto predeterminado | Motor/servicio |
| ---: | --- |
| 1433 | Microsoft SQL Server |
| 1521 | Oracle |
| 3306 | MySQL, MariaDB y Aurora compatible con MySQL |
| 5432 | PostgreSQL y Aurora compatible con PostgreSQL |
| 6379 | ElastiCache para Valkey o Redis OSS |
| 11211 | ElastiCache para Memcached |

## Cómo razonarlos

- Un puerto identifica el servicio de destino dentro de una máquina o endpoint.
- Abrir un puerto en un grupo de seguridad no instala ni inicia el servicio.
- Las reglas deben limitar el origen a los clientes que realmente necesitan conectarse.
- Son valores predeterminados: la configuración efectiva del endpoint es la fuente operativa.

## Fuentes oficiales del complemento

- [Conexión y puertos de una instancia Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.EndpointAndPort.html)
- [Referencia de reglas de grupos de seguridad de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html)
- [Acceso a clústeres o grupos de replicación de Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/accessing-elasticache.html)
