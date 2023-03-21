from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # email = models.EmailField(unique=True)
    # web_site = models.CharField(max_length=255, blank=True)

