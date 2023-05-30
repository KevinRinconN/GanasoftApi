from rest_framework.routers import DefaultRouter
from transaccion.api.views import TransaccionApiViewSet, CategoriaApiViewSet

router_transaccion = DefaultRouter()
router_transaccion.register(prefix='transaccion', basename='transaccion', viewset=TransaccionApiViewSet)

router_categoria = DefaultRouter()
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaApiViewSet)