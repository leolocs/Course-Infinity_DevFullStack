# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
# O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

lista_alunos = []

while True:
    op = int(input("""
                O que deseja fazer?
                1 - Cadastrar um aluno 
                2 - Remover um aluno
                3 - Ver lista de alunos
                0 - Sair
                : """))
    if op == 0:
        break

    elif op == 1:
        while True:
            nome = str(input("""Qual o nome do aluno?: """))
            #Validação do se o nome do aluno digitado possui apenas letras
            if nome.isalpha():
                print("""Nome válido""")
                break
            else:
                print("Digite um nome com letras do alfabeto, sem numeros, sem acento")

        while True:
            matricula = input("""Qual o numero de matricula? """)
            #verificação se a variável matricula tem apenas números
            if matricula.isdigit():
                print("""Número de matricula válida!""")
                break
            else:
                print("Número de matricula inválida, digite apenas números! ")
        
        #Criando um dicionário para cada aluno que for adicionado 
        aluno = {"Aluno":nome, "Matricula":matricula}
        
        #Inserindo o dicionário criado a lista de alunos
        lista_alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")


    elif op == 2:
        print(lista_alunos)
        matricula_del = input("Qual aluno você deseja remover? Digite o numero da matricula: ")
        
        for aluno in lista_alunos:
            if aluno["Matricula"] == matricula_del:
                lista_alunos.remove(aluno)
                print("Aluno removido com sucesso! ")

    elif op == 3:
        for aluno in lista_alunos:
            print(f"Aluno: {aluno['Aluno']}, Matricula: {aluno['Matricula']}")

    else:
        print("Opção inválida!")

        # for n in add_aluno:
        #     lista_alunos.append(nome)= input(f"Digite o nome do {n+1} aluno: ")
        #     lista_alunos["Matricula"] = input(f"Qual a matricula do aluno: ")
        #     {"Nome": nome, "Matricula":mat}

