from django.db import models
from album.models import Album

class Cancion (models.Model):
    titulo = models.CharField(max_length=200)
    cantante = models.CharField(max_length=200)
    duracion = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    
    def __str__(self):
        return self.titulo
    
