# Hibernación de Amazon EC2

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 90–92.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lectura 8: Hibernación de EC2.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [How Amazon EC2 instance hibernation works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html).
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
- **EC2 — Amazon Elastic Compute Cloud:** servicio de AWS para ejecutar computadoras virtuales llamadas instancias.
  - **Ejemplo:** una instancia EC2 puede ejecutar Linux y una aplicación de análisis.
- **RAM — Random Access Memory (memoria de acceso aleatorio):** memoria rápida donde viven temporalmente los programas y datos que la computadora está usando.
  - **Ejemplo:** si un programa tiene un cálculo abierto, parte de su estado se encuentra en RAM.
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques que puede conectarse a una instancia EC2.
  - **Ejemplo:** el volumen EBS raíz contiene el sistema operativo de la instancia.
- **Volumen raíz:** disco desde el que arranca el sistema operativo.
  - **Ejemplo:** al iniciar Linux, la instancia lee sus archivos desde el volumen raíz.
- **AMI — Amazon Machine Image:** plantilla con la información necesaria para lanzar una instancia EC2.
  - **Ejemplo:** una AMI puede incluir Linux y una aplicación ya instalada.
- **Hibernar:** guardar el contenido de la RAM en el disco antes de apagar, para recuperarlo al volver a iniciar.
  - **Ejemplo:** un cálculo abierto puede continuar desde el estado guardado en vez de empezar desde cero.
- **Bare metal (servidor físico dedicado):** instancia que da acceso directo al servidor físico, sin la virtualización habitual entre el cliente y el hardware.
  - **Ejemplo:** ciertas cargas que requieren acceso directo al hardware utilizan tipos bare metal.

- **RHEL — Red Hat Enterprise Linux:** distribución comercial del sistema operativo Linux.
  - **Ejemplo:** una AMI compatible puede usar RHEL como sistema operativo.
- **C3, C4, C5, I3, M3, M4, R3, R4, T2 y T3:** códigos de familias y generaciones de instancias EC2; no son siglas que describan por sí solas toda la capacidad.
  - **Ejemplo:** `T3` identifica una familia de rendimiento ampliable, pero el tamaño completo también incluye valores como `t3.micro`.

## Idea central

Detener una instancia conserva sus discos EBS, pero hibernarla también guarda en el volumen raíz cifrado el estado que estaba en RAM.

**Ejemplo integrador:** una aplicación tarda veinte minutos en cargar información en memoria. Al hibernar la instancia, EC2 guarda esa RAM en EBS; al reanudarla, recupera el estado y evita repetir toda la preparación.

> **Complemento oficial de AWS:** los tipos de instancia, sistemas operativos y demás límites compatibles cambian. Verifique la página oficial de requisitos antes de diseñar una solución; la lista del documento fuente representa el momento en que se creó el curso.

## Hibernación de EC2

### Parar, terminar e iniciar

- Al parar una instancia, los datos del disco EBS se mantienen intactos en el siguiente arranque.
- Al terminar una instancia, se pierden los volúmenes EBS root que estén preparados para destruirse.
- En el primer arranque, el sistema operativo inicia y se ejecuta EC2 User Data.
- En arranques siguientes, inicia el sistema operativo.
- Luego inicia la aplicación y se calientan cachés; eso puede tardar.

### Qué hace EC2 Hibernate

- Conserva estado en memoria RAM.
- Hace que el arranque sea mucho más rápido porque el sistema operativo no se detiene/reinicia.
- Bajo el capó, el estado de RAM se escribe en un archivo en el volumen EBS root.
- El volumen EBS root debe estar encriptado.
- Casos de uso:
  - procesamiento de larga duración;
  - guardar estado de RAM;
  - servicios que tardan en inicializarse.

### Condiciones y límites indicados

- Familias soportadas: C3, C4, C5, I3, M3, M4, R3, R4, T2, T3, entre otras indicadas con puntos suspensivos en fuente.
- RAM debe ser inferior a 150 GB.
- No se soporta para instancias bare metal.
- AMI mencionadas: Amazon Linux 2, Linux AMI, Ubuntu, RHEL, CentOS y Windows, con puntos suspensivos en fuente.
- Volumen root debe ser EBS y estar encriptado.
- Disponible para instancias bajo demanda, reservadas y Spot.
- Una instancia no puede estar hibernada más de 60 días.
