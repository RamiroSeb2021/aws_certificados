# Notas curso Cloud Practitioner CFL-C02 2026

> Fuente: `cloud_practitioner/Notas curso Cloud Practitioner CFL-C02 2026.odt`.
> Extracción local con `pandoc` a Markdown y limpieza conservadora de redacción/estructura.
> No se agrega contenido AWS nuevo; se preservan servicios, componentes, features e ideas presentes en la fuente.

## Criterio de edición

- Se corrigieron errores obvios de tipeo, casing de servicios AWS y estructura Markdown.
- Se mantuvo mezcla español/inglés cuando venía de la fuente.
- Notas dudosas o incompletas se conservaron para no cambiar significado.


El curso cubrirá 40 AWS services de los más de 200 que tiene AWS

AWS simplify the migration of database AWS: AWS database migration
service

Se estudiará: AWS Storage Gateway y Amazon EC2

### Ruta certificaciones AWS

### Foundational

Learn AWS Cloud fundamentals and core concepts - no prior experience
needed

- Cloud practitioner
- AI Practitioner

### Associate

Validate core AWS skills. Prior cloud or IT experience recommended

- Solutions architect
- Developer
- SysOps Administrator
- Data Engineer
- Machine Learning Engineer

### Professional

Master advanced AWS architecture and solutions. 2+ years AWS experience
required

- DevOps Engineer
- Solutions Architect

### Specialty

Demonstrate expertise in specific AWS technologies and services

- Machine learning
- Advanced Networking
- Security

AWS da 100 dólares en créditos por abrir una cuenta y 200 por hacer
tareas específicas

## Section 3: What is Cloud Computing?

Usar red para enrutar los paquetes, los datos al servidor

Para que el cliente encuentre el servidor y viceversa se usa las IPs

What is a server composed of?

Compute CPU

Memory ram

Storage: data

Database: store data in a structured way

Network: routers, switch, DNS server

Router: conecta diferentes redes y dirige el tráfico entre ellas

Tareas: asignar acceso a internet, dirigir paquetes de datos, crear
redes wifi, hacer nat y firewall básico

Switch: conecta dispositivos dentro de una misma red

DNS server: traduce nombres de dominio a direcciones IP

DNS: domain name system – Sistema de nombre de dominio

### IT Terminology

Network: cables, routers and servers connected with each other

Router: a networking device that forwards data packets between computer
networks. They know where to send your packets on the internet

Switch: takes a packet and send it to the correct server/client on your
network

Cloud computing is the on-demand delivery of computer power, database
storage, applications, and other IT resources.

Through a cloud services platform with pay-as-you-go pricing.

You can provision exactly the right type and size of computing resources
you need.

You can access as many resources as you need, almost instantly.

Simply way to access servers, storage, databases and a set of
application services

Amazon Web Services owns and maintains the network-connected hardware
required for these application services, while you provision and use
what you need via a web application

### The deployment models of the cloud

### Private cloud

Cloud services used by a single organization, not exposed to the public

Complete control

Security for sensitive applications

Meet specific business needs

For instance, Rackspace

### Public Cloud

### There are three providers

- Microsoft Azure
- Google Cloud
- Amazon Web Services AWS

Cloud resources owned and operated by a third-party cloud service
provider delivered over the internet

Six advantages of cloud computing

### Hybrid Cloud

Keep some servers on premises and extend some capabilities to the cloud

Control over sensitive assets in your private infrastructure

### The five characteristics of Cloud Computing

- On-demand self service (es totalmente a pedido y de autoservicio):
users can provision resources and use them without human interaction
from the service provider
- Broad network access: resources available over the network and can be
accessed by diverse client platforms
- Multi-tenancy and resource pooling (multicliente y recursos
compartidos): Multiple customers can share the same infrastructure and
applications with security and privacy and multiple customers are
serviced from the same physical resources
- Rapid elasticity and scalability: automatically and quickly acquire
and dispose resources when needed. Quickly and easily scale base on
demand
- Measured service: usage is measured, users pay correctly for what they
have used

### Six advantages of Cloud Computing

- Pay on-demand. Don't own hardware: Reduce el coste total de propiedad y
de sus gastos operativos
- Benefit from massive economies of scale: prices are reduced as AWS is
more efficient due to large scale
- Stop guessing capacity: scale based on actual measured usage
- Increase speed and agility
- Stop spending money running and maintaining data centers
- Go global in minutes leverage the AWS global infrastructure

Problems solved by the Cloud

Flexibility

Cost effectiveness

Scalability

Elasticity

High availability and fault tolerance

Agility

### Types of cloud computing

### Infrastructure as a Service(IaaS)

### El proveedor ofrece recursos básicos de computación

Cuándo usar IaaS

- Cuando necesitas mucho control del sistema
- Para migrar servidores tradicionales a la nube
- Para configuraciones personalizadas

- Provide building blocks for cloud IT
- Provides networking, computers, data storage space
- Highest level of flexibility
- Easy parallel with traditional on-premises IT (Migrar de TI
tradicional en las instalaciones de la nube)

### Platform as a Service (PaaS)

El proveedor administra casi toda la infraestructura y la plataforma

- Removes the need for your organization to manage the underlying
infrastructure
- Focus on the deployment and management of your applications

### Software as a Service (SaaS)

- Completed product that is run and managed by the service provider

### IaaS

Amazon EC2

GCP, Azure, Rackspace,Digital Ocean, Linode

### PaaS

Elastic Beanstalk

Heroku, Google App Engine (GCP), Windows Azure

### SaaS

Many AWS services example: Rekognition for machine learning

Google Apps like gmail, Dropbox, Zoom

### Pricing of the cloud

36. Compute: pay for compute time
37. Storage: pay for data stored in the cloud
38. Data: transfer out of the cloud(data transfer in is free)

## AWS Cloud History

2002: internally launched

2003: Amazon infrastructure is one of their core strength. Idea to
market

2004: Launched publicly with SQS

2007: Launched in Europe

AWS enables you to build sophisticated scalable applications

Applicable to a diverse set of industries

Enterprise IT, Backup and storage, big data analytics, website hosting,
mobile and social apps

## AWS Global Infrastructure

- AWS regions
- AWS availability zones
- AWS Data centers
- AWS Edge locations/points of presence

### AWS regions

Names can be us-east-I, eu-west-3

Son un conjunto de centros de datos

### How to choose an AWS region

Cumplimiento con gobiernos que quieren que los datos sean locales en el
que se está desplegando la aplicación por lo que se debe lanzar el
aplicativo en la región francesa

Proximidad de los clientes para reducir la latencia de las respuestas

Servicios disponible existen en cada región, algunos nuevos servicios o
características no están disponible en todas las regiones

El precio varía en cada región

### AWS availability zones

Each region has many availability zones: usually 3 min is 3 max is 6

Each availability zone is one or more discrete data centers with
redundant power, networking and connectivity

They are separate from each other, so that they are isolated from
disasters

They are connected with high bandwidth ultra low latency networking

AWS points of presence (edge locations)

Amazon has 400+ points of presence en 90 ciudades en 40 países, esto
asegura que la entrega de contenidos posea baja latencia

## AWS Console

### AWS has global services

Identity and Access Management (IAM)

Route 53 (DNS service)

CloudFront (Content Delivery Network)

WAF (Web Application Firewall)

La mayoría de los servicios de Amazon van a tener alcance regional como
Amazon EC2 (Infraestructura como servicio), Elastic Beanstalk (Platform
como servicio), Lambda (Función como servicio), Rekognition (Software como
servicio)

También existe una tabla de regiones para saber que servicios hay
disponibles en cada una de estas

## Share Responsibility Model Diagram

## Responsabilidades del CLIENTE

### El cliente debe proteger y administrar

## 1. Datos del cliente

Customer Data

### Ejemplo

- archivos,
- bases de datos,
- información de usuarios.

## 2. Plataforma, aplicaciones, identidad y accesos

Platform, Applications, Identity & Access Management

### Incluye

- aplicaciones,
- usuarios,
- roles IAM,
- permisos.

## 3. Sistema operativo, red y firewall

Operating System, Network & Firewall Configuration

### Ejemplos

- reglas de seguridad,
- puertos,
- configuración Linux,
- iptables,
- Security Groups.

## 4. Cifrado y protección de datos

### Del lado cliente

Client-side data encryption & data integrity authentication

### Del lado servidor

Server-side encryption (file system and/or data)

### Protección del tráfico de red

Networking traffic protection (encryption, integrity, identity)

### Ejemplos

- HTTPS/TLS,
- certificados,
- VPN,
- cifrado de discos.

## Responsabilidades de AWS

AWS protege la infraestructura física y lógica de la nube.

## 1. Software administrado por AWS

Software

### Incluye

- hipervisores,
- servicios internos,
- plataformas cloud.

## 2. Infraestructura tecnológica

### Compute

Compute

Servidores físicos.

### Storage

Storage

Discos y almacenamiento.

### Database

Database

Infraestructura de bases de datos.

### Networking

Networking

Switches, routers, backbone global.

## 3. Infraestructura global AWS

Hardware / AWS Global Infrastructure

### Incluye

### Regions

Regions

Regiones AWS.

### Availability Zones

Availability Zones

Datacenters separados dentro de una región.

### Edge Locations

Edge Locations

Puntos distribuidos para CloudFront y servicios globales.

AWS aceptable use policy

NO illegal harmful or offensive use or content

NO security violations

NO network abuse

NO email or other message abuse

## Section 4: IAM - IDENTITY AND ACCESS MANAGEMENT

Servicio iterador

Global services

Se crean usuarios y se asignan a grupos

Cuando se creó una cuenta, esa es una cuenta raíz: root account created
by default,solo se debe usar para configurar la cuenta, en lugar de
usarla o compartirla lo que se debe hacer es crear usuarios

Un usuario representa una persona dentro de la organización y los
usuario pueden ser agrupados si tienen sentido

Grupos solo contienen usuarios no otros grupos

Hay usuarios que no deben pertenecer a un grupo, no es lo recomendable
pero se puede hacer en AWS, así como un usuario puede pertenecer a
varios grupos

Porque los grupos y los usuarios? Para permitir crear una cuenta AWS y
para esto debemos otorgarles permisos

A los usuarios y grupos se les puede asignar documentos JSON (JSON
documents) llamados policies IAM = lo que un grupo de usuarios tiene
permitido hacer

Principio de Privilegio Mínimo: dar solo los permisos necesarios a un
usuario

### IAM Policies inheritance

Política en línea: solo se adjunta a un usuario, rol o grupo: no se
reutilizan. Si eliminas el usuario o rol la política también desaparece

Políticas administradas: son reutilizables, es decir que se pueden
adjuntar a muchos usuarios o roles, AWS ya trae muchas predefinidas

### Política de IAM consta de

Version: consta de un número de versión por lo que normalmente es el
17-10-2012, ese es la versión del idioma de la política

ID: para identificar esa política(optional)

### Statement: una o más declaraciones individuales (required)

- Sid: identificador de la declaración, opcional
- Effect: si la declaración permite o deniega acceso (Allow, deny)
- Principal: a qué cuentas o usuario o rol se aplicará esa política
- Action: lista de acciones que la política permite o deniega
- Resource: lista de recursos a los que se aplicarán las acciones
- Condition: a la que se debe o no aplicar la declaración, optional

## Tip Para Examen: Comprender El Efecto, El Principio, La Acción Y El
RECURSO

Policy AdministratorAccess: da acceso a todos los servicios de AWS

Se pueden seleccionar políticas predeterminadas o crear unas nuevas con
acciones y accesos específicos

IAM password policy: protección de usuario y grupos. Tenemos dos
### mecanismos de defensa

- Política de contraseñas: entre más fuerte la contraseña más seguridad
tendrán tus cuentas. Hay diferentes opciones: exigir un mínimo de
longitud, solicitar caracteres específicos: mayúsculas, minúsculas,
números. Permitir o no a los usuarios cambiar o no sus propias
contraseñas o que la cambien después de un tiempo o evitar la
reutilización de contraseñas
- Multi factor authentication – MFA: muy recomendable de usar, es
indispensable proteger las cuentas raíz y los usuarios IAM.
Dispositivo MFA: token generador.

## MFA Devices Options In AWS:

- Virtual MFA device: Google Authenticator, phone only or Authy by
Amazon para múltiples tokens en un solo dispositivo, con este último
puedes tener tantas cuentas o usuarios como desees
- Universal 2nd factor U2F Security Key: it is a physical device: Yubico
as a example
- Hardware Key Fob MFA device
- Hardware Key Fob MFA device for AWS GovCloud

Users accessing AWS

### They have three options

AWS management console: protected by password and MFA

AWS command line interface (CLI): protected by access keys, its necessary
to download in a few seconds from our terminal

AWS software developer kit (SDK) for code: protected by access keys,
cuando se desea llamar a las API de AWS desde el código de la aplicación
y esto está protegido por la mismas claves de acceso

Las llaves de acceso son generadas a través de la consola de AWS y los
usuarios son responsables del manejo de sus propias claves de acceso, esas
llaves son secretos como una contraseña por lo que no se deben
compartir.

Software Development Kit es un conjunto de librerías de un lenguaje
específico, por lo que habrá SDK para diferentes lenguajes de
programación y asimismo permite acceder a los servicios de AWS y APIs
programados, no se usa a través de una terminal sino que está embebido en
la aplicación, soporta muchos diferentes lenguajes como JavaScript,
Python, Java, go. También hay una versión para Android, iOS an IoT

Instalación de AWS command line on Windows

Cuando uno usa CloudShell para list los usuarios, devolverá una
respuesta app como si las credenciales estén siendo usadas, usadas al
mismo tiempo de ser consultadas y eso porque las llamadas de la API
están funcionando y por default se puede especificar cualquier tipo de
región que uno quiera, en CloudShell la región por defecto es la que
estás actualmente usando en el logueo

Otro aspecto a resaltar es que al usar CloudShell se tiene un
repositorio completo, lo que significa que guarda información de un
archivo recién creado por consola, permanecen

Otro aspecto interesante de CloudShell es que se puede configurar, por
ejemplo, el tamaño de la fuente, el tema o si el usuario quiere based or
nuts

También existe la posibilidad de subir y descargar archivos. Por ejemplo,
la descarga se realiza con la ruta del archivo. En el botón desplegable
actions se pueden subir y bajar archivos. También se puede tener varias
tabs para trabajar simultáneamente con la consola

El único problema es que CloudShell solo está disponible en algunas
regiones

### IAM roles for services

A veces es necesario realizar acciones en a través de nuestro nombre o
por nuestra cuenta, para hacer tales acciones como usuario necesitamos
algunos tipo de permisos, por lo que se necesita asignar permisos en AWS
services y para esto se crea lo que se conoce como IAM roles, estas
roles son asignados para usuarios pero su intención no es para ser
usados por gente física sino para ser usados por AWS services

Por ejemplo, para un EC2 instance puede realizar acciones necesitamos
dar los permisos a nuestro EC2 instances, para esto se hace una IAM role
y ambos van a ser una entidad, para obtener cierta información el EC2
usará el IAM role, si tal role tiene los permisos se podrá hacer la
petición

### Algunos de los roles son

- EC2 Instance roles
- Lambda Function Roles
- CloudFormation

Entidad: es cualquier identidad o componente que puede interactuar con
recursos de AWS y sobre el cual se pueden aplicar permisos

## Fundamentos EC2

EC2: Elastic Compute Cloud, infraestructura como servicio

Consiste en alquilar máquinas virtuales

Almacenar datos en unidades virtuales: EBS

Distribuir carga entre máquinas ELB

Escalar los servicios mediante Auto Scaling Group ASG

### EC2 tamaño y configuración

### Operating system

CPU

Ram

Storage space

Network attached EBS y EFS

## Amazon EBS (Elastic Block Store)

Amazon EBS

Es un almacenamiento tipo **disco duro virtual** para instancias EC2.

### Piensa en EBS como

- el SSD o disco duro conectado a una máquina virtual.

## Características

- Se conecta normalmente a **una instancia EC2**.
- Funciona a nivel de **bloques**.
- Muy rápido y con baja latencia.
- Ideal para sistemas operativos, bases de datos y aplicaciones.

## Ejemplo

### Tienes una instancia EC2 con Ubuntu

- el sistema operativo está instalado en un volumen EBS.
- si guardas archivos allí, quedan en ese “disco virtual”.

## Casos de uso

- Bases de datos
- Servidores web
- Sistemas operativos
- Aplicaciones empresariales

## Analogía

### EC2 + EBS sería como

- computador + disco duro interno.

## Amazon EFS (Elastic File System)

Amazon EFS

Es un sistema de archivos compartido en red.

### Piensa en EFS como

- una carpeta compartida a la que varias máquinas pueden acceder al
mismo tiempo.

## Características

- Varias instancias EC2 pueden usarlo simultáneamente.
- Funciona como un sistema de archivos Linux normal.
- Escala automáticamente.
- Acceso mediante red (NFS).

## Ejemplo

### Tienes 5 servidores web EC2

- todos leen imágenes desde el mismo EFS.
- si un servidor sube un archivo, los demás lo ven inmediatamente.

## Casos de uso

- Contenido compartido
- Aplicaciones distribuidas
- Machine learning
- Contenedores
- WordPress multi-servidor

## Analogía

### EC2 + EFS sería como

- varios computadores conectados a una carpeta compartida en red.

## Diferencia principal

| | | |
|--------------------|--------------------|----------------------|
| **Característica** | **EBS** | **EFS** |
| Tipo | Block storage | File storage |
| Compartido | Normalmente no | Sí |
| Conexión | Directa a EC2 | Por red |
| Velocidad | Muy alta | Alta |
| Escala automática | Limitada | Sí |
| Uso típico | Disco del servidor | Archivos compartidos |

## Relación con “red”

### La “red” aparece especialmente en EFS

- **EBS** se conecta casi directamente a la instancia.
- **EFS** funciona sobre red usando NFS.

### Por eso EFS suele verse como

- almacenamiento compartido en red.

## Ejemplo práctico sencillo

## EBS

### Un servidor con

- Ubuntu
- MySQL
- aplicación backend

Todo instalado en un volumen EBS.

## EFS

### Tres servidores web

- todos comparten:

- imágenes
- PDFs
- archivos de usuarios

Usan un mismo EFS.

## Regla rápida para recordarlo

- **EBS = disco duro de una máquina**
- **EFS = carpeta compartida por red**

### También existe

