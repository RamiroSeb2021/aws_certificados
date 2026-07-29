# Load balancing y Elastic Load Balancing

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 124–130.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lecturas 2 y 3: ELB y nota sobre CLB.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
