from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sign_up (models.Model):
    user = models.CharField("Usuario", max_length=50)
    email = models.EmailField("Correo electrónico", max_length=254, unique=True)
    phone = models.CharField("Teléfono", max_length=50)
    password = models.CharField("Contraseña", max_length=50)
    passwordConfirm = models.CharField("Confirmar contraseña", max_length=50)

class Datos_personales(models.Model):
    TIPO_DOCUMENTO = [
        ("TI", "Tarjeta de identidad"),
        ("CC", "Cedula de ciudadania"),
        ("CE", "Cedula de extranjería"),
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
    DISCAPACIDAD =[
        ("AUDITIVO","Auditivo"),
        ("VISUAL", "Visual"),        
        ("MOVILIDAD", "Movilidad"),
        ("NINGUNO", "Ninguno"),
    ]
    NIVEL_EDUCATIVO=[
        ("PRIMARIA", "Básica Primaria"),
        ("SECUNDARIA", "Básica secundaria"),
        ("BACHILLER", "Bachiller académico"),
        ("TECNICO", "Técnico"),
        ("TECNOLOGO", "Tecnólogo"),
        ("PROFESIONAL","Profesional"),
    ]
    SI_NO=[
        ("SI", "Si"),
        ("NO", "No"),
    ]
    DISPOSITIVOS=[
        ("TABLET","Tablet"),
        ("COMPUTADOR", "Computador"),
        ("SMARTPHONE", "Smartphone"),
        ("OTRO", "Otro"),
    ]    
    REGIMEN =[
        ("CONTRIBUTIVO","Contributivo"),
        ("SUBSIDIADO", "Subsidiado"),
    ]
    
    tipo_documento = models.CharField("Tipo de documento", max_length=50, choices=TIPO_DOCUMENTO)
    documento = models.IntegerField("Numero de documento")
    nombre =models.CharField("Nombre completos", max_length=50)
    apellidos = models.CharField("Apellido", max_length=50)
    genero = models.CharField("Genero", max_length=50 , choices=GENERO)
    telefono = models.CharField("Teléfono", max_length=12)
    email = models.EmailField("Correo electrónico",blank=True)
    municipio = models.CharField("Municipio de residencia", max_length=50)
    direccion = models.CharField("Dirección", max_length=50)
    localidad = models.CharField("Barrio - Localidad", max_length=50)
    fecha_nacimiento = models.DateField("Fecha de nacimiento", auto_now=False)
    etnia = models.CharField("Etnia", max_length=50, choices= ETNIA)
    discapacidad = models.CharField("Condición de discapcidad", max_length=50, choices=DISCAPACIDAD)
    estrato = models.CharField("Estrato socieconómico", max_length=50)
    educacion = models.CharField("Nivel educativo alcanzado", max_length=50, choices=NIVEL_EDUCATIVO)
    acceso = models.CharField("Acceso a dispositivos tecnológicos", max_length=10, choices = SI_NO)
    dispositivos= models.CharField("Dispositivos con acceso" , max_length = 50, blank=True, null=True, choices=DISPOSITIVOS)
    conectividad = models.CharField("Conectividad a internet", max_length = 10, choices= SI_NO )
    regimen = models.CharField("Regimen de afiliación", max_length =20, choices=REGIMEN)
    
    

    
    