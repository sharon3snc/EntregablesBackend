from django.urls import path
from . import views
from .views import Album_APIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('album_viewset', Album_APIViewSet)

urlpatterns= [
    #path("", views.api_cancion),
    path("<int:pk>", views.AlbumRetrieveAPIView.as_view()),
    path("create", views.AlbumListCreateAPIView.as_view()),
    path("update/<int:pk>", views.AlbumUpdateAPIView.as_view()),
    path("destroy/<int:pk>", views.AlbumDestroyAPIView.as_view()),
] + router.urls

