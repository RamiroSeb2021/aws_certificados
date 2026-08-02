# EC2 Instance Store

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 102–103.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 7: EC2 Instance Store.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html).
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
- **EC2 — Amazon Elastic Compute Cloud:** servicio para ejecutar computadoras virtuales.
  - **Ejemplo:** una instancia EC2 procesa imágenes y necesita espacio temporal rápido.
- **Instance Store (almacén de instancia):** almacenamiento físico local conectado al servidor que aloja la instancia.
  - **Ejemplo:** una instancia puede guardar archivos temporales en su Instance Store durante un procesamiento.
- **Efímero:** que no está diseñado para conservarse después de ciertos cambios o fallos de la instancia.
  - **Ejemplo:** los datos del Instance Store se pierden al detener o terminar la instancia.
- **EBS — Amazon Elastic Block Store:** almacenamiento en red persistente que tiene un ciclo de vida independiente de la instancia.
  - **Ejemplo:** los datos importantes se guardan en EBS en vez de depender solo del disco local efímero.
- **E/S — entrada/salida, también I/O en inglés:** operaciones mediante las que una aplicación lee o escribe datos.
  - **Ejemplo:** guardar mil archivos genera operaciones de E/S.
- **IOPS — Input/Output Operations Per Second:** cantidad de operaciones de lectura o escritura procesadas por segundo.
  - **Ejemplo:** una caché con muchas lecturas pequeñas puede beneficiarse de IOPS altas.
- **Caché:** copia temporal de datos usada para responder más rápido.
  - **Ejemplo:** si la caché se pierde, la aplicación puede reconstruirla desde la fuente permanente.
- **Buffer:** espacio temporal que absorbe datos mientras esperan ser procesados.
  - **Ejemplo:** un buffer puede guardar fragmentos de vídeo antes de transformarlos.

## Idea central

Instance Store prioriza acceso local rápido, pero sacrifica persistencia. Solo debe contener datos descartables, reproducibles o protegidos en otro lugar.

**Ejemplo integrador:** un procesador de vídeo guarda segmentos temporales en Instance Store y escribe el resultado final en almacenamiento persistente. Si la instancia falla, se repite el trabajo temporal sin perder el resultado guardado.

## EC2 Instance Store

- EBS ofrece unidades de red con rendimiento bueno pero limitado.
- Para disco de hardware de alto rendimiento, la fuente usa EC2 Instance Store.
- Ofrece mejor rendimiento de E/S e IOPS muy altas.
- Pierde almacenamiento si la instancia se detiene; es efímero.
- Bueno para buffer, caché, datos de memoria virtual y contenido temporal.
- Hay riesgo de pérdida de datos si falla el hardware.
- Backups y replicación son responsabilidad del usuario.
