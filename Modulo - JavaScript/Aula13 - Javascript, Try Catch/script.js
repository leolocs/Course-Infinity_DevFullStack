// localStorage.setItem("marca", "Fiat")
// localStorage.setItem("Modelo", "uno")
// localStorage.setItem("Cor", "preto")
// localStorage.setItem("Ano", "2004")
// localStorage.setItem("Ar_condicionado", false)

// ############### Forma de enviar um objeto para o banco de dados local ###############
// const carro = {
//     marca: "Fiat",
//     modelo: "Uno",
//     ano: 2004,
//     ar_condicionado: false
// }

// localStorage.setItem("meu_carro", JSON.stringify(carro))         //"Jogando" o objeto carro ao banco local transformado em String
// const buscar = JSON.parse(localStorage.getItem("meu_carro"))     // "Pegando" o objeto meu_carro no banco local transformando em Objeto

// console.log(meu_carro)

const container = document.querySelector("#container")
const formulario = document.querySelector("#formulario")
const nome_form = document.querySelector("#nome_form")
const data_nasc_form = document.querySelector("#data_nasc_form")
const cpf_form = document.querySelector("#cpf_form")
const tel_form = document.querySelector("#tel_form")
const email_form = document.querySelector("#email_form")
const pessoas = JSON.parse(localStorage.getItem("lista_pessoas") || [])

  function criarItem(){
    container.innerHTML= ""
    pessoas.forEach((element)=>{
        const card_pessoa = document.createElement("div")
        card_pessoa.className = "card_pessoa"
    
        const nome = document.createElement("h2")
        nome.textContent = `Nome: ${element.nome}`
        
        const data_nasc = document.createElement("p")
        data_nasc.textContent = `Data de Nascimento: ${element.data_nasc}`
    
        const cpf = document.createElement("p")
        cpf.textContent = `CPF: ${element.cpf}`
    
        const telefone = document.createElement("p")
        telefone.textContent = `Telefone: ${element.telefone}`
    
        const email = document.createElement("p")
        email.textContent = `Email: ${element.email}`
    
        card_pessoa.append(nome,data_nasc,cpf,telefone,email)
        container.appendChild(card_pessoa)
      })

  }

  criarItem() // A função criada é chamada para assim que a pagina carregar

  formulario.addEventListener("submit", evento =>{
    evento.preventDefault()
    const novo_objeto = {
        nome_form: nome_form.value,
        data_nasc_form: data_nasc_form.value,
        cpf_form: cpf_form.value,
        tel_form: tel_form.value,
        email_form: email_form.value
    }
    pessoas.push(novo_objeto)
    localStorage.setItem("lista_pessoas", JSON.stringify) // Subindo o novo objeto para o BD local em forma de String
    formulario.reset()
    nome.focus()
    criarItem() // A função é chamada para o item assim que uma pessoa é cadastrada na página

  })