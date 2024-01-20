#9.MAIOR DE IDADE: Faça um programa que pergunte qual ano o usuário nasceu e mostre na tela se ele é ou não maior de idade
while True:
    ano = int(input("Digite o ano que você nasceu: "))
    if ano == 0:
        break
    elif ano > 2005:
        print("Você é menor de idade!")
    elif ano <= 2005:
        print("Você é maior de idade!")
    elif ano >= 1973 and ano <= 1993:
        print("Você está na casa dos 30, 40! A idade do sucesso!")
    elif ano >= 1933 and ano <= 1963:
        print("O Sr./Sra. está na 3ª idade!, até 90 anos")
    elif ano >= 1923:
        print("O Sr./Sra. é um guerreiro por ter chegado até aqui! Casa dos 100 anos")
    elif ano < 1923:
        print("Provavelmente essa pessoa ja está morta!")