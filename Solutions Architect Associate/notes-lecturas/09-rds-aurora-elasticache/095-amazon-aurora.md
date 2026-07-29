# Amazon Aurora

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 170–174.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 5: Amazon Aurora.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

## Qué es Amazon Aurora

- Tecnología propietaria de AWS compatible con controladores PostgreSQL y MySQL.
- La fuente afirma rendimiento hasta 5 veces el de MySQL en RDS y más de 3 veces el de PostgreSQL en RDS.
- El almacenamiento crece automáticamente en incrementos de 10 GB hasta 256 TB.
- Puede tener hasta 15 réplicas con retraso de replicación indicado como inferior a 10 ms.
- La fuente indica un coste 20 % superior a RDS, compensado por mayor eficiencia.

## Alta disponibilidad

- Mantiene 6 copias de los datos en 3 AZ.
- Necesita 4 de 6 copias para escrituras y 3 de 6 para lecturas.
- Incluye autorreparación mediante replicación entre pares.
- Una instancia writer realiza escrituras; el writer y hasta 15 réplicas realizan lecturas.
- Recuperación automática del writer en menos de 30 segundos, según fuente.

## Endpoints

- **Writer endpoint:** apunta a la instancia principal de escritura.
- **Reader endpoint:** actúa como conexión balanceada hacia las réplicas.
- El escalado automático puede añadir réplicas cuando aumenta la carga de lectura.

## Por qué es importante

- Aurora integra almacenamiento distribuido, alta disponibilidad, failover y escalado de lectura como propiedades del clúster.
- No hay que confundir “compatible con MySQL/PostgreSQL” con que Aurora sea esos motores sin cambios: es una tecnología propia que expone compatibilidad.
