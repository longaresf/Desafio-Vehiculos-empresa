from django.contrib import admin
from vehiculos_app.models import Vehiculo, Chofer, RegistroContabilidad

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(RegistroContabilidad)