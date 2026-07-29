# Políticas de escalado de Auto Scaling Groups

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 156–159.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 17: Políticas de escalado.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
