from django.contrib import admin
from ahorro.models import Ahorro

# Register your models here.
@admin.register(Ahorro)
class ahorroAdmin(admin.ModelAdmin):
    list_display = ['cuenta', 'nombre', 'descripcion', 'monto_obj', 'fecha_fin', 'create_at']
    