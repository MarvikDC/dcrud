from django import forms
from django.forms import fields
from .models import Equipo

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ['equipo_serie', 'equipo_marca', 'equipo_descripcion']
        

