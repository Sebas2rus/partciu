from django import forms 
from .models import Respuesta, Respuesta_Sondeo
from django.forms import Textarea, ModelForm

class RespuestaForm(forms.ModelForm):
    
    class Meta:
        model= Respuesta
        fields = ['respuesta']
        widgets = {
            'respuesta': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        
class respuesta_sondeoForm(forms.ModelForm):
    
    class Meta:
        model = Respuesta_Sondeo
        fields="__all__"
        
    