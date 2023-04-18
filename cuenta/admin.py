from django.contrib import admin
from cuenta.models import Cuenta

@admin.register(Cuenta)
class cuentaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nombre', 'tipo_cuenta', 'saldo_disponible']
