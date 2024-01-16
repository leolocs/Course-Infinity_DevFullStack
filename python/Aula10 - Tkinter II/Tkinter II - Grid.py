from tkinter import*

tela = Tk()
tela.title("Aprendendo GRID")
tela.geometry("300x300")

idade_label = Label(text="Digite sua idade: ")
idade_label.grid(row=0, column=0)
idade_input = Entry()
idade_input.grid(row=0,column=1, pady=10)


altura_label = Label(text="Qual sua altura: ")
altura_label.grid(row=1,column=0)
altura_input = Entry()
altura_input.grid(row=1,column=1)

btn = Button(text="Enviar", width=25)
btn.grid(row=2, column=0, columnspan=2, pady=10)


tela.mainloop()