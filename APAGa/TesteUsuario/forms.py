from django.contrib.auth import forms
from django.forms import ModelForm, widgets
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User, Foto


class CriaUsuario(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ["nome", "apelido", "username",  "dataNascimento"]
        

class CriarComentario(ModelForm):
    class Meta:
        model = Foto
        fields = ["foto", "titulo",  "descricao"]



