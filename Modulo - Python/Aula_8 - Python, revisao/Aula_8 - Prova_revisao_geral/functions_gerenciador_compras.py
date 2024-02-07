
lista_produtos = []
produtos_removidos = []

def adicionar_produto(nome:str,qtd_produto:int,valor:float):
    while True:
        if nome.isalpha():
            print("Nome válido")
            break
        else:
            print("Digite um nome com apenas letras!")

    produto = {"nome":nome,"quantidade":qtd_produto, "valor":valor}
    lista_produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def atualizar_produto(novo_produto:str):
    for produto in lista_produtos:
        if produto["nome"] == novo_produto:
            novo_nome = input("Qual o nome do novo produto?: ")
            while True:
                if novo_nome.isalpha():
                    produto['nome'] = novo_nome
                    print ("Nome válido!")
                    break
                else:
                    print("Digite um nome válido com apenas letras!!")

            nova_qtd = input("Qual a quantidade do novo produto?: ")
            produto['quantidade'] = nova_qtd
            novo_valor = input("Qual o valor do novo produto?: ")
            produto['valor'] = novo_valor
            print("Novo produto atualizado com sucesso!")

def remover_produto(nome:str):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            produtos_removidos.append(produto)
            lista_produtos.remove(produto)
            print("Produto removido da lista de produtos e adicionado a lista de produtos removidos, com sucesso!")

def listar_produtos():
    for produto in lista_produtos:
        print(f"""
            Produto: {produto['nome']}
            Quantidade do produto: {produto['quantidade']}
            Valor do produto: {produto['valor']}
            Valor total do produto{produto['quantidade']*['valor']}
    
""")