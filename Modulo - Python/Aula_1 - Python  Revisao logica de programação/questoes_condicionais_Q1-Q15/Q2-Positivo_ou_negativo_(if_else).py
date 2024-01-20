#2.POSITIVO OU NEGATIVO: Faça um programa que pede para o usuário digitar um número inteiro e mostra na tela se o número digitado é positivo, negativo ou neutro
while True:
    num = int(input("Digite um numero inteiro: "))
    if num == -0:
        break
    elif num > 0:
        print("Número digitado é positivo!")
    elif num < 0:
        print("Numero digitado é negativo")
    elif num == 0:
        print("Número digitado é neutro")
    else:
        print("Número inválido")