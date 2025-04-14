from django.urls import path
from . import views
app_name = "contenido"

urlpatterns = [
    path('discos/', views.discos, name="discos"),
    path('agg_disco/', views.nuevo_disco, name="agg_disco"),
    path('libros/', views.libros, name="libros"),
    path('agg_libro/', views.libro_nuevo, name="agg_libro"),
    path('remeras/', views.remeras, name="remeras"),
    path('agg_remera/', views.remera_nueva, name="agg_remera"),
]
