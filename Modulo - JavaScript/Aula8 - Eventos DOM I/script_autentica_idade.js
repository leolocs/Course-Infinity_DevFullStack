const idade = document.querySelector("#idade")
const botao = document.querySelector("#botao")
const resultado_checar_idade = document.querySelector("#resultado_checar_idade")
    botao.addEventListener("click", () => {
        const novo_elemento = document.createElement("p")
        if(Number(idade.value) >= 18){
            resultado_checar_idade.append(novo_elemento)
            
        }else{
            novo_elemento.textContent = "Não pode entrar"
            novo_elemento.style.color = "red"
        }
        resultado_checar_idade.append(novo_elemento)
    })