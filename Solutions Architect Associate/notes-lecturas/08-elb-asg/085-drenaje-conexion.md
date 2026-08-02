# Drenaje de la conexión

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 150.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 14: Drenaje de la conexión.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Deregistration delay for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-target-group-health-settings).
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
- **Connection Draining (drenaje de conexiones):** nombre utilizado por CLB para dejar terminar solicitudes existentes mientras se retira un destino.
  - **Ejemplo:** un servidor que se está apagando termina una descarga ya iniciada, pero no recibe otra nueva.
- **Deregistration Delay (retraso de desregistro):** nombre usado por ALB y NLB para el periodo de drenaje de un destino retirado.
  - **Ejemplo:** el target permanece en estado de drenaje durante el tiempo configurado.
- **Solicitud en vuelo:** solicitud que ya fue enviada y todavía no terminó.
  - **Ejemplo:** un informe que tarda veinte segundos en generarse está en vuelo durante ese tiempo.
- **Desregistrar:** quitar un destino del grupo que puede recibir tráfico nuevo.
  - **Ejemplo:** antes de desplegar una versión nueva, se desregistra la instancia anterior.
- **CLB — Classic Load Balancer:** generación anterior del balanceador de AWS.
  - **Ejemplo:** su documentación utiliza el término Connection Draining.
- **ALB — Application Load Balancer:** balanceador de solicitudes de aplicaciones web.
  - **Ejemplo:** un ALB deja de enviar solicitudes nuevas a un target en drenaje.
- **NLB — Network Load Balancer:** balanceador de conexiones de red.
  - **Ejemplo:** un NLB aplica el retraso de desregistro a sus destinos.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden actuar como destinos.
  - **Ejemplo:** una instancia EC2 se retira durante un despliegue.
- **ASG — Auto Scaling Group:** grupo que crea y termina instancias EC2 según capacidad y salud.
  - **Ejemplo:** al reducir capacidad, el ASG coordina la retirada de una instancia registrada.

## Idea central

El drenaje evita cortar inmediatamente el trabajo ya comenzado cuando una instancia se retira por mantenimiento, despliegue o escalado.

**Ejemplo integrador:** un ASG decide terminar una instancia. El balanceador deja de asignarle solicitudes nuevas, espera que finalicen las existentes y luego completa el desregistro.

## Connection Draining

- Nombre de característica:
  - `Connection Draining` para CLB.
  - `Deregistration Delay` para ALB y NLB.
- Da tiempo para completar peticiones “en vuelo” mientras la instancia se desregistra o no está sana.
- Deja de enviar nuevas peticiones a la instancia EC2 que se está desregistrando.
- Rango: 1 a 3600 segundos.
- Por defecto: 300 segundos.
- Se puede desactivar fijando valor en 0.
- La fuente recomienda valor bajo si las peticiones son cortas.
