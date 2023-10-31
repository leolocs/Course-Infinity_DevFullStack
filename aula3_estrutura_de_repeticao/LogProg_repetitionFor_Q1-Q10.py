# #region - Q1: Faça um programa para imprimir os números de 1 a 10. Utilize a função range() para criar a coleção de números.
# for i in range(1,11):
#     print(i)
# #endregion

# #region Q2: Faça um programa para imprimir os números pares de 1 a 20. Utilize a função range() para criar a coleção de números.
for i in range(1,21):
    if i % 2 == 0:
        print(i)
# #endregion

# #region Q3: Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a função range() para criar a coleção de números.
for i in range(1,20):
    if i %2 != 0:
        print(i)
#endregion
#region Q4: Faça um programa para calcular a soma dos números de 1 a 100. Utilize a função range() para criar a coleção de números.
# soma = 0
# for i in range(1,101):
#     soma += i
# print(soma)
#endregion

# # region Q5: Faça um programa para calcular a média de uma lista de 10 números.
# soma = 0

# for i in range(10):
#     num = float(input(f"Digite o {i}º número: "))
#     soma += num
# media = soma / 10
# print(f"A média é: {media}")
# #endregion

# #region Q6: Faça um programa para verificar se um número é primo. Utilize a condicional IF dentro do laço FOR.
# num = int(input("Digite um número: "))

# if num <=1:
#     print("Número não primo")
# #endregion

#region Q7: Faça um programa para imprimir os caracteres de uma string separadamente.
# palavra = str(input("Digite uma palavra: "))
# for letra in palavra:
#     print(letra)

#endregion

#region Q8: Faça um programa para contar quantas vogais existem em uma palavra. Utilize a condicional IF dentro do laço FOR.
palavra = str(input("Digite uma palavra: ")).lower()
vogal = "aeiou"
contador = 0

for letra in palavra:
    if letra in vogal:
        contador += 1
print(f"A palavra tem {contador} vogais")
#endregion

#region Q9: Faça um programa para contar quantas consoantes existem em uma palavra. Utilize a condicional IF dentro do laço FOR.
palavra = str(input("Digite uma palavra: ")).lower()
contador = 0

for letra in palavra:
    if letra not in "bcdfghjklmnpqrstvwxyz":
        contador += 1
print(f"A palavra tem {contador} consoantes")
#endregion

#region Q10: Faça um programa para verificar se uma palavra é um palíndromo. Exemplo: ‘amor’ = ‘roma’ (NÃO É) / ‘arara’ = ‘arara’ (É PALÍNDROMO).
palavra = str(input("Digite uma palavra: ")).lower().strip
invertida = palavra[::-1]
if palavra == invertida:
    print(f"A palavra ou frase {palavra} é um Palindromo")
else:
    print(f"A palavra ou frase {palavra} não é um Palindromo")

#endregion

#region Q11: Faça um programa que solicite uma senha e verifica se a senha digitada é forte, a Senha deve: 
