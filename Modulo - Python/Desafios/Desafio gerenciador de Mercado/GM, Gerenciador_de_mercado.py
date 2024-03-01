# Primeiramente passaremos as informações! 
# ```
# A duração do desafio é do momento do anúncio do desafio até o dia 29/02/24 19:00h - Quinta-feira
# ```
# ```
# Ao finalizar o seu desafio, mande um e-mail com o título 'DESAFIO DEV FULL STACK' contendo:
# - Arquivos utilizados incluindo imagens para: dev@infinityschool.com.br
# - Nome completo 
# - Chave PIX
# - Nome no Discord

# Prêmio: R$40.00 - quarenta reais
# ```

# Segue agora desafio:

# **DESAFIO**

# Desenvolver um sistema de gerenciamento para um mercado local. O programa deve permitir a administração dos produtos, clientes e vendas de forma eficiente e organizada.

# **OBS:** O código deve ser escrito em POO (Programação Orientado a Objetos)

# **CLASSES E FUNCIONALIDADES**

# **Produto:**
# ```
# Atributos:
#    - Nome: nome do produto.
#    - Código: identificador único do produto.
#    - Preço: preço unitário do produto.
#    - Quantidade: quantidade disponível em estoque.
# ```

# **Cliente:**
# ```
# Atributos:
#    - Nome: nome do cliente.
#    - CPF: número de CPF do cliente.
#    - Histórico de Compras: registro das compras realizadas pelo cliente.
# ```

# **Venda:**
# ```
# Atributos:
#    - Produtos Vendidos: lista dos produtos vendidos na transação.
#    - Cliente Associado: cliente que realizou a compra.
#    - Valor Total: valor total da venda.
# ```
# ```
# Métodos:
#    - Adicionar Produto: adiciona um produto à lista de produtos vendidos.
#    - Calcular Total: calcula o valor total da venda.

# **CarrinhoDeCompras:**
# ```
# Atributos:
#    - Produtos no Carrinho: lista dos produtos adicionados ao carrinho.
#    - Cliente Associado: cliente que está utilizando o carrinho.
# ```
# ```
# Métodos:
#    - Adicionar Venda: adicionar uma venda ao carrinho de compras
#    - Adicionar Produto: adiciona um produto ao carrinho.
#    - Calcular Total: calcula o valor total dos produtos no carrinho.
# ```

# **Mercadinho:**
# ```
# Atributos:
#    - Produtos em Estoque: lista dos produtos disponíveis para venda.
# ```
# ```
# Métodos:
#    - Adicionar Produto: adiciona um novo produto ao estoque.
#    - Remover Produto: remove um produto do estoque.
#    - Adicionar Estoque: aumenta a quantidade de um produto no estoque.
#    - Remover Estoque: reduz a quantidade de um produto no estoque.
# ```

# **OBS:**
# - Tratamento de Exceções: Implementação de classes de exceção para situações como estoque insuficiente, cliente inexistente, etc.
# - Interatividade: Desenvolvimento de um programa de console que permita ao usuário:
# - Adicionar produtos ao estoque.
# - Remover produtos do estoque.
# - Adicionar clientes.
# - Realizar vendas.
# - Consultar relatórios.


cod_produto = 1

class Produto:
    def __init__(self, nome:str, cod:int, preco:float, qtd:int):
        self.nome = nome
        self.cod = cod
        self.preco = preco
        self.qtd = qtd
        

class Cliente:
    def __init__(self, nome:str, cpf:int):
        self.nome = nome
        self.cpf = cpf
        self.hist_compras_cliente = []

