# ElastiCache para Solutions Architect

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 189–192.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 13: ElastiCache para Solutions Architect.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
- Redis AUTH permite contraseña/token y soporta cifrado SSL en tránsito.
- Memcached soporta autenticación SASL, marcada como avanzada en la fuente.
- Los grupos de seguridad controlan conectividad de red.

## Patrones

- **Lazy loading:** carga en caché al leer; puede dejar datos obsoletos.
- **Write-through:** actualiza caché cuando se escribe en la base.
- **Session store:** guarda temporalmente sesiones usando TTL.

## Caso Redis

- Los Sorted Sets mantienen unicidad y orden.
- Caso de la fuente: tabla de clasificación de juegos actualizada en tiempo real.
