# region - 1.Faça um programa que checa se o usuário é maior ou menor de idade se ele for maior de idade adicione um novo campo no dicionário  com a chave "habilidade" e o valor True;
# se não muda o nome da pessoa para "Joãozinho"
# pessoa = {"nome":"João", "idade": 16, "cpf": "123.456.789-10"}

# if pessoa["idade"] > 18:
#     pessoa["habilitação"] = True # Atribuindo nova chave "habilidade" com valor "True" ao dicionário "pessoa";
# else:
#     pessoa["nome"] = "Joãozinho" # Reatribuindo o valor "joãzinho" a chave "nome" ao dicionário "pessoa"
# print(pessoa)
#endregion

#region - Mesma questão porém solicitando os dados ao usuário:
nome = str(input("Qual o seu nome? "))
idade = int(input("Qual sua idade? "))
cpf = int(input("Digite seu CPF, (utilize apenas números sem pontos e traços): "))

pessoa = {
    "nome":nome, 
    'idade': idade,
    "cpf": cpf
}

if pessoa["idade"] < 18:
    pessoa["nome"] = "Joãzinho"
else:
    pessoa["Habilitação"] = True
print(pessoa)
#endregion

#region - 2. Dado o dicionário: Carro = {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"}, 
#         Faça um programa que cheque se existe uma chave chamada "Cor" no dicionário
#         se existir, mude ela para "preto" se não existir delete a chave "ano"
carro = {
    "Marca": "Ford",
    "Modelo": "Ka",
    "Ano": 2020,
    "Cor": "Branco"
    }

if "Cor" in carro:
    carro["Cor"] = "Preto"
else:
    del carro["Ano"]
print(carro)
#endregion

#region - 3. 

#endregion