// Escreva um programa em JavaScript que solicite ao usuário o nome, altura em centímetros e peso de uma pessoa.
// O programa deve calcular o índice de massa corporal (IMC) dessa pessoa, considerando a fórmula IMC = peso / (altura * altura),
// onde a altura deve ser convertida de centímetros para metros. Em seguida, o programa deve classificar o peso com base no IMC calculado,
// de acordo com a tabela a seguir:

// Menor que 16: Baixo peso muito grave
// De 16 a 16.99: Baixo peso grave
// De 17 a 18.49: Baixo peso
// De 18.50 a 24.99: Peso normal
// De 25 a 29.99: Sobrepeso
// De 30 a 34.99: Obesidade grau I
// De 35 a 39.99: Obesidade grau II
// Maior ou igual a 40: Obesidade grau III
// O programa deve exibir o nome da pessoa, o índice de massa corporal calculado e a classificação correspondente.

const nome = prompt("Digite seu nome: ")
const altura = Number(prompt("Digite sua altura(em centimetros): "))
const peso = Number(prompt("Digite qual seu peso: "))

altura_metros = altura/100
imc = peso/(altura_metros*altura_metros)

if(imc<16){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está GRAVEMENTE ABAIXO DO PESO!`)
}else if(imc>16 && imc<=16.99){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está MUITO ABAIXO DO PESO!`)
}else if(imc>17 && imc <= 18.49){
        alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está ABAIXO DO PESO!`)
}else if(imc>=18.5 && imc<=25){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está com PESO IDEAL!`)
}else if(imc>25 && imc <=30){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está com SOBREPESO!`)
}else if(imc>30 && imc<=35){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está com OBESIDADE GRAU 1 !`)
}else if(imc>35 && imc<=40){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está com OBESIDADE GRAU 2!`)
}else if(imc >= 40){
    alert(`${nome}, seu IMC é de ${imc.toFixed(2)}, você está com OBESIDADE MÓRBIDA!`)
}
