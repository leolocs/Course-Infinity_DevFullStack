# Faça uma aplicação que pede ao usuário digitar quanto ele ganha pôr mês e quantas horas ele trabalha por mês;
# Calcule quanto ele ganha por hora e mostre na tela o valor da hora;
# Personalize as cores do resultado de acordo com o valor da hora da forma abaixo:
# R$0 - R$10 = Vermelho
# R$11 - R$25 = laranja
# R$26 - R$50 = Azul
# R$51+ = Rosa
from tkinter import *

tela = Tk()
tela.title("Calcula salário")
tela.geometry("600x600")

def calcular_salario():
    nome = str(nome_input.get())
    salario = float(salario_input.get())
    hrs_trabalho = int(horas_input.get())
    valor_hora = salario/hrs_trabalho
    cor = "white"

    if valor_hora > 0 and valor_hora <= 10:
        cor = "#FF4747" #vermelho
    elif valor_hora > 11 and valor_hora <= 25:
        cor = "#FF8D0A" #laranja
    elif valor_hora >= 26 and valor_hora <= 50:
        cor = "#3BC14A" # verde 
    elif valor_hora > 50:
        cor = "#7A3CB9" #roxo-grape
        
    resultado.configure(text=f"{nome} o valor da sua hora de trabalho é: {valor_hora}", fg=cor, font=("Montserrat", 10,"bold"))

nome_label = Label(text="Qual seu nome?").pack()
nome_input = Entry()
nome_input.pack()

salario_label = Label(text="Qual valor do seu salário mensal?").pack()
salario_input = Entry()
salario_input.pack()

horas_label = Label(text="Quantas horas você trabalha por mês?").pack()
horas_input = Entry()
horas_input.pack()

resultado = Label(text="")
resultado.pack()

Btn_enviar = Button(tela, text="Calcular", command=calcular_salario)
Btn_enviar.pack()

tela.mainloop()


