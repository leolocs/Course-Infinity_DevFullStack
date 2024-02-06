#Encapsulamento
class Animal:
    def __init__(self, raca:str, cor:str, peso:float) -> None:
        self.__raca = raca
        self.__cor = cor
        self.__peso = peso

    def getRaca(self):
        return self.__raca
    
    def setRaca(self, novo_valor):
        self.__raca = novo_valor
        return "Raça alterada com sucesso"
    

    def getCor(self):
        return self.__cor
    
    def setCor(self, novo_valor):
        self.__cor = novo_valor
        return "Cor alterada com sucesso"
    

    def getPeso(self):
        return self.__peso
    
    def setPeso(self, novo_valor):
        self.__peso = novo_valor
        return "Peso alterada com sucesso"
    
    
    def emitir_som(self):
        return "Som indefinido"
    

class Cachorro(Animal):
    def __init__(self, raca: str, cor: str, peso: float) -> None:
        super().__init__(raca, cor, peso)
    
    def pegar_bolinha(self):
        return "O cachorro pegou a bolinha"
    
    def emitir_som(self):
        return "Au aaau"


class Gato(Animal):
    def __init__(self, raca: str, cor: str, peso: float, cor_do_olho:str) -> None:
        super().__init__(raca, cor, peso)
        self.cor_do_olho = cor_do_olho

    def amassar_paozinho(self):
        return "O gato ta amassando paozinho"
    
    def emitir_som(self):
        return "Miauuuu"

cachorrim = Cachorro(raca="Pitbull", cor="Bege", peso=8.3)
gatim = Gato(raca="Angorá", cor="branco", peso=3.5, cor_do_olho="Azul")

print(cachorrim.emitir_som())
print(gatim.emitir_som())
print(gatim.emitir_som())


print(gatim.visualizar_raca())

gatim.editar_raca("Persa")

print(gatim.visualizar_raca())