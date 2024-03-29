#region - Leia os dados de um usuário - nome, sobrenome, idade, email - e
# imprima-os enumerando os mesmos.

nome = str(input("Qual o seu nome: "))
sobrenome = str(input("Qual seu sobrenome? "))
idade = int(input("Qual sua idade? "))
email = str(input("Qual seu email? "))

Aluno = {
    "1 - nome": nome,
    "2 - sobrenome":sobrenome,
    "3 - idade":idade,
    "4 - email":email
}
print(Aluno)

#endregion

#region - Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
# a. Nome do aluno
# b. As 4 notas obtidas
# c. Maior nota
# d. Menor nota
# e. Média
# f. Situação
# E imprima as informações deste aluno na saída padrão

# nota1 = float(input("Digite a 1ª nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# nota3 = float(input("Digite a 3ª nota: "))
# nota4 = float(input("Digite a 4ª nota: "))

notas = []
maior_nota = 0
menor_nota = float("inf")
soma = 0
aprovado = "reprovado"

for n in range(1,5):
    nota = float(input(f"Digite a {n}ª nota: "))
    notas.append(nota)
    soma += nota

    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

# Forma reduzida de descobrir a Maior e menor nota
# maior = max(notas)
# menor = min(notas)
if notas[0] > notas[1] and notas[0] > notas[2] and notas[0] > notas[3]:
    Aluno["Maior nota: "] = notas[0]
elif notas[1] > notas[0] and notas[1] > nota[2] and notas[1] > notas[3]:
    Aluno["Maior nota: "] = notas[1]
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    Aluno["Maior nota: "] = nota3
elif nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
    Aluno["Maior nota: "] = nota4

if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    Aluno["Menor nota: "] = nota1
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    Aluno["Menor nota: "] = nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    Aluno["Menor nota: "] = nota3
elif nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    Aluno["Menor nota: "] = nota4

# Tirando a média das notas digitadas
if media >= 7 and media < 10:
    Aluno["Situação": "Aprovado"]
elif media < 7:
    Aluno["Situação": "Reprovado"]
elif media == 10:
    Aluno["Situação": "Aprovado com distinção!"]

media = sum(notas)/len(notas)

Aluno.update({
    "Nota 1": notas[0],
    "Nota 2": notas[1],
    "Nota 3": notas[2],
    "Nota 4": notas[3],
    "Media": media
})


print(Aluno)
#endregion
