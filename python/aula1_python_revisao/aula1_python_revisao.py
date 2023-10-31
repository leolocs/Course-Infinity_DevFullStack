
#region - Revisão Estrutura condição: IF, ELIF, ELSE, MATCH CASE
#region: Faça um programa que pede ao usuário uma cor do semáforo, entre verde,amarelo, vermelho:
# UTILIZANDO if, elif, else
# while True:
#     cor = str(input("Digite uma cor entre verde, amarelo ou vermelho: ")).lower().strip()
#     if cor == "verde":
#         print("Sinal verde, acelere!")
#         break
#     elif cor == "amarelo":
#         print("Atenção!, sinal amarelo!")
#         break
#     elif cor == "vermelho":
#         print("PARE!, Sinal vermelho!")
#         break
#     else:
#         print("Cor inválida, digite uma cor válida!")

# UTILIZANDO Match case
# cor = str(input("Digite uma cor entre verde, amarelo ou vermelho: ")).lower().strip()
# match cor:
#     case "verde":
#         print("Sinal verde, acelere!")
#     case "amarelo":
#         print("Atenção!, sinal amarelo!")
#     case "vermelho":
#         print("PARE!, Sinal vermelho!")
#     case _:
#         print("Cor inválida!")

#UTILIZANDO entrada de dados INT:
# cor = int(input("""Escolha uma cor do semáforo:
#                 1 - Verde
#                 2 - Amarelo
#                 3 - Vermelho
#                 """))
# match cor:
#     case "verde":
#         print("Sinal verde, acelere!")
#     case "amarelo":
#         print("Atenção!, sinal amarelo!")
#     case "vermelho":
#         print("PARE!, Sinal vermelho!")
#     case _:
#         print("Cor inválida!")
#endregion

#region: Condição: Faça um programa que pede ao usuário 3 números inteiros e mostre na tela qual o maior deles
# while True
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite outro número: "))
#     num3 = int(input("Digite outro número: "))
#     if num1 != num2 and num1 != num3 and num2 != num3: 
#         if num1 > num2 and num1 > num3:
#             print(f"O número {num1} é o maior número")
#         elif num2 > num1 and num2 > num3:
#             print(f"O número {num2} é o maior número")
#         elif num3 > num1 and num3 > num2:
#             print(f"O número {num3} é o maior número")
#     else:
#         print("Digite numeros diferentes!")
#     break
#endregion

#region: Q1.Condição: Faça um programa que peça 2 números ao usuário e imprima o maior número.
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# if num1 != num2:
#     if num1 > num2:
#         print(f"O número {num1} é o maior número")
#     if num2 > num1:
#         print(f"O número {num2} é o maior número")
# else:
#     print("Digite números diferentes!")
#endregion

#region: Q2.Condilção: Faça um programa que pede ao usuário um valor e mostre na tela se o valor é positivo ou negativo.
# num = float(input("Digite um número: "))
# if num > 0:
#     print("Número positivo!")
# elif num < 0:
#     print("Número negativo")
#endregion

#region: Q3.Condição: Faça um programa que imprima na tela "Feminino", "Masculino" ou sexo inválido a partir de uma letra digitada: 
# F para feminino, M para masculino e qualquer outra letra para sexo inválido 
# sexo = str(input("Escreva qual o sexo: M para Masculino ou F para Feminino: ")).lower().strip()
# if len(sexo) == 1:
#     match sexo:
#         case "m":
#             print("Sexo Masculino")
#         case "f":
#             print("Sexo Feminino")
#         case _:
#             print("Sexo inválido!")
# else:
#     print("Digite apenas uma letra!")
#endregion

#region: Q4.Condição: Faça um programa que verifique se a letra digitada pelo usuário é vogal ou consoante.
# letra = str(input("Digite uma letra: "))
# if len(letra) == 1:
#     if letra in "aeiou":
#         print("A letra digitada é vogal!")
#     elif letra in "bcdfghjklmnpqrstvwxyz":
#         print("A letra digitada é consoante!")
# else:
#     print("Digite apenas uma letra!")
#endregion

