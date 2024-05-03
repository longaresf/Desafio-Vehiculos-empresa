from vehiculos_app.models import Vehiculo, Chofer, RegistroContabilidad
from django.db import models

def crear_vehiculo(patente, marca, modelo, year):
    nuevo_vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)
    return nuevo_vehiculo

def crear_chofer(rut, nombre, apellido, activo, patente):
    id_vehiculo_id = Vehiculo.objects.get(pk=patente)
    nuevo_chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, vehiculo_id=id_vehiculo_id)
    return nuevo_chofer

def crear_registro_contable(fecha_compra, valor, patente):
    id_vehiculo_id = Vehiculo.objects.get(pk=patente)
    nuevo_registro_contable = RegistroContabilidad.objects.create(fecha_compra=fecha_compra, valor=valor, vehiculo_id=id_vehiculo_id)
    return nuevo_registro_contable

def deshabilitar_chofer(rut):
    desabilitar_chofer = Chofer.objects.filter(pk=rut).update(activo=False)
    return desabilitar_chofer

def deshabilitar_vehiculo(patente):
    vehiculo_id = Vehiculo.objects.get(pk=patente)
    desabilitar_vehiculo = Chofer.objects.filter(pk=vehiculo_id).update(activo=False)
    return desabilitar_vehiculo

def habilitar_chofer(rut):
    habilitar_chofer = Chofer.objects.filter(pk=rut).update(activo=True)
    return habilitar_chofer

def habilitar_vehiculo(patente):
    vehiculo_id = Vehiculo.objects.get(pk=patente)
    habilitar_vehiculo = Chofer.objects.filter(pk=vehiculo_id).update(activo=True)
    return habilitar_vehiculo

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.filter(pk=patente)
    for c in vehiculo:
        print(f"[Patente: {c.patente}] => [Marca: {c.marca}] => [Modelo: {c.modelo}] => [Año del Año: {c.year}]")

def obtener_chofer(rut):
    chofer = Chofer.objects.filter(pk=rut)
    for c in chofer:
        print(f"[Rut: {c.rut}] => [Nombre: {c.nombre}] => [Apellido: {c.apellido}] => [Activo: {c.activo}] => [Creacion Registro: {c.creacion_registro}]")

def asignar_chofer_a_vehiculo(patente, rut):
    id_vehiculo_id = Vehiculo.objects.get(pk=patente)
    vehiculo_chofer = Chofer.objects.filter(pk=rut).update(vehiculo_id=id_vehiculo_id)
    return vehiculo_chofer

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    
    for c in vehiculos:
        print(f"[Nombre Chofer: {c.chofer.nombre}] => [Marca: {c.marca}] => [Fecha de Compra: {c.registrocontabilidad.fecha_compra}] => [Año Vehiculo: {c.year}]")
