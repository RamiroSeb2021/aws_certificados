# Sticky Sessions — sesiones persistentes

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 142–143.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 10: Sticky Sessions.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Sticky Sessions

- Permiten persistencia para que el mismo cliente sea redirigido a la misma instancia detrás de un Load Balancer.
- Funciona para Classic Load Balancer, Application Load Balancer y Network Load Balancer.
- Para CLB y ALB, la cookie de persistencia tiene fecha de expiración controlada por el usuario.
- Caso de uso: que el usuario no pierda datos de sesión.
- Puede provocar desbalanceo de carga entre instancias EC2 backend.

### Nombres de cookies

- Cookies basadas en la aplicación:
  - Cookie personalizada:
    - generada por el objetivo;
    - puede incluir atributos requeridos por la aplicación;
    - nombre especificado por target group;
    - no usar `AWSALB`, `AWSALBAPP` o `AWSALBTG`, reservadas para ELB.
  - Cookie de la aplicación:
    - generada por Load Balancer;
    - nombre `AWSALBAPP`.
- Cookies basadas en duración:
  - generadas por Load Balancer;
  - nombre `AWSALB` para ALB y `AWSELB` para CLB.
