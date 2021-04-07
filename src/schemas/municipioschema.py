from src import ma

class MunicipioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'idestado')