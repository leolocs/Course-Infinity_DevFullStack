// OPERADORES LÓGICOS
console.log(5==8)
console.log(5==8)
console.log(5=="5") // ESTÁ ERRADO!!
// UTILIZA-SE 3 === IGUAIS PARA SE COMPARAR TANTO O VALOR QUANTO O TIPO
console.log(5==="5")

console.log(5 != 8)
console.log(5 != 5)
console.log(5 != "5")
console.log(5 !== "5")

// AS OPERAÇÕES ABAIXO SÓ FUNCIONAM COM NÚMEROS, OPERAÇÕES MATEMÁTICAS
console.log(5>8)
console.log(5<8)
console.log(5<=8)
console.log(5>=8)

// CONDICIONAL COMPARATIVO "E" (&&)
alert(idade>= 18 && idade <= 70)

//CONDICIONAL COMPARATIVOU "OU" (||)
alert((idade>= 16 && idade <18) || idade >= 71)

//CONDICIONAL CONJUNTO
const vogais = "aeiou"
alert(vogais.includes("a"))
alert(vogais.includes("b"))
alert(!vogais.includes("b"))