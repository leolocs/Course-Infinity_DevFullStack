# Crie uma tabela "pedidos" com as colunas "id_pedido" "id_cliente" e "data_pedido".
# Adicione uma constraint de chave estrangeira na coluna "id_cliente" para garantir que um pedido so possa ser feito por um cliente existente na tabela "clientes"

CREATE DATABASE loja;
USE loja;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(45) NOT NULL,
    cpf NVARCHAR(11) UNIQUE NOT NULL,
    endereco NVARCHAR(50) NOT NULL,
    data_nasc DATE,
    idade INT,
    CHECK (idade >= 18)
);

ALTER TABLE clientes ADD endereco NVARCHAR(100) UNIQUE NOT NULL;

CREATE TABLE pedidos(
	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

# AP_2 - Crie uma tabela "produtos" com as colunas "id_produto", "nome_produto" e "preco"
# Adicione uma constraint de verificação para garantir que o preço do produto seja maior que zero

CREATE TABLE produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto NVARCHAR(45) UNIQUE,
    preco FLOAT,
    CHECK (preco > 0)
);

# AP_3 - Adicione uma constraint de restrição unica na coluna email da tabela "clientes" para garantir que nenhum cliente possa ter o mesmo endereço de email.
ALTER TABLE clientes ADD email nvarchar(50) UNIQUE;
ALTER TABLE clientes MODIFY endereco NVARCHAR(100) NOT NULL;
SELECT * FROM clientes

