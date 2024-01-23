# Crie uma classe Empresa que permita gerenciar
# funcionários. 
# Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz de adicionar, remover e listar funcionários.

class Empresa:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.lista_funcionario = []

    def add_funcionario(self,funcionario):
        self.lista_funcionario.append(funcionario)

    def remover_funcionario(funcionario):
        self.lista_funcionario.remove


class Funcionario:
    def __init__(self, nome:str, cpf:int, cargo:str, salario:float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario





empresa = Empresa()

while True:
    op = int(input(f"""
        Qual operação vocdeseja realizar:
        1 - Adicionar Funcionario
        2 - Remover funcionario
        3 - Lista funcionarios
        0 - Sair
        """))
    match op:
        case 0:
            break
        case 1:
            nome_funcionario = str(input("Digite o nome: "))
            cargo_funcionario = str(input("Digite o cargo: "))
            salario_funcionario = str(input("Digite o salario: "))

            funcionario = Funcionario(nome=nome_funcionario, cargo=cargo_funcionario, salario=salario_funcionario) 

            empresa.add_funcionario(funcionario)