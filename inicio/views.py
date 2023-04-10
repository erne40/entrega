from django.shortcuts import render, redirect
from inicio.models import Libro
from inicio.forms import CreacionLibroFormulario, BuscarLibro

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

def buscar_libro(request):
    nombre_a_buscar = request.GET.get('titulo', None)
    
    if nombre_a_buscar:
        libros = Libro.objects.filter(titulo__icontains=nombre_a_buscar)
    else:
        libros = Libro.objects.all()

    #libros = Libro.objects.all()
    formulario_busqueda = BuscarLibro()
    return render(request, 'inicio/buscar_libro', {'libros': libros, 'formulario': formulario_busqueda})


