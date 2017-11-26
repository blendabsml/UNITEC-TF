from django import forms
from django.db import models
from core.models import Curso, Aluno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()

    def envia_email(self):
        print("Email para você: \n" +
        "Aluno: " + self.cleaned_data["nome"] + "\n" +
        "Email: " + self.cleaned_data["email"] + "\n" +
        "Mensagem: " + self.cleaned_data["mensagem"]
        )

class EmailForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mensagem = forms.CharField(required=True, widget=forms.Textarea)