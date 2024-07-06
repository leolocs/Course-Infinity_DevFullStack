//  Programa que conta os números até o 10

/*let cont = 1
while (cont <10 ){
    console.log(`O ${cont} é menor que ou igual a 10`)
    cont++
}
console.log("Fim do loop")*/

// Faça um programa que mostre os números entre o 20 e o 50
// let cont = 20
// while (cont < 50){
//     console.log(`O ${cont} é menor ou igual a zero`)
//     cont++
// }
// console.log("Fim do jogo")

//Faça um programa que mostra todos os números pares entre 1 e 100.
// let cont = 1
// while (cont<100){
//     if ( cont > 0 && cont %2 === 0){
//         console.log(`O ${cont} é menor ou igual a zero`)
//     }
//     cont++
// }

//Faça um programa que pede ao usuário 10 números, no final mostrando quantos números foram pares e quantos foram impares

// let cont = 1
// let pares = 0
// let impares = 0 

// while(cont<=10){
//     const num = Number(prompt("Digite um número: "))
//     if (num %2 === 0){
//         pares++
//     }else if(num %2 !=0){
//         impares++
//     }
//     cont++
// }
// document.write(`Dos números contados a quantidade de números pares é ${pares} e ${impares} foram impares`)

//Faça um programa que pede para o usuário digitar 4 notas e calcula a media e mostra se ele for aprovado ou reprovado (media=7) use o while
let cont = 1
let soma_notas = 0
while(cont<=4){
    let nota = Number(prompt("Digite uma nota: "))
    if (nota<=0){
        alert("Digite uma nota maior que zero!")
    }else{
        soma_notas += nota
    }
    cont++
}
media = (soma_notas/4)
if (media>7){
    document.write(`Parabéns sua media é ${media}, você está aprovado!`)
}else{
    document.write(`Sua media é ${media}, você está reprovado!`)
}

//#region 
while(true){
    const idade = Number(prompt("Digite uma idade [0 para sair]: "))

    if(idade === 0){
        break
    }else if(idade >=18){
        maior_18++
    }
}

document.write(`${maior_18} pessoas maiores de idade`)
//#endregion

// #region - FAÇA UM PROGRAMA QUE PEDE UMA QUANTIDADE ILIMITADA DE NOTAS ATÉ QUE O USUÁRIO DIGITE UMA NOTA INVÁLIDA (NOTAS VÁLIDAS 0 A 10)
// DEPOIS CALCULE A MÉDIA DO ALUNO E INFORME SE ELE FOI APROVADO OU REPROVADO (MÉDIA 7).

let soma_total = 0
let qtde_notas = 0

while(true){
    const nota = Number(prompt("Digite uma nota:"))
    if(nota < 0 || nota > 10){
        break
    }else{
        soma_total += nota
        qtde_notas++
    }
}
const media = soma_total / qtde_notas

if(media>=7){
    document.write(`Aprovado com a média ${media}`)
}else{
    document.write(`Reprovado com a média ${media}`)
}
//#endregion
