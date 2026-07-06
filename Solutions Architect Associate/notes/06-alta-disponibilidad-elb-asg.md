# Alta disponibilidad y escalabilidad: ELB y ASG

> Fuente: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
> Páginas fuente: 118–159
> Índice Udemy relacionado: sección 8 `Alta disponibilidad y escalabilidad: ELB y ASG`
> Método: extracción local con `pdftotext -layout`.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Se conserva la progresión fuente: escalabilidad, alta disponibilidad, ELB, tipos de load balancer, sesiones persistentes, TLS y ASG.
- Se mantienen nombres, límites, protocolos y valores de tiempo presentes en las páginas fuente.
- Diagramas de flujo y topología se resumen como relaciones textuales trazables.

## Escalabilidad y alta disponibilidad

- Escalabilidad: una aplicación o sistema puede manejar mayores cargas adaptándose.
- Tipos de escalabilidad:
  - vertical;
  - horizontal, también llamada elasticidad.
- La escalabilidad está vinculada a la alta disponibilidad, pero no es lo mismo.

### Escalabilidad vertical

- Significa aumentar tamaño de instancia.
- Ejemplo fuente: pasar de `t2.micro` a `t2.large`.
- Es común para sistemas no distribuidos, como bases de datos.
- RDS y ElastiCache pueden escalar verticalmente.
- Suele existir límite de escalabilidad vertical por hardware.

### Escalabilidad horizontal

- Significa aumentar número de instancias o sistemas de la aplicación.
- Implica sistemas distribuidos.
- Es común en aplicaciones web y aplicaciones modernas.
- La fuente indica que es fácil escalar horizontalmente gracias a ofertas cloud como Amazon EC2.

### Alta disponibilidad

- Suele ir de la mano del escalado horizontal.
- Significa ejecutar aplicación o sistema en al menos 2 centros de datos, equivalentes a Zonas de Disponibilidad.
- Objetivo: sobrevivir a pérdida de un centro de datos.
- Puede ser pasiva, por ejemplo RDS Multi-AZ.
- Puede ser activa, por ejemplo escalado horizontal.

### En EC2

- Escalado vertical: cambiar tamaño de instancia; ejemplo fuente de `t2.nano` con 0,5 GB RAM y 1 vCPU hasta `u-12tb1.metal` con 12,3 TB RAM y 448 vCPUs.
- Escalado horizontal: aumentar número de instancias mediante Auto Scaling Group y Load Balancer.
- Alta disponibilidad: ejecutar instancias de la misma aplicación en múltiples AZ mediante ASG multi-AZ y Load Balancer multi-AZ.

## Elastic Load Balancing

### Qué es un Load Balancer

- Servidor que reenvía tráfico a varios servidores descendentes, por ejemplo instancias EC2.
- Razones para usarlo:
  - repartir carga entre varias instancias descendentes;
  - exponer un único punto de acceso DNS;
  - manejar fallos de instancias descendentes;
  - hacer comprobaciones periódicas de salud;
  - proporcionar terminación SSL/HTTPS;
  - imponer adherencia con cookies;
  - alta disponibilidad entre zonas;
  - separar tráfico público y privado.

### Por qué usar Elastic Load Balancer

- Es un balanceador gestionado.
- AWS garantiza su funcionamiento.
- AWS se encarga de actualizaciones, mantenimiento y alta disponibilidad.
- AWS ofrece pocas opciones de configuración según la fuente.
- La fuente indica que configurarlo cuesta poco y mejora disponibilidad y escalabilidad.
- Integraciones mencionadas:
  - EC2, EC2 Auto Scaling Groups, Amazon ECS;
  - AWS Certificate Manager (ACM), CloudWatch;
  - Route 53, AWS WAF, AWS Global Accelerator.

### Health checks

- Son cruciales para Load Balancer.
- Permiten saber si las instancias destino están disponibles para responder.
- Se realizan sobre puerto y ruta; `/health` aparece como ruta común.
- Si respuesta no es `200 OK`, la instancia no está sana.
- Ejemplo fuente: HTTP, puerto `4567`, endpoint `/health`.

### Grupos de seguridad de Load Balancer