- Amazon S3 → almacenamiento de objetos (archivos tipo bucket)
- Amazon FSx → sistemas de archivos especializados
- Amazon EC2 → máquinas virtuales donde se usan EBS/EFS

### Si quieres, también puedo explicarte

- diferencia entre EBS vs EFS vs S3,
- cómo se conectan a EC2,
- o cómo se ven en una arquitectura real de AWS.

Launch wizard: herramienta para automatizar y simplificar el despliegue.
Funciona como un asistente

## Tipos comunes de storage en AWS

| | |
|--------------|------------------------------------|
| **Servicio** | **Qué es** |
| Amazon EBS | Disco duro para una sola EC2 |
| Amazon EFS | Sistema de archivos compartido |
| Amazon S3 | Almacenamiento de objetos/archivos |

### EC2 instance Types

### Seven different types

- General purpose
- Compute optimized
- Memory optimized
- Accelerated computing
- Storage optimized
- Instance features
- Measuring instance performance

Ejemplo de convención de tipos de EC2

M familia

5 generacion

Tamaño large

M5.large

General purpose: MAC T, M, A

Computed Optimez: dedicate gaming services, media transcodin. C

Memory optimized: fast performand. Databases high performance. R, X,
Higmemory z

Storage optimized: accessing to large data sets. Relation databases,
apllications, D

### Introducción a grupos de seguridad(firewalls) alrededor de EC2

They are the fundamental of network security in AWS, they control how
traffic is allowed or out of our EC2 instances.

Security groups only contain allow rules: allow to go in or go out

Security groups rules can reference by IP or by security group like
where your computer is from or by other security groups

Seccurity groups can reference each other

### Security groups are a firewall on our EC2 instannces, they regulate

access to ports

Authorised IP ranges – IPv4 AND IPv6

Control of inbound network from other to the instance

Control of outbound network

### Security group son de la siguiente manera

