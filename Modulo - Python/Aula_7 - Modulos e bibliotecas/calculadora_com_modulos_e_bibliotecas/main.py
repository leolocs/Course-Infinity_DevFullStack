from calculadora import *



# Crie um programa que será uma calculadora.

# Nesta calculadora você deverá ter um módulo para as operações matemáticas, o arquivo principal deverá conter apenas um menu de escolha para o usuário
# (soma, subtração, multiplicação e divisão).

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
    
while True:
    op = int(input("""
                        Digite qual opeação deseja realizar: 
                        1- Multiplicação
                        2- Divisão
                        3- Adição
                        4- Subtração
                        0- Sair
                        """))
    match op:
        case 1:
            multiplicar(n1=num1, n2=num2)
        case 2:
            dividir(n1=num1, n2=num2)
        case 3:
            somar(n1=num1, n2=num2)
        case 4:
            subtrair(n1=num1, n2=num2)
        case 0:
            break
        case _:
            print("Opção inválida")