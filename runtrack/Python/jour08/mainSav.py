from tkinter import *

# Var decl./typ./init
# load class Tk()
window = Tk()
# buttons
button1 = "L1C1"
button2 = "L1C2"
button3 = "L1C3"
button4 = "L2C1"
button5 = "L2C2"
button6 = "L2C3"
button7 = "L3C1"
button8 = "L3C2"
button9 = "L3C3"
# grid memory
# board=[[button1,button2,button3],[button4,button5,button6],[button7,button8,button9]]
# loop parameters (essai)
# args=["a","b","c","d","e","f","g","h","i"]


# draw initialization
def drawInit(a, b, c, d, e, f, g, h, i):
    Button(window, text=a, width=20, height=4, borderwidth=1).grid(row=1, column=1)
    Button(window, text=b, width=20, height=4, borderwidth=1).grid(row=1, column=2)
    Button(window, text=c, width=20, height=4, borderwidth=1).grid(row=1, column=3)
    Button(window, text=d, width=20, height=4, borderwidth=1).grid(row=2, column=1)
    Button(window, text=e, width=20, height=4, borderwidth=1).grid(row=2, column=2)
    Button(window, text=f, width=20, height=4, borderwidth=1).grid(row=2, column=3)
    Button(window, text=g, width=20, height=4, borderwidth=1).grid(row=3, column=1)
    Button(window, text=h, width=20, height=4, borderwidth=1).grid(row=3, column=2)
    Button(window, text=i, width=20, height=4, borderwidth=1).grid(row=3, column=3)


# main exec. method
def ia(button1, button2, button3, button4, button5, button6, button7, button8, button9):
    drawInit(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    # draw execution
    window.mainloop()


ia(button1, button2, button3, button4, button5, button6, button7, button8, button9)
