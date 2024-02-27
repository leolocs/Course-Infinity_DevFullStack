# Criar uma aplicação de gerenciamento de biblioteca com
# classes e POO para representar livros, membros e a biblioteca.
# Passos do projeto:
# Criação de Classes:
# Crie as seguintes classes: Livro, Membro, Biblioteca.

# Classe Livro:
# A classe Livro deve conter atributos como título, autor, ID,
# status de empréstimo (disponível ou emprestado).

# Classe Membro:
# A classe Membro deve conter atributos como nome,
# número de membro e histórico de livros emprestados.

# Classe Biblioteca:
# A classe Biblioteca deve conter um catálogo de livros
# disponíveis, um registro de membros e métodos para
# empréstimo, devolução e pesquisa de livros.

# Operações da Biblioteca:

# Implemente métodos na classe Biblioteca para:
# Adicionar livros ao catálogo.
# Adicionar membros à biblioteca.
# Permitir empréstimo de livros por membros.
# Registrar a devolução de livros.
# Pesquisar livros por título, autor ou ID.


id_livro = 1
num_membro = 1

class Livro:
    def __init__(self, titulo:str, autor:str, id:int):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponibilidade = True

class Membro:
    def __init__(self, nome:str,numero:int):
        self.nome = nome
        self.numero = numero
        self.hist_livros = []

class Biblioteca:
    def __init__(self):
        self.catalogo_livro = []
        self.lista_membros = []
    
    def add_livro(self):
        global id_livro
        while True:
            try:
                titulo_livro = str(input("Digite o titulo do livro: "))
                break
            except:
                print(" Digite o nome de um livro válido!!")
        while True:
            try:                
                autor_livro = str(input("Digite o autor do livro: "))
                break
            except:
                print("Digite um nome de Autor válido com apenas letras!")

        livro = Livro(id=id_livro, titulo=titulo_livro, autor=autor_livro)
        id_livro += 1
        self.catalogo_livro.append(livro)
        print("Livro adicionado com sucesso!")
        

    def add_membro(self):
        global num_membro
        while True:
            try:
                nome_membro = str(input("Digite o nome do membro: "))
            except:
                print("Digite um nome de membro válido!")
            
            membro = Membro(numero=num_membro, nome=nome_membro)
            self.lista_membros.append(membro)
            num_membro += 1
            print (f"O Membro {membro.nome}, ID = {membro.numero} foi adicionado, com sucesso!")

    def emprestar_livro(self):
        while True:
            try:
                num_membro_escolhido = str(input("Digite qual o numero do Membro: "))
                break
            except:
                print("Digite um ID e o numero do membro válidos!")
        for membro_atual in self.lista_membros:
            if membro_atual.id == num_membro_escolhido:
                while True:
                    try:
                        id_livro_escolhido = int(input("Digite qual o ID do livro após a pesquisa: "))
                        break
                    except:
                        print("Digite um ID de livro válido!")
                for livro_atual in self.catalogo_livro:
                    if livro_atual == id_livro_escolhido and livro_atual.disponibilidade:
                        livro_atual.disponibilidade = False
                        membro_atual.hist_livros.append(livro_atual)
                        return f"O Livro {livro_atual.titulo} foi emprestado para o Membro: {membro_atual.nome}"


    def devolver_livro(self):
        while True:
            try:
                id_livro_escolhido = int(input("Qual o ID do livro que vc deseja devolver?: "))
                break
            except:
                print("Digite um ID válido!")
            
        for livro in self.catalogo_livro:
            if livro.id == id_livro_escolhido and livro.disponibilidade == False:
                livro.disponibilidade == True
                return f"Livro {livro.titulo} foi devolido, e está disponível novamente no Catálogo"
    
    def pesquisar_livro(self):
        pesquisa = str(input("Digite o ID do livro ou Título do Livro ou Autor do livro: "))
        livro_nao_encontrado = True
        for livro_atual in self.catalogo_livro:
            if livro_atual.titulo == pesquisa or livro_atual.autor == pesquisa or str(livro_atual.id) == pesquisa:
                livro_nao_encontrado = False
                print(f"""
                    Informações do livro encontrado:
                    ID do livro: {livro_atual.id}
                    Título do livro: {livro_atual.titulo}
                    Autor do Livro: {livro_atual.autor}
                    Status da disponibilidade: {livro_atual.disponibilidade}
                    """)

biblioteca = Biblioteca()

while True:
    menu = int(input("""Oque deseja fazer:
                     1 - Adicionar Livro
                     2 - Adicionar Membro
                     3 - Emprestar Livro
                     4 - Devolver Livro
                     5 - Pesquisar livro
                     0 - Sair do programa
                     """))
    match menu:
        case 0:
            print("Programa encerrado!")
            break
        case 1:
            biblioteca.add_livro()

        case 2:
            biblioteca.add_membro()
        
        case 3:
            biblioteca.emprestar_livro()
        
        case 4:
            biblioteca.devolver_livro()
        
        case 5:
            biblioteca.pesquisar_livro()

        case _:
            print("Opção valida")
