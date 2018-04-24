#adicionar inst.close() para fechar a comunicação visa

from datetime import datetime
import time


from tkinter import *


def printf (text):
    print(text,end="")


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

    space = Label(master, text="", padx=5, pady=5)
    space.grid(row=3, column=1, sticky=W+E+N+S)
   

    group4 = Label(master, text="Escolha a medida que deseja:")
    group4.grid(row=4, column=1, sticky=W)

    Ohm = IntVar()
    resistencia = Checkbutton(master, text="Resistência", variable=Ohm)
    resistencia.grid(row=5, column=1, sticky=W)
 
    Vdc = IntVar()
    tensao = Checkbutton(master, text="Tensão", variable=Vdc)
    tensao.grid(row=6, column=1, sticky=W)


    mensagem = Label(master, text="")
    mensagem.grid(row=7, column=1, sticky=W+E+N+S)


    button = Button(master, text='Enviar', command= lambda: iniciar())
    button.grid(row=8, column=1, sticky=W+E+N+S)

    space1 = Label(master, text="", padx=5, pady=5)
    space1.grid(row=9, column=1, sticky=W+E+N+S)

    dicas = Label(master, text="Dicas: \n No nome use apenas letras, números e traços.\n Use apenas números inteiros.\n Selecione apenas uma medida.\n", padx=5, pady=5)
    dicas.grid(row=10, column=0, columnspan=3, sticky=W+E+N+S)



    
    def iniciar():
        if ValueError:
            mensagem["text"] = "Erro encontrado. Verifique os dados \n e as conexões com os equipamentos"

        global nome
        global ti
        global tf
        global ohm
        global vdc
        
        nome=   w1.get()
        ti= int(w2.get())
        tf= int(w3.get())
        ohm=Ohm.get()
        vdc=Vdc.get()
        
        if(vdc and ohm): mensagem["text"] = "Escolha apenas uma medida"
        elif(vdc==0 and ohm==0): mensagem["text"] = "Escolha pelo menos uma medida"
        else: mensagem["text"] = "Comunicações estabelecidas. Feche a janela para continuar"
        FIM=0
  

    mainloop()


print("\n\nIniciando\n\n")


while True:
  
    master = Tk()
    master.geometry("+300+200") 
    master.title("SAME")

    
    titulo = Label(master, text="Dados do processo", padx=30, pady=30)
    titulo["font"] = ("Consolas", "20", "bold")
    titulo.grid(row=0, columnspan=3, column=0, sticky=W+E+N+S)

    group1 = LabelFrame(master, text="Temperatura inicial", padx=30, pady=30)
    group1.grid(row=2, column=0)
    w1 = Label(group1, text="Alo", padx=20, pady=20)
    w1.pack()


    group2 = LabelFrame(master, text="Temperatura final", padx=30, pady=30)
    group2.grid(row=2, column=1)
    w2 = Label(group2, text="Alo", padx=20, pady=20)
    w2.pack()
 

    group3 = LabelFrame(master, text="Degrau", padx=30, pady=30)
    group3.grid(row=2, column=2)
    w3 = Label(group3, text="Alo", padx=20, pady=20)
    w3.pack()

    group4 = LabelFrame(master, text="Temperatura atual", padx=30, pady=30)
    group4.grid(row=3, column=0)
    w4 = Label(group4, text="Alo", padx=20, pady=20)
    w4.pack()


    group5 = LabelFrame(master, text="Resistência atual", padx=30, pady=30)
    group5.grid(row=3, column=1)
    w5 = Label(group5, text="Alo", padx=20, pady=20)
    w5.pack()
 

    group6 = LabelFrame(master, text="???", padx=30, pady=30)
    group6.grid(row=3, column=2)
    w6 = Label(group6, text="Alo", padx=20, pady=20)
    w6.pack()


    mainloop()
   
    break







