# Escalabilidad y alta disponibilidad

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 119–123.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 1: Alta disponibilidad y escalabilidad.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
