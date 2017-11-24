from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *
from django import forms


class NovoAlunoForm(forms.ModelForm):
    class Meta:	
        model = Aluno    
        fields = ('ra', 'nome','curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('123@mudar')
        user.perfil = 'A'        
        if commit:           
            user.save()        
        return user

class AlterarAlunoForm(forms.ModelForm):
     class Meta:
        model = Aluno         
        fields = ('nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm    
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'curso')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','tipo', 'carga_horaria')
    list_filter = ('tipo',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'teoria')
    list_display = ('nome',)
    search_fields = ('nome',)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ra', 'email',)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('professor', 'turma_sigla', 'turno',)

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'ano', 'semestre',)

class GradeCurricularAdmin(admin.ModelAdmin):
    list_display = ('curso', 'ano', 'semestre',)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('gradeCurricular', 'numero',)

class ArquivosFotoAdmin(admin.ModelAdmin):
    list_display = ('arquivo',)

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'confirmado',)

class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('turma', 'id', 'descricao')

class ArquivosQuestaoAdmin(admin.ModelAdmin):
    list_display = ('questao', 'id')

class RespostaAdmin(admin.ModelAdmin):
    list_display = ('questao', 'aluno', 'descricao')

class ArquivosRespostaAdmin(admin.ModelAdmin):
    list_display = ('resposta', 'id')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(GradeCurricular, GradeCurricularAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(ArquivosFoto, ArquivosFotoAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(ArquivosQuestao, ArquivosQuestaoAdmin)
admin.site.register(Resposta, RespostaAdmin)
admin.site.register(ArquivosResposta, ArquivosRespostaAdmin)