# Gateway Load Balancer (GWLB)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 140–141.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 9: Gateway Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is a Gateway Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html).
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
- **GWLB — Gateway Load Balancer:** servicio que inserta y escala dispositivos virtuales de red dentro del recorrido del tráfico.
  - **Ejemplo:** distribuye paquetes entre varias instancias de firewall.
- **Gateway (puerta de enlace):** punto por el que el tráfico entra, sale o pasa hacia otra red o servicio.
  - **Ejemplo:** el tráfico de una VPC puede dirigirse a un gateway antes de llegar a su destino.
- **Firewall:** sistema que inspecciona comunicaciones y permite o bloquea tráfico según reglas.
  - **Ejemplo:** puede bloquear paquetes que llegan desde un origen prohibido.
- **Dispositivo virtual de red:** software que ejecuta funciones de red dentro de una máquina virtual.
  - **Ejemplo:** una instancia EC2 puede ejecutar un producto de inspección de seguridad.
- **IP — Internet Protocol:** protocolo de direccionamiento y envío de paquetes entre redes.
  - **Ejemplo:** cada paquete IP contiene información de origen y destino.
- **Capa 3:** capa de red, donde se manejan paquetes IP y su recorrido.
  - **Ejemplo:** GWLB dirige paquetes sin necesitar interpretar una ruta de aplicación web.
- **GENEVE — Generic Network Virtualization Encapsulation:** protocolo de encapsulación que transporta tráfico hacia y desde los dispositivos virtuales del GWLB.
  - **Ejemplo:** GWLB utiliza GENEVE en el puerto `6081` para comunicarse con sus destinos.
- **Target group:** conjunto de dispositivos virtuales registrados como destinos.
  - **Ejemplo:** un grupo puede contener cuatro instancias de inspección.

- **VPC — Virtual Private Cloud (nube privada virtual):** red virtual aislada que el cliente controla dentro de AWS.
  - **Ejemplo:** el tráfico de una VPC puede pasar por una flota de firewalls antes de llegar a la aplicación.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que puede ejecutar los dispositivos de red registrados.
  - **Ejemplo:** una instancia EC2 ejecuta un firewall virtual dentro del target group.

## Idea central

GWLB combina una puerta de enlace transparente con distribución de carga para que una flota de dispositivos inspeccione tráfico sin convertirse en un único punto de capacidad.

**Ejemplo integrador:** el tráfico entra a una VPC, pasa por GWLB, se distribuye a un firewall saludable y continúa hacia la aplicación después de la inspección.

## Gateway Load Balancer

- Implementa, escala y administra flota de dispositivos virtuales de red de terceros en AWS.
- Ejemplos fuente:
  - firewalls;
  - sistemas de detección y prevención de intrusiones;
  - inspección profunda de paquetes;
  - manipulación de cargas útiles.
- Opera en capa 3, paquetes IP.
- Combina:
  - gateway de red transparente como entrada/salida única para todo el tráfico;
  - load balancer para distribuir tráfico a dispositivos virtuales.
- Usa protocolo GENEVE en puerto `6081`.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas.
