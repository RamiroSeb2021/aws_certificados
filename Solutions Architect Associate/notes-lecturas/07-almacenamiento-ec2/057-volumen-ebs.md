# Volúmenes Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 94–97.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 1: Visión general de EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).
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
- **EBS — Amazon Elastic Block Store:** servicio de almacenamiento persistente por bloques para instancias EC2.
  - **Ejemplo:** un volumen EBS puede guardar el sistema operativo o los datos de una base de datos.
- **EC2 — Amazon Elastic Compute Cloud:** servicio que crea computadoras virtuales llamadas instancias.
  - **Ejemplo:** una instancia EC2 puede tener un volumen raíz y otro volumen EBS para datos.
- **Almacenamiento por bloques:** presenta el espacio como bloques que el sistema operativo puede organizar mediante particiones y sistemas de archivos.
  - **Ejemplo:** Linux puede formatear un volumen EBS y montarlo como `/datos`.
- **Volumen:** unidad lógica de almacenamiento que puede adjuntarse a una instancia.
  - **Ejemplo:** un volumen de `100 GiB` funciona de manera parecida a un disco adicional.
- **Persistencia:** capacidad de conservar datos aunque termine el proceso que los estaba usando.
  - **Ejemplo:** un volumen EBS no eliminado puede conservar archivos después de terminar una instancia.
- **AZ — Availability Zone (Zona de Disponibilidad):** ubicación aislada dentro de una región de AWS.
  - **Ejemplo:** un volumen en `us-east-1a` debe adjuntarse a una instancia de esa misma AZ.
- **IOPS — Input/Output Operations Per Second (operaciones de entrada/salida por segundo):** cantidad de lecturas o escrituras que el almacenamiento puede procesar cada segundo.
  - **Ejemplo:** una base de datos con muchas operaciones pequeñas puede necesitar más IOPS.
- **SSD — Solid-State Drive (unidad de estado sólido):** almacenamiento basado en memoria flash, apropiado para operaciones frecuentes y baja latencia.
  - **Ejemplo:** un volumen `gp3` utiliza tecnología SSD.
- **AWS CLI — AWS Command Line Interface:** herramienta para administrar AWS escribiendo comandos.
  - **Ejemplo:** puede modificarse el atributo `Delete on Termination` mediante AWS CLI.

- **CCP — AWS Certified Cloud Practitioner:** certificación fundamental de AWS a la que se refiere la frase “nivel CCP” del curso.
  - **Ejemplo:** a ese nivel se enseña primero el caso general de un volumen conectado a una instancia.
- **USB — Universal Serial Bus:** estándar físico usado para conectar dispositivos; aquí aparece únicamente dentro de una analogía.
  - **Ejemplo:** un dispositivo USB puede conectarse y desconectarse, como analogía limitada de adjuntar y separar EBS.

## Idea central

EBS separa el almacenamiento de la computadora virtual: la instancia procesa y el volumen conserva bloques de datos.

**Ejemplo integrador:** si una instancia falla, un volumen EBS conservado puede separarse y adjuntarse a otra instancia de la misma AZ para recuperar sus datos.

## Amazon EBS

### Qué es un volumen EBS

- `Elastic Block Store` es una unidad de red que se puede adjuntar a instancias mientras se ejecutan.
- Permite persistir datos incluso después de finalizar instancias.
- A nivel CCP, solo puede montarse en una instancia a la vez.
- Está vinculado a una zona de disponibilidad específica.
- Analogía fuente: “memoria USB de red”.
- Nivel gratuito mencionado: 30 GB mensuales de EBS de tipo Propósito General SSD o Magnético.

### Características del volumen EBS

- No es unidad física; usa red para comunicarse con la instancia y puede tener algo de latencia.
- Se puede separar de una instancia EC2 y conectar a otra rápidamente.
- Está bloqueado en una AZ; un volumen en `us-east-1a` no puede adjuntarse a `us-east-1b`.
- Para trasladar un volumen, primero hay que crear un snapshot.
- Tiene capacidad aprovisionada: tamaño en GB e IOPS.
- Se factura toda capacidad aprovisionada.
- Puede aumentar capacidad con el tiempo.

### Atributo “Borrar al terminar”

- Controla comportamiento de EBS cuando termina una instancia EC2.
- Por defecto, el volumen EBS root se elimina.
- Por defecto, otros volúmenes EBS adjuntos no se eliminan.
- Se puede controlar desde consola AWS o AWS CLI.
- Caso de uso: preservar volumen root cuando termina la instancia.
