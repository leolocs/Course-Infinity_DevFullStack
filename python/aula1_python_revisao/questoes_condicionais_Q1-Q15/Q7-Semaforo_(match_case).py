#7.SEMÁFORO: Faça um programa que pede para o usuário escrever uma cor e mostre “Pare” se for vermelho, “Atenção” se for amarelo, “Acelera” se for verde e “Cor inválida” se for qualquer outra cor.
cor = str(input("Escolha uma cor entre: (VERMELHO | AMARELO | VERDE)")).lower().strip()
match cor:
    case "verde":
        print("Sinal verde, Acelere!")
    case "amarelo":
        print("Sinal Amarelo, Pare!")
    case "Vermelho":
        print("Sinal Vermelho, Pare!")
    case _:
        print("Cor inválida!")