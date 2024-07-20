// #region - Faça uma função que dê uma saudação de acordo com o horário do dia,
// // a função recebe o nome da pessoa e a hora do dia (sem os minutos) e faz uma saudação apropriada como:
// // Bom dia
// // boa tarde
// // Boa noite

// // Versão 1:
// function saudacao(hora){
//     const nome = prompt("QUal seu nome?: ")
//     const hora = Number(prompt("Que horas são?: "))

//     if(hora < 0 || hora > 23){
//         return "horário inválido!"
//     }else if(hora >= 5 && hora <= 12){
//         return `Bom dia ${nome}`
//     }else if(hora > 13 && hora <= 18){
//         return `Boa tarde ${nome}`
//     }else{
//         return `Boa noite ${nome}`
//     }
    
// }
// document.write(saudacao())

// // Versão 2:
// function saudacao(hora){
//     if(hora < 0 || hora > 23){
//         return "horário inválido!"
//     }else if(hora >= 5 && hora <= 12){
//         return `Bom dia ${nome}`
//     }else if(hora > 13 && hora <= 18){
//         return `Boa tarde ${nome}`
//     }else{
//         return `Boa noite ${nome}`
//     }
    
// }
// const nome = prompt("Qual seu nome?: ")
// const hora = Number(prompt("Que horas são?: "))
// document.write(saudacao(nome,hora))

//#endregion

// #region - Aula 7 - Fazendo a Saudação utilizando o Event Listener 
const caixa_do_nome = document.querySelector("#nome") //input
const botao = document.querySelector("#botao") //processo
const p_do_resultado = document.querySelector("#resultado")

botao.addEventListener("click", ()=>{
    const agora = new Date()
    const hora = agora.getHours()
    const minuto = agora.getMinutes()
    //console.log(`${}`)
    if(hora >=5 && hora <= 12){
        p_do_resultado.textContent = `Bom dia, ${caixa_do_nome.value}`
    }else if(hora > 13 && hora <=18){
        p_do_resultado.textContent = `Boa tarde, ${caixa_do_nome.value}`
    }else{
        p_do_resultado.textContent=`Boa noite, ${caixa_do_nome.value}`
    }
})
// #endregion

// region - FAÇA UM PROGRAMA QUE calcula a média ATRAVES DO HTML USANDO DOIS INPUTS DUAS NOTAS PARA O USUÁRIO E
//CRIE UM BOTÃO QUE AO SER CLICADO VAI ALTERAR O CONTEÚDO DE TEXTO DE UM PARAGRAFO DO SEU HTML MOSTRANDO SE O ALUNO FOI APROVADO OU REPROVADO.
const n1 = document.querySelector("#nota1")
const n2 = document.querySelector("#nota2")
const n3 = document.querySelector("#nota3")
const btn_calculo_media = document.querySelector("#btn_calculo_media")
const resultado_media = document.querySelector("#resultado_media")

btn_calculo_media.addEventListener("click", ()=>{
    // const media = (Number(n1.value) + Number(n2.value) + Number(n3.value)) / 3
    
    if(media <= 7){
        resultado_media.textContent = `Sua média é:${media.toFixed(1)}, você está reprovado!`
    }else if(media > 7){
        resultado_media.textContent = `Sua média é: ${media.toFixed(1)}, você está aprovado!`
    }else if(media === 10)[
        resultado_media,textContent = `Sua media é: ${media.toFixed(1)}, está aprovado com distinção!`
    ]
})

//#endregion
