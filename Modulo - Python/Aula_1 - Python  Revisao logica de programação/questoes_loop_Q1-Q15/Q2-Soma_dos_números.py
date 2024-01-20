#Q2. Faça um programa que pede para o usuário digitar 10 números e mostre na tela a soma de todos os números digitados.
soma = 0
for n in range(1,11):
    num = int(input(f"Digite o {n}º número: "))
    if num <= 0:
        print("Digite um número válido maior que zero!")
    else:
        soma += num
print(f"A soma dos números digitados é: {soma}")