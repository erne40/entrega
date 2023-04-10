from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path('libro/', views.libro, name= 'libro'),
    path('buscar/', views.buscar_libro, name= 'buscar'),
]
