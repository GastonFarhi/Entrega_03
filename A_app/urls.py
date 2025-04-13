from django.urls import path
from . import views
app_name = "contenido"

urlpatterns = [
    path('discos/', views.discos, name="discos"),
    path('libros/', views.libros, name="libros"),
    path('remeras/', views.remeras, name="remeras"),
]
