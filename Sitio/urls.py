from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('mapa-sitio/', views.mapa_sitio, name='mapa_sitio'),
    path('buscar/', views.buscar, name='buscar'),
    path('maquillaje/', views.maquillaje, name='maquillaje'),
    path('404/', views.buscar, name='404'),
]