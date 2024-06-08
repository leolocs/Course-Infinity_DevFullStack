# PROVA DE CONDICIONAL:  Escreva um programa em python que pergunte ao usuário a velocidade de um carro. 
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

while True:
    velocidade = float(input("Qual a velocidade? "))
    multa = 0
    if velocidade > 80:
        multa = (velocidade - 80) * 20
        print(f"Você foi multado por excesso de velocidade, multa de R${multa}")
    else:
        print("Continue dirigindo em segurança!")