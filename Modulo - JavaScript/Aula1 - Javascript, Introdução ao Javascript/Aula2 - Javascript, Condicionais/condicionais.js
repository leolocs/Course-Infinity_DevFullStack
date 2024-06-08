// const idade = Number(prompt("Digite sua idade: "))
// if(idade >= 18){
//     alert("É maior de idade!")
// }else{
//     alert("É menor de idade!")
// }

//Faça um programa que pede para o usuário digitar um numero e mostre se o número é positivo ou negativo:
// const numero = Number(prompt("Digite um número: "))

// if(numero > 0){
//     alert(`O número ${numero} digitado é POSITIVO!`)
// }else if(numero < 0){
//     alert(`O número digitado é NEGATIVO!`)
// }else{
//     alert(`O número digitado é NEUTRO!`)
// }

//Faça um programa que pede para o usuário digitar sua idade e mostre se seu voto é:
//PROIBIDO
//OBRIGATÓRIO
//FACULTATIVO
const idade = Number(prompt("Digite sua idade: "))

if(idade < 16){
    alert(`Seu voto é PROIBIDO, você é menor de idade!`)
}else if(idade >= 16 && idade < 18 || idade >=70 && idade<200) {
    alert('Seu voto é FACULTATIVO!, não faz diferença')
}else if(idade >= 18 && idade<= 70){
    alert("Seu voto é OBRIGATÓRIO!")
}else if(idade >= 200){
    alert("Defuntos são incapazes de votar!!")
}
