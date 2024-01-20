#Q8.Faça um programa que pede para o usuário digitar 10 números inteiros e mostre na tela qual menor número que foi digitado.
num_menor = float('inf')
for n in range(1,11):
    num = int(input(f"Digite o {n}º número: "))
    if num < num_menor:
        num_menor = num
print(f"O menor número digitado foi o {num_menor}")