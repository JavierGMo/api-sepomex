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
- export FLASK_APP="app"
- export FLASK_ENV="development"
- export APP_SETTINGS_MODULE="config.local"

Windows
- set "FLASK_APP=app"
- set "FLASK_ENV=development"
- set "APP_SETTINGS_MODULE=config.local"

## Clona el proyecto

Tendras que clonar este proyecto con `git clone https://github.com/JavierGMo/api-sepomex`


# Configurar la URI de la bd

En el archivo local.py que esta en la carpeta config modificar la url con su usuario de base de datos y su respectica contraseña: `SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/sepomex'`

## Como usar este proyecto en UBUNTU 18.04.5 LTS
- Estar en la carpeta de api-sepomex
- Crear el entorno virtual desde la terminal: `python3 -m venv venv`, si manda un error ejecutar el siguiente comando en terminal: `sudo apt install python3-venv`
- Activar el entorno virtual, desde la terminal ejecutar el siguiente comando: `. venv/bin/activate`
- Instalar dependencias, en la terminal ejecutar lo siguiente: `pip install -r requirements.txt`

## Como usar en windows
- Estar en la carpeta de api-sepomex
- Crear el entorno virtual desde cmd: `py -3 -m venv venv`
- Activar el entorno virtal : `.\venv\Scripts\activate.bat`
- Instalar dependencias, en la terminal ejecutar lo siguiente: `pip install -r requirements.txt`


## Correr la app en local ya sea para ubuntu o windows
`flask run`


# Acceder a rutas desde navegador o postman o similares a postman

- `http://127.0.0.1:5000/colonias/` Todas las colonias
- `http://127.0.0.1:5000/municipios/` Todos los municipios
- `http://127.0.0.1:5000/estados/` Todos los estados
- `http://127.0.0.1:5000/codigospostales/` Todos los codigos postales

- `http://127.0.0.1:5000/colonia/id` Colonia por id, el id tiene que ser numerico
- `http://127.0.0.1:5000/municipio/id` Colonia por id, el id tiene que ser numerico
- `http://127.0.0.1:5000/estado/id` Estado por id, el id tiene que ser numerico
- `http://127.0.0.1:5000/codigopostal/id` Codigo postal por id, el id es el codigo postal XD

- `http://127.0.0.1:5000/colonianombre/nombre` Colonia por nombre, regresa una lista con nombres similares de colonias
- `http://127.0.0.1:5000/municipionombre/nombre` Colonia por nombre, regresa una lista con nombres similares de municipios
- `http://127.0.0.1:5000/estadonombre/nombre` Estado por id, regresa una lista con nombres similares de estados