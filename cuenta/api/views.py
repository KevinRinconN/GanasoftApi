from rest_framework.viewsets import ModelViewSet
from cuenta.models import Cuenta
from cuenta.api.serializers import CuentaSerializer

from django_filters.rest_framework import DjangoFilterBackend

from cuenta.api.filters import CuentaFilter
from cuenta.api.permissions import isAdminOrReadOnly

class CuentaApiViewSet(ModelViewSet):
    
    permission_classes = [isAdminOrReadOnly]
    
    
    serializer_class = CuentaSerializer
    queryset = Cuenta.objects.all()
    
    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250001)
    
    filter_backends = [DjangoFilterBackend]
    
    filterset_class = CuentaFilter
    
    
    
    
    
    
    
    