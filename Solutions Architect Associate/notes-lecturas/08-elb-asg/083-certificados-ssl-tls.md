# Certificados SSL/TLS en Elastic Load Balancing

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 146–149.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 12: Certificados SSL/TLS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
