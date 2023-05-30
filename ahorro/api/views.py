from rest_framework.viewsets import ModelViewSet
from ahorro.models import Ahorro
from ahorro.api.serializaers import AhorroSerializer

from django_filters.rest_framework import DjangoFilterBackend

from cuenta.api.filters import CuentaFilter
from cuenta.api.permissions import isAdminOrReadOnly

class AhorroApiViewSet(ModelViewSet):
    
    #permission_classes = [isAdminOrReadOnly]
    
    
    serializer_class = AhorroSerializer
    queryset = Ahorro.objects.all()
    
    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250001)
    
    filter_backends = [DjangoFilterBackend]

    