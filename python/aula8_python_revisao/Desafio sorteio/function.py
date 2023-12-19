
def nome_valido():
    while True:
        nome = str(input("Digite o nome do cliente: "))
        if all(c.isalpha() or c.isspace() for c in nome):
            return nome
        else:
            print("Por favor digite um nome válido (somente letras e espaços)")


# Validação Franco
def cpf_valido():
    while True:
        cpf = input("Digite a cpf do cliente:  ")
        if cpf.isdigit():  # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
            if len(cpf)!= 11:
                print("CPF deve 11 digitos. Tente novamente.")
            else:
                cpf = int(cpf)
                return cpf
        else:
            print("Não digitou uma cpf válida. Tente novamente.")

def valor_valido():
    while True:
        valorDigitado = input("Digite a valor da compra:  ")
        try:
            valor = float(valorDigitado)
            if valor > 0:
                return valor
            else:
                print("A entrada não é um número positivo valido. Tente novamente.")
            # if valor.isdigit():  # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
            #     valor = float(valor)
            #     return valor
            # else:
            #     print("Não digitou um valor válido. Tente novamente.")
        except ValueError:
        # Se ocorrer um erro durante a conversão, imprime uma mensagem de erro e continua no loop
            print("A entrada não é um número válido. Tente novamente.")

def maior_compra(lista_clientes):
    maior_valor = 0
    for valor in lista_clientes:
        if valor.get("valor_compra") > maior_valor:
            maior_valor = valor.get("valor_compra")
        if maior_valor == 0:
            return "Digite um valor positivo"
    return maior_valor