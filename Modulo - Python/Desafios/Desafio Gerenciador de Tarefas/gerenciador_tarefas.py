# Configuração do Ambiente Virtual:
# Crie um ambiente virtual utilizando o módulo venv para isolar as dependências do projeto.

# Definição de Dados:
# Utilize estruturas de dados, como dicionários, para representar as tarefas. 
#Cada tarefa deve conter informações como nome, descrição, prioridade e categoria.

#Funções:
# Implemente funções para adicionar tarefas, listar tarefas, marcar tarefas como concluídas, exibir tarefas por prioridade ou categoria, e outras funcionalidades desejadas.

# Menu de Comandos:
# Desenvolva um menu de comandos de linha de comando que permita ao usuário interagir com o programa. 
#Este menu deve oferecer opções para realizar operações como adicionar, listar, marcar como concluídas e visualizar tarefas por prioridade ou categoria.
# O projeto será organizado em partes distintas, utilizando diversas estruturas de dados e funções para oferecer uma experiência completa de gerenciamento de tarefas aos usuários.

lista = ["Leo","Leo",1,1]
print(lista)
dicionario = {"Leo":"1", "Leo":1}
print(dicionario)
tupla = ("Leo",1,"Leo",1)
print(tupla)

def add_tarefa():
    nome_tarefa = str(input("Qual o nome da tarefa?: "))
    descr_tarefa = str(input("Alguma descriçao da tarefa?: "))
    prio_tarefa = str(input("Qual a prioridade da tarefa?: "))
    categ_tarefa = str(input("Qual a categoria da tarefa?: "))


tarefas = {}

while True:
    op = int(input("""
                   O que deseja fazer?
                   1 - Adicionar Tarefa
                   2 - Listar tarefas
                   3 - Concluir uma tarefa
                   """))
    if op == 1:
        add_tarefa()    
