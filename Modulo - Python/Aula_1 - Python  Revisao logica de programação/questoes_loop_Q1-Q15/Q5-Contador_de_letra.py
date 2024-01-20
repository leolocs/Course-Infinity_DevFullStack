#Q5.Faça um programa que pede para o usuário digitar uma frase e conte quantas letras A existem na frase e mostre na tela a quantidade encontrada
palavra = str(input("Digite uma palavra ou frase: "))
letra = str(input("Qual letra gostaria de contar na palavra ou frase digitada? "))
count = 0

if len(letra) == 1:
    for l in palavra.lower().strip():
        if l == letra:
            count += 1
else:
    print("Digite apenas uma letra para verificação")

print(f"Existe {count} letras '{letra}' na palavra ou frase {palavra}")
