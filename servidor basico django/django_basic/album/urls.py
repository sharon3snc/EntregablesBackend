from django.urls import path
from . import views

urlpatterns= [
    #path("", views.api_cancion),
    path("<int:pk>", views.AlbumRetrieveAPIView.as_view()),
    path("create", views.AlbumListCreateAPIView.as_view()),
    path("update/<int:pk>", views.AlbumUpdateAPIView.as_view()),
    path("destroy/<int:pk>", views.AlbumDestroyAPIView.as_view()),
]
