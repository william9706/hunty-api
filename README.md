Python 3.8.15

# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Para qué es este repositorio? ###

* Sumario rápido
* Versión
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Cómo me configuro? ###

* Resumen de la configuración
* Configuración
Contenedores
- *app* - Aplicación en FastAPI no bd

`docker compose`


La primera vez que se ejecuta el comando se construyen la imagene del contenedor a partir del template, el proceso tarda alrededor de 2 minutos.
Para reconstruir la imagen se debe especificar `build` despues del `docker compose`.
Ejemplo para reconstruir la aplicacion FastApi:
`docker compose build`


* Dependencias
Para configuración local Docker
* para correr la aplicacion solo debe ejecutar el comando `docker compose up`
* Cómo ejecutar pruebas.
Para ejecutar las pruebas unitarias debe correr el siguiente comando `docker compose run fast-api pytest`
### Instrucciones de implementación ###
para que la aplicacion funcione correctamente primero debes crear vacantes despues usuarios y por ultimo empresas en las colecciones de postman ya esta todo listo para que la aplicacion funcione correctamente.



### Con quien hablo? ###

* Propietario o administrador del repositorio
* Otro contacto de la comunidad o del equipo
