#10.MAIOR DE 3: Faça um programa que pede 3 números inteiros para o usuário e mostra na tela qual o maior dos três ou se eles são iguais.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior número")
elif num3 > num1 and num3 > num2:
    print(f"O número {num3} é o maior número")
elif num1 == num2 and num1 == num3:
    print("Os números são iguais!")
