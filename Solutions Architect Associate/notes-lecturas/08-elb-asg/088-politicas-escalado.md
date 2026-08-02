# Políticas de escalado de Auto Scaling Groups

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 156–159.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 17: Políticas de escalado.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Dynamic scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) y [How predictive scaling works](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-policy-overview.html).
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
- **ASG — Auto Scaling Group:** grupo que mantiene y ajusta instancias EC2.
  - **Ejemplo:** un ASG añade dos servidores cuando aumenta la demanda.
- **Métrica:** valor numérico observado a lo largo del tiempo.
  - **Ejemplo:** el porcentaje medio de CPU utilizado cada minuto es una métrica.
- **CloudWatch:** servicio de AWS que recopila métricas, logs y alarmas.
  - **Ejemplo:** CloudWatch observa la utilización media del ASG.
- **Alarma:** regla que cambia de estado cuando una métrica cruza una condición.
  - **Ejemplo:** una alarma entra en estado `ALARM` si la CPU supera `70 %` durante el periodo configurado.
- **CPU — Central Processing Unit:** capacidad de procesamiento utilizada por las instancias.
  - **Ejemplo:** una CPU media alta puede indicar que faltan servidores.
- **Target tracking (seguimiento de objetivo):** política que ajusta capacidad para mantener una métrica cerca de un valor deseado.
  - **Ejemplo:** intenta mantener la CPU media alrededor del `40 %`.
- **Step scaling (escalado por pasos):** política que aplica cambios distintos según la magnitud de la alarma.
  - **Ejemplo:** añade una instancia con carga moderada y tres con carga muy alta.
- **Predictive scaling (escalado predictivo):** analiza datos históricos para pronosticar capacidad futura.
  - **Ejemplo:** prepara servidores antes del aumento que ocurre cada mañana.
- **Cooldown (periodo de enfriamiento):** intervalo que evita reaccionar repetidamente antes de que se observe el efecto de un cambio.
  - **Ejemplo:** después de añadir una instancia, espera a que arranque y contribuya antes de tomar otra decisión equivalente.
- **AMI — Amazon Machine Image:** plantilla usada para lanzar instancias.
  - **Ejemplo:** una AMI con la aplicación preparada reduce el tiempo hasta que el nuevo servidor atiende tráfico.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales cuya cantidad administra el ASG.
  - **Ejemplo:** una política aumenta de tres a cinco instancias EC2.

## Idea central

Una política de escalado convierte observaciones o previsiones de carga en cambios de capacidad del ASG.

**Ejemplo integrador:** CloudWatch detecta más solicitudes por destino; una política aumenta la capacidad deseada, el ASG lanza instancias y el Load Balancer reparte la carga entre ellas.

## Políticas y métricas de escalado

### CloudWatch

- ASG puede escalarse mediante alarmas de CloudWatch.
- Una alarma monitoriza una métrica, como CPU media o métrica personalizada.
- Métricas como CPU media se calculan para todas las instancias del ASG.
- En base a la alarma se pueden crear políticas para aumentar o reducir número de instancias.

### Políticas dinámicas

- Seguimiento de objetivos:
  - lo más sencillo y fácil de configurar;
  - ejemplo fuente: mantener media CPU del ASG alrededor de 40%.
- Escalado simple / escalonado:
  - si alarma CPU > 70%, añadir 2 unidades;
  - si alarma CPU < 30%, eliminar 1 unidad.
- Acciones programadas:
  - anticipan escalado por patrones conocidos;
  - ejemplo: aumentar capacidad mínima a 10 a las 17 h de los viernes.
- Escalado predictivo:
  - previsión continua de carga y programación del escalado por adelantado.

### Buenas métricas para escalar

- `CPUUtilization`: utilización media CPU en instancias.
- `RequestCountPerTarget`: mantener estable número de peticiones por instancia EC2.
- Promedio de entrada/salida de red si la aplicación está vinculada a la red.
- Métricas personalizadas enviadas con CloudWatch.

### Cooldown

- Tras una actividad de escalado, ASG entra en periodo de enfriamiento.
- Por defecto: 300 segundos.
- Durante cooldown, ASG no lanza ni termina instancias adicionales para permitir estabilización de métricas.
- Consejo de fuente: usar AMI lista para usar para reducir tiempo de configuración, servir peticiones más rápido y reducir periodo de enfriamiento.