- Usuarios acceden por HTTP/HTTPS desde cualquier lugar al grupo de seguridad del Load Balancer.
- La aplicación permite tráfico HTTP restringido desde el Load Balancer.
- Fuente: grupo de seguridad de aplicaciones debe permitir tráfico solo desde Load Balancer.

## Tipos de Load Balancer en AWS

| Tipo | Generación / año | Protocolos / capa | Notas fuente |
| --- | --- | --- | --- |
| Classic Load Balancer (CLB) | v1, 2009 | HTTP, HTTPS, TCP, SSL/TCP seguro; TCP capa 4, HTTP/HTTPS capa 7 | Comprobaciones de estado TCP o HTTP; nombre de host fijo `XXX.region.elb.amazonaws.com`. |
| Application Load Balancer (ALB) | v2, 2016 | HTTP, HTTPS, WebSocket; capa 7 | Recomendado para HTTP, microservicios, contenedores y enrutamiento avanzado. |
| Network Load Balancer (NLB) | v2, 2017 | TCP, TLS/TCP seguro, UDP; capa 4 | Rendimiento extremo, tráfico TCP/UDP, millones de peticiones por segundo, menor latencia, IP estática por AZ y soporte Elastic IP. |
| Gateway Load Balancer (GWLB) | 2020 | Capa 3, paquetes IP | Para desplegar, escalar y administrar dispositivos virtuales de red de terceros. Usa GENEVE puerto 6081. |

- La fuente recomienda en general usar load balancers de nueva generación por ofrecer más funciones.
- Algunos Load Balancer pueden configurarse como internos privados o externos públicos.

## Application Load Balancer

- ALB es capa 7 HTTP.
- Balancea múltiples aplicaciones HTTP en distintas máquinas mediante target groups.
- Balancea múltiples aplicaciones en una misma máquina, por ejemplo contenedores.
- Soporta HTTP/2 y WebSocket.
- Soporta redireccionamientos, por ejemplo HTTP a HTTPS.

### Enrutamiento

- Puede enrutar a distintos target groups por:
  - ruta de URL, por ejemplo `example.com/users` y `example.com/posts`;
  - nombre de host, por ejemplo `one.example.com` y `other.example.com`;
  - query string y cabeceras, por ejemplo `example.com/users?id=123&order=false`.
- Adecuado para microservicios y aplicaciones basadas en contenedores, como Docker y Amazon ECS.
- Tiene mapeo de puertos para redirigir a puerto dinámico en ECS.
- La fuente contrasta que con Classic Load Balancer harían falta varios CLB por aplicación.

### Target groups ALB

- Instancias EC2, posiblemente gestionadas por Auto Scaling Groups, usando HTTP.
- Tareas ECS, gestionadas por ECS, usando HTTP.
- Funciones Lambda: la petición HTTP se traduce a evento JSON.
- Direcciones IP privadas.
- ALB puede enrutar a múltiples target groups.
- Health checks son a nivel target group.

### Datos de cliente

- ALB tiene nombre de host fijo `XXX.region.elb.amazonaws.com`.
- Los servidores de aplicación no ven directamente IP del cliente.
- IP real del cliente se inserta en `X-Forwarded-For`.
- También se puede obtener puerto con `X-Forwarded-Port` y protocolo con `X-Forwarded-Proto`.

## Network Load Balancer

- NLB permite reenviar tráfico TCP y UDP a instancias.
- Puede manejar millones de peticiones por segundo.
- Tiene menor latencia.
- Tiene IP estática por AZ y soporta asignación de Elastic IP, útil para permitir una IP específica.
- Se usa para rendimiento extremo y tráfico TCP o UDP.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas;
  - Application Load Balancer.
- Health checks soportan TCP, HTTP y HTTPS.

## Gateway Load Balancer

- Implementa, escala y administra flota de dispositivos virtuales de red de terceros en AWS.
- Ejemplos fuente:
  - firewalls;
  - sistemas de detección y prevención de intrusiones;
  - inspección profunda de paquetes;
  - manipulación de cargas útiles.
- Opera en capa 3, paquetes IP.
- Combina:
  - gateway de red transparente como entrada/salida única para todo el tráfico;
  - load balancer para distribuir tráfico a dispositivos virtuales.
