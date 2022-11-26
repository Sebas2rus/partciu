from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from register.models import Datos_personales
from sondeos.models import Sondeo, Tema, Parametros, Respuesta_Sondeo
from django.utils import timezone

# Create your views here.

def usuario (request, username= None):    
    usuario = User.objects.filter(username = request.user.username)    
    if usuario:
        registrado = Datos_personales.objects.filter(email= request.user.email)
        if registrado:
            return render(request, 'usuario.html', {'usuarios': usuario})        
        else:
            return redirect('datos_personales')
    
    
def usuario_sondeo(request, username = None):
    usuarios = User.objects.filter(username = request.user.username)
    sondeos = Sondeo.objects.all()[:4]
    usuarioActual = Datos_personales.objects.filter(email=request.user.email)
    fecha_actual = timezone.now
    return render(request, 'usuarioSondeo.html', {"usuarios":usuarios,"sondeos": sondeos, "fecha_actual":fecha_actual, "usuarioActual": usuarioActual})

def usuario_pregunta(request, username = None):
    usuarios = User.objects.filter(username = request.user.username)
    temas = Tema.objects.all()[:4]
    fecha_actual = timezone.now
    return render(request, 'usuarioPregunta.html', {'usuarios': usuarios, "temas": temas, "fecha_actual":fecha_actual})


def sondeos_contestados(request, username = None):
    contestado=True
    usuarios = User.objects.filter(username = request.user.username)
    respuestas = Respuesta_Sondeo.objects.filter(sondeo = request.user.id)
    fecha_actual = timezone.now
    return render(request, "usuarioContestados.html", {"respuestas":respuestas, "fecha_actual":fecha_actual, "contestado" : contestado, "usuarios":usuarios })