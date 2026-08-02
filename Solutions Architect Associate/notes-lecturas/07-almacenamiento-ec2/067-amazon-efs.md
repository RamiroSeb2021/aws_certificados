# Amazon EFS — Elastic File System

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 112–115.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 11: Amazon EFS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) y [Amazon EFS performance specifications](https://docs.aws.amazon.com/efs/latest/ug/performance.html).
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
- **EFS — Amazon Elastic File System:** almacenamiento de archivos administrado, elástico y compartido.
  - **Ejemplo:** varias instancias EC2 pueden leer los mismos archivos de un sitio web desde EFS.
- **Sistema de archivos:** organización de archivos y carpetas que utilizan los programas.
  - **Ejemplo:** `/imagenes/logo.png` representa un archivo dentro de una estructura de carpetas.
- **NFS — Network File System:** protocolo que permite acceder por red a un sistema de archivos remoto.
  - **Ejemplo:** Linux puede montar EFS en `/mnt/compartido` mediante NFS.
- **EC2 — Amazon Elastic Compute Cloud:** servicio para ejecutar computadoras virtuales.
  - **Ejemplo:** dos instancias EC2 en AZ diferentes pueden montar el mismo EFS regional.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región.
  - **Ejemplo:** EFS Standard almacena datos de forma regional para acceso desde múltiples AZ.
- **POSIX — Portable Operating System Interface:** conjunto de convenciones de sistemas tipo Unix, incluidos permisos y operaciones de archivos.
  - **Ejemplo:** Linux puede aplicar propietario y permisos a un archivo guardado en EFS.
- **KMS — AWS Key Management Service:** servicio para administrar claves criptográficas.
  - **Ejemplo:** una clave KMS puede proteger datos de EFS cifrados en reposo.
- **Throughput:** cantidad de datos transferidos por segundo.
  - **Ejemplo:** procesar muchos vídeos grandes requiere más throughput que abrir unos pocos documentos.
- **IA — Infrequent Access (acceso poco frecuente):** clase para archivos consultados con menor frecuencia y con coste de acceso.
  - **Ejemplo:** informes antiguos pueden moverse automáticamente a EFS IA mediante una política de ciclo de vida.
- **CMS — Content Management System (sistema de gestión de contenidos):** aplicación para administrar contenido de sitios web.
  - **Ejemplo:** WordPress es un CMS que puede compartir archivos mediante EFS.

- **AMI — Amazon Machine Image:** plantilla utilizada para lanzar una instancia EC2.
  - **Ejemplo:** una AMI basada en Linux puede incluir las herramientas necesarias para montar EFS.
- **API — Application Programming Interface:** interfaz definida para que un programa use operaciones ofrecidas por otro componente.
  - **Ejemplo:** una aplicación usa operaciones estándar de archivos para abrir y guardar contenido en EFS.

## Idea central

EFS proporciona archivos compartidos por red; no se adjunta como un único disco exclusivo para una sola instancia.

**Ejemplo integrador:** un balanceador distribuye usuarios entre tres servidores web Linux. Los tres montan el mismo EFS, por lo que una imagen subida desde un servidor queda disponible para los demás.

> **Complemento oficial de AWS:** EFS ha incorporado modos y clases nuevas, incluido throughput elástico y EFS Archive. Las cifras y recomendaciones de rendimiento del documento fuente deben contrastarse con la documentación actual.

## Amazon EFS

- `Elastic File System` es NFS gestionado que puede montarse en muchas EC2.
- Funciona con instancias EC2 en multi-AZ.
- Fuente lo describe como alta disponibilidad, escalable, caro —3x `gp2`— y pago por uso.
- Casos de uso: gestión de contenidos, servicio web, intercambio de datos, WordPress.
- Usa protocolo NFSv4.1.
- Usa grupo de seguridad para controlar acceso.
- Compatible con AMI basadas en Linux, no Windows.
- Cifrado en reposo mediante KMS.
- Sistema de archivos POSIX similar a Linux con API estándar de archivos.
- Escala automáticamente y no requiere planificar capacidad.

### Rendimiento y almacenamiento EFS

- Escala a miles de clientes NFS concurrentes y 10 GB+/s de rendimiento.
- Crece automáticamente hasta escala de petabytes.
- Modos de rendimiento definidos al crear EFS:
  - Propósito general: predeterminado, sensible a latencia, por ejemplo servidor web o CMS.
  - E/S máxima: mayor latencia, más rendimiento, altamente paralelo, por ejemplo Big Data o procesamiento de medios.
- Modos de throughput:
  - Ráfaga: `1 TB = 50 MiB/s + ráfaga hasta 100 MiB/s`.
  - Aprovisionado: fija rendimiento independientemente del tamaño, por ejemplo `1 GiB/s` para `1 TB`.
- Clases de almacenamiento:
  - Estándar: archivos de acceso frecuente.
  - EFS-IA: coste de recuperación, menor precio de almacenamiento, habilitable con política de ciclo de vida.
- Disponibilidad y durabilidad:
  - Estándar: Multi-AZ, ideal para producción.
  - One Zone: una AZ, útil para desarrollo, backup activado por defecto, compatible con EFS One Zone-IA.
- La fuente menciona más de 90% de ahorro de costes.
