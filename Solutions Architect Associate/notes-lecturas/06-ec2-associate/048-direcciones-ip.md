# Direcciones IP en Amazon EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 79–84.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 1: IP privada vs pública vs elástica.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EC2 instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html) y [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html).
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo desde fundamentos.
- Cada concepto nuevo incluye una explicación sencilla y un ejemplo inmediato.
- Las siglas se desarrollan y explican en su primera aparición conceptual.
- Los límites y cifras del curso se preservan como contenido de la fuente y pueden cambiar; los complementos actuales se identifican por separado.

## Antes de empezar: conceptos y siglas

- **AWS — Amazon Web Services:** plataforma de servicios de nube donde se ejecutan los recursos del curso.
  - **Ejemplo:** una empresa puede alquilar una instancia EC2 en AWS en vez de comprar un servidor.
- **EC2 — Amazon Elastic Compute Cloud:** servicio para crear computadoras virtuales llamadas instancias.
  - **Ejemplo:** una instancia EC2 puede ejecutar el servidor de una tienda virtual.
- **IP — Internet Protocol (Protocolo de Internet):** conjunto de reglas de direccionamiento que permite identificar el origen y el destino de una comunicación en una red.
  - **Ejemplo:** `10.0.1.25` puede identificar la conexión de red de un servidor dentro de una VPC.
- **IPv4 — Internet Protocol version 4:** versión de IP que escribe una dirección como cuatro números separados por puntos.
  - **Ejemplo:** `1.160.10.240` es una dirección IPv4.
- **IPv6 — Internet Protocol version 6:** versión más reciente de IP, con un espacio de direcciones mucho mayor y una escritura hexadecimal separada por dos puntos.
  - **Ejemplo:** `2001:db8::10` es una dirección IPv6 reservada para documentación.
- **Dirección privada:** dirección usada para comunicación dentro de una red privada; no es alcanzable directamente desde Internet.
  - **Ejemplo:** una aplicación en `10.0.1.25` puede hablar con una base de datos en `10.0.2.20` dentro de la misma VPC.
- **Dirección pública:** dirección que puede ser alcanzable desde Internet cuando el enrutamiento y las reglas de seguridad lo permiten.
  - **Ejemplo:** un navegador puede usar la dirección pública de un servidor web para enviarle una solicitud.
- **Elastic IP:** dirección IPv4 pública y estática asignada a una cuenta de AWS hasta que se libera.
  - **Ejemplo:** si falla `EC2-A`, la misma Elastic IP puede reasociarse con `EC2-B`.
- **NAT — Network Address Translation (traducción de direcciones de red):** mecanismo que permite que recursos con direcciones privadas inicien comunicaciones hacia fuera usando otra dirección.
  - **Ejemplo:** varias instancias privadas pueden descargar actualizaciones mediante un dispositivo NAT sin recibir conexiones directas desde Internet.
- **DNS — Domain Name System (sistema de nombres de dominio):** traduce nombres legibles a direcciones IP.
  - **Ejemplo:** `tienda.example.com` puede apuntar a la dirección pública del servicio.
- **SSH — Secure Shell:** protocolo de acceso remoto cifrado, usado habitualmente para administrar sistemas Linux.
  - **Ejemplo:** un administrador puede conectarse por SSH al puerto `22` de una instancia autorizada.
- **IoT — Internet of Things (Internet de las cosas):** conjunto de objetos físicos conectados que intercambian información por red.
  - **Ejemplo:** miles de sensores pueden necesitar direcciones para enviar mediciones.

- **VPC — Virtual Private Cloud (nube privada virtual):** red virtual aislada que el cliente controla dentro de AWS.
  - **Ejemplo:** las direcciones privadas de dos instancias pueden comunicarse dentro de la misma VPC.
- **WWW — World Wide Web:** sistema de páginas y recursos enlazados que se consultan mediante Internet.
  - **Ejemplo:** un navegador abre una página publicada por un servidor web.

## Idea central

Una dirección IP permite localizar una interfaz en una red. La diferencia principal es el alcance: una IP privada se usa dentro de la red, una pública puede usarse desde Internet y una Elastic IP mantiene una dirección pública estable.

**Ejemplo integrador:** una instancia conserva su IP privada al detenerse e iniciarse. Su IPv4 pública asignada automáticamente puede cambiar; si el servicio necesita una dirección pública estable, puede utilizarse una Elastic IP.

> **Complemento oficial de AWS:** la asignación automática de IPv4 pública no ocurre en todas las instancias por defecto; depende de la configuración de la subred y de las opciones elegidas al lanzar la instancia. AWS cobra actualmente por las direcciones IPv4 públicas, incluidas las Elastic IP.

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
