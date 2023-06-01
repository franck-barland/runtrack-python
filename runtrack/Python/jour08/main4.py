import tkinter as tk

# Var decl./typ./init
# load class Tk()
window = tk.Tk()
row_idx = 0
# buttons
buttons = [{"title": "L1C1", "content": ""},           {"title": "L1C2", "content": ""},           {"title": "L1C3", "content": ""},           {"title": "L2C1", "content": ""},           {"title": "L2C2", "content": ""},           {"title": "L2C3", "content": ""},           {"title": "L3C1", "content": ""},           {"title": "L3C2", "content": ""},           {"title": "L3C3", "content": ""}]

# grid memory (2D table)
grid_game = [[buttons[0], buttons[1], buttons[2]],
             [buttons[3], buttons[4], buttons[5]],
             [buttons[6], buttons[7], buttons[8]]]

# draw initialization
def drawInit(grid_game):
    global row_idx
    # destroy existing widgets
    for row in grid_game:
        for btn_data in row:
            if "obj" in btn_data:
                btn_data["obj"].destroy()
                del btn_data["obj"]
    col_idx = 1
    row_idx = 1  # initialize row_idx to 1
    for row in grid_game:
        for btn_data in row:
            title = btn_data["title"]
            content = btn_data["content"]
            btn_data["obj"] = tk.Button(window, text=content, width=20, height=4, borderwidth=1, command=lambda b=btn_data: update_button(b))
            btn_data["obj"].grid(row=row_idx, column=col_idx)
            formatButton(btn_data["obj"], title)
            col_idx += 1
        row_idx += 1  # increment row_idx in outer loop
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
def update_button(btn_data):
    # do something with the button when it's clicked
    print("Button clicked:", btn_data["title"])

ia()
