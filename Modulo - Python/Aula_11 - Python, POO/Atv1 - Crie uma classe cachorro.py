class Animal:
    def __init__(self, nome, idade, peso, especie, raca, sexo) -> None:
        pass
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.especie = especie
        self.raca = raca
        self.sexo = sexo
    
nome = str(input("Qual o nome do animal: "))
idade = int(input("Qual a IDADE do animal? (em anos): "))
peso = float(input("Qual o PESO do animal?: "))
especie = str(input("Qual a ESPÉCIE do animal?: "))
raca = str(input("Qual a raça do animal?: "))
sexo = str(input("Qual o SEXO do animal?: "))

animal = Animal(nome=nome, idade=idade, peso=peso, especie=especie, raca=raca, sexo=sexo)

print(f"""
    Informações sobre o animal:
    Nome do animal: {animal.nome}
    Idade do animal: {animal.idade}
    Peso: {animal.peso}
    Espécie: {animal.especie}
    Raça: {animal.raca}
    Sexo: {animal.sexo}
""")