from django.shortcuts import render, redirect
from .models import Disco, Remera, Libros
from .forms import DiscoForm, LibroForm, RemeraForm


# Create your views here.
def discos(request):
    lista_discos = Disco.objects.all()
    return render(request, "A_app/discos.html",
                  {"lista_discos": lista_discos})


def remeras(request):
    lista_remeras = Remera.objects.all()
    return render(request, "A_app/remeras.html",
                  {"lista_remeras": lista_remeras})


def libros(request):
    lista_libros = Libros.objects.all()
    return render(request, "A_app/libros.html",
                  {"lista_libros": lista_libros})


def nuevo_disco(request):
    if request.method == "POST":
        formulario = DiscoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("contenido:discos")
    else:
        formulario = DiscoForm()
    return render(request, "A_app/submit_disco.html", {"formulario": formulario})


def libro_nuevo(request):
    if request.method == "POST":
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("contenido:libros")
    else:
        formulario = LibroForm()
    return render(request, "A_app/submit_libro.html", {"formulario": formulario})


def remera_nueva(request):
    if request.method == "POST":
        formulario = RemeraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("contenido:remeras")
    else:
        formulario = RemeraForm()
    return render(request, "A_app/submit_remera.html", {"formulario": formulario})
