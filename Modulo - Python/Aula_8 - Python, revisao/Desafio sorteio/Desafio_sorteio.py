# FAÇA UM PROGRAMA DE SORTEIO DE CLIENTES ONDE O PROGRAMA VAI CADASTRANDO CLIENTES ATÉ O PROPRIO USUÁRIO DECIDIR QUE QUER PARAR(LOOP INFINITO)
# OS DADOS PARA CADASTRO SÃO: nome, cpf, valor_compra
# QUANDO O USUÁRIO ENCERRAR O LOOP FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES CADASTRADOS E MOSTRE NA TELA TODOS OS DADOS DO CLIENTE QUE FOI SELECIONADO COM UMA MENSAGEM CUSTOMIZADA TIPO:
# """Parabéns {nome do cliente}, cpf: {cpf do cliente} você foi o sorteado por ter feito uma compra no valor de {valor da compra do cliente}"""
# MOSTRE TAMBÉM QUAL O NOME DO CLIENTE QUE TEVE O MAIOR VALOR DE COMPRA
# TRATE TODOS OS DADOS!

from unidecode import unidecode
import random
from function import *

lista_clientes = []

while True:
    op = int(input("Deseja cadastrar um novo cliente? Digite: (S para sim ou N para não)").strip().lower())
    if len(op) > 1:
        print("Digite apenas: (S/N)")
    else:
        if op == "n":
            print("Programa encerrado") 
            break
        if op == "s":
            nome = nome_valido()         
            cpf = cpf_valido()
            valor = valor_valido()
            lista_clientes.append({
                "Nome" : nome,
                "CPF" : cpf,
                "valor_compra" : valor 
            })     

if len(lista_clientes) > 0:
    sorteado = random.choice(lista_clientes)
    print(f"""
    O cliente sorteado foi: {sorteado}
    E o cliente com a compra mais alta foi: {maior_compra(lista_clientes)}
""")
else:
    print("Nenhum cliente cadastrado")



    

