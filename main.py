from tkinter import font
from tkinter import *
from tkinter import ttk

# cores (aleatórias) #
color1 = "#94fc03"
color2 = "#0373fc"
color3 = "#be03fc"
color4 = "#121111"

fundo = "#1435db"

window = Tk()
window.title('')
window.geometry('235x318')
window.configure(bg=color1)

# trabalhando nos frames e divisões #
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_screen = Frame(window, width=300, height=56, bg=fundo, pady=0, padx=0, relief="flat")
frame_screen.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(window, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat")
frame_quadros.grid(row=2, column=0, sticky=NW)

# Nome a ser dado
app_tela = Label(frame_screen, text='123456789', width=16, height=2, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=color1)
app_tela.place(x=0, y=0)

# Armazenar os valores
all_values = ""
text_value = StringVar()

def insert_value(event):
    global all_values

    all_values = all_values + str(event)
    text_value.set(all_values)

# Função para realizar o cálculo
def calcular():
    global all_values
    result = str(eval(all_values))
    text_value.set(result)
    all_values = ""

# Função para limpar a tela
def limpar_tela():
    global all_values
    all_values = ""
    text_value.set("")

    b_limpar = Button(frame_quadros, command=limpar_tela, text="Limpar", width=11, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_limpar.place(x=0, y=260)


# Botões
b_1 = Button(frame_quadros, command=lambda: insert_value('%'), text="C", width=11, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros, command=lambda: insert_value('%'), text="%", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_quadros, command=lambda: insert_value('/'), text="/", width=5, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros, command=lambda: insert_value('7'), text="7", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_quadros, command=lambda: insert_value('8'), text="8", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_quadros, command=lambda: insert_value('9'), text="9", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_quadros, command=lambda: insert_value('*'), text="*", width=5, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_quadros, command=lambda: insert_value('4'), text="4", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_quadros, command=lambda: insert_value('5'), text="5", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_quadros, command=lambda: insert_value('6'), text="6", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_quadros, command=lambda: insert_value('-'), text="-", width=5, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_quadros, command=lambda: insert_value('1'), text="1", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_quadros, command=lambda: insert_value('2'), text="2", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_quadros, command=lambda: insert_value('3'), text="3", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_quadros, command=lambda: insert_value('+'), text="+", width=5, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_quadros, command=lambda: insert_value('0'), text="0", width=11, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_quadros, command=lambda: insert_value('.'), text=".", width=5, height=2, bg=color3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_quadros, command=calcular, text="=", width=5, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

b_19 = Button(frame_quadros, command=limpar_tela, text="AC", width=11, height=2, bg=color4, fg=color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=0, y=260)

entry = Entry(frame_screen, font=('Ivy 25 '), relief=SUNKEN, textvariable=text_value, width=12, bd=0, justify=RIGHT, bg=fundo, fg=color2, insertbackground=color2, insertwidth=4)
entry.place(x=1, y=0)

window.mainloop()
