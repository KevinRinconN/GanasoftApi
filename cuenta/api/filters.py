from django_filters import NumberFilter, FilterSet
from cuenta.models import Cuenta

class CuentaFilter(FilterSet):
    saldo = NumberFilter(field_name='saldo_disponible', lookup_expr='gt')
    
    class Meta:
        model = Cuenta
        fields = ['saldo']