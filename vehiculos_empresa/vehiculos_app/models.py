from django.db import models

# Create your models here.

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.OneToOneField('Vehiculo', blank=False, null=False, on_delete=models.CASCADE, max_length=6)

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, null=False)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=20, null=False)
    year = models.IntegerField(null=False)

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(max_length=10, null=False)
    vehiculo_id = models.OneToOneField('Vehiculo', blank=False, null=False, on_delete=models.CASCADE, max_length=6)


# conductor_id = models.ForeignKey('Conductor', blank=False, null=False, on_delete=models.CASCADE, max_length=9)
# decimal_places = 2