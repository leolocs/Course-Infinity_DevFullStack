#12.SENHA CORRETA: Dada a senha 123456Ab. 
#Faça um programa que pede para o usuário inserir uma senha, se ele acertar a senha mencionada acima, mostre uma mensagem de acesso liberado, caso contrario, acesso negado.
senha_certa = "12345Ab"

while True:
    senha = str(input("Por gentileza, digite a senha: "))
    if senha == "sair":
        break
    else:
        if senha == senha_certa:
            print("Senha correta, Acesso permitido!")
            break
        else:
            print("Senha incorreta, Acesso negado!")