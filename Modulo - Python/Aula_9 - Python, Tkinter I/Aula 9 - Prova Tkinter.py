# Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unid_medida de medida de centímetros para metros.
from tkinter import ttk
from tkinter import *

#Criação da janela
tela = Tk()
tela.title("Prova Tkinter, Conversor de unidades ")
tela.geometry("600x300")

def converter():
    valor = float(valor_input.get())
    result = valor/1000
    resultado.config(text=f"{valor}cm convertido para metros são: {result}m")

def limpar():
    valor_input.config(text=f"")

valor_label = Label(text="Digite o valor em centimetros que deseja converter:")
valor_label.grid(row=0,column=0)
valor_input = Entry()
valor_input.grid(row=0,column=1)

#criando combobox

resultado = Label(text="")
resultado.grid(row=1,column=1,pady=5)

btn_converter = Button(tela, text="Converter",width=10, command=converter)
btn_converter.grid(row=1, column=0, pady=2)

btn_limpar = Button(tela, text="Limpar", width=10, command=limpar)
btn_limpar.grid(row=2, column=0, pady=2)


tela.mainloop()
