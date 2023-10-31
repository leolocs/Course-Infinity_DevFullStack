#region - Q1: Faça um programa que solicite um número ao usuário e imprima se o número é impar ou par.
# numero = int(input("Digite um número: "))
# if numero %2 == 0:
#     print(f"Esse número {numero} é par!")
# elif numero %2 !=0:
#     print(f"Esse número {numero} é impar!")
# else:
#     print("Número inválido")
#endregion
#region - Q2: Faça um programa que peça dois números e imprima o maior deles.
# num1 = int(input("Digite um número:"))
# num2 = int(input("Digite outro número: "))

# if num1 and num2 >=0:
#     print("Número válido")
#     if num1 > num2:
#         print(f"{num1} é o número maior")
#     elif num2 > num1:
#         print(num2,"é o número maior")
#     else:
#         print("Números iguais")
# else:
#     print("Número inválido")
#endregion

#region - Q3: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# num = float(input("Digite um número: "))

# if num > 0:
#     print("Número positivo")
# elif num < 0:
#     print("Número negativo")
# else:
#     print("Número neutro")
#endregion

#region - Q4: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Escrevendo: F - Feminino, M - Masculino, Sexo Inválido.
# letra = str(input("Qual seu sexo: M/F?: ")).lower()

# if letra == "m":
#     print("M - Sexo Masculino")
# elif letra == "f":
#     print("F - Sexo Feminino")
# else:
#     print("Sexo inválido")
#endregion

#region - Q5: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# letra = str(input("Digite uma letra para verificar: ")).lower().strip()

# if len(letra) == 1:
#     if letra in "aeiou":
#         print("Letra vogal")
#     elif letra in "bcdfghjklmnpqrstwxyz":
#         print("letra consoante")
# else:
#     print("Digite apenas UMA letra!!")
    

#endregion

#region - Q6: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# nota1 = float(input("Digite uma nota: "))
# nota2 = float(input("Digite outra nota: "))
# media = (nota1+nota2)/2

# if media >= 7 and  media < 10:
#     print("Aprovado")
# elif media < 7:
#     print("Reprovado")
# elif media == 10:
#     print("Aprovado com distinção!")
#endregion

#region - Q7:Faça um Programa que leia três números e mostre o maior deles.
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um segundo número: "))
# num3 = int(input("Digite um terceiro número: "))

# if num1 > num2 and num1 > num3:
#     print(f"Número {num1} é o maior número")
# elif num2 > num1 and num2 > num3:
#     print(f"Número {num2} é o maior número")
# elif num3 > num1 and num3 > num2:
#     print(f"Número {num3} é o maior número")
#endregion

#region - Q8: Faça um Programa que leia três números e mostre o maior e o menor deles.
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um segundo número: "))
# num3 = int(input("Digite um terceiro número: "))
# maior = num1
# menor = num1

# if num2 > maior:
#     maior = num2
# if num3 > maior:
#     maior = num3
# if num2 < menor:
#     menor = num2
# if num3 < menor:
#     menor = num3
# print(f"O maior número é {maior} e o menor número é {menor}")

#endregion

#region - Q9: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# prod1 = float(input("Informe o valor do primeiro produto: "))
# prod2 = float(input("Informe o valor do segundo produto: "))
# prod3 = float(input("Informe o valor do terceiro produto: "))


# if prod1 < prod2 and prod1 < prod3:
#     print(f"O produto {prod1} é o produto mais barato")
# if prod2 < prod1 and prod2 < prod3:
#     print(f"O produto {prod2} é o produto mais barato")
# if prod3 < prod1 and prod3 < prod2:
#     print(f"O produto {prod3} é o produto mais barato")
#endregion

#region - Q10: Faça um Programa que leia três números e mostre-os em ordem decrescente.
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite um segundo número: "))
# n3 = int(input("Digite um terceiro número: "))

# if n1 >= n2 and n2 >= n3:
#     print(f"Ordem decresente: {n1,n2,n3}")
# if n1 >= n3 and n3 >= n2:
#     print(f"Ordem decrescente: {n1,n3,n2}")
# if n2 >= n1 and n1 >= n3:
#     print(f"Ordem decresente: {n2,n1,n3}")
# if n2 >= n3 and n3 >= n1:
#     print(f"Ordem decresente: {n2,n3,n1}")
# if n3 >= n1 and n1 >= n2:
#     print(f"Ordem decresente: {n3,n1,n2}")
# if n3 >= n2 and n2 >= n1:
#     print(f"Ordem decresente: {n3,n2,n1}")

# Mesma questão porém utilizando listas[]:
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um segundo número: "))
# num3 = int(input("Digite um terceiro número: "))

# #criando lista com 3 números
# numeros = [num1, num2, num3]

# #ordena a lista dos números em decresente
# numeros.sort(reverse=True)
# print(f"A ordem decrescente dos números é: {numeros[0], numeros[1], numeros[2]}")
#endregion

#region - Q.11: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# turno = str(input("Em qual turno você estuda? M - Matutino, V - Vespertino, N - Noturno: ")).lower().strip()

# if turno == "m" or "v" or "n":
#     if turno == "m":
#         print("Bom dia!")
#     elif turno == "v":
#         print("Boa tarde!")
#     elif turno == "n":
#         print("Boa noite!")
#     else:
#         print("Opção inválida!")
# Mesma questão utilizando IN:
# turno = str(input("Em qual turno você estuda?")).strip().lower()
# turno = [m, v, t, n]
# if turno in "mvtn":
#     if turno in "m":
#         print("Bom dia!")
#     elif turno in "v" or "t":
#         print("Boa tarde!")
#     elif turno in "n":
#         print("Boa noite!")
#     else:
#         print("Opção inválida!")
#endregion 