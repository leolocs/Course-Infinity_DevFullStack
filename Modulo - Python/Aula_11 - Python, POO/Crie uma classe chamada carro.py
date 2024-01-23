# CRIE UMA CLASSE CHAMADA Carro QUE TEM COMO ATRIBUTOS:

# Ano (int), Marca(str), Modelo(str), Cor(str), 
# Qtde_portas(int), Arcondicionado(bool), 
# Vidro_eletrico(bool)

# INSTACIE 3 CARROS COM AS INFORMAÇÕES QUE VOCÊS QUISEREM E 
# DEPOIS PRINT NA TELA:
# A MARCA E O MODELO DO PRIMEIRO CARRO
# O MODELO, O ANO E SE O SEGUNDO CARRO TEM VIDRO ELÉTRICO
# TODAS AS INFORMAÇÕES DO TERCEIRO CARRO

class Carro:
    def __init__(self, marca, modelo,ano, cor, qtd_portas, ar_condicionado, vdr_eletrico) -> None:
        pass
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.ar_condicionado = ar_condicionado
        self.vdr_eletrico = vdr_eletrico

carro1 = Carro(marca= "Chevrolet", modelo="Onix", ano= 2020, cor= "Prata", qtd_portas= 4, ar_condicionado= True, vdr_eletrico= True)
carro2 = Carro(marca="VolksVagen", modelo="Gol", ano=1999, cor="Vermelho", qtd_portas=2, ar_condicionado=False, vdr_eletrico=False)

print(f"O primeiro carro, é de marca: {carro1.marca}e modelo: {carro1.modelo}")
print(f"O segundo carro, é de modelo: {carro2.modelo} ano {carro2.ano}")
if carro2.vdr_eletrico:
    print("O segundo carro possuir ar-condicionado")
else:
    print("O segundo carro não possui ar-condicionado")


marca_carro = str(input("Qual a marca do carro?: "))
modelo_carro = str(input("Qual o modelo do carro?: "))
ano_carro = int(input("Qual o ano do carro?: "))
cor_carro = str(input("Qual a cor do carro?: "))
qtd_portas = int(input("Quantas portas o carro possui?: "))
ar_condicionado = bool(input("O Carro possui ar-condicionado? (DIgite apenas: True ou False): "))
vdr_eletrico = bool(input("O Carro possui vidros eletricos?: "))

carro3 = Carro(marca=marca_carro, modelo=modelo_carro, ano= ano_carro, cor=cor_carro, qtd_portas=qtd_portas, ar_condicionado=ar_condicionado, vdr_eletrico=vdr_eletrico)

ar = "none"
vidro = "none"
if carro3.ar_condicionado:
    ar = "Sim"
    #print(f"O carro: {carro3.modelo} possui ar-condicionado!")
else:
    ar = "Não"
    #print(f"O carro{carro3.modelo} não possui ar-condicionado!")
    
if carro3.vdr_eletrico:
    vidro = "Sim"
    #print(f"O carro:{carro3.modelo}, possui vidros eletricos nas 4 portas!")
else:
    vidro = "Não"
    #print(f"O carro:{carro3.modelo}, não possui vidros eletricos nas 4 portas!")


print(f"""
    Informações terceiro carro:
    Marca: {carro3.marca} 
    Modelo: {carro3.modelo}
    Ano: {carro3.ano}
    Cor: {carro3.cor}
    {carro3.qtd_portas} portas
    Vidro elétrico: {vidro}
    Ar-condicionado:{ar}
    """)


