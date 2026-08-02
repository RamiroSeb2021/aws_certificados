# Application Load Balancer (ALB v2)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 131–136.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 4: Application Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) y [Target groups for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).
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
- **ALB — Application Load Balancer:** balanceador que entiende solicitudes HTTP y HTTPS y toma decisiones usando su contenido.
  - **Ejemplo:** puede enviar `/api` a un servicio y `/imagenes` a otro.
- **Capa 7:** capa de aplicación del modelo de redes, donde existen protocolos como HTTP.
  - **Ejemplo:** en esta capa el ALB puede leer la ruta y las cabeceras de una solicitud.
- **HTTP — Hypertext Transfer Protocol:** protocolo de solicitudes y respuestas de aplicaciones web.
  - **Ejemplo:** `GET /usuarios` pide al servidor la ruta `/usuarios`.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP cifrado y autenticado mediante TLS.
  - **Ejemplo:** un ALB puede recibir HTTPS y redirigir una solicitud HTTP hacia HTTPS.
- **URL — Uniform Resource Locator:** dirección que identifica un recurso y puede incluir protocolo, host, ruta y parámetros.
  - **Ejemplo:** `https://example.com/users?id=123` contiene host, ruta y query string.
- **Query string:** parámetros escritos después de `?` en una URL.
  - **Ejemplo:** en `?id=123`, el parámetro `id` vale `123`.
- **Cabecera HTTP:** metadato que acompaña la solicitud o respuesta.
  - **Ejemplo:** una cabecera puede indicar el tipo de contenido aceptado.
- **Listener:** componente que espera conexiones en un protocolo y puerto configurados.
  - **Ejemplo:** un listener HTTPS escucha normalmente en el puerto `443`.
- **Target group:** conjunto de destinos al que reenvía una regla.
  - **Ejemplo:** un target group puede contener instancias EC2 que sirven la API.
- **ECS — Amazon Elastic Container Service:** servicio administrado para ejecutar contenedores.
  - **Ejemplo:** un ALB puede dirigir solicitudes a tareas de ECS.
- **JSON — JavaScript Object Notation:** formato textual estructurado para intercambiar datos.
  - **Ejemplo:** una solicitud a Lambda puede convertirse en un evento JSON.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden actuar como targets.
  - **Ejemplo:** un target group registra dos instancias EC2.
- **IP — Internet Protocol:** sistema de direccionamiento de red.
  - **Ejemplo:** un ALB puede registrar una dirección IP privada como target compatible.
- **TLS — Transport Layer Security:** protocolo que protege HTTPS.
  - **Ejemplo:** el listener HTTPS usa TLS antes de aplicar sus reglas HTTP.
- **API — Application Programming Interface:** interfaz que permite que programas intercambien operaciones y datos.
  - **Ejemplo:** `/api/orders` puede ser la ruta de una API de pedidos.
- **CLB — Classic Load Balancer:** generación anterior del balanceador de AWS.
  - **Ejemplo:** el documento fuente lo compara con el enrutamiento más flexible del ALB.

## Idea central

El ALB no solo reparte solicitudes: puede leer información de HTTP y aplicar reglas para elegir el grupo de destino correcto.

**Ejemplo integrador:** un único ALB recibe `example.com/users` y `example.com/orders`; una regla envía cada ruta al microservicio correspondiente.

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
