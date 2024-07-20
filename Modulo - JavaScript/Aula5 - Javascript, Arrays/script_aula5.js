// const nome = "Leonardo"
// const idade = 26
// const habilitado = true

// const lista_frutas = ["Melancia", "Uva", "Banana", "Goiaba"]
// alert(frutas[0])


// #region - Crie um array de frutas vazio e então peça para o usuário inserir o nome de 6 frutas e adicione na lista(push) as frutas, quando terminar de pedir mostre no console log o resutado.
// Mostre tambem qual foi a segunda fruta.
// const frutas = []
// for(i=1;i<=6;i++){
//     const fruta = prompt("Digite o nome de uma fruta: ")
//     frutas.push(fruta)
// }
// alert(frutas);
// alert(frutas[1]);

// const frutas = ["melancia", "banana", "Uva", "goiaba"]
// console.log(frutas)
// const posicao = frutas.indexOf("banana")
//#endregion

//#region - DADO O ARRAY DE FRUTAS ["Melancia", "Uva", "Banana", "Goiaba", "Pêra", "Maça", "Acerola", "Kiwi", "Abacaxi", "Abacate"]
//PEÇA PRO USUÁRIO DIGITAR O NOME DE UMA FRUTA E REMOVA ELA DA LISTA. 
const frutas = ["Melancia", "Uva", "Banana", "Goiaba", "Pêra", "Maça", "Acerola", "Kiwi", "Abacaxi", "Abacate"]
alert(frutas)
const fruta = prompt("Digite o nome da fruta que deseja remover: ")
const posicao = frutas.indexOf(fruta)
if (posicao === -1){
    alert("A fruta informada não existe")
}else{
    frutas.splice(posicao,1)
}
console.log(`${frutas}`)
//#endregion

//#region - 
const animais = ["cachorro","Gato", "Papagaio"]

// animais.push("Tartaruga")       //adiciona ao fim da lista
// animais.shift()                 // remove do começo
// animais.unshift("coelho")       //adiciona no começo
// animais.[2] = "Hamster"         //altera uma posição especifica
// console.log(animais.length)     // visualiza o tamanho da lista
// console.log(animais[1])         // visualiza um elemento em uma posição especifica
// console.log(animais)            // ver toda a lista.

//#endregion