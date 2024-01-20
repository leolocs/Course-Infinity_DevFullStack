# Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings que serão:
# Inverter uma string, 
# Contar o número de palavras
# Verificar se uma string é um palíndromo (lê-se igual de trás para frente). 
# Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

def conta_palavra(texto:str):
    palavra = 1
    for l in texto.strip():
        if l == " ":
            palavra += 1
    return palavra

def inverter(texto):
    invertida = texto[::-1]
    return invertida

def palindromo(texto:str):
    texto_sem_espaco = texto.replace(" ", "")
    invertida = texto_sem_espaco [::-1] 
    if texto_sem_espaco == invertida:
        return f"A palavra {texto} é um palindromo"
    else:
        return f"A palavra {texto} não é um palindromo"