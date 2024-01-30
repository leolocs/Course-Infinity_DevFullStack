# Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. 
# O programa deve permitir adicionar, remover, atualizar e listar os alunos.
# Para isso, você deve implementar um módulo que contém as seguintes funções:

# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
# (Lembre Se de Modularizar o código)
#Funções do programa da Prova de Módulos e Bibliotecas

def adicionar_aluno(nome:str, matricula:int):
    while True:
        if nome.isalpha():
            print("Nome válido")
            return nome_aluno
        else:
            print("Digite um nome com apenas letra! :")

    while True:
        if mat_aluno.isdigit():
            print("Matricula valida!")
            break
        else:
            print("Digite uma matricula com apenas numeros!")
        
        aluno = ({"Nome": nome_aluno, "Matricula":matricula_aluno})
        lista_alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

lista_alunos = []

while True:
    print("##### Inicio do Programa #####")
    op = int(input("""
        Qual operação deseja fazer?:
        1 - Adicionar um aluno
        2 - Atualizar um aluno
        3 - Remover um aluno
        4 - Ver a lista de Alunos
        0 - Sair  
        """))
    match op:
        case 0:
            print("Encerrando programa...")
            break
        case 1:
            nome_aluno = str(input("Digite o nome do aluno: "))
            matricula_aluno = int(input("Digite a matricula do aluno: "))
            adicionar_aluno(nome= nome_aluno, matricula=matricula_aluno)
        
        case 2:
            