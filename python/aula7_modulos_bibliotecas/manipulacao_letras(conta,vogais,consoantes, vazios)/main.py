from caracteres import *

texto = str(input("Digite uma palavra ou frase: ")).strip().lower()

print(f"""
    A quantidade de letras na palavra digitada é: {conta_letras(texto)}
    A quantidade de letras vogais na palavra digitada é: {conta_vogais(texto)}
    A quantidade de letras consoantes no texto digitado é: {conta_consoantes(texto)}
    """)