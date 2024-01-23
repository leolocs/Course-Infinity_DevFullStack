#definicão da classe e atribuindo as propriedades
class Celular:
    def __init__(self, marca, modelo, cor, ano, armazenamento) -> None:
        pass 
        self.brand = marca
        self.model = modelo
        self.color = cor
        self.year = ano
        self.storage = armazenamento
    
    def ligar(self,numero):
        return f"O Celular {self.model}, está fazendo uma ligação para o numero: {numero}"
    
    def desligar(self):
        return f"Celular {self.model} desligando..."


#Criando instâncias:
celular1 = Celular(marca="Samsung", modelo= "S22 Ultra", cor="Cinza", ano=2022, armazenamento= 256)
celular2 = Celular(marca="Apple", modelo= "Iphone 15", cor= "Preto", ano=2023, armazenamento= 512)
celular3 = Celular(marca= "Xiaomi", modelo= "Redmi Note 11", cor= "Azul", ano= 2020, armazenamento= 256)


marca_celular = str(input("Digite a marca do celular: "))
modelo_celular = str(input("Digite o modelo do celular: "))
cor_celular = str(input("Digite a cor do celular: "))
ano_celular = int(input("Digite o ano do celular: "))
armazenamento_celular = int(input("Digite qual a capacidade em GB do celular: "))

celular4 = Celular(marca=marca_celular, modelo=modelo_celular, cor=cor_celular, ano=ano_celular, armazenamento=armazenamento_celular)


    