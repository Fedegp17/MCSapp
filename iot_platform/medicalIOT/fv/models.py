from datetime import datetime
from django.db import models

# Create your models here.

class Hospital(models.Model):
    Nombre= models.CharField(max_length=30)
class Medico(models.Model):
    Nombre= models.CharField(max_length=30)
    Apellido= models.CharField(max_length=30)
class Paciente(models.Model):
    Nombre= models.CharField(max_length=30)
    Apellido= models.CharField(max_length=30)
    Ingreso= models.DateField(datetime)