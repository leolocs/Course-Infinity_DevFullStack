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
id_membro = 1

class Livro:
    def __init__(self, titulo=str, autor=str, id=int):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome=str,numero=int) -> None:
        self.nome = nome
        self.numero = numero
        self.hist_livros = []

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livro = []
        self.lista_membros = []
    
    def add_livro(self):
        titulo_livro = str(input("Digite o titulo do livro: "))
        autor_livro = str(input("Digite o autor do livro: "))
        livro = Livro(id=id_livro, titulo=titulo_livro, autor=autor_livro)
        self.catalogo_livro.append(Livro)
        id_livro += 1

    def add_membro(self):
        nome_membro = str(input("Digite o nome do membro: "))
        membro = Membro(nome=nome_membro,numero=id_membro)
        self.lista_membros.append(Membro)
        id_membro += 1

    def emprestar_livro(self, ):
        id_livro = int(input("Digite qual o ID do livro após a pesquisa: "))
        num_membro = str(input("Digite qual o numero do Membro: "))
    
        for livro in self.catalogo_livro:
            if id_livro == livro.id:
                livro.disponivel == False

        for membro in self.lista_membros:
            if num_membro == membro.id:
                membro.hist_livros.append(livro)

    def devolver_livro(self):
        id_livro = int(input("Qual o ID do livro que vc deseja devolver?: "))
        for livro in self.catalogo_livro:
            if id_livro == livro.id:
                livro.disponivel == True
        
    def pesquisar_livro(self):
        

while True:
    menu = int(input("""Oque deseja fazer:
                     1 - Adicionar Livro
                     2 - Emprestar Livro
                     3 - Devolver Livro
                     4 - Pesquisar livro
                     3 - Adicionar Membro
                     0 - Sair do programa
                     """))
    match menu:
        case 0:
            print("Programa encerrado!")
            break
        case 1:
            Biblioteca.add_livro()

        case 2:
            Biblioteca.emprestar_livro()
        
        case 3:
            Biblioteca.devolver_livro()
        
        case 4:
            op = int(input("""
                           Deseja pesquisar o livro por:
                           1 - Nome
                           2 - Id
                           3 - Autor 
                           """))
            match op:
                case 1:
                    nome = str(input("Qual nome do Livro: ")).lower().strip()
                    
