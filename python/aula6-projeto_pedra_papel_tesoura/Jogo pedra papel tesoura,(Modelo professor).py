# Jogo pedra papel tesoura, modelo professor

contador1 = 0
contador2 = 0

from random import choice

def escolha_jogador():
    while True:
        escolha = str(input("Digite sua escolha: Pedra, Papel ou Tesoura:")).lower().strip()
        if escolha in ["pedra, papel, tesoura"]:
            return escolha

def escolha_maquina():
    lista = ["pedra, papel, tesoura"]
    escolha = choice(lista)
    return escolha

def checar_vencedor(usuario,computador):
    if usuario == computador:
        return "Empate"
    elif (usuario == "pedra" and computador == "tesoura") or (usuario == "tesoura" and computador=="papel") or (usuario == "papel" and computador== "pedra"):
        return "Você Ganhou"
    else:
        return "Você Perdeu"


while True:
    jogador = escolha_jogador()
    maquina = escolha_maquina()

    print(checar_vencedor(usuario=jogador, computador=maquina))
