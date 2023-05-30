from rest_framework.viewsets import ModelViewSet
from bovine.models import Bovine
from bovine.api.serializers import BovineSerializer

from django_filters.rest_framework import DjangoFilterBackend

from cuenta.api.filters import CuentaFilter
from cuenta.api.permissions import isAdminOrReadOnly

class BovineApiViewSet(ModelViewSet):
    
    #permission_classes = [isAdminOrReadOnly]
    
    
    serializer_class = BovineSerializer
    queryset = Bovine.objects.all()
    
