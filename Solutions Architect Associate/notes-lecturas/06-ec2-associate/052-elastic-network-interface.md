# Elastic Network Interface (ENI): interfaz de red elástica

> Fuente principal: documento `Solutions Architect Associate/AWS-Certified-Solutions-Architect-v5.pdf`.
> Páginas fuente: 89.
> Índice relacionado: `Solutions Architect Associate/indice-lecturas.md` — sección 6, lecturas 5 y 7: ENI y lectura extra.
> Método: extracción local con `pdftotext -layout` y revisión visual de las diapositivas relevantes.
> Fuente complementaria: [AWS News Blog — New: Elastic Network Interfaces in the Virtual Private Cloud](https://aws.amazon.com/blogs/aws/new-elastic-network-interfaces-in-the-virtual-private-cloud/).
> Verificación actual: [Amazon EC2 User Guide — Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html). El artículo original es de 2011; se usa por su modelo conceptual y no para límites numéricos actuales.
> Se preserva el significado de la fuente; cualquier complemento externo queda identificado.

## Criterio de edición

- Una lectura del curso por archivo.
- Redacción y estructura optimizadas para repaso activo.
- Límites, cifras y advertencias se mantienen como aparecen en el documento fuente y pueden cambiar con el tiempo.

## Idea central en lenguaje sencillo

Una instancia **Amazon Elastic Compute Cloud (EC2)** es una computadora virtual. Para comunicarse con otras computadoras necesita una conexión de red virtual. Esa conexión se representa mediante una **Elastic Network Interface (ENI)** o interfaz de red elástica.

**Ejemplo:** una portátil necesita un adaptador Wi-Fi para conectarse con el router. De forma parecida, una instancia EC2 necesita una ENI para conectarse con una red de Amazon Web Services (AWS).

## Diccionario mínimo antes de empezar

No es necesario memorizar todavía las siglas. Primero hay que entender qué representa cada cosa.

### AWS: Amazon Web Services

**AWS** significa `Amazon Web Services`. Es una plataforma que permite alquilar recursos tecnológicos por Internet, como computadoras, almacenamiento y redes.

**Ejemplo:** en lugar de comprar un servidor físico y colocarlo en una oficina, se puede alquilar una computadora virtual en AWS durante el tiempo que la necesites.

### Cloud o nube

La **nube** consiste en utilizar computadoras y servicios que pertenecen a un proveedor y que se administran por Internet. Esas computadoras siguen siendo físicas, pero están dentro de centros de datos del proveedor. Un **centro de datos** es un edificio preparado para alojar muchos servidores, conexiones de red y sistemas eléctricos.

**Ejemplo:** cuando alquilás una computadora virtual, no recibís una computadora en tu casa. El proveedor la ejecuta sobre servidores físicos ubicados en sus centros de datos.

### Red

Una **red** es un conjunto de dispositivos conectados que pueden intercambiar información.

**Ejemplo:** el teléfono, la computadora y el televisor de tu casa pueden conectarse al mismo router Wi-Fi y formar una red doméstica. El router es el aparato que conecta esos dispositivos y dirige sus comunicaciones.

### Tarjeta de red física

Una **tarjeta de red** es el componente que permite que una computadora se conecte con una red. Puede estar integrada dentro del equipo y utilizar un cable de red o Wi-Fi.

**Ejemplo:** cuando una portátil se conecta al router mediante Wi-Fi, su adaptador Wi-Fi está cumpliendo la función de tarjeta de red.

### Tarjeta de red virtual

Una **tarjeta de red virtual** es una representación creada por software que cumple para una computadora virtual la misma función que una tarjeta de red física: darle un punto por el cual enviar y recibir información.

No es una pieza que puedas tocar. El sistema operativo de la computadora virtual la reconoce como si fuera un dispositivo de red real.

**Ejemplo:** una computadora virtual con Linux puede mostrar una interfaz llamada `eth0`. Es el nombre que Linux utiliza normalmente para identificar una de sus conexiones de red virtuales.

### Interfaz de red

Una **interfaz de red** es el punto de conexión que una computadora utiliza para comunicarse con una red. En este contexto, “interfaz” y “tarjeta de red” describen prácticamente la misma función.

**Ejemplo:** el adaptador Wi-Fi es una interfaz física; `eth0` dentro de una computadora virtual es una interfaz virtual.

### Sistema operativo

El **sistema operativo** es el software principal que administra una computadora y permite ejecutar otros programas. Algunos ejemplos son Windows y Linux.

**Ejemplo:** una computadora virtual puede ejecutar Linux como sistema operativo y, sobre Linux, ejecutar distintos programas.

### Servidor, cliente y solicitud

Un **servidor** es una computadora o programa que ofrece algo a otros dispositivos. Un **cliente** es el dispositivo o programa que lo solicita. Una **solicitud** es el mensaje que el cliente envía para pedir ese contenido o servicio.

**Ejemplo:** el navegador es el cliente, pide una página mediante una solicitud y el servidor web responde enviando la página.

### IP: Internet Protocol

**IP** significa `Internet Protocol`, en español **Protocolo de Internet**. Una dirección IP es un número que permite localizar un dispositivo o una interfaz dentro de una red.

**Ejemplo:** `10.0.1.25` puede ser la dirección utilizada para localizar la conexión de red de un servidor virtual.

### Puerto de red

Un **puerto** es un número que identifica a qué programa o servicio debe entregarse una comunicación después de llegar a una dirección IP.

**Ejemplo:** una solicitud puede llegar a la IP `10.0.1.25` y al puerto `443`, utilizado normalmente por servicios web con comunicación cifrada.

### HTTPS: Hypertext Transfer Protocol Secure

**HTTPS** significa `Hypertext Transfer Protocol Secure`. Es el protocolo utilizado para comunicar un navegador con un sitio web mediante una conexión cifrada.

**Ejemplo:** cuando se abre una dirección que comienza con `https://`, el navegador utiliza HTTPS; normalmente se comunica con el puerto `443` del servidor.

### EC2: Elastic Compute Cloud

**EC2** significa `Elastic Compute Cloud`. Es el servicio de AWS para crear computadoras virtuales llamadas **instancias**.

**Ejemplo:** se puede crear una instancia EC2 con Linux e instalar allí una aplicación web.

### VPC: Virtual Private Cloud

**VPC** significa `Virtual Private Cloud`, en español **nube privada virtual**. Es una red virtual aislada que el cliente controla dentro de AWS.

**Ejemplo:** una empresa puede crear una VPC llamada `red-tienda` para alojar allí los servidores de su tienda virtual.

### Subred

Una **subred** es una división más pequeña de una VPC. Sirve para agrupar recursos y organizar dónde se conectan.

**Ejemplo:** dentro de `red-tienda` puede existir una subred pública para servidores web y una subred privada para bases de datos.

### Región de AWS

Una **región** es un área geográfica donde AWS agrupa varias Zonas de Disponibilidad independientes.

**Ejemplo:** `us-east-1` es una región de AWS ubicada en el norte de Virginia, Estados Unidos.

### AZ: Availability Zone

**AZ** significa `Availability Zone`, en español **Zona de Disponibilidad**. Es una ubicación física separada dentro de una región de AWS y contiene uno o más centros de datos.

**Ejemplo:** una VPC puede tener una subred en la Zona de Disponibilidad `us-east-1a` y otra subred en `us-east-1b`.

## Qué es una ENI

**ENI** significa `Elastic Network Interface`, en español **interfaz de red elástica**. Es una tarjeta de red virtual que existe dentro de una VPC y que puede conectarse a una instancia EC2.

**Ejemplo:** se crea una instancia EC2 para ejecutar una tienda virtual. AWS conecta una ENI principal a esa instancia. La tienda se ejecuta en EC2, pero las comunicaciones entran y salen por la ENI.

### MAC: Media Access Control

**MAC** significa `Media Access Control`, en español **control de acceso al medio**. Una dirección MAC es un identificador asignado a una interfaz de red para distinguirla de otras interfaces dentro de una red.

Una dirección MAC suele escribirse como seis grupos de números o letras separados por dos puntos. En una ENI no identifica una pieza física: identifica esa tarjeta de red **virtual**.

**Ejemplo:** una ENI podría tener una dirección MAC ficticia como `02:7B:64:10:20:30`. Si esa ENI secundaria se conecta a otra instancia EC2, conserva su dirección MAC porque el identificador pertenece a la ENI.

La dirección MAC y la dirección IP NO hacen el mismo trabajo:

- la **dirección IP** ayuda a localizar la conexión dentro de una red;
- la **dirección MAC** identifica la interfaz de red concreta que debe recibir la información en su entorno de red local.

**Ejemplo:** imagine un edificio. La dirección IP se parece al número del apartamento al que debe llegar un paquete; la dirección MAC se parece a la identificación de la persona concreta que lo recibe allí. Ambas ayudan a entregar correctamente, pero identifican cosas diferentes.

### Grupo de seguridad

Un **grupo de seguridad** es un conjunto de reglas que decide qué comunicaciones se permiten hacia o desde una ENI.

**Ejemplo:** una regla puede permitir que los navegadores accedan al puerto `443` de la ENI, pero impedir conexiones hacia otros puertos que no se necesitan.

La ENI reúne la identidad y parte de la configuración de red que la instancia necesita para comunicarse:

- sus direcciones IP;
- su dirección MAC;
- los grupos de seguridad que filtran tráfico;
- la subred y la Zona de Disponibilidad a las que pertenece.

La idea IMPORTANTE es que **la dirección de red pertenece a la ENI, no directamente a la instancia EC2**. La instancia aporta capacidad de procesamiento, memoria y sistema operativo; la ENI aporta una forma de entrar y salir de la red.

**Ejemplo:** si una ENI secundaria pasa de `EC2-A` a `EC2-B`, su configuración de red viaja con ella. La capacidad de procesamiento no viaja, porque pertenece a cada instancia EC2.

### Analogía: computadora y adaptador de red

Pensá en una computadora portátil:

- la portátil representa la instancia EC2;
- el adaptador Wi-Fi representa la ENI;
- la dirección IP identifica ese adaptador dentro de la red;
- las reglas del grupo de seguridad deciden qué comunicaciones se permiten.

En AWS todo esto es virtual, pero la separación conceptual es parecida.

### ENI principal y ENI secundaria

- **ENI principal:** interfaz que AWS conecta al crear una instancia EC2. Permanece con esa instancia y no puede desconectarse.
  - **Ejemplo:** al crear `EC2-A`, AWS crea o conecta su interfaz principal `eth0`, que contiene su dirección privada principal.
- **ENI secundaria:** interfaz adicional que se puede conectar a una instancia compatible y, posteriormente, desconectar o conectar a otra instancia dentro de la misma Zona de Disponibilidad.
  - **Ejemplo:** `ENI-servicio` puede estar conectada a `EC2-A` y luego trasladarse a `EC2-B` si se necesita reemplazar el servidor.

## Cómo encajan VPC, subred, ENI y EC2

```text
VPC
└── Subred dentro de una Zona de Disponibilidad
    └── ENI: IP + MAC + grupos de seguridad
        └── Instancia EC2: procesamiento + memoria + sistema operativo + aplicación
```

1. La **VPC** es la red virtual general.
2. Una **subred** es una parte más pequeña de esa red y pertenece a una Zona de Disponibilidad.
3. La **ENI se crea dentro de una subred**, por lo que queda vinculada a esa AZ.
4. La ENI se conecta a una instancia EC2 para darle conectividad en esa red.

## Ejemplo básico: servidor web

Imaginá una instancia EC2 que ejecuta una página web:

1. AWS conecta una ENI principal a la instancia.
2. La ENI tiene una IP privada, por ejemplo `10.0.1.25`.
3. El grupo de seguridad de la ENI permite tráfico web por el puerto `443`.
4. Una solicitud llega a la IP de la ENI.
5. El grupo de seguridad verifica si la comunicación está permitida.
6. Si está permitida, la información llega a la aplicación que se ejecuta en EC2.

La ENI no contiene la página web ni procesa la aplicación. Su trabajo es proporcionar la conexión y la identidad dentro de la red.

## Qué información puede tener una ENI

### IPv4: Internet Protocol version 4

**IPv4** significa `Internet Protocol version 4`, en español **Protocolo de Internet versión 4**. Es una versión del sistema de direcciones IP y utiliza números separados por puntos.

**Ejemplo:** `10.0.1.25` es una dirección IPv4 privada.

### IPv4 privada primaria

Es la dirección privada principal de la ENI dentro de su subred. **Privada** significa que se utiliza dentro de la red virtual y que no funciona por sí sola como dirección pública de Internet.

**Ejemplo:** la ENI principal de un servidor puede usar `10.0.1.25` para comunicarse con una base de datos dentro de la misma VPC.

### IPv4 privadas secundarias

Son direcciones privadas adicionales asociadas con la misma ENI.

**Ejemplo:** una ENI puede conservar `10.0.1.25` como dirección principal y usar `10.0.1.26` para un segundo servicio.

### Elastic IP

Una **Elastic IP** es una dirección IPv4 pública y fija que pertenece a la cuenta de AWS y puede asociarse con una dirección privada de una ENI.

**Ejemplo:** aunque se reemplace la instancia EC2, una Elastic IP asociada con la ENI puede conservar la misma dirección pública para los usuarios.

### IPv4 pública

Es una dirección que puede utilizarse para comunicación pública cuando las demás configuraciones de red y seguridad lo permiten.

**Ejemplo:** un usuario desde su casa puede abrir una página alojada en EC2 utilizando su dirección pública, siempre que la red y el grupo de seguridad permitan ese acceso.

### Dirección MAC

Es el identificador de la interfaz explicado anteriormente. Pertenece a la ENI y se conserva con ella.

**Ejemplo:** al trasladar una ENI secundaria a otra instancia, su dirección MAC también se traslada.

### Source/Destination Check

`Source/Destination Check` significa **comprobación de origen y destino**. AWS verifica normalmente que una instancia sea el origen o el destino del tráfico que procesa.

**Ejemplo:** un servidor web recibe solicitudes dirigidas a él y envía sus propias respuestas, por lo que la comprobación normal tiene sentido. Si una instancia funciona como intermediaria y reenvía mensajes destinados a otras computadoras, puede necesitar una configuración diferente.

### Delete on Termination

`Delete on Termination` significa **eliminar al terminar**. Indica si la interfaz debe eliminarse cuando se termina la instancia EC2 asociada.

**Ejemplo:** si está desactivado para una ENI secundaria, se puede terminar `EC2-A`, conservar la ENI y conectarla después a `EC2-B`.

## Por qué se llama “Elastic”

Según el artículo de AWS, una ENI puede tener una vida independiente de una instancia EC2:

- se puede crear antes de crear la instancia;
- una ENI secundaria puede conectarse a una instancia que ya está ejecutándose;
- puede conservar sus direcciones IP, dirección MAC y grupos de seguridad al cambiarla de una instancia a otra;
- puede seguir existiendo después de terminar una instancia si no está configurada para eliminarse.

Aquí **elastic** significa que la interfaz se puede crear, conectar, desconectar y reutilizar con flexibilidad. No significa que aumente automáticamente su capacidad.

> Importante: cada instancia tiene una ENI principal que no puede separarse. La movilidad entre instancias se aplica a ENI secundarias.

## Ejemplo de conmutación por error

La **conmutación por error**, también llamada `failover`, consiste en pasar un servicio a un recurso de reemplazo cuando el recurso principal falla.

**Ejemplo:** si el servidor principal deja de funcionar, otro servidor preparado puede continuar atendiendo a los usuarios.

Una empresa tiene dos instancias:

- `EC2-A`: servidor activo;
- `EC2-B`: servidor de reemplazo;
- `ENI-servicio`: interfaz secundaria con la IP utilizada por los clientes.

Funcionamiento:

1. `ENI-servicio` está conectada a `EC2-A`.
2. Los clientes llegan al servicio usando la IP de esa ENI.
3. `EC2-A` falla.
4. Se desconecta `ENI-servicio` de `EC2-A` y se conecta a `EC2-B`.
5. La IP, la dirección MAC y los grupos de seguridad viajan con la ENI.
6. El tráfico vuelve a llegar al servicio, ahora ejecutándose en `EC2-B`.

La ENI funciona como una **identidad de red reutilizable**. Cambia la computadora que atiende, pero se conserva la forma de localizarla y las reglas de acceso asociadas.

## Otro caso del artículo: dos redes para una instancia

Una instancia puede tener dos ENI, ubicadas en subredes de la misma Zona de Disponibilidad, con responsabilidades diferentes:

- **Subred pública:** parte de la VPC diseñada para recursos que pueden comunicarse públicamente cuando la configuración lo permite.
  - **Ejemplo:** una ENI pública recibe las solicitudes de los usuarios de una página web.
- **Subred privada:** parte de la VPC diseñada para recursos que no deben recibir conexiones directas desde Internet.
  - **Ejemplo:** otra ENI se utiliza únicamente para administración y envío de registros internos.

Cada ENI puede tener grupos de seguridad distintos. Esto permite separar el tráfico público del tráfico administrativo.

## Qué NO es una ENI

- No es una instancia EC2.
- No aporta capacidad de procesamiento ni memoria para ejecutar aplicaciones.
- No es toda la VPC ni toda la subred.
- No es por sí sola una conexión a Internet: el resto de la red y sus reglas también deben permitir la comunicación.
- No distribuye solicitudes entre varios servidores; solamente proporciona una interfaz de red.

## Claves de repaso

- **EC2 ejecuta el software; ENI conecta EC2 con la red.**
- La ENI pertenece a una subred y, por ello, a una Zona de Disponibilidad.
- Las direcciones IP y los grupos de seguridad están asociados con la ENI.
- Una instancia recibe una ENI principal y puede admitir ENI secundarias según el tipo de instancia.
- Una ENI secundaria puede trasladar su identidad de red a otra instancia para ciertos diseños de recuperación.
