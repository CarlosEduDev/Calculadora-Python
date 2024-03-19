from tkinter import *
from tkinter import ttk

# Colors
colorBlack = "#2a2b2a" # preto
colorWhite = "#f7f7f7" # branco
colorBlue = "#3a5e66" # azul
colorGrey = "#787777" # cinza
colorGreen = "#48dbb9" # verdinho
colorYellow = "#f5b41d"


# CONFIGURAÇÕES BÁSICAS
janela = Tk()
janela.title("Calculadora")
janela.geometry("280x310")
janela.config(bg= colorBlack)

# CRIAÇÃO DE FRAMES
frame_tela = Frame(janela, width= 352, height= 50, bg= colorBlue)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width= 352, height= 415)
frame_body.grid(row=1, column=0)

# variável global
todos_valores = ''

# Criação da função

# função que dá entrada para os calculos
def entrada_valores(event):
 global todos_valores

 todos_valores = todos_valores + str(event)
 

 #passando valor para a tela
 valor_texto.set(todos_valores)

 
# função que calcula os valores da entrada
def calcular():
 global todos_valores
 resultado = eval(todos_valores)
 valor_texto.set(str(resultado))

# função que limpa a tela
def limpar_tela():
 global todos_valores
 todos_valores = ''
 valor_texto.set("")


# CRIAÇÃO DE LABEL
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable= valor_texto, width=16 , height= 2, padx= 7, relief= FLAT, anchor="e", justify=RIGHT, font=('Ivy 22') , bg=colorBlue, fg=colorWhite)
app_label.place(x= 0, y= 0)

# CRIAÇÃO DE BOTÕES
button_C = Button(frame_body, command= limpar_tela, text= "C", width= 13, height=2, bg=colorWhite, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_C.place(x= 0 , y= 0)

button_2 = Button(frame_body, command= lambda: entrada_valores('%'), text= "%", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_2.place(x= 140 , y= 0)

button_div = Button(frame_body, command= lambda: entrada_valores('/'), text= "/", width= 6, height=2, bg=colorYellow, fg=colorWhite, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_div.place(x= 210 , y= 0,)

button_num7 = Button(frame_body, command= lambda: entrada_valores('7'), text= "7", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num7.place(x= 0 , y= 52)

button_num8 = Button(frame_body, command= lambda: entrada_valores('8'), text= "8", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num8.place(x= 70 , y= 52)

button_num9 = Button(frame_body, command= lambda: entrada_valores('9'), text= "9", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num9.place(x= 140 , y= 52)

button_mult = Button(frame_body, command= lambda: entrada_valores('*'), text= "x", width= 6, height=2, bg= colorYellow, font=('Ivy 13 bold'), fg=colorWhite , relief= RAISED, overrelief= RIDGE)
button_mult.place(x= 210 , y= 52)


button_num4 = Button(frame_body, command= lambda: entrada_valores('4'), text= "4", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num4.place(x= 0 , y= 104)

button_num5 = Button(frame_body, command= lambda: entrada_valores('5'), text= "5", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num5.place(x= 70 , y= 104)

button_num6 = Button(frame_body, command= lambda: entrada_valores('6'), text= "6", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num6.place(x= 140 , y= 104)

button_sub = Button(frame_body, command= lambda: entrada_valores('-'), text= "-", width= 6, height=2, bg= colorYellow, font=('Ivy 13 bold'), fg=colorWhite , relief= RAISED, overrelief= RIDGE)
button_sub.place(x= 210 , y= 104)

button_num1 = Button(frame_body, command= lambda: entrada_valores('1'), text= "1", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num1.place(x= 0 , y= 156)

button_num2 = Button(frame_body, command= lambda: entrada_valores('2'), text= "2", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num2.place(x= 70 , y= 156)

button_num3 = Button(frame_body, command= lambda: entrada_valores('3'), text= "3", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num3.place(x= 140 , y= 156)

button_adc = Button(frame_body, command= lambda: entrada_valores('+'), text= "+", width= 6, height=2, bg= colorYellow, font=('Ivy 13 bold'), fg= colorWhite , relief= RAISED, overrelief= RIDGE)
button_adc.place(x= 210 , y= 156)

button_num0 = Button(frame_body, command= lambda: entrada_valores('0'), text= "0", width= 13, height=2, bg=colorWhite, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_num0.place(x= 0 , y= 208)

button_dot = Button(frame_body, command= lambda: entrada_valores('.'), text= ".", width= 6, height=2, bg= colorGrey, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_dot.place(x= 140 , y= 208)

button_equal = Button(frame_body, command= calcular, text= "=", width= 6, height=2, bg=colorYellow, fg=colorWhite, font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE)
button_equal.place(x= 210 , y= 208)


janela.mainloop()