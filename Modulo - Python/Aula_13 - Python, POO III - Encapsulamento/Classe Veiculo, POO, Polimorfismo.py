# FAÇA UMA CLASSE PAI CHAMADA Veículo QUE TENHA OS ATRIBUTOS:
# marca(str), modelo(str), cor(str), ano(int)
# E UM ATRIBUTO INTERNO CHAMADO velocidade_atual QUE COMEÇA COM 0
# self.velocidade_atual = 0

# E OS MÉTODOS:
# acelerar(velocidade_acelerada) QUE EDITA A velocidade_atual PARA ELA MESMO + A velocidade_acelerada E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo} está acelerando"
# E O MÉTODO:
# freiar() QUE SEMPRE REDUZ EM 10 A velocidade_atual E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo}
# E O MÉTODO:
# buzinar() QUE RETORNA "Som indefinido"

# CRIE UMA CLASSE FILHA CHAMADA Carro QUE TEM O ATRIBUTO ADICIONAL:
# qtde_portas(int)
# FAÇA UM POLIMORFISMO NO MÉTODO buzinar() ALTERANDO O RETORNO DELE PARA "bi bi"

# CRIE UMA CLASSE FILHA CHAMADA Navio QUE FAZ UM POLIMORFISMO NO MÉTODO DE buzinar() ALTERANDO O RETORNO PARA "FOMMMM" 
# ENCAPSULE TODOS OS DADOS
# INSTANCIE UM CARRO E UM NAVIO
# TESTE OS MÉTODOS DE ACELERAR E FREIAR

class Veiculo:
    def __init__(self, marca:str, modelo:str, cor:str, ano:int, velocidade_atual:int) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__velocidade_atual = 0

    def getMarca(self):
         return self.__marca
    
    def setMarca(self, Nova_marca):
         self.__marca = Nova_marca
         return self.__modelo
    
    def getModelo(self):
         return self.__modelo
    
    def setModelo(self):
         return self.__modelo
    
    def getCor(self):
         return
    
    def acelerar(self, velocidade_acelerada):
        self.__velocidade_atual += velocidade_acelerada
        return f"O veículo {self.__modelo} está acelerando"

    def frear(self):
        self.__velocidade_atual -= 10
        return f"O veiculo {self.__modelo} está freando"

    def buzinar(self):
        return "Som Indefinido"
    
class Carro(Veiculo):
        def __init__(self, marca: str, modelo: str, cor: str, ano: int, velocidade_atual: int, qtd_portas:int) -> None:
             super().__init__(marca, modelo, cor, ano, velocidade_atual)
             self.__qtd_portas = qtd_portas

        def getQtd_portas(self):
            return __qtd_portas

        def setQtd_portas(self):
             

        def buzinar(self):
             return "Bi bi"
