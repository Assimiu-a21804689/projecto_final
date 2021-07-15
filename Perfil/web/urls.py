from django.urls import path

from Perfil.views import home

urlpatterns= [
    path("", home, name="homa")
]