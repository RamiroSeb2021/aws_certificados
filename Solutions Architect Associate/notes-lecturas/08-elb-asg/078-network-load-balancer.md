# Network Load Balancer (NLB)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 137–139.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 7: Network Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is a Network Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).
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
- **NLB — Network Load Balancer:** balanceador diseñado para tráfico de red de alto rendimiento.
  - **Ejemplo:** distribuye miles de conexiones TCP entre servidores de una aplicación.
- **Capa 4:** capa de transporte, donde el balanceador trabaja principalmente con protocolos, direcciones y puertos, sin analizar rutas HTTP como un ALB.
  - **Ejemplo:** puede decidir usando el puerto `5432`, pero no una ruta como `/usuarios`.
- **TCP — Transmission Control Protocol:** transporte orientado a conexión, con entrega ordenada.
  - **Ejemplo:** una conexión a PostgreSQL usa normalmente TCP.
- **UDP — User Datagram Protocol:** transporte basado en datagramas, sin garantía de entrega incorporada.
  - **Ejemplo:** una aplicación de tiempo real puede preferir UDP para reducir sobrecarga.
- **TLS — Transport Layer Security:** protocolo que cifra y autentica comunicaciones en tránsito.
  - **Ejemplo:** un listener TLS del NLB puede recibir una conexión cifrada.
- **IP — Internet Protocol:** sistema de direccionamiento para localizar interfaces en una red.
  - **Ejemplo:** un NLB puede registrar una dirección IP privada como destino.
- **AZ — Availability Zone:** Zona de Disponibilidad aislada dentro de una región.
  - **Ejemplo:** un NLB puede tener una dirección IP estática por AZ habilitada.
- **Elastic IP:** IPv4 pública estática asignada a la cuenta.
  - **Ejemplo:** puede asociarse una Elastic IP por AZ a un NLB orientado a Internet.
- **Health check:** comprobación periódica de que un destino puede recibir tráfico.
  - **Ejemplo:** si el puerto TCP del servidor no responde, el NLB deja de seleccionarlo.

- **ALB — Application Load Balancer:** balanceador que interpreta HTTP y HTTPS en la capa de aplicación.
  - **Ejemplo:** el NLB puede enviar tráfico hacia un ALB registrado como destino en un diseño compatible.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden registrarse como destinos del NLB.
  - **Ejemplo:** dos instancias EC2 reciben conexiones TCP desde el NLB.
- **HTTP — Hypertext Transfer Protocol:** protocolo de solicitudes y respuestas web.
  - **Ejemplo:** un health check HTTP solicita una ruta configurada.
- **HTTPS — Hypertext Transfer Protocol Secure:** HTTP protegido mediante TLS.
  - **Ejemplo:** un health check HTTPS comprueba una ruta usando una conexión cifrada.

## Idea central

Se elige NLB cuando importan el protocolo y el rendimiento de red; se elige ALB cuando se necesitan decisiones basadas en el contenido HTTP.

**Ejemplo integrador:** una aplicación recibe conexiones TCP en un puerto fijo y exige direcciones IP estáticas permitidas por clientes corporativos; un NLB distribuye esas conexiones entre destinos saludables.

## Network Load Balancer

- NLB permite reenviar tráfico TCP y UDP a instancias.
- Puede manejar millones de peticiones por segundo.
- Tiene menor latencia.
- Tiene IP estática por AZ y soporta asignación de Elastic IP, útil para permitir una IP específica.
- Se usa para rendimiento extremo y tráfico TCP o UDP.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas;
  - Application Load Balancer.
- Health checks soportan TCP, HTTP y HTTPS.
