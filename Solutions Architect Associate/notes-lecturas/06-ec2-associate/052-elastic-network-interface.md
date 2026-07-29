# Elastic Network Interface (ENI)

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 89.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lecturas 5 y 7: ENI y lectura extra.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Elastic Network Interfaces (ENI)

- ENI es un componente lógico de una VPC que representa una tarjeta de red virtual.
- Atributos mencionados:
  - IPv4 privada primaria;
  - una o más IPv4 secundarias;
  - una Elastic IP IPv4 por IPv4 privada;
  - una IPv4 pública;
  - uno o más grupos de seguridad;
  - una dirección MAC.
- Se pueden crear ENI independientes y adjuntarlas sobre la marcha a instancias EC2.
- La fuente menciona mover ENI entre instancias para conmutación por error.
- Están vinculadas a una AZ específica.
