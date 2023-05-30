from rest_framework import serializers
from ahorro.models import Ahorro
from cuenta.api.serializers import CuentaSerializer

class AhorroSerializer(serializers.ModelSerializer):
    #cuenta = CuentaSerializer()
    class Meta:
        model = Ahorro
        fields = ['nombre', 'descripcion', 'monto_obj', 'fecha_fin', 'cuenta']
    