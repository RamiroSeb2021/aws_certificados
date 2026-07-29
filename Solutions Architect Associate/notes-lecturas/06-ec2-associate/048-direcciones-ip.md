# Direcciones IP en Amazon EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 79–84.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 1: IP privada vs pública vs elástica.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
