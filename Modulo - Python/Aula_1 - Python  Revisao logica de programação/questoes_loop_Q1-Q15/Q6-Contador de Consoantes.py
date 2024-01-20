#Q6.Faça um programa que pede para o usuário digitar uma frase e mostre na tela quantas consoantes existem naquela frase.
consoantes = "bcdfghjklmnpqrstvxwyz"
frase = str(input("Digite uma frase: ")).lower().strip()
count = 0
for letra in frase:
    if letra in consoantes:
        count += 1
print(f"Existem '{count}' letras consoantes na frase {frase}")