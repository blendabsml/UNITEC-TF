from django.shortcuts import render

from core.models import Curso
from core.forms import ContatoForm

# Create your views here.
def index(request):
    contexto = {
        "usuario": "Blenda",
        "perfil" : "professor",
        "cursos": Curso.objects.all()
    }
    return render(request, "index.html", contexto)

def contato(request):
    if request.POST:    
        form = ContatoForm(request.POST)
        form.envia_email()

    else:
        form = ContatoForm()

    contexto = {
        "form": form
    }
    return render(request, "contato.html", contexto)

def index(request):
    return render(request, "index.html")

def Contato(request):
    return render(request, "Contato.html")

def ListaCurso(request):
    return render(request, "ListaCursos.html")

def AreaAluno(request):
    return render(request, "AreaAluno.html")

def Disciplinas(request):
    return render(request, "Disciplinas.html")

def esqueciSenha(request):
    return render(request, "esqueciSenha.html")

def form(request):
    return render(request, "form.html")

def Login(request):
    return render(request, "Login.html")

def noticia1(request):
    return render(request, "noticia1.html")

def noticia2(request):
    return render(request, "noticia2.html")

def Noticias(request):
    return render(request, "Noticias.html")

def novaDisciplina(request):
    return render(request, "novaDisciplina.html")

def novoUsuario(request):
    return render(request, "novoUsuario.html")

def SobreCurso(request):
    return render(request, "SobreCurso.html")