from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class Sala(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=2)

