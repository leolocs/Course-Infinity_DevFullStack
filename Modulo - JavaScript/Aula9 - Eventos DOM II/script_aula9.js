const botao = document.querySelector("#botao")
const caixa = document.querySelector("#caixa")

// #################### EVENTOS DE MOUSE ####################
//Evento ao clicar uma vez no botão
botao.addEventListener("Clik", ()=>{
    console.log("Clicou no botao")
})

//Evento ao dar 2 cliques seguidos
botao.addEventListener("dblClik", ()=>{
    console.log("Clique duplo no botao")
})

//Evento ao passar o mouse
botao.addEventListener("Mouseover", ()=>{
    console.log("Clicou no botao")
})

//Evento ao tirar o Mouse de cima do botão
botao.addEventListener("Mouseout", ()=>{
    console.log("Tirou o mouse de cima do botão")
})

botao.addEventListener("Mouseout", ()=>{
    console.log("Tirou o mouse de cima do botão")
})

// #################### EVENTOS DE TECLADO ####################
caixa.addEventListener("keydown", ()=>{
    console.log("Apertou a tecla")
})

// Evento ao apertar alguma tecla
caixa.addEventListener("keydown", (e)=>{
    console.log(e.key)
    console.log(`A tecla ${(e.key)} foi pressionada!`)
})

// Evento ao soltar a tecla
caixa.addEventListener("keyup", (e)=>{
    console.log(e.key)
})

//Evento ao apertar alguma tecla, porém teclas de letras do alfabeto e números
caixa.addEventListener("keypress", (e)=>{
    console.log(e.key)
})

// Evento input permite pegar cada letra digitada dentro do campo input de texto
caixa.addEventListener("input", (e)=>{
    console.log(e.target.value)
})

// Evento que é ativo quando é trocado de campo
caixa.addEventListener("change", (e)=>{
    console.log(e.target.value)
})