# Visión general de Auto Scaling Groups (ASG)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 151–155.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 15: Auto Scaling Groups.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
