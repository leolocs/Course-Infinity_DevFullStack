#region - Q1: Faça um programa que peça dois números e imprima o maior deles.
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

#region - Q2: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# num = float(input("Digite um número: "))

# if num > 0:
#     print("Número positivo")
# elif num < 0:
#     print("Número negativo")
# else:
#     print("Número neutro")
#endregion

#region - Q3: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Escrevendo: F - Feminino, M - Masculino, Sexo Inválido.
# letra = str(input("Qual seu sexo: M/F?: ")).lower()

# if letra == "m":
#     print("M - Sexo Masculino")
# elif letra == "f":
#     print("F - Sexo Feminino")
# else:
#     print("Sexo inválido")
#endregion

#region - Q4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra para verificar: ")).lower().strip()

if len(letra) == 1:
    if letra in "aeiou":
        print("Letra vogal")
    elif letra in "bcdfghjklmnpqrstwxyz":
        print("letra consoante")
else:
    print("Digite apenas UMA letra!!")
    

#endregion

#region - Q5: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
media = (nota1+nota2)/2

if media >= 7 and  media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção!")
#endregion

#region - Q6:Faça um Programa que leia três números e mostre o maior deles.

#endregion
