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
from django.contrib.auth.views import login, logout
from core.views import *
from django.conf.urls.static import static
from django.conf import settings
from core import views

#Arquivo responsável por gerar os endereços e url, o que será exibido ou solicitado na barra de endereços do navegador

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'^index/', index),
    url(r'^Contato/', Contato, name="Contato"),
    url(r'^curso/', curso),
    url(r'^entrar/', login,{"template_name":"login.html"}, name="login"),
    url(r'^sair/', logout, name="logout"),
    url(r'^ListaCursos/', ListaCurso),   
    url(r'^AreaAluno/$', AreaAluno, name='AreaAluno'), 
    url(r'^AreaAluno/boletim/', boletim, name='boletim'), 
    url(r'^AreaAluno/Mensagens/', Mensagens, name='Mensagens'),    
    url(r'^Disciplinas/', Disciplinas),
    url(r'^noticia1/', noticia1),
    url(r'^noticia2/', noticia2),
    url(r'^Noticias/', Noticias),
    url(r'^SobreCurso/', SobreCurso),
    url(r'^restrito/$', restrito, name='restrito'),
    url(r'^restrito/(?P<sigla>[A-Z,a-z]+)/questao/(?P<questao_id>[0-9]*)', questao_form, name='questao_form'),
	url(r'^email/', email),
    url(r'^Matricula/', Matricula),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)