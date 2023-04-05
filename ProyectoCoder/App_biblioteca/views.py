from django.http import HttpResponse
from django.shortcuts import render
from App_biblioteca.models import *
from App_biblioteca.forms import *



def inicio(self):
    return render(self, "inicio.html")

def autor(self):
    return render(self, "autor.html")

def biblioteca(self):
    return render(self, "biblioteca.html")

def libro(self):
    return render(self, "libro.html")

def autorFormulario(request):
    if request.method == "POST":
        miFormularioautor=AutorFormulario(request.POST)
        print(miFormularioautor)
        if miFormularioautor.is_valid():
            informacion=miFormularioautor.cleaned_data
            autor=Autor(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"])
            autor.save()
            return render(request, "inicio.html")
    else:
        miFormularioautor=AutorFormulario()
    return render(request, "autorFormulario.html", {"miFormularioautor": miFormularioautor})

            
    
 

def libroFormulario(request):
    if request.method=="POST":
        miFormulario_libro=LibroFormulario(request.POST)
        print(miFormulario_libro)
        if miFormulario_libro.is_valid():
            informacion=miFormulario_libro.cleaned_data
            libro=Libro(titulo=informacion["titulo"], autor_dni=informacion["autor_dni"], isbn=informacion["isbn"] )
            libro.save()
            return render(request, "inicio.html")
    else:
        miFormulario_libro=LibroFormulario()
    return render(request, "libroFormulario.html",{"miFormulario_libro": miFormulario_libro})

def bibliotecaFormulario(request):
     if request.method=="POST":
        miFormulario_biblioteca=BibliotecaFormulario(request.POST)
        print(miFormulario_biblioteca)
        if miFormulario_biblioteca.is_valid():
            informacion=miFormulario_biblioteca.cleaned_data
            biblioteca=Biblioteca(nombre=informacion["nombre"], ubicacion=informacion["ubicacion"], cant_sucursales=informacion["cant_sucursales"] )
            biblioteca.save()
            return render(request, "inicio.html")
     else:
        miFormulario_biblioteca=BibliotecaFormulario()
     return render(request, "bibliotecaFormulario.html", {"miFormulario_biblioteca": miFormulario_biblioteca})

def busquedaAutor(request):
     return render(request, "App_biblioteca/busquedaAutor.html")

def buscar(request):
    if request.GET["apellido"]:
        apellido=request.GET["apellido"]
        autores=Autor.objects.filter(apellido=apellido)
        return render(request, "App_biblioteca/resultadoBusqueda.html", {"autores":autores, "apellido":apellido})
    else:
        respuesta="No se envio datos"
    return HttpResponse(respuesta)
     


       
       