from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Home(models.Model):
    clientes = "CLIENTES"
    empleados = "EMPLEADOS"
    horas_a_cargar = "CARGAR HORAS CLIENTES"


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    cuit_empresa = models.IntegerField()
    nombre_contacto = models.CharField(max_length=100)
    cargo_contacto = models.CharField(max_length=100)
    cobro_mensual_honorarios = models.FloatField(default=0.0)
    

class HorasCliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_de_trabajo = models.DateField()
    horas_trabajadas = models.FloatField(default=0.0)
    