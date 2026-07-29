# EBS Multi-Attach

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 109.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 9: Multi-Attach EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## EBS Multi-Attach

- Aplica a familia `io1/io2`.
- Adjunta el mismo volumen EBS a varias instancias EC2 en la misma AZ.
- Cada instancia tiene permisos completos de lectura y escritura.
- Caso de uso: mayor disponibilidad de aplicaciones en clusters Linux, por ejemplo Teradata.
- Las aplicaciones deben gestionar escrituras concurrentes.
- Hasta 16 instancias EC2 a la vez.
- Debe usarse sistema de archivos compatible con clúster; la fuente indica “no XFS, EX4, etc.”.
