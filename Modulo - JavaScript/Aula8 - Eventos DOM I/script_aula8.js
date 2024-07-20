// #region - Aula 8 Parte 1

// const botao = document.querySelector("#botao")

// console.log(botao)
// console.log(botao.textContent)
// console.log(botao.id)

// botao.addEventListener("click", cliqueBotao(){
//     alert("Botão clicado")
// })


// const todos_os_h1 = document.getElementsByTagName("h1")
// const todos_os_li = document.getElementsByTagName("li")
// const meu_texto = document.getElementById("texto")
// const meus_itens = document.getElementsByClassName("item")
// const caixinha_nome = document.getElementsByName("nome")

// console.log(todos_os_h1)
// console.log(todos_os_li)
// console.log(meu_texto)
// console.log(meus_itens)
// console.log(caixinha_nome)


// const titulo_principal = document.querySelector("h1")
// const todos_os_li = document.querySelectorAll("li")
// const meu_texto = document.querySelector("#texto")
// const meus_itens = document.querySelectorAll(".item")
// const caixinha_nome = document.querySelector("[name='nome']")

// console.log(titulo_principal)
// console.log(todos_os_li)
// console.log(meu_texto)
// console.log(meus_itens)
// console.log(caixinha_nome)

//#endregion

// #region - Aula 8 - parte 2
// const texto = document.querySelector("#texto")
// const caixa_texto = document.querySelector("#caixa_texto")
// const minha_div = document.querySelector("#minha_div")

// console.log(texto)
// console.log(texto.textContent)
// console.log(texto.id)

// console.log(caixa_texto)
// console.log(caixa_texto.value)

// console.log(minha_div.textContent)
// console.log(minha_div.innerText)
// console.log(minha_div.innerHTML)
// #endregion

// #region - Atividades
    // Busque todos os itens que possuem um ID ou uma class no seu JS e guarde em uma variável altere o conteúdo de texto do titulo para "tudo sobre programação"
    // altere a imagem por outra imagem qualquer a sua escolha. Exiba no console todo o conteúdo de texto HTML da lista;
    // Exiba na tela todo conteudo de texto do ID:
    // nome do ID da TAG p

    // const titulo = document.querySelector("#titulo")
    // const img = document.querySelector("#img")
    // const lista = document.querySelector("#lista")
    // const itens = document.querySelectorAll(".item")
    // const nome = document.querySelector("#nome")

    // titulo.textContent = 'Tudo sobre programação'
    // img.src="https://www.gfinfo.com.br/wp-content/uploads/2023/06/principais-linguagens-de-programacao.png"
    // console.log(lista.innerText)
    // console.log(lista.innerHTML)

    // ########## Atividade 2 ##########

    const fruta = document.querySelector("#fruta")
    const cadastrar_fruta = document.querySelector("#btn_cadastrar_fruta")
    const resultado_cadastro_fruta = document.querySelector("#resultado_cadastro_fruta")

    botao.addEventListener("click", () => {
        const novo_elemento = document.createElement("p")
        novo_elemento.innerHTML = `Você cadastrou a fruta <b>${fruta.value}<b>`

        resultado_cadastro_fruta.append(novo_elemento)
        fruta.value = ""
        fruta.focus()
    })

    

//#endregion