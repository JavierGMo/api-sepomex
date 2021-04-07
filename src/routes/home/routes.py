from flask import current_app, jsonify
from . import homeBP


@homeBP.route("/")
def getAllEstado():
    return 'hola'