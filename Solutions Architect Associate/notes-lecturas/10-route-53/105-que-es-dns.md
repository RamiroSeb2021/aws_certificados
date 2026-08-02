# ¿Qué es DNS?

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 194–196.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 10, lectura 1: ¿Qué es un DNS?.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon Route 53 concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html).
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
- **DNS — Domain Name System (sistema de nombres de dominio):** red jerárquica que traduce nombres legibles a información como direcciones IP.
  - **Ejemplo:** convierte `www.example.com` en la dirección IP de un servidor.
- **IP — Internet Protocol:** sistema de direccionamiento que permite localizar interfaces en una red.
  - **Ejemplo:** el navegador utiliza la IP devuelta por DNS para intentar conectarse al servidor.
- **Dominio:** nombre registrado dentro de la jerarquía DNS.
  - **Ejemplo:** `example.com` es un dominio.
- **Subdominio:** nombre añadido delante de un dominio.
  - **Ejemplo:** `shop.example.com` es un subdominio de `example.com`.
- **Hostname (nombre de host):** nombre que identifica un host o servicio dentro de DNS.
  - **Ejemplo:** `www.example.com` puede ser el hostname de un sitio web.
- **TLD — Top-Level Domain (dominio de nivel superior):** parte situada más a la derecha, debajo de la raíz DNS.
  - **Ejemplo:** `.com` es el TLD de `example.com`.
- **SLD — Second-Level Domain (dominio de segundo nivel):** etiqueta registrada directamente bajo el TLD en el ejemplo habitual.
  - **Ejemplo:** `example` es el SLD de `example.com`.
- **FQDN — Fully Qualified Domain Name (nombre de dominio completamente calificado):** nombre completo de un recurso dentro de la jerarquía DNS.
  - **Ejemplo:** `api.dev.example.com` identifica completamente ese nombre dentro del dominio.
- **Resolver DNS:** servidor que busca la respuesta en nombre del cliente y puede guardarla temporalmente.
  - **Ejemplo:** el equipo pregunta a su resolver por `www.example.com`.
- **Servidor autoritativo:** servidor que contiene la respuesta oficial para una zona DNS.
  - **Ejemplo:** devuelve el registro configurado por el propietario de `example.com`.
- **Zona DNS:** contenedor de registros para un dominio y sus subdominios.
  - **Ejemplo:** la zona `example.com` contiene registros para `www` y `api`.

- **A:** tipo de registro que devuelve una dirección IPv4.
  - **Ejemplo:** `www.example.com` puede tener un registro A con `192.0.2.10`.
- **AAAA:** tipo de registro que devuelve una dirección IPv6.
  - **Ejemplo:** `www.example.com` puede tener un registro AAAA con `2001:db8::10`.
- **CNAME — Canonical Name:** alias desde un nombre DNS hacia otro nombre.
  - **Ejemplo:** `shop.example.com` apunta a `stores.example.net`.
- **NS — Name Server:** registro que identifica servidores autoritativos de una zona.
  - **Ejemplo:** el registrador delega `example.com` a los NS de Route 53.

## Idea central

DNS ayuda a localizar servicios mediante nombres; no transporta la página, el correo ni los datos de la aplicación.

**Ejemplo integrador:** el navegador pregunta por `www.example.com`; el resolver obtiene la IP desde la jerarquía DNS y luego el navegador inicia una conexión separada hacia esa IP.

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
