from django.urls import path
from . import views
app_name = "contenido"

urlpatterns = [
    path('discos/', views.discos, name="discos"),
    path('discos/nuevo/', views.nuevo_disco, name="nuevo_disco"),
    path('libros/', views.libros, name="libros"),
    path('remeras/', views.remeras, name="remeras"),
]
