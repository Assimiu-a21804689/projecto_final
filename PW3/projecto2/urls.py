from django.urls import path

from . import  views

from .views import contactos_view, login_view

app_name = "projecto2"
urlpatterns = [
    path('', views.home_view, name="home"),
    path('telefone', views.telefone_view, name="telefone"),
    path('tablet', views.tablet_view, name="tablet"),
    path('computador', views.computador_view, name="computador"),
    path('encomenda', views.encomenda_view, name="encomenda"),
    path('informacao', views.informa_view, name= "informacao"),
    path('sobre', views.sobre_view, name = "sobre"),
    path('contacto', views.contacto_view, name="contacto"),

    path('principal', contactos_view, name="principal"),
    path('login', login_view, name="login"),
]