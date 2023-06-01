import tkinter as tk

# Var decl./typ./init
# load class Tk()
window = tk.Tk()
row_idx = 0
# buttons
buttons = [["L1C1", ""], ["L1C2", ""], ["L1C3", ""],
           ["L2C1", ""], ["L2C2", ""], ["L2C3", ""],
           ["L3C1", ""], ["L3C2", ""], ["L3C3", ""]]

# grid memory (2D table)
grid_game = [[buttons[0], buttons[1], buttons[2]],
             [buttons[3], buttons[4], buttons[5]],
             [buttons[6], buttons[7], buttons[8]]]

# draw initialization
def drawInit(grid_game):
    global row_idx
    col_idx = 1
    for row in grid_game:
        for button in row:
            title = button[0]
            content = button[1]
            button[1] = tk.Button(window, text=content, width=20, height=4, borderwidth=1, command=lambda b=button[1]: update_button(b))
            button[1].grid(row=row_idx, column=col_idx)
            formatButton(button[1], title)
            col_idx += 1
        row_idx += 1
        col_idx = 1

# format button
def formatButton(button, title):
    l = tk.LabelFrame(button, text=title, padx=40, pady=20)
    l.pack(fill="both", expand="yes")
    tk.Label(l, text="").pack()

# main method
def ia():
    drawInit(grid_game)
    # draw execution
    window.mainloop()

# necessité de créer cette méthode pour drawInit(grid_game)
def update_button(b):
    # do something with the button when it's clicked
    print("Button clicked:", b)

ia()
