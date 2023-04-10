from django.shortcuts import render, redirect
from inicio.models import Libro
from inicio.forms import CreacionLibroFormulario

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def libro(request):
    if request.method == "POST":
        formulario = CreacionLibroFormulario(request.POST)
    
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data

            libro = Libro(titulo= datos_correctos['titulo'], autor= datos_correctos['autor'], publicacion= datos_correctos['publicacion'], editorial= datos_correctos['editorial'])
            libro.save()
            
            return redirect('libro')

    formulario = CreacionLibroFormulario()
    return render(request, 'inicio/libro.html', {'formulario':formulario})