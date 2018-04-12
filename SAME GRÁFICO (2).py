from datetime import datetime
import time
import visa
import minimalmodbus
from tkinter import *

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
    



    group4 = LabelFrame(master, text="Degrau", padx=20, pady=20)
    group4.grid(row=3, column=0)
    w4 = Entry(group4)
    w4.pack()


    
    

    group5 = LabelFrame(master, text="Nº de ciclos", padx=20, pady=20)
    group5.grid(row=3, column=1)
    w5 = Entry(group5)
    w5.pack()
    
    
    group6 = LabelFrame(master, text="Tempo de estabilização", padx=20, pady=20)
    group6.grid(row=3, column=2)
    w6 = Entry(group6)
    w6.pack()




    mensagem = Label(master, text="", padx=20, pady=20)
    mensagem.grid(row=4, column=1, sticky=W+E+N+S)

    button = Button(master, text='Enviar', command= lambda: iniciar())
    button.grid(row=5, column=1, sticky=W+E+N+S)

    space = Label(master, text="", padx=5, pady=5)
    space.grid(row=6, column=1, sticky=W+E+N+S)

    def iniciar():

      nome=  w1.get()
      print(nome)
      ti=    w2.get()
      print(ti)
      tf=    w3.get() 
      degrau=w4.get() 
      ciclos= w5.get()
      estab=   w6.get()



      #iniciando comunicação com o multimetro
      rm = visa.ResourceManager()                
      dmm = rm.open_resource('GPIB0::22::INSTR') 
      dmm.write("END ALWAYS")

      #iniciando comunicação com o controlador
      c704 = minimalmodbus.Instrument('COM4', 1)
      c704.serial.baudrate = 57600    
    
      mensagem["text"] = "Feche a janela para continuar"
      FIM=0
  

    mainloop()


print("\n\nIniciando\n\n")

#a variavel CICLO indica o ciclo atual
CICLO=1



ti=to_int(ti)
tf=to_int(tf)
degrau=to_int(degrau)
ciclos=to_int(ciclos)
estab=to_int(estab)
Testabilizacao = estab*60
tf = tf-degrau 


while(CICLO <= ciclos):        

 

 pasta = '/Medidas/'  
 ext = '.txt'
 nomearq = nome + '(' + str(CICLO) + ')'
 arquivo = pasta + nomearq + ext
 arquivo2 = pasta + nomearq + "_com_filtro" + ext

#inicia os arquivos de texto
 arq = open(arquivo, 'w')   
 arq2 = open(arquivo2, 'w')
 
 arq.write('Hora          T(C)          R(Ohms)\n')
 arq2.write('Hora          T(C)          R(Ohms)\n')

 setpoint = ti    #primeiro setpoint igual a temperatura inicial     
 END=0            #variavel que indica o fim de um ciclo
 tolerancia = 1   #define o erro maximo entre o setpoint e o leitura de T (+ ou -)
 Tespera=10        #tempo entre rotinas (Tespera + 1s do processo)
 contagem=0       #indica se o programa esta no periodo de estabilizacao
 timer = 0        #cronometro da estabilizacao

 while (END != 1):

    #comando para medir RESISTENCIA no 3458A
    resistencia = dmm.query("OHM")
    #comando para ler pv do c704
    pv = c704.read_register(0, 1)                   

    today = datetime.now()
    if (today.second <10):
        segundos =  '0' + str(today.second)
    elif (today.second > 9):
        segundos = str(today.second) 
    if (today.minute <10):
        minutos = '0' + str(today.minute) 
    elif (today.minute > 9):
        minutos = str(today.minute)
    if (today.hour <10):
        horas = '0' + str(today.hour)  
    elif (today.hour > 9):
        horas = str(today.hour)  
    
    today = datetime.now()
    hora = horas + ':' + minutos + ':' + segundos 

    PV=str(pv)
    arq.write(hora)
    arq.write('    ')
    arq.write(PV)
    arq.write('    ')
    arq.write(resistencia)

    printf(hora)
    printf("  SETPOINT:")
    printf(setpoint)
    printf("  SP-PV:")
    x=abs(setpoint-pv)
    x=round(x,2)
    printf(x)
    printf("  PV:")
    printf(pv)
    printf("  RESISTENCIA:")
    print(resistencia)

	
    
    if( (abs(setpoint-pv) <= 1) and contagem==0 ):
      contagem = 1
      timer = -Tespera
      print("Contando o tempo de estabilizacao.\n")
      

    if(contagem):
      timer=timer+Tespera
      
      PV=str(pv)
      arq2.write(hora)
      arq2.write('    ')
      arq2.write(PV)
      arq2.write('    ')
      arq2.write(resistencia)
      
    
    if(timer==Testabilizacao and (setpoint-degrau) != tf-degrau ):
      print("Tempo de estabilizacao concluido. Atualizando SETPOINT.\n")
      setpoint = setpoint - degrau
      timer = 0
      contagem=0

    if( setpoint-degrau == tf-degrau):
      END=1


    if(END!=1):
      c704.write_register(1,setpoint,1)
      time.sleep(Tespera)

    else:
      arq.close()
      arq2.close()
      CICLO=CICLO+1
      print("Ciclo finalizado.\n")






    

print ('Arquivos criado em: /Medidas')
print('Para fechar tecle Enter.')
a = input()
