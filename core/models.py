from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

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

class Aluno(Usuario):
    curso = models.ForeignKey(to='Curso', related_name="alunos")
    turmas = models.ManyToManyField('Turma', db_table='Matricula', related_name='alunos', blank=True)
    # email = models.CharField(max_length=80)

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

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(to='Disciplina', related_name="disciplinasOfertadas", null=False, blank=False)
    ano = models.IntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return "{}: {} - {}".format(self.disciplina, self.ano, self.semestre)
    class Meta:
        db_table = 'DisciplinaOfertada'

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

class Turma(models.Model):
    professor = models.ForeignKey(to='Professor', null=False, blank=False)
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1)
    cursos = models.ManyToManyField('Curso', blank=False) # ManyToManyField = Uma turma para multiplos cursos

    def __str__(self):
        return "{} - {}".format(self.turma_sigla, self.turno)

    class Meta:
        db_table = 'Turma'

