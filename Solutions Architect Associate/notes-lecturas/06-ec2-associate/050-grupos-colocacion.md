# Grupos de ubicación o colocación de EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 85–88.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 3: Grupos de colocación de EC2.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Placement strategies for your placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html).
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo desde fundamentos.
- Cada concepto nuevo incluye una explicación sencilla y un ejemplo inmediato.
- Las siglas se desarrollan y explican en su primera aparición conceptual.
- Los límites y cifras del curso se preservan como contenido de la fuente y pueden cambiar; los complementos actuales se identifican por separado.

## Antes de empezar: conceptos y siglas

- **AWS — Amazon Web Services:** proveedor de nube que decide en qué infraestructura física ejecuta cada instancia.
  - **Ejemplo:** AWS puede iniciar dos instancias del cliente en servidores físicos diferentes.
- **EC2 — Amazon Elastic Compute Cloud:** servicio que ofrece computadoras virtuales llamadas instancias.
  - **Ejemplo:** una aplicación distribuida puede ejecutarse en cinco instancias EC2.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación física aislada dentro de una región de AWS, compuesta por uno o más centros de datos.
  - **Ejemplo:** `us-east-1a` y `us-east-1b` son nombres de AZ dentro de una misma región para una cuenta.
- **Grupo de colocación:** regla que orienta cómo AWS ubica físicamente un conjunto de instancias EC2.
  - **Ejemplo:** una estrategia puede mantener instancias cerca para reducir latencia o separarlas para reducir fallos compartidos.
- **Latencia:** tiempo que tarda la información en viajar de una instancia a otra.
  - **Ejemplo:** si una respuesta tarda `2 ms`, su latencia es de dos milisegundos.
- **Gbps — gigabits por segundo:** unidad para medir cuántos datos puede transportar una red por segundo.
  - **Ejemplo:** una conexión de `10 Gbps` puede transportar más datos por segundo que una de `1 Gbps`.
- **CPU — Central Processing Unit (unidad central de procesamiento):** componente físico que ejecuta instrucciones.
  - **Ejemplo:** una instancia virtual utiliza capacidad de CPU proporcionada por el servidor físico subyacente.
- **HDFS — Hadoop Distributed File System:** sistema de archivos que reparte datos entre varias máquinas.
  - **Ejemplo:** HDFS puede guardar copias de bloques en particiones diferentes para evitar un único punto de fallo.

## Idea central

Los grupos de colocación controlan una decisión física invisible para la instancia: qué tan juntas o separadas deben quedar varias EC2.

**Ejemplo integrador:** un trabajo que necesita comunicación muy rápida puede usar `cluster`; una aplicación crítica con pocas instancias puede usar `spread`; un sistema distribuido grande puede usar `partition`.

> **Complemento oficial de AWS:** la documentación actual describe `cluster` como una agrupación lógica dentro de una sola AZ y un segmento de red de alto ancho de banda; no garantiza que todas las instancias estén en un único rack. El diagrama del curso debe entenderse como un modelo simplificado.

## Grupos de ubicación o colocación

- Permiten controlar estrategia de colocación de instancias EC2.
- Al crear un placement group se especifica una estrategia.

### Qué son

Un grupo de colocación es una configuración que indica a AWS **cómo debe ubicar varias instancias EC2 entre Zonas de Disponibilidad, racks y hardware físico**. No crea las instancias ni distribuye tráfico: controla la relación física entre ellas para priorizar baja latencia, aislamiento de fallos o separación por particiones.

### Qué son un rack y el hardware físico

> Aclaración conceptual: estas definiciones ayudan a interpretar los diagramas del documento fuente, que no desarrolla ambos términos por separado.

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
2. El modelo simplificado del documento fuente representa las instancias juntas, en un mismo rack y dentro de una única AZ; la documentación actual garantiza la agrupación lógica en una AZ, no un rack concreto.
3. Esto proporciona baja latencia y alto rendimiento de red entre las instancias.
4. Como contrapartida, concentrarlas aumenta el riesgo de que un fallo de infraestructura correlacionado afecte a varias a la vez.

| Estrategia | Descripción | Ventajas / uso | Contras / límites |
| --- | --- | --- | --- |
| Cluster | Agrupa instancias en baja latencia dentro de una única AZ. | Red de 10 Gbps entre instancias con red mejorada activada; Big Data que necesita completarse rápido; aplicaciones de latencia extremadamente baja y alto rendimiento de red. | Si falla el rack, todas las instancias fallan al mismo tiempo. |
| Distribuida | Coloca un pequeño grupo de instancias en hardware físico diferente para reducir fallos correlacionados. | Puede abarcar varias AZ; reduce riesgo de fallos simultáneos; útil para máxima alta disponibilidad y aplicaciones críticas donde cada instancia debe aislarse de fallos de otras. | Máximo 7 instancias por AZ por grupo. |
| Partición | Reparte instancias en particiones que dependen de conjuntos diferentes de racks dentro de una AZ. | Puede abarcar varias AZ en la misma región; hasta 7 particiones por AZ; hasta 100 instancias EC2; instancias acceden a información de partición como metadatos; casos: HDFS, HBase, Cassandra, Kafka. | Un fallo de partición puede afectar muchas EC2, pero no otras particiones. |