Type, protocol,, the port, source(IP address range, description

### Some things about security groups

- Can be attached to multiple instances

- An instances can have multiple security groups

- Lock down to a región o virtual private cloud VPC, AWS

- VPC uno crea EC2, base de datos, balanceadores de carga (Elastic
      Load Balancing)y servicios internos

It is a firewall outside your EC2 instance

Its good to maintain one separate security group for SSH access

When your application is not accesible probably it is a security group
issue

If you recieve a conection refused means your security group actually
worked, it is an application or it is not launched

All inbound traffic is block by default

### Classic ports to know

22 = SSH (secure shell) – log into a Linux instance for example EC2

21 = FTP (file transfer protocol) - upload files into a file share

22 SFTP(Secure File Transfer Protocol) - upload files using SSH

80 = HTTP – access unsecured websites

443 = HTTPS – Access secured websites

389 = RDP (Remote Desktop Protocol) - log into a Windows instance

SSH overview

How do you connects inside of your servers to perform some maintenance
or action?

For Linux you can use SSH to do a secure sheell into our servers

SSH is a command line interface utility which can be use on mac or Linux
as well as Windows over versión 10, if it is a previous versión of
Windows 10 there is something called putty, putty is available for any
kind of Windows

There is something new called EC2 instance connect which is going to use
your web browser to connect to EC2 instance and it is valid for mac,
Linux, Windows, all versions

SSG allows you to control a remote machi, ne or server, all using the
command line

The machine EC2 has a public IP. To access that machine there is a
security group where it was allowed the port 22 of SSH

SSH o EC2Tutorial.pem <ec2user@3.250.26.200>P public IP conectarse a a
Amazon Linux 2 AMI

Para salir con commandos exit o control g

### SHH thoubleshooting

** There's a connection timeout**

This is a security group issue. Any timeout (not just for SSH) is
related to security groups or a firewall.

**here's still a connection timeout issue**

If your security group is properly configured as above, and you still
have connection timeout issues, then that means a corporate firewall or
a personal firewall is blocking the connection. **Please use EC2
Instance Connect as described in the next lecture.**

**SSH does not work on Windows**

- If it says: SSH command not found, that means you have to use Putty

**here's a connection refused**

This means the instance is reachable, but no SSH utility is running on
the instance

- Try to restart the instance
- If it doesn't work, terminate the instance and create a new one. Make
sure you're using **Amazon Linux 2**

**Permission denied (publickey,gssapi-keyex,gssapi-with-mic)**

### This means either two things

- You are using the wrong security key or not using a security key.
Please look at your EC2 instance configuration to make sure you have
assigned the correct key to it
- You are using the wrong user. Make sure you have started an **Amazon
Linux 2 EC2 instance**, and make sure you're using the user
**EC2-user.** This is something you specify when doing
**EC2-user@**\<public-IP\> (ex: EC2-user@35.180.242.162) in your SSH
command or your Putty configuration

**I was able to connect yesterday, but today I can't**

This is probably because you have stopped your EC2 instance and then
started it again today. **When you do so, the public IP of your EC2
instance will change.** Therefore, in your command, or Putty
configuration, please make sure to edit and save the new public IP.

EC2 INSTANCE CONNECT: this allows us to do a browser base SSH session
into our EC2 instance, user is determined by default

Para usar EC2 instance connect es necesario tener abierto el puerto 22
de SSH para que corra el EC2

### EC2 instance roles demo

Amazon Linux AMI: imagen de sistema operativo Linux preparada por Amazon
web services para usar EC2

AMI= Amazon Machine Image

AWS IAM list-users

AWS configure, then especify a access id, a secret access key and a
region name, don't do that ever person who tries to connect using connect
can retrieve the values of this blanks, don't enter your IAM API key,
instead of that use IAM rules

We have to configure a role IAM, go to the console, then instances, the
EC2, actions, security and then modify IAM role, select de role and save

### EC2 purchasing options

On demand instances – short workload, predictable pricin, pay by second

- Reserved: for 1 and 3 yerar

- **Reverved instances** – long workloads
- **Convertible reserved instances:** long workloads with flexible
    instances, change instances over time

- Savings plans (1 and 3 years) commitment to an amount of usage, long
workload.

- Spot instances – short workloads, cheap, can lose instances(less
reliable)

- Dedicated hosts – book an entire physical server, control instance
placement

- Dedicated Instances – no other customers will share your hardware

- Capacity reservations – reserve capaity in a specific AZ for any
duration

### EC2 on demand

Linux or Windows: billing per second, after ther first minute

Other OS billing per hour

Has the highest cost but no upfront payment(pago adelantado)

No lorng-term commitment

Recommended for short-term and un-interrupted workloads, where you cant
predict how the application will behave

### EC2 reserved instances

- Up to 72% disconun t compared to on demand
- You reserve a specific instance attributes(instance type, Region,
Tenancy(como se comparte el hadware fisico entre clientes o
instancias), OS
- You specify a reservation period – 1 year + discount or 3 years
+++discount
- Payment options\_-no upfront+ (sin pago inicial), partial upfront++,
all upfront+++
- Reserved instance’s scope – regional o zonal. Reserve caácotu om am
AZ(availability zone)
- Recommended for steady-state- usage applicaitons (database)
- Convertible reserved instance can change the EC2 instance type,
instance family, os, scope and tenancy
- Up to 66%

### EC2 savings plans

discont based on long-term usage, up to 72%

Commit to a certain type of usage(10 per hour for i or 3 years)

Usage beyond EC2 savings plans is billed at the on demand price

Locked to a specific instance family and AWS region

Flexible across: image size, os, tenancy

### EC2 spot instances

Can get a discount fo up to 90& compared to ondemand

But they are instances that you can lose at any point of time because of
you previously pay you

It is the most cost-efficient instances in AWS

### Useful for workloads that are resilient to failure

- Batch jobs – trabajos por lotes
- Data analysis
- Image processing
- Any distributed workloads
- Workloads with a flexible start and end time

Not suitable for critical jobs or databases

### EC2 Dedicated Hosts

Aphysical server with EC2 instance capacity fully dedicated to your use

En el caso de uso donde tienes requisites de compliance\
o necesitas usar tus licencias de software existentes ligadas al
servidor,\
que tienen facturación basada por socket, por núcleo (core) o por
máquina virtual (VM).”

### Purcharsing options

- On-demand: pay per second for active dedicated host
- Reserved – 1 or 3 years

The most expensive option

Useful for software that have complicated licensing model, bring your
own license or for companies that have strong regulatory or compliance
needs

EC2 dedicated instances

- instances run on hardware thats dedicated to you

-may share hadware with other instances in same account

-no control over instance placement

EC2 capacity reservations

- Reserve on demand instances capacity capacity in a specific az for any
duration
- You always have access to EC2 capacity when you need it}
- You can cancel anytume, no billing discounts
- Combine with regional reserved instances and savings plans for
discounts
- You are charged at ondemand rate whether your run instances or not
- SUitable for short termn, uninterrupted workloadsw

### Types sumary

On-demand: pay for time , pay full price

Reserve: planing ahead if you plan is for long time

Savings plans: pay a certain amount per houyr for certain period and
stay in any instance

Spot instances: capacidad sobrante de AWS, hasta 90% menos en costes con
otras instancias, pero AWS puede interrumpirlas en cualquier momento

Dedicated host: book an entire hardware

Capacity reservation: book an instance for a period full price even you
don use or not

### Responsabilities EC2

AWS: hardaware, validation

Client: security groups, patches and updats OS, software and utilities
installed on the EC2 instance, IAM roles assigned to EC2 and IAM user
access managment, data security on your instance

### EBS (volumen)

Elastic block store, unidad de red, permiten que persistan los datos,
incluso después finalizacion, solo se puede mmontar una a la vez

Vinculados a una zona disponibiildad especifica

- Unidad de red: unidad física
- Utiliza red para comunicar instancia, latencia
- Separar instancia EC2 y conectar con otra
- Esta bloqueado en zona de disponibilidad
- Para transladar volumen primero hay que hacer un snapshot
- Tener capacidad provisionada en gbs o instrucciones por segunda
- Se factura por toda la capacidad provisionada, todas de espacio
solicitado
- Se puede aumentar capacidad con el tiempo
- EBS no adjunto, no depende de estar connectada a un EC2
- EBS borrar al terminar: controlar el comportamiento de EBS cuando una
instancia EC2 termina
- Se elimina el volumen EBS raíz
- Cualquier otro EBS no se elimina
- Eliminacion se puede controlar por AWS CLI

Snapshot/instantánea de EBS

Copia de seguridad del volumen y para mover EBS en zonas

No es necesario separar el volumen para hacer la instantea, pero se
recomienda

Puedes copiar las instantáneas a través de AZ o regios

### Archivo Snapshots de EBS

- Mover un snapshot a un nivel de archivo que es un 75 por ciento más
barato

- Restaurarcion de archivo tarde entre 24 y 72 horas

- Papelera de reciclaje:

- Configurar reglas de retencion de snapshots después de borrado
    accidental
- Se puede hacer entre 1 dia y 1 año

### AMI

- Amazon Machine Image

- Personalización de una instancia EC2 para enviarla más rápido: añades
software, configuración, sistema operativo.

- Tiempo de arranque más rápido de EC2

- La AMI se construye en región especifica y pueden copiarse entre
regiones

- Lanzamiento de instancias EC2 desde:

- AMI pública
- Propia AMI, la creas y la mantienes tu mismo
- AMI AWS market place, heco por otra persona

- Iniciar una instancia EC2 y personalizarla
- Detener la instancia
- Cosntruir AMI, creara instantáneas de EBS
- Lanzar instancias desde otras AMIs

### EC2 Image Builder

Automatizar la creacion, mantenimiento,, validacion y probra las amis de
EC2

Recurso gratuito

### EC2 Instance Store

-unidades de red de alto rendimiento

- son efimeros a los datos

-mejor rendimiento

-estos se pierden si los EC2 se detienen

-bueno para buffer, cache, memoria virtual, contenido temporal

-riesgo de pérdida de datos si el hardware fall

-copias de seguridad y replicación responsabilidad de usuario

- Alto rendimiento – EC2 instance Store

### EFS

- Elastic File System
- NFS network file system, sistema de arhivos de red
- Gestionado y que puede montarse en 100 EC2s
- Funciona con instancias EC2 linuz en multi-az
- Alta disponibilidad, escalable, caro 3xgps, pago por uso, sin
planificacion de capacidad
- MAs flexible y estar conectado

### EBS vs EFS

EBS necesita snapshot para pasarlo a otra disponibilidad haciendo
restauración

EFS tienen múltiples instancias en diferentes zonas de disponibilidad
con el **EFS mount target**

EFS Infrecuent Access (EFS-IA)

-clase de almacenamiento con costes optimizados, hasta **92 por ciento de
descuento**

**-**EFS moverá automáticamente tus archivos, basándose en la última
vez que se accedio a ellos a través de reglas o política del ciclo de
vida

-Transparecentes app que acceden a EFS

### Modelo de responsabilidad compartida para almacenamiento EC2

### Amazon

- Infraestructura
- Replicación de datos volúmenes EBS y unidades EFS
- Sustitución hardware defectuoso
- Empleados Amazon no puede acceder a datos

Clientes

- Configuración procedimientos de copia de seguridad instantánea
- Configuración encriptación
- Responsabilidad de los datos de las unidades
- Riesgo de utilizar EC2 instance store, es efímero

### Amazon FSx

- Lanzar sistemas de archivos de alto rendimiento de terceros en AWS
- Totalmente gestionado
- FSx para lustre
- FSx para Windows file server
- FSx para NetApp ONTAP

### Para Windows file server

- Sistema de archivos nativo de Windows totalmente gestionado
- Construido sobre Windows file server
- Soporta protocolo SMB y el protocolo de Windows NTFS
- Hacer una conexión con el centro de datos de la empresa,
bidireccional, con instancia EC2
- Microsoft Active Directory

### Para Lustre

- Almacenamiento de archivos gestionado, de alto rendimiento y escalable,
## High Performance Computing
- Lustre = Linux y cluster
- Machine learning, análisis, procesamiento video, modelado financiero

### ELB (Elastic Load Balancing) y ASG (Auto Scaling Groups)

- Escalabilidad: aplicación o sistema puede manejar mayores cargas
adaptándose a su funcionalidad.
- Escalabilidad vertical
- Escalabilidad horizontal (elasticidad)
- La escalabilidad está vinculada pero es diferente a la alta
disponibilidad

- Escalabilidad vertical: aumentar tamaño de una instancia, es muy común
para sistemas no distribuidos como una base de datos

- Hay un límite en cuanto se puede escalar verticalmente

- Escalabilidad horizontal: aumentar número de instancias sistemas para
la aplicación, implica sistemas distribuidos, ejemplo aplicación web
como EC2

- Alta disponibilidad: conectado con escalado horizontal

- Alta disponibilidad: significa ejecutar la aplicación al menos en dos
zonas de disponibilidad

- Objetivo de alta disponibilidad es sobrevivir a la pérdida de centro
de datos, desastre

- Escalabilidad en EC2:

- Vertical: aumentar tamaño de la instancia o hacia abajo

- Horizontal: aumentar número de instancias hacia fuera o hacia
### adentro

### - Servicios para esto

      - Auto Scaling Group
      - Load Balancer

- Alta disponibilidad: ejecutar instancias para la misma aplicación a
través de múltiples AZ

- Auto Scaling Group multi AZ
- Load Balancer multi AZ

### Escalabilidad vs elasticidad (vs agilidad)

- Escalabilidad: reforzando hardware: scale up or añadiendo nodos scale
out
- Elasticidad: una vez un sistema es escalable, habrá un cierto
### autoescalado para que el sistema pueda escalar en función de la carga
pago por uso, adecuación de la demanda, optimización de costes

### Agilidad

- It los recursos están a un solo click, de semanas a minutos

### Elastic Load Balancing (ELB)

- Los load balancer – equilibradores de carga – son servidores que
reenvían el tráfico de internet a múltiples servidores instancias EC2
en sentido descendente
- Balancear el tráfico de internet
- Distribuir la carga entre múltiples instancias
- Exponer un único punto de acceso DNS en tu aplicación
- Manejar fallos de las instancias descendentes
- Comprobaciones de estado de instancias
- Proporcionar terminación sll https para sitio web
- Alta disponibilidad entre zonas

### ELB

- AWS garantiza su funcionamiento

- Se encarga actualizaciones, mantenimiento, alta disponibilidad

- Solo pocos controles de configuración

- Se puede configurar un load balancer dentro de la instancia pero
requiere más esfuerzo, mantenimiento, integraciones

- Varios tipos:

- Application Load Balancer solo HTTP y HTTPS – capa 7
- Network Load Balancer – rendimiento ultra alto, permite TCP / UDP –
    capa 4
- Gateway Load Balancer – Capa 3 – envía a seguridad de
    terceros/FIREWALL
- Classic Load Balancer (retirado en 2023) capa 4 y 7

### Auto Scaling Group

- Objetivo

- Reducir o añadir instancias EC2 para adaptarse a un aumento de carga
- Aumentar o eliminar para que coincida con una disminución de la
    cargas
- Mínimos y máximos de máquinas
- Registrar automáticamente nuevas instancias en el Load Balancer
- Reemplazar las instancias en mal estado
- Solo se ejecuta a una capacidad óptima, ahorro de costes
- Tamaño mínimo, tamaño real-capacidad deseada, y tamaño máximo

### Estrategias de escaldado – Auto Scaling Groups

- Escalado manual: actualizar tamaño de un ASG manualmente

- Escalado dinámico: responde a cambios por demanda

- Escalado simple/pasos:

    - Cuando se activa una alarma de CloudWatch, aumento CPU más del 70%
      se añaden 2 unidades
    - CloudWatch, ejemplo –30 % entonces se elimina una instancia

- Escalado de objetivos

    - CPU se mantenga al 40 %, seguir el objetivo media 40 por ciento

- Escalado programado

    - Anticipar un escalado basado en patrones de uso conocido
    - Aumentar la capacidad mínima a una hora determinada
    -

- Escalado predictivo

    - Utiliza machine learning para predecir tráfico futuro, da el
      número de EC2 por adelantado

## Amazon S3

- Bloques de construcción de AWS

- Almacenamiento de escala infinita

- Muchos sitios web utilizan S3 como columna vertebral: contenido
estático, fiable y barato

- Servicios AWS utilizar S3 como un integración porque log, datos
análisis suelen almacenarse automáticamente en S3

- Casos de uso:

- Copias de seguridad almacenamiento
- Recuperación de desastres
- Archivado
- Almacenamiento cloud híbrido
- Alojamiento de aplicaciones: backend de almacenamiento
- Alojamiento de medios
- Data lakes y big data
- Entrega de software
- Sitio web estático

### Buckets

- Permite almacenar objetos – archivos en buckets o directorios

- Dos tipos:

- Uso general – tradicional S3
- Tipo directorio: optimizado para baja latencia

- Buckets pueden crearse en dos tipos de espacio de nombres:

- Espacio de nombre global:

    - Nombre bucket debe ser único globalmente, cuentas y regiones,
      único a nivel global
    - Nombre regional de la cuenta: es único dentro de tu cuenta y
      región
    - AWS añade un sufijo al nombre del bucket tiene prefijo y sufijo

- Se definen a nivel región

- Convención de nombres:

    - Sin mayúsculas
    - Sin guion bajo
    - 3 – 63 caracteres
    - No IP
    - Empezar por letra minúscula o número
    - No prefijo xn
    - No sufijo –s3alias

- Objetos (archivos):

- Tienen una clave que identifica el archivo dentro del bucket
- La clave es la ruta completa
- Clave, prefijo + nombre del objeto
- No hay directorios
- Máximo tamaño de objeto es de 50 TB
- Si se sube un objeto de más de 5 GB usar subida multiparte
- Metadatos: información útil(clave-valor de texto) datos del sistema
    o usuario
- Etiqueta: par clave-valor, hasta 10. Útil para seguridad, ciclo de
    vida
- Id versión, si está activado el versionado. Para recuperar versiones
    anteriores

### Seguridad en S3

- Basada en usuario: permisos a entidades

- Políticas IAM.
-

- Basada en recursos

- Políticas de bucket, desde la consola de S3 – permite cuentas
    cruzadas, incluso desde otras cuentas
- Listas control de acceso a objetos – nivel de detalle profundo puede
    desactivarse
- Lista control acceso de bucket

- Un usuario IAM puede acceder a un objeto

- Los permisos IAM lo permiten
- La política de recursos lo permite
- No hay denegación explícita

Cifrado se hace automáticamente

### Políticas de bucket S3

- Basadas en JSON.
- Resource: a que recursos aplica la política, puede ser bucket u
objetos
- Effect: permitir o denegar política
- Action: conjunto de API para leer o escribir objetos
- Principal: la cuenta o usuario al que aplicar la política

### Utilizar política de bucket S3 es para

- Conceder acceso público al bucket
- Forzar que los objetos se cifren al subirlos (pregunta de examen)
- Conceder acceso a otra cuenta, cuenta cruzada

Bloquear acceso público

### Amazon S3 – alojamiento de sitios web estáticos

- S3 puede alojar sitios web estáticos y hacerlos accesibles en internet

- La URL del sitio web será dependiendo de la región
- Si recibes 403 forbidden, asegurarse política del bucket permite
lecturas públicas

### Versionado de S3

- Cada vez que se haga un cambio se genera una versión
- Protege contra borrados no contemplados
- Rolling fácil a la versión anterior
- Cualquier archivo que no esté versionado antes de activar el
versionado tendrá la versión nula
- Suspender el versionado no elimina las versiones anteriores

### S3 – replicación

- Replicación CRR y SRR

- Activar el versionado en los buckets de origen y destino

- Replicación entre regiones
- Replicaciones en la misma región
- Pueden estar en las diferentes cuentas AWS
- La copia es asíncrona
- Debes dar permisos IAM adecuados a S3

### Casos de uso

- CRR: normativa, acceso de menor latencia, replicación entre cuentas
- SRR: agragacuib de kigsm reokucacuib eb vuvi ebtre cyebtas de
oridyccuib t de test

### Clases de almacenamiento S3

- S3 Standard – uso general : datos constantes y se necesita velocidad
- S3 Express One Zone: baja latencia pero sacrificando redundancia,
porque solo está en una zona de disponibilidad para obtener datos muy
rápido
- S3 Standard –infrequent-access IA : más baratas para datos que se
acceden poco
- S3 One Zone – infrequent access: más barata que IA pero en una sola
zona, más riesgo
- S3 Glacier instant retrieval: datos que casi no se usa pero que se
quieren recuperar rápido
- S3 Glacier Flexible Retrieval: aceptamos tiempos de espera para
recuperar por un coste menor
- S3 Glacier Deep Archive: más barata, para almacenar datos por largos
periodos sin necesidad de acceso frecuente
- S3 intelligent tiering: automatiza los datos entre diferentes clases.
- Comose pasan los datos de una clase a otra? Se puede manual pero lo
mejor es con el ciclo de vida de S3, se definie cada cuanto se mueven
los datos

### Durabilidad y disponibilidad en S3

- Durabilidad: alta durabilidad de los objetos por estar en múltiples AZ

- Durabilidad es igual para todas las clases
-

- Disponibilidad:

- Disponibilidad del servicio
- Varia en función de la clase

### Standard S3

- Disponibilidad 99.99%
- Datos de acceso frecuente
- Baja latencia y alto rendiminto
- Soporta 2 fallo concurrente de la instalación
- Análisis big data, app móviles, juegos,

S3 Ingrequent Access

- Coste inferior a standar

- S3-IA:

- DISPONIBILIDAD 99.9 %

- recuperación desastres, copias de seguridad

- S3 One Zone- Ingrecuenta Access

- Alta durabilidad 99.99999, en una AZ, los datos se puerden cuando
se destruye la AZ

- Desonibilidad 99,5

- alamcenmianeto copias de seguridad locales

- S3 Glacier:

- Almacenamiento bajo coste pensado para archivar, hacer copias de
seguridad

- precio: precio de almacenamiento + coste de recuperación del
objeto.

- S3 glacier instant retrieval: recuperación en retrieval, duración
mínima 90 días

-S3 Glacier Flexible Retrieval: accelerada de uno a 5 minutos,
estándar de 3 a 5 horas y masiva de 5 a 12 horas – gratis. Duración
mínimo 90 días

-S3 Glacier Deep Archive: estándar 12 horas, masiva 48 horas. Duración
mínima de almacenamiento 180 días

- S3 Intelligent –Tiering:

-pequeña cuota mensual de monitorización y jerarquización automática

- mueve objetos automáticamente entre los niveles de acceso en
función de acceso

- no har cargos por recuperación

- Frequent Access tier- automático: nivel por defecto
- Infrequent access tier – automtico: objetos accedidos durante 30 días
- Archive instant access tier – auto : objetos no accedidos durante 90
días
- Archive Access tier – optional : configurable de 90 a más de 700 días
- Deep archive Access tier – optional: configurable 180 días a 700 días

Precios de recuperación por cada mill solicitudes

### S3 Express One Zone

- Clase de almacenamiento de alto rendimiento, maxima velocidad
- SE alamcenan en un Directory Buckeet, ubicado en una sola zona
- 100.000 solicitudes por segundo con latencia de milisegundos ede un
solo digito
- 10 mejor rendimiento que un S3 Standard, 50 % mayor coste
- Alta durabilidad y alta disponibilidad 99.95
- Coloca tu almacenamiento y los recursos de computo en la misma az,
esto reduce la latencia
- Aplicaciones sensibles a la latancia, entrenamiento de IA, modelado
financiero
- SageMaker Model Training, Athena , EMR, GLue

### Cifrado S3

- AWS hace cifrado por el servidor, este lo cifra después de recibirlo
- Cifrado también puede ser realizado por el cliente, antes de subirlo
- Por defecto hoy en dia se cifra la info

### IAM Access Analyzer para S3

- Garantiza solo personas autorizadas pueden acceder a bucket
automáticamente, quien puede acceder y detectar accesos no deseados
- Se identifica datos expuestos
- Evalúa políticas de buckets de S3, ACL de S3 y políticas de S3 Access
Point
- Funciona con el respaldo de IAM Access Analyzer
- Análisis de políticas para accesos interno y externos

### Modelo responsabilidad compartida S#

### AWS

- Infraestructura, seguridad global, durabilidad, sostener la perdidad,
- Análisis de configuración y vulnerabilidad
- Validacion de la normativa

### Cliente

- Versionado de S3
- Políticas bucket S3
- Configuracion de la replicación de S3
- Logs y monitorización
- Clases de almacenamiento de S3
- Encriptacion de datos en reposo y transite

### Familia AWS Snow

- Dispositivos portatiles de alta seguridad para recopilar, procesar
### datos y migrar hacia y desde AWS

- Migracion de datos:

- Snowcone
- Snowball Edge
- Snowmobile

- Edge computing, computacon cerda de los datos

- Snowcone
- Snowball edge

- Desafios:

- Conectividad limitada
- Ancho de banda limitado
- Alto coste de la red
- Ancho de banda compartido
- Estabilidad de la conexión

Si la transferencia de datos tarda más de una semana, usar dispositivos
snowball

### Snowball Edge

- Transferencia de dsatos: transporte fisico de datos dentro y fuera de
Amazon
- Alternativa para mover datos en red
- Trabajo por transferencia de datos
- Alamcenamiento de bloques y almacenamiento de objetos con S3
- Almacenamiento optimizados de 80 TB en HDD
- Computacion optimizada 43 TB hh o 28 TB NVMe para bloques scon se
- Casos de uso: migraciones cloud o desastres
- Agente data sync preintalado

### AWS snowcone

- Pequeño y portatil ,robusto
- Ligero
- Computacion borde, almacenmineto y tranferencia de datos
- Snownoe 8tb hdd
- Snowcone ssd 14 TB de alamenimainto sdd

### AWS Snowmobile

- Transfiere exabytes de datos = 1EB = 100 PB = 1000000 TBS
- Cada snowmobile tien \|00 pb de capacidad
- Alata seguridad, temperatura controlada, gps, videovigilancia

### PAso para usar

- solicita dispositivo
- Instala cliente snowball AWS opshub

**Edge Computing:** procesar datos mientras se crean en una edge
location, se pueden configurar snowball edge, snwcone: preprocesamiento
de datos, machine learning,, se puede devolver el dispositivo

Snowcone y SSD: 2cpu, 4 gb memroias, acceso a cable o inalabrinco

Alimentacion usb

### **Snowball edge** – computación optimizada

104 cpus 419 gib ram

GPU opciones

Alamcemanieminto utilizable de 28 TB nvmw o 42 de hdd

Cluster de almacenamiento

### Snowball edge – almacenamiento optimizado

Hasta 40 Vcpu, 80 gib de ram, 80 TB alamecenmiento

Todos puede ejecutar instancias EC2 y funciones Lambda

Se puede usar AWS opshub para administrar tu dispiositivo de la familia
snow: se puede desbloquear y configurar dispositios indifiduales o en
cluster, transferir archivos, lanzar y administrar instancias,
supervisar métricas del dispositivos, almacenamiento capacidad,
instancias activas y lanzar servicios AWS compatibles en tus
disositiviosas

### Precios de AWS snowball edge

- Pago por uso del dispositivo y por transferencia de datos de salida
desde AWS

- Transferencia de datos entrada S3 no cuesta

- BAjo demanda:

- Tarifa unica por trabajo, 10 días uso snowball edge storage
    optimizaed 80 TB
- 15 días uso snowball edge storeaz optimizaed 210 TB
- Dias de envio no cuentas
- Se paga por cada dia extra
-

- Compromiso por adelantado

- Pagas por adelantado por suo mensual 1 a 3 años
- 62 % descuento

### Vision General Storage Gateway - Cloud híbrido para el almacenmiento

- Parte infraestructura reside en cloud o otra en instalaciones de
### cliente

- Esto por largas migraciones a el cloud

- Requisites seguridad

- Requisites normativa

- Estrategias de it

- S3 tecnología almacenamiento propia, a diferencia de EFS y NFS

- ¿Como se expone los datos de S3 en las instalaciones:

    - AWS Storage Gateway

### Opciones nativas del cloud de almacenamiento de AWS

### Bloque

- Bloque:

- EBS
- EC2 instance store

- Fichero

- EFS

- Objeto

- Amazon S3
- Glacier

### AWS Storage Gateway

- Puente entre los datos locales en instalaciones y lo de cloud en S3

- Servicio de alamceminaito híbrido

- Casos de uso: recuperación de desastres, copias de seguridad,
almacenamiento por niveles

- Tipos de Gateway de almacenamiento:

- File Gateway
- Volume Gateway
- Tape Gateway

## Bases De Datos AWS

- Almacenamiento de datos en disco puede tener sus limites
- A veces quieres alamecenar data en base de datos
- Puedes estructurar los datos
- Construyes indices para consultas
- Puedes definir relaciones entre tus conjuntos de datos
- Están optimizadas para un propósito

### Bases de datos relacionales

- Tiene el mismo aspecto de hojas de cálculo excel con enlaces entre
ellas
- SQL para consultas

### Bases de datos NoSQL

- Creadas para modelos de datos específico y tienen esquemas flexibles
para construir aplicaiones modernas

- Ventajas:

- Flexibilidad, fácil evolutiva
- Escalabilidad: cluster distribuidos
- Alto rendimiento: optimizado modelo datos específico
- Alta funcionalidad: tipos optimizados para el modelo de datos

### Ejemplos

- Bases de datos clave-valor

- Documento.

- Grafico

- En memoria

- De busqueda

- JSON:

- Encaja modelo no relacional
- Datos pueden estar anidados
- Campos pueden cambiar con el tiempo
- Soporte nuevos tipos arrays, etc

### Bases de datos y responsabildiad compartida

- AWS ofrese el uso de gestionar diferentes bases de datos.

- Beneficios:

- Aprovisionamiento rápido, alta disponibilidad, escalado vertical y
    horizaontal
- Copia de seguridad y restauración automatizadas, operaciones y
    actualizaciones
- Parcheo sistema operatio
- Moniotorizacoin, alertas
- SE podría gestionar bases de datos en EC2 pero las copias de
    seguridad, parches y alta disponibilidad, tolerancia a fallos las
    gestiona el cliente
-

### Amazon RDS

- RDS: Servicio de Base de Datos RElacional

- Utiliza SQL

- Crea bases de datos gestionadas por AWS, configura todo

- Postgres
- Mysqul
- Mariadb
- Oracle
- SQL SERVEr microsoft
- Imb DB2
- Aurora de AWS

PErmite centrar en la logica y consulta de datos

### Ventajas RDS frente al despliegue del BD en EC2

- RDS es un servicio gestionado:

- Aprovisionamiento automatizado, parcheo del so
- Copias de seguridad continuas, restauración da una fecha
    determinada, point in time restore
- Dashboards de monitorización
- Replicas de lectura
- Configurar mult AZ para DR disaster recovery
- Ventana de mantenimieot para actualizaciones
- Capacidad de escalado, vertical y horizontal
- Alamcenamineto respaldado por EBS

- No se puede acceder por RDS SSH a tus instancias porque AWS abstrae
completamente la infraestructura

### Arquitectura RDS

Elastic Load Balancer ---- Instancias EC2 -------- SQL Amazon RDS

Instancias EC2, logica de negocio

RDS backed de datos centralizado y no se conecta directamente por
internet, sino se conecta de forma privada. Es fundamental entender
que no se exponsa la base de datos

### Amazon Aurora

- Base de datos, no es de open source
- Acepta tanto posgressql como MySQL
- Esta optimizada para AWS y mejora el rendimiento de MySQL en RDS y más
de 3 veses el rendimiento de postgres en RDS
- Tiene un precio más elevado que otros servicios
- El almacenamiento crece automáticamente en incrementos de 10 gb,
bloques, hasta 256 TB
- Aurora cuesta RDS un 20 por ciento pero es más eficiente
- No está a nivel gratuito pero las cuentas nuevas pueben probarlo
usando créditos

Amazon Aurora Serverless

- Creacion automática de la bases de datos con escalado dinamindco en
función de la demanda
- Postgres y MySQL son compatibles
- No se necesita planificacion de capacidad. Esto es fundamental para
escenarios impredecibles
- El pago es por segundo, podria ser más rentable
- Cargas de trabajo infrecuentes, intermitentes o impredecibles
- Elimina la gestion de servidores por el usuario
- La aplicación no se conecta a la base de datos sino a la capa de
proxies, como intermediario, permite que AWS cambie la
infraestructura sin afectar la aplicación: aumenta o disminuye
recursos. Alamacenmiento está separado pero es compartido

### Opciones de despliegue de RDS

- Replicas de lectura

- Escalada de carga de trabajo de lectura de la BD con está replica
- Se pueden crear hasta 15 replicas de lectura
- Los datos solo se escriben en la base de datos principal
- Replias de lectura para escalar información

- Multi AZ

- Recuperación en caso de caída de la AZ alta disponibilidad
- SE puede tener una replicación cruzada AZ para tener una base de
    datos en caso de recuperación de desastres, estara en otra zona de
    disponibilidad en la misma región
- Sol ose puede tener otra AZ compo conmutacion por error

### Despliegues de RDS: multiregion

- Replicas de lectura en varias en regiones
- Bajar la latencia al tener la base de datos en varias regiones
- Rendimiento local para lecturas globales
- Coste de replicación

### ElastiCache

- Servicio de base de datos

- Es para conseguir Redis o Memcached gestionados

- Caches: bases de datos en memoria de alto rendimiento y baja latencia

- Reducir carga de BD en lecturas intensivas

- AWS se encarga de mantenimiento parche del sistema operativo,
optimizaciones, instalación, configuración, supervisión, recuperación
de fallos y copias de seguridad

- Arquitectura de ElastiCache –cache:

- ELB – EC2 /grupo de autoescalado – leer/escribir - Amazon RDS SQL –
    ElastiCache base de datos en memoria

### DynamoDB

- Totalmente gestionado con replicación 3 AZ
- No relacional
- Escala de trabajos masiva , distribuida sin servidor
- Millones de peticiones por segundo, trillones por fila, cientos de TB
de almacenamiento
- Rendimiento rápido y constante
- Latencia de milisegundo
- Integrada con IAM para seguridad, autorización y administración
- Bajo coste y autoescalado
- Tabla de acceso estándar e infrecuente IA
-

### Dynamo –tipos de datos

- Clavo/valor - atributos

### DynamoDB Accelerator - DAX

- Cache en memoria está gestionada en DynamoDB
- Mejorar el rendimiento x10 – milisengo a microsenduo
- Seguridad, alta escalabilidad y alta disponibilidad
- DAX solo se utiliza con DynamoDB, en cambio ElastiCache puede usarse
con toras basesd de datos

### Tablas globales DynamoDB

- Se puede reducir la latencia para varias regioines usando tablas
globales
- Replicación biderencional
- Replicación es activa – activa –lecutra y escritura en cualquier
región en AWS

### Redshift

- Servicio de base de datos, se basa en posgreSQL pero no utiliza OLTP
ONLINE TRANSACTION PROCCESING, pequeñas operacoin por segundo, sino
OLAP, procesamiento analitico en línea, carga los datos cada hora, no
cada segundo
- Rendimiento 10 veces superior a otros almacenes de datos, escala a pbs
de datos
- Almacemiento de datos en columnas en lugar de filas
- Ejecucion de consultas en paralelo masivo MPP
- Pago en función instancias aprovisionadas
- Tiene interfaz sql
- Herramientas de BI business intelligence(convertir datos en
representaciones visuales), como QuickSight o Tableau se ingregran con
ella
-

EMR – Elastic MApReduce

- Cluster Hadoop, big data para analizar py procesar datos

- Clusters puden estar formados por cientos de EC2
- Compatible con apache spark hbase presto flink
- EmR se encarga arpovisionamiento y la configuracoin
- Autoescalado e integrado con instancias Spot
- Uso: procesamiento, machine learnhing, **cluster, big data**

### Ahtena

- Servicio de consultar sin servidor para analizar datos alamcenados en
Amazon S3
- Athena consulta y análisis, se puede extraer informar y dashboards a
través de quicksight
- Lenguaje SQL estándar para consultar archivos
- Admite CSV, JSON, ORC, AVRO Y PARQUET
- Utiliza datos comprimidos o en columnas para ahorrar costes
- Uso: inteligencia empresarial, análisis informes, analizar y consultar
logs de flujo de VPC, logs de ELB, rastros de CLOUD TRAIL
- Precio: 5 dólares por TB de datos analizados
- EXAMEN: analiza los datos en S3 usando SQL soin servidor: Athena

### QuickSight

- Servicios de inteligencia empresarial impulsado por machine learning
sin servidor para crear dashboards interactivos

- Rapido, escalable auto, integrable, con precios por sesion

- Uso:

- Análisis empresarial
- Construir visualizaciones
- Análisis Ad-hoc
- Obten informacion empresarila con los datos
- Intregracion con RDS, aurora, redshift, S3

### DocumentDB

- Aurora fue la implementacion AWS de postgreSQL y MySQL
- DocumentDB es lo mismo que MongoDB
- Conultar, alamcerna e inderxar datos en JSON
- Conceptos despliegue similiares en Aurora
- Gestionado, alta disponibilidad con replicación en 3 AZ
- Almacenamiento crece automáticamente en incrementos de 10 gh hasta
128 TB
- Escala automáticamente peticiones con millónnes de peticiones por
segundo
- BASE DE DATOS NO SQL: DYNAMO DB COMO MONGO DB

### Neptune

- Base de datos grafica totalmente gestionada
- Conjunto de datos de grafos: ejemplo red social
- Alta disponibilidad en 3 ZA con 16 replicas lectura, sin embargo,
siempre se escribe en la base de datos principal
- Construye aplicaciones que trabajan con conjuntos de datos altamente
conectados y optimizados
- Almacenar miles de millónnes de relacionas y consultar el grafico
- Replicas múltiples AZs
- Buena para grafo de conocimiento wikipedio y deteccion de fraudes,
motores de recomendacion, redes sociales

### QLDB

- Base de datos
- Significa: Quantum Ledger Database, base de datos de libros contables
- Libro de contabilidad es un libro que registra transacciones
financieras
- Totalmente gestionada, sin servidor, alta disponibilidad, con
replicación 3 AZ
- Revisar historial de los cambios realizados en los datos
- Sistema inmutable, nada puede ser elimando o modificado, verficicable
criptobgraficamente
- Mejor 2 o 3 veces que blocahin de libro mayor común
- Diferencia con Amazon Managed BlockChain: **no hay componentes de
descentralizacion, de acuerdo con regulacion financiera**

### TimeStream

- Servicio BD para trabajar con datos de series temporales, datos que
llegan constantemente con marca de tiempo: log, métricas de sistema
- Es serverless
- Es gestionado
- Escalado auto hacia arriba o abajo
- Permite almacenar y analizar billones de eventos por dia
- Hasta 1000 veces más rápida y a 1/1’0 del coste de la base de datos
relacionales
- Incluye funciones integradas análisis de series temporales, para
identificar patrones en tiempo real
-

### Managed BlockChain

- BlockCahin permite crear aplicaciones en las que varias partes pueden
ejecutar transacciones sin necesidad de una autoridad central de
confianza
- Envío de usuario a usuario – peer to peer
- Es un servicio para unirse a redes publicas de blockchain
- O crear una red propia privada y escalable
- Comptatible con hyperledger fabric y etherreum

### Glue

- Servicio de extraccion, transformacion y carga **ETL**
- Útil para preparar, y transformar datos para la analitica
- Sin servidor
- Se accede de S3 bucket o RDS, se extrae y se transforma y se carga a
Redshift
- Glue Data Catalog: repositorio central para almacenar metadatos
estructurales y operativos de todos tus activos de datos

### DMS – Migration Service

- Servicio para migracion de datos

- Migración rápida y segura con capacidad de recuperación y
autocuracion

- La base de datos de origen sigue disponible durante la migracion

- Soporta:

- Migraciones homogeneas: oracle a oracle
- Migraciones heterogeneas: SQL server a aurora

### Otros servicios de computacion

### Docker

- Plataforma de desarrollo de software para desplegar aplicaciones

- App se empaquetan en contenedores que se ejecutan en cualquier sistema
operativo

- Empaquetar el software en contenedores para que funcione en cualquier
entorno

- Funciona:

- Cualquier maquina

- No hay problemas de compatibilidad

- El comportamiento es predecible

- Representa menos trabajo

- Es fácil de mantener y desplegar

- Funciona con cualquier lenguaje, sistema operativo o tecnología

- Se puede ampliar o reducir los contenedores muy rapidamente, puede
    ser monolitica (ejecutarse en un único contendor), o tener
    microservicios

- Alamcenamiento imágenes de docker:

    - Repositorio de docker

### - Publico Como Docker hub

      - Imagenes para muchas tecnologías o sistemas operativos

    - Privado: Amazon ECR Elastic Container Registry

### Docker vs máquinas virtuales

- Es una virtualizacion pero los recursos se comparten con el anfitrion,
es decir que muchos contenedores pueden haber en un servidor

- Maquinas virtuales:

- Insfraestructure – host OS – hypervisro – virtual machine (muchas) -
    apps
-

- Docker:

- Infraestructure – host OS EC2 instance – docker daemon - container

### ECS (servicio para contenedores de docker)

- Elastic Container Service
- Lanzar contenedores Docker en AWS
- Debes aprovisionar y mantener infraesctructura EC2
- AWS incia y detiene los contenedores
- Tiene integracioners con el Application Load Balancer

### Fargate

- Permite lanzar contenedores docker en AWS
- Cliente no aprovisiona la infrraestructura, no hay instancias EC2 que
gestionar
- Oferta serverless
- AWS ejecuta los contenedores por ti en función de la CPU RAM que
necesites

### ECR

- Elastic Container Registry
- Registro privado de Docker en AWS
- Alamcenar imágenes cliente para que puedan ser ejecutadas por ECS o
Fargate

### EKS

- Elastic Kubernetes Service
- Permite lanzar clústeres de kubernetes administrados por AWS
- Kubernetes es un sistema de código abierto para la administración,
despliegue y escalado de aplicaciones en contenedores
- Kubernetes es una plataforma de código abierto
- En vez de lanzar contenedores de forma manual es organizar todo en un
cluster en donde se distribuyen y ejecutan las apps
- Los contenedores de kubernetes que se despliegan se agrupan en
unidades mínimas o pods, unidad mínima de ejecución, también pueden
llamarse contendores que se alojan en EC2 o pueden lanzanrse en
fargate serverless
- Kubernetes is agnóstico a la nube, puede usarse en cualquier nube, o
en las oficinas

Docker crea contenedores.

Kubernetes los organiza y administra.

### Concepto Serverless

- Nuevo paradigma en el que desarrolladores ya no gestionan servidores,
solo despliegan código, despliegan funciones

- Serverless era igual a Funcion como Servicio

- Serverless fue pionero por Lambda, ahora también incluye todo lo que se
gestiona base de datos, mensajeria, alameceniamiento, etc

- Significa que no los gestionas, aprovisionas o ves

- Ejemplos

- S3
- DynamoDB
- Fargate
- Lambda

### Lambda

- Serverless

- Funciones virtuales

- Limitado por el tiempo. Ejecuciones cortas

- Ejecucion bajo demanda

- Escalado es automatizado

- Beneficios:

- Paga por solicitud y tiempo de computacion
- Capa gratuita de uno millóns solicitudes y 400 mill gb teimpo
    computacion
- Intergrado conjunto de servicios AWS
- Dirigdo por eventos: funciones son invocadas por AWS cuando se
    necesitan
- Integrado con muchos lenguajes de programación
- Fácil monitorización con CloudWatch
- Fácil obtener recursos por funciones, hasta 10 gb pde ram

### Soporte de lenguaje Lambda

- Node

- Python

- Java

- C#

- Golang

- C#

- Ruby

- Api tiempo ejecución personalizado, rust

- Imagen contendor Lambda:

- Se prefiere ECS o fargate para imágenes docker arbirarias
- Debe implementar la API de tiempo de ejecución Lambda

### Precios de Lambda

### Pago por llamadas

- Primer millónn de solicitudes gratis
- 0.20 dólares por cada millón de solicitudes
-

### Pago por duracion

- Incrementos de un milisegundos
- 400 milll gb seundos tde timpo de cálculo mes gratis

Despues 1 dolar por 600 mil gb segundos

### Amazon API Gateway

- Construir una API serverless
- Proxy requests
- SErvigio totalmente gestionado, para crear publicar, mantener,
supervisar y asegurar las API
- Serverless y escalable
- Soporta apis restful y apis web socket
- Soporta seguridad, autenticación usuario, claves API y monitorización

### Batch

- Procesamiento por lotes
- Ejecuta eficientemente 100 mil trabajos por computacion por lotes
- Trabajo por lotes = inicio y un final, diferente a uno continuo
- Lanza dinamincamente instancias EC2 o spot instances
- Proporciona la cantidad adecuada de computacion memoria
- Tu envias o programas los trabajos por lotes y Batch se encarga del
resto
- Lo trabajos por lotes se definen como imágenes Docker y se ejecutan
ECS
- Útil para optimizar costes y centrarse menos infraestructura
- Batch: inicio/trigger y luego insert(objeto procesado)

### Batch vs Lambda

- Lambda:

- Limite de tiempo
- Tiempos de ejecución limitados
- Espacio de disco temporal limitado
- Serverless
-

- Por lotes:

- Sin limite de tiempo
- Cualquier tiempo de ejecución siempre que este empaquetado como
    imagen docker
- Depende de EBS y almacen de instancias para el espacio en disco
- Depende de EC2. Es decir que puede ser gestionado por AWS si se
    desea

### Lightsail

- Sirve para servidores virtuales, almacenamiento, bases de datos y
redes

- Precios bajos y predecibles

- Alternativa más sencilla a EC2 RDS ELB EBS

- Para personas con poca experiencia en cloud

- Configurar notificación y nonitorizacion de tus recursos

- Usos:

- Aplicaciones web sencillas
- Sitio web, plantilla wordpress
- Entorno de desarrollo y testeo
- Alta dispnibiildad , integraciones limitadas con AWS

## Despliegue Y Gestion De La Infraestructura A Escala

### CloudFormation

- Forma declarativa de definir infraestructura de AWS
- Describir lo que se quiere en una plantilla
- Luego se puede desplegar en forma de infraestructura
- CloudFormation lo crea por los clientes en orden correcto y la
configuración exacta

### Ventajas de CloudFormation

- Infraestructura como código: no se crean recursos manualmente, todo
está definido en archivos que se pueden versionar o revisar a través
de código

- Coste no tiene asociado, el coste son los recursos

- El stack tiene un id y se puede ver cuento cuesta esa pila

- Puede estimar costes utilizando la plantilla de CloudFormation

- Estrategia de ahorro, se puede atuormatizar las plantilla en ciertos
horarios o fehcas

- Productividad:

- Destruir y volver a crear infraestrecutra en el cloud en marcha
- Gerancion automatizada de diagramas para las plantilla
- Programación declarativa, en forma de código y no es necesario
    averiguar el orden y la orquestacion
- Se puede usar plantillas existentes
- Aprovechar documentacion
- Soporta casi todos lo recursos de AWS
- Se pueden utilzar recursos personalizados para lo que no sea
    compatible

### CloudFormation + infraestructure composer

- Con la suma de estos el IC permite de forma visual ver todos los
recurso sy relaciones entre componentes

- En base al idagrama se crea la plantilla en CloudFormation

### CDK

- Cloud Development KIt
- Servicio para definir una infraestructura de cloud con un lenguaje
conocido:Java, Python. Se pueden programar ficheros para programar
infraestructura
- Codigo se compila en una platina de CF
- Toda la infraestructrau se puede desdplegar en un solo lenguaje
- Funcione muy bien para funciones Lambda
- Funciona para contenedores docker eCS o EKS

### Elastic Beanstalk

- Una Arquitectura típica: web app de 3 niveles. La mayoría de las
aplicaciones web tiene la misma arquitectura: ALB + ASG: aplication
load balancer para gestionar carga de trabajo y grupos de auto
escalado. Hay que gestionar y configurar cosas pero esto se puede
solventar con **Elastic Beanstalk**
- Elastick Beanstalk es una vision centrada en el desarrollador de la
implementacion de un app
- Utiliza todos los componentes pero todo está en una vista y fácil de
entender, control total sobre configuración
- Plataforma como servicio (PaaS)
- Gratuito pero pagas por las instancias

### Elastic Beanstalk

- Servicio gestionado, elementos gestionado por AWS
- Instancia y SO, estrategia de despliegue es configurable pero lo hace
EBS

- Aprovisionamiento de capacidad
- Equilibrio de carga y autoescalado
- Supervisión del estado de la aplicación y capacidad de respuesta
- Solo el config app es responsabilidad del desarrollador

### Tres modelo architectura

- Despliegue instancia unica
- LB + ASG para app web de producción o preproducción
- ASG app no web en producción

- Soporte muchas plataformas, go Java se tomcat,etc, constructor
paquetes, docker solo contendor, multicontendor, preconfig

- Puedes escribir tu plataforma personalizada

- Permite la monitorización de la salud:

- Envios de salud a CloudWatch, comprueba la salud
- Dashboard, panel de control
- Plataforma como servicio EXAMEN

### CodeDeploy

- Desplegar aplicaciones de forma automática
- Gestion de instancias como cambiar de versiones, actualizacion EC2 a
versiones
- Funciona para servidores locales: estos también pueden usar CodeDeploy
- SErvicio híbrido, instalaciones locales como los de AWS
- Servidores o instancias deben ser aprovisionados y configurados antes
con el agente CodeDeploy
- EXAMEN: desplegar aplicación forma automática es CodeDeploy

### CodeCommit

- Antes de enviar código de la aplicación a servers, en necesario
almacenar en algun lugar

- Repositorio de código y tener un control de versiones, se hace usando
tecnología Git, el producto competidor de AWS es codecommit

- Servicio de control de fuentes que aloja repositorio que se basan en
git

- Facilita la colaboración con otros en el código

- Cambios en el código se versionan de forma auto

- Ventajas:

- Gestionado
- Escalable, alta disponibilidad
- Privado, seguro e integrado con AWS
- Examen: sistema de repositerios CodeCommit

### CodeBuild

- Servicio construcción de código

- Compila, ejecuta pruebas y produce paquetes para ser desplegados

- CodeCommit – recupera el código- CodeBuild – construye el código
–artefacto listo para desplegar

- Ventajas:

- Gestionado,
- Sin servidor
- Escalable y disponible
- Seguro
- Precio de pago por uso, solo pagas tiempo compilacion

### CodePipeline

- Orquestar pasos para que el código sea empujado auto a producción

- Codigo – construir – probar – aprovisionar – desplega (Lo que hace
este servicio)

- Base de integración continua y entrega continua CICD

- Ventajas:

- Gestionado

- Compatible con:

    - CodeCommit
    - Codebuild
    - Codedeploy
    - Elastic Beanstalk
    - CloudFormation
    - Git Hub
    - Servicios terceros
    - Plugins personalizados

- Entrega rápida y actualizaciones rapidas

- Codepipeline orquesta: codecommit – codebuild – CodeDeploy – elastic
    beanstalk

- Orquestar: codepipeline

### CodeArtifact

- Paquetes de software dependen unos de otros para ser construidos,
**dependencias de código** y se crean otros nuevos
- **Almacenar y recuperar estas dependencia se llama gestion de
artefactos**
- **Servicio para gestion de artefactos segura, escalable y rentable**
- **Funciona con herramientas de gestion de dependencias como Maven,
Gradle, npm, yarn, twine, pip, NuGet**
- CodeBuild y desarrolladores pueden recuperar dependencias desdes
codeartifact
- Examen: servicio de gestion de artefactos es CodeArtifact

- - CodeCommit
    - Codebuild
    - Codedeploy
    - Elastic Beanstalk
    - CloudFormation
    - Git Hub
    - Servicios terceros
    - Plugins personalizados

### Systems Manager

- Servicio para gestionar sistemas EC2 y on premises a escala

- Hibrido

- Obtener Informacion operativa sobre el estado de la infraestructura

- Conjunto de más de 10 productos

- Caracteristicas:

- Auto parches mejorar la normativa
- Ejecuta commando en toda una flota de servidores
- Almacenar config parametros con SSM
- Funciona para Linux, Windows, MAcos , raspberryy ppios

- Como funciona:

- Agente SSM para controlar los sistemas

- Se instala por defecto en las AMI de Amazon Linux y en algunas AMI
    de ubuntu

- Agente hace la gestion en EC2 como en virtual machines en las
    instalaciones

- Gracias agente

    - Ejecutar commandos
    - Parchear
    - Configurar servidores

### SSM Session Manager

- Permite iniciar un shell seguro en servidores EC2 y locales
- No necesita acceso SSH ni claves SSH
- No necesita puerto 22
- Se necesitan permisos IAM
- Los log se puede enviar a un bucket de S3 o hacia CloudWatch

### System Manager Parameter Store

- Servicio para almacenar de forma segura config y secretos como:

- Api
- Contraseñas
- Configuraciones

- Serverless

- Escalable

- Duradero

- Y con SDK fácil de usar

- Controla los permisos de acceso mediante IAM

- Versionado y cifrado opcional **AWS KMS**

## **Infraestructura Global De AWS:**

- Aplicacion global es una aplicación en múltiples geografias:

- PUEDE SER REGIONES O EDGE LOCATIONS

- Disminicio de latencia:

- Latencia: tiempo que tarde un paquete de red en llegar a un servidor

- Recuperarcion de desastres (Disaster Recovery DR)

- Computar por error a otra región y que siga funicionando la app

- Proteccion contra ataques

- Aplicaciones:

- DNS glbal: Route 53:

    - Encaminar al despliegue más cercano con la menor latencia
    - Estrategias de recuperación de desastres

- Red global de entrega de contenidos (CDN) CloudFront:

    - Replica parte aplicación a las ubicaciones edge de AWS
    - Almacenar solicitudes comunes, disminuir latencia

- S3 Transfer Acceleration:

    - Acelera cargas y descargas globales en S3

- AWS Global Accelerator:

    - Mejora disponibilidad y rendimiento de aplicaciones globales
      utilizando la red glogal

### Route 53

- DNS gestionado, sistema de nombre de dominio

- Reglas y registros para lllegar a un servidor a través de URL

- Enlaza IP con dominio

- Convertir URL a IP, devuelve la IP después de recibir el dominio, el
cliente luego envía la solicitud HTTP a la IP del servidor

- POLITICA DE ENRUTAMIENTO DE LA ROUTE 53:

- SIMPLE ROUTING POLICY:

    - No hay controles de salud: no se revisa el estado de la maquinaria
    - Envío de URL y respuesta de IP

- Weighted routing policy:

    - Distribucion de peso en función de lo que le asignemos a cada
      instancia

- Latency routing policy:

    - En función de la latencia distribuiomos hacia un lado u otro

- Failover routing policy:

    - Por error o fallos
    - Envío a servidor primario, pero en caso de fallo o desastre lo
      envía al servidor de fallo

### CloudFront

- Red entrega contenidos
- Mejora el rendimiento de lectura, contenido en cache en edge location
- +400 puntos presencia a nivel muldial, ubicaciones edge
- Proteccion DDoS integración con shield o Web Application Firewall

### CloudFront – origenes

- Origen informacion

- Bucket S3: almacenar archivos y distribuierlo en cache en el borde

    - Segurirdad mejoradea con CloudFront Origin Access Control OAC
    - Puede usarse como entrada a contenido

- Origen VPC:

    - Aplciaciones alojads en subredes privadas dentro de una VPC
    - ALB privado o NLB para exponer estos servicios

- Origen personalizado HTTP

##     - Alb
##     - EC2
    - Sitios web S3
    - Backend HTTP

- En petición llega primero CloudFront Edge Location y revisa si ya
    está en cache primero, luego, consulta el origen y guarda el
    contenido en cache para un futuro

- S3 como origen:

    - La OAC: identidad de accsso al origen y una política de bucker S3
      solo da acceso a las edge location al origen que podría ser un
      bucket S3

- Diferencia entre CloudFront y S3 cross región repolication CRR:

### - CloudFront

      - Red global de edge locations
      - Archivos se almacenan en cache durante TTL, time to life, tiempo
        de vida
      - Ideal para contenido estático, disponible globalmente

##     - Crr:

      - Replicar datos distinteas regiones
      - Tiempo real actualizacion
      -  **Es más para disponibilidad y redundancia de datos de solo
        lectura en la regiones replicadas**
      - Es ideal para contenido dinámico con baja latencia

### S3 Transfer Acceleration

- Aumenta la velocidad de transferencia moviendo el archvio a una
ubicacion edge que reenvia los datos al bucket S3 en la región destino
- Fichero – wwwpublica – edge location – rápido y privado – bucket S3

### Global Accelerator

- Mejora disponibilidad y el rendimiento global usando la red global de
AWS
- Usa red interna para optimizar la ruta hacia aplicación, 60 % mejora
- Se crean 2 IP anycast para la aplicación y el tráfico se envía
a través de los edge location
- Las ubiciones edge envian tráfico a tu aplicación

### Global Accelerator vs CloudFront

- Ambos utilizan red blobas y edge locations

- Integran shield para la protección DDos

- CloudFront: red entrega contenido\_

- Mejora rendimiento almacenable en cache, imágenes y videos
- Contenido entregado en edge location

- Global Accelerator:

- No almacemiento en cathe
- Proxy en paquetes en edge lotacion app que se ejecutan en una omas
    regiones
- Mejora rendiemiento en aplica gama app sobre TCP o UDP
- Usos de HTTP con IP estáticas
- Http con conkmutacion por error regional
-

### Outposts

- Cloud híbrido: empresas que mantienen una infraestructura local y una
una infra en la nube

- Dos formas de uso

- Cloud: utilizando consola AWS, CLI, Y API
- Una infra on-premises

- Outposts = racks de servidores. Con la misma infraestructura,
servicios, API, herramientas AWS para crear las aplicaciones de
cliente

- AWS configura y administra los racks outposts en la infra del cliente
para usar los servicios de AWS en las instalaciones de la empresa de
este

- Cliente responsable de la seguridad física

- Ventajas:

- Acceso baja latencia a sistemas locales

- Procesamiento local de los datos

- Residencia de datos

- Migraciaon más fácil de las intalaciones del cloud

- Servicio totalmente gestionado

- Servicios que funcionan con outposts:

##     - EC2
##     - Ebs
    - S3
##     - Eks
##     - Ecs
    - Rds
    - Emr

EXAMEN: como llevar la nube – híbrido – a la empresa el servicio es
Outposts

### Wavelength

- Despliegue infraestructura incrustado en centros de datos de
proveedroes de telecomunicacoines de redes 5G
- Llevar servicios al limite de redes 5g
- EC2. EBS. VPC
- App latencia ultra baja con redes 5 g
- Trafico no sale de la red del proveedor de red
- Conexion segura y gran ancho de bandda con la región AWS matriz
- No hay cargos adicionales ni acuerdos de servicio
- Usos: ciudades inteligentes, diagnósticos machine learning, vehículos
conectados, flujos de video

### Local Zones

- Asignar informatica, almacenamiento, base de datos u otras servicios
para ejecutar aplicaciones sensibles a la latencia
- Amplia la Virtual Private Cloud VPC a más ubicaciones, seria una
extension de una región de AWS
- Compatible con EC2, RDS, ECS, EBS, ElastiCache, Direct Connect

### Arquitectura global de aplicaciones

### Opciones

- Región unica, AZ unica:

- Baja disponibilidad, baja latencia global, dificulta baja para hacer
    esto

- Una región, AZ multiple:

- Alta disponibilidad, mala latencia global, dificulta un poco más
    elevvada

- Multiregion, Activa-Pasiva:

- Activa: usuario pueden hacer acciones de lectura y escritura
- Pasiva: usuarios solo pueden leer
- Baja Latencia de lectura, no latencia de escrituras

- Multiregion, activa-activa

- Latencia de lectura y escritura baja

## Integraciones Del Cloud

- Hay dos patrones de comunicaciones:

- Sincronas

    - Comunicacion de app a app

- Asincrona

    - Basada en eventos , es decir, existe un intermediario entre
      servicio y servicio llamado cola

### - Ventajas en uso de colas

      - Es buena en caso de picos repentinos de tráfico
      - Desacoplar con SQS (modelo de cola)
      - SNS – modelo publicacion-subscripcion
      - Kinesis: modelo de flujo de datos en tiempo real

Examen: pregunta direcoinada a desacoplar app utiles estos servicios

### SQS (Simple Queue Service)

- Una cola:

- Productores envian mensajes que se guardan en una cola, puede ser en
    orden o sin orden

- Consumidores envian mesajes de encuesta si hay algo a consumir o
    hacer algo con los mensaje que están guardados en la cola

- SQS – cola estándar:

    - Oferta más antigua de AWS, más de 10 años
    - Gestionado, utilizado para desacoplar aplicaciones
    - El escalonamiento puede ser de un mensaje por segundo hasta 10
      mill
    - Puede haber retencion de mensajes de 4 adias y máximo de 14
    - No hay limite de menajes que puede haber en la cola
    - Mensaje se eliminan después de ser leidos por consumidores
    - Baja latensia, -10ms pen publicacion y receptcion
    -  Consumidores pueden comartir trabajo de lectura de mensaje y hay
      escalonamiento horizontal,
    - El escalonamiento horizaontal ocurre cuando SQS solicita al Auto
      Scaling Group que gestione las instancias para consumir mensajes o
      peticiones

- SQS para desvincular niveles de aplicación

- SQS - Cola FIFO:

    - FIFO: First In First Out: ordenación de mensajes en la cola
    - Productores envian mensajes pero estos se numeran por SWS y los
      consumidores los consumen en el mismo orden

### Kinesis Data Streams

- Es igual a streaming de big data en tiempo real
- Servicio adminsitrado para recopilar, procesar y analizar datos en
streaming en tiempo real a cualquier escala.
- Kinesis data Streams: ingerir datos de múltiples funtes con baja
latencia
- Kinesis data Firehose: se encarga de cargar los datos en S3,
redshift, opensearch, etc de forma automática
- Furntes – kinesis data streams – kinesis data firehose – destinos: S3,
redshift

### SNS

- Desacoplar aplicaciones

- Enviar un mensaje a muchos receptores

- Alternativa a integración directa fuente a receptores

- Un servicio de publicacoin/subscripcion:

- SNS Topic pública infor de fuente y se subscriben todos los modulos
    que requieren los mensajes, incluido las SQS Queue

- Publicadores de eventos enviand mensaje a un solo SNS Topic

- Subscritores habran tanto como cliente requiera y estos escucharan las
notificaciones de SNS topic

- Cada subscritor del Topic recibira todos los mensajes

- Pueden haber hasta 12millónnes 500 de subscriptores por SNS topic,
liminite de 100 mil topics

- **EXAMEN : Modelos de publicacion/subscripcion pensar en SNS**

### MQ

- Servicio no nativo que usan protocolos no abiertos
- Gsetionado de intermediacion/broker de mensajes para RabbitMQ o Active
MQ
- No escala igual que SQS
- Se ejecuta en servidores, en múltiples AZ con conmutacoin por error
- MQ tiene tanto la función de cola como la de tema SQS y SNS

## Monitorizacion Del Cloud

### CloudWatch

- Control de servicio y gestion de estos

### CloudWatch Metrics

- Servicio que proporciona métricas para los servicios AWS

- Metrica variable que se puede monitorizar

- Metricas tienen marcas de tiempo

- Se pueden crear dashboardas o panel de control con las métricas

- Metricas relevantes:

- Instancias EC2:

##     - CPU
    - Comprobaciones del estado de la instancia
    - Red
    - Metrica por defecto 5 minutos
    - Opcion metrica detallada, pago, cada minuto

- Volumenes EBS:

    - Lecturas y escrituras sobre el disco

- S3

    - Bucketsizebytes, numberofobjects, allrequests

- FACTURACION:

    - Cargo total estimado mensualmente, solo en us-esast1

- Coutas de servicio:

    - Utilizacoin de API de servicio

- Metricas personalizadas

-

### CloudWatch Alarms

- Para activar notificaciones de métricas

- Acciones alarmans:

- Autoescalado: auamentar o disminuir ECS

- Acciones EC2: detern terminar o reicniar o recuperar una EC2

- Notificaciones SNS:

- Opciones:

    - Muestreo, máximo, mínimo

- Eleccion de periodo para evaluar alarma

- Estados alarma: ok, insufficiente, data, alarm

### CloudWatch Logs

- Recoger logs:

- Elastic Beanstalk: recogida logs desde app
- ECS desde los contenedores
- Lambda: logs de funciones
- CloudTrail: usando un filtro
- Agentes de logs de CloudWatch, EC2 y servidores locales
- Route 53: registro consultas DNS

- Monitorizacoin en tiempo real

- Retencion de logs de CloudWatch ajustable

- CloudWatch para EC2:

- Ningun log de EC2 va para cloudwathc
    - Ejecutar un agente de CloudWatch en EC2 para enviar los archivos
      de logs
    - Asegurar permisos IAM
    - Agente puede ser configurado en instalaciones del cliente,
      servidor local

### EventBridge

- Previamente CloudWatch Events

- Trabajos Cron, scripts programados

- Crear patrones de eventos, reglas para reaccionar ante una accion de
un servicio

- Reglas:

- Fuentes de ejemplo

    - Lo que va a generar accion y esa accion se va a generar en un
      destino

- Destinos de ejemplo

    - Computacion: Lambda, batch, ECS task
    - Integración: sqs, sns, kinesis data streams
    - Orquestacion:\_ step functions, codepipeline, codebuild
    - Mantenimiento: ssm, EC2 actions

- Bus:

### - De eventos por defecto

      - De aplicaciones y servicios y se puede ejecutar código

    - De eventos de socios:\_

      - De aplicaciones externos a AWS
      - Mas fluidez

### - De eventos personalizados

      - Separa flujos de eventos
      - Reglas y permisos para diferentes buses

    - Buses tiene registro de esquemas, archivacion y reproducir eventos
      archivados

### CloudTrail

- Proporciona gobernanza, normativa y auditoria de cuenta AWS

- Activado por defecto

- Inspeccion y auditoria

- Obten historial de eventos o llamada de la APIs:

- Por consola
- Skd
- Cli
- Servicio de AWS

- Se puede asignar los logs de CloudTrail en CloudWatch logs o en S3

- Rastro puede aplicarse a todas las regiones por defectos a una
especifica

- Si se elimina un recurso en AWS, investigar primero en cloudtrail

- Se pueden instancias llamdas desde usuario IAM y roles IAM

- Todos lo registro se pueden guardar en CloudWatch logs o en un S3
bucket

-

-

### X-Ray

- Análisis visual de aplicaciones:

- registro de como actua un servicio

- tiempo medio de respuesta

-como está conectado con otros servicios

- Como son las ips de esos servicios

- Ventajas:

- Solventar problemas de rendimiento o performance
- Comprender las dependencias en arquitectura de un microservicio
- Identificar problemas del servicio
- Revisar el comportamiento de solicitudes
- Encontrar errore y excepciones
- X-ray puede responder si se cumple el acuardo de nivel de servicio
    SLA de tiempo y donde está limitado en cuanto el servicio
- Identificar los usuarios afectados

### CodeGuru

- Servicio con tecnología machine learnigng para revisiones de código
automatizadas

- Recomendaciones sobre el rendimiendo apps

- Funcionalidades:

- CodeGuru Reviewer: revisiones de código automatizadas

    - Análisis estático de código, desarrollo

- CodeGuru Profiler:

### - Visibilidad Y recomendaciones

      - Sobre el rendimiento de la app durante tiempo ejecución,
        producción

- CodeGuru Reviewer: revisiones de código y recomendacones practivas

    - Programacion

### - Ventajas

      - Identifica problemas criticos
      - Vulnerabilidades de seguraidad
      - Fallos dificiles de encontrar
      - Mejores practicas de codificacion
      - Fugas de recursos
      - Detecion de seguridad
      - Validacion de entradas
      - Utiliza machine learning y razonamiento automatizado
      - Lecciones aprendidas con revisioens de muchos repositerioas
        abiertos de Amazon
      - Soporta Java y Python
      - Se ingrega con github, bitbucket y AWS codeCommit

- CodeGuru Profiler:

    - Detecta y optimiza líneas costosas de código preproducido

    - Construye y testea

    - Mide el rendimiento y mejores de costes en la producción

### - Ventajas

      - Comprender el comportamiento en tiempo de ejecución

### - Funciones

        - Identificas y eliminar las ineficiciencias del código
        -  Mejorar rendimiento aplicación, reducir uso harware
        - Resumen de pila, identifica objetos que consumen memoria
        - Deteccion de anomalias
        - Se puede ejecutar en aplicaciones que se ejecutan en AWS o en
          instalaciones

### Health Dashboard

- Historial de servicios

- Muestra todas las regiones los servicios y su salud por días

- Muestra informacion historica de cada dia

- Tiene un canal de RSS para recibir alertas

- **Health Dashboard - Estado de Cuenta – Afectaciones a servicios de
### cliente**

- Revision de servicios en uso
- Alertas y orientación para solucionar problemas como ventanas de
    mantenimiento que puede afectar el fucionamiento de apps de clientes
- Ofrece una versión personalizada enfocada en servicio que usa un
    cliente y la disponibilidad de los servicios AWS
- Gestiona eventos den curso y da notificaciones para planificar antes
    eventos en los servicios de Amazon
- Agregar datos de un organizacoin amaozn
- Servicio global

## Virtual Private Cloud – VPC

- Conceptos clave:

- VPC
- Subredes
- Puertas de enlace de internet
- Puertas de enlace NAT
- Grupos de seguridad
- ACL de red NACL
- Logs de flujo de la VPC
- VPC peering
- VPC endpoints
- Site to Site VPN
- Direct Connect
- Transit Gateway

### Direcciones IP en AWS

- IPv4: protocolo de inteernet versión 4, 4.3 mil millónnes de
direcciones

- IPv4 pública: puede usarse en internet
- EC2 obtiene una nueva IP pública cada vez que se detiene y luego se
    reinicia
- IPv4 privada: dentro de redes privadas LAN como la red interna de
    AWS, siempre será la misma en EC2

- IP Elastica: fijar una dirección IPv4 pública fina a una instancia EC2

- Costos de IPv4 en AWS de 0.005 dólares por hora, incluye EIP

- IPv6 – protocolo de internet versión 6 (3.4x10 a la 38 direcciones)

- AWS soporta IPv6 pública y la IPv6 privada en VPC
- Esta es gratuito en AWS

### VPC –Virtual Private Cloud

- red privada para desplegar recursos, es un recurso regional

- Subredes: particionar la red dentro de VPC. Recurso zona
disponibilidad
- Subred pública: subred accesible desde internet
- Subre privada: no se puede acceder desde internet, pero ella si puede
acceder a internet con NAT
- Tablas de ruta: definir acceso a internet y entre subredes
- RANGO = IP

- GATEWAY DE INTERNET

- Ayudan a instancias VPC a conectarse a internet
- Subredes publicas tiene un ruta hacia el gateway de internet

- Opciones para permitir que subredes privadas accedan a internet SIN
## Dejar De Ser Privadas:

- GATEWAYS NAT:

    - Gestionados por AWS

- INSTANCIAS NAT:

    - Autogestionadas

- Subred privada se conecta con el NAT Y este se conecta con el gateway
de internet para salir a internet

### NACl y grupos de seguridad

- NACL (ACL de red):

- Firewall o cortafuegos que controla el tráfico desde y hacia la
    subred
- Puede tener reglas de ALLOW y DENY
- Se adjunta a nivel de subred NO de instancia
- Reglas solo incluyen direcciones IP
- Sin estado: reglas deben permitir de forma explícita el trafic de
    retorno
- Procesa reglas en orden, empezando por regla numerada más baja
- Aplica automáticamente a todas las instancias de las subredes con
    las que se ha asociado

- Grupos de Seguridad:

- Firewall que controla el tráfico hacia y desde una instancia EC2
- Solo reglas de ALLOW
- Reglas de direcciones IP y otros grupos de seguridad
- Con estado, tráfico retorno se admite autometicamente
- Evaluar todas las normas antes de decidir si permitir tráfico
- Se aplica a una instancia unicamente

**Logs de flujo de la VPC:**

- Captura info sobre tráfico IP que entra a interfaces:

- Logs de flujo VPC
- Logs flujo subred
- Logs de flujo interfaz de Red Elastica

- Spervisar y solucionar problemas de conectividad

- Subredes a internet
- Subred a subred
- Internet a subredes

- Captura informacion red interfases gestionadas como elastic load
balancers, elasticcache, RDS, aurora, etc

- Estos dastos de log se pueden almacenar en CloudWatch logs y kinesis
data firehose

### VPC peering

- Conectar dos vpc en forma privada usando red AWS
- Como si estuvieran en la misma red
- No deben tener un rango de dirección IP CIDR superpuesto o establecido
- Conexion no es transitiva, debe establecerse par acada VPC que
necesite comunicarse entre si

### VPC endpoints

- Conectar a servicio AWS utilizando una red privada en lugar de una red
pública
- Mayor seguridad y menos latencia para servicios AWS
- VPC endpoint Gateway está enfocado a S3 y DynamoDB
- VPC endpoint interface para el resto de los servicios, ejem,
CloudWatch

### AWS PrivateLink (Servicios VPC endpoint)

- Forma más segura y escalable de exponer servicios a VPCs
- No requier VPC, gateway de internet, NAT, tablas de rutas...
- Solo es un link que se lanza para conectar VPCs, el tráfico no viaja
por internet sino por la red privada

### Site to site VPN

- Conectar una VPN :

- Conectar una VPN on premise a AWS
- Conexión encriptada auto
- Pasa por internet pública

### Direct Connect

- Establecer una conexión física entre las instalaciones del cliente y
AWS
- Conexion privada, segura y rápida
- Pasa por una red privada
- Tarda al menos un mes en establecerse

Centro datos-------pública--------- site to site
VPN-------pública----------VPC

Centro datos-----privada---------directconect-------privada------VPC

Centro datos----customer Gateway------SITE TO SITE VPN-------Virtual
private gateway –VPC-----Subredprivada

### Cliente VPN

- Conectar desde ordenador personal mediante OpenVPN a red privada en
AWS e instalaciones
- Conectar a EC2 desde unaIP privada, como si estuviera en una red VPC
privada
- Pasa por internet pública

### Transit gateway

- Servicio para simplificar topologías de conexiones y servicio de red
- Se hace teniendo una conexcion peering transitivo entre miles VPC y
locales
- Conexion estrella: un único gateway para proporcionar está
funcionalidad
- Funciona con el gateway de Direct Connect y las conexiones VPN

### Seguridad y normativa AWS

### Modelo de responsabilidad compartida

- AWS – seguridad del cloud

- Servicios gestionados

- Cliente:

- Seguridad dentro del cloud

- EC2, ejemplo:

    - Gestion sistema operativo invitado

      - Parches
      - Actualizacion de seguridad
      - Configuracion firewall
      - Red
##       - IAM

- Encriptacoin de los datos de la app

- Controles compartidos:

    - Gestion de parches
    - Gestion de configuración
    - Concienciacion
    - Formacion

- RDS, ejemplo:

##     - AWS:

      - Gestionar EC2 subyacente
      - Desactivar acceso SSH
      - Parcheo automatizado del BD
      - Parche auto SO
      - Auditar discos, instancia subyacente y garantizar su
        funcionamiento

    - Cliente

      - Comprobar reglas de entrada puerto, IP, grupo de seguridad con
        la BD
      - Creacion usuario BD y permisos
      - Crear una BD con o sin acceso pública
      - Asegurar parametros de la BD para permitir solo conexiones ssl
      - Config cifrado BD

- S3:

##     - AWS:

      - Alamcenamiento iliimitado
      - Encriptacion
      - Separacion datos clientes
      - Empleados AWS no tenga acceso datos

### - Clientes

      - Configurar el buckt
      - Política pública y configuración pública
      - Usarioa e IAM
      - Habilitar cifrado

### Ataque denegación de servicio: DDoS

- Inundar peticiones al servidor para saturarlo

- Soluciones desde Amazon, servicios:

- AWS Shield Standard:

    - Protege contra DDos
    - Sin coste}
    - Contra SYN/UDP FLOOD
    - Atques de reflexion y otros ataques de capa 3 y capa 4