#region: Q5.Condição: Faça um programa que leia 4 notas de um aluno e calcule a média e imprima:
# "Aprovado" se a media for maior ou igual a 7;
# "Reprovado" se a media for a baixo de 7;
# "Aprovado com distinção" se a média for igual a dez 10;
# nota1 = float(input("Digite uma nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# nota3 = float(input("Digite a 3ª nota: "))
# nota4 = float(input("Digite a 4ª nota: "))
# media = 0
# media = (nota1+nota2+nota3+nota4) /4
# if media >=7 and media < 10:
#     print("Aprovado!")
# elif media < 7:
#     print("Reprovado!")
# elif media == 10:
#     print("Aprovado com distinção")
#endregion

#region: Q6.Condição: Faça um programa que receba 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# o resultado da operação deve aparecer com uma frase que diga se o número digitado é:
# • Positivo ou negativo
# • Par ou Ímpar
# cal = 0
# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite outro número: "))
# oper = str(input("""Qual operação deseja realizar: (+ | - | * | /)? 
#                  +: Soma
#                  -: Subtração
#                  *: Multiplicação
#                  /: Divisão
#                  : """))
# if len(oper) == 1 and oper not in ("+-*/"):
#     match oper:
#         case "+":
#             cal = num1 + num2
#             print(cal)
#         case "-":
#             cal = num1 - num2
#             print(cal)
#         case "*":
#             cal = num1 * num2
#             print(cal)
#         case "/":
#             cal = num1 / num2
#             print(cal)
#         case _:
#             print("Digite uma operação válida!")
# if cal %2 == 0:
#     print(f"Resultado {cal} da operação é par!")
# else:
#     print(f"Resultado {cal} da operação é impar")

# if cal <= 0:
#     print(f"Resultado {cal} é positivo")
# else:
#     print(f"Resultado {cal} é negativo")
#endregion

#region: Condição: Faça um programa que solicite ao usuário um nome e mostre quantas letras "A" o nome possui.
# nome = str(input("Digite um nome: ")).strip()
# letra = str(input("Qual letra gostaria de encontrar? ")).lower().strip()
# count = 0
# for let in nome:
#     if let.lower() == letra:
#         count += 1
# print(f"O nome {nome} possui {count} {letra}")
#endregion
#endregion

#region - Revisão Repetição: FOR, RANGE
#region - Repetição: Faça um programa que imprima na tela os números de 5 a 50.
# for n in range (5,51):
#     print(n)
#endregion

#region - Repetição: Faça um programa que mostre os números de 10 a 100, porém apenas os que forem divisíveis por 3 e 5 ao mesmo tempo.
# for n in range(10,101):
#     if n %3 ==0 and n %5 == 0:
#         print(n)
#endregion

#region - Repetição: Faça um programa que pede ao usuário digitar 5 numeros e no final mostra a soma dos 5 números digitados. 
# soma = 0
# for n in range(1,6):
#     num = float(input(f"Digite o {n}º número: "))
#     soma = soma + num
# print(f"A soma dos números digitados é: "{soma})
#endregion
#endregion - Revisão Repetição

#region - Revisão repetição: WHILE, TRUE, BREAK
#Faça um programa que pede para o usuário escrever o nome de uma fruta e que fique preso num loop infinito até o usuário escrever "fim" no lugar do nome da fruta.
# while True:
#     fruta = str(input("Digite o nome de uma fruta: "))
#     if fruta.lower() == "fim":
#         break
#endregion

#region - Revisão Python, Questões 1 a 5
#region - 1.Escreva um programa que solicite ao usuário um número inteiro positivo e realize uma contagem regressiva a partir desse número até zero, imprimindo cada número no processo.
# while True:
#     numero = int(input("Digite um número: "))
#     for n in range(numero, -1, -1):
#         print(n)
#     break
# #Com WHILE    
# while numero >= 0:
#     print(numero)
#     numero -= 1
#endregion

#region - 2.Escreva um programa que solicite ao usuário um número inteiro e imprima a tabuada desse número, de 1 a 10.
num = int(input("Digite um número: "))
for n in range(1,11):
    print(f"{num} x {n} = {num*n}")
#endregion

#region - 3.

#endregion

#endregion - Revisão Python, Questões 1-5