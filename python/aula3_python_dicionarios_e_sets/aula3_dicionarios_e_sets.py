#Exemplo de criação de lista:
pessoa = ["leo", 25, 1.76, True, 299] 
# A partir da 4ª casa da lista se torna sem sentido a informação sem uma identificação, por isso passa a se usar dicionários:

# Exemplo de criação de dicionário:
pessoa2 = {"nome":"Leonardo", "idade": 25, "altura": 1.76} #na criação de um dicionário se torna mais fácil entender oque cada item significa, através de um nome para identificação
#imprimindo o item de um dicionário
print(pessoa2["nome"])

#classes conhecidas:
str()
int()
float()
bool()
list()
tuple()
# nova classe aprendida:
dict()

#criando dicionários com a classe dict():
dicionario = dict([("Módulo",'python'), ("Instituição","Infinity School")])

# Outra forma para criar um dicionário utilizando classe dict():
dicionario2 = (Módulo = 'Python', Instituição = 'Infinity School')


# Dicionários usando com Métodos:
list(dicionario) # Retorna uma lista com todas as chaves usadas no dicionário

len(dicionario) # Retorna o número de itens de um dicionário

dicionario[chave] # retorna o valor da chave específica entre os valores colchetes[] caso a chave não exista, uma exceção tipo KeyError será lançada

dicionario[chave] = valor # altera o valor de uma chave dentro do dicionario, atribuindo um novo valor a ela

del dicionario[chave] # Deleta a chave e valor especificada dentro do colchetes[];

chave in dicionario # retorna True se a chave for encontrada no dicionario, se não retorna false

dicionario_copia = dicionario.copy() # Faz uma copia do dicionario original e atribui a um novo dicionario;

dict.fromkeys(dicionario) # Cria uma lista com tuplas com base em um dicionario;

