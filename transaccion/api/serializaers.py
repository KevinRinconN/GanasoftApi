from rest_framework import serializers
from transaccion.models import  Transaccion,Categoria
from cuenta.api.serializers import CuentaSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre', 'tipo', 'descripcion']
        

class TransaccionSerializer(serializers.ModelSerializer):
    #cuenta = CuentaSerializer()
    #categoria = CategoriaSerializer()
    class Meta:
        model = Transaccion
        fields = ['cuenta', 'categoria', 'monto', 'descripcion','create_at']
        

