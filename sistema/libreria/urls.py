from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('',views.inicio, name = 'inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    #""" Interfaz de los libros """
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_libro, name='crearlibros'),
    path('libros/editar', views.editar, name='editar'),
    path('crear/sesion', views.crear_sesion, name = 'crearsesion'),
    path('cerrar/sesion', views.cerrar_sesion, name = 'cerrarsesion'),
    path('iniciar/sesion', views.iniciar_sesion, name = 'iniciarsesion'),    
]
