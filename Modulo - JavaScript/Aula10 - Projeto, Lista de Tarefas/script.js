const tarefa_nome = document.querySelector("#tarefa_nome")
const formulario = document.querySelector("#lista_tarefas_form")
const resultado = document.querySelector("#resultado")

formulario.addEventListener("submit", (evento)=>{
    evento.preventDefault();

    // Criando a div da tarefa que será inserida
    const elemento = document.createElement("div");
    elemento.className = "tarefa"

    // Criando a checbox e inserido a função
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("click", (evento)=>{
        // console.log(evento.target.checked)
        if(evento.target.checked){
            // texto.style.textDecoration = "line-through";
            elemento.className = "tarefa_concluida"
            // elemento.style.background-color = "rgb(16, 161, 113)"
        }else{
            // texto.style.textDecoration = "none"
            elemento.className = "tarefa"
        }
    });

    const texto = document.createElement("p");
    texto.textContent = tarefa_nome.value;

    const btn_excluir = document.createElement("button")
    btn_excluir.textContent = "Excluir"
    btn_excluir.addEventListener("click", ()=>{
        resultado.removeChild(elemento)
    });

    elemento.append(checkbox,texto,btn_excluir);
    resultado.append(elemento);
    elemento.value = "";
    texto.focus();
})