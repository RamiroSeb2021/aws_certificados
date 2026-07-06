# IAM y CLI de AWS

> Fuente: `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`
> Páginas fuente: 24–40
> Índice Udemy relacionado: sección 4 `IAM y CLI de AWS`
> Método: extracción local con `pdftotext -layout`.
> No se agrega contenido AWS nuevo; se preserva significado de fuente.

## Criterio de edición

- Se reorganizan las diapositivas en secciones de estudio, manteniendo el significado de la fuente.
- Se conservan conceptos, ejemplos, advertencias y nombres de servicios presentes en las páginas fuente.
- Las demos del índice Udemy se reflejan como contexto de sección; el contenido técnico sale de las páginas 24–40.

## IAM: usuarios, grupos y permisos

- IAM significa `Identity and Access Management` y aparece como servicio global.
- La cuenta root se crea por defecto y no debe utilizarse ni compartirse.
- Los usuarios representan personas dentro de una organización.
- Los usuarios pueden agruparse.
- Los grupos contienen usuarios, no otros grupos.
- Un usuario no está obligado a pertenecer a un grupo y puede pertenecer a varios grupos.

### Políticas IAM

- A usuarios o grupos se les pueden asignar documentos JSON llamados políticas.
- Las políticas definen los permisos de los usuarios.
- AWS aplica el principio de mínimo privilegio: no dar más permisos de los que el usuario necesita.
- La fuente muestra herencia de políticas entre grupos y usuarios como ejemplo visual.

### Estructura de una política IAM

Una política consta de:

- `Version`: versión del lenguaje de la política; la fuente indica incluir siempre `2012-10-17`.
- `Id`: identificador opcional para la política.
- `Statement`: una o más declaraciones individuales; es obligatorio.

Cada declaración puede incluir:

- `Sid`: identificador opcional de la declaración.
- `Effect`: permite o deniega acceso (`Allow` / `Deny`).
- `Principal`: cuenta, usuario o rol al que aplica la política.
- `Action`: lista de acciones permitidas o denegadas.
- `Resource`: lista de recursos sobre los que aplican las acciones.
- `Condition`: condiciones opcionales para que la política esté en efecto.

## Seguridad de acceso

### Política de contraseñas

AWS permite configurar una política de contraseñas para mejorar la seguridad:

- Longitud mínima.
- Tipos de caracteres requeridos:
  - mayúsculas;
  - minúsculas;
  - números;
  - caracteres no alfanuméricos.
- Permitir que usuarios IAM cambien sus propias contraseñas.
- Requerir cambio de contraseña después de un tiempo.
- Impedir reutilización de contraseñas.

### Multi Factor Authentication (MFA)

- Los usuarios pueden cambiar configuraciones o eliminar recursos de una cuenta AWS.
- La fuente recomienda proteger la cuenta root y usuarios IAM.
- MFA combina contraseña conocida + dispositivo de seguridad poseído.
- Beneficio principal: si la contraseña es robada o hackeada, la cuenta no queda comprometida.

Opciones de dispositivos MFA mencionadas:

- Dispositivo virtual MFA:
  - Google Authenticator, solo en teléfono.
  - Authy, multidispositivo.
  - Soporte para múltiples tokens en un dispositivo.
- Clave de seguridad Universal 2nd Factor (U2F):
  - YubiKey de Yubico, tercero.
  - Soporte para múltiples usuarios root e IAM con una única clave.
- Dispositivos MFA de llavero por hardware:
  - Gemalto, tercero.
  - SurePassID para AWS GovCloud (US), tercero.

## Formas de acceder a AWS

La fuente presenta tres opciones:

- Consola de administración de AWS: protegida por contraseña + MFA.
- AWS CLI: protegida por claves de acceso.
- AWS SDK: protegido por claves de acceso para uso desde código.

### Claves de acceso

- Se generan desde la consola de AWS.
- Los usuarios gestionan sus propias claves de acceso.
- Son secretas, como una contraseña; no deben compartirse.
- `Access Key ID` se compara en la fuente con un nombre de usuario.
- `Secret Access Key` se compara en la fuente con una contraseña.
- La fuente incluye claves falsas como ejemplo y recalca no compartirlas.

## AWS CLI y AWS SDK

### AWS CLI

- Herramienta para interactuar con servicios de AWS mediante comandos en la shell.
- Da acceso directo a las API públicas de servicios AWS.
- Permite desarrollar scripts para gestionar recursos.
- Es open source: `https://github.com/aws/aws-cli`.
- Es alternativa al uso de la consola de administración de AWS.

### AWS SDK

- `AWS Software Development Kit`.
- APIs específicas por lenguaje mediante bibliotecas.
- Permite acceder y administrar servicios AWS mediante programación.
- Se integra en la aplicación.
- La fuente menciona SDKs para:
  - JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js y C++;
  - móviles, como Android e iOS;
  - dispositivos IoT, como Embedded C y Arduino.
- La fuente indica que AWS CLI está construido sobre AWS SDK para Python.

## Roles IAM para servicios

- Algunos servicios AWS necesitan realizar acciones en nombre del usuario.
- Para eso, se asignan permisos a servicios AWS mediante Roles IAM.
- Roles comunes mencionados:
  - roles de instancia EC2;
  - roles de función Lambda;
  - roles para CloudFormation.

## Herramientas de seguridad IAM

- `IAM Credentials Report` / informe de credenciales IAM:
  - opera a nivel de cuenta;
  - enumera todos los usuarios de la cuenta y el estado de sus credenciales.
- `IAM Access Advisor` / asesor de acceso IAM:
  - opera a nivel de usuario;
  - muestra permisos de servicio concedidos al usuario y cuándo se accedió por última vez a esos servicios;
  - sirve para revisar políticas.

## Buenas prácticas IAM

- No usar cuenta root excepto para configuración de cuenta AWS.
- Un usuario físico = un usuario AWS.
- Asignar usuarios a grupos y permisos a grupos.
- Crear política de contraseñas fuerte.
- Usar y reforzar MFA.
- Crear y usar roles para dar permisos a servicios AWS.
- Usar claves de acceso para acceso programático mediante CLI o SDK.
- Revisar permisos con informe de credenciales IAM o asesor de acceso IAM.
- No compartir usuarios IAM ni claves de acceso.

## Claves de repaso

- IAM es global; usuarios representan personas; grupos contienen usuarios; políticas JSON describen permisos.
- Cuenta root: usar solo para configuración de cuenta AWS, no para trabajo diario.
- MFA protege incluso si una contraseña es robada.
- Consola usa contraseña + MFA; CLI y SDK usan claves de acceso.
- Roles IAM permiten que servicios AWS actúen con permisos asignados.
- Auditoría IAM: `Credentials Report` a nivel cuenta y `Access Advisor` a nivel usuario.

## Caveats de extracción

- Las páginas 27, 31 y 32 son muy visuales; se preservan relaciones y opciones visibles, pero no se replica el diagrama.
- La página 34 contiene claves falsas; se conserva solo la advertencia y naturaleza del ejemplo, no como credenciales útiles.