- Usa protocolo GENEVE en puerto `6081`.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas.

## Sticky Sessions

- Permiten persistencia para que el mismo cliente sea redirigido a la misma instancia detrás de un Load Balancer.
- Funciona para Classic Load Balancer, Application Load Balancer y Network Load Balancer.
- Para CLB y ALB, la cookie de persistencia tiene fecha de expiración controlada por el usuario.
- Caso de uso: que el usuario no pierda datos de sesión.
- Puede provocar desbalanceo de carga entre instancias EC2 backend.

### Nombres de cookies

- Cookies basadas en la aplicación:
  - Cookie personalizada:
    - generada por el objetivo;
    - puede incluir atributos requeridos por la aplicación;
    - nombre especificado por target group;
    - no usar `AWSALB`, `AWSALBAPP` o `AWSALBTG`, reservadas para ELB.
  - Cookie de la aplicación:
    - generada por Load Balancer;
    - nombre `AWSALBAPP`.
- Cookies basadas en duración:
  - generadas por Load Balancer;
  - nombre `AWSALB` para ALB y `AWSELB` para CLB.

## Load Balancer entre zonas

- Con cross-zone load balancing, cada instancia del Load Balancer distribuye uniformemente entre todas las instancias registradas en todas las AZ.
- Sin cross-zone load balancing, las solicitudes se distribuyen en instancias del nodo del Elastic Load Balancer.

| Tipo | Estado según fuente |
| --- | --- |
| ALB | Siempre activado; no se puede desactivar; no se cobra por datos inter-AZ. |
| NLB y GWLB | Desactivado por defecto; si se activa, se paga tarifa por datos entre zonas geográficas. |
| CLB | Desactivado por defecto; no se cobra por datos inter-AZ si está activado. |

## SSL/TLS y certificados

- Certificado SSL permite cifrar en tránsito tráfico entre clientes y Load Balancer.
- SSL significa `Secure Sockets Layer`.
- TLS significa `Transport Layer Security` y es versión más reciente.
- La fuente indica que hoy se usan principalmente certificados TLS, aunque se les siga diciendo SSL.
- Certificados SSL públicos son emitidos por autoridades de certificación como Comodo, Symantec, GoDaddy, GlobalSign, Digicert y Letsencrypt.
- Tienen fecha de caducidad y deben renovarse.

### Certificados en Load Balancer

- Load Balancer usa certificado X.509, certificado de servidor SSL/TLS.
- Certificados pueden gestionarse con AWS Certificate Manager (ACM).
- También se pueden crear y subir certificados propios.
- Listener HTTPS:
  - requiere certificado por defecto;
  - permite lista opcional de certificados para múltiples dominios;
  - clientes pueden usar SNI para especificar nombre de host;
  - se puede especificar política de seguridad para soportar versiones antiguas SSL/TLS en clientes heredados.

### SNI

- `Server Name Indication` resuelve problema de cargar varios certificados SSL en un servidor web para servir varios sitios.
- Requiere que el cliente indique nombre del servidor destino en handshake SSL inicial.
- El servidor encuentra certificado correcto o devuelve el predeterminado.
- Solo funciona para ALB, NLB y CloudFront según fuente.
- No funciona con CLB.

### Soporte de certificados por tipo

- CLB v1: soporta un solo certificado SSL; para varios hostnames con varios certificados se requieren varios CLB.
- ALB v2: soporta múltiples listeners con múltiples certificados SSL; usa SNI.
- NLB v2: soporta múltiples listeners con múltiples certificados SSL; usa SNI.

## Connection Draining

- Nombre de característica:
  - `Connection Draining` para CLB.
  - `Deregistration Delay` para ALB y NLB.
- Da tiempo para completar peticiones “en vuelo” mientras la instancia se desregistra o no está sana.
- Deja de enviar nuevas peticiones a la instancia EC2 que se está desregistrando.
- Rango: 1 a 3600 segundos.
- Por defecto: 300 segundos.
- Se puede desactivar fijando valor en 0.
- La fuente recomienda valor bajo si las peticiones son cortas.

## Auto Scaling Groups (ASG)

### Objetivo

