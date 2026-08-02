# RDS y Aurora — copias de seguridad y monitorización

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 180–183.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 8: Copia de seguridad y monitorización.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Introduction to RDS backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html).
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
- **Backup (copia de seguridad):** copia creada para recuperar datos después de una pérdida o error.
  - **Ejemplo:** una copia automática permite restaurar la base al estado de una hora anterior.
- **Snapshot:** copia de la instancia o clúster de base de datos en un punto del tiempo.
  - **Ejemplo:** un snapshot manual se conserva hasta que el usuario decida eliminarlo.
- **PITR — Point-in-Time Recovery (recuperación a un punto en el tiempo):** restauración al estado aproximado de un instante dentro del periodo disponible.
  - **Ejemplo:** recuperar la base al momento anterior a un `DELETE` accidental.
- **Log de transacciones:** registro ordenado de cambios realizados en la base.
  - **Ejemplo:** RDS utiliza registros para avanzar desde una copia hasta el punto solicitado.
- **RDS — Amazon Relational Database Service:** servicio administrado de bases de datos relacionales.
  - **Ejemplo:** RDS crea backups automáticos durante la ventana configurada.
- **Aurora:** motor relacional administrado de AWS con almacenamiento de clúster distribuido.
  - **Ejemplo:** un snapshot de Aurora restaura un clúster nuevo.
- **S3 — Amazon Simple Storage Service:** servicio de almacenamiento de objetos.
  - **Ejemplo:** algunos flujos compatibles permiten restaurar datos de MySQL desde archivos en S3.
- **Copy-on-write (copia al escribir):** técnica que comparte inicialmente bloques y crea copias separadas cuando se modifican.
  - **Ejemplo:** un clon de Aurora se crea rápidamente y empieza a consumir almacenamiento adicional al cambiar datos.
- **Staging:** entorno previo a producción usado para probar cambios.
  - **Ejemplo:** un clon de producción puede servir para verificar una migración sin modificar la base original.

## Idea central

Un backup protege la capacidad de recuperar; restaurar NO modifica normalmente la base original, sino que crea una base o clúster nuevo al que después se redirige la aplicación.

**Ejemplo integrador:** un operador elimina datos a las 10:15. Restaura RDS a las 10:14, valida la nueva instancia y recupera la información necesaria.

## Copias de seguridad de RDS

- Copia completa diaria durante la ventana de mantenimiento.
- Logs de transacciones respaldados cada 5 minutos.
- Permite restaurar a un punto en el tiempo desde la copia más antigua hasta hace 5 minutos.
- Retención automática de 1 a 35 días; `0` desactiva las copias automáticas en RDS, según fuente.
- Los snapshots manuales se conservan durante el tiempo elegido por el usuario.

## Copias de seguridad de Aurora

- Retención automática de 1 a 35 días y no se puede desactivar.
- Recuperación a un punto en el tiempo.
- Snapshots manuales con retención administrada por el usuario.

## Restauración y clonación

- Restaurar backup o snapshot crea una nueva base de datos.
- La fuente describe restauración de RDS MySQL y Aurora MySQL desde Amazon S3.
- La clonación Aurora usa `copy-on-write`: comparte inicialmente el volumen y separa bloques cuando cambian.
- Es útil para crear staging desde producción con rapidez y sin afectar la base original.

## Monitorización

- RDS ofrece dashboards de monitorización.
- Los logs de auditoría pueden enviarse a CloudWatch Logs para aumentar su retención.
