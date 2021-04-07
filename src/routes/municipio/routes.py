from flask import current_app, jsonify
from . import municipioBP

@municipioBP.route("/municipios/")
def getAllMunicipios():
    return 'municipios'