from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html') 



""" Interfaz de los libros """
def libros(request):
    libro = Libro.objects.all()
    
    return render(request, 'libros/index.html', {'libros':libro})

def crear_libro(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')