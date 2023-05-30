from django.db import models
from user.models import User

from django.core.validators import MinValueValidator


class Bovine(models.Model):
    distinctiveTrait = models.CharField(max_length=100, null=False, blank=False)
    breed = models.CharField(max_length=100, null=False, blank=False)
    is_female = models.BooleanField(default=False)
    dateOfBirth = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return f"Rasgo distintivo: {self.distinctiveTrait} - Raza: {self.breed} - Es hembra?: {self.is_female}"


class Record(models.Model):
    dateOfRecord = models.DateTimeField(auto_now_add=False)
    WeightRecord = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    bovine = models.ForeignKey(Bovine, on_delete=models.CASCADE)

class BovineHeat (models.Model):
    
    start_date = models.DateTimeField(auto_now_add=False)
    term = models.DateTimeField(auto_now_add=False)
    is_current = models.BooleanField(default=False)
    bovine = models.ForeignKey(Bovine, on_delete=models.CASCADE)
