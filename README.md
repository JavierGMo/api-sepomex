# API REST SEPOMEX con Flask y MySQL
## Toma los datos de SEPOMEX para poder hacer consultas con respecto al estado, municipio y colonia
## Este proyecto fue creado en UBUNTU 18.04.5 LTS
## Requisitos: 
- Python 3.6.9
- LAMP para poder usar MySQL
- Flask 1.1.2
- UBUNTU 18.04.5 LTS

## Variables de entorno
Crear las siguientes variables de entorno:
Ubuntu:
- export FLASK_APP="src"
- export FLASK_ENV="development"
- export APP_SETTINGS_MODULE="config.local"

## Como usar este proyecto en UBUNTU 18.04.5 LTS
1.- Estar en la carpeta de APISEPOMEX
2.- Crear el entorno virtual desde la terminal: `python3 -m venv venv`, si manda un error ejecutar el siguiente comando en terminal: `sudo apt install python3-venv`
3.- Activar el entorno virtual, desde la terminal ejecutar el siguiente comando: `. venv/bin/activate`
4.- Instalar Flask, desde la terminal ejecutar el siguiente comando: `pip install Flask`
5.- Instalar Marshmallow, ejecute lo siguiente en la linea de comandos: `comando`
6.- marshmallow-sqlalchemy
7.- Instalar Flask-Sqlalchemy, ejecute lo siguiente en la linea de comandos: `Comando`
8.- drivers mysql

Correr la app en local
`flask run`
