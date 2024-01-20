#A duração do desafio é do momento do anúncio do desafio até o dia 11/12/23 19:00h - Segunda-feira

#Ao finalizar o seu desafio, mande um e-mail com o título 'DESAFIO DEV FULL STACK' contendo:
# - Arquivos utilizados incluindo imagens para: dev@infinityschool.com.br
# - Nome completo 
# - Chave PIX
# - Nome no Discord
# Prêmio: R$40.00 - quarenta reais

# Segue agora desafio:
# SISTEMA DE GERENCIAMENTO DE BIBLIOTECA

# Desenvolver um programa em Python que simule o gerenciamento de uma biblioteca. O programa deve permitir ao usuário interagir com um catálogo de livros através de um menu interativo dentro de um laço de repetição.
# Cada livro deve ter um título, autor, Ano de publicação e um identificador único.
# O catálogo deve ser armazenado em uma lista ou dicionário.
# Implemente uma função de empréstimo de livros que registre quem pegou o livro e a data de devolução.
# Implemente uma função de retorno de livros.

catalogo = {
    "livro1": {
        "id": 1,
        "Titulo": "Como fazer amigos e influenciar pessoas",
        "Autor": "Dale Carnegie",
        "Ano": 2016
    },
    "livro2": {
        "id": 2,
        "Titulo": "Viagem ao centro da terra",
        "Autor": "Julio Verne",
        "Ano": 2019
    },
    "livro3": {
        "id": 3,
        "Titulo": "Breves respostas para grandes questões",
        "Autor": "Stephen Hawking",
        "Ano": 2018
    }
}

livros_alugados = {}

def aluga_livro(id):
    if id == 1:
        livros_alugados['livro1'] = catalogo.pop("livro1", {})
    if id == 2:
        livros_alugados['livro2'] = catalogo.pop("livro2", {})
    if id == 3:
        livros_alugados['livro3'] = catalogo.pop("livro3", {})
    return id

# Verificar se existe a possibilidade de inserir uma função aonde o usuário poderia adicionar um novo livro ao dicionario ja criado Ex: 1- Inserir um novo livro a biblioteca

while True: 
    op = int(input(""" Olá, bem vindo a biblioteca online, oque gostaria de fazer?
                    1- Alugar um livro
                    2- Devolver um livro
                    3- Sair da biblioteca
                """))
    if op == 3:
        break
    if op == 1:
       print("Esse é nosso catálogo da biblioteca: ")
       for livro, catalogo_interno in catalogo.items():
            print(f"Informações do {livro}")
            for id, titulo in catalogo_interno.items():
                print(f"{id}:{titulo}")
            print()
            id = int(input("Qual o livro que deseja alugar? (Digite o id do livro!): "))
            aluga_livro(id=id)
                
