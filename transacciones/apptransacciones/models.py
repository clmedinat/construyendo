from django.db import models

class Usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    imagen=models.CharField(max_length=100, null=True)
    usuario=models.CharField(max_length=45)
    password=models.CharField(max_length=20)
    roles=models.CharField(max_length=30, default='user')
    fecha_creado=models.DateTimeField(auto_now_add=True)

class Empresas(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    nit=models.IntegerField()
    ciudad=models.CharField(max_length=50, null=True)
    direccion=models.CharField(max_length=50, null=True)
    telefono=models.CharField(max_length=15)
    sector=models.CharField(max_length=40, null=True)
    fecha_creado=models.DateTimeField(auto_now_add=True)

class Empleados(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    telefono=models.CharField(max_length=12)
    empresa=models.ForeignKey(Empresas, on_delete=models.RESTRICT, null=False)
    fecha_creado=models.DateTimeField(auto_now_add=True)

class Transacciones(models.Model):
    id=models.AutoField(primary_key=True)
    concepto=models.CharField(max_length=40)
    monto=models.IntegerField()
    tipo=models.CharField(max_length=40)
    usuario=models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=False)
    empresa=models.ForeignKey(Empresas, on_delete=models.RESTRICT, null=False)
    fecha_creado=models.DateTimeField(auto_now_add=True)
