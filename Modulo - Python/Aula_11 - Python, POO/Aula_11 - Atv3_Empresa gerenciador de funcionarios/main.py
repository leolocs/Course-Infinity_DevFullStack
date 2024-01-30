from empresa_classes import *

empresa = Empresa(nome=str)

while True:
    op = int(input(f"""
        Qual operação você deseja realizar:
        1 - Adicionar Funcionario
        2 - Remover funcionario
        3 - Lista funcionarios
        0 - Sair
        """))
    
    match op:
        case 0:
            print("Saindo do programa...")
            break
        case 1:
            while True:
                nome_funcionario = str(input("Digite o nome: "))
                if nome_funcionario.isalpha() or nome_funcionario in " ":
                    print("Nome validado!")
                    break
                else:
                    print("Digite um nome apenas com LETRAS!")
            while True:
                cpf = str(input("Digite o CPF do funcionario: "))
                if len(cpf) < 11:
                    print("CPF validado!")
                    break
                else:
                    print("Digite um CPF com 11 DIGITOS!")
                    
            while True:
                cargo_funcionario = str(input("Digite o cargo do funcioario: "))
                if cargo_funcionario.isalpha():
                    print("Cargo validado!")
                    break
                else:
                    print("Digite um cargo apenas com letras")
            while True:
                salario_funcionario = float(input("Digite o salario: "))
                break
            
            funcionario = Funcionario(nome=nome_funcionario, cpf=cpf, cargo=cargo_funcionario, salario=salario_funcionario) 
            empresa.add_funcionario(funcionario)

        case 2:
            cpf_a_remover = int(input("Qual o CPF do funcionario que você deseja remover?: "))
            empresa.remover_funcionario(cpf= cpf_a_remover)

        case 3:
            empresa.listar_funcionarios()

print (type(empresa))