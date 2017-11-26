from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

#Função Usuario------------------------------------------------------#
class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,ra, password=None, **extra_fields):
        return self._create_user(ra,password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=50)
    ra = models.IntegerField(unique=True)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default="C")
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']


    objects = UsuarioManager()

    @property
    def is_staff(self):
        return self.perfil == 'C'

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome

    def __str__(self):
        return self.nome

#Função Curso------------------------------------------------------#
class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Curso'

#Função Aluno------------------------------------------------------#
class Aluno(Usuario):
    curso = models.ForeignKey(to='Curso', related_name="alunos")
    turmas = models.ManyToManyField('Turma', db_table='Matricula', related_name='alunos', blank=True)
    email = models.EmailField(max_length=254)

#Função Disciplina------------------------------------------------------#
class Disciplina(models.Model):
    nome = models.CharField(max_length=240)
    carga_horaria = models.SmallIntegerField()
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.nome, self.carga_horaria, self.teoria)

    class Meta:
        db_table = 'Disciplina'

#Função DisciplinaOfertada------------------------------------------------------#
class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(to='Disciplina', related_name="disciplinasOfertadas", null=False, blank=False)
    ano = models.IntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return "{}: {} - {}".format(self.disciplina, self.ano, self.semestre)
    class Meta:
        db_table = 'DisciplinaOfertada'

#Função Professor------------------------------------------------------#
class Professor(models.Model):
    ra = models.IntegerField(unique = True, null = False)
    apelido = models.CharField(max_length=30,unique = True, null = True)
    nome = models.CharField(max_length =  120)
    email = models.CharField(max_length =  80)
    celular = models.CharField(max_length =  11)

    def __str__(self):
        return "{} - {}".format(self.ra, self.apelido)

    class Meta:
        db_table = 'Professor'

#Função Turma------------------------------------------------------#
class Turma(models.Model):
    professor = models.ForeignKey(to='Professor', null=False)
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1)
    cursos = models.ManyToManyField('Curso', blank=False) # ManyToManyField = Uma turma para multiplos cursos

    def __str__(self):
        return "{} - {}".format(self.turma_sigla, self.turno)

    class Meta:
        db_table = 'Turma'

#Função Grade Curricular--------------------------------------------#
class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="gradesCurriculares", null=False)
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)
    
    def __str__(self):
        return "{}: {} - {}".format(self.curso, self.ano, self.semestre)
    class Meta:
        db_table = 'GradeCurricular'

#Função Periodo------------------------------------------------------#
class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False)
    numero = models.SmallIntegerField(null=False)
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return "{} - {}".format(self.numero, self.disciplinas)

    class Meta:
        db_table = 'Periodo'

class ArquivosFoto(models.Model):
    arquivo = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format( self.arquivo)
    class Meta:
        db_table = 'ArquivosFoto'

class Candidato(models.Model):
    nome = models.CharField(max_length=250, null=True)
    ra = models.CharField(max_length=80, null=True)
    email = models.CharField(max_length=80, null=True)
    celular = models.CharField(max_length= 11, null=True)
    codigo_acesso = models.CharField(max_length=120, null=True)
    confirmado = models.BooleanField(default=False)
    matricula_aceita = models.BooleanField(default=False)
    turma = models.ForeignKey(to='Turma', related_name="candidatos", null=True)
    foto = models.ForeignKey(to='ArquivosFoto', related_name="candidatos", null=True)
    
    def __str__(self):
        return "{}: {} - {}".format(self.nome, self.email, self.confirmado)

    class Meta:
        db_table = 'Candidado'
    
class Questao(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="questoes", null=False, blank=False)
    descricao = models.TextField()
    data_limite_entrega = models.DateField()
    numero = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return "{} - {}: {}".format(self.turma.turma_sigla, self.id, self.descricao)

    class Meta:
        db_table = 'Questao'

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(to='Questao', related_name="arquivosQuestao", null=False, blank=False)
    arquivo = models.CharField(max_length=500)

    def __str__(self):
        return "{}: {}".format(self.questao, self.id)
    class Meta:
        db_table = 'ArquivosQuestao'

class Resposta(models.Model):
    aluno = models.ForeignKey(to='Aluno', related_name="respostas", null=False, blank=False)
    questao = models.ForeignKey(to='Questao', related_name="respostas", null=False, blank=False)
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.DateField()

    def __str__(self):
        return "{} - {}: {}".format(self.questao.id, self.aluno.ra, self.descricao)

    class Meta:
        db_table = 'Resposta'
    
class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(to='Resposta', related_name="arquivosResposta", null=False, blank=False)
    arquivo = models.CharField(max_length=250)

    def __str__(self):
        return "{}: {}".format(self.resposta, self.id)

    class Meta:
        db_table = 'ArquivosResposta'