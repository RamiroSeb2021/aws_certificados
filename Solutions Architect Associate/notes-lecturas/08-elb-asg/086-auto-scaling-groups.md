# Visión general de Auto Scaling Groups (ASG)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 151–155.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 15: Auto Scaling Groups.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html).
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
- **ASG — Auto Scaling Group (grupo de escalado automático):** conjunto que mantiene una cantidad definida de instancias EC2 y puede ajustarla.
  - **Ejemplo:** conserva al menos dos servidores y aumenta hasta diez durante una promoción.
- **EC2 — Amazon Elastic Compute Cloud:** servicio para ejecutar computadoras virtuales.
  - **Ejemplo:** cada miembro del ASG es una instancia EC2.
- **Capacidad mínima, deseada y máxima:** límites y objetivo actual del número de instancias.
  - **Ejemplo:** mínimo `2`, deseado `4` y máximo `10` significa que el grupo intenta tener cuatro sin bajar de dos ni superar diez.
- **Launch template (plantilla de lanzamiento):** configuración usada para crear nuevas instancias.
  - **Ejemplo:** define la AMI, el tipo de instancia, la red y los grupos de seguridad.
- **AMI — Amazon Machine Image:** plantilla del sistema y software inicial de EC2.
  - **Ejemplo:** todas las instancias del grupo pueden iniciar desde la misma AMI preparada.
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques para EC2.
  - **Ejemplo:** la plantilla puede indicar qué volumen EBS crear con cada instancia.
- **IAM — AWS Identity and Access Management:** servicio que controla identidades y permisos en AWS.
  - **Ejemplo:** un rol IAM permite que la aplicación lea un bucket autorizado sin guardar claves estáticas.
- **SSH — Secure Shell:** protocolo de administración remota cifrada.
  - **Ejemplo:** un par de claves puede autorizar acceso SSH a Linux cuando sea necesario.
- **Load Balancer:** punto de entrada que distribuye tráfico entre instancias saludables.
  - **Ejemplo:** registra automáticamente las instancias nuevas del ASG.

- **ELB — Elastic Load Balancing:** servicio administrado que distribuye tráfico y puede comprobar la salud de destinos.
  - **Ejemplo:** un ASG registra sus instancias en un Load Balancer de ELB.

## Idea central

Un ASG administra la cantidad y salud de instancias; no distribuye por sí solo las solicitudes de usuarios.

**Ejemplo integrador:** el ASG detecta que una instancia no está sana, crea un reemplazo desde la launch template y el Load Balancer comienza a enviarle tráfico cuando supera sus comprobaciones.

## Auto Scaling Groups (ASG)

### Objetivo

- En la vida real, carga de sitios web y aplicaciones puede cambiar.
- En Cloud, se pueden crear y eliminar servidores rápidamente.
- Objetivos de ASG según fuente:
  - añadir instancias EC2 para adaptarse a aumento de carga;
  - eliminar instancias EC2 para ajustarse a disminución de carga;
  - asegurar mínimo y máximo de instancias EC2 en funcionamiento;
  - registrar nuevas instancias automáticamente en Load Balancer;
  - recrear instancia EC2 si se elimina una anterior o si no está sana.
- ASG son gratuitos; se paga por instancias EC2 subyacentes.

### Capacidad y Load Balancer

- ASG usa capacidad mínima, deseada y máxima.
- Puede ampliar escala según necesidad.
- Con Load Balancer, ELB puede comprobar salud de instancias EC2.

### Atributos de ASG

- Plantilla de lanzamiento; la fuente indica que configuraciones de lanzamiento antiguas están obsoletas.
- Incluye:
  - AMI y tipo de instancia;
  - EC2 User Data;
  - volúmenes EBS;
  - grupos de seguridad;
  - par de claves SSH;
  - roles IAM para instancias EC2;
  - información de red y subredes;
  - información de Load Balancer.
- Tamaño mínimo, máximo y capacidad inicial.
- Políticas de escalado.
