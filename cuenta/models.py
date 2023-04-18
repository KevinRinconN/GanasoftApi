from django.db import models
from user.models import User

from django.core.validators import MinValueValidator


class Cuenta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tipo_cuenta = models.CharField(max_length=100, null=False, blank=False)
    saldo_disponible = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cuenta: {self.nombre} - Saldo disponible: {self.saldo_disponible}"


