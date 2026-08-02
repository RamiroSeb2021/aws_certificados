# Cifrado de Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 110–111.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 10: Cifrado de EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Verificación oficial: [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) y [How Amazon EBS encryption works](https://docs.aws.amazon.com/ebs/latest/userguide/how-ebs-encryption-works.html).
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
- **Cifrado:** transformación de datos para que no puedan interpretarse sin la clave adecuada.
  - **Ejemplo:** si alguien obtiene bloques cifrados del disco sin autorización, no puede leer su contenido directamente.
- **EBS — Amazon Elastic Block Store:** almacenamiento persistente por bloques utilizado con EC2.
  - **Ejemplo:** un volumen EBS cifrado puede contener archivos de una base de datos.
- **Datos en reposo:** datos mientras permanecen almacenados.
  - **Ejemplo:** los bloques guardados dentro del volumen están en reposo.
- **Datos en tránsito:** datos mientras viajan entre componentes.
  - **Ejemplo:** los bloques que pasan entre una instancia y su volumen EBS están en tránsito.
- **KMS — AWS Key Management Service:** servicio administrado para crear y controlar claves criptográficas.
  - **Ejemplo:** EBS utiliza una clave de KMS para proteger la clave de datos del volumen.
- **AES-256 — Advanced Encryption Standard con claves de 256 bits:** algoritmo de cifrado simétrico utilizado para proteger datos.
  - **Ejemplo:** EBS cifra los datos del volumen usando claves de datos protegidas mediante KMS.
- **Snapshot:** copia de un volumen en un punto del tiempo.
  - **Ejemplo:** un snapshot de un volumen cifrado también permanece cifrado.
- **Transparente:** no exige que la aplicación cambie la forma habitual de leer o escribir.
  - **Ejemplo:** la aplicación abre el mismo archivo mientras EBS cifra y descifra por debajo.

- **EC2 — Amazon Elastic Compute Cloud:** servicio de computadoras virtuales que pueden utilizar volúmenes EBS cifrados.
  - **Ejemplo:** una instancia EC2 lee el volumen normalmente mientras EBS realiza el cifrado de forma transparente.

## Idea central

El cifrado de EBS protege el volumen, sus snapshots y el tráfico entre el volumen y la instancia compatible sin que la aplicación implemente el algoritmo.

**Ejemplo integrador:** se copia un snapshot no cifrado indicando una clave KMS; desde esa copia cifrada se crea un volumen nuevo y se adjunta a la instancia.

## Cifrado de EBS

Al crear un volumen EBS cifrado:

- Datos en reposo se cifran dentro del volumen.
- Datos en movimiento entre instancia y volumen se cifran.
- Snapshots quedan cifrados.
- Volúmenes creados desde snapshot quedan cifrados.
- Cifrado y descifrado son transparentes.
- Impacto mínimo en latencia.
- Usa claves KMS con AES-256.
- Copiar un snapshot no cifrado permite cifrado.
- Snapshots de volúmenes cifrados están cifrados.

### Cifrar un volumen EBS existente

1. Crear snapshot del volumen EBS.
2. Cifrar snapshot mediante copia.
3. Crear nuevo volumen EBS desde snapshot; el volumen queda cifrado.
4. Adjuntar volumen cifrado a instancia original.
