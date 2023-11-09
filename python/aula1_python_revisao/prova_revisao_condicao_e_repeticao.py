# region - PROVA REVISÃO DE CONDIÇÃO E REPETIÇÃO
# Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, 
# em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado 
# pelo usuário é igual ao email e senha cadastrados antecipadamente. 
# E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

email_certo = "leo@gmail.com"
senha_certa = "1234abcd"
while True:
    email = str(input("Digite o email: "))
    senha = str(input("Digite a senha: "))
    if email == email_certo and senha == senha_certa:
        print("Acesso liberado!")
        break
    else:
        print("Acesso negado! Email ou senha incorretos, tente novamente")



#endregion
