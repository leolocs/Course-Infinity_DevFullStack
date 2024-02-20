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
        

    def emprestar_livro(self):
        pass

    def devolucao_livro(self):
        pass

    def pesquisar_livro(self):
        pass

while True:
    menu = int(input("""Oque deseja fazer:
                     1 - Adicionar Livro
                     2 - Emprestar Livro
                     3 - Devolver Livro
                     4 - Pesquisar livro
                     3 - Adicionar Membro"""))