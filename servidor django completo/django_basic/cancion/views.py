from django.shortcuts import render
from rest_framework import generics
from .models import Cancion
from album.models import Album
from .serializers import CancionSerializer
from album.serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import choice

class CancionRetrieveAPIView(generics.RetrieveAPIView):
    queryset= Cancion.objects.all()
    serializer_class = CancionSerializer

class CancionListCreateAPIView(generics.ListCreateAPIView):
    queryset= Cancion.objects.all()
    serializer_class = CancionSerializer

class CancionUpdateAPIView(generics.UpdateAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class CancionDestroyAPIView(generics.DestroyAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

@api_view (['GET'])
def api_cancion(request):
    
    album = choice(Album.objects.all())
    canciones = Cancion.objects.filter(album=album)
    
    album_serializer = AlbumSerializer(album)
    canciones_serializer = CancionSerializer(canciones, many=True)

    data = {
        'album': album_serializer.data,
        'canciones': canciones_serializer.data,
    }
    
    return Response(data)
