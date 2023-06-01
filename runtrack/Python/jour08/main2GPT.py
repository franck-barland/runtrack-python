from tkinter import *

# Var decl./typ./init
# load class Tk()
window = Tk()
# buttons (Format buttonX = [localisationInGrid,content])
button1 = ["L1C1","X"]
button2 = ["L1C2",""]
button3 = ["L1C3",""]
button4 = ["L2C1",""]
button5 = ["L2C2",""]
button6 = ["L2C3",""]
button7 = ["L3C1",""]
button8 = ["L3C2",""]
button9 = ["L3C3",""]

# grid memory (2D table) for algorythmy                           
gridGame=[[button1,button2,button3],[button4,button5,button6],[button7,button8,button9]]

# loop parameters (essai)
# args=["a","b","c","d","e","f","g","h","i"]

# cf labelFrame.py
def formatButton(text, button):
    l = LabelFrame(button, text=text, padx=20, pady=20)
    l.pack(fill="both", expand="yes")
    Label(l, text="A l'intérieure de la frame").pack()


# draw initialization (a-> button1, b-> button2...) (factorisation by ChatGPT)
def drawInit(buttons_text):
    for row in range(3):
        for column in range(3):
            button_text = buttons_text[row * 3 + column]
            button_obj = Button(window, text=button_text, width=20, height=4, borderwidth=1)
            button_obj.grid(row=row+1, column=column+1)
            formatButton(button_text, button_obj)

#Main method
def ia(button1, button2, button3, button4, button5, button6, button7, button8, button9):
    #factorisation by chatGPT
    buttons_text = (button1, button2, button3, button4, button5, button6, button7, button8, button9)
    drawInit(buttons_text)
    # draw execution
    window.mainloop()

ia(button1, button2, button3, button4, button5, button6, button7, button8, button9)