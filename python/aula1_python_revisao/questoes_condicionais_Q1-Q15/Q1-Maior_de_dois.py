#1. MAIOR DE DOIS: Faça um programa que pede 2 números inteiros para o usuário e mostra na tela qual o maior dos dois ou se ele são iguais.
num = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número: "))
if num > num2:
    print(f"O numero {num} é maior que {num2}")
elif num2 > num:
    print(f"O numero {num2} é maior que {num}")
elif num == num2:
    print(f"O numero {num2} e {num} são iguais!")
else:
    print("Número inválido")
