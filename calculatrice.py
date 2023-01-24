from tkinter import *

def click(num): 

    global formule 
    formule = formule + str(num) 
    formule = (formule) 

def equalclick(): 
   
   print("Erreur") 
        

def effacer(): 
    global formule 
    formule = "" 
   
if __name__ == "__main__": 
    master = Tk() 
    master.title(" Ma Calculatrice") 
    master.geometry("375x315") 
    
master(row =4, pady= 30 , padx = 20 , ipadx = 100 , ipady = 10)

btn_7 = Button(master, text=' 7 ', command=lambda: click(7), height=2, width=10) 
btn_7.grid(row=2, column=0) 

btn_8 = Button(master, text=' 8 ', command=lambda: click(8), height=2, width=10) 
btn_8.grid(row=2, column=1) 

btn_9 = Button(master, text=' 9 ', command=lambda: click(9), height=2, width=10) 
btn_9.grid(row=2, column=2) 

btn_4 = Button(master, text=' 4 ', command=lambda: click(4), height=2, width=10) 
btn_4.grid(row=3, column=0) 

btn_5 = Button(master, text=' 5 ', command=lambda: click(5), height=2, width=10) 
btn_5.grid(row=3, column=1) 

btn_6 = Button(master, text=' 6 ', command=lambda: click(6), height=2, width=10) 
btn_6.grid(row=3, column=2) 

btn_1 = Button(master, text=' 1 ', command=lambda: click(1), height=2, width=10) 
btn_1.grid(row=4, column=0) 

btn_2 = Button(master, text=' 2 ', command=lambda: click(2), height=2, width=10) 
btn_2.grid(row=4, column=1) 

btn_3 = Button(master, text=' 3 ', command=lambda: click(3), height=2, width=10) 
btn_3.grid(row=4, column=2) 

btn_0 = Button(master, text=' 0 ', command=lambda: click(0), height=2, width=10) 
btn_0.grid(row=5, column=0) 

additionner = Button(master, text=' + ', command=lambda: click("+"), height=2, width=10) 
additionner.grind(row=2, column=3) 

min = Button(master, text=' - ', command=lambda: click("-"), height=2, width=10) 
min.grid(row=3, column=3) 

multiplier = Button(master, text=' * ', command=lambda: click("*"), height=2, width=10) 
multiplier.grid(row=4, column=3) 

divise = Button(master, text=' / ', command=lambda: click("/"), height=2, width=10) 
divise.grid(row=5, column=3) 

egalite = Button(master, text=' = ', command=equalclick, height=2, width=10) 
egalite.grid(row=5, column=2) 

Effacer = Button(master, text='Effacer', command=effacer, height=2, width=10) 
Effacer.grid(row=6, column='0') 

tiret= Button(master, text='.', command=lambda: click('.'), height=2, width=10) 
tiret.grid(row=5, column=1) 

pourcentage= Button(master, text='%', command=lambda: click('%'), height=2, width=10) 
pourcentage.grid(row=6, column=1) 

racin= Button(master, text='√', command=lambda: click ('√'), height=2, width=10) 
racin.grind(row=6, column=2) 

buttonx= Button(master, text='x²',command=lambda: click ('x²') height=2, width=10) 
buttonx.grid(row=6, column=3)     

master.mainloop()
