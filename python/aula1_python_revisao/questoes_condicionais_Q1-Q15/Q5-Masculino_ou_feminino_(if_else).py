#5.MASCULINO OU FEMININO: Faça um programa que pede para o usuário digitar uma letra (M ou F) e mostra uma mensagem respectiva M - Masculino, F - Feminino ou Sexo inválido
while True:
    sexo = str(input("Qual o sexo entre (M/F)? "))
    if sexo == "out":
        break
    elif sexo.lower() == "m":
        print("Sexo Masculino!")
    elif sexo.lower() == "f":
        print("Sexo é feminino!")
    else:
        print("Sexo inválido!  Digite uma letra de sexo válida! ")