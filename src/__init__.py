import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

ma = Marshmallow()

def create_app(settingsModule):
    
    app = Flask(__name__, instance_relative_config=True)

    #Config app
    print("settings module: {}".format(settingsModule))
    app.config.from_object(settingsModule)

    # Base de datos
    db.init_app(app)
    #Para los schemas
    ma.init_app(app)
    
    #Blueprints para las rutas
    from .routes.home import homeBP
    app.register_blueprint(homeBP)

    from .routes.estado import estadoBP
    app.register_blueprint(estadoBP)

    from .routes.municipio import municipioBP
    app.register_blueprint(municipioBP)

    from .routes.colonia import coloniaBP
    app.register_blueprint(coloniaBP)

    from .routes.codigopostal import codigoPostalBP
    app.register_blueprint(codigoPostalBP)

    return app