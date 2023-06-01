# coding: utf-8

from tkinter import * 

def buttonCheck():
    #load class Tk()
    fenetre = Tk()

    # canvas 
    # canvas.coords(element, x0, y0, x1, y1)
    canvas = Canvas(fenetre, width=150, height=120, background='yellow')
    ligne1 = canvas.create_line(75, 0, 75, 120)
    ligne2 = canvas.create_line(0, 60, 150, 60)
    txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
    canvas.pack()
     
    canvas.delete(ligne1)
    ''' create_arc()        :  arc de cercle
        create_bitmap()     :  bitmap
        create_image()      :  image
        create_line()       :  ligne
        create_oval()       :  ovale
        create_polygon()    :  polygone
        create_rectangle()  :  rectangle 
        create_text()       :  texte
        create_window()     :  fenetre'''
    
    print(dir(Canvas()))

    #execution
    fenetre.mainloop()

buttonCheck()