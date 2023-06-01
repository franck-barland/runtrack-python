# coding: utf-8

from tkinter import * 

def buttonCheck():
    #load class Tk()
    fenetre = Tk()

    # checkbutton
    bouton = Checkbutton(fenetre, text="Nouveau?")
    bouton.pack()
     
    #execution
    fenetre.mainloop()

buttonCheck()