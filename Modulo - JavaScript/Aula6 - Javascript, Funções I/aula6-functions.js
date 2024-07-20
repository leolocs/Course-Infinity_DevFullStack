//#region - Exemplo de função:
// idade = Number(prompt("Qual sua idade: "))
// if(idade>=18){
//     document.write("Pode entrar")
// }else{
//     document.write("Não pode passar")
// }

// function saudacao(nome){
//     return `Olá ${nome} seja vem vindo`
// }

// console.log(saudacao("joão"))
// console.log(saudacao("Maria"))
//#endregion
// #region - Faça uma função que recebe duas notas e retorne se o aluno foi aprovado ou reprovado
// function calc_media(n1,n2,n3){
//         media = n1,n2,n3/3
//         if(media<7){
//             return `Sua media foi ${media} você foi reprovado!`
//         }else if(media>7){
//             return `Você foi aprovado com média ${media}`
//         }
// }

// const n1 = Number(prompt("Digite uma nota: "))
// const n2 = Number(prompt("Digite uma nota: "))

// console.log(calc_media(n1,n2))
//#endregion

//#region - ########## Atividades Pratica 1 ##########
// Contar o número de vogais contidas em uma string fornecida pelo usuário. Por exemplo, o usuário informa a string “Beterraba”, e a função retorna o número 4 
// (há 4 vogaisnessa palavra).

function conta_letras(palavra){
    let cont_vogais = 0
    let cont_consoantes = 0
    const letras_vogais = "aeiouáàãâeéèêiíìoóòôõuúùû"
    const letras_consoantes = "bcdfghjklmnpqrstvwxyz"
    for (let letra of palavra){
        if (letras_vogais.includes(letra)){
            cont_vogais++
        }else if(letras_consoantes.includes(letra)){
            cont_consoantes++
        }
    }
    return cont_vogais, cont_consoantes
}

const palavra = prompt("Digite uma palavra: ")
console.log(conta_letras(palavra))
//#endregion

//#region - Atividade 2: Implemente uma função que receba um número como parâmetro e informe o quadrado desse número.
function calc_quadrado(num){
    return num**2
    return num*num
}

console.log(calc_quadrado(Number(prompt("DIgite um número: "))))
//#endregion

//#region - Atividade 3: Escreva uma função que encontre a área e o perímetro de um círculo, de acordo com o raio fornecido. (INCOMPLETA)
function calc_area(num){
    pi = 3,14
    area = pi*(num*num)

}

console.log(calc_area(Number(prompt("Digite um número para descobrir a área e perímetro: "))))

//#endregion