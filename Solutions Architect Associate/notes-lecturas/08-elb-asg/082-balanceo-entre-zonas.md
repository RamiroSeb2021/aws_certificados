# Balanceo de cargas entre zonas

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 144–145.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 11: Balanceo de carga entre zonas.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#cross-zone-load-balancing).
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
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región de AWS.
  - **Ejemplo:** una aplicación puede tener dos servidores en `AZ-A` y ocho en `AZ-B`.
- **Nodo del Load Balancer:** componente del balanceador que recibe tráfico en una AZ habilitada.
  - **Ejemplo:** el nodo de `AZ-A` puede recibir parte de las solicitudes de los clientes.
- **Cross-zone load balancing (balanceo entre zonas):** permite que cada nodo distribuya tráfico a destinos situados en todas las AZ habilitadas.
  - **Ejemplo:** el nodo de `AZ-A` puede enviar solicitudes también a servidores de `AZ-B`.
- **ALB — Application Load Balancer:** balanceador de capa de aplicación para HTTP y HTTPS.
  - **Ejemplo:** un ALB regional reparte solicitudes entre target groups.
- **NLB — Network Load Balancer:** balanceador de capa de red.
  - **Ejemplo:** con cross-zone desactivado, cada nodo NLB elige destinos de su propia AZ.
- **GWLB — Gateway Load Balancer:** balanceador para dispositivos virtuales de red.
  - **Ejemplo:** puede distribuir paquetes entre dispositivos de inspección por zona.
- **CLB — Classic Load Balancer:** generación anterior de balanceadores.
  - **Ejemplo:** una aplicación heredada puede conservar un CLB con una configuración de cross-zone específica.

- **HTTP — Hypertext Transfer Protocol:** protocolo web interpretado por un ALB.
  - **Ejemplo:** el ALB distribuye solicitudes HTTP entre destinos.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP protegido mediante TLS.
  - **Ejemplo:** el mismo ALB puede recibir solicitudes HTTPS en un listener seguro.

- **TLS — Transport Layer Security:** protocolo que cifra y autentica comunicaciones en tránsito.
  - **Ejemplo:** HTTPS utiliza TLS para proteger una solicitud web.

## Idea central

Con cross-zone activado, la capacidad se considera entre zonas; desactivado, cada nodo depende de los destinos registrados en su zona.

**Ejemplo integrador:** hay dos destinos en `AZ-A` y ocho en `AZ-B`. Con cross-zone, los diez pueden compartir la carga total; sin cross-zone, la parte recibida por `AZ-A` se reparte solo entre sus dos destinos.

> **Complemento oficial de AWS:** en ALB el balanceo entre zonas permanece activado a nivel del Load Balancer, pero la documentación actual permite desactivarlo en target groups compatibles. La frase del documento fuente “no se puede desactivar” necesita este matiz.

## Load Balancer entre zonas

- Con cross-zone load balancing, cada instancia del Load Balancer distribuye uniformemente entre todas las instancias registradas en todas las AZ.
- Sin cross-zone load balancing, las solicitudes se distribuyen en instancias del nodo del Elastic Load Balancer.

| Tipo | Estado según fuente |
| --- | --- |
| ALB | Siempre activado; no se puede desactivar; no se cobra por datos inter-AZ. |
| NLB y GWLB | Desactivado por defecto; si se activa, se paga tarifa por datos entre zonas geográficas. |
| CLB | Desactivado por defecto; no se cobra por datos inter-AZ si está activado. |
