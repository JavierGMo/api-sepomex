from src import ma

#Schema para poder parsear los datos a un json

class ColoniaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'idmunicipio', 'idcp')