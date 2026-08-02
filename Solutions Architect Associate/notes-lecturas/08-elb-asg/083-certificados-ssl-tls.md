# Certificados SSL/TLS en Elastic Load Balancing

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 146–149.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 12: Certificados SSL/TLS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [SSL/TLS certificates for Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html) e [Infrastructure security in Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/infrastructure-security.html).
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
- **TLS — Transport Layer Security (seguridad de la capa de transporte):** protocolo actual que cifra la comunicación y permite verificar la identidad presentada por el servidor.
  - **Ejemplo:** TLS protege una contraseña mientras viaja del navegador al Load Balancer.
- **SSL — Secure Sockets Layer (capa de sockets seguros):** antecesor histórico de TLS; el nombre “certificado SSL” todavía se usa de manera coloquial.
  - **Ejemplo:** cuando una consola habla de “SSL/TLS”, normalmente la conexión moderna utiliza TLS.
- **HTTPS — Hypertext Transfer Protocol Secure (protocolo seguro de transferencia de hipertexto):** HTTP transportado dentro de una conexión protegida por TLS.
  - **Ejemplo:** `https://tienda.example.com` indica que el navegador espera una conexión cifrada.
- **Certificado digital SSL/TLS:** identificación digital X.509 emitida y firmada por una autoridad certificadora. Vincula una identidad, como un dominio, con una clave pública e incluye datos que permiten revisar quién lo emitió y durante qué periodo es válido.
  - **Ejemplo:** el certificado presentado para `tienda.example.com` permite que el navegador compruebe que el dominio solicitado coincide con la identidad indicada en el certificado.
- **X.509:** estándar de formato utilizado por certificados de servidor.
  - **Ejemplo:** un listener HTTPS presenta al cliente un certificado X.509.
- **CA — Certificate Authority (autoridad certificadora):** entidad que emite y firma certificados digitales para que otros puedan verificar su procedencia.
  - **Ejemplo:** el navegador confía en una CA reconocida y puede validar la firma del certificado.
- **ACM — AWS Certificate Manager (administrador de certificados de AWS):** servicio de AWS para aprovisionar y administrar certificados.
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

## Qué es realmente un certificado SSL/TLS

Un certificado SSL/TLS es una identificación digital que el servidor o el Load Balancer presenta al cliente durante el inicio de una conexión segura. Su propósito es aportar información verificable sobre la identidad del dominio y proporcionar la clave pública necesaria para el proceso criptográfico de TLS.

**Ejemplo:** cuando una persona entra en `https://tienda.example.com`, el ALB presenta un certificado cuyo dominio debe coincidir con `tienda.example.com`.

### Qué problema resuelve

Sin una verificación de identidad, un navegador no tendría una prueba digital suficiente para saber si el extremo que responde por un dominio presenta credenciales emitidas para ese nombre. TLS utiliza el certificado para autenticar la identidad presentada y establecer comunicación cifrada.

**Ejemplo:** antes de enviar una contraseña a `tienda.example.com`, el navegador revisa el certificado presentado y solo continúa normalmente si puede verificarlo para ese dominio.

### Analogía: un documento de identidad, pero digital

Una analogía útil es pensar en el certificado como un documento de identidad:

- indica para quién fue emitido;
- muestra quién lo emitió;
- tiene un periodo de vigencia;
- lleva una firma que permite comprobar su procedencia.

**Ejemplo:** así como una persona revisa el nombre, la entidad emisora y la vigencia de un documento, el navegador revisa datos equivalentes del certificado de `tienda.example.com`.

La analogía solo ayuda a entender la función. Técnicamente, el certificado es un objeto digital X.509 que contiene campos e información criptográfica; no es una imagen escaneada ni una tarjeta física.

**Ejemplo:** el ALB entrega datos digitales del certificado durante la negociación TLS, no una fotografía de un documento.

### Qué información contiene

- **Identidad o dominio:** nombre para el que se emitió el certificado.
  - **Ejemplo:** `tienda.example.com` debe coincidir con el dominio utilizado por el cliente.
