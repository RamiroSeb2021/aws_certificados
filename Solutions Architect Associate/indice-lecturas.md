# Índice de lecturas y apuntes

Este índice relaciona las secciones y lecturas de [`course-content.md`](course-content.md) con las temáticas disponibles en [`notes/`](notes/) y con los apuntes individuales de [`notes-lecturas/`](notes-lecturas/README.md). Los números de línea apuntan al bloque más específico que desarrolla cada tema.

> **Cobertura actual:** hay apuntes consolidados para las secciones 4 a 8 y apuntes por lectura revisada para las secciones 6 a 10. Las secciones 1 a 3 y 11 a 34 todavía no tienen una nota equivalente.
> Las demostraciones (`[DEMO]`) se excluyen para mantener el índice enfocado en las lecturas teóricas, artículos y cuestionarios.

## Apuntes por lectura revisada

Las 37 lecturas seleccionadas de las secciones 6 a 10 tienen un archivo Markdown independiente:

- [`notes-lecturas/README.md`](notes-lecturas/README.md) — índice completo por sección y número de lectura.
- Cada archivo identifica las páginas del PDF usadas como fuente.
- La lectura adicional de puertos combina la diapositiva de puertos clásicos con referencias oficiales de AWS claramente identificadas.

## Ruta rápida por sección

| Sección del curso | Apunte | Cobertura |
| --- | --- | --- |
| 1. Introducción al curso | — | Sin apunte temático |
| 2. Descarga del material del curso | — | Sin apunte temático |
| 3. Empezando con AWS | — | Sin apunte temático |
| 4. IAM y CLI de AWS | [`notes/02-iam-y-cli.md`](notes/02-iam-y-cli.md) | Disponible |
| 5. Fundamentos de EC2 | [`notes/03-ec2-fundamentos.md`](notes/03-ec2-fundamentos.md) | Disponible |
| 6. EC2 - Nivel Solutions Architect Associate | [`notes/04-ec2-associate.md`](notes/04-ec2-associate.md) | Disponible |
| 7. Almacenamiento de instancias EC2 | [`notes/05-ec2-instance-storage.md`](notes/05-ec2-instance-storage.md) | Disponible |
| 8. Alta disponibilidad y escalabilidad: ELB y ASG | [`notes/06-alta-disponibilidad-elb-asg.md`](notes/06-alta-disponibilidad-elb-asg.md) | Disponible |
| 9. RDS + Aurora + ElastiCache | [`notes-lecturas/09-rds-aurora-elasticache/`](notes-lecturas/09-rds-aurora-elasticache/) | Disponible por lectura seleccionada |
| 10. Route 53 | [`notes-lecturas/10-route-53/`](notes-lecturas/10-route-53/) | Disponible por lectura seleccionada |
| 11–34 | — | Todavía sin apuntes |

## 4. IAM y CLI de AWS

**Apunte principal:** [`notes/02-iam-y-cli.md`](notes/02-iam-y-cli.md)

| # | Lectura del curso | Dónde encontrarla en los apuntes |
| ---: | --- | --- |
| 1 | Introducción de IAM: Usuarios, grupos y políticas | Líneas 15–46: **IAM: usuarios, grupos y permisos** y **Políticas IAM** |
| 5 | Políticas de IAM | Líneas 24–46: **Políticas IAM** y estructura de una política |
| 8 | Visión general de IAM MFA | Líneas 64–83: **Multi Factor Authentication (MFA)** |
| 10 | Claves de acceso a AWS, CLI y SDK | Líneas 84–121: **Formas de acceder a AWS**, claves, CLI y SDK |
| 11 | Configuración de la CLI de AWS en Windows | Líneas 101–110: **AWS CLI**; no hay pasos específicos por sistema operativo |
| 12 | Configuración de la CLI de AWS en Mac OS X | Líneas 101–110: **AWS CLI**; no hay pasos específicos por sistema operativo |
| 13 | Configuración de la CLI de AWS en Linux | Líneas 101–110: **AWS CLI**; no hay pasos específicos por sistema operativo |
| 15 | AWS CloudShell | Líneas 84–121: **Formas de acceder a AWS / AWS CLI y SDK**; cobertura general, sin bloque propio |
| 16 | Roles de IAM para los servicios de AWS | Líneas 123–130: **Roles IAM para servicios** |
| 18 | Herramientas de seguridad IAM | Líneas 132–140: **Herramientas de seguridad IAM** |
| 20 | Mejores prácticas de IAM | Líneas 142–152: **Buenas prácticas IAM** |
| 21 | Resumen de IAM | Líneas 154–161: **Claves de repaso** |
| 22 | Cuestionario - Identity and Access Management (IAM) | Líneas 154–161: **Claves de repaso** como preparación |

