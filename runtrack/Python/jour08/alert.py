# coding: utf-8
# code HS

from tkinter import *

from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

def buttonCheck():
    #load class Tk()
    fenetre = Tk()

    # alert button
    Button(text='Action', command=callback).pack()
    
    #execution
    fenetre.mainloop()

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

''' askquestion()
    askokcancel()
    askyesno()
    askretrycancel()'''


buttonCheck()