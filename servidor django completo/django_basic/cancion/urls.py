from django.urls import path
from . import views

urlpatterns= [
    path("", views.api_cancion),
    path("<int:pk>", views.CancionRetrieveAPIView.as_view()),
    path("create", views.CancionListCreateAPIView.as_view()),
    path("update/<int:pk>", views.CancionUpdateAPIView.as_view()),
    path("destroy/<int:pk>", views.CancionDestroyAPIView.as_view()),
]

