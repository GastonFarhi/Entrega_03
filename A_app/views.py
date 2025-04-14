from django.shortcuts import render, redirect
from .models import Disco, Remera, Libros
from .forms import DiscoFrom


# Create your views here.
def discos(request):
    lista_discos = Disco.objects.all()
    return render(request, "A_app/discos.html",
                  {"lista_discos": lista_discos})


def nuevo_disco(request):
    if request.method == "POST":
        form = DiscoFrom(request.POST)
        if form.is_valid():
            disco = form.save(commit=False)
            if request.user.is_authenticated:
                disco.artista = request.user
                disco.save()
                return redirect("A_Main:index")
            else:
                form.add_error(None, "NOSE BRO ERROR")

    else:
        form = DiscoFrom()
    return render(request, "A_app/submit_disco.html", {"form": form})


def remeras(request):
    lista_remeras = Remera.objects.all()
    return render(request, "A_app/remeras.html",
                  {"lista_remeras": lista_remeras})


def libros(request):
    lista_libros = Libros.objects.all()
    return render(request, "A_app/libros.html",
                  {"lista_libros": lista_libros})
