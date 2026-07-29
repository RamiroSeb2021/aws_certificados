# Cifrado de Amazon EBS

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 110–111.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 7, lectura 10: Cifrado de EBS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
