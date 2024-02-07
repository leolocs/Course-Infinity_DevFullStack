lista_alunos = []
alunos_removidos = []

def adicionar_aluno(nome:str, matricula:str):
    while True:
        if nome.isalpha():
            print("Nome válido")
            break
        else:
            print ("Digite um nome apenas com letras!: ")

        if matricula.isdigit():
            print("Matricula valida!")
            break
        else:
            return "Digite uma matricula com apenas numeros!"

    aluno = {"nome": nome, "matricula":matricula}
    lista_alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")


def atualizar_aluno(matricula:str):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            novo_nome = input(f"Atualize o nome do aluno da matricula {matricula}: ")
            aluno['nome'] = novo_nome
            print("Aluno alterado com sucesso!")

def remover_aluno(matricula:str):
    for aluno in lista_alunos:
        if aluno['matricula'] == matricula:
            alunos_removidos.append(aluno)
            lista_alunos.remove(aluno)
            print(f"Aluno da matricula {aluno['matricula']} foi removido com sucesso!")

def listar_alunos():
    for aluno in lista_alunos:
        print (f"Aluno: {aluno['nome']}, Matricula: {aluno['matricula']}")

def listar_alunos_removidos():
    for aluno in listar_alunos_removidos:
        print(f"Aluno:{aluno['nome']}, Matricula:{aluno['matricula']}")