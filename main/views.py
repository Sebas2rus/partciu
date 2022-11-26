from django.shortcuts import render, redirect
from sondeos.models import Tema, Respuesta, Sondeo, Respuesta_Sondeo
from register.models import Datos_personales
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def index(request):
    temas = Tema.objects.all()[:3]
    sondeos = Sondeo.objects.all()[:4]
    fecha_actual = timezone.now
    return render(request, 'index.html', {'temas': temas, "sondeos":sondeos, "fecha_actual":fecha_actual})

def busqueda(request):
    fecha_actual = timezone.now
    encontrados=False
    if request.method =="POST":
        buscar = request.POST.get("buscar")
        sondeos = Sondeo.objects.filter(
            Q(nombre_s__icontains = buscar) |
            Q(descripcion_s__icontains = buscar) |
            Q(categoria_s__icontains = buscar)).distinct()[:4]

        if sondeos:
            encontrados=True        
            return render (request, "busquedas.html", {"sondeos" : sondeos, "fecha_actual":fecha_actual, "buscar":buscar,"encontrados":encontrados})
    
        else:
            sondeos = Sondeo.objects.all()[:2]
            return render(request, "busquedas.html", {"sondeos" : sondeos, "fecha_actual":fecha_actual,"buscar":buscar, "encontrados":encontrados})
        
        
def validar_certificado(request):
    
    if request.method == "POST":
        id_sondeo = request.POST.get("id_certificado")
        nombre = request.POST.get("nombre") 
        apellido = request.POST.get("documento")
        if id_sondeo:
            sondeos = Respuesta_Sondeo.objects.filter(id = id_sondeo)        
            email = ""
            for sondeo in sondeos:
                email = sondeo.usuario.email
            usuarios = Datos_personales.objects.filter(email = email)
            return render (request, "validar_certificado.html", {"sondeos":sondeos, "nombre": nombre, "apellido":apellido, "usuarios":usuarios})
        else:
            return render (request, "validar_certificado.html")
    elif request.method =="GET":
        return render (request, "validar_certificado.html")