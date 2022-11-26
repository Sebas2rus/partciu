from django.contrib import admin
from .models import Tema, Respuesta, Parametros, Sondeo,Respuesta_Sondeo

# Register your models here.

admin.site.register(Tema)

# La siguiente clase permite visualizar los datos como si fueran una tabla, podemos elegir los 
# Campos que vamos a mostrar
class Respuesta_admin(admin.ModelAdmin):
    list_display= ('pregunta', 'respuesta', 'usuario')
    fields = ('Pregunta', 'Respuesta', 'Usuario')
    
admin.site.register(Respuesta, Respuesta_admin)

class Sondeo_admin(admin.ModelAdmin):
    list_display = ('nombre_s', 'fecha_publicacion_s', 'fecha_cierre_s')    

admin.site.register(Sondeo, Sondeo_admin)

admin.site.register(Parametros)
admin.site.register(Respuesta_Sondeo)