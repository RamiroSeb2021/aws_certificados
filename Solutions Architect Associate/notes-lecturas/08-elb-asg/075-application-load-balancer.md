# Application Load Balancer (ALB v2)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 131–136.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 4: Application Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Application Load Balancer

- ALB es capa 7 HTTP.
- Balancea múltiples aplicaciones HTTP en distintas máquinas mediante target groups.
- Balancea múltiples aplicaciones en una misma máquina, por ejemplo contenedores.
- Soporta HTTP/2 y WebSocket.
- Soporta redireccionamientos, por ejemplo HTTP a HTTPS.

### Enrutamiento

- Puede enrutar a distintos target groups por:
  - ruta de URL, por ejemplo `example.com/users` y `example.com/posts`;
  - nombre de host, por ejemplo `one.example.com` y `other.example.com`;
  - query string y cabeceras, por ejemplo `example.com/users?id=123&order=false`.
- Adecuado para microservicios y aplicaciones basadas en contenedores, como Docker y Amazon ECS.
- Tiene mapeo de puertos para redirigir a puerto dinámico en ECS.
- La fuente contrasta que con Classic Load Balancer harían falta varios CLB por aplicación.

### Target groups ALB

- Instancias EC2, posiblemente gestionadas por Auto Scaling Groups, usando HTTP.
- Tareas ECS, gestionadas por ECS, usando HTTP.
- Funciones Lambda: la petición HTTP se traduce a evento JSON.
- Direcciones IP privadas.
- ALB puede enrutar a múltiples target groups.
- Health checks son a nivel target group.

### Datos de cliente

- ALB tiene nombre de host fijo `XXX.region.elb.amazonaws.com`.
- Los servidores de aplicación no ven directamente IP del cliente.
- IP real del cliente se inserta en `X-Forwarded-For`.
- También se puede obtener puerto con `X-Forwarded-Port` y protocolo con `X-Forwarded-Proto`.
