# Amazon EFS — Elastic File System

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 112–115.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 11: Amazon EFS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
