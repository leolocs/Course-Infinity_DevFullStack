#8.DIA DA SEMANA: Faça um programa que pede pro usuário escrever um número inteiro entre 1 e 7 e mostre o dia da semana respectivo ao número digitado (1 - domingo, 2 - segunda e etc)
while True:
    dia = int(input("Digite um dia da semana entre 1 a 7: "))
    if dia == 0:
        break
    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda")
        case 3:
            print("Terça")
        case 4:
            print("Quarta")
        case 5:
            print("Quinta")
        case 6:
            print("Sexta")
        case 7:
            print("Sábado")
        case _:
            print("Número da semana inválido, digite um npumero válido entre 1 a 7")