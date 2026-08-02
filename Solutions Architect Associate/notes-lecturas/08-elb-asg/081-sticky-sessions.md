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
- **Cookie:** pequeño dato que un servidor envía al navegador y que este devuelve en solicitudes posteriores.
  - **Ejemplo:** el balanceador usa una cookie para reconocer la afinidad del cliente.
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

## Idea central

La persistencia resuelve aplicaciones que guardan estado en un servidor concreto, pero puede repartir la carga de manera desigual.

**Ejemplo integrador:** cien clientes llegan al ALB. Aunque un servidor quede más ocupado, cada cliente vuelve al destino asociado hasta que vence su cookie. Una alternativa más escalable es guardar la sesión en un almacén compartido.

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
