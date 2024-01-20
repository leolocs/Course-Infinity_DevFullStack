#Faça um programa que recebe uma cor e retorne:
# Pare! se for vermelho
# Atenção! se for amarelo
# Avance! se for verde

def semaforo(cor:str):
    match cor:
        case "vermelho":
            return f"Sinal {cor}, Pare!"
        case "amarelo":
            return f"Sinal {cor}, Atenção!"
        case "verde":
            return f"Sinal {cor}, Avance!"
        case _:
            return f"Sinal {cor} inválida!, digite uma cor válida!"

cor = str(input("Digite uma cor entre: (verde, Amarelo, vermelho: )")).lower().strip()
print(semaforo(cor=cor))
