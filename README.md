Python 3.8.2

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
- *db* - Base de datos
- *app* - Aplicación en Django (no NGINX)
- *redis* - Agente de mensajes para Celery
- *celery* - Cola de tareas distribuidas
- *flower* - Herramienta de monitoreo para Celery

`docker-compose -f docker-compose.dev.yml up -d`


La primera vez que se ejecuta el comando se construyen las imagenes de los contenedores a partir del template, posterior a esto solo se refresca la información. Adicionalmente, aplica las migraciones y carga los fixtures. El proceso completo tarda alrededor de 20 minutos.
Para reconstruir una imagen se debe especificar `--build` junto al nombre o los nombres de los servicios.
Ejemplo para reconstruir la base de datos y el agente de mensajes para Celery:
`docker-compose -f docker-compose.dev.yml up -d --build db redis`


* Dependencias
Para configuración local Docker
* Configuración de la base de datos
* Cómo ejecutar pruebas
* Instrucciones de implementación (Deployment)

### Pautas de contribución ###

* Fixtures
Todos los parametros debe contener información real y esta debe ser cargada por fixtures

*Generar fixtures*
`python manage.py dumpdata app.modelname --indent 4 > fixtures/file_name.json`

*Cargar uno a uno*
`python manage.py loaddata fixtures/model_name.json --app app.model_name`

*Carga completa (metodo personalizado)*
`python manage.py load-fixtures`

* Pruebas de escritura
* Revisión de código
* Otras pautas

### Con quien hablo? ###

* Propietario o administrador del repositorio
* Otro contacto de la comunidad o del equipo
