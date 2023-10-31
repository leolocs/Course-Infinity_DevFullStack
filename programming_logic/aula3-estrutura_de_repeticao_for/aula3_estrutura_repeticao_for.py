#region: Programa que percorre e imprime o nome
#nome = "maria"
# for letra in nome:
#     print (letra)
#endregion

#region: Faça um programa que solicite uma palavra ao usuário, conte a quantidade de letras "a" que a palavra possua e exiba na tela 
# palavra = str(input("Digite uma palavra: ")).lower().strip()
# letra_a = False
# qtd = 0
# for letra in palavra:
#     if letra == 'a':
#         letra_a = True
#         qtd = qtd +1
# if letra_a == True:
#     print(f"sua palavra contém {qtd} letras A")
# else:
#     print(f"Sua palavra não possui a")
#endregion

#region: Exibe o Alfabeto retirando as vogais do alfabeto
# alfabeto = "abcdefghijklmnopqrstuvwxyz"
# vogais = "aeiou"
# for letra in alfabeto:
#      if letra not in vogais:
#           print(letra)
#endregion

#region: Programa solicita uma frase ao usuário e se tiver números na frase mostre na tela 
# frase = str(input("Digite uma frase: "))
# numero = "0123456789" 
# for num in frase:
#      if num in numero:
#           print(f"Econtrei um número: {num}")
#endregion

#region: Função FOR range contagem 
# for i in range(10): # 0 a 9
#      print(i)
# for i in range(1,20): # função range do 1 até número 19
#      print(i)
# for i in range(1,101,2): # Função range contagem de 1 a 100 com intervalo de 2 numeros
#     print(i)
#endregion