- Shield Advance:

    - Premium, pagada 3000 dólares por organización
    - 24/7 contra DDos
    - Ataquees más sofisticados para EC2, ELB, CloudFront, Global
      Accelerator, Route 53
    - Consultas equipo de respuesta DDoS

- WAF:

    - Filtra solicitudes específicas basadasd en reglas

    - Vulnerabilidades capa7 – HTTP

    - Se despliega en el ALB, API gateway, CloudFront

### - Define la ACL lista de control de acceso a la web

### - Reglas de

        - Direccoines IP
        - Cabeceras HTTP
        - CUERTPO Http
        - Cadenas URI

### - Proteccion contra

        - Inyeccion SQL
        - Cross Site Scripting XSS

      - Restriccion de tamaño, geo-match bloquear países

      - Reglas basadas en la tasa para la protección DDoS

- CloudFront y Route 53:

    - Proteccoin de disponibilidad mediante red borde global
    - Combinando con shield mitigar ataques en el borde

- Auto Scaling

### Network Firewall

- EXAMEN: COMO PROTEGER TU VPC EN GENRAL: NF

- Proteccion de capa 3 a 7

- Protege desde cualquier dirección:

- Trafico VPC A VPC
- Saliente a internet
- Entrante de internet
- Hacia desde Direct Connect y VPN site to site

