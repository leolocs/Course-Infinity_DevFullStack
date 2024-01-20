#region - Faça um programa que recebe alguma hora e retorne uma saudação apropriada
# def saudacao(hora):
#     if hora <= 5 and hora <=12:
#         return "Bom dia"
#     elif hora > 12 and hora <= 18:
#         return "Boa tarde"
#     else:
#         return "boa noite"

# hr = int(input("Que horas são? (Digite apenas números):"))
# print(saudacao(hr))
#endregion

#region - Faça uma função que recebe 3 números e retorna qual o maior dos 3:
# def maior(n1,n2,n3):
#     if n1 >= n2 and n1 >= n3:
#         return n1
#     elif n2 >= n1 and n2 >= n3:
#         return n2
#     elif n3 >= n1 and n3 >= n2:
#         return n3
    
# n = int(input("Digite um número: ")) 
# n2 = int(input("Digite outro número: ")) 
# n3 = int(input("Digite outro número: "))

# print(maior(n,n2,n3))

#Mesma questão porem usando lista:
# lista_n = []

# for i in range(1,4):
#     n = int(input(f"Digite o {i}º numero: "))

# def maior(n):
#     if n[0] > n[1] and n[0] > n[2]:
#         return f"O maior número é: {n[0]}"
#     elif n[1] > n[0] and n[1] > n[2]:
#         return f"O maior número é {n[1]}"
#     elif n[2] > n[0] and n[2] > n[1]:
#         return f"O maior número é {n[2]}
# print(maior(lista_n[0],lista_n[1],lista_n[2]))

#Mesma questão melhor forma:
def maior(lista_n):
    maior_num = 0
    for n in lista_n:
        if n > maior_num:
            maior_num = n
    if maior_num == 0:
        return "Digite números positivos"
    else:
        return maior_num

lista_n = []
for i in range(1,4):
    n = int(input(f"Digite o {i}º numero: "))
    lista_n.append(n)
print(maior(lista_n))
#endregion

#region - Parametro posicionais:
def saudacao(nome, hora):
    if hora <= 5 and hora <=12:
        return f"Bom dia {nome}"
    elif hora > 12 and hora <= 18:
        return f"Boa tarde {nome}"
    else:
        return "boa noite"
nome = str(input("Digite seu nome: "))
hora = int(input("Que horas são?: "))

print(saudacao(nome,hora))

#endregion - Parametro posicional

#region - Parametros Nomeados

#endregion - Parametros nomeados