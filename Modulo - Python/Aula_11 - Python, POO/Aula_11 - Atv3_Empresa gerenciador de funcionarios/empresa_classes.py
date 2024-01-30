# Crie uma classe Empresa que permita gerenciar funcionários. 
# Os funcionários devem ter as informações:
# Nome
#cargo e salário. 
#A empresa deve ser capaz de adicionar, remover e listar funcionários.

class Funcionario:
    def __init__(self, nome:str, cpf:str, cargo:str, salario:float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.funcionarios = []
        self.funcionarios_removidos = []

    def add_funcionario(self,funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(cpf:str):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                self.funcionarios_removidos.append(funcionario)
                self.funcionarios.remove(funcionario)
                print(f'Funcionario {funcionario} com CPF {cpf}, removido com sucesso!')
                return
            else:
                print(f"Funcionario com CPF: {cpf} não encontrado na empresa!")
        
    def listar_funcionarios():
        for funcionario in self.funcionarios:
            print(f"""
            Funcionario: {funcionario.nome};
            CPF: {funcionario.cpf};
            Cargo: {funcionario.cargo};
            Salário: {funcionario.salario}
""")