# Amazon EBS vs Amazon EFS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 116–117.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 14: EFS vs EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## EBS vs EFS vs Instance Store

| Servicio | Recordatorio de fuente |
| --- | --- |
| EBS | Volúmenes adjuntos a una instancia a la vez; bloqueados a AZ; migración entre AZ mediante snapshot y restauración; backups consumen IO y no deberían ejecutarse con mucho tráfico; root EBS se termina por defecto si instancia se termina, salvo desactivación. |
| EFS | Puede montarse en cientos de instancias a través de AZ; comparte archivos de sitio web como WordPress; solo Linux/POSIX; precio más elevado que EBS; puede usar EFS-IA para ahorrar costes. |
| EC2 Instance Store | Alto rendimiento local; efímero; útil para caché, buffer y temporales; backups y replicación a cargo del usuario. |
