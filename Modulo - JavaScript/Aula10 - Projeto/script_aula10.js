const tarefa_nome = document.querySelector("#tarefa_nome")
const formulario = document.querySelector("#lista_tarefas_form")
const resultado = document.querySelector("#resultado")

formulario.addEventListener("submit", (evento)=>{
    evento.preventDefault()

    // Criando a div da tarefa que será inserida
    const tarefa_div = document.createElement("div")
    tarefa_div.className = "nova_tarefa"

    // Criando a checbox e inserido a função
    const checkbox = document.createElement("input")
    checkbox.type = "checkbox"
    checkbox.addEventListener("click", (evento)=>{
        texto.className = "tarefa_marcada"
        console.log(evento.target.checked)
        if(!evento.target.checked){
            texto.className = ""
        }
    })

    const texto = document.createElement("p")
    texto.textContent = tarefa_nome.value

    const btn_excluir = document.createElement("button")
    btn_excluir.textContent = "Excluir"
    btn_excluir.addEventListener("click", ()=>{
        resultado.removeChild(tarefa_div)
    })

    tarefa_div.append(checkbox,texto,btn_excluir)
    resultado.append(tarefa_div)
    texto.value = ""
    texto.focus()
})