CREATE DATABASE aula1;
USE aula1;
CREATE TABLE alunos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome NVARCHAR(50),
	altura FLOAT,
	data_nasc DATE, #tipo DATE datas entre 01/JAN/1000 até 31/DEZ/9999, tipo aaaa/mm/dd
	hor_aul TIME, 	#tipo TIME tempo hh:mm:ss
	registro_chegada DATETIME,
    descricao TEXT
);

DROP TABLE alunos;
DROP DATABASE aula1;