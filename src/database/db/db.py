from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class DB:
    db = None
    app = None
    def __init__(self, app: Flask):
        #Inicializamos la base de datos
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://javier:password12345@localhost/sepomexdb'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
    def getDB(self):
        return self.db