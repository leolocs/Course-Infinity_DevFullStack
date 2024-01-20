#14. REAJUSTE: Faça um programa que pede para o usuário digitar seu salário e calcule o reajuste dele baseado em quando ele ganha: 
# abaixo de 5.000 reajuste de 15%,  entre 5.000 e 10.000 reajuste de 10% acima de 10.000 reajuste de 5%

sal = int(input("Qual o seu sálário? "))
sal_reaj = 0

if sal <= 0:
    print("Por favor digite um salário válido!")
else:
    if sal < 5000:
        sal_reaj = sal + (sal*0.15)
    elif 5000 < sal < 10000:
        sal_reaj = sal + (sal*0.10)
    elif 10.000 > sal:
        sal_reaj = sal + (sal*0.5)
print(f"Seu salário reajustado é: {sal_reaj}")