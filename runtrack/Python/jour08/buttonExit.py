# coding: utf-8
 
from tkinter import * 

def buttonExit():
    #load class Tk()
    fenetre = Tk()

    # Exit button
    bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
    bouton.pack()

    fenetre.mainloop()

buttonExit()