- En la vida real, carga de sitios web y aplicaciones puede cambiar.
- En Cloud, se pueden crear y eliminar servidores rápidamente.
- Objetivos de ASG según fuente:
  - añadir instancias EC2 para adaptarse a aumento de carga;
  - eliminar instancias EC2 para ajustarse a disminución de carga;
  - asegurar mínimo y máximo de instancias EC2 en funcionamiento;
  - registrar nuevas instancias automáticamente en Load Balancer;
  - recrear instancia EC2 si se elimina una anterior o si no está sana.
- ASG son gratuitos; se paga por instancias EC2 subyacentes.

### Capacidad y Load Balancer

- ASG usa capacidad mínima, deseada y máxima.
- Puede ampliar escala según necesidad.
- Con Load Balancer, ELB puede comprobar salud de instancias EC2.

### Atributos de ASG

- Plantilla de lanzamiento; la fuente indica que configuraciones de lanzamiento antiguas están obsoletas.
- Incluye:
  - AMI y tipo de instancia;
  - EC2 User Data;
  - volúmenes EBS;
  - grupos de seguridad;
  - par de claves SSH;
  - roles IAM para instancias EC2;
  - información de red y subredes;
  - información de Load Balancer.
- Tamaño mínimo, máximo y capacidad inicial.
- Políticas de escalado.

## Políticas y métricas de escalado

### CloudWatch

- ASG puede escalarse mediante alarmas de CloudWatch.
- Una alarma monitoriza una métrica, como CPU media o métrica personalizada.
- Métricas como CPU media se calculan para todas las instancias del ASG.
- En base a la alarma se pueden crear políticas para aumentar o reducir número de instancias.

### Políticas dinámicas

- Seguimiento de objetivos:
  - lo más sencillo y fácil de configurar;
  - ejemplo fuente: mantener media CPU del ASG alrededor de 40%.
- Escalado simple / escalonado:
  - si alarma CPU > 70%, añadir 2 unidades;
  - si alarma CPU < 30%, eliminar 1 unidad.
- Acciones programadas:
  - anticipan escalado por patrones conocidos;
  - ejemplo: aumentar capacidad mínima a 10 a las 17 h de los viernes.
- Escalado predictivo:
  - previsión continua de carga y programación del escalado por adelantado.

### Buenas métricas para escalar

- `CPUUtilization`: utilización media CPU en instancias.
- `RequestCountPerTarget`: mantener estable número de peticiones por instancia EC2.
- Promedio de entrada/salida de red si la aplicación está vinculada a la red.
- Métricas personalizadas enviadas con CloudWatch.

### Cooldown

- Tras una actividad de escalado, ASG entra en periodo de enfriamiento.
- Por defecto: 300 segundos.
- Durante cooldown, ASG no lanza ni termina instancias adicionales para permitir estabilización de métricas.
- Consejo de fuente: usar AMI lista para usar para reducir tiempo de configuración, servir peticiones más rápido y reducir periodo de enfriamiento.

## Claves de repaso

- Escalado vertical cambia tamaño; horizontal cambia cantidad de instancias.
- Alta disponibilidad busca sobrevivir pérdida de AZ y suele acompañar escalado horizontal.
- ELB aporta DNS único, health checks, terminación SSL, sticky sessions, alta disponibilidad entre zonas y separación público/privado.
- ALB: capa 7 HTTP, routing por path/host/query/header y target groups variados.
- NLB: capa 4, TCP/UDP, baja latencia, IP estática por AZ.
- GWLB: capa 3 para dispositivos virtuales de red, con GENEVE puerto 6081.
- Sticky sessions conservan sesión de cliente, pero pueden desbalancear backend.
- ASG controla mínimo/deseado/máximo, usa launch template y puede escalar por CloudWatch, políticas dinámicas, acciones programadas o predicción.

## Caveats de extracción

- Páginas 133, 135, 138, 140, 144, 152 y 153 son diagramas; se preserva el flujo descrito por texto extraído, no la diagramación.
- La fuente usa “reducir” para añadir instancias y “aumentar” para eliminarlas en página 151; se mantuvo el objetivo operativo claro sin añadir explicación externa.
- Los nombres español/inglés de características se conservan cuando aparecen juntos, por ejemplo `Connection Draining` y retraso en desregistro.
