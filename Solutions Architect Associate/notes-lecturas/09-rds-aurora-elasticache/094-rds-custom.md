# RDS Custom para Oracle y Microsoft SQL Server

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 169.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 4: RDS personalizado.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Qué es RDS Custom

- Base de datos administrada para Oracle y Microsoft SQL Server con personalización del sistema operativo y de la base.
- A diferencia de RDS estándar, permite acceso administrativo a la base y al sistema operativo subyacente.
- Permite configurar ajustes, instalar parches, habilitar funciones nativas y acceder mediante SSH o SSM Session Manager.

## Modo de automatización

- Para personalizar, se desactiva temporalmente el modo de automatización.
- La fuente recomienda tomar un snapshot antes.

## Diferencia clave

- **RDS estándar:** AWS administra la base de datos y el sistema operativo.
- **RDS Custom:** el cliente obtiene acceso administrativo completo para cargas que necesitan personalizaciones incompatibles con el modelo cerrado de RDS.
