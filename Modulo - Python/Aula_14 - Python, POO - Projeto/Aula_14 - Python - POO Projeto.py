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
                titulo_livro = str(input("Digite o titulo do livro: ")).lower()
                if titulo_livro.isalpha() or titulo_livro.strip():
                    break
                else:
                    print("Digite apenas letras!")
            except:
                print(" Digite o nome de um livro válido!!")
        while True:
            try:                
                autor_livro = str(input("Digite o autor do livro: ")).lower()
                if autor_livro.isalpha() or autor_livro.strip():
                    break
                else:
                    print("Digite apenas letras!")
            except:
                print("Digite um nome de Autor válido!")

        livro = Livro(id=id_livro, titulo=titulo_livro, autor=autor_livro)
        id_livro += 1
        self.catalogo_livro.append(livro)
        print(f"O Livro: {livro.titulo.capitalize()} do autor {livro.autor.capitalize()} com ID: {livro.id} foi cadastrado com sucesso!")
        

    def add_membro(self):
        global num_membro
        while True:
            try:
                nome_membro = str(input("Digite o nome do membro: ")).lower()
                if nome_membro.isalpha() or nome_membro.strip():
                    break
                else:
                    print("Digite apenas letras!")
            except:
                print("Digite um nome de membro válido!")
            
        membro = Membro(numero=num_membro, nome=nome_membro)
        self.lista_membros.append(membro)
        num_membro += 1
        print (f"O Membro {membro.nome.capitalize()}, ID = {membro.numero} foi adicionado, com sucesso!")

    def emprestar_livro(self):
        while True:
            try:
                num_membro_escolhido = int(input("Digite qual o numero do Membro: "))
                break
            except:
                print("Digite um numero de membro válido!")
        for membro_atual in self.lista_membros:
            if membro_atual.numero == num_membro_escolhido:
                while True:
                    try:
                        id_livro_escolhido = int(input("Digite qual o ID do livro para o emprestimo: "))
                        break
                    except:
                        print("Digite um ID de livro que seja um número válido!")
            for livro_atual in self.catalogo_livro:
                if livro_atual.id == id_livro_escolhido:
                    if livro_atual.disponibilidade:
                        livro_atual.disponibilidade = False
                        membro_atual.hist_livros.append(livro_atual)
                        print (f"O Livro {livro_atual.titulo} foi emprestado para o Membro: {membro_atual.nome.capitalize()}")

    def devolver_livro(self):
        while True:
            try:
                id_livro_escolhido = int(input("Digite o ID do livro que deseja devolver: "))
                break
            except:
                print("Digite um numero de ID válido!")
        for livro in self.catalogo_livro:
            if livro.id == id_livro_escolhido:
                if livro.disponibilidade == False:
                    livro.disponibilidade = True
                    print (f"Livro {livro.titulo} foi devolido, e está disponível novamente no Catálogo")
        
    def pesquisar_livro(self):
        pesquisa = str(input("Digite o ID do livro ou Título do Livro ou Autor do livro: ")).lower()
        livro_nao_encontrado = True

        for livro_atual in self.catalogo_livro:
            if pesquisa in str(livro_atual.titulo).lower() or pesquisa in str(livro_atual.autor)  or pesquisa in str(livro_atual.id):
                livro_nao_encontrado = False
                print(f"""
                    Informações do livro encontrado:
                    ID do livro: {livro_atual.id}
                    Título do livro: {livro_atual.titulo.capitalize()}
                    Autor do Livro: {livro_atual.autor.capitalize()}
                    Disponibilidade: {livro_atual.disponibilidade}
                    """)
                
    def visualizar_catalogo(self):
        if self.catalogo_livro:
            for livro in self.catalogo_livro:
                print(f"""
                    ID: {livro.id}
                    Título:{livro.titulo.capitalize()}
                    Autor:{livro.autor.capitalize()}
                    Disponibilidade:{livro.disponibilidade}
                    """)
        else:
            print("O catálogo de livros está vazio, adicione algum livro ao catálogo da Biblioteca na função (1) de Adicionar Livro!")

biblioteca = Biblioteca()

while True:
    menu = int(input("""
                     ##### SGB: Sistema de Gerenciamento de bibliotecas #####
                     Escolha uma das opções abaixo:
                     1 - Adicionar Livro
                     2 - Adicionar Membro
                     3 - Emprestar Livro
                     4 - Devolver Livro
                     5 - Pesquisar livro
                     6 - Ver Catálogo de livros
                     0 - Sair do programa
                     Oque deseja fazer: """))
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

        case 6:
            biblioteca.visualizar_catalogo()

        case _:
            print("Opção inválida")
