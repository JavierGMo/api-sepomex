from flask import current_app, jsonify
from . import coloniaBP
@coloniaBP.route("/colonias/")
def getAllColonias():
    return 'colonias'
