from django.shortcuts import render
from sondeos.models import Respuesta_Sondeo
from register.models import Datos_personales
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

# Create your views here.

def certificado_sondeo(request, username=None):
    respuesta = Respuesta_Sondeo.objects.filter(usuario = request.user.id)
    usuario = Datos_personales.objects.filter(email = request.user.email)
    return render(request, "certificadoPDF.html", {"respuestas":respuesta, "usuarios":usuario})

def certificado_sondeoPDF(request):
    respuestas = Respuesta_Sondeo.objects.all()
    usuario = Datos_personales.objects.filter(email = request.user.email)
    template_path = 'certificadoPDF.html'
    context = {'respuestas':respuestas, "usuarios":usuario}
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    