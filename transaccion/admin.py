from django.contrib import admin
from transaccion.models import Transaccion, Categoria

@admin.register(Transaccion)
class transaccionAdmin(admin.ModelAdmin):
    list_display = ['cuenta', 'categoria', 'monto', 'descripcion','create_at']

@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'descripcion']
