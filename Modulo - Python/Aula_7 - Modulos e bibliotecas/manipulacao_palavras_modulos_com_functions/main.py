# Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings, como inverter uma string, contar o número de palavras
# em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para frente). Crie um programa principal que importe o módulo e use
# essas funções com strings fornecidas pelo usuário.

from manipulacao_strings import * 

while True:
    texto = str(input("Digite uma palavra ou texto: "))
    if texto == "sair":
        break
    print(f"""
        O texto digitado:
        Possui {conta_palavra(texto=texto)} palavra
        Invertida é: {inverter(texto)}
        {palindromo(texto)}
        """)