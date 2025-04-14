from django import forms
from .models import Disco, Remera, Libros


class DiscoFrom(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ["nombre", "artista", "year"]

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ["autor", "titulo", "year"]

class RemeraForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ["disenio", "talle"]