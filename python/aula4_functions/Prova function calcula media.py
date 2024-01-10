# Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
# Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno.
# Também crie uma função chamada "verificar_situacao" que, com base na média calculada, 
# irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

def calc_media(notas):
    if not notas:
        return "Não possui notas registradas"
    else:
        return sum(notas)/len(notas)

def ver_situacao(media):
    if media == 10:
        return "Parabéns sua media é 10"
    elif media < 7:
        return f"Reprovado"
    elif media > 7:
        return f"Aprovado"

notas = []
qtd_notas = int(input("Quantas notas você deseja inserir? "))
for n in range(qtd_notas):
    nota = float(input(f"Digite a nota {n + 1}: "))
    notas.append(nota)

media = calc_media(notas)
situacao_aluno = ver_situacao(media)

print(f"A media do aluno é: {media:.1f}")
print(f"Situação do aluno: {situacao_aluno}")