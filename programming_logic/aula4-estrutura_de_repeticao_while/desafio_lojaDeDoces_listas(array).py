#region - DESAFIO: Loja de Doces
# PROBLEMA: Uma loja de doces vai lançar uma promoção onde sorteará um brinde entre 3 clientes do dia

# O SORTEIO: Ao registrar uma venda o caixa da loja pergunta nome, endereço e telefone do cliente e insere essas informações em uma aplicação que ficará executando durante todo o expediente da Loja (em processo de repetição)
# A aplicação deve guardar todas as ocorrências de informações sobre o cliente até que o caixa seja encerrado (você decide como será inserida a informação)
# ao final do expediente, o caixa informa na aplicação um cliente chamado "fim", e a aplicação, sorteará um dos clientes atendidos ao longo do dia;
# a aplicação informará na tela todos os os dados do cliente sorteado e se encerrará.

# ENTREGA: Deve ser entregue um fluxograma contendo a sequência lógica de instruções para a aplicação funcionar;
# A codificação em linguagem Python da solução do problema.


# import random
# lista = []
# while True:
#     nome = str(input("Digite seu nome: "))
#     if nome == "fim":
#         break
#     telefone = str(input("Digite seu telefone: "))
#     endereco = str(input("Digite seu endereco: "))
#     lista.append([nome, telefone, endereco])

# sorteado = random.choice(lista)

# sorteado2 = random.choice(lista)

# while sorteado[0] == sorteado2 [0]:
#     sorteado2 = random.choice(lista)

# sorteado3 = random.choice(lista)

# while sorteado[0] == sorteado3 [0] or sorteado2[0] == sorteado3[0]:
#     sorteado2 = random.choice(lista)

# print(f"""
#         Sorteado foi
#         Nome: {sorteado[0]}
#         Telefone: {sorteado[1]}
#         Endereço: {sorteado[2]}
# """)
#endregion