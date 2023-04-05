from django import forms

class AutorFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    dni=forms.CharField()
    email=forms.EmailField()

class LibroFormulario(forms.Form):
    titulo=forms.CharField()
    autor=forms.CharField()
    isbn=forms.CharField()

class BibliotecaFormulario(forms.Form):
    nombre=forms.CharField()
    ubicacion=forms.CharField()
    cant_sucursales=forms.IntegerField()
    
