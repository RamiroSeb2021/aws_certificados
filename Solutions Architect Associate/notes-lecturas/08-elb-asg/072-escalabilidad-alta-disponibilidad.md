# Escalabilidad y alta disponibilidad

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 119–123.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 1: Alta disponibilidad y escalabilidad.
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
- **Escalabilidad:** capacidad de un sistema para atender más o menos trabajo ajustando sus recursos.
  - **Ejemplo:** una tienda añade servidores durante una promoción y los reduce cuando termina.
- **Escalado vertical:** aumentar o reducir la capacidad de una sola máquina.
  - **Ejemplo:** cambiar una instancia de `t3.small` a `t3.large` le asigna más capacidad.
- **Escalado horizontal:** aumentar o reducir la cantidad de máquinas que trabajan juntas.
  - **Ejemplo:** pasar de dos servidores web a seis distribuye más solicitudes.
- **Alta disponibilidad:** diseño que intenta mantener el servicio funcionando aunque falle un componente o una ubicación.
  - **Ejemplo:** si una AZ falla, otra AZ continúa atendiendo la aplicación.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación físicamente aislada dentro de una región de AWS.
  - **Ejemplo:** una aplicación ejecutada en `us-east-1a` y `us-east-1b` no depende de una sola AZ.
- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales de AWS.
  - **Ejemplo:** cada servidor web puede ser una instancia EC2.
- **ASG — Auto Scaling Group (grupo de escalado automático):** conjunto que mantiene y ajusta una cantidad de instancias EC2.
  - **Ejemplo:** un ASG puede mantener como mínimo dos instancias y aumentar hasta seis.
- **ELB — Elastic Load Balancing:** servicio que distribuye tráfico entre destinos disponibles.
  - **Ejemplo:** ELB reparte solicitudes entre las instancias creadas por un ASG.
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** una base RDS puede usar una implementación Multi-AZ para disponibilidad.
- **vCPU — virtual Central Processing Unit:** unidad de capacidad de procesamiento virtual asignada a una instancia.
  - **Ejemplo:** una instancia con más vCPU puede ejecutar más trabajo de procesamiento simultáneo.

- **RAM — Random Access Memory:** memoria rápida usada por programas y datos activos.
  - **Ejemplo:** una instancia más grande puede proporcionar más RAM a una base de datos.

## Idea central

Escalar responde a cambios de carga; alta disponibilidad responde a fallos. Un diseño puede necesitar ambas cosas, pero NO significan lo mismo.

**Ejemplo integrador:** un ASG ejecuta al menos dos instancias en AZ diferentes y un Load Balancer distribuye las solicitudes. El grupo añade instancias cuando sube la carga y conserva servicio si una instancia falla.

## Escalabilidad y alta disponibilidad

- Escalabilidad: una aplicación o sistema puede manejar mayores cargas adaptándose.
- Tipos de escalabilidad:
  - vertical;
  - horizontal, también llamada elasticidad.
- La escalabilidad está vinculada a la alta disponibilidad, pero no es lo mismo.

### Escalabilidad vertical

- Significa aumentar tamaño de instancia.
- Ejemplo fuente: pasar de `t2.micro` a `t2.large`.
- Es común para sistemas no distribuidos, como bases de datos.
- RDS y ElastiCache pueden escalar verticalmente.
- Suele existir límite de escalabilidad vertical por hardware.

### Escalabilidad horizontal

- Significa aumentar número de instancias o sistemas de la aplicación.
- Implica sistemas distribuidos.
- Es común en aplicaciones web y aplicaciones modernas.
- La fuente indica que es fácil escalar horizontalmente gracias a ofertas cloud como Amazon EC2.

### Alta disponibilidad

- Suele ir de la mano del escalado horizontal.
- Significa ejecutar aplicación o sistema en al menos 2 centros de datos, equivalentes a Zonas de Disponibilidad.
- Objetivo: sobrevivir a pérdida de un centro de datos.
- Puede ser pasiva, por ejemplo RDS Multi-AZ.
- Puede ser activa, por ejemplo escalado horizontal.

### En EC2

- Escalado vertical: cambiar tamaño de instancia; ejemplo fuente de `t2.nano` con 0,5 GB RAM y 1 vCPU hasta `u-12tb1.metal` con 12,3 TB RAM y 448 vCPUs.
- Escalado horizontal: aumentar número de instancias mediante Auto Scaling Group y Load Balancer.
- Alta disponibilidad: ejecutar instancias de la misma aplicación en múltiples AZ mediante ASG multi-AZ y Load Balancer multi-AZ.
