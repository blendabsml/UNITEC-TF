create database LMSVERSAOFINAL

go

drop database LMSVERSAOFINAL

create table Disciplina (
    id int not null IDENTITY (1,1),
    nome varchar(240),
    carga_horaria tinyint,
    teoria decimal(3),
    pratica decimal(3),
    emenda text,
    competencias text,
    habilidades text,
    conteudo text,
    bibliografia_basica text,
    bibliografia_complementar text,
    constraint pk_idDisciplina primary key (id),
    constraint uq_Disciplin unique (nome)
)

go

create table Curso(
    id int not null IDENTITY (1,1),
    sigla varchar(5) not null,
    nome varchar(50) ,
    constraint pk_idSigla primary key (id),
    constraint uq_nomeII UNIQUE ( sigla ),
    constraint uq_nomeI UNIQUE ( nome ),
)



go


create table Professor(
	id int not null identity (10000, 1), ---Ra_professor
    apelido varchar (30),
    nome varchar (120),
    email varchar (80),
    celular char (11),

    constraint uq_apeli UNIQUE (apelido),

    constraint pk_prof primary key (id),
)


go


create table Aluno(
    id int not null IDENTITY (100000, 1), ---Ra_aluno
    nome varchar (120),
    email varchar (80),
    celular char (11),
    sigla_curso char (2),

    constraint pk_aluno primary key (id),
)
 

 go 


create table GradeCurricular(
    id int not null IDENTITY (1,1),
    sigla_curso varchar (5),
    ano smallint,
    semestre char (1),

    constraint pk_idGraCr primary key (id),

    constraint uq_GradCr UNIQUE (sigla_curso, ano, semestre),

    constraint fk_SigCur foreign key (sigla_curso)
        references Curso (sigla),
)


go

create table Periodo(
    id int not null IDENTITY (1,1),---numero
    sigla_curso int,
    id_gradeCurri int not null,


    constraint pk_Periodo primary key (id),

    constraint fk_SigCurII foreign key (sigla_curso)
        references Curso (id),

    constraint fk_GradCurr foreign key (id_gradeCurri)
        references GradeCurricular (id),     

    constraint uq_periodo UNIQUE (sigla_curso, id_gradeCurri),
    
)


go


create table PeriodoDisciplina(
    id int not null IDENTITY (1,1),
    sigla_curso int,
    numero_periodo int,
    nome_disciplina int,

    constraint pk_PeriodoDisciplina primary key (id),

    constraint fk_SigCurIII foreign key (sigla_curso)
        references Curso (id),

    constraint fk_idPeriodo foreign key (numero_periodo)
        references Periodo (id),
    
    constraint fk_nomeDisc foreign key (nome_disciplina)
        references Disciplina (id),

    constraint uq_periodoDisciplinar UNIQUE (sigla_curso, numero_periodo,nome_disciplina ),

)

go

create table DisciplinaOfertada(
    id int not null IDENTITY (1,1),
    nome_disciplina int,
    ano smallint,
    semestre char(1),

    constraint pk_DisciplinaOfertada primary key(id),

    constraint fk_nomeDiscII foreign key (nome_disciplina)
        references Disciplina (id),
    
    constraint uq_DisciplinaOfert UNIQUE (nome_disciplina, ano, semestre),
)

go

create table Turma(
    id int not null IDENTITY (1,1),
    nome_disciplina int,
    turno varchar(15),
    ra_professor int,
    id_dicipOferta int not null,

    constraint pk_Turma primary key (id),

    constraint fk_nomeDiscIII foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),
    
    constraint fk_raProf foreign key (ra_professor)
        references Professor (id),
    
    constraint uq_Turma UNIQUE (nome_disciplina, id_dicipOferta),
)

go

create table CursoTurma(
    id int not null IDENTITY (1,1),
    sigla_curso int,
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int,

    constraint pk_CursoTurma primary key (id),

    constraint fk_SigCur2 foreign key (sigla_curso)
        references Curso (id),

    constraint fk_nomeDiscIV foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta1 foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),

    constraint fk_idTurma1 foreign key (id_turma)
        references Turma (id),
    
    constraint uq_CursoTurma UNIQUE (sigla_curso, nome_disciplina, id_dicipOferta, id_turma),
)

go

create table Matricula(
    id int not null IDENTITY (1,1),
    ra_aluno int,
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int,

    constraint pk_Matricula primary key (id),

    constraint fk_raAlu foreign key (ra_aluno)
        references Aluno (id),

    constraint fk_nomeDiscV foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta01 foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),

    constraint fk_idTurmaI foreign key (id_turma)
        references Turma (id),

    constraint uq_Matricula UNIQUE (ra_aluno, nome_disciplina, id_dicipOferta,id_turma),
)

go

create table Questao(
    id int not null IDENTITY (1,1), /* ESTE ID É A COLUNA 'NUMERO', COLOQUEI ID PARA DEIXAR PADRONIZADO*/
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int ,
    data_limite_entrega DATE,
    descricao text,
    _data date,

    constraint pk_QuestaoNumero primary key (id),


    constraint fk_nomeDiscVI foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta02 foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),

    constraint fk_idTurmaII foreign key (id_turma)
        references Turma (id),

    constraint uq_Questao UNIQUE (nome_disciplina, id_dicipOferta, id_turma),
)

go

create table ArquivoQuestao(
    arquivo varchar (500) not null, 
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int ,
    numero_questão int not null,

    constraint pk_arquivo primary key (arquivo),

    constraint fk_nomeDiscVII foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta03 foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),

    constraint fk_idTurmaIII foreign key (id_turma)
        references Turma (id),

    constraint fk_idQuestao foreign key (numero_questão)
        references Questao (id),

    constraint uq_ArquiQues UNIQUE (nome_disciplina, id_dicipOferta, id_turma, numero_questão),
)

go

create table Resposta (
    ra_aluno int not null IDENTITY (1,1),
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int,
    numero_questão int not null,
    data_avaliacao date,
    nota decimal (4,2),
    avaliacao text,
    descricao text,
    data_de_envio date,

    constraint pk_Resposta primary key (ra_aluno),

    constraint fk_nomeDiscVIII foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta04 foreign key (id_dicipOferta)
        references DisciplinaOfertada (id),

    constraint fk_idTurmaIV foreign key (id_turma)
        references Turma (id),

    constraint fk_idQuestaoI foreign key (numero_questão)
        references Questao (id),

    constraint uq_resposta UNIQUE (nome_disciplina, id_dicipOferta,  id_turma, numero_questão),
)

go

create table ArquivoResposta (
    arquivo varchar (500) not null,
    nome_disciplina int,
    id_dicipOferta int,
    id_turma int ,
    numero_questão int not null,
    ra_aluno int,
    
    constraint pk_arquivoI primary key (arquivo),
    
    constraint fk_nomeDiscIX foreign key (nome_disciplina)
        references Disciplina (id),

    constraint fk_dicipOferta05 foreign key (id_dicipOferta)
    references DisciplinaOfertada (id),

    constraint fk_idTurmaV foreign key (id_turma)
        references Turma (id),

    constraint fk_idQuestaoII foreign key (numero_questão)
        references Questao (id),

    constraint fk_raAluI foreign key (ra_aluno)
        references Aluno (id),

    constraint uq_ArquivosRes0 unique (nome_disciplina , id_dicipOferta, id_turma, numero_questão, ra_aluno),
   
)
