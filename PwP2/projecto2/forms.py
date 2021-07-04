from django.forms import ModelForm
from .models import Encomendar
from .models import Sobre
from .models import Contacto
class EncomendarForms(ModelForm):
    class Meta:
        model = Encomendar
        fields = "__all__"

class SobreForms(ModelForm):
    class Meta:
        model = Sobre
        fields = "__all__"

class ContactForms(ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"