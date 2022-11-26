from django.shortcuts import render, redirect
from .forms import Infor_personal, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def body (request):
    emailActual = request.user.email
    
    return render(request, 'body.html', {"email": emailActual})

def signup (request):
    form = UserRegisterForm()    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)     
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']            
            messages.success(request, f'Usuario {usuario} creado')                                    
    else:
        form = UserRegisterForm()    
    return render(request, "register.html", {'form':form})


def datos_personales(request):
    personal = Infor_personal()    
    if request.method == "POST":
        personal = Infor_personal(request.POST)
        if personal.is_valid() and  request.user.is_authenticated:                        
            personal.save()
            messages.success(request, f'Datos almacenados correctamente')            
            return redirect('index')
        else:            
            messages.error(request, f'Error al completar el formulario')
    return render(request,"datos_personales.html", {"form" : personal})