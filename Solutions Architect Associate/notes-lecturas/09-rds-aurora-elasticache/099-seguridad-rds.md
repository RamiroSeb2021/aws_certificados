# Seguridad de RDS y Aurora

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 184.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 9: Seguridad RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Security in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html) y [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).
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
- **Cifrado en reposo:** protege datos mientras están almacenados.
  - **Ejemplo:** cifra el almacenamiento, snapshots, backups y logs compatibles de una instancia RDS cifrada.
- **Cifrado en tránsito:** protege datos mientras viajan por la red.
  - **Ejemplo:** una aplicación usa TLS al enviar una contraseña y una consulta a RDS.
- **KMS — AWS Key Management Service:** servicio para crear y controlar claves criptográficas.
  - **Ejemplo:** RDS usa una clave KMS para proteger recursos cifrados en reposo.
- **AES-256 — Advanced Encryption Standard con clave de 256 bits:** algoritmo usado por RDS para cifrado en reposo.
  - **Ejemplo:** los datos almacenados se cifran antes de escribirse en el medio subyacente.
- **TLS — Transport Layer Security:** protocolo que cifra y autentica comunicaciones.
  - **Ejemplo:** el cliente valida el certificado de RDS antes de intercambiar datos cifrados.
- **IAM — AWS Identity and Access Management:** servicio de identidades y permisos de AWS.
  - **Ejemplo:** IAM decide quién puede modificar una instancia RDS y, en motores compatibles, puede generar autenticación temporal para la base.
- **Grupo de seguridad:** firewall virtual con estado que controla qué conexiones de red están permitidas.
  - **Ejemplo:** permite el puerto `5432` únicamente desde el grupo de seguridad de la aplicación.
- **SSH — Secure Shell:** protocolo de administración remota cifrada.
  - **Ejemplo:** RDS estándar no ofrece acceso SSH al servidor subyacente.
- **Autenticación:** proceso de comprobar quién intenta acceder.
  - **Ejemplo:** una base puede validar usuario y contraseña o un token IAM compatible.
- **Autorización:** decisión sobre lo que una identidad autenticada puede hacer.
  - **Ejemplo:** un usuario puede consultar una tabla pero no eliminarla.

- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** una instancia RDS combina grupos de seguridad, autenticación y cifrado.

## Idea central

La seguridad de RDS usa capas: red, autenticación, autorización y cifrado protegen problemas diferentes y deben combinarse.

**Ejemplo integrador:** solo las instancias de la aplicación pueden llegar al puerto de PostgreSQL; la aplicación usa TLS, se autentica y recibe únicamente permisos de lectura sobre ciertas tablas.

## Capas de seguridad

- **Cifrado en reposo:** base principal y réplicas mediante AWS KMS; se define al crearla.
- Si la base principal no está cifrada, sus réplicas de lectura no pueden cifrarse.
- Para cifrar una base existente no cifrada: crear snapshot y restaurarlo como base cifrada.
- **Cifrado en tránsito:** TLS con certificados raíz de AWS en el cliente.
- **Autenticación IAM:** permite usar roles IAM en lugar de usuario/contraseña en los casos compatibles.
- **Grupos de seguridad:** controlan acceso de red a RDS y Aurora.
- No hay SSH, excepto en RDS Custom.
- Los logs de auditoría pueden enviarse a CloudWatch Logs.

## Modelo mental

- KMS protege datos almacenados.
- TLS protege la comunicación cliente-base.
- IAM o credenciales determinan quién se autentica.
- Los grupos de seguridad determinan desde qué red se permite llegar.
