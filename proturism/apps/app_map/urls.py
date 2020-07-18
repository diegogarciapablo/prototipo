from django.urls import path

from .views import MostrarMapa

urlpatterns = [
    	path('',MostrarMapa,name='mapa')
]