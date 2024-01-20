#Q3. Faça um programa que pede para o usuário digitar 8 notas e no final calcula a média dessas notas
soma_notas = 0
for n in range(1,9):
    nota = float(input(f"Digite a {n}ª nota: "))
    if nota <= 0:
        print("Digite uma nota válida maior que zero 0")
    else:
        soma_notas += nota
media = soma_notas /8 
print(f"A media das notas digitadas é: {media}")