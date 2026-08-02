# Snapshots de Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 98–99.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 3: Visión general de EBS Snapshots.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html).
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo desde fundamentos.
- Cada concepto nuevo incluye una explicación sencilla y un ejemplo inmediato.
- Las siglas se desarrollan y explican en su primera aparición conceptual.
- Los límites y cifras del curso se preservan como contenido de la fuente y pueden cambiar; los complementos actuales se identifican por separado.

## Antes de empezar: conceptos y siglas

- **AWS — Amazon Web Services:** proveedor de servicios de nube utilizado en estas notas.
  - **Ejemplo:** AWS opera servicios de computación, almacenamiento, bases de datos y redes.
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques utilizado con EC2.
  - **Ejemplo:** un volumen EBS puede contener los archivos de una aplicación.
- **Snapshot:** copia de un volumen en un punto concreto del tiempo.
  - **Ejemplo:** un snapshot creado el lunes permite crear después otro volumen con el estado guardado ese lunes.
- **Copia incremental:** copia que almacena únicamente los bloques que cambiaron desde la copia anterior, aunque cada snapshot pueda restaurar el estado completo correspondiente.
  - **Ejemplo:** si solo cambia un archivo, el siguiente snapshot guarda los bloques modificados en lugar de duplicar todo el volumen.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región.
  - **Ejemplo:** un snapshot regional permite crear un volumen nuevo en otra AZ de la misma región.
- **Región:** área geográfica de AWS que contiene varias Zonas de Disponibilidad.
  - **Ejemplo:** un snapshot puede copiarse de `us-east-1` a `us-west-2` para ciertos planes de recuperación.
- **Restaurar:** crear o recuperar almacenamiento a partir de una copia guardada.
  - **Ejemplo:** se crea un volumen EBS nuevo desde un snapshot después de un borrado accidental.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales al que pueden adjuntarse volúmenes creados desde snapshots.
  - **Ejemplo:** una instancia EC2 monta un volumen restaurado después de una pérdida de datos.

## Idea central

Un snapshot no es un disco conectado a una instancia: es una copia administrada desde la cual pueden crearse nuevos volúmenes.

**Ejemplo integrador:** antes de una actualización riesgosa, se crea un snapshot. Si la actualización daña los datos, se restaura un volumen nuevo desde esa copia.

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
