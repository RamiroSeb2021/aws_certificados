# Balanceo de cargas entre zonas

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 144–145.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 11: Balanceo de carga entre zonas.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Load Balancer entre zonas

- Con cross-zone load balancing, cada instancia del Load Balancer distribuye uniformemente entre todas las instancias registradas en todas las AZ.
- Sin cross-zone load balancing, las solicitudes se distribuyen en instancias del nodo del Elastic Load Balancer.

| Tipo | Estado según fuente |
| --- | --- |
| ALB | Siempre activado; no se puede desactivar; no se cobra por datos inter-AZ. |
| NLB y GWLB | Desactivado por defecto; si se activa, se paga tarifa por datos entre zonas geográficas. |
| CLB | Desactivado por defecto; no se cobra por datos inter-AZ si está activado. |