### FIrewall Manager

- Adrministrar reglas de seguridad en las cuentas

- Política de seguridad:

- Conjunto común de reglas de seguridad

    - Para VPC para EC2 o ALB
    - Reglas WAF
    - Shield Admanced
    - Network Firewall

- Las reglas se aplican a los nuevos y futuros recursos

### Pruebas de penetracion

- En la infraestructura del cliente en ocho servicios

- EC2
- NAT Gateways
- ELB
- RDS
- CloudFront
- Aurora
- API Gateway
- Lambda y Lambda Edge
- Lightsail

- Actividades prohibiadas sin previa autorización de AWS:

- Caminar zona DNS en zonas alojadas de Route 53
- DOS DDOS
- Inuncdacion puerto
- Inundacion protocolos
- Inundacion solicitudes de inicio sesion o solicitudes API
- Otros eventos: contactar a AWS
-

### Encriptacion KMS Y CloudHSM

- datos en reposo:datos almacenados o archivados

- En transite: datos que se transladas

- Servicio que cifra datos en ambos estados para protegerlos:

- Claves de cifrado

- KMS:

##     - Examen: Si Mencionan Encriptacion, Lo Mas Probable Es Que Sea

- **KEY MANAGEMENT SERVICE**

    - Gestion de claves de crifrado por nosotros

