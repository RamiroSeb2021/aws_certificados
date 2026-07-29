# Gateway Load Balancer (GWLB)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 140–141.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 8, lectura 9: Gateway Load Balancer.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Gateway Load Balancer

- Implementa, escala y administra flota de dispositivos virtuales de red de terceros en AWS.
- Ejemplos fuente:
  - firewalls;
  - sistemas de detección y prevención de intrusiones;
  - inspección profunda de paquetes;
  - manipulación de cargas útiles.
- Opera en capa 3, paquetes IP.
- Combina:
  - gateway de red transparente como entrada/salida única para todo el tráfico;
  - load balancer para distribuir tráfico a dispositivos virtuales.
- Usa protocolo GENEVE en puerto `6081`.
- Target groups:
  - instancias EC2;
  - direcciones IP privadas.
