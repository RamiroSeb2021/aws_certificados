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

### Qué son

Un grupo de colocación es una configuración que indica a AWS **cómo debe ubicar varias instancias EC2 entre Zonas de Disponibilidad, racks y hardware físico**. No crea las instancias ni distribuye tráfico: controla la relación física entre ellas para priorizar baja latencia, aislamiento de fallos o separación por particiones.

### Qué son un rack y el hardware físico

> Aclaración conceptual: estas definiciones ayudan a interpretar los diagramas del PDF, que no desarrolla ambos términos por separado.

- **Rack:** armario físico de un centro de datos que agrupa varios servidores y componentes de red y energía. Si un rack pierde alimentación o conectividad, los servidores alojados en él pueden verse afectados al mismo tiempo.
- **Hardware físico:** servidor real que aporta CPU, memoria, almacenamiento y conectividad. Sobre ese servidor AWS puede ejecutar una o más instancias virtuales EC2.
- **Diferencia:** un rack contiene varios servidores físicos. Por eso, dos instancias pueden estar en servidores diferentes, pero continuar dentro del mismo rack y compartir parte del riesgo físico.

#### Ejemplo

Imaginá un rack con tres servidores físicos:

- La instancia EC2 A se ejecuta en el servidor 1.
- La instancia EC2 B se ejecuta en el servidor 2.
- Ambas usan hardware físico diferente, pero siguen dentro del mismo rack.
- Si falla solamente el servidor 1, A puede caer y B continuar funcionando.
- Si falla el rack completo, ambas instancias pueden verse afectadas.

### Ejemplo sencillo

Una aplicación de Big Data utiliza varias instancias EC2 que necesitan intercambiar información rápidamente:

1. Se crea un grupo de colocación con estrategia **Cluster**.
2. Las instancias se colocan juntas, en el mismo rack y dentro de una única AZ.
3. Esto proporciona baja latencia y alto rendimiento de red entre las instancias.
4. Como contrapartida, si falla el rack, todas las instancias pueden fallar simultáneamente.

| Estrategia | Descripción | Ventajas / uso | Contras / límites |
| --- | --- | --- | --- |
| Cluster | Agrupa instancias en baja latencia dentro de una única AZ. | Red de 10 Gbps entre instancias con red mejorada activada; Big Data que necesita completarse rápido; aplicaciones de latencia extremadamente baja y alto rendimiento de red. | Si falla el rack, todas las instancias fallan al mismo tiempo. |
| Distribuida | Coloca un pequeño grupo de instancias en hardware físico diferente para reducir fallos correlacionados. | Puede abarcar varias AZ; reduce riesgo de fallos simultáneos; útil para máxima alta disponibilidad y aplicaciones críticas donde cada instancia debe aislarse de fallos de otras. | Máximo 7 instancias por AZ por grupo. |
| Partición | Reparte instancias en particiones que dependen de conjuntos diferentes de racks dentro de una AZ. | Puede abarcar varias AZ en la misma región; hasta 7 particiones por AZ; hasta 100 instancias EC2; instancias acceden a información de partición como metadatos; casos: HDFS, HBase, Cassandra, Kafka. | Un fallo de partición puede afectar muchas EC2, pero no otras particiones. |
