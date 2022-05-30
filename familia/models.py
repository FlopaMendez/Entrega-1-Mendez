from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()

class Home(models.Model):
    clientes = "CLIENTES"
    empleados = "EMPLEADOS"

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    cuit_empresa = models.IntegerField()
    nombre_contacto = models.CharField(max_length=100)
    cargo_contacto = models.CharField(max_length=100)
    cobro_mensual_honorarios = models.FloatField(default=0.0)
    