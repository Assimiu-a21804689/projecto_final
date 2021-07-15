from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    nome = models.CharField(max_length=40)
    apelido = models.CharField(max_length=40)
    username = models.EmailField("E-mail", max_length=40, unique=True)
    dataNascimento = models.DateField(null=True)


class Foto(models.Model):
    foto = models.ImageField(blank=True, upload_to="meus/ficheiros/")
    titulo = models.CharField(max_length= 50)
    descricao = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, models.CASCADE)