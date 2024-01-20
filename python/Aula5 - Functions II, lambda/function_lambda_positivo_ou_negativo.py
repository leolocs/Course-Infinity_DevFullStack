pos_neg = lambda numero: f"O {numero} é positivo" if numero > 0 else f"O número {numero} é negativo"

while True:
    numero = int(input("Digite um número que não seja 0: "))
    if numero == 0:
        break
    print(pos_neg(numero))