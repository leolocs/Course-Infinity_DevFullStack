//Peça ao usuário que insira um preço de um produto usando o prompt. Em seguida, aplique um desconto de 10% a esse preço e exiba o preço com desconto no console.

const preco = Number(prompt("Qual o preço do produto? "))
const valor_c_desconto = preco - preco * 0.10

alert(`O preço do produto com desconto é: ${valor_c_desconto}`)