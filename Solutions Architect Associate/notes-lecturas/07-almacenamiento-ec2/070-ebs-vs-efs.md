# Amazon EBS vs Amazon EFS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 116–117.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 14: EFS vs EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Choosing an AWS storage service](https://docs.aws.amazon.com/pdfs/decision-guides/latest/storage-on-aws-how-to-choose/storage-on-aws-how-to-choose.pdf).
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
- **EBS — Amazon Elastic Block Store:** almacenamiento por bloques persistente que se adjunta a instancias dentro de una AZ.
  - **Ejemplo:** una instancia usa un volumen EBS como disco del sistema operativo.
- **EFS — Amazon Elastic File System:** sistema de archivos compartido que varias instancias Linux pueden montar por red.
  - **Ejemplo:** varios servidores web comparten imágenes mediante EFS.
- **EC2 — Amazon Elastic Compute Cloud:** servicio para ejecutar computadoras virtuales.
  - **Ejemplo:** una instancia EC2 puede usar EBS para su disco y EFS para archivos compartidos.
- **Instance Store:** almacenamiento local y efímero conectado al servidor físico de la instancia.
  - **Ejemplo:** una aplicación usa Instance Store para una caché que puede reconstruir.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región.
  - **Ejemplo:** un volumen EBS pertenece a una AZ; un EFS regional puede atender montajes desde varias AZ.
- **Bloques frente a archivos:** EBS entrega bloques que el sistema operativo organiza; EFS ya presenta archivos y carpetas compartidos.
  - **Ejemplo:** EBS se parece a conectar un disco; EFS se parece a abrir una carpeta compartida en red.
- **IA — Infrequent Access:** clase de EFS para archivos de acceso poco frecuente.
  - **Ejemplo:** documentos antiguos pueden pasar a EFS IA para reducir el coste de almacenamiento.

- **I/O — Input/Output (entrada/salida):** operaciones de lectura y escritura realizadas contra el almacenamiento.
  - **Ejemplo:** un backup que lee muchos bloques consume capacidad de I/O.
- **POSIX — Portable Operating System Interface:** convenciones de sistemas tipo Unix para operaciones y permisos de archivos.
  - **Ejemplo:** EFS conserva propietarios y permisos que utiliza Linux.

## Idea central

La pregunta no es cuál servicio es mejor, sino qué necesita la carga: un disco persistente, archivos compartidos o almacenamiento local temporal.

**Ejemplo integrador:** una aplicación usa EBS para el sistema operativo, EFS para archivos que deben ver varios servidores e Instance Store para resultados temporales que puede recalcular.

## EBS vs EFS vs Instance Store

| Servicio | Recordatorio de fuente |
| --- | --- |
| EBS | Volúmenes adjuntos a una instancia a la vez; bloqueados a AZ; migración entre AZ mediante snapshot y restauración; backups consumen IO y no deberían ejecutarse con mucho tráfico; root EBS se termina por defecto si instancia se termina, salvo desactivación. |
| EFS | Puede montarse en cientos de instancias a través de AZ; comparte archivos de sitio web como WordPress; solo Linux/POSIX; precio más elevado que EBS; puede usar EFS-IA para ahorrar costes. |
| EC2 Instance Store | Alto rendimiento local; efímero; útil para caché, buffer y temporales; backups y replicación a cargo del usuario. |
