#6.MÉDIA: Faça um programa que pede para o usuário escrever 3 notas, calcule a média e mostre se ele foi aprovado (acima de 7) ou reprovado
media = 0
n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
soma = n1+n2+n3
media = soma/3
if media < 7:
    print("Reprovado!")
elif media > 7 and media < 10:
    print("Aprovado!")
elif media == 10:
    print("Aprovado com distinção!")