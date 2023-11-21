#3.Crie um programa que solicite o salário e horas de trabalho de um funcionário e crie uma função que calcule o valor da hora e retorne esses valores.


def cal_salario(salario,hrs_trab)
    valor_hora =  salario / hrs_trab
    return valor_hora

salario = float(input("Qual o seu salário? "))
hrs_trab = int(input("Quantas horas trabalhadas? "))

print(f"Você ganha {cal_salario(salario,hrs_trab):.2f} por hora")