### - Opcion de cifradoo

      - Volumenes EBS: cifrar volúmenes
      - Buckets S3: encriptación de objetos del lado del servidor
      - BD Redshift: cifrado de datos
      - BD RDS: cifrado de datos
      - Unidades EFS: cifrado de datos

### - Cifrado automatico

      - Log de CloudTrail

- CloudHSM:

    - Proporciona el hardware de encriptación

    - Harware Security Module

    - Gestiona por completo el cliente sus claves de cifrado

    - El dispositivo hsm es resistente a manipulacion

    - Customer Master Keys CMK

- Gestionado por cliente:

          - Creada, grestionada y utilizada por el cliente
          - Posiblidad de política de rotacion
          - Posibilidad de traer propia clave

        - Gestionada por AWS

          - Crea, gestionanda y utlizada por AWS
          - Utilizada por los servicios de AWS

### - CMK propiedad de AWS

          - Colleecion de calves que un servicio posee ygestionana para
            utilizarla en múltiples cuentas
          - AWS usa para protegar recursos de cuentas del cliente, pero
            este no las puede ver

### - Claves CloudHSM

          - Claves generadas por tu propio dispositivo de hardware cloud
            sm
          - Operacoines criptograficas se realizan dentor cluster
            cloudhsm

### Certificate Manager

- Permite aprivisionar, gestionar y desplegar certificados SSLTLS

- Los certificados se utilizan para encriptar los sitios web https

- Admite certificados TLS públicos y privados

- Gratuito para TLS públicos

- Renovacion automaticos para TLS

- Integraciones con carga de certificados TLS

- ELB
- Distribuciones CloudFront
- APIs en API gateway

### Secrets Manager

- Destinado a almacenar secretos
- Forza rotacion de secretos cada xdias
- Automatiza generecion de secretos en rotacion
- Integración con RDS, MySQL, postgresql, aurora
- Los secretos se encriptan con KMS
- Servicio pensado para ingregracion con RDS

### Artifact

- NO ES UN SERVICIO

- Portal que proporiciona acceso bajo demandanda a la documentacion de
### conformidad de AWS y sus acuerdos

- Artifact Reports: descargas docuemntos de seguridad y confirmaidad
    de auditores externos, certificaciones ISO, informes de sector
    tarjetas de pago PCI, informes de control de sistemas y organización
    SOC
- Artifact Agreemients: revisar, aceptar y hacer seguimiento del
    estado de los acuerdos de AWS, el Business Associate Addendum BAA o
    Health INsurance Portability and Accountability Act HIPAA
- SE PUEDE USAR PARA APOYAR LA AUDITORIA INTERNA O NORMATIVA

### GuardDuty

- Desubrimiento inteligente de amenzas para proteger cuenta AWS

- Utiliza algoritmos de ML, deteccion de anomalias y datos de terceros

- Se activa con un click

- No se debe instalar softwares

- Los datos de entrada incluyen:

- Log de eventos de cloudtrail:

    - Llamadas inusiales API, despliegues no autorizados
    - Eventos gestio CloudTrail: crear subred VPC, rastros
    - Eventos datos S3 en CloudTrail: obtener un objetos, listasr y
      eliminar objetos

- Logs de flujo de VPC:

    - Trafico interno inusual, direcicon IP inusual

- Logs de DNS:

    - Instacias EC2 comprometidas que envian datos coficiados dentro las
      consultas DNS

- Caract opciones: datos de entrada: EKS audit logs, RDS, Aurora, EBS,
    Lambda, S3 Data Events

- Puedes configurar reglas de EVentBridge de CloudWatch para hallazgos

- Estas reglas pueden dirigirse a la lambdao SNS

- Puede proteger contra ataques de criptomonedas

### Inspector

- Evaluaciones de seguridad automatizadas

- Para EC2:

- Usa agente AWS system manager
- Analiza contra accesibilidad no intenciopnada en la red
- Analiza SO en ejecución frente a vulnerabilidades conocidas

- Para imágenes del contendor enviadas a ECR

- Evaluacion de imágenes a meidad que se envian

- Funciones Lambda

- Identifica vulnerabilidades en código y en las dependencias de los
    paquetes
- Evaluacion de funciones a medida que se despliegan

- Informes e integración con Security Hub

- Se envian informes a eventbridge

- SOLO EC2, IMAGENES CONTENDOR Y FUNCIONES LAMBDA

- Escaneo continuo de infraestructura solo cuando sea necesario

- Vulnerabilidades de pagquetes EC2 ECR Lambda base de datos de CVE

- Evaluar accebilidad a la red cuando se usa EC2

- Se asocia una puntuacion de riesgo para priorizarlas, una lista

### Config

- Audita y registra normativa de recursos AWS

- Registrar configuracoines y los cambios a lo largo del tiempo

- Posibildiad de alamancer los datos de configuración de S3 analizados
por athena

- Preguntas que se pueden resolver:

- Acceso SSH sin restricciones a mis grupos de seguridad
- Buckets tiene acceso público
- Como ha cambiado configuración de mi ALB con el tiempo

- Recibe alertas SNS de cualquier cambio en los servicio

- Es un servivio por región

- Permite agregar se por regiones o cuentas

- Este es un servicio de pago

### Macie

- Servicio de seguridad y privacidad getionado que utiliza ML y
concordancia de patrones para descubrir y proteger datos sensiebles en
AWS
- Identificar y alertas sobre datos sensibles coomm informacion personal
identificacbles PII
- Analiza y descubre datos sensibles, usa EventBridge par ala
notificación

### Security Hub

- Herramienta de seguridad central para gestionar seguridad de varias
cuentas de AWS

- Automatizar comprobaciones de seguridad

- Posee dashboards integrados que muestra el estado actual de la
seguridad y normativa para tomar medidas rapidamente

- Agrega automáticamente alertas yen formatos predefinidios o de
### hallazgos personales de servicios de AWS y herramientas de socios AWS

- Config, GuardDuty,inspector, macie, IAM acess analizer, system
    manager, firewall manager, health, partner network solutions
- Es fundamental primero habilitar el servicio de Config de AWS
- Precio puede ir en función de comprobaciones de seguridad o por
    busquedas de eventos de ingesta

### Detective

- Analiza, investiga e identifica rápido la causa raíz de los problemas
de seguridad o las actividades sospechosas
- Recoge y procesa auto los eventos de logs de flujo de la VPC, cloud
trail, guardduty y crea una vista unificada
- Produce visualizacoines con detealles y contexto para llegar a la
causa raíz

### Abuse

- Informar sospecha de recursos AWS con fines abusivos o ilegales

- Estos son :

- SPAM
- Escaneo de puertos: envio de paquetes a sus puertos para descubrir
    los no seguros
- Ataques DoS o DDoS
- Intentos de intrusion: logs en tus recursos
- Alojar contenido censurable o con derechos de autor
- Distribucion de malvare: recursos AWS que distribuyen software para
    dañar ordenadores o máquinas

\*Privilegios de usuario root;

- Usuario root= propietario de la cuenta

- Tiene acceso completo a todos los servivcios o recursos de AWS

- Se debe bloquear las claves de acceso del usuario root

- No usar este usuario para tareas coditidanas ni administrtivas

- Acciones de este usuario:

### - Cambiar confi de la cuenta

      - Nombre cuenta
      - Correo
      - Contraseña
      - Claves de acceso
      - Ver facturas de impuestos
      - Cerrar cuenta AWS
      - Restaurar permisos de usuario IAM
      - Cambiar o cancelar plan AWS support
      - Se puede registrar como verndedor del market place reseved
        instances
      - Configurar un bucket S3 para habilitar la MFA
      - Editar o eliminar política de bucket S3 que incluya un ID de VPC
        o in ID de enpoint no VPC no valido

### IAM Access Analyzer

- NO ES UN SERVICIO, ES UNA HERRAMIENTA DE IAM

- Descubrir permisos de sus recursos en AWS

- Averigua que recursos se comparten externamente:

- S3
- Roles IAM
- Claves KMS
- Lambda y capas
- SQS
- Secrets Manager

- Se define una zona de confianza = cuenta AWS o AWS organization

- Acceso fuera de está zona: hallazgos

-

## Machine Learning

### Rekognition

- Encontrar y detectar personas, objetos, textos, escenas en imágenes y
videos mediante Machine Lerarning

- Análisis facial y busqueda facial para verfiica usuario o recuento de
personas

- Crear BD de caras conocidas o compara con famosos

- Casos de uso:

- Etiquetado
- Moderacion de contenidos
- Deteccion de textos
- Deteccion y análisis de rostros, genero, rango de edad ,emociones
- Busqueda y vreificacion de rostros
- Reconomiento de fasosos
- Trayectoria, análisis de juegos

### Transcribe

- Convertir de forma autormatica el habla en texto

- Proceso de deep learning llamado RECONOCIMIENTO AUTOMATICO DEL HABLA,
ASR, para convertir el habla en texto de forma rápida y precisa

- Elimina auto info de identificacion personal PII

- Identificacion auto de idio para audio multilingue

- Usos:

- Transcribi llamadas de atencion al cliente
- Auto subtitulado y los subtitulos
- Generar metadatos para los activos de los medio de comunicaicon para
    crear un arvhico con todas las posiles busquedas

### Polly

- Convierte texto en voz real utilizando deep learning
- Permitiendo crear aplicaaciones que hablan

### Translate

- Servivcio para traduccion natural y precisa
- Permite localizar contenidos como sitios web y app para usuarios
internacionales ytraducir grandes volumnes de texto

### Lex & Connect

- Lex:

- Reconocimiento del habla para convertirlo en texto
- Compresion del lenguaje natural para reconocer intención del texto
    de las personas que llaman
- Ayuda a crear chatbots o bots de centros de llamadas

- Connect:

- Recibe llamadas y creas flujos de contacto, ejem, centro de contacto
    virtual basado en la nube
- Pueden integrarse con sistemas CRM o AWS
- NO TIENE PAGOS INICIALES, 80 % MAS BARATOS QUE SOLUCIONES
##     Tradicionales
-

### Comprehend

- Procesamiento de lenguaje natural, NLP – Natural Language Processing

- Gestionado, sin servidor

- Usa ML para encontrar ideas y relaciones en el texto

- Tiene:

- Lenguaje de texto
- Extrae frases clave, lugares, personas, marcas o eventos
- Comprende lo positivo y negativo del texto
- Analiza texto utilizando tokenizacion y partes del discurso
- Organiza auto coleccion de archivos de texto por temas

- Usos:

- Analiza interaccion con los clientes, correos electronicos para
    entonctarr lo que conduce a un experiencia posibtiva o negativa
- Crear y agrupar articulos por temas que Comprehend descrubrira:
    analizarlos y clasificarlos
-

### SageMaker AI

- Servicio gestionado para construir, entrenar y desplegar modelo de ML
sin pensar en infraestructura
- Este servicio agrupa todos los procesos en un solo lugar y ademas
provisionar servidores
-
-

### Kendra

