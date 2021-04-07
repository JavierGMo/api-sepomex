# API REST SEPOMEX con Flask y MySQL
## Toma los datos de SEPOMEX para poder hacer consultas con respecto al estado, municipio y colonia
## Este proyecto fue creado en UBUNTU 18.04.5 LTS
## Requisitos: 
- Python 3.6.9
- LAMP para poder usar MySQL o XAMPP
- Flask 1.1.2
- UBUNTU 18.04.5 LTS o windows 10

## Variables de entorno
Crear las siguientes variables de entorno:
Ubuntu:
- export FLASK_APP="src"
- export FLASK_ENV="development"
- export APP_SETTINGS_MODULE="config.local"

Windows
- set "FLASK_APP=app"
- set "FLASK_ENV=development"
- set "APP_SETTINGS_MODULE=config.local"


## Como usar este proyecto en UBUNTU 18.04.5 LTS
- Estar en la carpeta de APISEPOMEX
- Crear el entorno virtual desde la terminal: `python3 -m venv venv`, si manda un error ejecutar el siguiente comando en terminal: `sudo apt install python3-venv`
- Activar el entorno virtual, desde la terminal ejecutar el siguiente comando: `. venv/bin/activate`
- Instalar Flask, desde la terminal ejecutar el siguiente comando: `pip install Flask`
- Instalar Marshmallow, ejecute lo siguiente en la linea de comandos: `comando`
- marshmallow-sqlalchemy
- Instalar Flask-Sqlalchemy, ejecute lo siguiente en la linea de comandos: `Comando`
- drivers mysql

## Como usar en windows
- Crear el entorno virtual desde cmd: `py -3 -m venv venv`
- Activar el entorno virtal : `.\venv\Scripts\activate.bat`


Correr la app en local
`flask run`
