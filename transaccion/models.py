from django.db import models
from cuenta.models import Cuenta
# Create your models here.
class Categoria(models.Model):
    
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    
    
    def __str__(self):
        return f"categoria: {self.nombre} - descripcion: {self.descripcion}"


class Transaccion(models.Model):
    
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.CharField(max_length=100, default=0, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaccion: {self.nombre} - descripcion: {self.descripcion}"

