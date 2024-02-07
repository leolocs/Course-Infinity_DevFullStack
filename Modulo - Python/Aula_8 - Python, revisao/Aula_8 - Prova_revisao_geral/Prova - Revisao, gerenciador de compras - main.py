# Você está desenvolvendo um programa para gerenciar uma lista de compras:
# O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. 
# Além disso, o programa calcula o valor total de todos os produtos da lista.

# O programa oferece as seguintes opções:
# Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. 
# O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

# Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto.
# Além disso, exibe o valor total de todos os produtos da lista.
# Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
# Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
# Encerrar programa: Encerra a execução do programa.

# O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: 
# "produto", "valor", "quantidade" e "total". 
# A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.

# A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.
from functions_gerenciador_compras import *

while True:
    op = int(input("""
                Oque deseja fazer?
                1 - Adicionar produto
                2 - Atualizar um produto
                3 - Remover um produto
                4 - Ver lista de produtos
                0 - Encerrar programa   
            """))
    match op:
        case 1:
            nome_produto = str(input("Qual o nome do produto que deseja inserir?: "))
            qtd_produto = int(input("Qual a quantidade desse produto deseja inserir?: "))
            valor_produto = float(input("Qual o valor unitario do produto?: "))
            adicionar_produto(nome=nome_produto, qtd_produto=qtd_produto, valor=valor_produto)
        
        case 2:
            novo_produto = str(input("Qual o nome do produto que deseja alterar?: ")).lower()
            if novo_produto.isalpha():
                atualizar_produto(novo_produto=novo_produto)
            else:
                print("Digite apenas letras do produto!")
        
        case 3:
            produto_remover = str(input("Qual o nome do produto que deseja remover?: "))
            if produto_remover.isalpha():
                remover_produto()

        case 4:
            listar_produtos()

        case 0:
            print("Encerrando programa...")
            break