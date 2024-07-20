// #region - Atividade 01 - Faça um programa que leia 20 números inteiros e armazene-os em um vetor.
//Armazene os números pares no vetor 'PAR' e os números ímpares no vetor 'ímpar '. Imprima os três vetores.
const num_pares = []
const num_impares = []
const numeros = []
for(i=0;i<20;i++){
    const num = Number(prompt("Digite um número: "))
    if(num %2 == 0){
        num_pares.push(num)
    }else{
        num_impares.push(num)
    }
    numeros.push(num)
}
console.log(`Os números apresentados foram:${numeros}`)
console.log(`Os números numeros pares foram: ${num_pares}`)
console.log(`Os números numeros impares foram: ${num_impares}`)

//#endregion

// #region = Atividade 02: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.


//#endregion