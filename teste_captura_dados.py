from datetime import datetime
import time
import visa
import minimalmodbus
from tkinter import *

nome="a"
ti=0
tf=0

def printf (text):
    print(text,end="")

def to_int(in_str):
    """Converts a string to an integer"""
    out_num = 0
    if in_str[0] == "-":
        multiplier = -1
        in_str = in_str[1:]
    else:
        multiplier = 1
    for x in range(0, len(in_str)):
        out_num = out_num * 10 + ord(in_str[x]) - ord('0')
    return out_num * multiplier

def aaa():
     return w1.get()

FIM=1

if FIM:
    master = Tk()
    master.geometry("+300+200") 
    master.title("SAME")

    
    titulo = Label(master, text="Dados do processo", padx=20, pady=20)
    titulo["font"] = ("Consolas", "20", "bold")
    titulo.grid(row=0, columnspan=3, column=0, sticky=W+E+N+S)

    group1 = LabelFrame(master, text="Nome", padx=20, pady=20)
    group1.grid(row=2, column=0)
    w1 = Entry(group1)
    w1.pack()



    group2 = LabelFrame(master, text="Temperatura inicial", padx=20, pady=20)
    group2.grid(row=2, column=1)
    w2 = Entry(group2)
    w2.pack()
 
    

    group3 = LabelFrame(master, text="Temperatura final", padx=20, pady=20)
    group3.grid(row=2, column=2)
    w3 = Entry(group3)
    w3.pack()
  




    mensagem = Label(master, text="", padx=20, pady=20)
    mensagem.grid(row=4, column=1, sticky=W+E+N+S)

    button = Button(master, text='Enviar', command= lambda: iniciar())
    button.grid(row=5, column=1, sticky=W+E+N+S)

    space = Label(master, text="", padx=5, pady=5)
    space.grid(row=6, column=1, sticky=W+E+N+S)



    
    def iniciar():
      nome=w1.get()
      ti= w2.get()
      tf= w3.get()  
    
      mensagem["text"] = "Feche a janela para continuar"
      FIM=0
      return nome,ti,tf
  

    mainloop()


print("\n\nIniciando\n\n")
printf(nome)
printf(ti)
printf(tf)




