# EC2 Instance Store

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 102–103.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 7: EC2 Instance Store.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## EC2 Instance Store

- EBS ofrece unidades de red con rendimiento bueno pero limitado.
- Para disco de hardware de alto rendimiento, la fuente usa EC2 Instance Store.
- Ofrece mejor rendimiento de E/S e IOPS muy altas.
- Pierde almacenamiento si la instancia se detiene; es efímero.
- Bueno para buffer, caché, datos de memoria virtual y contenido temporal.
- Hay riesgo de pérdida de datos si falla el hardware.
- Backups y replicación son responsabilidad del usuario.
