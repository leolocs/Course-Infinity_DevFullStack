# Dicionário externo
# dicionario_externo = {
#     'pessoa1': {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'},
#     'pessoa2': {'nome': 'Maria', 'idade': 30, 'cidade': 'Rio de Janeiro'},
#     'pessoa3': {'nome': 'Carlos', 'idade': 22, 'cidade': 'Belo Horizonte'},
# }

# # Iterando sobre as chaves e valores do dicionário externo
# for chave_externa, dicionario_interno in dicionario_externo.items():
#     print(f"Informações da pessoa {chave_externa}:")
    
#     # Iterando sobre as chaves e valores do dicionário interno
#     for chave_interna, valor_interno in dicionario_interno.items():
#         print(f"  {chave_interna}: {valor_interno}")

#     print()  # Adiciona uma linha em branco entre as pessoas


# Movendo um dicionário interno para outro dicionário:
 
# Dicionário de origem
dicionario_origem = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'dicionario_interno': {
        'subchave1': 'subvalor1',
        'subchave2': 'subvalor2',
    }
}

# Dicionário de destino
dicionario_destino = {
    'outra_chave': 'outro_valor'
}

# Mover o dicionário interno para o dicionário de destino por atribuição direta
dicionario_destino['dicionario_interno'] = dicionario_origem.pop('dicionario_interno', {})

# Exibindo os resultados
print("Dicionário de origem após a movimentação:")
print(dicionario_origem)

print("\nDicionário de destino após a movimentação:")
print(dicionario_destino)

