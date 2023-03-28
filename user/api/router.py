from django.urls import path
from user.api.views import RegistrerView

urlpatterns = [
    path('auth/register', RegistrerView.as_view())
]