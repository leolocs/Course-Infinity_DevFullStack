#15. PREÇO DO TECLADO: Os teclados custam R$ 30 cada se forem compradas menos do que uma dúzia, e R$ 25 se forem compradas pelo menos doze. 
#Escreva um programa que leia o número de teclados compradas, calcule e escreva o valor total da compra.
tecl_comprado = int(input("Qual a quantidade de teclados que irá comprar? "))
if tecl_comprado == 0:
        print("Digite uma quantidade válida!")  
else:
    if tecl_comprado < 12:
        soma = tecl_comprado*30
    elif tecl_comprado >= 12:
         soma = tecl_comprado*25
print(f"O total da soma dos teclados comprados é de: R${soma}")