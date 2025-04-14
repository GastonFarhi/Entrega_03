from django.shortcuts import render, redirect
from .models import Disco, Remera, Libros
from .forms import DiscoFrom


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
        formulario = DiscoFrom(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
    else:
        formulario = DiscoFrom()
    return render(request, "A_app/submit_disco.html", {"formulario": formulario})
