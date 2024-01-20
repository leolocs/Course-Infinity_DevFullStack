#13.SAUDAÇÃO: Faça um programa que pergunte o nome do usuário e que horas são e mostre na tela um cumprimento. 
#Por exemplo “Bom dia fulano” ou “Boa noite fulano” ou “Boa tarde fulano”.
from datetime import datetime
hora_atual = datetime.now().hour
min_atual = datetime.now().minute
hora_e_min_atual = (f"{hora_atual}:{min_atual}") 

nome = str(input("Qual o seu nome? "))

if 0 <= hora_atual < 12:
    print(f"Olá {nome}, bom dia!, São {hora_e_min_atual}")
elif 12 <= hora_atual < 18:
    print(f"Olá {nome}, boa tarde!, São {hora_e_min_atual}")
else:
    print(f"Olá {nome}, boa noite!, São {hora_e_min_atual}")