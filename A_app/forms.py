from django import forms
from .models import Disco

class DiscoFrom(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ["nombre", "artista", "year"]
