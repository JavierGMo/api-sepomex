from flask import current_app, jsonify
from . import estadoBP


@estadoBP.route("/estados/")
def getAllEstado():
    print(Estado.getAllEstados())
    return 'estados'