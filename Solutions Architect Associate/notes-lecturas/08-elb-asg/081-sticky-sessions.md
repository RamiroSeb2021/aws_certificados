# Sticky Sessions — sesiones persistentes

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 142–143.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 10: Sticky Sessions.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Sticky sessions for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#sticky-sessions).
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
- **Sticky session (sesión persistente o afinidad de sesión):** regla que intenta enviar las solicitudes de un cliente al mismo destino durante cierto tiempo.
  - **Ejemplo:** después de iniciar sesión, las solicitudes de Ana continúan llegando al servidor `A`.
- **Sesión:** estado que una aplicación conserva sobre la interacción de un usuario.
  - **Ejemplo:** el contenido temporal del carrito de compras puede pertenecer a la sesión.
- **Cookie del navegador:** pequeño dato compuesto por un nombre, un valor y, según el caso, reglas como su dominio y vencimiento. Un sitio web o un balanceador lo envía al navegador; este lo conserva en el almacenamiento de cookies asociado al sitio y lo devuelve cuando una solicitud posterior cumple esas reglas.
  - **Ejemplo:** el ALB envía una cookie llamada `AWSALB`; el navegador la guarda para `tienda.example.com` y la incluye cuando vuelve a solicitar una página de esa tienda.
- **Backend:** parte de la aplicación que procesa las solicitudes detrás del punto de entrada.
  - **Ejemplo:** tres instancias EC2 forman el backend de una tienda.
- **ALB — Application Load Balancer:** balanceador de solicitudes HTTP y HTTPS.
  - **Ejemplo:** un ALB puede aplicar persistencia basada en cookies en un target group.
- **CLB — Classic Load Balancer:** generación anterior de balanceador de AWS.
  - **Ejemplo:** `AWSELB` es el nombre histórico de una cookie generada por CLB.
- **NLB — Network Load Balancer:** balanceador de tráfico de red.
  - **Ejemplo:** NLB puede utilizar afinidad de IP de origen para target groups compatibles, no las mismas cookies HTTP del ALB.
- **Target group:** conjunto de destinos que reciben solicitudes.
  - **Ejemplo:** la persistencia se configura para mantener al cliente unido a un destino del grupo.

- **ELB — Elastic Load Balancing:** familia administrada de balanceadores de AWS.
  - **Ejemplo:** ALB, NLB y CLB pertenecen a Elastic Load Balancing.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden ejecutar el backend.
  - **Ejemplo:** una cookie persistente mantiene al cliente asociado con una instancia EC2.
- **HTTP — Hypertext Transfer Protocol:** protocolo de solicitudes y respuestas web en el que viajan las cookies.
  - **Ejemplo:** el navegador devuelve la cookie en una cabecera HTTP.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP protegido mediante TLS.
  - **Ejemplo:** la cookie también se envía dentro de solicitudes HTTPS cuando corresponde.
- **IP — Internet Protocol:** sistema de direccionamiento de red.
  - **Ejemplo:** una afinidad compatible de NLB puede basarse en la IP de origen.
- **`AWSALB`, `AWSALBAPP`, `AWSALBTG` y `AWSELB`:** nombres reservados de cookies del balanceador; son identificadores, no conceptos que deban traducirse palabra por palabra.
  - **Ejemplo:** una aplicación no debe elegir `AWSALB` como nombre de su cookie personalizada.

- **TLS — Transport Layer Security:** protocolo que cifra y autentica comunicaciones en tránsito.
  - **Ejemplo:** HTTPS utiliza TLS para proteger una solicitud web.

## Qué es una cookie del navegador

Una cookie es un dato corto que permite que un sitio reconozca información entre una solicitud y la siguiente. El navegador la conserva conceptualmente en su propio almacén de cookies, separada por sitio y sujeta a reglas como el dominio y la fecha de vencimiento.

**Ejemplo:** `tienda.example.com` puede enviar una cookie llamada `carrito` con un identificador. Cuando el navegador regresa a esa tienda, puede devolver el mismo identificador.

La cookie **no es un programa ni un archivo ejecutable**: el navegador no la ejecuta como si fuera una aplicación. Es información que acompaña ciertas comunicaciones web.

**Ejemplo:** una cookie puede contener un identificador como `cliente-123`; ese texto no puede instalar ni abrir por sí solo un programa en la computadora.

La cookie tampoco es necesariamente la sesión completa. Puede funcionar como una etiqueta que permite localizar información guardada en otro lugar, o como una señal de afinidad que el balanceador utiliza para recordar un destino.

**Ejemplo:** el carrito con tres productos puede permanecer en el servidor `A`, mientras la cookie solo ayuda a relacionar las siguientes solicitudes del navegador con ese servidor.

### Cómo viaja una cookie

**HTTP — Hypertext Transfer Protocol (protocolo de transferencia de hipertexto)** y **HTTPS — Hypertext Transfer Protocol Secure (HTTP seguro)** organizan la comunicación web como solicitudes del cliente y respuestas del servidor. HTTPS protege esa comunicación mediante TLS.

**Ejemplo:** el navegador solicita la página de un producto y la tienda responde con el contenido de esa página.

Una **cabecera HTTP** es un campo de información adicional que acompaña una solicitud o una respuesta.

**Ejemplo:** una respuesta puede usar una cabecera `Set-Cookie` para pedirle al navegador que conserve una cookie; una solicitud posterior puede usar la cabecera `Cookie` para devolverla.

El recorrido simplificado es el siguiente:

1. El navegador envía una solicitud HTTP o HTTPS sin la cookie de persistencia porque todavía no la ha recibido.
2. El ALB selecciona un destino del target group, por ejemplo el servidor `A`.
3. La respuesta incluye una cookie generada por el balanceador, por ejemplo `AWSALB`.
4. El navegador conserva esa cookie dentro de su almacenamiento de cookies para el sitio correspondiente.
5. En una solicitud posterior compatible, el navegador envía la cookie junto con la solicitud.
6. El ALB lee la cookie y dirige la solicitud al mismo destino mientras la persistencia siga vigente y el destino pueda recibir tráfico.

**Ejemplo:** la primera solicitud de Ana llega al servidor `A`; al regresar a otra página de la tienda, su navegador devuelve `AWSALB` y el ALB vuelve a elegir el servidor `A`.

> **Complemento oficial de AWS:** AWS documenta que las sticky sessions requieren clientes compatibles con cookies. Para la persistencia basada en duración, el ALB genera `AWSALB`, la incluye en la respuesta y espera que el cliente la devuelva en solicitudes posteriores. Si la cookie vence, deja de existir la afinidad asociada: [atributos de target groups y sticky sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#sticky-sessions).

## Idea central

La persistencia resuelve aplicaciones que guardan estado en un servidor concreto, pero puede repartir la carga de manera desigual.

**Ejemplo integrador:** cien clientes llegan al ALB. Aunque un servidor quede más ocupado, cada cliente vuelve al destino asociado hasta que vence su cookie. Una alternativa más escalable es guardar la sesión en un almacén compartido.

## Sticky Sessions

- Permiten persistencia para que el mismo cliente sea redirigido a la misma instancia detrás de un Load Balancer.
- Funciona para Classic Load Balancer, Application Load Balancer y Network Load Balancer.
- Para CLB y ALB, la cookie de persistencia tiene fecha de expiración controlada por el usuario.
- Caso de uso: que el usuario no pierda datos de sesión.
- Puede provocar desbalanceo de carga entre instancias EC2 backend.

### Ejemplo paso a paso: carrito y afinidad

1. Ana abre una tienda que distribuye solicitudes entre los servidores `A` y `B` mediante un ALB.
2. El ALB envía la primera solicitud al servidor `A`.
3. Ana agrega un libro al carrito y la aplicación mantiene la información de esa sesión en el servidor `A`.
4. El ALB devuelve una cookie de persistencia y el navegador de Ana la conserva.
5. Ana abre la página de pago; el navegador devuelve la cookie en esa nueva solicitud HTTPS.
6. El ALB reconoce la afinidad y envía la solicitud nuevamente al servidor `A`, donde se encuentra la información temporal del carrito.
7. Si la cookie vence, la sesión deja de ser persistente para el balanceador y una solicitud posterior puede ser asignada a otro destino saludable.

**Qué demuestra el ejemplo:** la cookie ayuda al ALB a mantener la afinidad con un servidor. No contiene obligatoriamente todo el carrito ni constituye por sí sola toda la sesión.

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
