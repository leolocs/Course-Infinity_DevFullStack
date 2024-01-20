#Q10.Faça um programa que pede 10 números inteiros para o usuário, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
n_par = 0
n_impar = 0

for n in range(1,11):
    num = int(input(f"Digite um o {n}º número: "))
    if num %2 == 0:
        n_par += 1
    elif num %2 != 0:
        n_impar += 1
print(f"A quantidade de numeros pares é {n_par}, e de números impares é: {n_impar}")