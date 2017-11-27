from django import forms
from django.db import models
from core.models import Document , Questao, Curso, Aluno

#Essas classes são usadas nos formulários de HTML, os campos dinâmicos são gerados aqui

#Formulário de Curso, Considerando todos os campos
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

#Formulário de Contato, usado para envio
class ContatoForm(forms.Form):
    Nome_Completo = forms.CharField(required=True)
    Telefone = forms.IntegerField(required=True)
    Email = forms.EmailField(required=True)
    Assunto_Contato = forms.CharField(required=True)
    Mensagem = forms.CharField(required=True, widget=forms.Textarea)

#Formulário de Email, usado para envio
class EmailForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mensagem = forms.CharField(required=True, widget=forms.Textarea)

#Formulário de Documento, Considerando todos os campos
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

#Formulário de Questãp, usando um modelo de "Questão", criado em models.py, excluindo "curso" dos campos
class QuestaoForm(forms.ModelForm):
      class Meta:
        model = Questao
        exclude = ["curso"]