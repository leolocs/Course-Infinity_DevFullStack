#4.VOGAL OU CONSOANTE: Faça um programa que pede para o usuário escrever uma letra qualquer e mostre na tela se ele digitou uma vogal ou uma consoante ou outro caracter.
while True:
    letra = str(input("Digite uma letra: "))
    if letra == "sair":
        break
    if len(letra) > 1:
        print("Digite apenas uma letra: ")
    elif letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal!")
    elif letra in 'bcdfghjklmnpqrstvwxyz':
        print(f"A letra '{letra}' é uma consoante!")
    else:
        print("A letra digitada não é vogal nem consoante!")