// Peça ao usuário para digitar sua idade usando o prompt e, em seguida, calcule e exiba o ano de nascimento com uma frase personalizada usando o console.

const idade = Number(prompt("Digite sua idade: "))
const data_atual = new Date().getFullYear()
const ano_nasc = data_atual-idade

alert(`Seu ano de nascimento é: ${ano_nasc}`)