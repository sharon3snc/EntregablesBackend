from django.db import models

class Album (models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    