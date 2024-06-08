// ########## VARIÁVEIS ##########
// UMA VARIÁVEL STRING ESTÁ SEMPRE DENTRO DE ASPAS PARA INDICAR QUE É UM CARACTERE OU PALAVRA
String
"Abel"
"j"
"@#$%"

// NUMBER É QUAQUER NÚMERO ESCRITO
12
-10
1.6
1997
-72.5

// Variável: Boolean: verdadeiro ou falso
true
false

undefined
null

//Criando variáveis
var nome = "Leonardo" //String
var idade = 26 //number
var altura = 1.76 //number
var habilitado = true //Boolean
var hobby = "Jogar" // String

var nomedamae // undefined
var escola_ = "Infinity_school"

//Formas de se criar uma variável
var pessoa1 = "joão" //não se deve ser utilizada atualmente pois caiu em dezuso 

let pessoa2 = "Maria" //Variável let é uma variável local, só pode ser chamada no local onde foi criada

const pessoa3 = "Pedro" //Váriavel tambem local, porém constante, não muda

// Maneiras de entrada e saida de dados (print)
const nome = prompt("Digite aqui seu nome: ")
let number = prompt("Digite um numero: ")
let num1 = Number(prompt("Digite um número: ")) // Solicita obrigatoriamente um número ao usuário
console.log(nome)
alert(nome)
document.write(nome)

// Para fazer a concatenação sem precisar utilizar a ",":

console.log(`Olá $(nome), vem vindo, seu cadastro foi um sucesso sua idade: $(idade) seu CPF: $(cpf)`)

