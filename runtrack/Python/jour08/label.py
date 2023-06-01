# coding: utf-8
 
from tkinter import * 

def label():
    #load class Tk()
    fenetre = Tk()

    # label
    label = Label(fenetre, text="Texte par défaut", bg="yellow")
    label.pack()    

    fenetre.mainloop()

label()