from django.db import models

# Create your models here.
class Actor(models.Model):
    nombreCompleto = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreCompleto
    
class Pelicula(models.Model):
    actor = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    fecha_salida = models.DateField()

    def __str__(self):
        return self.nombre