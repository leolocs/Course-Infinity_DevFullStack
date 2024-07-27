#Crie um programa que gere a sequência de Fibonacci até o número digitado pelo usuário
# Inicializa os dois primeiros termos da sequência
termo1 = 0
termo2 = 1

# Exibe os primeiros 10 termos da sequência de Fibonacci
while True:
    num = int(input("\n Digite o número que deseja saber a sequencia de fibonnaci: "))
    for n in range(15):
        print(termo1, end=" ")
        proximo_termo = termo1 + termo2
        termo1, termo2 = termo2, proximo_termo
    break
    
