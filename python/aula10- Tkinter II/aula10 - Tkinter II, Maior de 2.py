#Faça uma aplicação que pede apara o usuário digitar 2 números, com um botão que ao clicado, mostre na tela qual dos 2 números é o maior.
from tkinter import *


janela = Tk()
janela.title("Maior de 2")
janela.geometry("600x600")

def ver_maior_num():
    num1 = float(n1_input.get())
    num2 = float(n2_input.get())
    if num1 > num2:  
        resultado.configure(text=f"O {num1} é o maior número")
    elif num2 > num1:
        resultado.configure(text=f"O {num2} é o maior número")
    else:
        resultado.configure(text=f"Os números são iguais!", font=("Montserrat",12))
lista_num = []

n1_label = Label(text="Digite o primeiro número:", font= ("Montserrat", 11)).pack()
n1_input = Entry()
n1_input.pack()

n2_label = Label(text="Digite o segundo número:", font= ("Montserrat",11)).pack()
n2_input = Entry()
n2_input.pack()

enviar = Button(janela, text="Enviar", command= ver_maior_num)
enviar.pack()

resultado = Label(text="")
resultado.pack()

janela.mainloop()