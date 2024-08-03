const formulario = document.querySelector("#formulario")
const email = document.querySelector("#email")
const senha = document.querySelector("#senha")

const letras = "abcdefghijklmnopqrstuvxwyz"
const numeros = "abcdefghijklmnopqrstuvxwyz"
const carac_especial = "!@#$%¨&*()_+{}^/"

caixa.addEventListener("submit", (e)=>{
    e.preventDefault()
    for (let caracter of senha){
        if (letras.includes(caracter)){
            console.log(`Letras inclusas`)
            break
        }else if(numeros.includes(caracter)){
            console.log("Números inclusos")
            break
        }else if(carac_especial.includes(caracter)){
            console.log(`Caracteres inclusos`)
            break
        }
    }
    
})


//Modelo apra fazer atividade
for(let caracter of senha){
    if(letras.includes(caracter)){
        alert("confere letra")
    }
}

