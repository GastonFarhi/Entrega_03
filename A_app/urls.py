from django.urls import path
from . import views
app_name = "contenido"

urlpatterns = [
    path('discos/', views.discos, name="discos"),
    path('agg_disco/', views.nuevo_disco, name="prueba"),
    path('libros/', views.libros, name="libros"),
    path('remeras/', views.remeras, name="remeras"),
]
