# Drenaje de la conexión

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 150.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 14: Drenaje de la conexión.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
