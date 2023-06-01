# coding: utf-8
# code HS

from tkinter import * 

def buttonRadio():
    #load class Tk()
    fenetre = Tk()

    # radiobutton
    value = StringVar() 
    bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
    bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
    bouton3 = Radiobutton(fenetre, text="Peut être", variable=value, value=3)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()
     
    #execution
    fenetre.mainloop()

buttonRadio()