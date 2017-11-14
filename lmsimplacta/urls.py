"""lmsimplacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'^index', index),
    url(r'^Contato', Contato, name="Contato"),
    url(r'^curso', curso),
    url(r'^entrar', entrar, name="login"),
    url(r'^sair', sair, name="logout"),
    url(r'^ListaCursos', ListaCurso),   
    url(r'^AreaAluno', AreaAluno),      
    url(r'^Disciplinas', Disciplinas),
    url(r'^noticia1', noticia1),
    url(r'^noticia2', noticia2),
    url(r'^Noticias', Noticias),
    url(r'^SobreCurso', SobreCurso),
]
