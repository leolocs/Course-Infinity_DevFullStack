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
INSERT INTO clientes (nome_completo, cpf, endereco, idade) 
	VALUES 
		("Maria Eduarda", "31125670233","Rua jurubeba, 5",22),
		("José Maria","71165226520", "Rua circunflexo, 16",42),
        ("Orinocula Pernicula", 73085642265, "Rua Jatobá, 124",56);
        
SELECT * FROM clientes;
DELETE FROM clientes WHERE cpf = '2147483647';

UPDATE clientes
SET nome_completo = "João da Silva"
WHERE id = 3;

SELECT nome_completo, idade FROM clientes;
SELECT * FROM clientes WHERE idade > 20;

INSERT INTO produtos (nome,preco,qtd_estoque) 
VALUES 
("Recheado", 2.5, 87), 
("Ruffles Tradicional", 6.25, 51), 
("Doritos", 9.5, 10), 
("Gua Jesus", 5.99, 20), 
("Pringles", 14.99, 75);

SELECT * FROM produtos
WHERE preco > 5 AND qtd_estoque < 60;

SELECT * FROM produtos WHERE qtd_estoque > 60 OR preco < 5;

UPDATE produtos SET 
preco = 7.5, qtd_estoque = 25 
WHERE id = 3;

DELETE FROM produtos WHERE id = 4;
