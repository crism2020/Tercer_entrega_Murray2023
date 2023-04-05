from django.urls import path
from App_biblioteca.views import *

urlpatterns=[
    path("", inicio, name="Inicio"),
    path("autor/", autor, name="Autor"),
    path("biblioteca/", biblioteca, name="Biblioteca"),
    path("libro/", libro, name="Libro"),
    #path("libroFormulario/", libroFormulario, name="LibroFormulario"),
    #path("autorFormulario/", autorFormulario, name="AutorFormulario"),
    #path("bibliotecaFormulario/", bibliotecaFormulario, name="BibliotecaFormulario"),
    path("busquedaAutor/", busquedaAutor, name="BusquedaAutor"),
    path("buscar/", buscar, name="Buscar"),
]