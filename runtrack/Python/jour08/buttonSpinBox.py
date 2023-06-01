# coding: utf-8
 
from tkinter import * 

def buttonSpinBox():
    #load class Tk()
    fenetre = Tk()

    s = Spinbox(fenetre, from_=0, to=10)
    s.pack()

    fenetre.mainloop()

buttonSpinBox()