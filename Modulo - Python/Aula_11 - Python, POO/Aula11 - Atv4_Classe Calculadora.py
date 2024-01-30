# Crie uma classe Calculadora que tenha métodos
# para realizar operações matemáticas básicas 
# (+ , - ,*, / ).

class Calculadora:
    def __init__(self) -> None:
        self.resultado = 0

    def somar(self, num1:float,num2:float):
        self.resultado = num1 + num2
        return self.resultado

    def subtrair(self, num1:float,num2:float):
        self.resultado = num1 - num2
        return self.resultado
    
    def multiplicar(self, num1:float,num2:float):
        self.resultado = num1 * num2
        return self.resultado
    
    def dividir(self, num1:float,num2:float):
        if num2 != 0:
            self.resultado = num1/num2
            return self.resultado
        else:
            print("O número não pode ser digitado por zero")

calculadora1 = Calculadora()

while True:
    menu = int(input("""
        Escolha a operação que deseja:
        1 - Soma
        2 - Subtrair
        3 - Dividir
        4 - Multiplicar
"""))
    
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo número: "))
    
    match menu: 
        case 1: #Somar
            print (calculadora1.somar(num1 = n1, num2=n2))
        case 2: #Subtrair
            print (calculadora1.subtrair(num1=n1, num2=n2))
        case 3: #Dividir
            print (calculadora1.dividir(num1=n1, num2=n2))
        case 4: #Multiplicar
            print(calculadora1.multiplicar(num1=n1,num2=n2))
        case _:
            print("Opção inválida")
