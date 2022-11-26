from django.urls import path
from . import views

urlpatterns = [
    path( "<str:username>/certificadoPDF", views.certificado_sondeo, name="certificado_sondeo"),
    path("generar_certificado", views.certificado_sondeoPDF, name ="generar_certificado")
]
