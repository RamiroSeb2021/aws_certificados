# Volúmenes Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 94–97.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 1: Visión general de EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
