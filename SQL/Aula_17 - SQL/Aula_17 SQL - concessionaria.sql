# CRIE UM BANCO CHAMADO conssessionaria
# COM UMA TABELA CHAMAMA carros:
# id, marca, modelo, ano(year), cor, preco, ar-condicionado

# UMA TABELA clientes:
# id, nome, cpf, endereco, data_nasc

# UMA TABELA vendas
# id, id_cliente, id_carro, horario_venda

# INSIRA 10 CARROS E 5 CLIENTES E 3 VENDAS

# ATUALIZE A MARCA DO 8 CARRO
# ATUALIZE O CPF E O ENDEREÇO O 4 CLIENTE
# DELETE O 7 CARRO

# VISUALIZE TODOS OS CARROS
# VISUALIZE TODOS OS CLIENTES
# VISUALIZE TODOS AS VENDAS

# VISUALIZE A MARCA E O MODELO DE TODOS OS CARROS LANÇADOS DEPOIS DE 2015
# VISUALIZE TODOS OS CARROS DA MARCA FIAT QUE TENHA A COR VERMELHA
# VISUALIZE TODOS OS CARROS QUE CUSTEM MAIS QUE 80.000

CREATE DATABASE concessionaria_bd;
USE concessionaria_bd;

CREATE table carros(
id iNT PRIMARY KEY AUTO_INCREMENT,
marca NVARCHAR(45) NOT NULL,
modelo NVARCHAR(45) NOT NULL,
ano YEAR,
cor NVARCHAR(15),
preco float,
ar_condicionado bool
);

CREATE TABLE clientes(
id INT PRIMARY KEY auto_increment,
nome NVARCHAR(50) NOT NULL,
cpf CHAR(11) UNIQUE NOT NULL,
endereco NVARCHAR(60),
data_nasc DATE
);

CREATE TABLE vendas(
id INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES clientes(id),
id_carro INT, FOREIGN KEY (id_carro) REFERENCES carros(id),
data_venda DATETIME
);

INSERT INTO carros
	(marca,modelo,ano,cor,preco,ar_condicionado) VALUES 
    ("Renault", "Kwid", "2020", "Branco", 50.000, True),
    ("Mitsubishi","Lancer_Evolution","2019","Azul", 42.500, True),
    ("Nissan", "350Z","2007","Verde", 280.000, True),
    ("Chevrolet", "Camaro","2015","Amarelo", 280.000, True);
    
INSERT INTO clientes (nome, cpf, endereco, data_nasc) VALUES
	('João Silva', '12345678901', 'Rua A, 123', '1990-05-15'),
	('Maria Santos', '23456789012', 'Av. B, 456', '1985-10-20'),
	('Pedro Oliveira', '34567890123', 'Travessa C, 789', '1978-03-08'),
	('Ana Souza', '45678901234', 'Rua D, 321', '1992-07-25'),
	('Carlos Pereira', '56789012345', 'Av. E, 654', '1982-12-12'),
	('Juliana Martins', '67890123456', 'Rua F, 987', '1975-09-30');
    
INSERT INTO vendas (id_cliente, id_carro, data_venda) VALUES
(1, 1, '2023-10-01 10:00:00'),
(2, 2, '2023-10-05 15:30:00'),
(3, 3, '2023-10-10 11:45:00');

    
UPDATE carros SET marca = "Renault" WHERE id = 8;
UPDATE clientes SET cpf = "12345678900", endereco = "Rua logo ali,16" WHERE id = 4;
DELETE FROM carros WHERE id = 6;

SELECT * FROM carros;
SELECT * FROM clientes;
SELECT * FROM vendas;

SELECT marca, modelo FROM carros WHERE ano > 2019;

SELECT * FROM carros WHERE marca = "Volkswagen" OR cor = "Preto";

SELECT * FROM carros WHERE preco > 60000.00;