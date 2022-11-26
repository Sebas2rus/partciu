from django import forms 
from .models import Sign_up, Datos_personales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
        
    class Meta:        
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class Infor_personal(forms.ModelForm):
    email = forms.EmailField(help_text="Ingrese el mismo correo electrónico con el que se registró", label="Correo electrónico")
    fecha_nacimiento = forms.DateTimeField(label="Fecha de nacimiento", required=True, help_text="Año-mes-dia")
    
    class Meta:        
        model = Datos_personales
        fields = [
            'tipo_documento','documento','nombre','apellidos','email','telefono','genero','municipio','direccion',
            'localidad','fecha_nacimiento','etnia','discapacidad','estrato','educacion',
            'acceso','dispositivos','conectividad','regimen'
        ]    
                
            

    