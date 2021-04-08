from flask import current_app, request, jsonify
from src.models.estado import Estado
from . import estadoBP
from src.schemas.estadoschema import EstadoSchema

#Los schemas nos facilitan para poder usar JSON en las respuestas


@estadoBP.route("/estados/")
def getAllEstado():
    estadosSchema = EstadoSchema(many=True)
    estados = Estado.getAllEstados()
    print("Estados en json")
    
    return estadosSchema.jsonify(estados)

@estadoBP.route("/estado/<int:id>")
def getEstadoById(id):
    estadoSchema = EstadoSchema()
    estado = Estado.getEstadoById(id)

    return estadoSchema.jsonify(estado)

@estadoBP.route("/estadonombre/<string:nombre>")
def getEstadoByName(nombre):
    estadosSchema = EstadoSchema(many=True)
    estados = Estado.getEstadoByName(nombre)

    return estadosSchema.jsonify(estados)

@estadoBP.route("/estado/", methods=['Post'])
def createEstado():
    id = request.json['id']
    nombre = request.json['nombre']
    nuevoEstado = Estado(id, nombre)
    nuevoEstado.createEstado()
    return jsonify({
        'ok' : True,
        'message' : 'Estado creado'
    })
