from django.db import models
from cuenta.models import Cuenta

from django.core.validators import MinValueValidator


class Ahorro(models.Model):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    monto_obj = models.IntegerField( default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    fecha_fin = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name='Cuenta')
    
    def __str__(self):
        return f"Ahorro: {self.nombre} - descripcion: {self.descripcion}"


