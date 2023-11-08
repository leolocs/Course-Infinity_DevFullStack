#region - Programa que conta de 1 a 10 com While
# numero = 0
# while numero < 10:
#     print(numero)
#     numero = numero + 1
#     # numero += 1
#endregion

# region - PROGRAMA QUE MOSTRE TODOS OS NÚMEROS DE 1 A 200 USANDO WHILE E DEPOIS USANDO FOR
# numero = 1
# while numero <= 200:
#     print(numero)
#     numero += 1

# for i in range(1,201):
#     print(i)
#endregion

# region - PROGRAMA QUE MOSTRE OS NÚMEROS DE 0 A 100 PORÉM MOSTRANDO APENAS AS DEZENAS utilizando WHILE E FOR
# valor = 0
# while valor <= 100:
#     print(valor)
#     valor = valor + 10

# #Utilizando FOR, RANGE
# for i in range(0,101,10):
#     print(i)

# valor = 0

# Utilizando matemática
# while valor <= 100:
#     if valor % 10 == 0:
#         print(valor)
#     valor = valor + 1
#endregion

#region - Programa que solicita que usuário digite um número, quando o número digitado for maior que 100 ele finaliza
# while True:
#     numero = int(input("Digite um número: "))   

#     if numero > 100:
#         break
#     else:
#         print(numero) 
#endregion

#region - ##### Area de testes While #####
x=50
while x <= 100:
    print(x)
    x += 1
#endregion