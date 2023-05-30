from rest_framework.viewsets import ModelViewSet
from transaccion.models import Transaccion,Categoria
from transaccion.api.serializaers import TransaccionSerializer, CategoriaSerializer

from django_filters.rest_framework import DjangoFilterBackend

from cuenta.api.filters import CuentaFilter
from cuenta.api.permissions import isAdminOrReadOnly

class TransaccionApiViewSet(ModelViewSet):
    
    #permission_classes = [isAdminOrReadOnly]
    
    
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()
    
    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250001)
    
    filter_backends = [DjangoFilterBackend]

class CategoriaApiViewSet(ModelViewSet):
    
    #permission_classes = [isAdminOrReadOnly]
    
    
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    
    # queryset = Cuenta.objects.filter(saldo_disponible__gte=250001)
    
    filter_backends = [DjangoFilterBackend]