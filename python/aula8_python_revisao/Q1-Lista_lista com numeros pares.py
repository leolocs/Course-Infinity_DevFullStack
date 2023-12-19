# Dada uma lista de numeros, crie uma nova lista contendo apenas os números pares.

lista_num = []
num_pares = []

for n in range(1,11):
    num = int(input(f"Digite o {n}º numero: "))
    lista_num.append(num)

for n in lista_num:
    if n %2 == 0:
        num_pares.append(n)

print(f"Os numeros pares dos números passados são: {num_pares}")