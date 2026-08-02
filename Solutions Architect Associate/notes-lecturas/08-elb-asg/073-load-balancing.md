# Load balancing y Elastic Load Balancing

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 124–130.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lecturas 2 y 3: ELB y nota sobre CLB.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) y [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html).
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
- **Load Balancer (balanceador de carga):** punto de entrada que recibe comunicaciones y las distribuye entre varios destinos.
  - **Ejemplo:** reparte cien solicitudes entre tres servidores saludables.
- **ELB — Elastic Load Balancing:** familia administrada de balanceadores de carga de AWS.
  - **Ejemplo:** AWS mantiene la infraestructura del balanceador mientras el cliente configura listeners, reglas y destinos.
- **Target (destino):** recurso que recibe el tráfico enviado por el balanceador.
  - **Ejemplo:** una instancia EC2 que ejecuta la aplicación es un target.
- **Target group (grupo de destino):** conjunto lógico de destinos a los que una regla puede reenviar tráfico.
  - **Ejemplo:** el grupo `servidores-web` contiene tres instancias EC2.
- **Health check (comprobación de estado):** solicitud periódica para comprobar si un destino puede atender tráfico.
  - **Ejemplo:** si `/health` deja de responder correctamente, el balanceador evita enviarle nuevas solicitudes.
- **DNS — Domain Name System:** sistema que traduce nombres a direcciones de red.
  - **Ejemplo:** el cliente accede al nombre DNS del Load Balancer en vez de conocer cada servidor.
- **HTTP — Hypertext Transfer Protocol:** protocolo de solicitudes y respuestas utilizado por la Web.
  - **Ejemplo:** un navegador envía una solicitud HTTP para obtener una página.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP protegido mediante TLS.
  - **Ejemplo:** una compra viaja cifrada al abrir una URL que comienza por `https://`.
- **TCP — Transmission Control Protocol:** protocolo de transporte orientado a conexión y entrega ordenada.
  - **Ejemplo:** una conexión a una base de datos suele utilizar TCP.
- **UDP — User Datagram Protocol:** protocolo de transporte sin una conexión persistente ni garantía de entrega incorporada.
  - **Ejemplo:** ciertos sistemas de tiempo real priorizan rapidez usando UDP.
- **ALB — Application Load Balancer:** balanceador de capa de aplicación para HTTP y HTTPS.
  - **Ejemplo:** envía `/imagenes` y `/usuarios` a grupos diferentes.
- **NLB — Network Load Balancer:** balanceador de red para tráfico como TCP, UDP y TLS.
  - **Ejemplo:** distribuye conexiones TCP que necesitan alto rendimiento.
- **GWLB — Gateway Load Balancer:** balanceador para flotas de dispositivos virtuales de red.
  - **Ejemplo:** distribuye paquetes entre varias instancias de firewall.
- **CLB — Classic Load Balancer:** generación anterior de Elastic Load Balancing.
  - **Ejemplo:** una aplicación antigua puede seguir usando un CLB, aunque AWS recomienda generaciones actuales para diseños nuevos.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden registrarse como destinos.
  - **Ejemplo:** un target group contiene tres instancias EC2.
- **AZ — Availability Zone:** Zona de Disponibilidad aislada dentro de una región.
  - **Ejemplo:** el balanceador distribuye tráfico entre destinos de varias AZ habilitadas.
- **IP — Internet Protocol:** sistema de direccionamiento y envío de paquetes en una red.
  - **Ejemplo:** un target puede registrarse mediante una dirección IP privada compatible.
- **TLS — Transport Layer Security:** protocolo moderno de cifrado y autenticación en tránsito.
  - **Ejemplo:** un listener TLS protege una conexión de red.
- **SSL — Secure Sockets Layer:** antecesor histórico de TLS; el nombre todavía aparece en expresiones heredadas.
  - **Ejemplo:** “terminación SSL” suele referirse actualmente a terminar una conexión TLS.
- **ACM — AWS Certificate Manager:** servicio para administrar certificados.
  - **Ejemplo:** un ALB usa un certificado de ACM en su listener HTTPS.
- **ECS — Amazon Elastic Container Service:** servicio administrado para ejecutar contenedores.
  - **Ejemplo:** un ALB registra tareas ECS como destinos.
- **WAF — AWS Web Application Firewall:** firewall para filtrar solicitudes web según reglas.
  - **Ejemplo:** AWS WAF puede bloquear un patrón malicioso antes de que llegue a la aplicación.
- **GENEVE — Generic Network Virtualization Encapsulation:** protocolo usado por GWLB para encapsular tráfico hacia dispositivos virtuales.
  - **Ejemplo:** GWLB usa GENEVE en el puerto `6081`.

## Idea central

El Load Balancer desacopla al cliente de los servidores concretos: el cliente usa un punto de entrada y el balanceador elige un destino saludable.

**Ejemplo integrador:** `tienda.example.com` apunta al balanceador. Si una de tres instancias falla su health check, las solicitudes nuevas se reparten entre las otras dos.

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
