# Seguridad de RDS y Aurora

> Fuente principal: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 184.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 9, lectura 9: Seguridad RDS.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y caveats se mantienen como aparecen en el PDF y pueden cambiar con el tiempo.

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
