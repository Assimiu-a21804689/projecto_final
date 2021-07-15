from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from TesteUsuario.forms import CriaUsuario, CriarComentario
from TesteUsuario.models import Foto, User


def registar (request):
    usuario = CriaUsuario(request.POST or None)
    if request.POST:
        if usuario.is_valid():
            usuario.save()
            email = usuario.cleaned_data["username"]
            senha1 = usuario.cleaned_data["password1"]

            usuario = authenticate(username=email, password=senha1)
            login(request, usuario)
            print("OLA")
            return render(request, "principal.html")

    return render(request, "registar.html",  {"form": usuario})



def carregarFoto (request):
    if request.POST:
        post = CriarComentario(request.POST)
        fotos = request.FILES.getlist("imagem")
        descricao = request.POST["descricao"]
        titulo = request.POST["titulo"]
        #Preenche campo de formulario que vem de request e valida
        post.instance.foto = fotos
        post.instance.usuario = request.user
        post.instance.descricao = descricao
        post.instance.titulo = titulo
        if post.is_valid():
            for foto in fotos:
                post = CriarComentario(request.POST)
                post.instance.foto = foto
                post.instance.usuario = request.user
                post.instance.descricao = descricao
                post.instance.titulo = titulo
                post.save()
            fotos = Foto.objects.all()
            context = {"fotos": fotos}
            return render(request, "principal.html", context)
    return render(request, "carregarFoto.html")

def principal (request):
    if request.POST:
        query = request.POST["pesquisa"]
        fotos = Foto.objects.all().filter(titulo=query)
        
        print("ola")
        context = {"fotos": fotos}
        return render(request, "principal.html", context)

    fotos = Foto.objects.all()
    context = {"fotos": fotos}
    return render(request, "principal.html", context)

def index (request):
    if request.POST:
        query = request.POST["pesquisa"]
        fotos = Foto.objects.all().filter(titulo = query)
        context = {"fotos": fotos}
        return render(request, "principal.html", context)
    return render(request, "index.html")


def visualFoto (request, id):
    foto = Foto.objects.all().get(pk=id)
    context = {"fotoVisual": foto}
    return render(request, "visualFoto.html", context)


def editar (request, id):
    intancia = Foto.objects.all().get(pk=id)
    foto = CriarComentario(instance=intancia)
    if request.POST:
        descricao = request.POST["descricao"]
        titulo = request.POST["titulo"]

        fotos = Foto.objects.all()
        foto = CriarComentario(instance=intancia)
        foto.cleaned_data = intancia

        foto.instance.titulo = titulo
        foto.instance.descricao = descricao
        foto.save()
        return render(request, "principal.html", {"fotos": fotos})

    return render(request,"editar.html", {"fotoEditar": foto, "foto": intancia})

def confirmacao(request, id):
    foto = Foto.objects.all().get(pk=id)
    if request.POST:
        foto.delete()
    fotos = Foto.objects.all()
    return render(request, "principal.html", {"fotos": fotos, "fotoApaga": foto})

def apagar(request, id):
    foto = Foto.objects.all().get(pk=id)
    return render(request, "apagar.html", {"fotoApagar": foto})

            
def conetar(request):
    if request.POST:
        email = request.POST["email"]
        senha = request.POST["senha"]
        usuario = authenticate(username=email, password=senha)
        fotos = Foto.objects.all()
        login(request, usuario)
        return render(request, "principal.html", {"fotos": fotos})
    return render(request, "conetar.html")

def disconetar(request):
    logout(request)
    return render(request, "menu.html")