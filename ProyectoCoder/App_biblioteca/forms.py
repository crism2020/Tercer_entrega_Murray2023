from django import forms
from .models import *

class AutorFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    dni=forms.CharField()
    email=forms.EmailField()

class LibroFormulario(forms.Form):
    titulo=forms.CharField()
    isbn=forms.CharField()
    autor_dni = forms.ModelChoiceField(queryset=Autor.objects.all(), empty_label="Seleccionar autor", required=True)



   

class BibliotecaFormulario(forms.Form):
    nombre=forms.CharField()
    ubicacion=forms.CharField()
    cant_sucursales=forms.IntegerField()
    
