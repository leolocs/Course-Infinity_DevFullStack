# Crie uma função que retorne a quantidade de letras digitadas por um usuário
# Crie uma função que retorne a quantidade de vogais digitadas pelo usuário
# Crie uma função que retorne a quantidade de consoantes digitadas pelo usuário
# Crie uma função que  retorne a quantidade de espaços vazios digitados pelo usuário

def conta_letras(texto):
    caractere = 0
    for l in texto:
        caractere += 1
    return caractere
    #return len(caractere)

def conta_vogais(texto):
    vogais = 0
    for letra in texto:
        if letra in "aeiou":
            vogais += 1
    return vogais

def conta_consoantes(texto):
    consoantes = 0
    for letra in texto:
        if letra in "bcdfghjklmnpqrstvwxyz":
            consoantes +=1
    return consoantes

def contar_vazios(texto):
    vazios = 0
    for letra in texto:
        if letra == " ":
            vazios += 1
    return vazios