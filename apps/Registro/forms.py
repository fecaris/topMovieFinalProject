from django import forms
from .models import Actor, Pelicula

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombreCompleto']

        labels = {
            'nombreCompleto': 'Nombre Completo',
        }
        widgets = {
            'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
        }
