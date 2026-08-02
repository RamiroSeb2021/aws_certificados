# RDS Custom para Oracle y Microsoft SQL Server

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 169.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 4: RDS personalizado.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html).
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
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** RDS estándar restringe el acceso al servidor subyacente para que AWS pueda administrarlo.
- **RDS Custom:** modalidad administrada que permite personalizar el sistema operativo y la base para cargas compatibles.
  - **Ejemplo:** una aplicación heredada puede necesitar instalar un parche específico del sistema.
- **Sistema operativo:** software base que administra el servidor y ejecuta el motor de base de datos.
  - **Ejemplo:** Windows Server puede ser el sistema operativo de una carga de SQL Server.
- **Acceso administrativo:** permisos elevados para modificar configuraciones sensibles.
  - **Ejemplo:** un administrador instala un componente requerido por una aplicación comercial.
- **SSH — Secure Shell:** protocolo de acceso remoto cifrado, habitual en sistemas tipo Linux.
  - **Ejemplo:** un administrador autorizado puede acceder al entorno compatible cuando RDS Custom lo permite.
- **SSM — AWS Systems Manager:** familia de capacidades para administrar recursos; Session Manager permite sesiones controladas sin exponer un puerto de administración público.
  - **Ejemplo:** un operador abre una sesión mediante Systems Manager Session Manager.
- **Snapshot:** copia de la base o su almacenamiento en un momento determinado.
  - **Ejemplo:** antes de una personalización riesgosa se crea un snapshot para recuperación.
- **Automatización de RDS Custom:** procesos con los que AWS monitoriza y administra el entorno dentro de límites compatibles.
  - **Ejemplo:** cambios fuera del perímetro permitido pueden interferir con la automatización.

- **SQL — Structured Query Language:** lenguaje utilizado por bases de datos relacionales y parte del nombre SQL Server.
  - **Ejemplo:** una aplicación envía consultas SQL a Microsoft SQL Server.

## Idea central

RDS Custom intercambia parte de la simplicidad de RDS estándar por mayor control administrativo; ese control también aumenta la responsabilidad del cliente.

**Ejemplo integrador:** una aplicación para Oracle necesita un agente del sistema operativo. El equipo usa RDS Custom, pausa la automatización cuando corresponde, crea un snapshot y realiza la personalización siguiendo la documentación.

## Qué es RDS Custom

- Base de datos administrada para Oracle y Microsoft SQL Server con personalización del sistema operativo y de la base.
- A diferencia de RDS estándar, permite acceso administrativo a la base y al sistema operativo subyacente.
- Permite configurar ajustes, instalar parches, habilitar funciones nativas y acceder mediante SSH o SSM Session Manager.

## Modo de automatización

- Para personalizar, se desactiva temporalmente el modo de automatización.
- La fuente recomienda tomar un snapshot antes.

## Diferencia clave

- **RDS estándar:** AWS administra la base de datos y el sistema operativo.
- **RDS Custom:** el cliente obtiene acceso administrativo completo para cargas que necesitan personalizaciones incompatibles con el modelo cerrado de RDS.
