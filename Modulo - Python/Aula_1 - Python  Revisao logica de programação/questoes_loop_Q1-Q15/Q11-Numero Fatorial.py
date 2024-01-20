#Q11.Faça um programa que pede para o usuário digitar um número inteiro e positivo e mostre na tela o fatorial desse número.
num_fat = 0
while True:
    num = int(input("Digite um número inteiro positivo: "))
    if num <= 0:
        print("Digite um número maior que zero 0")
    else:
        num_fat = num**2
        print(num_fat)
        break