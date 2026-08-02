# Certificados SSL/TLS en Elastic Load Balancing

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 146–149.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 12: Certificados SSL/TLS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html).
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
- **TLS — Transport Layer Security:** protocolo actual que cifra la comunicación y permite verificar la identidad presentada por el servidor.
  - **Ejemplo:** TLS protege una contraseña mientras viaja del navegador al Load Balancer.
- **SSL — Secure Sockets Layer:** antecesor histórico de TLS; el nombre “certificado SSL” todavía se usa de manera coloquial.
  - **Ejemplo:** cuando una consola habla de “SSL/TLS”, normalmente la conexión moderna utiliza TLS.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP transportado dentro de una conexión protegida por TLS.
  - **Ejemplo:** `https://tienda.example.com` indica que el navegador espera una conexión cifrada.
- **Certificado digital:** documento firmado que vincula una identidad, como un dominio, con una clave pública.
  - **Ejemplo:** el certificado de `tienda.example.com` ayuda al navegador a comprobar que habla con ese dominio.
- **X.509:** estándar de formato utilizado por certificados de servidor.
  - **Ejemplo:** un listener HTTPS presenta al cliente un certificado X.509.
- **CA — Certificate Authority (autoridad certificadora):** entidad que valida y firma certificados.
  - **Ejemplo:** el navegador confía en una CA reconocida y puede validar la firma del certificado.
- **ACM — AWS Certificate Manager:** servicio de AWS para aprovisionar y administrar certificados.
  - **Ejemplo:** un ALB puede usar un certificado público administrado por ACM.
- **SNI — Server Name Indication:** extensión de TLS con la que el cliente indica el nombre de dominio solicitado al comenzar la conexión.
  - **Ejemplo:** el Load Balancer elige un certificado para `tienda.example.com` y otro para `api.example.com` usando SNI.
- **Handshake (negociación inicial):** intercambio inicial para acordar seguridad y establecer claves de sesión.
  - **Ejemplo:** durante el handshake el servidor presenta su certificado.
- **Listener:** componente que espera conexiones en un protocolo y puerto.
  - **Ejemplo:** un listener HTTPS escucha normalmente en el puerto `443`.

- **HTTP — Hypertext Transfer Protocol:** protocolo web sin la protección TLS incorporada.
  - **Ejemplo:** una regla puede redirigir HTTP del puerto `80` hacia HTTPS.
- **ALB — Application Load Balancer:** balanceador de capa de aplicación que admite múltiples certificados mediante SNI.
  - **Ejemplo:** un ALB sirve dos dominios con certificados distintos.
- **NLB — Network Load Balancer:** balanceador de red que puede usar listeners TLS.
  - **Ejemplo:** un NLB selecciona un certificado para una conexión TLS compatible.
- **CLB — Classic Load Balancer:** generación anterior con capacidades de certificados más limitadas.
  - **Ejemplo:** el curso indica un certificado por CLB.

## Idea central

El certificado demuestra una identidad y participa en el establecimiento del cifrado; NO decide a qué servidor se envía la solicitud.

**Ejemplo integrador:** el navegador solicita `api.example.com`, envía ese nombre mediante SNI, el ALB presenta el certificado correcto y después aplica las reglas del listener para escoger un target group.

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

## Modelo mental para entender TLS

1. El cliente abre una conexión HTTPS con el Load Balancer.
2. El Load Balancer presenta un certificado X.509 para demostrar la identidad del dominio.
3. Cliente y Load Balancer establecen una conexión cifrada: ese tramo queda protegido en tránsito.
4. El Load Balancer termina la conexión TLS y reenvía la solicitud al target group según el listener y sus reglas.
5. ACM puede administrar los certificados; el listener HTTPS necesita un certificado predeterminado.

### Por qué existe SNI

- Un mismo Load Balancer puede servir varios dominios.
- SNI permite que el cliente indique el hostname solicitado durante el inicio de la conexión TLS.
- Con ese dato, el Load Balancer selecciona el certificado correcto.
- Según la fuente, SNI funciona con ALB, NLB y CloudFront, pero no con CLB.

## Punto de confusión

- SSL es el nombre histórico; TLS es el protocolo más reciente, aunque coloquialmente se siga diciendo “certificado SSL”.
- El certificado no balancea tráfico: autentica el dominio y habilita cifrado. El listener y sus reglas deciden el enrutamiento.
