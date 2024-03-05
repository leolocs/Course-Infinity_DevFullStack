# Você está criando um banco de dados para gerenciar vendas de produtos em uma loja online.
# Você precisa projetar o esquema do banco de dados e escrever consultas SQL para atender a várias necessidades da loja. 
# Aqui estão os requisitos:
# Crie um banco de dados chamado "loja_online" e as seguintes tabelas:

# Produtos: Armazena informações sobre produtos, incluindo um ID, nome, preço e quantidade em estoque.
# Clientes: Armazena informações sobre os clientes, incluindo um ID, nome, endereço de e-mail e histórico de compras.
# Pedidos: Registra informações sobre os pedidos feitos pelos clientes, incluindo um ID, data do pedido,ID do cliente e status do pedido.
# itens_Pedido: Registra os produtos incluídos em cada pedido, incluindo um ID, ID do pedido, ID do produto e quantidade.

CREATE DATABASE loja;
USE loja;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(45) NOT NULL,
    cpf NVARCHAR(11) UNIQUE NOT NULL,
    endereco NVARCHAR(50) NOT NULL,
    data_nasc DATE,
    idade INT,
    CHECK (idade >= 18),
    hist_compras JSON
);

CREATE TABLE produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto NVARCHAR(45) UNIQUE,
    preco FLOAT,
    CHECK (preco > 0)
);

CREATE TABLE pedidos(
	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE itens_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT, FOREIGN KEY (id_pedidos) REFERENCES produtos(id),
    id_clientes INT, FOREIGN KEY (id_clientes) REFERENCES clientes(id),
    qtd INT
)