// ########## Enunciado ##########
// Você foi convidado(a) a desenvolver um aplicativo web para ajudar a gerenciar as tarefas domésticas de uma família agitada.
// O objetivo é criar um "Gerenciador de Tarefas Domésticas" que permita que todos os membros da família adicionem,
// removam e atualizem suas tarefas diárias, garantindo que tudo seja feito de forma organizada.

const nome_tarefa = document.querySelector("#nome_tarefa")
const formulario = document.querySelector("#formulario")
const resultado = document.querySelector("#resultado")

formulario.addEventListener("submit", (evento)=>{
    evento.preventDefault();

    const elemento = document.createElement("div");
    elemento.className = "tarefa"

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("click", (evento)=>{
        
        if (evento.target.checked){
            elemento.className = "tarefa_concluida"
        }else{
            elemento.className = "tarefa"
        }

    });

    const texto = document.createElement("p")
    texto.textContent = nome_tarefa.value;

    const btn_excluir = document.createElement("button")
    btn_excluir.textContent = "Excluir"
    btn_excluir.addEventListener("click", ()=>{
        resultado.removeChild(elemento)
    });

    const btn_alterar = document.createElement("button");
    btn_alterar.textContent = "Alterar";
    btn_alterar.addEventListener("click", () => {
        const new_input = document.createElement("input");
        new_input.type = "text";
        new_input.value = texto.textContent;
        
        const btn_salvar = document.createElement("button");
        btn_salvar.textContent = "Salvar";

        elemento.replaceChild(new_input, texto); // Substitui o parágrafo pelo campo de texto
        elemento.replaceChild(btn_salvar, btn_alterar); // Substitui o botão "Alterar" pelo "Salvar"

        btn_salvar.addEventListener("click", () => {
            texto.textContent = new_input.value; // Atualiza o texto com o valor do campo de texto
            elemento.replaceChild(texto, new_input); // Volta para o modo de visualização
            elemento.replaceChild(btn_alterar, btn_salvar); // Volta o botão "Alterar"
        });
    });

    elemento.append(checkbox, texto, btn_alterar, btn_excluir);
    resultado.append(elemento);
    elemento.value = "";
    texto.focus();
})