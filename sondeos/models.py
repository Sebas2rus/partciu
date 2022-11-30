from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tema (models.Model):
    pregunta = models.CharField("Pregunta - Tema", max_length=100)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=timezone.now)        
    
    class Meta:
        verbose_name_plural="Temas"
        ordering = ['-fecha_creacion']        
    
    def __str__(self):
        return self.pregunta
    
class Respuesta (models.Model):
    pregunta = models.ForeignKey(Tema, on_delete=models.CASCADE)        
    respuesta = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pregunta)


class Parametros(models.Model):
    PARAMETROS_EDAD = [
        ("MENOR QUE", "Menor a "),
        ("MAYOR QUE", "Mayor a "),
    ]
    GENERO =[
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("IT", "Intersexual"),
        ("I", "Indefinido"),
        ("N","Prefiero no decir") ,       
    ]
    ETNIA =[
        ("NINGUNA","Ninguno"),
        ("AFRO","Afro"),
        ("INDIGENA","Indigena"),
        ("RAIZAL","Raizal"),
        ("PALENQUERO", "Palenquero"),
        ("GITANO", "Gitano"),
    ]
    rango_p = models.CharField("Rango de edad", max_length=50, choices=PARAMETROS_EDAD, blank=True)
    edad_p = models.IntegerField("Edad" , blank=True)
    genero_p = models.CharField("Genero", max_length=50, choices=GENERO , blank=True)
    etnia_p = models.CharField("Etnia", max_length=50, choices=ETNIA, blank=True)

class Sondeo(models.Model):
    nombre_s = models.CharField("Nombre del sondeo", max_length=50)    
    descripcion_s = models.CharField("Descripción del sondeo", max_length=500)    
    categoria_s = models.CharField("Categoria", max_length=50)
    fecha_publicacion_s = models.DateTimeField("Fecha y hora de publicación", default=timezone.now)
    fecha_cierre_s = models.DateTimeField("Fecha y hora de cierre", auto_now=False)    
    id_pregunta = models.ManyToManyField(Tema) 
    id_parametro = models.ForeignKey(Parametros, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField("Icono del sondeo", upload_to="static/db" )
    
    def __str__(self):
        return f'{self.nombre_s}'
    
class Respuesta_Sondeo (models.Model):
    
    sondeo = models.ForeignKey(Sondeo, on_delete=models.CASCADE)    
    respuesta1 = models.CharField("respuesta", max_length=250)
    respuesta2 = models.CharField("respuesta" , blank=True, null=True, max_length=250)
    respuesta3 = models.CharField("respuesta", blank=True, null=True, max_length=250)
    respuesta4 = models.CharField("respuesta", blank=True, null=True, max_length=250)
    respuesta5 = models.CharField("respuesta", blank=True, null=True, max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField("Fecha", auto_now=True)
     