class Caixa:     # Pela lógica a Classe Venda foi substituida pela Classe Caixa, pois logicamente faz mais sentido adicionar vendas ao caixa e o mesmo calcular o total de vendas!
    def __init__(self, valor_total:float, cliente_ass:str):
        self.vendas = []
        self.cliente_ass = cliente_ass

    def add_venda(self, venda, cliente):
         while True:
            try:
                cpf_cliente_inserido = int(input("Digite o CPF do cliente cadastrado!: "))
                for cliente in self.clientes:
                    if cliente.cpf == cpf_cliente_inserido:   
                        print("Cliente encontrado com sucesso!")
                        break
                    else:
                        print("Cliente não encontrado!, cadastre o cliente para proseguir com a compra!")
                        mercadinho.add_cliente()
            except:
                print("Digite um codigo válido do produto!")
            while True:
                try:
                    cod_produto = int(input("Digite o codigo do produto: "))
                    for produto in self.produtos_em_estoque:
                        if produto.cod == cod_produto:
                            break
                    else:
                        print("Produto não encontrado em estoque!, cadastre o produto no estoque do mercado para poder prosseguir com a compra!")
                except:
                    print("Digite um codigo válido do produto!")

                while True:
                    try:
                        nome_produto = str(input("Digite o nome do produto: ")).lower()
                        if nome_produto.isalpha() or nome_produto.strip():
                            break
                        else:
                            print("Digite um nome válido de produto com apenas letras!")
                    except:
                        print("Digite um nome válido de produto!")
                while True:
                    try:
                        preco_produto = float(input("Digite o valor do produto: "))
                        break
                    except:
                        print("Digite um valor válido de produto apenas com numeros!")
                while True:
                    try:
                        qtd_produto = int(input("Digite a quantidade do produto: "))
                        break
                    except:
                        print("Digite uma quantidade válida do produto com apenas numeros!")

                produto = Produto(cod=cod_produto, nome=nome_produto, preco=preco_produto, qtd=qtd_produto)
                self.vendas.append(produto)
                self.hist_compras_cliente.append(self.vendas)


    def cal_total(self):
        pass

class CarrinhoDeCompras:
    def __init__(self, cliente:str):
        self.produtos_no_carrinho = []
        self.cliente = cliente

    def add_produto(self):
        pass

class Mercadinho:
    def __init__(self):
        self.produtos_em_estoque = []
        self.clientes = []

    def add_produto_ao_estoque(self):
        global cod_produto
        while True:
            try:
                nome_produto = str(input("Digite o nome do produto que voce deseja adicionar ao estoque: "))
                if nome_produto.isalpha() or nome_produto.strip():
                    break
                else:
                    print("Digite apenas letras!")
            except:
                print("Digite o nome de um produto válido!")
        while True:
            try:
                preco_produto = float(input("Qual o preço do produto: "))
                break
            except:
                print("Digite um preço válido do produto!")
        while True:
            try:
                qtd_produto = int(input("Digite a quaintidade do produto: "))
                break
            except:
                print("Digite uma quantidade válida do produto com apenas numeros inteiros!")

        produto = Produto(cod=cod_produto, nome=nome_produto, preco=preco_produto, qtd=qtd_produto)
        cod_produto += 1
        self.produtos_em_estoque.append(produto)
        print(f"O produto {produto.nome} foi adicionado ao estoque de produtos!")

        
    def remover_produto_do_estoque(self):
        while True:
            try:
                produto_a_remover = int(input("Digite o codigo do produto que deseja remover: "))
                break
            except:
                print("Digite um codigo de produto válido, com apenas numeros!")
            for produto in self.produtos_em_estoque:
                if produto.cod == produto_a_remover:
                    self.produtos_em_estoque.remove(produto)
    
    def add_cliente(self):
        while True:
            try:
                nome_cliente = str(input("Digite o nome do cliente: ")).lower()
                if nome_cliente.isalpha() or nome_cliente.strip():
                    break
                else:
                    print("Digite apenas letras!")
            except:
                print("Digite o nome de um cliente válido!")
        while True:
            try:
                cpf_num = int(input("Digite o cpf do cliente: "))
                break
            except:
                print("Digite um numero de CPF válido com apenas números!")

        cliente = Cliente(nome=nome_cliente, cpf=cpf_num)
        self.clientes.append(cliente)
        print(f"O Cliente {cliente.nome.capitalize()}, com CPF: {cliente.cpf} foi adicionado com sucesso ao Mercadinho!")

    def add_estoque(self):
        pass

    def remover_estoque(self):
        pass

mercadinho = Mercadinho()
carrinho = CarrinhoDeCompras()
caixa = Caixa()

while True:
    menu = int(input(""" 
                ##### Bem-vindo ao SGM - Sistema gerenciador de mercado #####
                1 - Adicionar produtos ao estoque
                2 - Remover produtos do estoque
                3 - Adicionar cliente
                4 - Realizar uma venda
                5 - Consultar relatorio
                0 - Sair do Programa
                Oque deseja fazer: """))
    match menu:
        case 1:
            mercadinho.add_produto_ao_estoque()
        case 2:
            mercadinho.remover_produto_do_estoque()
        case 3:
            mercadinho.add_cliente()
        case 4:
            caixa.add_venda()
        case 5:
            
        case 0:
            print("Encerrando o programa!")
            break
        