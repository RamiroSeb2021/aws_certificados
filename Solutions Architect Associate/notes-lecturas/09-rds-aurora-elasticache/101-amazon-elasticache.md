# Visión general de Amazon ElastiCache

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 186–188.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 11: Visión general de ElastiCache.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Qué es Amazon ElastiCache

- Servicio administrado para Redis o Memcached.
- Proporciona bases en memoria de alto rendimiento y baja latencia.
- Reduce carga de lectura sobre bases de datos.
- Puede ayudar a que la aplicación no mantenga estado local.
- AWS administra instalación, configuración, mantenimiento, parches, monitorización, recuperación y backups.
- Adoptarlo suele exigir cambios importantes en el código de la aplicación.

## Patrón de caché de base de datos

1. La aplicación consulta ElastiCache.
2. Si encuentra el dato, ocurre un `cache hit`.
3. Si no lo encuentra, ocurre un `cache miss`: lee RDS y guarda el dato en caché.
4. Debe existir estrategia de invalidación para evitar datos obsoletos.

## Almacén de sesiones

- La aplicación escribe la sesión del usuario en ElastiCache.
- Otra instancia de la aplicación puede recuperar esa sesión.
- Esto evita depender de la memoria local de una sola instancia.
