#3.PÁR OU ÍMPAR: Faça um programa que pede um número inteiro e positivo para o usuário e mostre na tela se aquele número é par ou ímpar.
while True:
    num = int(input("Digite um número inteiro e positivo: "))
    if num == -0:
        break
    elif num <= 0:
        print(f"Número {num} é menor ou igual a zero, digite um número válido!")
    elif num %2 == 0:
        print(f"O numero {num} é par!")
        break
    elif num %2 != 0:
        print(f"O número digitado é ímpar!")
        break