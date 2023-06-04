from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class AlbumRetrieveAPIView(generics.RetrieveAPIView):
    queryset= Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset= Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumUpdateAPIView(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDestroyAPIView(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
