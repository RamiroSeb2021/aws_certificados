# EC2 - Nivel Solutions Architect Associate

> Fuente: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
> Páginas fuente: 78–92
> Índice Udemy relacionado: sección 6 `EC2 - Nivel Solutions Architect Associate`
> Método: extracción local con `pdftotext -layout`.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Se compactan comparaciones de IP, placement groups, ENI e hibernación sin agregar detalles externos.
- Se conservan límites, recomendaciones y caveats explícitos de la fuente.
- Las páginas con diagramas se traducen a descripciones textuales trazables.

## IP privada, IP pública e IP elástica

### IPv4 e IPv6

- La fuente distingue IPv4 e IPv6.
- Ejemplos fuente:
  - IPv4: `1.160.10.240`.
  - IPv6: `3ffe:1900:4545:3:200:f8ff:fe21:67cf`.
- En el curso se usará solo IPv4.
- IPv4 sigue siendo el formato más utilizado en Internet.
- IPv6 es más reciente y resuelve problemas del Internet de las Cosas (IoT).
- IPv4 permite 3.7 mil millones de direcciones diferentes en espacio público.
- Formato IPv4: `[0-255].[0-255].[0-255].[0-255]`.

### Diferencias fundamentales

| Tipo | Según fuente |
| --- | --- |
| IP pública | Identifica la máquina en Internet; debe ser única en toda la red; puede geolocalizarse fácilmente. |
| IP privada | Identifica la máquina solo dentro de una red privada; debe ser única dentro de esa red privada; redes privadas distintas pueden usar las mismas IP. |

- Las máquinas con IP privada se conectan a la WWW mediante NAT + Internet Gateway, descrito como proxy en la fuente.
- Solo puede utilizarse un rango específico de IPs como IP privada.

### IPs en EC2

- Por defecto, una máquina EC2 viene con:
  - una IP privada para red interna de AWS;
  - una IP pública para WWW.
- Para SSH desde fuera de la red, no se puede usar IP privada; se usa IP pública.
- Si la instancia se detiene y vuelve a iniciar, la IP pública puede cambiar.

### Elastic IP

- Si se necesita IP pública fija para una instancia, se usa Elastic IP.
- Elastic IP es una IPv4 pública que pertenece a la cuenta mientras no se elimine.
- Se puede asignar a una instancia a la vez.
- Puede enmascarar fallo de instancia o software reasignando la dirección a otra instancia de la cuenta.
- Límite fuente: solo 5 Elastic IP en la cuenta; se puede pedir aumento a AWS.
- La fuente recomienda evitar Elastic IP en general:
  - suelen reflejar malas decisiones de arquitectura;
  - alternativa: IP pública aleatoria + nombre DNS;
  - alternativa posterior del curso: Load Balancer sin IP pública.

## Grupos de ubicación o colocación

- Permiten controlar estrategia de colocación de instancias EC2.
- Al crear un placement group se especifica una estrategia.

| Estrategia | Descripción | Ventajas / uso | Contras / límites |
| --- | --- | --- | --- |
| Cluster | Agrupa instancias en baja latencia dentro de una única AZ. | Red de 10 Gbps entre instancias con red mejorada activada; Big Data que necesita completarse rápido; aplicaciones de latencia extremadamente baja y alto rendimiento de red. | Si falla el rack, todas las instancias fallan al mismo tiempo. |
| Distribuida | Coloca un pequeño grupo de instancias en hardware físico diferente para reducir fallos correlacionados. | Puede abarcar varias AZ; reduce riesgo de fallos simultáneos; útil para máxima alta disponibilidad y aplicaciones críticas donde cada instancia debe aislarse de fallos de otras. | Máximo 7 instancias por AZ por grupo. |
| Partición | Reparte instancias en particiones que dependen de conjuntos diferentes de racks dentro de una AZ. | Puede abarcar varias AZ en la misma región; hasta 7 particiones por AZ; hasta 100 instancias EC2; instancias acceden a información de partición como metadatos; casos: HDFS, HBase, Cassandra, Kafka. | Un fallo de partición puede afectar muchas EC2, pero no otras particiones. |

## Elastic Network Interfaces (ENI)

- ENI es un componente lógico de una VPC que representa una tarjeta de red virtual.
- Atributos mencionados:
  - IPv4 privada primaria;
  - una o más IPv4 secundarias;
  - una Elastic IP IPv4 por IPv4 privada;
  - una IPv4 pública;
  - uno o más grupos de seguridad;
  - una dirección MAC.
- Se pueden crear ENI independientes y adjuntarlas sobre la marcha a instancias EC2.
- La fuente menciona mover ENI entre instancias para conmutación por error.
- Están vinculadas a una AZ específica.

## Hibernación de EC2

### Parar, terminar e iniciar

- Al parar una instancia, los datos del disco EBS se mantienen intactos en el siguiente arranque.
- Al terminar una instancia, se pierden los volúmenes EBS root que estén preparados para destruirse.
- En el primer arranque, el sistema operativo inicia y se ejecuta EC2 User Data.
- En arranques siguientes, inicia el sistema operativo.
- Luego inicia la aplicación y se calientan cachés; eso puede tardar.

### Qué hace EC2 Hibernate

- Conserva estado en memoria RAM.
- Hace que el arranque sea mucho más rápido porque el sistema operativo no se detiene/reinicia.
- Bajo el capó, el estado de RAM se escribe en un archivo en el volumen EBS root.
- El volumen EBS root debe estar encriptado.
- Casos de uso:
  - procesamiento de larga duración;
  - guardar estado de RAM;
  - servicios que tardan en inicializarse.

### Condiciones y límites indicados

- Familias soportadas: C3, C4, C5, I3, M3, M4, R3, R4, T2, T3, entre otras indicadas con puntos suspensivos en fuente.
- RAM debe ser inferior a 150 GB.
- No se soporta para instancias bare metal.
- AMI mencionadas: Amazon Linux 2, Linux AMI, Ubuntu, RHEL, CentOS y Windows, con puntos suspensivos en fuente.
- Volumen root debe ser EBS y estar encriptado.
- Disponible para instancias bajo demanda, reservadas y Spot.
- Una instancia no puede estar hibernada más de 60 días.

## Claves de repaso

- IP pública identifica en Internet; IP privada identifica dentro de red privada.
- Elastic IP fija IP pública, pero la fuente recomienda evitarla como diseño general.
- Placement groups: Cluster prioriza latencia/rendimiento; Distribuida prioriza aislamiento de fallos; Partición escala grupos grandes con particiones.
- ENI es tarjeta de red virtual de VPC y puede moverse para failover dentro de restricciones de AZ.
- Hibernación conserva RAM en EBS root cifrado y reduce tiempo de arranque.

## Caveats de extracción

- Páginas 80 y 86–89 contienen diagramas; se preservan relaciones técnicas, no posiciones visuales.
- La lista de familias/AMI para hibernación aparece con puntos suspensivos; se conserva como lista no exhaustiva según fuente.
