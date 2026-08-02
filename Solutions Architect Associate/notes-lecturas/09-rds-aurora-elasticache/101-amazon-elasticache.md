# Visión general de Amazon ElastiCache

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 186–188.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 11: Visión general de ElastiCache.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [What is Amazon ElastiCache?](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html).
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
- **Caché:** almacenamiento temporal de datos usados con frecuencia para responder más rápido.
  - **Ejemplo:** guardar temporalmente la ficha de un producto evita consultarla repetidamente en la base principal.
- **En memoria:** datos guardados principalmente en RAM, que ofrece acceso muy rápido.
  - **Ejemplo:** recuperar una sesión desde memoria suele ser más rápido que leerla de almacenamiento persistente.
- **RAM — Random Access Memory:** memoria rápida utilizada por procesos activos.
  - **Ejemplo:** ElastiCache mantiene datos disponibles en memoria para baja latencia.
- **Latencia:** tiempo que tarda una operación en responder.
  - **Ejemplo:** una caché busca reducir el tiempo entre pedir un dato y recibirlo.
- **ElastiCache:** servicio administrado de almacenes de datos y cachés distribuidas en memoria.
  - **Ejemplo:** AWS administra nodos o una caché serverless compatible.
- **Valkey, Redis OSS y Memcached:** motores compatibles con ElastiCache que ofrecen modelos y capacidades diferentes.
  - **Ejemplo:** una aplicación puede elegir Memcached para una caché simple distribuida o Valkey/Redis OSS para estructuras más ricas.
- **Cache hit (acierto):** el dato solicitado ya existe en la caché.
  - **Ejemplo:** la aplicación devuelve el producto directamente desde ElastiCache.
- **Cache miss (fallo):** el dato no está en caché y debe buscarse en la fuente original.
  - **Ejemplo:** la aplicación consulta RDS y luego guarda el resultado en la caché.
- **Invalidación:** eliminación o actualización de datos en caché cuando dejan de ser válidos.
  - **Ejemplo:** al cambiar el precio, se elimina la copia antigua para no mostrar información obsoleta.
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** ElastiCache puede reducir consultas repetidas contra RDS.

- **OSS — Open Source Software (software de código abierto):** software cuyo código fuente se publica bajo una licencia abierta.
  - **Ejemplo:** Redis OSS distingue la oferta basada en el proyecto de código abierto.

## Idea central

La caché acelera el acceso y descarga la fuente, pero introduce el problema de mantener datos temporales suficientemente actualizados.

**Ejemplo integrador:** la primera solicitud de un producto falla en caché, lee RDS y guarda el resultado. Las siguientes solicitudes lo encuentran en ElastiCache hasta que se invalida.

> **Complemento oficial de AWS:** la documentación actual presenta Valkey, Memcached y Redis OSS. La lista del documento fuente que menciona solo Redis y Memcached refleja una versión anterior del servicio.

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