- **Clave pública:** información criptográfica pública incluida en el certificado y utilizada por el protocolo TLS durante el establecimiento de la conexión segura.
  - **Ejemplo:** el navegador obtiene del certificado la clave pública asociada con la identidad presentada por `tienda.example.com`.
- **Periodo de validez:** intervalo durante el cual el certificado se considera vigente.
  - **Ejemplo:** si el certificado de la tienda está vencido, el navegador no lo acepta como un certificado vigente.
- **Emisor y firma digital del emisor:** identifican a la CA y permiten verificar que esa autoridad firmó el certificado.
  - **Ejemplo:** el navegador comprueba la firma de la CA en lugar de aceptar un certificado solo porque afirma pertenecer a la tienda.
- **Número de serie:** identificador asignado al certificado por su emisor.
  - **Ejemplo:** dos certificados renovados para el mismo dominio pueden tener números de serie diferentes.

> **Complemento oficial de AWS:** AWS describe el certificado X.509 como una identificación digital emitida por una CA que contiene información de identidad, periodo de validez, clave pública, número de serie y firma digital del emisor: [certificados SSL/TLS para Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html).

### Qué hace una autoridad certificadora

Una CA — Certificate Authority (autoridad certificadora) emite y firma el certificado. La firma permite que el cliente compruebe que el certificado fue emitido por esa autoridad y que no debe confiar únicamente en lo que el sitio dice sobre sí mismo.

**Ejemplo:** `tienda.example.com` presenta un certificado firmado por una CA; el navegador utiliza esa firma y su información de confianza para validar la procedencia del certificado.

ACM — AWS Certificate Manager (administrador de certificados de AWS) permite crear o importar certificados y desplegarlos en un Load Balancer compatible. ACM administra el certificado, pero una CA sigue siendo la entidad emisora del certificado público.

**Ejemplo:** el equipo solicita en ACM un certificado público para `tienda.example.com` y lo asocia con el listener HTTPS del ALB.

### Cómo se valida y se establece HTTPS

El flujo simplificado es el siguiente:

1. El navegador solicita `https://tienda.example.com` e inicia una negociación TLS con el ALB.
2. El ALB presenta el certificado configurado en su listener HTTPS.
3. El navegador verifica que el dominio del certificado coincide con `tienda.example.com`.
4. También revisa el periodo de validez y la firma del emisor para determinar si puede confiar en el certificado presentado.
5. Si la verificación es correcta, navegador y ALB completan la negociación TLS y establecen claves para proteger la comunicación.
6. A partir de ese momento, las solicitudes y respuestas HTTPS de ese tramo viajan cifradas.

**Ejemplo:** la contraseña enviada desde el navegador hacia el ALB de `tienda.example.com` viaja dentro de la conexión TLS establecida después de validar el certificado.

> **Complemento oficial de AWS:** Elastic Load Balancing admite listeners seguros para comunicación cifrada; un ALB admite listeners HTTPS y puede administrar sus certificados con ACM: [seguridad de infraestructura en Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/infrastructure-security.html).

### Ejemplo completo: `tienda.example.com` y un ALB

1. La empresa posee el dominio `tienda.example.com`.
2. Solicita mediante ACM un certificado para ese nombre y completa la validación requerida para el dominio.
3. Asocia el certificado con el listener HTTPS del Application Load Balancer.
4. Un cliente abre `https://tienda.example.com` en su navegador.
5. El ALB presenta el certificado durante la negociación TLS.
6. El navegador comprueba el nombre del dominio, la vigencia y la firma del emisor.
7. Si todo es válido, se establece la conexión HTTPS cifrada entre el navegador y el ALB.
8. El ALB descifra la solicitud en la terminación TLS y después la dirige a un target group mediante las reglas del listener.

**Qué demuestra el ejemplo:** el certificado permite autenticar la identidad presentada y establecer el tramo seguro; las reglas del listener, no el certificado, deciden a qué destino se envía la solicitud.

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
