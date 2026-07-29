# Grupos de ubicación o colocación de EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 85–88.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 3: Grupos de colocación de EC2.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Grupos de ubicación o colocación

- Permiten controlar estrategia de colocación de instancias EC2.
- Al crear un placement group se especifica una estrategia.

| Estrategia | Descripción | Ventajas / uso | Contras / límites |
| --- | --- | --- | --- |
| Cluster | Agrupa instancias en baja latencia dentro de una única AZ. | Red de 10 Gbps entre instancias con red mejorada activada; Big Data que necesita completarse rápido; aplicaciones de latencia extremadamente baja y alto rendimiento de red. | Si falla el rack, todas las instancias fallan al mismo tiempo. |
| Distribuida | Coloca un pequeño grupo de instancias en hardware físico diferente para reducir fallos correlacionados. | Puede abarcar varias AZ; reduce riesgo de fallos simultáneos; útil para máxima alta disponibilidad y aplicaciones críticas donde cada instancia debe aislarse de fallos de otras. | Máximo 7 instancias por AZ por grupo. |
| Partición | Reparte instancias en particiones que dependen de conjuntos diferentes de racks dentro de una AZ. | Puede abarcar varias AZ en la misma región; hasta 7 particiones por AZ; hasta 100 instancias EC2; instancias acceden a información de partición como metadatos; casos: HDFS, HBase, Cassandra, Kafka. | Un fallo de partición puede afectar muchas EC2, pero no otras particiones. |
