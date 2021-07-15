from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#class CriaPerfil(CreateView):
    #model = Perfil
    #fields = ["comenta"]
   # template_name = "home.html"
   # def form_valid(self, form):
       # pass
        #form.instance.usuario = self.request.user
        #url = super().form_valid(form)
        #return url




class Usuario(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = "__all__"

