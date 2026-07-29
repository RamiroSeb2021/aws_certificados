# Visión general de Amazon RDS y autoescalado de almacenamiento

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 161–163.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 1: Visión general de Amazon RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Qué es Amazon RDS

- RDS significa `Relational Database Service`.
- Es un servicio administrado para bases de datos relacionales que utilizan SQL.
- Motores mencionados: PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server y Aurora.

## RDS administrado vs base de datos en EC2

- RDS automatiza aprovisionamiento y parcheo del sistema operativo.
- Ofrece copias continuas y restauración a un punto en el tiempo.
- Incluye dashboards de monitorización, réplicas de lectura, Multi-AZ, ventanas de mantenimiento y escalado.
- El almacenamiento se respalda con EBS, según la fuente `gp2` o `io1`.
- En RDS estándar no se accede por SSH a la instancia subyacente.

## Autoescalado de almacenamiento

- Aumenta dinámicamente el almacenamiento cuando RDS detecta poco espacio libre.
- Se define un umbral máximo para limitar el crecimiento.
- La fuente indica que modifica el almacenamiento si:
  - queda menos del 10 % del almacenamiento asignado;
  - esa condición dura al menos 5 minutos;
  - han pasado 6 horas desde la última modificación.
- Es útil para cargas imprevisibles y soporta los motores RDS enumerados en la diapositiva.

## Claves de repaso

- RDS reduce trabajo operativo; no elimina la necesidad de diseñar motor, capacidad, disponibilidad y seguridad.
- Autoescalado de almacenamiento aumenta espacio, no capacidad de CPU ni número de réplicas.
