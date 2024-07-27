// Você é um desenvolvedor de software que trabalha em uma equipe especializada em criar ferramentas matemáticas para uma empresa do mercado financeiro.
// A empresa precisa de uma nova funcionalidade para sua plataforma online, permitindo que os usuários obtenham informações sobre cálculos matemáticos importantes
// relacionados aos investimentos.

// Sua tarefa é criar um módulo JavaScript que ofereça aos usuários a possibilidade de inserir um número inteiro positivo e, em resposta,
// calcular o fatorial desse número e também a sequência de Fibonacci até aquele número.
// Isso ajudará os investidores a realizar análises mais detalhadas sobre suas decisões financeiras.

let num_fat = 0
let termo1 = 0
let termo2 = 1
let termo_fib = 0

let num_dig = Number(prompt("Digite um número inteiro positivo para o calculo: "))
num_fat = num_dig**2
document.write(`Sequencia Fibonnaci: `)
if (num_dig<=2){
    termo_fib = num_dig-1
}else{
    count = 3;
    while(count <= num_dig){
        document.write(`${termo_fib} `)
        termo_fib = termo1+termo2;
        termo1 = termo2;
        termo2 = termo_fib;
        count++;
        // for(let num of num_dig){
        //     document.write(`${termo1} ${prox_termo}`)
        //     prox_termo = termo1 + termo2
        //     termo1, termo2 = termo2, prox_termo
        // }
        
    }
    
}
    
    document.write(`<br><br> Número fatorial: ${num_fat}`)