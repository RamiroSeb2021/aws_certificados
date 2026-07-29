# Hibernación de Amazon EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 90–92.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 8: Hibernación de EC2.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Hibernación de EC2

### Parar, terminar e iniciar

- Al parar una instancia, los datos del disco EBS se mantienen intactos en el siguiente arranque.
- Al terminar una instancia, se pierden los volúmenes EBS root que estén preparados para destruirse.
- En el primer arranque, el sistema operativo inicia y se ejecuta EC2 User Data.
- En arranques siguientes, inicia el sistema operativo.
- Luego inicia la aplicación y se calientan cachés; eso puede tardar.

### Qué hace EC2 Hibernate

- Conserva estado en memoria RAM.
- Hace que el arranque sea mucho más rápido porque el sistema operativo no se detiene/reinicia.
- Bajo el capó, el estado de RAM se escribe en un archivo en el volumen EBS root.
- El volumen EBS root debe estar encriptado.
- Casos de uso:
  - procesamiento de larga duración;
  - guardar estado de RAM;
  - servicios que tardan en inicializarse.

### Condiciones y límites indicados

- Familias soportadas: C3, C4, C5, I3, M3, M4, R3, R4, T2, T3, entre otras indicadas con puntos suspensivos en fuente.
- RAM debe ser inferior a 150 GB.
- No se soporta para instancias bare metal.
- AMI mencionadas: Amazon Linux 2, Linux AMI, Ubuntu, RHEL, CentOS y Windows, con puntos suspensivos en fuente.
- Volumen root debe ser EBS y estar encriptado.
- Disponible para instancias bajo demanda, reservadas y Spot.
- Una instancia no puede estar hibernada más de 60 días.
