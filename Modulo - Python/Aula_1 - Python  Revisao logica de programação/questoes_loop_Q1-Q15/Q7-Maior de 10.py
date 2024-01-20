#Q7.Faça um programa que pede para o usuário digitar 10 números inteiros e mostre na tela qual maior número que foi digitado.

num_maior = 0
for n in range(1,11):
    num = int(input(f"Digite o {n}º número: "))
    if num > num_maior:
        num_maior = num
print(f"O maior número digitado é o: {num_maior}")