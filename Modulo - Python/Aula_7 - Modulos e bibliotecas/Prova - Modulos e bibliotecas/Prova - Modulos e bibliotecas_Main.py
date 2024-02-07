# Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. 
# O programa deve permitir adicionar, remover, atualizar e listar os alunos.
# Para isso, você deve implementar um módulo que contém as seguintes funções:

# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
# (Lembre Se de Modularizar o código)

#Funções do programa da Prova de Módulos e Bibliotecas
from Modulos_functions import *

while True:
    print("##### Inicio do Programa #####")
    op = int(input("""
        Qual operação deseja fazer?:
        1 - Adicionar um aluno
        2 - Atualizar um aluno
        3 - Remover um aluno
        4 - Ver a lista de Alunos
        5 - Ver lista alunos removidos
        0 - Sair  
        """))
    match op:
        case 0:
            print("Encerrando programa...")
            break
        case 1:
            nome_aluno = str(input("Digite o nome do aluno: ")).strip().lower()
            matricula_aluno = str(input("Digite a matricula do aluno: ")).strip()
            adicionar_aluno(nome= nome_aluno, matricula= matricula_aluno)
        
        case 2:
            mat_atualizar = str(input("Digite a matricula do aluno que deseja atualizar o nome: "))
            atualizar_aluno(matricula=mat_atualizar)
            
        case 3:
            matricula_remover = str(input("Digite qual a matricula do aluno que deseja remover: "))
            if matricula_remover.isdigit():
                remover_aluno(matricula=matricula_remover)
            else:
                print("Digite apenas números!")

        case 4:
            listar_alunos()
            
        case 5:
            listar_alunos_removidos()