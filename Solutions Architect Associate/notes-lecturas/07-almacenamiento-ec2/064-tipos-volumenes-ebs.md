# Tipos de volúmenes EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 104–108.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 8: Tipos de volúmenes EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Tipos de volúmenes EBS

- Tipos mencionados:
  - `gp2` / `gp3` SSD: propósito general, equilibrio precio/rendimiento para variedad de cargas.
  - `io1` / `io2` SSD: mayor rendimiento para cargas de misión crítica con baja latencia o alto rendimiento.
  - `st1` HDD: bajo coste para cargas de acceso frecuente y alto rendimiento.
  - `sc1` HDD: HDD más barato para acceso menos frecuente.
- Se caracterizan por tamaño, rendimiento e IOPS.
- La fuente recomienda consultar documentación AWS en caso de duda.
- Solo `gp2/gp3` e `io1/io2` pueden usarse como volúmenes de arranque.

### Casos de uso por tipo

| Tipo | Datos de fuente |
| --- | --- |
| SSD propósito general | Rentable, baja latencia; volúmenes de arranque, escritorios virtuales, desarrollo y prueba; 1 GiB–16 TiB. |
| `gp3` | Base de 3.000 IOPS y 125 MiB/s; puede aumentar IOPS hasta 16.000 y rendimiento hasta 1000 MiB/s independientemente. |
| `gp2` | Volúmenes pequeños pueden usar ráfagas de IOPS hasta 3.000; tamaño e IOPS vinculados; IOPS máximas 16.000; 3 IOPS por GB, con 5.334 GB se llega al máximo. |
| PIOPS SSD `io1/io2` | Aplicaciones críticas con IOPS sostenidas o más de 16.000 IOPS; excelente para bases de datos sensibles a rendimiento y consistencia. |
| `io1/io2` | 4 GiB–16 TiB; PIOPS máximos: 64.000 para Nitro y 32.000 para otras instancias; PIOPS independientes del tamaño; `io2` más durabilidad y más IOPS por GiB al mismo precio que `io1`. |
| `io2 Block Express` | 4 GiB–64 TiB; latencia menor a un milisegundo; PIOPS máximas 256.000 con relación IOPS:GiB de 1.000:1. |
| HDD `st1` | No puede ser volumen de arranque; 125 GiB–16 TiB; Big Data, data warehouses, procesamiento de logs; rendimiento máximo 500 MiB/s e IOPS máximo 500. |
| HDD `sc1` | Datos de acceso poco frecuente; menor coste; rendimiento máximo 250 MiB/s e IOPS máximas 250. |
