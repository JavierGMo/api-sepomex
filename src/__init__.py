import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def create_app(settingsModule):
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)
    from .routes.home import homeBP
    app.register_blueprint(homeBP)
    from .routes.estado import estadoBP
    app.register_blueprint(estadoBP)
    from .routes.municipio import municipioBP
    app.register_blueprint(municipioBP)
    from .routes.colonia import coloniaBP
    app.register_blueprint(coloniaBP)
    return app