- Servicio de busquedad de documentos
- Gestionado
- Potenciado por ML
- Extrae respuestas de documentos de texto, pdf, html
- Hay una fuente --- se indexa conocimiento de ML en KENDRA- Esto
capacita busquedas en lenguaje natural
- Aprende de interacciones con los usuarios, para buscar resultados
preferidos, APRENDIZAJE INCREMENTAL
- Capacidad para afinar manualmente resultados de busqueda: importancia
de datos, frescura, personalización

### Personalize

- Servicio que usa ML para crear app con recomendaciones personalizadas
en tiempo real

- Gestionado

- Recomendaciones de productos personalizados

- Marketin directo personalizado

- Utiliza tecnología Amazon.com

- Integración de datos en tiempo real usando Amazon Personalize API

- Se integra en sitios web, app movil, sms, email

- Se implementa en días no meses

- Usos:

- Tiendas minoristas,
- Medios de comunicacion
- Entretenimiento

### Textract

- SErvicio de extracion de texto, escritura y datos de cualquier
documento con escaneo de estos usando IA y ML

- Extrae datos de formularios y tablas

- Lee y procesa cualquier tipo de documento

- Usos:

- Servicios financieros: facturas e informes financieros
- Sanidad: historiales medicos o reclamanciones de seguros

- EXAMEN: EXTRAER INFORMACIÓN DE TEXTO

## Gestion De La Cuenta, Facturacion Y Soporte Tecnico

### Organizations

- Servicio global

- Gestionar varias cuentas de AWS

- Cuenta principal es la master account

- Beneficios costes:

- Facturacion consólida en todas las cuentas, metodo de pago único
- Factura unica
- Beneficios de precios por uso agregado, descuento por volument para
##     EC2 ...
- Agrupacion de instancias EC2 reservadas para ahorro optimo

- API disponible para automatizar creacoin cuentasa AWS

- Restringe privilegios de las cuentas mediantes POLITICAS DE CONROL DE
## Servicios, Scp

### Estrategias multicuenta

- Crear cuentas por:

- Departamento

- Centro de costes

- Entorno desarrollo, testing producttion

- Funcion restricciones normativas

### - usandoSCP

- Mejor aislamiento de recursos: VPC

- Limites de servicio separados por cuenta

- Cuenta aislada para registrar los logs

- Cuenta multiple vs cuenta unica con VPC multiple

- Utilizar normas de etiquetado para la facturación

- Activa CloudTrail en todas las cuentas para enviar logs a la cuenta
S3 central

### Unidades Organizativas UO

### Ejemplos

- UNidad de negocio (negocios, finanzas)
- Ciclo de vida medioambiental
- Basada en proyectos

### Service Control Policies SCP

- Se puede restriginr acceso que tienen los usuarios

- List blanca o negre de acciones IAM

- Se aplica a nivel de OU o cuenta

- No se aplica a cuenta maestra

- Se aplica a todos los usuarios y roles de la cuenta incluido el usuario
Raiz

- No afecta a los roles vinculados al servicio

- Roles vinculado a servicios permiten que otros servicio se integren
    con las Organizaciones de AWS y no pueden ser restringidos por SCP

- SCP debe tener un PERMITIR EXPLICITO, no permite nada por defecto

- Usos:

    - Restringir acceso a servicios específicos
    - Aplicar la normativa PCI

### Organization – Facturacion consólidaa

- Cuando se activa:

- Uso combinado: de todas las cuentas en la organización para
    compartir precios por volumen, instancias reservadas y descuentos de
    plos planes d ahorro
- Se proporciona una factura para todas las cuentas de Amazon
- Cuenta administración puede desactivar uso compartido de los
    descuentos de las instancias reservadas para cualquier cuenta de la
    organización de AWS incliuda ella misma

### Control Tower

- Servicio para configurara y gobernar un entorno AWS multicuenta seguro
### y conforme a las mejores practicas

- Ventajas:

    - Automatiza config entorno pocos clicks
    - Automatiza gestion continua de las políticas
    - Detecta infracciones de las políticas y las puede corregir
    - Supervisa normativa a través de un dashboard interactivo

- Este servicio se ejecuta sobre las organizacoines de AWS:

    - Se configura de forma automática las Organizaciones para
      implementar las organiacoines SCL

### Resource Access Manager

- Servicio para compartir recirsps de AWS con otras cuentas de AWS

- O dentro de la organización

- Evita duplicar recursos:

- Aurora, VPC, Trasit Gateway, Route 53

### Service Catalog

- Servicio para organizar y gestionar catalogos de servicios aprobados
para uso de toda la empresa en concreto

- Usuario tiene un portal rápido de autoservicio de un conjunto de
productos autorizados predefinidos por los administradores

- Incluye:

- Maquinas virtuales
- BD
- Opciones de almacenamiento

- Servicios etiquetado y configurados en el portafolio

### Modelos de precios

- 4 modelos de precios:

- Pagos por uso

- Ahorra cuando reserves

##     - EC2
    - DynamoDB capacidad reservada
    - Nodos reservados de ElastiCache
    - Instancias reservadas de RDS
    - Nodos reservados Redshift

- Paga menos usando más: descuentos por volumen

- Paga menos al crecer AWS

### Servicios y niveles gratuitos en AWS

- Nueva cuenta AWS = 200 créditos

- Plan gratuito: expira en 6 meses o cuando se consumen los créditos

- Plan pago: comienza a cobrarse duespues de consumir créditos

- Servicios Always Free:

- Lambda 1 millóns solicitudses mes 400 mil gb segybdi cinoyti nes
- DynamoDB: 25 gb alamceminato y 200 millóns solicitudes mes

### Precios computacion – EC2

- Solo cobra por lo que usas

- Numero de instancias, más intnacias más conste

- Configuracion de instancia

- Capacidad física
- Región
- SO y software
- Tipo de instancia
- Tamaño instancia

- Tiempo funcinamiento ELB y cantidad de datos procesados

- Monitorizacion detallada: CloudWatch tiene un coste

- INSTANCIAS BAJO DEMANDA:

- MINIMO 60S
- Paga por segundo Linux windos o por hora otros

- Instancias reservadas:

- 75% descuento en comparacoin con las instancias bajo demanda en la
    tarifa por hora
- Compormiso de 1 a 3 años
- Todo por adelantado, parcialmente por adelantando o sin adelanto

- Instancias spot:

- 90% descuento comparacion con la tarifa horaria bajo demanda
- Con riesgo interrupción
- Puja por la capacidad no utilizada

- Host dedicado:

- Bajo demanda
- Resserva para un compormiso 1 o 3 años

- Planes de ahorro:

- Alternativa más flexible para uso de instancias

### Precio de computacion – Lambda y ECS

- Lambda:

- Pago por llamada
- Pago por duracion

- ECS:

- Modelo tipo lanzamiento EC2,
- Pagas por los recursos de AWS almacenados y creadots en tu
    aplicación

- Fargate:

- Pago por recursos de vCPU y memoria asignados a tus apps en
    contenedoresf

### Precios de almacenamiento – S3

- Clase de almacenamiento: S3 standar, infrequent access, S3 ONe-Zone,
IA, S3 intelligent tiering, glacier y glacier deep archive
- Numero y tamaño de objetos
- Numero y tipo de solicitudes
- Transferencia de datos FUERA región S3
- Aceleracion de transferencia en S3
- Transiciones ciclo de vida

- Servicio similar EFS, pago por uso, reglas de acceso y ciclo de vida
poco frecuentes

### Precios de almacenamiento – EBS

- Tipo de volumen, vinculado al rendimiento

- Volumen de almacenamiento de GB por mes provisionado

- IPOS (INPUT – OUTPUT OPERATIONS PER SECOND) rendimiento de disco:

- SSD de propósito general : incluido
- IOPS provisionadas SDSD: pago por rendimiento adicional
- Magnetico número de peticiones

- Snapshots:

- Coste por almacenamiento incremental
- Costes de datos añadidos por GB al mes

- Transferencia de datos:

- La entrada es gratis
- Salida tiene un coste y está escalonada para descuentos por volumen
-

### Precios de las bases de datos – RDS

- Facturacoin por horas:

- Caracteristicas de la BD:

- Motos: sql, postgres
- Tamaño
- Clase de memoria, afecta rendimiento afecta el coste

- Tipo de compra:

- Bajo demanda
- Instancias reservas 1 a 3 años con pago inicial requerido

- Almacenamiento de copias de seguridad: hasta cierto tipo es gratuito
para una región

- Almacenamiento adicional por GB al mes

- Numero peticiones entrada y salida al mes

- Tipo de despliegue:

- Una unica AZ más barato, menos resiliente
- Varias AZ, mayor dispoinibilidad mayor coste

- Transferencia de datos:

- Datos salientes con coste pero escalonado por descuentos por
    volumen
- La entrada es gratis
-
-

### Precios – CloudFront

- Entrega de contenidos
- Los precios varias según las regiones geograficas
- Agregado pra cada ubicacion de borde, se factura por edge location y
se aplica a la factura
- Transferencia de datos a domicilio, descuento por volumen
- Numero de peticiones HTTP/HTTPS

### Costes de red en AWS por GB – Simplificado

- Trafico entre instancias gratis si se utiliza IP privada

- Trafico dos instancias de diferentes zonas de disponibilidad 0.02 sis
se utiliza IP pública o IP elastica

- 0.02 para tráfico entre dos instancias de diferentes regiones

- Consejos:

- Utiliza IP privada en lugar de IP pública para ahorro y rendimiento
- Utiliza la misma AZ para obetener máximo ahorro a pesar del la
    pérdida de alta disponibilidad

### Planes de ahorro SAVING PLANS

- Compromiso para pagar una cantidada de dólares por hora durante 1 o 3
años

- Es la forma fácil de establecer comprimisis a largo plazo

- PLAN AHORRO EC2:

- Descuento 72% contra el bland bajo demanda
- Compromiso uso de familias de instancias individuales en una región
    independientemente de la AZ, el tañamo, SO o ltenencia
- Pagos por adelantado, parcialmente o sin adelanto

- PLAN DE AHORRO DE COMPUTACION:

- 66% contra bajo demanda

- Independiente de familia, regiosn, tamaño, so , tenencia y opciones

- Opciones:

##     - EC2
    - Fargate
    - Lambda

- Plan de ahorro de ML: SageMaker

- Configuracion desde consolo Cost Explorer

### Compute Optimizer

- Ahorrar costes en despliegues y servicios a usar

- Mejora el rendimiento de AWS optimos para cargasd de trabajo que
tengan

- Ayuda a elegir config óptimas y dimensionar correctamente cargas de
trabajo = sobre o sub provisionamient

- Utiliza ML para analizar config recursos y métricas de utilzacion
CloudWatch

- Recursos soportados:

- EC2
- Grupos de autoescalado EC2
- Funciones Lambda

- Reducción de costes hasta un 25%

### Herramientas de facturación y cálculo de costes

- Estimación de costes en el Cloud:

- Calculadora de precios

- Seguimiento de los costes:

- Dsbhoards de facturación
- Etiquetas de asignación de costes
- Informes de costes y uso
- Explorador de costes

- Seguimientos planes de costes

- Alarmas de facturación
- Presupuestos

### Calculadora – Pricing Calculator

- Calcula el coste de la arquite de nuestra solucion

### Dashboards de facturación

- Herramienta de visualizacion

### Etiquetas – tags de asignación de costes

- Etiquetasd generads por AWS

- Se crea auto al recurso que creas
- Comienza con prefijo AWS:

- Definidas por el usuario:

- Prefijo: user:

### Etiquetado y grupos de recursos

- Se usan para organizar recursos

- EC2, instancias, imágenes, Load Balancer, grupos de seguridad

- RDS, recursos VPC, Route 53, usuarios IAM,

- Recursos de creados por CloudFormation se etiquetan de la misma
manerna

- Nomencaltura libre, más comunes: nombre, entorno, equipo

- Etiquetas se utilizan para crear grupos de recursos:

- Crear, mantener y ver coleccion de recursos que cmpoarten etiquetas
    comunes
- Gestionar estas etiquetas utilizando el Tag Editor

Cost and Usage Reports – CUR

- Profundiza costes y uso de AWS
- Conjunto más completo de facturación, se puede desglosar el uso por
servicio, por cuenta, etc
- Incluye metadatos adicinales sobre servicios, precios y reservas
- Enumera uso AWS para categoria de servicio por una cuenta y sus
usuarios IAM en partidas horarias o diarias
- Puede integrarse con Athena, Redshift o QuickSight

### Cost Explorer

- Visualizar, entender y gestionar los costes y usos de AWS a largo
plazo
- Herramienta principal de control
- Crea informes personalizados para analizar costes y uso
- Analiza datos a alto nivel : costes totales y uso en todas las cuentas
- O granularidad mensual, por horas y a nivel de recursos
- AWS recomienda planes de ahorro
- Prevision de uso con margen de confianza
- SE puede hacer una exportacion de datos

### Alarmas de facturación en CloudWatch

- Metricas de datos de facturación se almacena en CloudWatch us-east-I
- Datos facturación son costes globales en todo el mundo
- Coste real no para los costes proyectados
- Pretende ser una simple alamrna cuando supera un umbral, no es tan
potente como Budgets

Budgets

- Crear presupuesto y envía alarmas cuando los costes superar el
presupuesto

- 4 tipos de presupustos:

- Uso
- Coste
- Reserva
- Planes de ahorro

- Para instancias reservadas RI

- Hace un seguimiento de la utilizacion
- Para medir aprovechamiento
- Soporta EC3, ElastiCache, RDS, Redshift

- Hasta 5 notificaciones SNS por presupuesto

- Puede filtrar, servicio, cuenta vinculada, etiqueta, opción de compra,
instancia, regios, zona disponibilidaque Cost Explorer,

- Misamas opciones , capacidad de filtrado avanzadas

### Cost Anomaly Detection

- Monitorizar continua costes y sus mediante ML para detectar gastos
inusuales
- Aprende patrones de gastos unicos e historicos para detectar picos de
costes puntuales o aumentos continuos de costes
- Detecta gastos puntuales como la compra de un dominio
- No se define un umbral de coste
- Monitoriza servicios de AWS, cuentas asociadas, etiquetasd de
asignación de costes o categorias de costes
- Envia informe deteccion de anomalias con el analsis de causa raíz
- Recibe alertas o resumen diario, semana mediante SNS

### Service Quotas

- Servicio para avisar de un umbral de valor de cuota de servicio
- Crea alamas CludWatch en la consola de cuotas de servgicio
- Se puede solicitar un aumento de cuota en el servicio o apagar los
recursos antes de alcanzar el limite

### Trusted Advisor

- Servicio para evaluacion de alto nivel de la cuenta

- No es necesario instalar nada

- Analiza cuentas y genera recomendaciones en 5 categorias:

- Optimizacion de costes: ejem servicios inutilizados
- Rendimiento: mejoras para app sean eficientes
- Seguridad: config insegura o riesgos potenciales
- Tolerancia a fallos: análisis como mejorar resilencia sistemas
- Limites de servicio, aviso cuota AWS
- Excelencia operativa: buenas practicas para gestionar recursos

- Para acceder a verificaciones completas del servicio es necesario
### tener Plan de Soporte Business y Enterprise

- Conjunto completo de verificaciones
- Acceso programatico resultados mediante SUPPORT API

### Precios Planes de soporte para AWS

- Basico:

- Servicio atencion al cliente y comunidades, acceso 24x7 servicioal
    cliente, documentacion, libros blancos y foroes de dsportore
- Trusted Advisor: acceso 7 comprobaciones principales de Trusted
    Advisro y orientación para aprovisionar recursos siguiendo mejores
    practicas para aumentar rendimiento y y mejorar seguridad
- Acceso personal health dashboard: vision personalidad salud
    servicios AWS y alertas de recrusos que puedan afectarse

- Desarrollador :

- Basico

- Acceso por correo a asociacods en horario laboral de soporte cloud

- Casos ilimitados

- Un contacto principal

- Tiempo de respuesta:

    - Orientacion general menor 24 horas
    - Sistema deteriorado menor a 12 horas

- Business:

- Destinado a cargas de trabajo de producción

- Trusted Advisor con full comprovacion y acceso a la API

- Acceso telefonio y por correo y cah ingenieros de soprte cloud

- Casos ilimitados y contactos ilimitados

- Acceso a la gestion de eventos de infraestreuta por tarifa adicional

- Tiempo resputa:

    - Orientacion general: - 24 horas laborales
    - Sistema deterioradao – 12 horas
    - Sistema de producción deteriorado – 4 horas
    - Sistema producción averiado –1 hora

- Enterprise on ramp

- Destinado a ser utilizado en carga de trabajo de producción o
    criticas para el negocio

- Todo el plan soprote business

- Acceso a grupo GESTORES TECNICOS DE CUENTAS - TAM

- Equipo de sporte de atenciaon para facturación y mejores practicas
    de cuenta

- Gestion de evento sinfraestructura, revisiones de operacoines y bien
    diseñadas

- Tiempos de respuesta:

    - Orientacion general: - 24 horas laborales
    - Sistema deterioradao – 12 horas
    - Sistema averiado -1 hora
    - Sistema critico de negocio caido -30 minutos

-

- Enterprise:

- Destinado a ser utilizado si tienes cargas de trabajo de mision
    critica

- Incluido todo el plan empresarial

- Acceso a un GESTOR TECNICO DE CUENTAS TAM

- Equipo de soporet de atencion para la facturación y mejores
    practicas de la cuenta

- Tiene gestion de eventos de infraestructura, revision de operación y
    de la arquitectura

- Tiempo de respuesta:

    - Orientacion general: - 24 horas laborales
    - Sistema deterioradao – 12 horas
    - Sistema producción deterioradao – 4 horas
    - Sistema de producion averiado – 1 hora
    - Sistema critico de negocio caido – 15 minutos

### Mejores practicas pra las cuentas

- Operar múltiples cuentas utilizando organizacoines
- Utiliza SCP políticas de control de servicios para restringir el poder
de las cuentas
- Configurar facilmente varias cuentas con las mejores practicas con
Control Tower
- Utiliza etiquetas y etiquetas de asignación de costes para la gestion
y la facturación
- Pautas IAM: MAF, mínimo privilegio, política de contraseñas, rotacion
de contraseñas
- Config para hacer un registro de configutraciones de recursos y
normativa en el tiempo
- Utliliza CloudFormation para desplegar stacks entre cuentas y
regiones
- Trusted advisor para obtener información, plan de soporte adaptado a
tus necesidades
- Envía logs de servicio y de acceso a S3 o a CloudWatch logs
- Cloud trail servicio para registarr las llamdas a las API realizadas
en tu cuenta
- Si tu cuenta se ve compormoetica: cambia la contraseña root y borra y
rota todas contraseñas y contacta a soporte AWS
- Permitir a los usuarios stacks predefinidos definidos por los
adminsitradores mediantesAWS service catalog

