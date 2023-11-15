#11. DIVISÍVEL POR 3 E 5: Faça um programa que pede para o usuário escrever um número inteiro positivo e mostre na tela se aquele número é ou não divisível por 3 e por 5 ao mesmo tempo.
while True:
    num = int(input("Digite um número positivo: "))
    if num == 00:
        break
    if num <= 0:
        print("Esse número não é positivo, digite um número positivo!")
    else:
        if num % 3 == 0 and num %5 == 0:
            print(f"Esse número {num} é divisível por 3 e 5")
        else:
            print("O numero digitado não é divisivel por 3 e 5 ao mesmo tempo")