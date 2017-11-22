insert into Disciplina (nome, carga_horaria)
values  ('Matematica N1','80'),
        ('Matematica N2','80'),
        ('Gestão de Projetos','80'),
        ('Libra','80'),
        ('SQL', '80'),
        ('Portugues','80'),
        ('Linguagem de Programação','80'),
        ('Engenharia de SoftWare','80');

GO

INSERT INTO Curso (sigla, nome)
values  ('ADS','Analise e desenvolvimento de sistema'),
        ('BD', 'Banco de dados'),
        ('GTI', 'Gestão de Tecnologia da Informação'),
        ('ADM','Administração');

GO

INSERT INTO Professor (apelido, nome, email, celular)
VALUES  ('Dré','Andre Luis','Andre@live.com','988776655'),
        ('Lan','Alan Batista','Alan209@gmail.com,','955223377'),
        ('Kaka','Karol Silva','kaka@outlook.com','922441155'),
        ('Mende','Amanda Jataí','mandinha@gmail.com','988005942');
        

GO

INSERT INTO  Aluno (nome, email, celular, sigla_curso)
VALUES  ('José Pereira','jo@live.com','911223344','1'),
        ('Oliver Joaquim','liver@gmail.com','976341342','3'),
        ('Renato Cicca','re.cicca@gmail.com','983625131','1'),
        ('Miguel Sousa','misousa@live.com','922114455','4'),
        ('Luiza Venancio','lubalu@hotmail.com','988776655','1'),
        ('Matheus Andrade','math@outlook.com','976452719','2'),
        ('Vinicius Rodrigues','viniro@lhotmail.com','922118822','2'),
        ('Robson Gouveia','robgou@outlook','954327890','4'),
        ('Viviane Inacio','vivis@live.com','912413821','3'),
        ('Vanessa Chico','nessas@hotmail.com','987456218','1'),
        ('Bruno Felix','brubru@gmail.com','930225544','2'),
        ('Josenelma','jooonelma@uol.com.br','920301222','3'),
        ('Reginaldo Brito','ginabrito@bol.com.br','933663213','4'),
        ('Regis Amadeu','regis_amadeu@hotmail.com','933221983','2'),
        ('Iraneide Souza','irasoso@bol.com.br','987654322','3'),
        ('Melissa Figueiras','mel@uol.com.br','944884332',4)



GO

INSERT INTO GradeCurricular (sigla_curso, ano, semestre)
VALUES  ('ADS','2017', '1º'),
        ('BD' ,'2017','1º'),
        ('GTI','2017','2º'),
        ('ADM','2017','2º'),
        ('ADS','2017', '2º'),
        ('BD' ,'2017','2º'),
        ('GTI','2017','1º'),
        ('ADM','2017','1º');

GO

INSERT INTO Periodo(sigla_curso, id_gradeCurri)
VALUES  ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('4','4'),
        ('3','3'),
        ('2','2'),
        ('1','1');

GO

INSERT INTO PeriodoDisciplina (sigla_curso, numero_periodo, nome_disciplina)
VALUES  ('1','1','1'),
        ('2','2','2'),
        ('3','3','4'),
        ('4','5','6'); 

GO

INSERT INTO Turma (nome_disciplina, turno, ra_professor)
VALUES  ('1','Noite','10004'),
        ('2','Noite','10002'),
        ('5','Manhã','10001'),
        ('3','Noite','10002'),
        ('4','Noite','10003'),
        ('6','Manhã','10004'),
        ('7','Noite','10003'),
        ('8','Manhã','10001');

GO

INSERT INTO CursoTurma(sigla_curso, nome_disciplina, id_turma)
VALUES  ('1','7','7'),
        ('1','8','8'),
        ('2','5','3'),
        ('2','8','8'),
        ('3','3','4'),
        ('3','4','5'),
        ('4','2','1'),
        ('4','1','2');

GO

INSERT INTO Matricula (ra_aluno, curso, id_turma)
values  ('100001','1','1'),
        ('100002','2','3'),
        ('100003','3','5'),
        ('100004','4','7'),
        ('100005','3','5'),
        ('100006','2','4'),
        ('100007','4','8'),
        ('100008','1','2'),
        ('100009','4','7'),
        ('100010','3','6'),
        ('100011','2','4'),
        ('100012','1','1'),
        ('100013','1','2'),
        ('100014','2','4'),
        ('100015','3','5'),
        ('100016','4','7');




---------TABELAS QUE NÃO INSERI NADA---------
---------DisciplinaOfertada
---------
---------
---------