## Identidad Avanzada

### Security Token Service STS

- Permite crear credenciales temporales con privilegio limiatos para
acceder a recursos

- Credenciales corta duracion con periodo de caducidad que lo configura
el usuario

- Uso:

- Federacion de identidades:

    - Gestionar las identifdades en sistemas externos y proporciona
      tokens STS para acceder a recursos de AWS, estos token tienen
      caducidad
    - Roles IAM para el acceso cruzado de la misma cuenta, cuando un
      usuario quiere acceder mediante un rol IAm a unos recursos
    - Usuario y máquinas se puede limiart para que accedan a otros
      recursos

### Cognito

- Servicio para dar identidada a usuario de aplicacoines web y móviles a
través de un usuario en Cognito
- Gestionar usuarios si son millónnes se puede usar congnito

### MIcrosoft Active Directory AD

- Base de datos de objetos: cuentas de usuario, ordenadores, impresoras,
archivos compartirdos, grupos de seguridad
- Gestion centralizada de la seguridad, creacion de cuentas y asignación
de permisos
- Se encuentra en cualquier servidor Windows con servicios de dominio AD

### Directory Services

- Managed Microsoft AD:

- Servicio para crear tu propio AD, administra los usuarios localmente,
    soporta MFA
- Establece conexiones de confianza con tu AD local, servidores
    locales con servidores cloud

- Conector

- Servicio enfocado a Directory Gateway para redirigir al AD local,
    soprta MFA

- Simple AD:

    - Directorio gestionado compatible con AD en AWS
    - No se puede unir con AD local

### IAM Identity Center

- Inicio de sesion único para todas tus cuentas de AWS en AWS
organizations

- Aplicaiones empresariales en el cloud: slesforce, box, microsofts
365...

- Aplicaciones habilitadas para SMAL2.0

- Instancias de Windows EC2

- Proveedor de identidad:

- Alamcen de identidades incorporado en IAM Identity center
- De terceros

## Otros Servicios

- Servicios separados de los grupos principales
- A veces aparecen en los examenes

### Workspaces

- Solucion de escritorio gestionado cmo servicio DaaS en Windows y Linux
- Eliminar gestion de VDI infraestructura de Escritorio Virtual local
- Rapidamente escalable a miles de usuario
- Datos seguros, se integra con KMS
- SERVICIO PAGO POR USO, TARIFAS MENSUALES O POR HORA
- EXAMEN: SERVICIO PARA DISMINUIR O MINIZAR ACCESO A ESPACIOS DE TRABAJO
## – Multiple Regions

AppStream 2.0

- Servicio de streaming de apps de escritorio para usuarios
- Entrega a culquier ordenador, sin adquirir, infraestructura de
aprovisionamiento
- EXAMEN: como entregar una app desde un navegador web
-

### Workspaces Vs AppStream 2.0

### WS

- Dispone una VDI y un escritorio gestionados
- Usuarios se conetan a la VDI y abren apps nativas o WAM
- Espacios de trabajo bajo demanda o siempre encendidos
-

### Appstream

- Trasmite app de escritorio a navegadores
- Funciona con cualquier dispositivo
- Configura tipo de instancia por tipo de aplicación

### IoT Core

- Permite conectar dispositerivos o sensores IOt a la nube
- Sin servidor,seguro y escalable a miles de milleones de devices o
billones de mensajes
- Apps pueden comunicarse con tus dispositivos incluso cuando no están
conectados
- Se integra con muchos servicios
- Construye applicaciones Iot que recopilen, procesen analizar y actuaen
sobre los datos
- EXAMEN: SERVICIO INTERNET DE LAS COSAS

### AppSync

- Almacenar y sincronizar datos entre app móviles y web en tiempo real
- Utiliza GraphQL, una tecnología movil de facebook
- El código del cliente se puede generar auto con GRAph
- Posee intregraciones con DynamoDB y Lambda
- Suscrpciion se pueden dar en tiempo real
- Sincronización de datos se puede dar sin conexción, sustituye cognito
sync
- El servicio de AMplify puede aprovechar AppSync en segundo plano

### Amplify

- Servicio: conjunto de herramientas y servicios para desarrollar y
desplegar aplicaciones web y móviles
- Suite con lo que se necesita para aplicaiones y desplegarlas
- Getionar autenticacion, alamcenmaiento, API, CICD, pubsub , análisis,
predicciones de IAML, moniotirzación, código fuente de AWS, git hub,
et

### Infrastructure Compose

- Diseñar y crear de manera visual apps serverless de forma rápida en
AWS
- Despliega código de infraestructura sin necesidad de ser un experto

- Configura como interactua los recursos en si
- Genera infraestructura como código, infraestructura como código usando
Cloud Formation
- Permite importar plantillas existentes de CloudFormation/SAM para
visualizarlas

### Device Farm

- Servicio gestionado que prueba apps web y móviles en navegadores de
escritorio, dispositevos móviles reales y tabletas
- Ejecutas pruebas simultaneas en varios dispositivos, accelara la
ejecución
- Posibilidad para ajustar dispoisiteo GPS, idioma, WIFI
- EXAMEN: COMO TESTEAR APPS CON DISPOSITVOS REALES

### Backup

- Servicio gestionado para administrar y automatizar copias de seguridad
de servicios
- Gestion Copias de seguridad bajo de manda y programadas
- Soporta point-in-time-recovery
- Peridodos de retencion, gestion del ciclo de vida, políticas de copoia
de seguridad
- Copias de seguridad entre regiones
- Copidas de seguridad entre cuentas, usando Organizations
- EXAMEN: COMO CREAR COPIAS DE SEGURIDAD

### Estrategias de recuperación antidesastres

- Copia de seguridad y restauración:

- Reconstruye todo desde cero
- Mas barata pero la más lenta

- Pilot light:

- Se mantiene una versión mínima para escalar rapidamente
- Precio mayor que la anterior pero menor que otras

- Warm Standby:

- Version completa de la app corriendo en AWS pero con un tamaño
    mínimo, recursos
- Reduce el tiempo de recuperación

- Mulsitio/HotSite:

- App completamente despelgada en múltiples ubicaciones ativas, alta
    dispnibilidad
- Opcion más costosa

### Configuracion típica de RD para implementaciones en el cloud

- Desplegar recursos en múltiples zonas de disponibilidad y regiones
- Failover = recuperación de fallos

### Elastic Disaster Recovery

- Recupera rápida y fácil info servidores, fisico, virtuales y en la
nube
- Replicación continua a nivle de bloque para tus servidores

### DataSync

- Mover gran cantidad de daros de las instalaciones cliente a AWS
- Se puede sincronizar a S3, incluyendo Glacier, EFS, FSx para Windows
- Tareas de replicación se puede programar cada hora, dia, semana
- EXAMEN: TAREA DE REPLICACION SON INCREMENTALES DESPUES DE LA PRIMERA
CARGA

### Estrategias de migracion a la nube

- Las 7R:

- Retire

    - Apagar o eliminar lo que no se necesita, a veces como resultado de
      rearquitectura
    - Ayuda a reducir superficie de ataque
    - Reducción costes, entre 10 y 20 por ciento
    -

- Retain

    - No migrar apps por momento
    - Factores como seguridad, cumplimiento de datos, rendimiento o
      dependencias non resultas
    - No hya valor de negocio para migrarr

- Relocate

    - Mover apps a la nube sin cambios en la arquitectura
    - Mover instancias EC2 a un VPC diferente, cuentas o regiones

- Rehost – lift and shift

    -  Migracion simple, mover tal cual está, meidante rehosting
    - Migrar máquinas fisicas o virtuales o desde otra nuvbe
    - No se realizan optimizaciones para la nueve, la app se migra tal
      cual está
    - Puede ser 30% en costes con respecto on-premises

- Replatform – lift and reshape

    - Migrar sin gestionar manualmente
    - Simplificando el despliegue
    - No se cambia la arquitectura pero si se aprovechn optimización de
      la nube como servicios gestionado, ahorra tiempo y dinero al
      reducir carga operativa

- Repurchase – drop and shop

    - Migrar a un producto difreten mientras se mueve a la nube
    - A menudo se migra a plataforma SaaS
    - Es más costoso a corto plazo pero rápido de implementar

- Refactor:

    - Rediseñar la app usando características cloud nativa
    - Por la necesidad de agregar funcionalidades y mejorar la
      escalabilidad, rendimiento, seguridad y agilidad
    - Pasar de una app monolitica a microservicios
    -

### Application Discovery Service

- Servicio para planificar los proyectos de migracion recopilando
información sobre loscentros de datos locales sobre sus depetendencias
y patrones de rendimiento
- Los datos de utilizacion de los servidores y la asignación de
dependencias son importantes para las migraciones

-

## Well Architected Framework

### Principios generales de orientacion

Ayuda a los arquitectos a crear una infraestructura segura y para esto
### hay que usar unos servicios específicos

De alto rendimiento

Resistente

Eficiente

- Dejar de adivinar tus necesidades de capacidad

- Prueba sistemas a escala de producción

- Automatizar para facilitar experimentacion arquitectonica

- Permitir arquitectura evolutivas:

- Diseñar en función requisites cambiantes

- Impulsar las arquitecturas utilizando datos

- Mejorar a través de días de juego, días de testeo

-

## Mejores Practicas En El Cloud

### Principios de diseño

- Escalabilidad:

- Vertical
- Horizontal

- Recursos desechables:

- Servidores desechables y facilmente configurables, no sean necesario
    conservar por mucho tiempo

- Automatizacion:

- Todos los proceos
- Serverless
- Infraestructura como servicio
- Autoescalado

- Acoplamiento:

- Dividir apps en componentes más pequeños y debilmente acoplados =
    microservicios o modulos
- Un cambio o fallo en componente no deberia afectar en cascada otros
    componente

- Servicios, no servidores:

- No utilizar EC2
- Servicios gestionados bases de datos, severless

### 6 V Well Architected Framework

- Excelencia operativa
- Seguridad
- Fiabilidad
- Eficiencia del rendimiento
- Optimizacion de costes
- Sostenibilidad

### 1\. Excelencia Operativa

- Capacidad de ejecutar y supervisar los sistemas para aportar valor al
negocio y mejorar continuamente los procesos y procedimientos de
soporte

- Principios de diseño

- Realizar operaciones como código – infraestructura como código –
    CloudFormation

- Anotar la documentacion – automatizar la creacion documentacion
    anotada después de cada construcción que se haga

- Realizar cambios frecuentes, pequeños y reversibles, para que en
    caso de cualquier falllo pueda ser revertido

- Perfecciona procedimientos de las operaciones con frecuencia

- Anticipate a los fallos

- Aprender de fallos operativos, documentarlo

- Servicios involucrados:

### - Preparar

      - Cloud formation
      - Config

    - Operar

      - CloudFormation
      - Config
      - Cloudtrail – registrar llamdas en API
      - Cloudwatch
      - x-ray

    - Evolucionar

      - CloudFormation
      - Codebuild
      - Codecommit
      - Codedeploy
      - Codepipeline

### 2.Seguridad

- Proteger información, sistemas y activos, y proporciona valor
empresarial mediante evaluaciones de riesgo y estrategias de
mitigacion

- Principios de diseño:

- implementar base sólida identidad:

    - Centralizar gestion de privilegios y reducir dependencia de
      credenciales a largo plazo
    - Principio de mínimo privilegio

- Habilitar trazabilidad:

    - Integrar logs y métricas con sis temas para responder y actuar
      automáticamente

- Aplicar seguridad en todas capas:

    - En red borde, VPC, subred, equilibrador de carga, cada instancia,
      sistema operativo y aplicación

- Automatizar mejores practicas de seguridad

- Preteccion datos en transite: cifrado y tokenizacion

- Mantener personas alejadas de datos: reducir o eliminar necesidad de
    acceso directo procesamiento manual de datos

- Preparacion eventos de seguridad: simulaciones de respuesta a
    incidentes

    - Uso herramientas automatizacion para aumentar velocidad de
      detección, investigación y recuperación
    - Modelo de responsabilidad compartida

- Servicio:

### - Gestion de identidades y accesos

      - Iam
      - Sts
      - MFA token
      - Organizacions

    - Controles deteccion

      - Config
      - Cloudtrail
      - Cloudwatch

    - Proteccion de infraestructura

      - CloudFront
##       - Vpc
      - Shield
      - Waf
      - Inspector

    - Proteccion datos

      - Kms
##       - S3
##       - Elb
##       - Ebs
##       - Rds
##       - IAM
      - CloudFormation
      - Cloudawatch events

### 3.Fiabilidad

- Capacidad sistema de recuperación de interrupción de infraestructura o
servicio

- Adquirir recursos informáticos dinamicamente satisfacer demanda y
mitigar interrupciones como

- Desconfiguración
- Problemas transites de red

- Principios de diseño:

- Probar procedimientos recuperación:

    - Automatización simular diferentes fallos o eventos de fallos
      anteriormente

- Recuperar automática de fallos

    - Anticipa y remedia fallos antes que se produzcan

- Escala horizontalmente para aumentar disponibilidad agregada al
    sistema

    - Distribuye peticiones entre múltiples recursos

- No adivinar capacidad:

    - Mantener nivel optimo para satisfacer demanda

- Gestionar cambio automatizacion :

    - Utilizar auto para realizar cambios de infraestructura

- Servicios:

### - Fundamentos

##       - IAM
      - Vpc
      - Quotas
      - Trusted advisor

    - Gestion del cambio

      - Auto Scaling
      - Cloudwatch
      - Cloud trail
      - Config

    - Gestion del fracaso

      - Backups
      - CloudFormation
##       - S3
      - S3 glacier

### 4.Eficiencia del rendimiento

- Capacidad usar recursos informaticos eficientemente para satisfacer
requisites sistema y mantener eficiencia a medadi que cambia demanda y
evoluciona tecnologias

- Principios de diseño:

- Democratizar tecnologias avanzadas:

    - Tecno avanzadas se convierten en servicios para centrarse en
      desarrollo de productos

- Global en minutos

    - Despliegue fácil en múltiples regiones

- Uso Arquitecturas sin servidor

    - Evitar carga de gestionar servidores

- Experimentar a menudo

    - Pruebas comparativas

- Simpatia mecanica

    - Conocer servicios de Amazon

- Servicios

- Seleccion:

    - Auto Scaling
    - Lambda
    - Elastic Block Store
    - S3
##     - Rds

- Revision:

    - CloudFormation
    - News blog

- Monitorizacion

    - Cloudwatch
    - Lambda

- Ventajas/desventajas:

    - RDS: Aurora
    - Elasticache - precio
    - Snowball – tiempo
    - CloudFront -

### 5.Optimizacion de costes

- Capacidad ejecutar sistemas para ofrecer valor empresarial al precio
más bajo

- Principios de diseño:

- Adopta modo de consumo

    - Paga por lo que usas

- Medir eficiencia global

    - Cloudwatch

- No gastar dinero en opracoines de datos fisico propio

    - AWS hace infraestructura

- Analizar y atribuir gastos:

    -  Identificacion del uso y coste del sistema
    - Medir retorno de inversion
    - Utilizar etiquetas

- Uso servicios gestionados y a nivel aplicación para reducir coste
    propiedad

- Servicios

- Conciencia del gasto

    - Budgets
    - Cost and usaget report
    - Cost explorer
    - Reserved instance reporting

- Recursos rentables

    - Spot instance
    - Reserved instance
    - S3 glacier

- Adecuación oferta y demanda

    - Auto Scaling
    - Lambda

- Optimizacoin tiempo

    - Trusted advisor
    - Cost and usage report

Sostenibilidad

- minimizar impacto ambiental de ejecución de cargas de trabajo en el
cloud

-principio de diseño:

-comprension de impacto:

indicadores de rendimiento, evalua mejoras

- establece objetivos sostenibilidad:

establece objetivos a largo plazo

Modela retorno inversion

- Anticipa y adpta nuevas ofertas hardware y software más eficinetes:

- Diseña flexibilidad de adoptar nuevas tecnologias

- Utiliza servicios gestionados

- Servocops compartidos, reducen cantidad infraestructura
- Ayudan a automatizar cantidad infraestructura
- Reduce cantidad energia o recursos necesario para utilizar tus
    servicio

- Servicios

- Autoescalada EC2
- Oferta serverless: Lambda o fargate
- Explorador de costes:
- Instancias EC2 o spot
- EFS-IA,
- S3 Glacier
- Volumenes EBS
- Configuraciones ciclo vida S3
- S3 intelligent tiering
- Administrador ciclo vida datos en Amazon
- Lectura local
- Escribura global RDS Read Replicas
- Aurora Global DB,
- DynamoDB Global Tale
- Cloud front

### Herramienta AWS Well-Architected

- Herramienta gratuita para revisar arquiteturas con el marco de los 6
pilares

Customer Carbon Footprint Tool

- Herramienta de seguimiento, medicion, revision y proyection de
emisiones de carbono
- Ayuda a cumplir propios objetivos sostenibilidad

Cloud Adoption Framework CAF

- Servicio construir y ejecutar un plan integral para transformación
digital meidante uso innovador AWS

- Transformacion hacia el cloud

- Agrupa capacidades en seis perspectivas

- Negocio
- Personas
- Gobierno
- Plataforma
- Seguridad
- Operacion

- Dominios de transformacion

- Tecnologia

- Proceso: automatizar y optimizacoinoperacoines empresariales

    - Nuevas plataformas de datos y análisis
    - Uso machine learning para mejorar experiencia

- Organizacion

    - Reimaginando modelo oprativo

      - Orgniza equipo
      - Metodos agiles

- Producto

    - Nuevas propuestas de valor, modelos de negocioa

- Fases de transformacion

- Envision:

    - vision y oprtuniadad de la nube

- Align:

    - Gaps o carencia y crea plan de accion

- Launch

    - Implementar proyectos piloto en produccoin

- Scale

    -  Amplia adopción cloud a toda la organzacion

### Dimensionar correcto EC2

- Hay muchos instancias pero hay que elegir el que más convenga
- Adecuar tipos y tamaños de instancia a los requisites de requerimiento
y capacidad de carga de trabajo al menor coste posible
