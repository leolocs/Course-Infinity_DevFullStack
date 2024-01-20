#Faça um programa que pede para o usuário digitar um número inteiro e positivo e mostre na tela se ele é ou não um número primo.
while True:
    num = int(input("Digite um número inteiro positivo: "))
    if num <= 1:
        print("Digite um número inteiro positivo maior que zero e 1")
    else:
        for i in range(2, int(num**0.5) + 1):
            print(f"O número {num}  é positivo e é um numero primo")
            if num % i == 0: