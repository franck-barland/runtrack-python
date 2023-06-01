# coding: utf-8
 
from tkinter import * 

def scale():
    #load class Tk()
    fenetre = Tk()

    value = DoubleVar()
    scale = Scale(fenetre, variable=value)
    scale.pack()

    fenetre.mainloop()

scale()