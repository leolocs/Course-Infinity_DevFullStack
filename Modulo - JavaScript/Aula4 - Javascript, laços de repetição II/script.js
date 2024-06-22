// Faça um programa que pede para o usuário digitar seu nome e conte quantas vogais tem no nome da pessoa e mostre na tela.

const nome = prompt("Digite seu nome: ")
const vogais = "aeiouáàâãéèíìóòõú"
let letras_vogais = 0

for(let letra of nome){
    if(vogais.includes(letra.toLowerCase())){
        letras_vogais++
    }
}
document.write(`O nome ${nome} digitado possui ${letras_vogais} letras vogais`)