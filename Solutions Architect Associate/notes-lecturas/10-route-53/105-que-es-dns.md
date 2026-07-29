# ¿Qué es DNS?

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 194–196.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 10, lectura 1: ¿Qué es un DNS?.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Qué es DNS

- `Domain Name System` traduce nombres de host legibles por humanos a direcciones IP.
- Es la “guía telefónica” de Internet.
- Usa una jerarquía de nombres: raíz, TLD, dominio y subdominios.

## Terminología

- **Registrador de dominios:** vende o registra el dominio; ejemplos de la fuente: Route 53 y GoDaddy.
- **Registro DNS:** asociación como A, AAAA, CNAME o NS.
- **Zona:** contiene registros.
- **Servidor de nombres:** responde consultas DNS, de forma autoritativa o no autoritativa.
- **TLD:** dominio de primer nivel, como `.com`, `.us`, `.in`, `.gov` u `.org`.
- **SLD:** dominio de segundo nivel, como `amazon.com`.
- **FQDN:** nombre completo de un host dentro de la jerarquía.

## Cómo se resuelve un nombre

1. El navegador consulta al servidor DNS local.
2. Si no tiene la respuesta, este consulta la jerarquía: raíz, TLD y servidor autoritativo del dominio.
3. El servidor autoritativo devuelve la IP.
4. El cliente usa esa IP para conectarse al servidor web.

## Punto de confusión

- DNS no transporta la página web: únicamente ayuda a localizar el endpoint.
- Registrar un dominio y alojar su DNS son responsabilidades distintas, aunque Route 53 puede realizar ambas.
