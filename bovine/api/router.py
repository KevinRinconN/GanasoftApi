from rest_framework.routers import DefaultRouter
from bovine.api.views import BovineApiViewSet

router_bovine = DefaultRouter()

router_bovine.register(prefix='bovine', basename='bovine', viewset=BovineApiViewSet)