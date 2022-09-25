from tkinter import *
from tkinter import ttk
from turtle import width
from func import *

# Cores
preto = '#060606'
branco = '#fcfcfc'
azul = '#38576b'
cinza = '#1f1f1f'
operadores = '#000000'
calc = '#2c2c2c'

# Janela
janela = Tk()# Declarando janela
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=preto)

# Visor
visor = Frame(janela, width=235, height=50, bg = cinza)
visor.grid(row=0, column=0)

# Corpo
corpo = Frame(janela, width=235, height=260)
corpo.grid(row=1, column=0)

# Label
texto = StringVar()
texto.set('0')
label = Label(visor, textvariable=texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cinza, fg=branco)
label.place(x=0,y=0)

# Botões
# Fileira 1
limpa = Button(corpo,command=lambda: limpatela(texto), text='C', width=11, height=2, bg = calc, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
limpa.place(x=0,y=0)

modulo = Button(corpo, command=lambda: mostrar('%', texto), text='%', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
modulo.place(x=118, y=0)

barra = Button(corpo, command=lambda: mostrar('/', texto), text='/', width=5, height=2, bg = operadores, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
barra.place(x=177, y=0)

#Fileira 2

sete = Button(corpo, command=lambda: mostrar('7', texto), text='7', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
sete.place(x=0, y=52)

oito = Button(corpo,command=lambda: mostrar('8', texto), text='8', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
oito.place(x=59, y=52)

nove = Button(corpo, command=lambda: mostrar('9', texto), text='9', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
nove.place(x=118, y=52)

asterisco = Button(corpo, command=lambda: mostrar('*', texto), text='*', width=5, height=2, bg = operadores, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
asterisco.place(x=177, y=52)

#Fileira 3

quatro = Button(corpo, command=lambda: mostrar('4', texto), text='4', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
quatro.place(x=0, y=104)

cinco = Button(corpo, command=lambda: mostrar('5', texto), text='5', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
cinco.place(x=59, y=104)

seis = Button(corpo, command=lambda: mostrar('6', texto) ,text='6', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
seis.place(x=118, y=104)

menos = Button(corpo, command=lambda: mostrar('-', texto), text='-', width=5, height=2, bg = operadores, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
menos.place(x=177, y=104)

#Fileira 4

um = Button(corpo, command=lambda: mostrar('1', texto), text='1', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
um.place(x=0, y=156)

dois = Button(corpo, command=lambda: mostrar('2', texto), text='2', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
dois.place(x=59, y=156)

tres = Button(corpo, command=lambda: mostrar('3', texto), text='3', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
tres.place(x=118, y=156)

mais = Button(corpo, command=lambda: mostrar('+', texto), text='+', width=5, height=2, bg = operadores, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
mais.place(x=177, y=156)

# Fileira 5
zero = Button(corpo, command=lambda: mostrar('0', texto), text='0', width=11, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
zero.place(x=0,y=208)

virgula = Button(corpo, command=lambda: mostrar('.', texto), text=',', width=5, height=2, bg = preto, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
virgula.place(x=118, y=208)

igual = Button(corpo, command=lambda: calcular('=', texto), text='=', width=5, height=2, bg = calc, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
igual.place(x=177, y=208)


# Executando janela
janela.mainloop()

