from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def base(request):
    return render({'user':User})

def inicio(request):
    return render(request, 'paginas/inicio.html' )

def crear_sesion(request):
    if request.method == 'GET':
        return render(request, 'registrate/crear_sesion.html',{
            'crear_sesion':UserCreationForm
        })
    else:
        print(request.POST)
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'] )
                user.save()
                login(request,user)
                return redirect('inicio')
            except:
                return render(request, 'registrate/crear_sesion.html',{
                'crear_sesion':UserCreationForm,
                'error':'El usuario ya esta creado'
        })
        return render(request, 'registrate/crear_sesion.html',{
            'crear_sesion':UserCreationForm,
            'error_clave':'Las claves no coinsiden'
        })
    
def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'registrate/iniciar_sesion.html',{
            'iniciar_sesion_form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'registrate/iniciar_sesion.html',{
            'iniciar_sesion_form': AuthenticationForm,
            'error':'La clave es incorrecta o cuenta no encontrada'
        })
        else:
            login(request, user)
            return redirect('inicio')
    
    
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


    
    
    
    
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
