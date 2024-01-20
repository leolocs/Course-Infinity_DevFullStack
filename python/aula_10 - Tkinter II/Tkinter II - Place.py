from tkinter import*

tela = Tk()
tela.title("Aprendendo Place")
tela.geometry("300x300")

idade_label = Label(text="Digite sua idade: ")
idade_label.place(x=5, y=5)
idade_input = Entry()
idade_input.place(x=100, y=5)

altura_label = Label(text="Qual a sua altura: ")
altura_label.place(x=5, y=30)
altura_input = Entry()
altura_input.place(x=105, y=30)

tela.mainloop()