from flask import current_app, jsonify, request
from . import municipioBP
from src.schemas.municipioschema import MunicipioSchema
from src.models.municipio import Municipio


@municipioBP.route("/municipios/", methods=['Get'])
def getAllMunicipios():
    municipiosSchema = MunicipioSchema(many=True)
    municipios = Municipio.getAllMunicipio()
    return municipiosSchema.jsonify(municipios)


@municipioBP.route("/municipio/<int:id>", methods=['Get'])
def getMunicipioById(id):
    municipioSchema = MunicipioSchema()
    municipio = Municipio.getEstadoById(id)
    return municipioSchema.jsonify(municipio)

@municipioBP.route("/municipio/", methods=['Post'])
def createMunicipio():
    id = request.json['id']
    nombre = request.json['nombre']
    idestado = request.json['idestado']
    nuevoMunicipio = Municipio(id, nombre, idestado)
    nuevoMunicipio.createMunicipio()

    return jsonify({
        'ok' : True,
        'message' : 'Municipio creaod'
    })