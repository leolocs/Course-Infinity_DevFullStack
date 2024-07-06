// Você foi contratado(a) para desenvolver um programa que irá auxiliar um professor a calcular algumas estatísticas das notas de seus alunos.
// O programa deve solicitar ao professor o número total de estudantes na turma e, em seguida, pedir que ele insira as notas de cada aluno individualmente.
// Após receber todas as notas, o programa deverá calcular a média da turma e identificar a maior e a menor nota obtida.

// Instruções:

// Solicite ao professor que digite o número total de estudantes na turma.
// Em seguida, peça que o professor insira a nota de cada aluno individualmente, uma por vez.
// Calcule a média da turma somando todas as notas e dividindo pelo número total de estudantes.
// Identifique e registre a maior nota obtida na turma.
// Ao final, exiba a média da turma e a maior e a menor nota encontrada.

// Dicas:

// Utilize um loop while para coletar as notas de todos os alunos.
// Armazene as notas em uma variável e vá atualizando o valor da soma a cada nova nota inserida.
// Compare cada nota com a maior nota atualmente registrada para encontrar a maior nota.
// Para calcular a média, divida a soma das notas pelo número total de estudantes.
// Exiba os resultados de forma clara e organizada.


// Lembre-se de testar o programa com diferentes valores de notas e número de estudantes para garantir que ele funcione corretamente em diversas situações.
// Boa programação

let cont= 1
let soma= 0
let media = 0
let maior_nota = 0
let menor_nota = 0

const qtd_alunos = Number(prompt("Digite a quantidade de alunos: "))
while(cont <= qtd_alunos){
    const nota = Number(prompt("Digite uma nota do aluno: "))
    if(nota > maior_nota){
        maior_nota = nota
    }else if(nota< menor_nota){
        menor_nota = nota
    }
    cont++
    soma += nota
    alert(`+ ${cont} notas cadastradas`)
}
media = soma/qtd_alunos
console.log(`A média da turma é ${media} a menor nota:${menor_nota} e a maior nota:${maior_nota}`)