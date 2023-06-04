from rest_framework import serializers
from .models import Cancion

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cancion
        fields = ("titulo", "cantante", "duracion", "album")
