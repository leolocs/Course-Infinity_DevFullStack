# Q4. Function Calculadora: Crie Funções para calcular de acordo com os operadores matemáticos de uma calculadora:
# ●somar(parm1, parm2)
# ●subtracao(parm1, parm2)
# ●multiplicacao(parm1, parm2)
# ●divisao(parm1, parm2)

# Em seguida, escreva um programa que receba dois números inteiros ou float e que possa calcular esses números de acordo com a escolha dos usuários sob operadores.
# • Use um laço de repetição infinito e verifique a cada resultado da operação selecionada se o usuário deseja continuar calculando, se não, interrompa o loop e finalize o programa.
# • Use bloco condicional para chamar a função apropriada
# • Crie comentarios em seus códigos
# • utilize type hint
# • A função de divisão deverá informar ao usuário uma mensagem de erro se o divisor for igual a zero

def somar(num1: float, num2: float): #Função de soma 
    soma = num1 + num2
    return soma

def subtrai(num1:float, num2:float): #Função da subtração
    subtracao = num1-num2
    return subtracao

def multipli(num1:float,num2:float): #Função da multiplicação
    multi = num1*num2
    return multi

def dividir (num1:float, num2:float): #Função da divisão
    if num1 or num2 == 0:
        print("Digite um número maior que zero 0")
    else:
        divisao = num1/num2
        return divisao

print("########## Função Calculadora ##########")
while True:                                         #Loop infinito aonde o usuário só sai quando digitar o numero 0
    oper = int(input(print("""\n Qual cálculo gostaria de realizar?
          0- Sair
          1- Soma
          2- Subtração
          3- Multiplicação
          4- Divisão
          : """)))
    if oper == 0:
        break
                # Match case para verificar qual a operação o usuário deseja realizar 
    match oper:
        case 1:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"A soma dos números é: {(somar(num1=n1, num2=n2))}")
        case 2:
            n1 = float(input("Digite o minuendo: "))
            n2 = float(input("Digite o subtraendo: "))           
            print(f"O resto da subtração é: {subtrai(num1=n1,num2=n2)}")
        case 3:
            n1 = float(input("Digite o multiplicando: "))
            n2 = float(input("Digite o multiplicador: "))
            print(f"O produto da multiplicação é: {(multipli(num1=n1,num2=n2))}")
        case 4:
            n1 = float(input("Digite o dividendo: "))
            n2 = float(input("Digite o divisor: "))
            print(f"O quociente da divisão é: {dividir(num1=n1,num2=n2)}")
        
