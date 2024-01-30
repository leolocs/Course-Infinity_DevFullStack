class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar():
        return f"O veiculo {self.modelo} está ligando..."

    def desligar():
        return f"O veiculo {self.modelo} está desligando..."


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtd_portas=int) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.qtd_portas = qtd_portas

    def ligar_ar(self):
        return f"O carro {self.modelo} ligou o ar-condicionado"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas=int) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

    def empinar():
        return f"A moto está dando grau.... "

carro1 = Carro(marca="Fiat", modelo="Uno", ano=2002, cor="Prata", qtd_portas=2)
moto1 = Moto(marca="BMW", modelo="S1000RR", ano=2018, cor="branca", cilindradas=1000)
