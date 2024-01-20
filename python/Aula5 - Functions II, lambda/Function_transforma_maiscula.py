#Q1.Faça um programa que recebe uma palavra qualquer e retorne essa mesma palavra toda em maiusculo
def transf_maiuscula(texto:str):
    return texto.upper()

palavra = str(input("Digite uma palavra: "))
print(transf_maiuscula(texto=palavra))

