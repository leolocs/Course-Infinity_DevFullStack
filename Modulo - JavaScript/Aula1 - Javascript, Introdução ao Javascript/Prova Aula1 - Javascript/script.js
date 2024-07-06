// Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3).
// Calcule a média ponderada das notas e atribua o resultado à variável "media".
// Após o cálculo, exiba a média ponderada no console.

// OBS: Para calcular a média ponderada multiplica os valores das notas pelos valores dos pesos, e divide pelas somas de todos os pesos.
// Lembre-se de declarar valores para os pesos e para as notas.

const n1 = Number(prompt("Digite uma nota: "))
const n2 = Number(prompt("Digite uma nota: "))
const n3 = Number(prompt("Digite uma nota: "))
soma = n1+n2+n3
media = soma/3

console.log(`A sua média ponderada é: ${media.toFixed(0)}`)