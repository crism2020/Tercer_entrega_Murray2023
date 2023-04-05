from django.db import models

class Autor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
        return f'{self.dni}'

    
class Libro(models.Model):
    titulo=models.CharField(max_length=20)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn=models.CharField(max_length=20)



class Biblioteca(models.Model):
    nombre=models.CharField(max_length=20)
    ubicacion=models.CharField(max_length=15)
    cant_sucursales=models.IntegerField()



# Create your models here.
