from rest_framework.routers import DefaultRouter
from ahorro.api.views import AhorroApiViewSet

router_ahorros = DefaultRouter()

router_ahorros.register(prefix='ahorro', basename='ahorro', viewset=AhorroApiViewSet)