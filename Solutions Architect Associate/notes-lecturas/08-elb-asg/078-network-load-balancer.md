# Network Load Balancer (NLB)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 137–139.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 7: Network Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Network Load Balancer

- NLB permite reenviar tráfico TCP y UDP a instancias.
- Puede manejar millones de peticiones por segundo.
- Tiene menor latencia.
- Tiene IP estática por AZ y soporta asignación de Elastic IP, útil para permitir una IP específica.
- Se usa para rendimiento extremo y tráfico TCP o UDP.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas;
  - Application Load Balancer.
- Health checks soportan TCP, HTTP y HTTPS.
