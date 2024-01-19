#region - Q1: Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre essa lista e exiba cada número elevado ao quadrado.
# list_num = [2, 5, 8, 11, 14]

# for num in list_num:
#     print(num**2)
#endregion

#region - Q2: Dada a tupla de nomes de países: ("Brasil", "Canadá", "Austrália", "Espanha", "Índia"), crie um programa que itere sobre a tupla e exiba na tela  cada país 
# seguido pelo número de caracteres presentes em seu nome.
# tupla_paises = ("Brasil", "Canadá", "Austrália", "Espanha", "Índia")
# for pais in tupla_paises:
#     caracter = len(pais)
#     print(f"O país {pais} tem {caracter} caracteres.")
#endregion

#region - Q3: Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu preço. 
#Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
lista_frutas = [
    ("Maçã", 2.50), 
    ("Banana", 1.75),
    ("Laranja", 3.00)
    ]
soma = 0

for tupla in lista_frutas:
    soma += tupla[1]

print(f"A soma dos produtos é: {soma}")

#endregion

#region - Q4:Considere a seguinte lista de palavras: ["Python", "é", "uma", "linguagem", "poderosa"]. 
#Escreva um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4 letras.

#endregion
