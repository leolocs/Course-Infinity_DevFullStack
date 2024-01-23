# Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero

class Pessoa:
    def __init__(self,nome, idade, peso, sexo) -> None:
        pass
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.sexo = sexo

nome = str(input("Qual o NOME da pessoa?: "))
idade = int(input("Qual a IDADE da pessoa?: "))
peso = float(input("Qual o PESO da pessoa?: "))
sexo = str(input("Qual o SEXO da pessoa?: "))

pessoa = Pessoa(nome=nome, idade=idade, peso=peso, sexo=sexo)

print(f"""
    Infomrações sobre a pessoa:
    Nome:{pessoa.nome}
    Idade:{pessoa.idade}
    Peso:{pessoa.peso}
    Sexo:{pessoa.sexo}
      """)

