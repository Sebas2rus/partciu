from django.shortcuts import render, redirect
from .models import Respuesta, Tema, Sondeo, Respuesta_Sondeo
from django.contrib.auth.models import User
from register.models import Datos_personales
from .forms import RespuestaForm, respuesta_sondeoForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def tema (request, id_pregunta=None):
    form = RespuestaForm()
    pregunta1 = Tema.objects.filter(id = id_pregunta)    
    respuesta1 = Respuesta.objects.all()
    usuario = User.objects.filter(username = request.user.username)    
    if pregunta1:
        registrado = Datos_personales.objects.filter(email= request.user.email)
        if not registrado:
            return redirect('datos_personales')            
            
        contestado = Respuesta.objects.filter(pregunta = id_pregunta, usuario = request.user.id)
        
        if contestado  : 
            return redirect("contestado")    
    
        if request.method =="POST":
            formRespuesta = RespuestaForm(request.POST)
            if formRespuesta.is_valid():
                campoRespuesta = formRespuesta.cleaned_data['respuesta']    
                preguntaa = Tema.objects.get(id = id_pregunta)                                            
                guardarRespuesta = Respuesta(pregunta = preguntaa , respuesta = campoRespuesta, usuario = request.user)
                guardarRespuesta.save()
                messages.success(request, f'Se registró correctamente su respuesta')            
                return redirect('index')
            else:            
                messages.error(request, f'Error al completar el formulario')
                
        return render(request, 'pregunta.html', {'respuestas': respuesta1, "preguntas": pregunta1, "form": form})    
    else:
        return redirect('index')
    
    
def contestado (request):
    return render(request, 'contestado.html')

def contestar_sondeo (request, id_sondeo=None):    
    
    
    sondeo = Sondeo.objects.filter(id = id_sondeo)
    item =["", "respuesta1", "respuesta2", "respuesta3", "respuesta4", "respuesta5"]
    usuario = User.objects.filter(username = request.user.username)    
    
    if sondeo:
        registrado = Datos_personales.objects.filter(email= request.user.email)
        if not registrado:
            return redirect('datos_personales')     
        
        contestado = Respuesta_Sondeo.objects.filter(sondeo = id_sondeo, usuario = request.user.id)        
        if contestado  : 
            return redirect("contestado")                   
        
        if request.method =="POST":            
            respuesta1 = request.POST.get('respuesta1', False)            
            respuesta2 = request.POST.get('respuesta2')            
            respuesta3 = request.POST.get('respuesta3')
            respuesta4 = request.POST.get('respuesta4')
            respuesta5 = request.POST.get('respuesta5')
            sondeo_id = Sondeo.objects.get(id = id_sondeo)
            guardar_respuesta = Respuesta_Sondeo(sondeo=sondeo_id, respuesta1=respuesta1, respuesta2=respuesta2, respuesta3=respuesta3, respuesta4=respuesta4, respuesta5=respuesta5, usuario=request.user)
            guardar_respuesta.save()
            messages.success(request, f'Se registró correctamente la respuesta al sondeo')            
            return redirect('index')
        elif request.method == "GET":
            return render(request, 'contestar_sondeo.html', {"sondeos":sondeo, "item": item})        
        else:            
            messages.error(request, f'Error al completar el formulario')
    
        return render(request, 'contestar_sondeo.html', {"sondeos":sondeo, "item": item})
    
    