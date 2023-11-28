#region - Q1. Escreva uma função lambda que receba um número e verifique se ele é par ou ímpar. 
# A função deve retornar "par" se o número for par e "ímpar" caso contrário.
# par_impar = lambda num : f"O número {num} é par" if num % 2 == 0 else f"O número {num} é ímpar"

# num = int(input("Digite um número: "))
# print(par_impar(num))
#endregion

#region - Q2.Implemente uma função lambda que receba duas strings e retorne a concatenação das duas, apenas se ambas as strings tiverem mais de 5 caracteres. 
# Caso contrário, a função deve retornar uma mensagem de erro.
# une_palavra = lambda txt1, txt2: f"{txt1} {txt2}" if len(txt1) >= 5 and len(txt2) >= 5 else f"A palavra ou texto {txt1, txt2} tem menos de 5 caracteres"
# txt1 = str(input("Digite uma palavra ou texto: "))
# txt2 = str(input("Digite outra palavra ou texto: "))

# print(une_palavra(txt1,txt2))
#endregion

#region - Q3. Escreva uma função lambda que receba um número e verifique se ele é maior que 10. 
# Se for maior, a função deve retornar o próprio número; caso contrário, deve retornar o número dividido por 2.
# num10 = lambda num : f"{num} é maior que ou igual a 10" if num >= 10 else f"O número {num} é menor que 10 dividio por 2 é {num/2}"
# num = int(input("Digite um número: "))
# print (num10(num))
#endregion

#region - Q4. Implemente uma função lambda que receba um número e verifique se ele é divisível por 3 e por 5. 
# A função deve retornar "divisível" se a condição for satisfeita e "não divisível" caso contrário.
div_3e5 = lambda num : f"{num} é divisível por 3 e 5" if num %3 == 0 and num %5 == 0 else f"{num} não é um número divisível por 3 e 5 ao mesmo tempo"

num = int(input("Digite um número: "))
print(div_3e5(num))

#endregion