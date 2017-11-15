from django.shortcuts import render

from core.models import Curso
from core.forms import ContatoForm, CursoForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def Contato(request):
    if request.POST:    
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()

    else:
        form = ContatoForm()

    contexto = {
        "form": form
    }
    return render(request, "Contato.html", contexto)

def curso(request):
    if request.POST:    
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CursoForm()

    contexto = {
        "form": form
    }
    return render(request, "curso.html", contexto)


def ListaCurso(request):
    return render(request, "ListaCursos.html")

def AreaAluno(request):
    return render(request, "AreaAluno.html")

def Disciplinas(request):
    return render(request, "Disciplinas.html")

def noticia1(request):
    return render(request, "noticia1.html")

def noticia2(request):
    return render(request, "noticia2.html")

def Noticias(request):
    return render(request, "Noticias.html")

def SobreCurso(request):
    return render(request, "SobreCurso.html")