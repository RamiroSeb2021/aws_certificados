# ElastiCache para Solutions Architect

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 189–192.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 13: ElastiCache para Solutions Architect.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Choosing between Valkey, Memcached, and Redis OSS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html) y [Caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html).
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
- **Redis OSS:** motor de estructuras de datos en memoria derivado del proyecto Redis de código abierto.
  - **Ejemplo:** un Sorted Set mantiene jugadores ordenados por puntuación.
- **Valkey:** motor de datos en memoria de código abierto compatible con muchos patrones y comandos del ecosistema Redis OSS.
  - **Ejemplo:** una aplicación puede usar Valkey para sesiones y caché administradas en ElastiCache.
- **Memcached:** sistema distribuido de caché en memoria con un modelo simple de clave y valor.
  - **Ejemplo:** guarda temporalmente `producto:42` con la información consultada.
- **Sharding (particionamiento):** reparto de datos entre varios nodos.
  - **Ejemplo:** distintas claves se almacenan en nodos diferentes para aumentar capacidad.
- **AOF — Append Only File:** registro de operaciones que puede usarse para reconstruir datos persistidos por motores compatibles.
  - **Ejemplo:** cada escritura se añade al registro para ayudar a recuperar el estado.
- **IAM — AWS Identity and Access Management:** servicio de identidades y permisos de AWS.
  - **Ejemplo:** una política IAM controla quién puede crear o eliminar recursos de ElastiCache.
- **API — Application Programming Interface:** interfaz mediante la que software solicita operaciones a otro sistema.
  - **Ejemplo:** la API de ElastiCache permite administrar clústeres; no equivale a leer una clave dentro del motor.
- **AUTH:** comando o mecanismo de autenticación usado por motores compatibles para validar credenciales.
  - **Ejemplo:** un cliente presenta un token antes de ejecutar comandos permitidos.
- **TLS — Transport Layer Security:** protocolo de cifrado y autenticación en tránsito.
  - **Ejemplo:** protege la conexión entre la aplicación y la caché compatible.
- **SASL — Simple Authentication and Security Layer:** marco de autenticación compatible con Memcached en configuraciones admitidas.
  - **Ejemplo:** el cliente usa credenciales SASL para autenticarse ante el nodo.
- **TTL — Time To Live (tiempo de vida):** tiempo después del cual una entrada expira.
  - **Ejemplo:** una sesión con TTL de treinta minutos desaparece si no se renueva.

- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región de AWS.
  - **Ejemplo:** un diseño Multi-AZ coloca nodos en zonas distintas para disponibilidad.
- **OSS — Open Source Software:** software distribuido con su código fuente bajo una licencia abierta.
  - **Ejemplo:** Redis OSS es el nombre usado por AWS para versiones compatibles del motor abierto.
- **SSL — Secure Sockets Layer:** antecesor histórico de TLS; la configuración moderna debe describirse como TLS cuando ese sea el protocolo real.
  - **Ejemplo:** “cifrado SSL” en material antiguo suele referirse al cifrado TLS en tránsito.

## Idea central

La elección del motor depende del modelo de datos, la persistencia, el escalado y la disponibilidad que necesita la aplicación.

**Ejemplo integrador:** una tabla de clasificación usa un Sorted Set en Valkey o Redis OSS; una caché simple de objetos desechables puede usar Memcached con sharding.

> **Complemento oficial de AWS:** para diseños actuales incluí Valkey en la comparación. Redis AUTH no debe llamarse “cifrado SSL”: la autenticación y el cifrado TLS son controles diferentes.

## Redis vs Memcached

| Tema | Redis | Memcached |
| --- | --- | --- |
| Alta disponibilidad | Multi-AZ con Auto-Failover. | La fuente lo presenta sin replicación de alta disponibilidad. |
| Escalado | Réplicas de lectura. | Múltiples nodos con particionamiento (`sharding`). |
| Persistencia | AOF; backup y restore. | No persistente; backup/restore aparece para Serverless. |
| Procesamiento | Sets y Sorted Sets. | Arquitectura multihilo. |

## Seguridad

- ElastiCache soporta autenticación IAM para Redis.
- Las políticas IAM también controlan operaciones de la API de AWS.
- Redis AUTH permite contraseña o token; el cifrado en tránsito se configura mediante TLS en las opciones compatibles.
- Memcached soporta autenticación SASL, marcada como avanzada en la fuente.
- Los grupos de seguridad controlan conectividad de red.

## Patrones

- **Lazy loading:** carga en caché al leer; puede dejar datos obsoletos.
- **Write-through:** actualiza caché cuando se escribe en la base.
- **Session store:** guarda temporalmente sesiones usando TTL.

## Caso Redis

- Los Sorted Sets mantienen unicidad y orden.
- Caso de la fuente: tabla de clasificación de juegos actualizada en tiempo real.
