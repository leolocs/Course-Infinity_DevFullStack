# Crie um banco de dados chamado loja;
# Crie uma tabela chamada clientes com atributos:
#id, nome, cpf, endereco, data_nasc

# Crie uma tabela com nome: produtos com atributos:
#id, nome, preco, qtde_estoque

CREATE DATABASE loja;
USE loja;

CREATE TABLE clientes(
	id INT primary key auto_increment,
    nome NVARCHAR(50),
    cpf INT(11),
    endereco nvarchar (255),
    data_nasc DATE
);

CREATE TABLE produtos(
	id  INT PRIMARY KEY auto_increment,
    nome NVARCHAR (45),
    preco FLOAT,
    qtd_estoque INT
);

CREATE TABLE vendas(
	id INT PRIMARY KEY auto_increment,
    id_cliente INT, foreign key (id_cliente) REFERENCES clientes(id),
    id_produto INT, foreign key (id_produto) REFERENCES produtos(id),
    hora_compra DATETIME
);

ALTER TABLE clientes MODIFY endereco NVARCHAR (100);  			# Modifica o tipo do atributo referenciado
ALTER TABLE clientes ADD idade INT; 							# Adiciona um atributo a tabela clientes
ALTER TABLE clientes DROP data_nasc; 							# Exclui por completo um atributo da tabela
ALTER TABLE clientes CHANGE nome nome_completo CHAR(100); 		# Muda o nome de um atributo por outro digitado em seguida


ALTER TABLE clientes MODIFY cpf NVARCHAR(11);					

INSERT INTO clientes VALUES (DEFAULT,"Joâo da Silva", 61145223522,"rua das alamedas",22);

SELECT FROM clientes * 
