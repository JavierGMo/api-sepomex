import os
from flask import Flask
from src import create_app
#from flask_marshmallow import Marshmallow
#from flask_sqlalchemy import SQLAlchemy
#from database.db.db import DB

settingsModule = os.getenv('APP_SETTINGS_MODULE')

app = create_app(settingsModule)


