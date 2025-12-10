from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50, choices=[
        ('admin', 'Administrador'),
        ('usuario', 'Usuario Regular'),
    ], default='usuario')
    ciudad = models.CharField(max_length=100, blank=True, null=True)