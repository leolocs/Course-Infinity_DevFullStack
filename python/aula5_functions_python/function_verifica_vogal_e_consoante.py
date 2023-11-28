#Faça um programa que pede ao usuário para digitar uma palavra, e conte quantas vogais ou consoantes tem na palavra ou frase digitada, em seguida imprima a quantidade de vogais e consoantes na palavra ou frase.


def check_vowel_consonant(txt:str):
    vogais = 0
    consoantes = 0
    for l in txt:
        if l in 'aeiou':
            vogais += 1
        if l in 'bcdfghjklmnpqrstvxwyz':
            consoantes += 1
    return {
        "Vogais" = vogais
        "Consoantes" = consoantes
    }

palavra = str(input("Digite uma palavra ou frase: ")).lower().strip()

print (f"A quantidade de vogais na palavra ou texto é: {(check_vowel_consonant(txt=palavra))})