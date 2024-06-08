// Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
// Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
//8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

// 1.salário bruto.
// 2.quanto pagou ao INSS.
// 3.quanto pagou ao sindicato.
// 4.salário liquido
// 5.calcule os descontos e o salário liquido

const salario_bruto = Number(prompt("Qual seu salário bruto?: "))
const desc_inss = salario_bruto * 0.09
const desc_sindicado = salario_bruto * 0.05
const salario_liquido = salario_bruto - (desc_inss + desc_sindicado)
const valor_hora = (salario_liquido/ 30) / 8

alert(
    `   
    O seu salário Bruto é: ${salario_bruto}
    O valor de desconto do INSS é: ${desc_inss}
    O valor de desconto do sindicato é: ${desc_sindicado}
    O salario liquido é: ${salario_liquido}
    O valor hora: ${valor_hora.toFixed(2)}
    `)