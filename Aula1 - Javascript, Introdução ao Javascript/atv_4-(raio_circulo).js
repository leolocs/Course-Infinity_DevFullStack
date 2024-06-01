// Crie um programa que solicite ao usuário que insira o raio de um círculo usando o prompt e, em seguida, calcule e exiba a área do círculo usando o console.

const raio = Number(prompt("Informe o raio do circulo: "))
const pi = Math.PI
const area = raio*pi

alert(`A área do circulo pelo valor do raio informado é: ${area.toFixed(2)}`)

