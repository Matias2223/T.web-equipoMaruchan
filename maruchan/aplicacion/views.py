from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import usuarios

# Acceso a vistas 
def inicio(request):
    return HttpResponse("<h1>Bienvenido</h1>")

# Visualizacion de elementos 
def index(request):
    usuario = usuarios.objects.all()
    return render(request, 'index.html',{'Usuarios': usuario})

def sesion(request):
    return render(request, 'paginas/sesion.html',{})

def registro(request):
    return render(request, 'paginas/registro.html',{})

def crear(request):
    return render(request, 'crud/crear.html',{})

def eliminar(request, id):
    usuario = usuarios.objects.get(id_user = id)
    usuario.delete()
    return render(request, 'index.html',{})

def insertUser(request):
    name = request.POST['name']
    usuario = request.POST['user']
    pas = request.POST['pass']
    rolu = request.POST['rol']
    cel = request.POST['tel']
    correo = request.POST['email']  
    us = usuarios(nombre = name, user = usuario, contra = pas, rol = rolu, tel = cel, email = correo)
    us.save()
    return redirect('../index')

def editar(request, id):
    usuario = usuarios.objects.get(id_user = id)
    return render(request, 'crud/editar.html',{'usuarios': usuario})

def updateUser(request):
    id_u = request.POST['id']
    name = request.POST['name']
    usuario = request.POST['user']
    pas = request.POST['pass']
    cel = request.POST['tel']
    correo = request.POST['email']  
    usuarios.objects.filter(id_user=id_u).update(nombre = name, user = usuario, contra = pas, tel = cel, email = correo)
    return redirect('../index')