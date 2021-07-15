from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import conetar, disconetar,  carregarFoto, confirmacao, editar, apagar, carregarFoto, registar, principal, index, visualFoto

app_name ="TesteUsuario"

urlpatterns = [

    path("registar", registar, name="registar"),
    path("carregar?fotos!", carregarFoto, name="carregarFoto"),
    path("principal", principal, name="principal"),
    path("index", index, name = "index"),
    path("visual<int:id>", visualFoto, name="visualFoto"),
    path("editar<int:id>", editar, name="editar"),
    path("apagar<int:id>", apagar, name="apagar"),
    path("confirma<int:id>", confirmacao, name="confirmacao"),
    path("conectar", conetar, name="conetar"),
    path("disconetar", disconetar, name="disconetar")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
