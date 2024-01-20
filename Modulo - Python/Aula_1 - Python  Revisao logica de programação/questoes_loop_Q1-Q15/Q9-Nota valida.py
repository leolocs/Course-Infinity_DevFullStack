#Q9.Faça um programa que pede para o usuário uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    num = int(input("Digite uma nota de 0 a 10: "))
    if num <= 0:
        print("Digite uma nota maior que zero 0!")
    break