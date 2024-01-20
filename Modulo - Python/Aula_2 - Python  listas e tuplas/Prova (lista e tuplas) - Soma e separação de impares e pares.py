# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista,
# e a soma de todos os números pares e ímpares, respectivamente.

lista_num = []
for num in range(10):
    lista_num.append(int(input(f"Digite o {num+1} número: ")))

#List Comprehension:
num_pares = [n for n in lista_num if n %2 == 0]
qtd_pares = 0
for n in num_pares:
    qtd_pares += 1

num_impares = [n for n in lista_num if n %2 != 0]
qtd_impares = 0
for n in num_impares:
    qtd_impares += 1


print(f"""
    Números Pares: {num_pares} 
    Números impares: {num_impares}
    Quantidade de numeros pares: {qtd_pares}
    Quantidade de numeros impares: {qtd_impares}
    Soma de todos os números: {sum(lista_num)}
    Soma dos números pares: {sum(num_pares)}
    Soma dos números impares: {sum(num_impares)}
""")



