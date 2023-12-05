#projeto jogo pedra, papel, tesoura
# Neste projeto você desenvolverá o jogo pedra, papel e tesoura. Os jogadores serão o usuário e o computador.
# O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel" ou "tesoura" e então o computador irá fazer a escolha aleatoriamente, 
# após isso, o jogo deve informar quem venceu.
# Para recordar:
# Utilize funções para separar cada funcionalidade do jogo!
# Dica : Utilize a função random.choice(lista) do pacote random para realizar a escolha do computador

import random 

jogador_vitoria = 0
cpu_vitoria = 0
empates = 0

opcoes_jogada = ['pedra', 'papel','tesoura']

def cpu_joga():
    cpu_escolha = random.choice(opcoes_jogada)
    return cpu_escolha

while True:
    cpu = cpu_joga()
    jogador = str(input("""
                    Qual sua jogada?                    
                    (Pedra, Papel, Tesoura, ou Sair): """)).lower().strip()
    
    if jogador == "sair":
        print(f"""O placar foi de:
            {jogador_vitoria} Vitorias do Jogador
            {cpu_vitoria} Vitorias do Computador
            e {empates} empates!
            """)
        break
    elif jogador in opcoes_jogada:
        if jogador == cpu:
                print(f"""O cpu jogou: {cpu} e você jogou: {jogador}, foi empate!""")
                empates += 1
        elif (jogador == "pedra" and cpu == "tesoura") or (jogador == "papel" and cpu == "pedra") or (jogador == "tesoura" and cpu == "papel"):
            print(f"""O cpu jogou: {cpu}, Você jogou: {jogador}, você venceu!""")
            jogador_vitoria += 1
        else:
            print(f"""O cpu jogou: {cpu}, você jogou: {jogador}, você perdeu!""")
            cpu_vitoria += 1
    else:
         print(f"Opção inválida! Digite uma opção válida!")