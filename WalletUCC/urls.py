"""WalletUCC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cuenta.api.router import router_cuentas
from ahorro.api.router import router_ahorros
from transaccion.api.router import router_transaccion, router_categoria
from bovine.api.router import router_bovine

schema_view = get_schema_view(
   openapi.Info(
      title="Api WalletUCC",
      default_version='v1',
      description="Esta es la documentacion de la Api Rest de WalletUcc",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('user.api.router')),
    path('api/', include(router_cuentas.urls)),
    path('api/', include(router_ahorros.urls)),
    path('api/', include(router_transaccion.urls)),
    path('api/', include(router_categoria.urls)),
    path('api/', include(router_bovine.urls))
]
