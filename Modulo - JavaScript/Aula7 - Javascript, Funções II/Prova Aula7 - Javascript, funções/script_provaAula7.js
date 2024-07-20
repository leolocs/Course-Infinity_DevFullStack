// Imagine que você está criando uma solução digital para restaurantes, incluindo uma calculadora de gorjetas de fácil uso.
// O objetivo é desenvolver uma página da web onde os clientes possam inserir o valor total da conta e escolher a qualidade do serviço:
// "Bom", "Regular" ou "Ruim".
// Para isso, serão utilizadas arrow functions e funções de callback.


function avaliacao_servico(nota){
    if (nota === 1){
        return `Você avaliou o serviço como Bom, obrigado pela avaliação`
    }
    if(nota === 2){
        return `Você avaliou o serviço como Regular`
    }
    if(nota === 3){
        return `Você avaliou o serviço como Ruim`
    }
}

const valor_total = Number(prompt("Digite o valor total da conta: "))
const nota = Number(prompt("Qual a sua nota para a qualidade de  serviço do estabelecimento?: (1 - Bom | 2 - Regular | 3 - Ruim) (Digite apenas um número respectivo!)"))

alert(avaliacao_servico(nota))