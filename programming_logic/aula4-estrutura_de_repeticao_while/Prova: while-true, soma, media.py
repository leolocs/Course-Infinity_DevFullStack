#region - Faça um programa em python que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
count = 0
media = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        break
    elif num > 0:
        count += 1
        soma += num
        media = soma/count
print (f"""A soma, media e quantidade de números digitados respectivamente são:
    Soma = {soma}
    Media = {media}
    {count} números digitados""")

#endregion
