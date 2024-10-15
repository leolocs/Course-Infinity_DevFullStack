// Você trabalha em um banco e foi solicitado a desenvolver uma parte da interface de um caixa eletrônico para o site do banco.
// Crie um código HTML e JavaScript que simule a tela de operações do caixa eletrônico.

// Na tela, deve haver um título 'Simulador de Caixa Eletrônico', um menu suspenso com opções para 'Consultar Saldo', 'Sacar' e 'Depositar',
// um campo de entrada onde o cliente possa inserir o valor da transação e um botão 'Realizar'.
// O resultado da operação deve ser exibido em um parágrafo.

// Use JavaScript para implementar as ações selecionadas.
// Defina um saldo inicial fictício de R$ 1000. Certifique-se de que o código trate erros, como valores inválidos e saldos insuficientes.

let saldo_inicial = 1000;
const consultar = document.querySelector("#consultar");
const sacar = document.querySelector("#sacar");
const depositar = document.querySelector("#depositar");
const saldo = document.querySelector("#saldo");
const mensagem = document.querySelector("#mensagem")
const valorInput = document.querySelector("#valorInput")


consultar.addEventListener("click", (evento)=>{
    evento.preventDefault();
    saldo.textContent = `R$ ${saldo_inicial.toFixed(2)}`;
})


depositar.addEventListener("click", (evento)=>{
    evento.preventDefault();
    mensagem.textContent = `Digite o valor que deseja depositar:`;
    valorInput.style.display = 'block';
    valorInput.value = "";
    valorInput.focus();
    try{
        const saldo = parseFloat(valorInput.value);
        if(isNaN(saldo) || saldo <=0){
            throw new Error("Insira um valor válido para depósito.");
        }else{
            saldo += valor;
            mensagem.textContent = `Depósito no valor de R$ ${valor.toFixed(2)} realizado com sucesso`
            valorInput.value = "";
        }
        
    }
    catch{
        
    }
})


