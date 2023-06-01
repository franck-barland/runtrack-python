

from tkinter import *

gui = Tk()

# init. btn
btn = None

def entryOnClick():
    #Grid user interface size
    gui.geometry('200x100')
    #btn variable defined as global
    global btn
    #Change the word in the button
    btn = Button(gui, text = "Cliquez ici!", command = lambda: changeText('Welcome to WayToLearnX!'))
    #Var btn
    btn.pack()
    
    gui.mainloop()

def changeText(str):  
    btn['text'] = str

entryOnClick()




