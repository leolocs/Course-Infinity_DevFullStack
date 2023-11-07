#Lista com vários objetos de tipos diferentes
# lista = ["Leonardo",25, 1.76, True]

#lista com informações de uma pessoa 
# lista = ["Leonardo", 4121997, 1.76, "brasileiro"]

#Imprime a quantidade de itens que tem em uma lista
# print(len(lista))

#lista com resultado de operações
# lista = [1,5,6,7,10]

#Faça um programa com essa lista: ["Texto", 25, True, 1.4, "Texto2"], pegue o número 25 dessa lista e faça uma soma com 10, 25+10 e mostre o resultado da soma na tela
# info = ["Nome", 25, True, 1.4, "Texto2"]
# print(info[1] + 10)

# Faça um programa que altere a lista: ["Matia, 25, 1.58 ["Maçã", "banana", "Uva"], "solteira"]. 
# Mude a fruta "banana" para "Melancia" e mostre na tela a lista atualizada.
# lista = ["Matia, 25, 1.58 ["Maçã", "banana", "Uva"], "solteira"]
# lista[3][1] = "Melancia"
# print(lista)

#Faça um programa que pede ao usuário que digite 5 frutas e adicione as 5 frutas na lista de frutas ja existente: ["uva", "pera", "melão"]
# frutas = ["uva", "pera", "melao"]
# qt_frutas = 0
# for i in range(5):
#     frutas.append(input("Digite o nome da fruta: "))

# Mesma atividade com While
# lista_frutas = []
# qtd_frutas = int(input("Quantas frutas você deseja inserir no carrinho? "))

# while len(lista_frutas) < qtd_frutas:
#     # fruta = str(input("Digite o nome da fruta: "))
#     lista_frutas.append(str(input("Digite o nome da fruta: ")))
# print(lista_frutas)

#Dado a lista: ["Uva", "pera","melão","maçã", "banana", "acerola"] Faça um programa que pergunta ao usuário qual fruta ele quer excluir (A posição da fruta) e exclua ela:
# frutas= ["Uva", "pera","melão","maçã", "banana", "acerola"]
# pos = int(input("""Qual a fruta que você quer retirar? 
#                 [1: Uva: 
#                 2- Pera
#                 3- Melão
#                 4- Maçã
#                 5- Banana
#                 6- Acerola"""))
# frutas.pop(pos-1)
# print(frutas)

# Dado a lista: ["Uva", "pera","melão","maçã", "banana", "acerola"], Faça um programa que pergunta se o usuário quer remover a ultima fruta ou se ele quer remover pela posição;
# se ele escolher a primeira opção, remova a ultima fruta, se escolher a segunda, pergunte ao usuário qual a posição, para sair do programa o usuário deve digitar "0"
# lista_frutas = ["Uva", "pera","melão","maçã", "banana", "acerola"]
# while True:
#     print(lista_frutas)
#     op = int(input(f"""
#                 {lista_frutas}
#                 O que você quer fazer? 
#                 1- Excluir ultimo
#                 2- Excluir pela posição
#                 0- Sair:
#                    """))
#     if op == 0:
#         break
#     elif op == 1:
#         lista_frutas.pop()
#     elif op == 2:
#         print(lista_frutas)
#         pos = int(input("Qual posição da fruta você quer deletar? "))
#         lista_frutas.pop(pos-1)
#     else:
#         print("Opção inválida! ")

#utilizando metodo remove

# Iteração de listas
#Faça um programa que itere sobre uma lista de frutas e print na tela "eu achei uma uva" sempre que ele econtrar uma fruta digitada pelo usuário:
lista_frutas = ["uva", "pera", "abacaxi", "laranja", "uva", "banana", "uva"]
for fruta in lista_frutas:
    if fruta == "uva":
        print(f"Eu achei uma uva")

lista_fruta = []
