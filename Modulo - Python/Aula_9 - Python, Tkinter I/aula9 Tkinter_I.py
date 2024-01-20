from tkinter import *

# Criação da Janela do programa 
box = Tk()
box.title("Aula 1 TK")
box.geometry("600x300")

#Função de saudação
def saudacao():
    nome = user_input.get()
    resultado.configure(text= f"bem vindo {nome}")

##### Inserção dos Widgets ao programa #####
user_label = Label(text="Digite o nome do usuário: ", bg="black", fg="white", font=("Calibri",12,"bold","italic")).pack()

# Widget entrada de texto
user_input = Entry()
user_input.pack()

#Criação do botão de envio
submit = Button(box, text="Enviar", command=saudacao)
submit.pack()

resultado = Label(text="")
resultado.pack()

box.mainloop()

