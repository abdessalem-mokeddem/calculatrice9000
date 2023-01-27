from tkinter import *
 
formule = "" 
 
def click(num): 
 
    global formule 
    formule = formule + str(num) 
    equation.set(formule) 
 
def equalclick(): 
    try: 
        global formule 
 
        result = str(eval(formule)) 
        equation.set(result) 
        formule = result
 
    except: 
        equation.set(" ereur ") 
        formule = "" 
 
def effacer(): 
    global formule 
    formule = "" 
    equation.set("") 
 
if __name__ == "__main__": 
    window = Tk() 
    window.title(" Ma Calculatrice") 
    window.geometry("385x335") 
    equation = StringVar() 
    frame = Entry(window, textvariable=equation) 
    frame.grid(columnspan=4,  pady= 20 , padx = 20 , ipadx = 100 , ipady = 10)
    btn_7 = Button(window, text=' 7 ', command=lambda: click(7), height=2, width=10) 
    btn_7.grid(row=2, column=0) 
 
    btn_8 = Button(window, text=' 8 ', command=lambda: click(8), height=2, width=10) 
    btn_8.grid(row=2, column=1) 
 
    btn_9 = Button(window, text=' 9 ', command=lambda: click(9), height=2, width=10) 
    btn_9.grid(row=2, column=2) 
 
    btn_4 = Button(window, text=' 4 ', command=lambda: click(4), height=2, width=10) 
    btn_4.grid(row=3, column=0) 
 
    btn_5 = Button(window, text=' 5 ', command=lambda: click(5), height=2, width=10) 
    btn_5.grid(row=3, column=1) 
 
    btn_6 = Button(window, text=' 6 ', command=lambda: click(6), height=2, width=10) 
    btn_6.grid(row=3, column=2) 
 
    btn_1 = Button(window, text=' 1 ', command=lambda: click(1), height=2, width=10) 
    btn_1.grid(row=4, column=0) 
 
    btn_2 = Button(window, text=' 2 ', command=lambda: click(2), height=2, width=10) 
    btn_2.grid(row=4, column=1) 
 
    btn_3 = Button(window, text=' 3 ', command=lambda: click(3), height=2, width=10) 
    btn_3.grid(row=4, column=2) 
 
    btn_0 = Button(window, text=' 0 ', command=lambda: click(0), height=2, width=10) 
    btn_0.grid(row=5, column=0) 
 
    additionner = Button(window, text=' + ', command=lambda: click("+"), height=2, width=10) 
    additionner.grid(row=2, column=3) 
 
    minimum = Button(window, text=' - ', command=lambda: click("-"), height=2, width=10) 
    minimum.grid(row=3, column=3) 
 
    multiplier = Button(window, text=' * ', command=lambda: click("*"), height=2, width=10) 
    multiplier.grid(row=4, column=3) 
 
    divise = Button(window, text=' / ', command=lambda: click("/"), height=2, width=10) 
    divise.grid(row=5, column=3) 
 
    egale = Button(window, text=' = ', command=equalclick, height=2, width=10) 
    egale.grid(row=6, column=2) 
 
    effacer = Button(window, text='effacer', command=effacer, height=2, width=10) 
    effacer.grid(row=5, column='0') 
 
    Decimal= Button(window, text='.', command=lambda: click('.'), height=2, width=10) 
    Decimal.grid(row=5, column=1) 
    
    pourcent= Button(window, text='%', command=lambda: click('%'), height=2, width=10) 
    pourcent.grid(row=6, column=1) 
    
    racine= Button(window, text='√',  height=2, width=10) 
    racine.grid(row=5, column=2) 
    
    suppr= Button(window, text='C',  height=2, width=10) 
    suppr.grid(row=5, column=3)     
    
    window.mainloop()

   