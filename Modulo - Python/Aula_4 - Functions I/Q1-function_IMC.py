#region - Q1: Faça um programa que pede peso e altura do usuário e calcula seu IMC:
# O programa deve fazer o calculo do IMC de 4 pessoas e armazena-las em uma lista
# Imprima os IMC's armazenados

def calc_imc(peso:float,altura:float):
    imc = peso/(altura**2)
    return imc

lista_user = []

qtd_pessoas = int(input("Quantas pessoas irão fazer o calculo IMC? "))

for i in range(qtd_pessoas):
    nome = str(input("Qual seu nome? "))
    altura = float(input("Qual sua altura: "))
    peso = float(input("Qual seu peso? "))
    imc = calc_imc(peso=peso, altura=altura)
    lista_user.append(
        {
        "nome": nome,
        "altura": altura,
        "peso": peso,
        "IMC": imc
    }
    )

for item in lista_user:
    print(f"""
          Nome: {item["nome"]}
          Altura: {item["altura"]}
          Peso: {item["peso"]}
          IMC: {item["IMC"]:.2f}
        """)

#endregion