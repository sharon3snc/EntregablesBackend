from django.test import TestCase
from rest_framework.test import APIClient
from .models import Album
from rest_framework import status

class AlbumViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.album1 = Album.objects.create(nombre='album1',  anio=1999)
        self.album2 = Album.objects.create(nombre='album2', anio=1999)
    
    def test_restringir_put(self):
        url = f'/album/album_viewset/{self.album1.id}/'
        data = {'nombre':'album1', 'album':2000}

        response= self.client.put(url, data, format='json')
        self.assertEqual(response.status_code,405)

    def test_update_non_existing_album(self):
        non_existing_id= self.album2.id + 1
        url= f'/album/update/{non_existing_id}/'
        data= {'nombre': 'Nuevo nombre', 'anio': 2023}

        response= self.client.put(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
