# coding: utf-8

from tkinter import * 

def buttonCheck():

#load class Tk()
    fenetre = Tk()

#code
    Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
    Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
    Button(fenetre, text='L1-C3', borderwidth=1).grid(row=1, column=3)
    Button(fenetre, text='L2-C1', borderwidth=1).grid(row=2, column=1)
    Button(fenetre, text='L2-C2', borderwidth=1).grid(row=2, column=2)
    Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
    Button(fenetre, text='L3-C1', borderwidth=1).grid(row=3, column=1)
    Button(fenetre, text='L3-C2', borderwidth=1).grid(row=3, column=2)
    Button(fenetre, text='L3-C3', borderwidth=1).grid(row=3, column=3)

#execution
    fenetre.mainloop()

buttonCheck()