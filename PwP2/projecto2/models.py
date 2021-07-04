from django.db import models

# Create your models here.




class Encomendar(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    dataNascimento = models.DateField();
    telefone = models.IntegerField()
    email = models.EmailField()
    morada = models.CharField(max_length= 40)
    codigo_postal = models.CharField(max_length= 50)
    quantidade = models.IntegerField()
    cor = models.IntegerField()

    def __str__(self):
        return f"{self.nome} {self.apelido}"

class Sobre (models.Model):
    sugestao = models.TextField()

    def __str__(self):
        return self.sugestao[:30]

class Contacto (models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=40)
    email = models.EmailField()
    contacto = models.IntegerField()

    def __str__(self):
        return self.nome + " " + self.email

class Contact (models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=40)
    email = models.EmailField()
    contacto = models.IntegerField()
    dataNasc = models.CharField(max_length=8)


    def __str__(self):
        return self.nome + " " + self.email