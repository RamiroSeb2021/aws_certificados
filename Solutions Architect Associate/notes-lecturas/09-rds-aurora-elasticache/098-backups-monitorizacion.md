# RDS y Aurora — copias de seguridad y monitorización

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 180–183.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 8: Copia de seguridad y monitorización.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Copias de seguridad de RDS

- Copia completa diaria durante la ventana de mantenimiento.
- Logs de transacciones respaldados cada 5 minutos.
- Permite restaurar a un punto en el tiempo desde la copia más antigua hasta hace 5 minutos.
- Retención automática de 1 a 35 días; `0` desactiva las copias automáticas en RDS, según fuente.
- Los snapshots manuales se conservan durante el tiempo elegido por el usuario.

## Copias de seguridad de Aurora

- Retención automática de 1 a 35 días y no se puede desactivar.
- Recuperación a un punto en el tiempo.
- Snapshots manuales con retención administrada por el usuario.

## Restauración y clonación

- Restaurar backup o snapshot crea una nueva base de datos.
- La fuente describe restauración de RDS MySQL y Aurora MySQL desde Amazon S3.
- La clonación Aurora usa `copy-on-write`: comparte inicialmente el volumen y separa bloques cuando cambian.
- Es útil para crear staging desde producción con rapidez y sin afectar la base original.

## Monitorización

- RDS ofrece dashboards de monitorización.
- Los logs de auditoría pueden enviarse a CloudWatch Logs para aumentar su retención.
