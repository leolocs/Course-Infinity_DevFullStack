#Faça uma aplicação que simule um semáforo aonde a aplicação deve ter 3 botões com 3 cores: Vermelho, Amarelo, verde;
#Para cada botão clicado a aplicação deve exibir a respectiva frase:
# Vermelho: "Pare!"
# Amarelo: "Atenção!"
# Verde: "Siga!"
from tkinter import *
from tkinter import ttk

# Única função para os 3 botões:
#def ver_cor(cor):
#     color = "white"
#     if cor "vermelho":
#         color = "Pare!"
#    resultado.configure(text="") 

#Pegando o texto do botão:
# def btn_amarelo = btn_amarelo.cget("text")
# btn_verde = btn_verde.cget("text")

def vermelho():
    resultado.configure(text="Pare!")
    
def amarelo():
    resultado.configure(text="Atenção!")

def verde():
    resultado.configure(text="Siga!")


tela = Tk()
tela.title("Semáforo")
tela.geometry("250x300")

btn_vermelho = Button(tela, text="Vermelho", width=20, height=4, bg="#FF4747", fg="black", font=("Calibri", 11, "bold"), command=vermelho)
btn_vermelho.pack()
div = ttk.Separator(tela, orient=HORIZONTAL)
div.pack(padx=50, ipadx=50)

btn_amarelo = Button(tela, text="Amarelo", width=20, height=4, bg="Yellow", fg="black", font=("Calibri", 11, "bold"), command=amarelo)
btn_amarelo.pack()

btn_verde = Button(tela, text="Verde", width=20, height=4, bg="Green", fg="black", font=("Calibri", 11, "bold"), command=verde)
btn_verde.pack()

resultado = Label(text="")
resultado.pack()

tela.mainloop()