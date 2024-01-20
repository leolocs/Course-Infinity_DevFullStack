#Q1. Faça um programa que pede 1 número inteiro entre 1 e 10 para o usuário e mostre na tela a tabuada desse número.
num = int(input("Digite o número para a tabuada: "))

for n in range (1,11):
    print(f"{num} X {n} = {num*n}")