## 5. Fundamentos de EC2

**Apunte principal:** [`notes/03-ec2-fundamentos.md`](notes/03-ec2-fundamentos.md)

| # | Lectura del curso | Dónde encontrarla en los apuntes |
| ---: | --- | --- |
| 2 | Conceptos básicos de EC2 | Líneas 15–38: **Amazon EC2 como IaaS** y configuración de instancias |
| 4 | Tipos básicos de instancias EC2 | Líneas 52–68: **Tipos de instancias EC2** |
| 5 | Grupos de seguridad y puertos clásicos | Líneas 70–103: **Grupos de seguridad** y **Puertos clásicos** |
| 7 | Visión general de SSH | Líneas 105–124: **SSH e Instance Connect** |
| 8 | Cómo utilizar SSH usando Linux o Mac | Líneas 105–124: cobertura conceptual; sin pasos específicos por sistema operativo |
| 9 | Cómo utilizar SSH usando Windows | Líneas 105–124: cobertura conceptual; sin pasos específicos por sistema operativo |
| 10 | Cómo utilizar SSH usando Windows 10 | Líneas 105–124: cobertura conceptual; sin pasos específicos por sistema operativo |
| 11 | Solución de problemas de SSH | Líneas 117–124: **Solución de problemas SSH** |
| 12 | EC2 Instance Connect | Líneas 105–124: **SSH e Instance Connect** |
| 13 | Demostración de los roles de las instancias de EC2 | Sin bloque específico; los roles IAM están en `notes/02-iam-y-cli.md`, líneas 123–130 |
| 14 | Opciones de compra de instancias EC2 | Líneas 126–159: **Opciones de compra de instancias EC2** |
| 15 | Instancias Spot y Flota Spot | Líneas 161–188: **Spot y Spot Fleets** |
| 17 | Cuestionario - EC2 | Líneas 190–197: **Claves de repaso** como preparación |

## 6. EC2 - Nivel Solutions Architect Associate

**Apunte principal:** [`notes/04-ec2-associate.md`](notes/04-ec2-associate.md)

| # | Lectura del curso | Dónde encontrarla en los apuntes |
| ---: | --- | --- |
| 1 | IP privada vs pública vs elástica | Líneas 15–57: **IP privada, IP pública e IP elástica** |
| 3 | Grupos de colocación de EC2 | Líneas 59–68: **Grupos de ubicación o colocación** |
| 5 | Visión general de Interfaces de red elásticas (ENI) | Líneas 70–82: **Elastic Network Interfaces (ENI)** |
| 7 | ENI - Lectura extra | Líneas 70–82: **Elastic Network Interfaces (ENI)** |
| 8 | Hibernación de EC2 | Líneas 84–113: **Hibernación de EC2** |
| 10 | Cuestionario - Nivel Solutions Architect Associate SAA | Líneas 115–121: **Claves de repaso** como preparación |

## 7. Almacenamiento de instancias EC2

**Apunte principal:** [`notes/05-ec2-instance-storage.md`](notes/05-ec2-instance-storage.md)

| # | Lectura del curso | Dónde encontrarla en los apuntes |
| ---: | --- | --- |
| 1 | Visión general de EBS | Líneas 15–42: **Amazon EBS**, características y “Borrar al terminar” |
| 3 | Visión general de EBS Snapshots | Líneas 44–58: **Snapshots de EBS** |
| 5 | Visión general de AMI | Líneas 60–77: **AMI** |
| 7 | EC2 Instance Store | Líneas 79–87: **EC2 Instance Store** |
| 8 | Tipos de volúmenes EBS | Líneas 89–111: **Tipos de volúmenes EBS** y casos de uso |
| 9 | Multi-Attach EBS | Líneas 113–121: **EBS Multi-Attach** |
| 10 | Cifrado de EBS | Líneas 123–142: **Cifrado de EBS** |
| 11 | Amazon EFS | Líneas 144–173: **Amazon EFS**, rendimiento y almacenamiento |
| 14 | EFS vs EBS | Líneas 175–181: **EBS vs EFS vs Instance Store** |
| 16 | Cuestionario - Almacenamiento de instancias EC2 | Líneas 183–190: **Claves de repaso** como preparación |

## 8. Alta disponibilidad y escalabilidad: ELB y ASG

**Apunte principal:** [`notes/06-alta-disponibilidad-elb-asg.md`](notes/06-alta-disponibilidad-elb-asg.md)

| # | Lectura del curso | Dónde encontrarla en los apuntes |
| ---: | --- | --- |
| 1 | Alta disponibilidad y escalabilidad | Líneas 15–50: escalabilidad vertical, horizontal y alta disponibilidad |
| 2 | Visión general del Elastic Load Balancing (ELB) | Líneas 52–91: **Elastic Load Balancing**, health checks y seguridad |
| 3 | Nota: Acerca del Classic Load Balancer (CLB) | Líneas 93–103: **Tipos de Load Balancer en AWS** |
| 4 | Application Load Balancer (ALB) | Líneas 105–137: **Application Load Balancer** |
| 7 | Network Load Balancer (NLB) | Líneas 139–150: **Network Load Balancer** |
| 9 | Gateway Load Balancer (GWLB) | Líneas 152–167: **Gateway Load Balancer** |
| 10 | Elastic Load Balancer - Sesiones Persistentes (Sticky Sessions) | Líneas 169–190: **Sticky Sessions** y nombres de cookies |
| 11 | Elastic Load Balancer (ELB) - Balanceo de carga entre zonas | Líneas 192–201: **Load Balancer entre zonas** |
| 12 | Elastic Load Balancer (ELB) - Certificados SSL/TLS | Líneas 203–235: SSL/TLS, certificados, SNI y soporte por tipo |
| 14 | Elastic Load Balancer (ELB) - Drenaje de la conexión | Líneas 237–247: **Connection Draining** |
| 15 | Visión general de los Auto Scaling Groups (ASG) | Líneas 249–282: **Auto Scaling Groups (ASG)** |
| 17 | Auto Scaling Groups - Políticas de escalado | Líneas 284–319: **Políticas y métricas de escalado** |
| 20 | Cuestionario - Alta disponibilidad y escalabilidad con ELB y ASG | Líneas 321–330: **Claves de repaso** como preparación |

## Secciones todavía sin correspondencia

Las siguientes secciones aparecen en `course-content.md`, pero aún no tienen apuntes equivalentes:

- 1–3: introducción, materiales del curso y primeros pasos con AWS.
- 11–16: arquitecturas clásicas, S3, SDK/IAM, CloudFront y Global Accelerator.
- 17–24: almacenamiento adicional, mensajería y streaming, contenedores, serverless, bases de datos, analíticas y Machine Learning.
- 25–31: monitorización, IAM avanzado, seguridad y cifrado, VPC, recuperación, migraciones, arquitecturas adicionales y otros servicios.
- 32–34: whitepapers, preparación para el examen y cierre del curso.

Cuando se agreguen nuevos apuntes, este índice debería ampliarse usando el mismo criterio: **lectura del curso → archivo → bloque temático → líneas**.
