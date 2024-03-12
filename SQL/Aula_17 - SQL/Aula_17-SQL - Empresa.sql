

CREATE DATABASE empresa;
USE empresa;

CREATE TABLE funcionarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(255),
    cpf CHAR(11),
    data_nasc DATE,
    departamento NVARCHAR(255)
);

INSERT INTO funcionarios (nome, cpf, data_nasc, departamento) VALUES
('Ana Silva', '12345678901', '1990-05-15', 'RH'),
('João Oliveira', '98765432109', '1985-10-20', 'Financeiro'),
('Pedro Santos', '45612378965', '1978-03-12', 'Vendas'),
('Mariana Costa', '78965412308', '1995-08-25', 'TI'),
('Lucas Pereira', '32198745602', '1982-12-03', 'RH'),
('Camila Souza', '45612378965', '1989-07-14', 'Financeiro'),
('Rafaela Lima', '78965412308', '1986-04-30', 'Vendas'),
('Gustavo Santos', '32198745602', '1992-11-18', 'TI'),
('Fernanda Oliveira', '12345678901', '1993-09-22', 'RH'),
('Bruno Costa', '98765432109', '1984-06-05', 'Financeiro'),
('Larissa Rodrigues', '45612378965', '1990-03-17', 'Vendas'),
('Ricardo Almeida', '78965412308', '1987-01-25', 'TI'),
('Amanda Martins', '32198745602', '1994-08-08', 'RH'),
('Roberto Silva', '12345678901', '1988-12-10', 'Financeiro'),
('Carla Santos', '98765432109', '1983-02-28', 'Vendas'),
('Renata Costa', '45612378965', '1991-11-09', 'TI'),
('Daniel Pereira', '78965412308', '1980-07-02', 'RH'),
('Patrícia Oliveira', '32198745602', '1985-05-19', 'Financeiro'),
('Marcos Silva', '12345678901', '1986-10-24', 'Vendas'),
('Vanessa Costa', '98765432109', '1981-03-07', 'TI');

SELECT departamento, count(*) as total_funcionario
FROM funcionarios
GROUP BY departamento;


#SOBRE ORDER BY:

CREATE TABLE transacoes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    data_efetuada DATE,
    valor float
);

INSERT INTO transacoes (data_efetuada, valor) VALUES
('2024-03-01', 1000.00),
('2024-03-03', 1500.00),
('2024-03-05', 800.00),
('2024-03-07', 2000.00),
('2024-03-10', 1200.00),
('2024-03-12', 1750.00),
('2024-03-14', 900.00),
('2024-03-16', 1300.00),
('2024-03-18', 1600.00),
('2024-03-20', 1100.00);


SELECT * FROM transacoes ORDER BY valor;
SELECT * FROM transacoes ORDER BY valor DESC;


