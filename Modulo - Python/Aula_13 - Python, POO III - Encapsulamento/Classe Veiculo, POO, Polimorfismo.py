# FAÇA UMA CLASSE PAI CHAMADA Veículo QUE TENHA OS ATRIBUTOS:
# marca(str), modelo(str), cor(str), ano(int)
# E UM ATRIBUTO INTERNO CHAMADO velocidade_atual QUE COMEÇA COM 0
# self.velocidade_atual = 0

# E OS MÉTODOS:
# acelerar(velocidade_acelerada) QUE EDITA A velocidade_atual PARA ELA MESMO + A velocidade_acelerada E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo} está acelerando"
# freiar() QUE SEMPRE REDUZ EM 10 A velocidade_atual E RETORNA UMA MENSAGEM TIPO "O veículo {self.modelo}
# buzinar() QUE RETORNA "Som indefinido"

# CRIE UMA CLASSE FILHA CHAMADA Carro QUE TEM O ATRIBUTO ADICIONAL:
# qtde_portas(int)
# FAÇA UM POLIMORFISMO NO MÉTODO buzinar() ALTERANDO O RETORNO DELE PARA "bi bi"

# CRIE UMA CLASSE FILHA CHAMADA Navio QUE FAZ UM POLIMORFISMO NO MÉTODO DE buzinar() ALTERANDO O RETORNO PARA "FOMMMM" 
# ENCAPSULE TODOS OS DADOS
# INSTANCIE UM CARRO E UM NAVIO
# TESTE OS MÉTODOS DE ACELERAR E FREIAR

class Veiculo:
    def __init__(self, marca:str, modelo:str, cor:str, ano:int) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__velocidade_atual = 0

    def getMarca(self):
         return self.__marca
    
    def setMarca(self, novo_valor:str):
         self.__marca = novo_valor
         return self.__marca
    
    def getModelo(self):
         return self.__modelo
    
    def setModelo(self, novo_valor:str):
         self.__modelo = novo_valor
         return self.__modelo
    
    def getCor(self):
         return self.__cor
    
    def setCor(self, novo_valor:str):
         self.__cor = novo_valor
         return self.__cor
    
    def getAno(self):
         return self.__ano
    
    def setAno(self, novo_valor:int):
         self.__ano = novo_valor
         return self.__ano
    
    def acelerar(self, velocidade_acelerada:float):
        self.__velocidade_atual += velocidade_acelerada
        return f"O veículo {self.__modelo} está acelerando, sua velocidade: {self.__velocidade_atual}km"

    def frear(self, velocidade_freada:int):
        if self.__velocidade_atual >= 10:
          self.__velocidade_atual -+ 10:
          return f"O veiculo {self.__modelo} está freando, velocidade: {self.__velocidade_atual}km"
        else: 
          self.__velocidade_atual = 0
          return f"O veiculo {self.__modelo} parou!"

    def buzinar(self):
        return "Som Indefinido"
    
class Carro(Veiculo):
     def __init__(self, marca: str, modelo: str, cor: str, ano: int, velocidade_atual: int, qtd_portas:int) -> None:
          super().__init__(marca, modelo, cor, ano, velocidade_atual)
          self.__qtd_portas = qtd_portas

     def getQtd_portas(self):
          return self.__qtd_portas

     def setQtd_portas(self, novo_valor:int):
          self.__qtd_portas = novo_valor
          return self.__qtd_portas

     def buzinar(self):
          return "Bi bi"
        
class Navio(Veiculo):
     def __init__(self, marca: str, modelo: str, cor: str, ano: int, velocidade_atual: int) -> None:
          super().__init__(marca, modelo, cor, ano, velocidade_atual)

     def buzinar(self):
          return "Fommmmm"

carro1 = Carro(marca="Chevrolet", modelo="Camaro", cor="Amarelo", ano=2022, velocidade_atual=20, qtd_portas=2)
navio = Navio(marca="Bethlehem Shipbuilding", modelo="Des Moines", cor="Prata", ano= 1946, velocidade_atual= 10)

print(carro1.buzinar())
print(carro1.acelerar(velocidade_acelerada=100))
print(carro1.frear(velocidade_freada=50))

print(navio.buzinar())
print(navio.acelerar(velocidade_acelerada=20))
print(navio.frear(velocidade_freada=10))
