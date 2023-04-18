from rest_framework import serializers
from cuenta.models import Cuenta
from user.api.serializers import UserSerializer

class CuentaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    class Meta:
        model = Cuenta
        fields = ['id', 'usuario', 'nombre', 'tipo_cuenta', 'saldo_disponible']