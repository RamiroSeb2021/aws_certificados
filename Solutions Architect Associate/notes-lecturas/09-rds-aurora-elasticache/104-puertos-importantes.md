# Puertos importantes para EC2, RDS y ElastiCache

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 57; complemento oficial AWS.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 14: Lista de puertos que debes conocer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Complemento: documentación oficial de Amazon RDS, Amazon ElastiCache y referencia de grupos de seguridad EC2
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Puertos clásicos del PDF

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
