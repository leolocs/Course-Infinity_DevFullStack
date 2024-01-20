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
# num = int(input("Digite um número: "))
# for n in range(1,11):
#     print(f"{num} x {n} = {num*n}")
#endregion

#region - 3.Escreva um programa que solicite ao usuário uma frase e conte quantas vogais (a, e, i, o, u) existem nessa frase.
# from unidecode import unidecode
# palavra = str(input("Digite uma Palavra ou frase: ")).lower().strip()
# count = 0
# for letra in palavra:
#     if letra in "aeiou":
#         count += 1
# print(f"A frase ou palavra digitada possui {count} vogais")
#endregion

#region - 4. Escreva um programa que possa verificar uma sequência de 10 números se são par ou ímpar.
# for n in range(10):
#     numero = int(input("Digite um numero: "))
#     if numero %2 == 0:
#         print(f"Número {numero} é par")
#     elif numero %2 != 0:
#         print(f"O número {numero} é ímpar")
#     else:
#         print(f"Número invalido")
#endregion

#region - 5. Hora de otimizar a questão número 3, após ter criado seu programa que conta quantas vogais existem numa frase, implemente mais uma
#funcionalidade. O programa agora deve imprimir a quantidade de vogais e consoantes encontradas.
palavra = str(input("Digite uma Palavra ou frase: ")).lower().strip()
vogais = 0
cons = 0
for letra in palavra:
    if letra in "aeiou":
        vogais += 1
    elif letra in "acdfghjklmnpqrstvwxyz":
        cons += 1
print(f"""
        A frase ou palavra digitada possui {vogais} vogais;
        E possui {cons} consoantes
        """)
#endregion
#endregion - Revisão Python, Questões 1-5