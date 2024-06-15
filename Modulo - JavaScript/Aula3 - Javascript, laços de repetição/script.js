const n1 = Number(prompt("Digite um primeiro número: "))
const n2 = Number(prompt("Digite um segundo número: "))
const n3 = Number(prompt("Digite um terceiro número: "))

if (n1>n2 && n1>n3){
    alert(`O  ${n1} é o maior número!`)
}else if (n2>n1 && n2>n3){
    alert(`O número ${n2} é o maior número!`)
}else if (n3>n1 && n3>n2){
    alert(`O número ${n3} é o maior número!`)
}else{
    alert(`Os números são iguais!`)
}