# Snapshots de Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 98–99.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 3: Visión general de EBS Snapshots.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Snapshots de EBS

- Snapshot es una copia de seguridad de un volumen EBS en un momento dado.
- No es necesario separar el volumen para crear snapshot, pero se recomienda.
- Se pueden copiar snapshots entre AZ o regiones.

### Características de snapshots

- Archivo de snapshots EBS:
  - permite mover un snapshot a un nivel de archivo de menor costo, 75% más barato según la fuente;
  - restauración del archivo tarda entre 24 y 72 horas.
- Papelera de reciclaje para snapshots EBS:
  - permite configurar reglas para retener snapshots eliminados;
  - ayuda a recuperarlos tras borrado accidental;
  - retención especificable de 1 día a 1 año.
