#Q12.Faça um programa que pede 2 números para o usuário e exibe um menu perguntando qual operação matemática ele quer realizar 
# ou se ele quer encerrar o programa e exiba o resultado na tela a cada escolha do usuário.
print("### CALCULADORA ###")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
while True:
    res = 0
    ope = int(input("""
                    Digite o numero da operação desejada: 
                    1: Adição + 
                    2: Subtração - 
                    3: Multiplicação * 
                    4: Divisão /
                    0: Sair
                    :
                    """))
    match ope: 
        case 1:
            res = num1+num2
            print(f"A soma é: {res}")
            break
        case 2:
            res = num1 - num2
            print(f"A subtração é: {res}")
            break
        case 3:
            res = num1*num2
            print(f"A multiplicação é: {res}")
            break
        case 4:
            if num2 != 0:
                res = num1/num2
                print(f"A divisão é: {res}")
                break
            else:
                print("Número não pode ser dividio por zero")
        case _:
            print("Operação inválida, digite uma operação válida!")