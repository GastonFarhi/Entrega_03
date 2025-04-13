from django.shortcuts import render
from .models import Disco, Remera, Libros


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
