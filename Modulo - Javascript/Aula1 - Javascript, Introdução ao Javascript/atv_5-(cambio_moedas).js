// Crie um programa que solicite ao usuário que insira um valor em dólares usando o prompt. Em seguida, converta esse valor para euros (1 dólar = 0,85 euros) 
// e exiba o resultado no console.

const dolar = Number(prompt("Digite qual o valor em dólar: "))
const euro = 0.92
const valor_cambio = dolar/euro

alert(`O valor US${$dolar} equivale a: €${valor_cambio.toFixed(2)}`)