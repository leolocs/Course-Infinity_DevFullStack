#region - Estrutura de condição, números iguais

# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite outro numero: "))

# if num1 == num2:
#     print("São números iguais")
# else:
#     print("Não são iguais")
#endregion

#region - Verifica se a pessoa é menor ou maior de idade
# Verifica se a pessoa é menor ou maior de idade
# idade = int(input("Informe sua idade: "))

# if idade >= 18:
#     print("é maior de idade!")
# else:
#     print("é menor de idade!")
#endregion

#region - Estrutura IF, ELIF, ELSE : Verifica se número é negativo ou positivo
# Verifica se número é negativo ou positivo
# num = float(input("Digite um número: "))

# if num > 0:
#     print("Número positivo")
# elif num < 0:
#     print("Número negativo")
# else:
#     print("Número neutro")
#endregion


#region - Condição IF, ELIF, ELSE: Semáforo
# Semáforo
# cor = str(input("Escreva  uma cor entre Verde, amarelo ou vermelho: ")).lower().strip() # (.lower(): Transforma todas as letras em minúscula, .strip(): Retira os espaços digitados sem intenção)

# if cor == "verde":
#     print("Avance o sinal")
# elif cor == "vermelho":
#     print("Pare!")
# elif cor == "amarelo":
#     print("Atenção!")
# else:
#     print("Cor inválida")
#endregion

#region - Condição AND
# num = int(input("Digite um número: "))
# if num >= 0 and num <=10:
#     print("Nota válida")
# else:
#     print("Nota inválida")

#endregion

#region - Condição OR
# alte = str(input("Você deseja sair? S/N: ")).lower()

# if alte == "s" or alte == "n":
#     print("Operação válida")
#     if alte == "s":
#         print("Vá embora")
#     else:
#         print("Continue usando o programa")
# else:
#     print("Operação inválida")
#endregion

# region - Condição MATCH com semáforo
# cor = str(input("Digite uma cor: [Vermelho | Amarelo | Vermelho]: "))

# match cor:
#     case "vermelho":
#         print("Pare")
#     case "amarelo":
#         print("Atenção!")
#     case "verde":
#         print("Avance o sinal")
#     case _:
#         print("Cor inválida")
#endregion