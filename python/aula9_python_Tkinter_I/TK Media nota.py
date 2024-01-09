from tkinter import *
#Faça uma aplicação TK que pede duas notas ao usuário e mostra na tela a soma dessas duas notas
# Customize a aplicação: 
# "Você foi aprovado" COM O FUNDO VERDE E A FONTE BRANCA, SE A MÉDIA FOR MAIOR OU IGUAL A 7
# "Você foi reprovado" COM A COR DE FUNDO VERMELHO E A FONTE BRANCA, SE A MÉDIA FOR MENOR DO QUE 7
# "Aprovado com distinção" COM A FOR DE FUNDO AZUL E A FONTE BRANCA, SE A MÉDIA FOR IGUAL A 10
# CUSTOMIZE SEU PROGRAMA A VONTADE.

box = Tk()
box.title("Media notas")
box.geometry("600x300")

def calc_media():
    nome = nome_input.get()
    nota1 = float(n1_input.get())
    nota2 = float(n2_input.get())
    nota3 = float(n3_input.get())
    soma = nota1+nota2+nota3
    media = soma/3
    
    if media >= 7 and media < 10:
        result.configure(text=f"Parabéns {nome}, Você foi aprovado! Media: {media:.1f}", bg="green", fg="white", font=("Calibri", 12, "bold"))
    elif media < 7:
        result.configure(text=f"Parabéns {nome}, Você foi reprovado! Sua Media: {media:.1f}", bg="red", fg="white", font=("Calibri", 12, "bold"))
    elif media == 10:
        result.configure(text=f"Parabéns {nome}, Você foi aprovado com distinção! Media: {media:.1f}", bg="#00ABE7", fg="white", font=("Calibri", 12, "bold"))
    else:
        result.configure(text=f"Média {media:.1f} é inválida, digite", bg="grey", fg="white", font=("Calibri", 12, "bold"))

    #result.configure(text=f""" A soma das notas do Aluno {nome} é: {soma} e a media das notas é: {media}""")


nome_label = Label(text= "Qual nome do aluno?", font=("Montserrat", 11)).pack()
nome_input = Entry()
nome_input.pack()

n1_label = Label(text= "Digite a primeira nota:", font=("Calibri", 11)).pack()
n1_input = Entry()
n1_input.pack()

n2_label = Label(text="Digite a segunda nota:", font=("Calibri", 11)).pack()
n2_input = Entry()
n2_input.pack()

n3_label = Label(text="Digite a segunda nota:", font=("Calibri", 11)).pack()
n3_input = Entry()
n3_input.pack()

submit = Button(box, text="Enviar", command= calc_media)
submit.pack()

result = Label(text="")
result.pack()

box.mainloop()


