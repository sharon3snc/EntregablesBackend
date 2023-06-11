from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class AlbumRetrieveAPIView(generics.RetrieveAPIView):
    queryset= Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes= [permissions.DjangoModelPermissions]

class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset= Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes= [permissions.DjangoModelPermissions]

class AlbumUpdateAPIView(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDestroyAPIView(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class Album_APIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def update(self, request, *args, **kwargs):
        return Response(status= status.HTTP_405_METHOD_NOT_ALLOWED)

